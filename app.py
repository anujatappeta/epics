import streamlit as st
import tensorflow as tf
import numpy as np
from tensorflow.keras import layers, models
from tensorflow.keras.applications import EfficientNetB3, efficientnet
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

# ---------------- LOCALIZED TEXT ----------------
LOCALIZED_HEADERS = {
    "en": {"upload_title":"Mango Leaf Detector","upload_subtitle":"Upload or capture a mango leaf image below",
           "upload_file":"📂 Upload Image","capture_camera":"📸 Capture using Camera","info_upload":"Please upload or capture a leaf image to continue.",
           "solution_title":"Organic Solution","solution_button":"🌱 Show Organic Solution","solution_header":"Solution:",
           "ingredients_header":"Ingredients / How to Apply:","back_language":"↩ Back to Language","back_upload":"↩ Back to Upload",
           "try_again":"🔁 Try Another Image","analyzing":"🧠 Analyzing leaf...","success":"✅ Prediction:"},
    "hi": {"upload_title":"आम के पत्ते की पहचान","upload_subtitle":"आम के पत्ते की इमेज अपलोड करें या कैप्चर करें",
           "upload_file":"📂 इमेज अपलोड करें","capture_camera":"📸 कैमरा उपयोग करें","info_upload":"आगे बढ़ने के लिए कृपया पत्ते की इमेज अपलोड करें या कैप्चर करें।",
           "solution_title":"जैविक उपाय","solution_button":"🌱 जैविक उपाय देखें","solution_header":"उपाय:",
           "ingredients_header":"सामग्री / आवेदन कैसे करें:","back_language":"↩ भाषा चुनें","back_upload":"↩ पिछली इमेज पर",
           "try_again":"🔁 नई इमेज के लिए","analyzing":"🧠 पत्ते का विश्लेषण हो रहा है...","success":"✅ पहचान:"},
    "te": {"upload_title":"మామిడి ఆకు డిటెక్టర్","upload_subtitle":"మామిడి ఆకు చిత్రాన్ని అప్‌లోడ్ చేయండి లేదా క్యాప్చర్ చేయండి",
           "upload_file":"📂 చిత్రాన్ని అప్‌లోడ్ చేయండి","capture_camera":"📸 కెమెరా ఉపయోగించండి","info_upload":"కొనసాగడానికి దయచేసి ఆకు చిత్రాన్ని అప్‌లోడ్ చేయండి లేదా క్యాప్చర్ చేయండి.",
           "solution_title":"సేంద్రీయ పరిష్కారం","solution_button":"🌱 సేంద్రీయ పరిష్కారం చూపించు","solution_header":"పరిష్కారం:",
           "ingredients_header":"కావలసినవి / ఎలా దరఖాస్తు చేయాలి:","back_language":"↩ భాషకు తిరిగి","back_upload":"↩ అప్‌లోడ్‌కు తిరిగి",
           "try_again":"🔁 మరొక ఇమేజ్ ప్రయత్నించండి","analyzing":"🧠 ఆకు విశ్లేషిస్తోంది...","success":"✅ అంచనా:"}
}

st.set_page_config(page_title="🌿 Mango Doctor", page_icon="🍃", layout="centered")

# ---------------- MODEL ----------------
@st.cache_resource
def download_model():
    if not os.path.exists(MODEL_PATH):
        st.info("📥 Downloading model weights... please wait.")
        url = f"https://drive.google.com/uc?id={DRIVE_FILE_ID}"
        gdown.download(url, MODEL_PATH, quiet=False)

