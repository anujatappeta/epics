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

# ---------------- LOCALIZED TEXT MAPPING (Unchanged) ----------------
LOCALIZED_HEADERS = {
    "en": {
        "upload_title": "Mango Leaf Detector",
        "upload_subtitle": "Upload or capture a mango leaf image below",
        "upload_file": "📂 Upload Image",
        "capture_camera": "📸 Capture using Camera",
        "info_upload": "Please upload or capture a leaf image to continue.",
        "solution_title": "Organic Solution",
        "solution_button": "🌱 Show Organic Solution",
        "solution_header": "Solution:",
        "ingredients_header": "Ingredients / How to Apply:",
        "back_language": "↩ Back to Language",
        "back_upload": "↩ Back to Upload",
        "try_again": "🔁 Try Another Image",
        "analyzing": "🧠 Analyzing leaf...",
        "success": "✅ Prediction:"
    },
    "hi": {
        "upload_title": "आम के पत्ते की पहचान",
        "upload_subtitle": "आम के पत्ते की इमेज अपलोड करें या कैप्चर करें",
        "upload_file": "📂 इमेज अपलोड करें",
        "capture_camera": "📸 कैमरा उपयोग करें",
        "info_upload": "आगे बढ़ने के लिए कृपया पत्ते की इमेज अपलोड करें या कैप्चर करें।",
        "solution_title": "जैविक उपाय",
        "solution_button": "🌱 जैविक उपाय देखें",
        "solution_header": "उपाय:",
        "ingredients_header": "सामग्री / आवेदन कैसे करें:",
        "back_language": "↩ भाषा चुनें",
        "back_upload": "↩ पिछली इमेज पर",
        "try_again": "🔁 नई इमेज के लिए",
        "analyzing": "🧠 पत्ते का विश्लेषण हो रहा है...",
        "success": "✅ पहचान:"
    },
    "te": {
        "upload_title": "మామిడి ఆకు డిటెక్టర్",
        "upload_subtitle": "మామిడి ఆకు చిత్రాన్ని అప్‌లోడ్ చేయండి లేదా క్యాప్చర్ చేయండి",
        "upload_file": "📂 చిత్రాన్ని అప్‌లోడ్ చేయండి",
        "capture_camera": "📸 కెమెరా ఉపయోగించండి",
        "info_upload": "కొనసాగడానికి దయచేసి ఆకు చిత్రాన్ని అప్‌లోడ్ చేయండి లేదా క్యాప్చర్ చేయండి.",
        "solution_title": "సేంద్రీయ పరిష్కారం",
        "solution_button": "🌱 సేంద్రీయ పరిష్కారం చూపించు",
        "solution_header": "పరిష్కారం:",
        "ingredients_header": "కావలసినవి / ఎలా దరఖాస్తు చేయాలి:",
        "back_language": "↩ భాషకు తిరిగి",
        "back_upload": "↩ అప్‌లోడ్‌కు తిరిగి",
        "try_again": "🔁 మరొక ఇమేజ్ ప్రయత్నించండి",
        "analyzing": "🧠 ఆకు విశ్లేషిస్తోంది...",
        "success": "✅ అంచనా:"
    }
}

st.set_page_config(page_title="🌿 Mango Doctor", page_icon="🍃", layout="centered")

# ---------------- MODEL FUNCTIONS (omitted for brevity) ----------------
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

