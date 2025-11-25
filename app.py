import streamlit as st
import tensorflow as tf
import numpy as np
from tensorflow.keras import layers, models
from tensorflow.keras.applications import EfficientNetB3, efficientnet
from PIL import Image
import os
import gdown
import cv2
from solutions import get_solution

# ---------------- CONFIG ----------------
IMG_SIZE = (300, 300)
CLASS_NAMES = [
    'Anthracnose', 'Bacterial Canker', 'Cutting Weevil',
    'Die Back', 'Gall Midge', 'Healthy', 'Powdery Mildew', 'Sooty Mould'
]

MODEL_PATH = "best_model_weights.h5"
DRIVE_FILE_ID = "10R4Z7M95v1lXHu71C8j4Rg7QZUNy1TwV"
THRESHOLD = 0.60  # Confidence threshold


# ---------------------------------------------------------------
# 🔥 IMPROVED LEAF DETECTOR (supports dried, yellow, brown leaves)
# ---------------------------------------------------------------
def is_leaf(img_pil):

    img = img_pil.resize((224, 224))
    arr = np.array(img)
    r, g, b = arr[:,:,0], arr[:,:,1], arr[:,:,2]

    # --- Green Leaf ---
    green_mask = (g > r) & (g > b) & (g > 50)

    # --- Yellow Leaf ---
    yellow_mask = (r > 120) & (g > 120) & (b < 100)

    # --- Brown Leaf ---
    brown_mask = (r > 90) & (g > 50) & (b < 60)

    color_ratio = np.sum(green_mask | yellow_mask | brown_mask) / (224*224)

    # --- Shape Check (Mango leaf = long shape) ---
    h, w = img.size
    aspect_ratio = max(h, w) / min(h, w)

    # --- Edge detection (dried leaves show strong edges) ---
    gray = cv2.cvtColor(arr, cv2.COLOR_RGB2GRAY)
    edges = cv2.Canny(gray, 40, 120)
    edge_ratio = np.sum(edges > 0) / (224*224)

    # ---------------- DECISION ----------------
    if color_ratio > 0.06:
        return True
    if aspect_ratio > 1.8:
        return True
    if edge_ratio > 0.06:
        return True

    return False


# ---------------- MODEL DOWNLOAD ----------------
@st.cache_resource
def download_model():
    if not os.path.exists(MODEL_PATH):
        st.info("📥 Downloading model weights...")
        gdown.download(
            f"https://drive.google.com/uc?id={DRIVE_FILE_ID}",
            MODEL_PATH,
            quiet=False
        )


# ---------------- MODEL LOAD ----------------
@st.cache_resource
def load_model():
    download_model()

    data_aug = tf.keras.Sequential([
        layers.RandomFlip("horizontal"),
        layers.RandomRotation(0.06),
        layers.RandomZoom(0.06),
        layers.RandomTranslation(0.03, 0.03),
        layers.RandomContrast(0.06)
    ])

    inputs = layers.Input(shape=IMG_SIZE + (3,))
    x = data_aug(inputs)
    x = layers.Lambda(lambda t: efficientnet.preprocess_input(t))(x)

    base = EfficientNetB3(include_top=False, weights="imagenet", input_tensor=x)
    base.trainable = False

    x = layers.GlobalAveragePooling2D()(base.output)
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

if "model" not in st.session_state:
    with st.spinner("Loading model..."):
        st.session_state.model = load_model()


# ---------------- LANGUAGE TEXT ----------------
LOCALIZED_HEADERS = {
    "en": {
        "upload_title": "Mango Leaf Detector",
        "upload_subtitle": "Upload or capture a mango leaf image below",
        "upload_file": "📂 Upload Image",
        "capture_camera": "📸 Capture with Camera",
        "info_upload": "Please upload or capture a leaf image.",
        "solution_title": "Organic Solution",
        "solution_button": "🌱 Show Organic Solution",
        "solution_header": "Solution:",
        "ingredients_header": "Ingredients / Application:",
        "back_language": "↩ Language",
        "back_upload": "↩ Back",
        "try_again": "🔁 Try Another Image",
        "analyzing": "🧠 Analyzing leaf...",
        "success": "✅ Prediction:"
    }
}


# ---------------- PAGES ----------------
def language_page():
    st.title("🌍 Choose Your Language")
    col1, col2, col3 = st.columns(3)
    if col1.button("English"): st.session_state.page="upload"; st.session_state.lang="en"
    if col2.button("हिन्दी"): st.session_state.page="upload"; st.session_state.lang="hi"
    if col3.button("తెలుగు"): st.session_state.page="upload"; st.session_state.lang="te"


def upload_page():
    headers = LOCALIZED_HEADERS["en"]

    st.title("🍃 " + headers["upload_title"])
    st.write(headers["upload_subtitle"])

    col1, col2 = st.columns(2)
    uploaded = col1.file_uploader(headers["upload_file"], type=["jpg","png","jpeg"])
    camera = col2.camera_input(headers["capture_camera"])

    img_source = uploaded or camera
    if not img_source:
        st.info(headers["info_upload"])
        return

    img = Image.open(img_source).convert("RGB")
    st.image(img, use_container_width=True)

    # ---- Leaf Validation ----
    with st.spinner("🌿 Checking leaf validity..."):
        if not is_leaf(img):
            st.error("❌ Please upload a clear mango leaf image.")
            return

    # ---- Prediction ----
    with st.spinner(headers["analyzing"]):
        arr = np.expand_dims(np.array(img.resize(IMG_SIZE)), axis=0)
        arr = efficientnet.preprocess_input(arr)
        preds = st.session_state.model.predict(arr)[0]

    pred_idx = np.argmax(preds)
    conf = preds[pred_idx]

    # ---- Low Confidence ----
    if conf < THRESHOLD:
        st.error("❌ Please upload a clear mango leaf image.")
        return

    pred_class = CLASS_NAMES[pred_idx]
    st.success(f"{headers['success']} {pred_class} ({conf*100:.2f}%)")

    if st.button(headers["solution_button"]):
        st.session_state.pred_class = pred_class
        st.session_state.page = "solution"


def solution_page():
    headers = LOCALIZED_HEADERS["en"]
    pred = st.session_state.get("pred_class")

    if not pred:
        st.warning("Upload an image first.")
        return

    st.title("🌱 " + headers["solution_title"])
    sol = get_solution(pred, st.session_state.lang)

    st.subheader(headers["solution_header"])
    st.write(sol["organic_solution"])

    st.subheader(headers["ingredients_header"])
    st.write(sol["ingredients"])

    if st.button(headers["back_upload"]):
        st.session_state.page="upload"


# ---------------- MAIN ----------------
if st.session_state.page == "language":
    language_page()
elif st.session_state.page == "upload":
    upload_page()
elif st.session_state.page == "solution":
    solution_page()