@st.cache_resource
def load_model():
    download_model()
    data_augmentation = tf.keras.Sequential([
        layers.RandomFlip("horizontal"),
        layers.RandomRotation(0.06),
        layers.RandomZoom(0.06),
        layers.RandomTranslation(0.03,0.03),
        layers.RandomContrast(0.06)
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
if "lang" not in st.session_state:
    st.session_state.lang = "en"
if "pred_class" not in st.session_state:
    st.session_state.pred_class = None
if "confidence" not in st.session_state:
    st.session_state.confidence = 0.0

# ---------------- STYLE ----------------
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Poppins:wght@400;600;700;800&display=swap');
[data-testid="stAppViewContainer"] {background: linear-gradient(145deg,#a8df8e 0%,#68b368 50%,#4a8d4a 100%); font-family:'Poppins',sans-serif; color:#1a4301;}
[data-testid="stMain"] {background-color:transparent;}
.main-container {text-align:center; margin:8vh auto 0; max-width:700px; padding:2rem; animation: fadeIn 1.2s ease-in-out;}
@keyframes fadeIn {from{opacity:0; transform:translateY(30px);} to{opacity:1; transform:translateY(0);}}
h1.title {font-size:3.8rem; font-weight:800; color:#ffffff; text-shadow:2px 2px 10px rgba(0,0,0,0.4); margin-bottom:0.5rem;}
p.subtitle {font-size:1.4rem; color:#ffffff; text-shadow:1px 1px 4px rgba(0,0,0,0.3); margin-bottom:3rem; font-weight:500;}
.stButton>button {background:linear-gradient(90deg,#3c9a40,#7bc950); color:white!important; border:none!important; border-radius:14px!important; padding:0.9rem 2.5rem!important; font-weight:700!important; font-size:1.1rem!important; transition: transform 0.2s ease;}
.stButton>button:hover {transform: scale(1.05);}
.confidence {font-weight:800; color:#1a4301; margin-top:1.5rem; font-size:2rem;}
.solution-text {text-align:left; color:#1a4301; background-color: rgba(255,255,255,0.95); padding:25px; border-radius:18px; margin-top:25px;}
.solution-text h3 {color:#2e7d32; margin-top:0; font-weight:700;}
</style>
""", unsafe_allow_html=True)

# ---------------- PAGE FUNCTIONS ----------------
def language_page():
    headers = LOCALIZED_HEADERS[st.session_state.lang]
    st.markdown("<div class='main-container'>", unsafe_allow_html=True)
    st.markdown("<h1 class='title'>🌍 Choose Your Language</h1>", unsafe_allow_html=True)
    st.markdown("<p class='subtitle'>Select your preferred language to continue.</p>", unsafe_allow_html=True)
    col1, col2, col3 = st.columns(3)
    for col, name, code in zip([col1, col2, col3], ["English","हिन्दी","తెలుగు"], ["en","hi","te"]):
        with col:
            if st.button(name, key=f"lang_{code}", use_container_width=True):
                st.session_state.lang = code
                st.session_state.page = "upload"
    st.markdown("</div>", unsafe_allow_html=True)

def upload_page():
    lang = st.session_state.lang
    headers = LOCALIZED_HEADERS[lang]
    st.markdown("<div class='main-container'>", unsafe_allow_html=True)
    st.markdown(f"<h1 class='title'>🍃 {headers['upload_title']}</h1>", unsafe_allow_html=True)
    st.markdown(f"<p class='subtitle'>{headers['upload_subtitle']}</p>", unsafe_allow_html=True)

    col1, col2 = st.columns(2)
    with col1: uploaded_file = st.file_uploader(headers['upload_file'], type=["jpg","png","jpeg"], label_visibility="collapsed")
    with col2: capture_image = st.camera_input(headers['capture_camera'], label_visibility="collapsed")
    image_source = uploaded_file or capture_image

    if image_source:
        image = Image.open(image_source).convert("RGB")
        st.image(image, use_container_width=True)
        img_array = np.expand_dims(np.array(image.resize(IMG_SIZE)), axis=0)
        img_array = efficientnet.preprocess_input(img_array)
        with st.spinner(headers['analyzing']):
            model = load_model()
            preds = model.predict(img_array)[0]
            pred_idx = np.argmax(preds)
            st.session_state.pred_class = CLASS_NAMES[pred_idx]
            st.session_state.confidence = preds[pred_idx]*100

        st.markdown(f"<div class='confidence'>{headers['success']} {st.session_state.pred_class} ({st.session_state.confidence:.2f}%)</div>", unsafe_allow_html=True)

        col_back, col_sol = st.columns([1,2])
        with col_back:
            if st.button(headers['back_language'], use_container_width=True):
                st.session_state.page = "language"
        with col_sol:
            if st.button(headers['solution_button'], use_container_width=True):
                st.session_state.page = "solution"
    else:
        st.info(headers['info_upload'])
        if st.button(headers['back_language']): st.session_state.page = "language"
    st.markdown("</div>", unsafe_allow_html=True)

def solution_page():
    lang = st.session_state.lang
    headers = LOCALIZED_HEADERS[lang]
    st.markdown("<div class='main-container'>", unsafe_allow_html=True)
    st.markdown(f"<h1 class='title'>🌱 {headers['solution_title']}</h1>", unsafe_allow_html=True)

    if not st.session_state.pred_class:
        st.warning("⚠ Upload an image first.")
    else:
        sol = get_solution(st.session_state.pred_class, lang)
        for i in range(3):
            solution_text = sol.get(f"organic_solution_alt{i}", "") or sol.get("organic_solution", "")
            ingredients_text = sol.get(f"ingredients_alt{i}", "") or sol.get("ingredients", "")
            st.markdown(
                f"<div class='solution-text'>"
                f"<h3>{headers['solution_header']} {i+1}</h3>"
                f"<p>{solution_text}</p>"
                f"<h3>{headers['ingredients_header']}</h3>"
                f"<p>{ingredients_text}</p>"
                f"</div>", unsafe_allow_html=True
            )

    col1, col2 = st.columns(2)
    with col1:
        if st.button(headers['back_upload'], use_container_width=True):
            st.session_state.page = "upload"
    with col2:
        if st.button(headers['try_again'], use_container_width=True):
            st.session_state.page = "upload"
    st.markdown("</div>", unsafe_allow_html=True)

# ---------------- MAIN ----------------
if st.session_state.page == "language":
    language_page()
elif st.session_state.page == "upload":
    upload_page()
elif st.session_state.page == "solution":
    solution_page()
