# solutions.py

DISEASE_SOLUTIONS = {
    "Anthracnose": {
        "en": {
            "name": "Anthracnose",
            "organic_solution": "Prune and destroy infected twigs and debris. Improve air circulation and avoid water splash.",
            "ingredients": "Mix 5g Trichoderma harzianum in 1L water and spray every 10 days."
        },
        "hi": {
            "name": "एन्थ्रेक्नोज़",
            "organic_solution": "संक्रमित शाखाएँ काटें और नष्ट करें। हवा का संचार बढ़ाएँ और पानी छिड़काव से बचें।",
            "ingredients": "1 लीटर पानी में 5 ग्राम Trichoderma harzianum मिलाकर हर 10 दिन छिड़काव करें।"
        },
        "te": {
            "name": "ఆంత్రాక్నోజ్",
            "organic_solution": "సోకిన కొమ్మలను తొలగించండి. గాలి ప్రసరణ పెంచండి మరియు నీటిని నేరుగా వదలవద్దు.",
            "ingredients": "1 లీటర్ నీటిలో 5గ్రా Trichoderma harzianum కలిపి ప్రతి 10 రోజులకు స్ప్రే చేయండి."
        }
    },

    "Bacterial Canker": {
        "en": {
            "name": "Bacterial Canker",
            "organic_solution": "Remove infected branches and disinfect tools. Avoid overhead irrigation.",
            "ingredients": "Spray 0.3% copper oxychloride once every 15 days or 3% neem oil solution."
        },
        "hi": {
            "name": "बैक्टीरियल कैंकर",
            "organic_solution": "संक्रमित शाखाएँ हटाएँ और उपकरण की सफाई करें। ऊपर से पानी देने से बचें।",
            "ingredients": "हर 15 दिन में 0.3% कॉपर ऑक्सीक्लोराइड या 3% नीम तेल का छिड़काव करें।"
        },
        "te": {
            "name": "బ్యాక్టీరియల్ క్యాంకర్",
            "organic_solution": "సోకిన కొమ్మలను తొలగించండి. పై నుండి నీటిని వదలవద్దు. పరికరాలను శుభ్రం చేయండి.",
            "ingredients": "ప్రతి 15 రోజులకు 0.3% కాపర్ ఆక్సీక్లోరైడ్ లేదా 3% వేపనూనె స్ప్రే చేయండి."
        }
    },

    "Cutting Weevil": {
        "en": {
            "name": "Cutting Weevil",
            "organic_solution": "Collect weevils manually in the evening and destroy them. Spray 3% neem oil.",
            "ingredients": "Mix 300 ml neem oil + 10 L water + 10 ml soap solution and spray."
        },
        "hi": {
            "name": "कटिंग वीविल",
            "organic_solution": "शाम को कीट इकट्ठा करें और नष्ट करें। 3% नीम तेल छिड़कें।",
            "ingredients": "300 ml नीम तेल + 10 L पानी + 10 ml साबुन मिलाकर छिड़काव करें।"
        },
        "te": {
            "name": "కట్టింగ్ వీవిల్",
            "organic_solution": "సాయంత్రం వీవిల్స్ సేకరించి నాశనం చేయండి. 3% వేపనూనె స్ప్రే చేయండి.",
            "ingredients": "300 మి.లీ వేపనూనె + 10 లీటర్ నీరు + 10 మి.లీ సబ్బు కలిపి స్ప్రే చేయండి."
        }
    },

    "Die Back": {
        "en": {
            "name": "Die Back",
            "organic_solution": "Cut 2 inches below infected area. Apply Trichoderma paste on cut ends.",
            "ingredients": "Mix 10g Trichoderma + 100ml water + 10g cow dung, apply on cut surface."
        },
        "hi": {
            "name": "डाई बैक",
            "organic_solution": "संक्रमित भाग को काटें। कटे हिस्सों पर ट्राइकोडर्मा पेस्ट लगाएँ।",
            "ingredients": "10g Trichoderma + 100ml पानी + 10g गोबर मिलाकर कटे हिस्सों पर लगाएँ।"
        },
        "te": {
            "name": "డై బ్యాక్",
            "organic_solution": "సోకిన భాగాన్ని 2 అంగుళాలు కత్తిరించండి. కత్తిరించిన చోట Trichoderma పేస్ట్ అప్లై చేయండి.",
            "ingredients": "10g Trichoderma + 100ml నీరు + 10g గోবর కలిపి కత్తిరించిన చోట రాయండి."
        }
    },

    "Gall Midge": {
        "en": {
            "name": "Gall Midge",
            "organic_solution": "Remove and burn affected leaves. Spray 5% neem seed kernel extract (NSKE).",
            "ingredients": "Soak 500g crushed neem seeds in 10L water overnight, filter, and spray."
        },
        "hi": {
            "name": "गॉल मिज",
            "organic_solution": "प्रभावित पत्तियाँ तोड़ें और जलाएँ। 5% नीम बीज अर्क छिड़कें।",
            "ingredients": "500g नीम बीज को 10 L पानी में रात भर भिगोएँ, छानें और छिड़काव करें।"
        },
        "te": {
            "name": "గాల్ మిడ్జ్",
            "organic_solution": "సోకిన ఆకులను తొలగించి దహనం చేయండి. 5% వేప గింజల ఎక్స్‌ట్రాక్ట్ స్ప్రే చేయండి.",
            "ingredients": "500g వేప గింజలను 10 L నీటిలో రాత్రంతా నానబెట్టండి, వడకట్టి స్ప్రే చేయండి."
        }
    },

    "Powdery Mildew": {
        "en": {
            "name": "Powdery Mildew",
            "organic_solution": "Spray 2% potassium bicarbonate or diluted cow milk. Avoid dense canopy and improve sunlight.",
            "ingredients": "Mix 200 ml cow milk + 1.8 L water or 2% potassium bicarbonate solution; spray weekly."
        },
        "hi": {
            "name": "पाउडरी मिल्ड्यू",
            "organic_solution": "2% पोटैशियम बाइकार्बोनेट या दूध का छिड़काव करें।",
            "ingredients": "200 ml दूध + 1.8 L पानी मिलाकर छिड़काव करें।"
        },
        "te": {
            "name": "పౌడరీ మిల్డ్యూ",
            "organic_solution": "2% పొటాషియం బైకార్బోనేట్ లేదా పాల ద్రావణం స్ప్రే చేయండి.",
            "ingredients": "200 ml పాల + 1.8 L నీటిని కలపండి మరియు వారానికి ఒకసారి స్ప్రే చేయండి."
        }
    },

    "Sooty Mould": {
        "en": {
            "name": "Sooty Mould",
            "organic_solution": "Wash leaves with mild soap solution. Control aphids and scales using neem oil.",
            "ingredients": "Mix 5 ml neem oil + 1 L water + few drops of soap and spray."
        },
        "hi": {
            "name": "स्यूटी मोल्ड",
            "organic_solution": "हल्के साबुन के घोल से पत्तियाँ धोएँ। नीम तेल से अफिड और स्केल नियंत्रित करें।",
            "ingredients": "5 ml नीम तेल + 1 L पानी + कुछ बूंदे साबुन मिलाकर छिड़काव करें।"
        },
        "te": {
            "name": "సూటీ మోల్డ్",
            "organic_solution": "తేలికపాటి సబ్బుతో ఆకులను శుభ్రం చేయండి. వేపనూనెతో ఆఫిడ్లు మరియు స్కేలు నియంత్రించండి.",
            "ingredients": "5 ml వేపనూనె + 1 L నీరు + కొన్ని బిందువులు సబ్బు కలిపి స్ప్రే చేయండి."
        }
    },

    "Healthy": {
        "en": {
            "name": "Healthy Leaf",
            "organic_solution": "Maintain clean orchard, regular care, and balanced nutrition.",
            "ingredients": "Spray 2% neem oil monthly. Apply Panchagavya or Jeevamruth as organic nutrition."
        },
        "hi": {
            "name": "स्वस्थ पत्ता",
            "organic_solution": "ताजा और साफ़ बगीचा रखें, नियमित देखभाल करें और संतुलित पोषण दें।",
            "ingredients": "महीने में 2% नीम तेल छिड़कें। पंचगव्य या जीवामृत का उपयोग करें।"
        },
        "te": {
            "name": "ఆరోగ్యమైన ఆకు",
            "organic_solution": "తోటను శుభ్రంగా ఉంచండి, సరైన సంరక్షణ చేయండి మరియు సమతుల్య పోషణ అందించండి.",
            "ingredients": "నెలకు ఒకసారి 2% వేపనూనె స్ప్రే చేయండి. పంచగవ్య లేదా జీవామృతం ఉపయోగించండి."
        }
    }
}


def get_solution(disease_name: str, lang: str = "en"):
    """Fetch organic solution for a disease safely in the chosen language."""
    return DISEASE_SOLUTIONS.get(disease_name, DISEASE_SOLUTIONS["Healthy"]).get(lang, DISEASE_SOLUTIONS["Healthy"]["en"])