# ---------------- STYLE (WOW Factor - Highly Polished) ----------------
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@400;600;700;800&display=swap');
    
    /* Global Background and Font */
    [data-testid="stAppViewContainer"] {
        /* Softer, more elegant green gradient */
        background: linear-gradient(145deg, #a8df8e 0%, #68b368 50%, #4a8d4a 100%);
        font-family: 'Poppins', sans-serif;
        color: #1a4301; /* Darker, richer text color */
    }
    
    [data-testid="stMain"] { background-color: transparent; }

    .main-container {
        text-align: center;
        margin: 8vh auto 0;
        max-width: 700px; /* Slightly wider */
        padding: 2rem;
        animation: fadeIn 1.2s ease-in-out;
    }
    
    @keyframes fadeIn {
        from { opacity: 0; transform: translateY(30px); }
        to { opacity: 1; transform: translateY(0); }
    }
    
    h1.title {
        font-size: 3.8rem; /* Even Larger Title */
        font-weight: 800;
        color: #ffffff; /* White title for contrast */
        text-shadow: 2px 2px 10px rgba(0,0,0,0.4); /* Stronger shadow */
        margin-bottom: 0.5rem;
    }
    
    p.subtitle {
        font-size: 1.4rem; /* Larger Subtitle */
        color: #ffffff;
        text-shadow: 1px 1px 4px rgba(0,0,0,0.3);
        margin-bottom: 3rem;
        font-weight: 500;
    }
    
    /* --------------------------------- */
    /* 🌿 Language Button Cards (Glassmorphism/Neumorphism Hybrid) */
    /* --------------------------------- */
    .language-button-container {
        display: flex;
        justify-content: center;
        gap: 30px; /* More space between buttons */
        margin-top: 20px;
    }
    
    .language-selection-button > button {
        /* Glass/Frosted effect */
        background-color: rgba(255, 255, 255, 0.2) !important;
        backdrop-filter: blur(10px) !important;
        -webkit-backdrop-filter: blur(10px) !important; 
        
        color: white !important; /* White text on translucent background */
        border: 1px solid rgba(255, 255, 255, 0.4) !important; /* Light border */
        border-radius: 20px !important;
        padding: 1.5rem 1.5rem !important; /* More padding */
        transition: all 0.3s cubic-bezier(.25,.8,.25,1) !important;
        
        /* Subtle Neumorphism-like lift */
        box-shadow: 0 4px 15px rgba(0, 0, 0, 0.3), /* Outer shadow */
                    inset 0 0 0 0 rgba(255, 255, 255, 0.6) !important; /* Inner glow (off by default) */

        width: 170px !important; /* Larger fixed width */
        height: 110px !important;
        font-size: 1.6rem !important;
        font-weight: 700 !important;
    }

    .language-selection-button > button:hover {
        transform: translateY(-8px) scale(1.05) !important; /* Dramatic lift */
        box-shadow: 0 15px 30px rgba(0, 0, 0, 0.4), /* Larger shadow on hover */
                    inset 0 0 15px 5px rgba(255, 255, 255, 0.4) !important; /* Visible inner glow on hover */
        background-color: rgba(255, 255, 255, 0.3) !important;
    }

    /* --------------------------------- */
    /* 🌿 General Buttons (Used for Continue/Back/Upload) */
    /* --------------------------------- */
    .stButton>button {
        background: linear-gradient(90deg, #3c9a40, #7bc950);
        color: white !important;
        border: none !important;
        border-radius: 14px !important;
        padding: 0.9rem 2.5rem !important;
        font-weight: 700 !important;
        font-size: 1.1rem !important;
        box-shadow: 0px 4px 15px rgba(0,0,0,0.3);
        transition: all 0.4s ease;
        animation: none; /* Removed constant glow animation */
    }
    
    .stButton>button:hover {
        transform: scale(1.07);
        background: linear-gradient(90deg, #4aa84a, #85e085);
        box-shadow: 0px 8px 20px rgba(0,0,0,0.4);
    }
    
    /* Remaining CSS adjusted for cleaner look */
    img {
        border-radius: 18px; /* Slightly smoother corners */
        margin-top: 15px;
        box-shadow: 0px 5px 15px rgba(0,0,0,0.2);
    }
    
    .confidence {
        font-weight: 700;
        color: #1a4301;
        margin-top: 1.5rem;
        font-size: 1.3rem;
    }
    
    .solution-text {
        text-align: left;
        color: #1a4301;
        background-color: rgba(255, 255, 255, 0.95); /* Nearly opaque white card */
        padding: 25px;
        border-radius: 18px;
        margin-top: 25px;
        box-shadow: 0 5px 15px rgba(0,0,0,0.15);
    }
    
    .solution-text h3 {
        color: #2e7d32;
        margin-top: 0;
        font-weight: 700;
    }
    
    @media (max-width: 768px) {
        h1.title { font-size: 2.5rem; }
        p.subtitle { font-size: 1.1rem; }
        .main-container { margin-top: 5vh; }
        .language-selection-button > button {
            width: 100px !important;
            height: 70px !important;
            font-size: 1.2rem !important;
        }
    }
    </style>
""", unsafe_allow_html=True)

# ---------------- STATE ----------------
if "page" not in st.session_state:
    st.session_state.page = "language"

# ---------------- PAGE: LANGUAGE (WOW Factor - Clickable Buttons) ----------------
if st.session_state.page == "language":
    st.markdown("<div class='main-container'>", unsafe_allow_html=True)
    st.markdown("<h1 class='title'>🌍 Choose Your Language</h1>", unsafe_allow_html=True)
    st.markdown("<p class='subtitle'>Select your preferred language to continue.</p>", unsafe_allow_html=True)

    st.markdown("<div class='language-button-container'>", unsafe_allow_html=True)

    col1, col2, col3 = st.columns(3)

    # Helper function to generate styled buttons
    def generate_lang_button(col, lang_name, lang_code):
        with col:
            # Wrap st.button in a div to apply specific CSS class
            st.markdown("<div class='language-selection-button'>", unsafe_allow_html=True)
            if st.button(lang_name, key=f"lang_{lang_code}", help=f"Select {lang_name}", use_container_width=True):
                st.session_state.lang = lang_code
                st.session_state.page = "upload"
                st.rerun()
            st.markdown("</div>", unsafe_allow_html=True)

    generate_lang_button(col1, "English", "en")
    generate_lang_button(col2, "हिन्दी", "hi")
    generate_lang_button(col3, "తెలుగు", "te")
    
    st.markdown("</div>", unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)

# ---------------- PAGE: UPLOAD ----------------
elif st.session_state.page == "upload":
    lang = st.session_state.get("lang", "en")
    headers = LOCALIZED_HEADERS.get(lang, LOCALIZED_HEADERS["en"])
    
    st.markdown("<div class='main-container'>", unsafe_allow_html=True)
    st.markdown(f"<h1 class='title'>🍃 {headers['upload_title']}</h1>", unsafe_allow_html=True)
    st.markdown(f"<p class='subtitle'>{headers['upload_subtitle']}</p>", unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    with col1:
        uploaded_file = st.file_uploader(headers['upload_file'], type=["jpg", "jpeg", "png"], label_visibility="collapsed")
    with col2:
        capture_image = st.camera_input(headers['capture_camera'], label_visibility="collapsed")
        
    image_source = uploaded_file or capture_image
    
    if image_source:
        image = Image.open(image_source).convert("RGB")
        st.image(image, caption="Uploaded Image", use_container_width=True) 
        img = image.resize(IMG_SIZE)
        img_array = np.expand_dims(np.array(img), axis=0)
        img_array = efficientnet.preprocess_input(img_array)
        
        with st.spinner(headers['analyzing']):
            model = load_model()
            preds = model.predict(img_array)[0]
            pred_idx = np.argmax(preds)
            pred_class = CLASS_NAMES[pred_idx]
            confidence = preds[pred_idx] * 100
            
        st.session_state.pred_class = pred_class
        st.session_state.confidence = confidence
        st.markdown(f"<div class='confidence'>{headers['success']} **{pred_class}** ({confidence:.2f}% confidence)</div>", unsafe_allow_html=True)
        
        st.markdown("<div style='margin-top: 30px;'>", unsafe_allow_html=True)
        btn_col1, btn_col2 = st.columns([1, 2])
        with btn_col1:
            if st.button(headers['back_language'], key="back_from_upload", help="Go back to the language selection page", disabled=False, use_container_width=True):
                st.session_state.page = "language"
                st.rerun()
        with btn_col2:
            if st.button(headers['solution_button'], key="show_solution", use_container_width=True):
                st.session_state.page = "solution"
                st.rerun()
        st.markdown("</div>", unsafe_allow_html=True)
    else:
        st.info(headers['info_upload'])
        
        st.markdown("<div style='margin-top: 30px;'>", unsafe_allow_html=True)
        if st.button(headers['back_language'], key="back_from_upload_empty", help="Go back to the language selection page"):
            st.session_state.page = "language"
            st.rerun()
        st.markdown("</div>", unsafe_allow_html=True)

    st.markdown("</div>", unsafe_allow_html=True)

# ---------------- PAGE: SOLUTION ----------------
elif st.session_state.page == "solution":
    st.markdown("<div class='main-container'>", unsafe_allow_html=True)
    
    lang = st.session_state.get("lang", "en")
    headers = LOCALIZED_HEADERS.get(lang, LOCALIZED_HEADERS["en"])
    
    st.markdown(f"<h1 class='title'>🌱 {headers['solution_title']}</h1>", unsafe_allow_html=True)
    
    if "pred_class" not in st.session_state:
        st.warning("⚠ Upload an image first.")
    else:
        disease = st.session_state.pred_class
        sol = get_solution(disease, lang)
        
        st.markdown(f"### 🌿 {sol['name']}")
        
        st.markdown(f"""
            <div class='solution-text'>
                <h3>{headers['solution_header']}</h3>
                <p>{sol['organic_solution']}</p>
            </div>
            <div class='solution-text'>
                <h3>{headers['ingredients_header']}</h3>
                <p>{sol['ingredients']}</p>
            </div>
        """, unsafe_allow_html=True)
        
    st.markdown("<div style='margin-top: 40px;'>", unsafe_allow_html=True)
    btn_col_sol1, btn_col_sol2 = st.columns(2)
    with btn_col_sol1:
        if st.button(headers['back_upload'], key="back_from_solution", help="Go back to upload a new image", use_container_width=True):
            st.session_state.page = "upload"
            st.rerun()
    with btn_col_sol2:
        if st.button(headers['try_again'], key="try_again_solution", use_container_width=True):
            st.session_state.page = "upload"
            st.rerun()
    st.markdown("</div>", unsafe_allow_html=True)
        
    st.markdown("</div>", unsafe_allow_html=True)
