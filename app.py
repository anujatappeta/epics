import streamlit as st
import tensorflow as tf
import numpy as np
from tensorflow.keras import layers, models
from tensorflow.keras.applications import EfficientNetB3
from PIL import Image
import os
import gdown
from solutions import get_solution

# ---------------- CONFIG ----------------
IMG_SIZE = (300, 300)
CLASS_NAMES = [
    'Anthracnose', 'Bacterial Canker', 'Cutting Weevil',
    'Die Back', 'Gall Midge', 'Healthy', 'Powdery Mildew', 'Sooty Mould'
]
MODEL_PATH = "best_model_weights.h5"
DRIVE_FILE_ID = "10R4Z7M95v1lXHu71C8j4Rg7QZUNy1TwV"

st.set_page_config(page_title="🌿 Mango Doctor", page_icon="🍃", layout="wide")

# ---------------- DOWNLOAD MODEL IF MISSING ----------------
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
    x = layers.Lambda(lambda t: tf.keras.applications.efficientnet.preprocess_input(t))(x)

    base_model = EfficientNetB3(include_top=False, weights=None, input_tensor=x)
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
    html, body, [class*="css"] {
        font-family: 'Poppins', sans-serif;
        background: linear-gradient(160deg, #e8f5e9 0%, #e3f2fd 100%);
    }
    .main-container {
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: center;
        min-height: 90vh;
        text-align: center;
        padding: 1rem;
    }
    .title {
        font-size: 2.5rem;
        font-weight: 700;
        color: #2e7d32;
        margin-bottom: 0.5rem;
    }
    .subtitle {
        font-size: 1rem;
        color: #444;
        margin-bottom: 2rem;
    }
    .card {
        background: white;
        padding: 2rem;
        border-radius: 20px;
        box-shadow: 0px 4px 12px rgba(0,0,0,0.1);
        max-width: 500px;
        width: 95%;
        margin: auto;
    }
    .stButton>button {
        background-color: #2e7d32 !important;
        color: white !important;
        border: none !important;
        border-radius: 10px !important;
        padding: 0.6rem 1.5rem !important;
        font-weight: 600 !important;
        transition: all 0.2s ease-in-out;
    }
    .stButton>button:hover {
        transform: scale(1.05);
        background-color: #43a047 !important;
    }
    img {
        border-radius: 12px;
        margin-top: 10px;
    }
    @media (max-width: 768px) {
        .title { font-size: 2rem; }
        .card { padding: 1.5rem; width: 90%; }
    }
    </style>
""", unsafe_allow_html=True)


# ---------------- PAGE: LANGUAGE ----------------
if st.session_state.page == "language":
    st.markdown("<div class='main-container'><div class='card'>", unsafe_allow_html=True)
    st.markdown("<h1 class='title'>🌍 Choose Your Language</h1>", unsafe_allow_html=True)
    lang = st.radio("", ["English", "हिन्दी", "తెలుగు"], horizontal=True)

    if lang == "English":
        st.session_state.lang = "en"
    elif lang == "हिन्दी":
        st.session_state.lang = "hi"
    else:
        st.session_state.lang = "te"

    if st.button("➡️ Continue"):
        st.session_state.page = "upload"
        st.rerun()
    st.markdown("</div></div>", unsafe_allow_html=True)

# ---------------- PAGE: UPLOAD ----------------
elif st.session_state.page == "upload":
    st.markdown("<div class='main-container'><div class='card'>", unsafe_allow_html=True)
    st.markdown("<h1 class='title'>🍃 Mango Leaf Detector</h1>", unsafe_allow_html=True)
    st.markdown("<p class='subtitle'>Upload or capture a mango leaf image below</p>", unsafe_allow_html=True)

    uploaded_file = st.file_uploader("📸 Upload Image", type=["jpg", "jpeg", "png"])
    capture_image = st.camera_input("Or capture using camera")

    image_source = uploaded_file or capture_image

    if image_source:
        image = Image.open(image_source).convert("RGB")
        st.image(image, caption="Uploaded Image", use_container_width=True)

        img = image.resize(IMG_SIZE)
        img_array = np.expand_dims(np.array(img), axis=0)
        img_array = tf.keras.applications.efficientnet.preprocess_input(img_array)

        with st.spinner("🧠 Analyzing..."):
            model = load_model()
            preds = model.predict(img_array)[0]
            pred_idx = np.argmax(preds)
            pred_class = CLASS_NAMES[pred_idx]
            confidence = preds[pred_idx] * 100

        st.session_state.pred_class = pred_class
        st.session_state.confidence = confidence
        st.success(f"✅ **{pred_class}** ({confidence:.2f}% confidence)")

        if st.button("💊 Show Organic Solution"):
            st.session_state.page = "solution"
            st.rerun()
    else:
        st.info("Please upload or capture a leaf image to continue.")

    st.markdown("</div></div>", unsafe_allow_html=True)

# ---------------- PAGE: SOLUTION ----------------
elif st.session_state.page == "solution":
    st.markdown("<div class='main-container'><div class='card'>", unsafe_allow_html=True)
    st.markdown("<h1 class='title'>💊 Organic Solution</h1>", unsafe_allow_html=True)

    if "pred_class" not in st.session_state:
        st.warning("⚠️ Upload an image first.")
    else:
        disease = st.session_state.pred_class
        lang = st.session_state.get("lang", "en")
        sol = get_solution(disease, lang)
        st.markdown(f"### 🌱 {sol['name']}")
        st.markdown(f"<div style='text-align:left;'>{sol['description']}</div>", unsafe_allow_html=True)

    if st.button("🔁 Try Another Image"):
        st.session_state.page = "upload"
        st.rerun()
    st.markdown("</div></div>", unsafe_allow_html=True)
