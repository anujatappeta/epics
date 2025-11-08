import streamlit as st
import tensorflow as tf
import numpy as np
from tensorflow.keras import layers, models
from tensorflow.keras.applications import EfficientNetB3, efficientnet
from PIL import Image
import os
import gdown
from solutions import get_solution  # keep your solutions.py

# ---------------- CONFIG ----------------
IMG_SIZE = (300, 300)
CLASS_NAMES = [
    'Anthracnose', 'Bacterial Canker', 'Cutting Weevil',
    'Die Back', 'Gall Midge', 'Healthy', 'Powdery Mildew', 'Sooty Mould'
]
MODEL_PATH = "best_model_weights.h5"
DRIVE_FILE_ID = "10R4Z7M95v1lXHu71C8j4Rg7QZUNy1TwV"

st.set_page_config(page_title="🌿 Mango Doctor", page_icon="🍃", layout="wide")

# ---------------- DOWNLOAD MODEL ----------------
@st.cache_resource
def download_model():
    if not os.path.exists(MODEL_PATH):
        st.info("📥 Downloading model weights... please wait.")
        url = f"https://drive.google.com/uc?id={DRIVE_FILE_ID}"
        gdown.download(url, MODEL_PATH, quiet=False)

# ---------------- LOAD MODEL ----------------
@st.cache_resource
def load_model():
    download_model()

    data_augmentation = tf.keras.Sequential([
        layers.RandomFlip("horizontal"),
        layers.RandomRotation(0.06),
        layers.RandomZoom(0.06),
        layers.RandomTranslation(0.03, 0.03),
        layers.RandomContrast(0.06),
    ])

    inputs = layers.Input(shape=IMG_SIZE + (3,))
    x = data_augmentation(inputs)
    x = layers.Lambda(lambda t: efficientnet.preprocess_input(t))(x)

    base_model = EfficientNetB3(include_top=False, weights='imagenet', input_tensor=x)
    base_model.trainable = False

    x = layers.GlobalAveragePooling2D()(base_model.output)
    x = layers.BatchNormalization()(x)
    x = layers.Dropout(0.4)(x)
    x = layers.Dense(512, activation="swish")(x)
    x = layers.BatchNormalization()(x)
    x = layers.Dropout(0.2)(x)
    outputs = layers.Dense(len(CLASS_NAMES), activation="softmax")(x)

    model = models.Model(inputs, outputs)
    model.load_weights(MODEL_PATH)
    return model


# ---------------- STATE ----------------
if "page" not in st.session_state:
    st.session_state.page = "language"

# ---------------- STYLE ----------------
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@400;600;700&display=swap');

    .stApp {
        background: linear-gradient(135deg, #2e7d32 0%, #c5e384 50%, #fff3b0 100%);
        font-family: 'Poppins', sans-serif;
        color: #1b4332;
        overflow: hidden;
    }

    /* 🌿 Fullscreen Center */
    .main-container {
        position: fixed;
        top: 50%;
        left: 50%;
        transform: translate(-50%, -50%);
        text-align: center;
        animation: fadeIn 1.2s ease-in-out;
        width: 100%;
    }

    @keyframes fadeIn {
        from { opacity: 0; transform: translate(-50%, -45%); }
        to { opacity: 1; transform: translate(-50%, -50%); }
    }

    h1.title {
        font-size: 3rem;
        font-weight: 700;
        color: #1a4301;
        text-shadow: 1px 1px 6px rgba(255,255,255,0.3);
        margin-bottom: 1rem;
    }

    p.subtitle {
        font-size: 1.2rem;
        color: #2e4600;
        margin-bottom: 1.5rem;
    }

    /* 🌿 Radio Buttons */
    div[data-testid="stRadio"] label {
        font-size: 1.2rem !important;
        margin-right: 1rem;
        color: #2b580c !important;
    }

    /* 🌿 Animated Button */
    .stButton>button {
        background: linear-gradient(90deg, #3c9a40, #7bc950);
        color: white !important;
        border: none !important;
        border-radius: 14px !important;
        padding: 0.9rem 2.5rem !important;
        font-weight: 600 !important;
        font-size: 1.1rem !important;
        box-shadow: 0px 4px 15px rgba(60,154,64,0.4);
        transition: all 0.4s ease;
        animation: glow 2.5s infinite alternate;
    }

    @keyframes glow {
        from { box-shadow: 0px 0px 10px rgba(124,252,0,0.4); }
        to { box-shadow: 0px 0px 20px rgba(173,255,47,0.7); }
    }

    .stButton>button:hover {
        transform: scale(1.07);
        background: linear-gradient(90deg, #52b788, #d4d700);
    }

    img {
        border-radius: 15px;
        margin-top: 10px;
        box-shadow: 0px 3px 10px rgba(0,0,0,0.15);
    }

    .confidence {
        font-weight: 600;
        color: #1a4301;
        margin-top: 1rem;
        font-size: 1.1rem;
    }

    @media (max-width: 768px) {
        h1.title { font-size: 2.2rem; }
        p.subtitle { font-size: 1rem; }
    }
    </style>
""", unsafe_allow_html=True)


# ---------------- PAGE: LANGUAGE ----------------
if st.session_state.page == "language":
    st.markdown("<div class='main-container'>", unsafe_allow_html=True)
    st.markdown("<h1 class='title'>🌍 Choose Your Language</h1>", unsafe_allow_html=True)
    lang = st.radio("", ["English", "हिन्दी", "తెలుగు"], horizontal=True, label_visibility="collapsed")

    if lang == "English":
        st.session_state.lang = "en"
    elif lang == "हिन्दी":
        st.session_state.lang = "hi"
    else:
        st.session_state.lang = "te"

    if st.button("➡ Continue"):
        st.session_state.page = "upload"
        st.rerun()
    st.markdown("</div>", unsafe_allow_html=True)


# ---------------- PAGE: UPLOAD ----------------
elif st.session_state.page == "upload":
    st.markdown("<div class='main-container'>", unsafe_allow_html=True)
    st.markdown("<h1 class='title'>🍃 Mango Leaf Detector</h1>", unsafe_allow_html=True)
    st.markdown("<p class='subtitle'>Upload or capture a mango leaf image below</p>", unsafe_allow_html=True)

    uploaded_file = st.file_uploader("📂 Upload Image", type=["jpg", "jpeg", "png"])
    capture_image = st.camera_input("📸 Capture using Camera")

    image_source = uploaded_file or capture_image

    if image_source:
        image = Image.open(image_source).convert("RGB")
        st.image(image, caption="Uploaded Image", use_container_width=True)

        img = image.resize(IMG_SIZE)
        img_array = np.expand_dims(np.array(img), axis=0)
        img_array = efficientnet.preprocess_input(img_array)

        with st.spinner("🧠 Analyzing leaf..."):
            model = load_model()
            preds = model.predict(img_array)[0]
            pred_idx = np.argmax(preds)
            pred_class = CLASS_NAMES[pred_idx]
            confidence = preds[pred_idx] * 100

        st.session_state.pred_class = pred_class
        st.session_state.confidence = confidence
        st.markdown(f"<div class='confidence'>✅ *{pred_class}* ({confidence:.2f}% confidence)</div>", unsafe_allow_html=True)

        if st.button("💊 Show Organic Solution"):
            st.session_state.page = "solution"
            st.rerun()
    else:
        st.info("Please upload or capture a leaf image to continue.")

    st.markdown("</div>", unsafe_allow_html=True)


# ---------------- PAGE: SOLUTION ----------------
elif st.session_state.page == "solution":
    st.markdown("<div class='main-container'>", unsafe_allow_html=True)
    st.markdown("<h1 class='title'>💊 Organic Solution</h1>", unsafe_allow_html=True)

    if "pred_class" not in st.session_state:
        st.warning("⚠ Upload an image first.")
    else:
        disease = st.session_state.pred_class
        lang = st.session_state.get("lang", "en")
        sol = get_solution(disease, lang)
        st.markdown(f"### 🌱 {sol['name']}")
        st.markdown(f"<div style='text-align:left;color:#1a4301;'>{sol['description']}</div>", unsafe_allow_html=True)

    if st.button("🔁 Try Another Image"):
        st.session_state.page = "upload"
        st.rerun()
    st.markdown("</div>", unsafe_allow_html=True)
