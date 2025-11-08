# solutions.py

DISEASE_SOLUTIONS = {
    "Anthracnose": {
        "en": {
            "name": "Anthracnose",
            "organic_solution": "Prune infected twigs, improve air circulation, avoid water splash.",
            "ingredients": "5g Trichoderma harzianum in 1L water, spray every 10 days.",
            "organic_solution_alt1": "Baking soda spray every 7-10 days; avoid overhead watering.",
            "ingredients_alt1": "1-2 tsp baking soda in 1L water, spray foliage until runoff.",
            "organic_solution_alt2": "Compost-tea soil drench every 2-4 weeks.",
            "ingredients_alt2": "1 part mature compost : 10 parts water, aerate overnight."
        },
        "hi": {
            "name": "एन्थ्रेक्नोज़",
            "organic_solution": "संक्रमित शाखाएँ काटें। हवा का संचार बढ़ाएँ, पानी छिड़काव से बचें।",
            "ingredients": "1 लीटर पानी में 5 ग्राम Trichoderma harzianum, हर 10 दिन छिड़काव करें।",
            "organic_solution_alt1": "बेकिंग सोडा स्प्रे 7-10 दिन में एक बार; ऊपर से पानी देने से बचें।",
            "ingredients_alt1": "1-2 चम्मच बेकिंग सोडा + 1 लीटर पानी, पत्तियों पर छिड़काव।",
            "organic_solution_alt2": "कम्पोस्ट‑टी ड्रींच हर 2-4 सप्ताह।",
            "ingredients_alt2": "मूल कम्पोस्ट : पानी = 1 : 10, रातभर एयरटेट करें।"
        },
        "te": {
            "name": "ఆంత్రాక్నోజ్",
            "organic_solution": "సోకిన కొమ్మలను తొలగించండి, గాలి ప్రసరణ పెంచండి, పై నీటివిడవడం నివారించండి.",
            "ingredients": "1 లీటర్ నీటిలో 5గ్రా Trichoderma harzianum, ప్రతి 10 రోజులకు స్ప్రే చేయండి.",
            "organic_solution_alt1": "బేకింగ్ సోడా స్ప్రే 7–10 రోజుల్లో ఒకసారి, పై నీరు నివారించండి.",
            "ingredients_alt1": "1–2 టీస్పూన్ల బేకింగ్ సోడా + 1 లీటర్ నీరు, ఆకులపై స్ప్రే చేయండి.",
            "organic_solution_alt2": "కంపోస్ట్‑టీ ప్రతి 2–4 వారాల్లో మట్టి చుట్టూ ఉపయోగించండి.",
            "ingredients_alt2": "కంపోస్ట్ : నీరు = 1 : 10, రాత్రిపూట గాలి వేయండి."
        }
    },
    "Bacterial Canker": {
        "en": {
            "name": "Bacterial Canker",
            "organic_solution": "Remove infected parts, apply neem oil or garlic extract spray.",
            "ingredients": "Neem oil 2% or garlic extract 50ml/L water, spray every 7-10 days.",
            "organic_solution_alt1": "Use bio-fertilizers like Trichoderma for soil health.",
            "ingredients_alt1": "Soil drench with Trichoderma every 2 weeks.",
            "organic_solution_alt2": "Mulching and pruning improve resistance.",
            "ingredients_alt2": "Mulch base of plant, prune dead/diseased branches."
        },
        "hi": {
            "name": "बैक्टीरियल कैंकर",
            "organic_solution": "संक्रमित भाग हटाएँ, नीम तेल या लहसुन का अर्क छिड़कें।",
            "ingredients": "नीम तेल 2% या लहसुन अर्क 50ml/लीटर, हर 7-10 दिन छिड़काव।",
            "organic_solution_alt1": "मिट्टी स्वास्थ्य के लिए ट्राइकोडर्मा जैव उर्वरक उपयोग करें।",
            "ingredients_alt1": "हर 2 सप्ताह में ट्राइकोडर्मा से मिट्टी ड्रींच करें।",
            "organic_solution_alt2": "मल्चिंग और छंटाई रोग प्रतिरोधक क्षमता बढ़ाते हैं।",
            "ingredients_alt2": "पौधे के आधार पर मल्च करें, मृत शाखाएँ काटें।"
        },
        "te": {
            "name": "బాక్టీరియల్ కాంకర్",
            "organic_solution": "సోకిన భాగాలను తొలగించండి, వేపనూనె లేదా వెల్లుల్లి సారాన్ని స్ప్రే చేయండి.",
            "ingredients": "2% వేపనూనె లేదా వెల్లుల్లి సారం 50ml/1L నీరు, ప్రతి 7–10 రోజుల్లో స్ప్రే చేయండి.",
            "organic_solution_alt1": "మట్టిలో ట్రైకోడర్మా బయో‑ఫర్టిలైజర్ ఉపయోగించండి.",
            "ingredients_alt1": "మట్టిలో ప్రతి 2 వారాల్లో ట్రైకోడర్మా డ్రీంచ్ చేయండి.",
            "organic_solution_alt2": "మల్చింగ్ మరియు కత్తిరింపు రోగ నిరోధకత పెంచుతాయి.",
            "ingredients_alt2": "మూల వద్ద మల్చ్ చేయండి, మృత/రోగబారిన కొమ్మలు తొలగించండి."
        }
    },
    "Cutting Weevil": {
        "en": {
            "name": "Cutting Weevil",
            "organic_solution": "Handpick adult weevils, use neem-based traps and pheromone traps.",
            "ingredients": "Spray neem oil 2% weekly; maintain orchard sanitation.",
            "organic_solution_alt1": "Encourage natural predators like birds and ants.",
            "ingredients_alt1": "Install bird perches; avoid insecticides harming ants.",
            "organic_solution_alt2": "Remove infested twigs and destroy them.",
            "ingredients_alt2": "Prune and burn affected branches monthly."
        },
        "hi": {
            "name": "कटिंग वीविल",
            "organic_solution": "कीड़ों को हाथ से चुनें, नीम-आधारित ट्रैप और फेरोमोन ट्रैप लगाएँ।",
            "ingredients": "नीम तेल 2% साप्ताहिक छिड़काव; बगीचे की सफाई बनाए रखें।",
            "organic_solution_alt1": "प्राकृतिक शिकारी पक्षियों और चींटियों को प्रोत्साहित करें।",
            "ingredients_alt1": "पक्षियों के बैठने के लिए पोल लगाएँ; कीटनाशक से बचें।",
            "organic_solution_alt2": "संक्रमित शाखाएँ काटें और नष्ट करें।",
            "ingredients_alt2": "प्रभावित शाखाओं को मासिक रूप से काटें और जला दें।"
        },
        "te": {
            "name": "కట్టింగ్ వీవిల్",
            "organic_solution": "పెద్ద వీవిల్స్‌ను చేతితో తొలగించండి, వేపనూనె- traps మరియు pheromone traps ఉపయోగించండి.",
            "ingredients": "ప్రతి వారం 2% వేపనూనె స్ప్రే; తోట శుభ్రతను ఉంచండి.",
            "organic_solution_alt1": "ప్రाकृतिक శికారులను ప్రోత్సహించండి, పక్షులు మరియు చీమలు.",
            "ingredients_alt1": "పక్షుల కోసం perch లు ఏర్పాటు చేయండి; చీమలకు హానికరమైన инсెక్టిసైడ్ లు నివారించండి.",
            "organic_solution_alt2": "ప్రమాదిత కొమ్మలను తొలగించి నశింపజేయండి.",
            "ingredients_alt2": "మాసికంగా ప్రభావిత కొమ్మలను prune చేసి కాల్చండి."
        }
    },
    "Die Back": {
        "en": {
            "name": "Die Back",
            "organic_solution": "Prune affected branches, avoid waterlogging, maintain tree nutrition.",
            "ingredients": "Spray 2% neem oil and apply organic compost around the base.",
            "organic_solution_alt1": "Foliar spray with bio-fertilizers like Panchagavya.",
            "ingredients_alt1": "Spray every 15 days for better resistance.",
            "organic_solution_alt2": "Ensure good drainage to reduce root stress.",
            "ingredients_alt2": "Remove dead debris and improve soil aeration."
        },
        "hi": {
            "name": "डाई बैक",
            "organic_solution": "संक्रमित शाखाएँ काटें, जलभराव से बचें, पेड़ को पोषण दें।",
            "ingredients": "2% नीम तेल छिड़कें और आधार के चारों ओर जैविक कम्पोस्ट डालें।",
            "organic_solution_alt1": "पंचगव्य जैसे जैविक उर्वरक छिड़काव।",
            "ingredients_alt1": "बेहतर प्रतिरोध के लिए हर 15 दिन छिड़काव।",
            "organic_solution_alt2": "अच्छी जल निकासी सुनिश्चित करें।",
            "ingredients_alt2": "मृत मलबा हटाएँ और मिट्टी में हवा प्रवाह बढ़ाएँ।"
        },
        "te": {
            "name": "డై బ్యాక్",
            "organic_solution": "ప్రమాదిత కొమ్మలను prune చేయండి, నీటివిసర్జన నివారించండి, చెట్టును పోషించండి.",
            "ingredients": "2% వేపనూనె స్ప్రే చేయండి, మూల చుట్టూ ఆర్గానిక్ కంపోస్ట్ ఉపయోగించండి.",
            "organic_solution_alt1": "పంచగవ్య వంటి బయో-ఫర్టిలైజర్ స్ప్రే.",
            "ingredients_alt1": "ప్రతీ 15 రోజులకు స్ప్రే చేయండి.",
            "organic_solution_alt2": "మట్టి డ్రీనేజ్ మెరుగుపరచి రూట్ స్ట్రెస్ తగ్గించండి.",
            "ingredients_alt2": "మృత మల్బ్ తొలగించండి, మట్టిలో గాలి ప్రవాహాన్ని పెంచండి."
        }
    },
    "Gall Midge": {
        "en": {
            "name": "Gall Midge",
            "organic_solution": "Remove infested shoots, apply neem oil and sticky traps.",
            "ingredients": "2% neem oil spray weekly; maintain orchard hygiene.",
            "organic_solution_alt1": "Introduce natural predators like parasitoid wasps.",
            "ingredients_alt1": "Release every month in affected orchards.",
            "organic_solution_alt2": "Prune and destroy galled shoots.",
            "ingredients_alt2": "Burn infected shoots to stop spread."
        },
        "hi": {
            "name": "गैल मिड्ज़",
            "organic_solution": "संक्रमित कल्मों को हटाएँ, नीम तेल और स्टिकी ट्रैप लगाएँ।",
            "ingredients": "2% नीम तेल साप्ताहिक छिड़काव; बगीचे की सफाई बनाए रखें।",
            "organic_solution_alt1": "प्राकृतिक शिकारी परजीवी ततैया।",
            "ingredients_alt1": "संक्रमित बगीचों में मासिक छोड़ें।",
            "organic_solution_alt2": "संक्रमित कल्मों को काटें और नष्ट करें।",
            "ingredients_alt2": "प्रसार रोकने के लिए जला दें।"
        },
        "te": {
            "name": "గాల్ మిడ్",
            "organic_solution": "ప్రమాదిత కొమ్మలను తొలగించండి, వేపనూనె మరియు స్టికీ traps ఉపయోగించండి.",
            "ingredients": "ప్రతి వారం 2% వేపనూనె స్ప్రే; తోట శుభ్రత ఉంచండి.",
            "organic_solution_alt1": "ప్రाकृतिक శికారులు: పారాసైటాయిడ్ wasps.",
            "ingredients_alt1": "మాసానికి ఒకసారి ప్రభావిత తోటల్లో విడుదల చేయండి.",
            "organic_solution_alt2": "గాల్డ్ కొమ్మలను prune చేసి నశింపజేయండి.",
            "ingredients_alt2": "విద్యుత్ కాల్చి వ్యాప్తి ఆపండి."
        }
    },
    "Powdery Mildew": {
        "en": {
            "name": "Powdery Mildew",
            "organic_solution": "Spray potassium bicarbonate or neem oil; remove infected leaves.",
            "ingredients": "1% potassium bicarbonate or 2% neem oil every 7-10 days.",
            "organic_solution_alt1": "Improve air circulation and avoid dense planting.",
            "ingredients_alt1": "Prune crowded branches; avoid wet foliage.",
            "organic_solution_alt2": "Use biofungicides like Trichoderma.",
            "ingredients_alt2": "Apply as soil drench every 2 weeks."
        },
        "hi": {
            "name": "पाउडरी मिल्ड्यू",
            "organic_solution": "पोटैशियम बाइकार्बोनेट या नीम तेल छिड़कें; संक्रमित पत्तियाँ हटाएँ।",
            "ingredients": "1% पोटैशियम बाइकार्बोनेट या 2% नीम तेल, हर 7-10 दिन।",
            "organic_solution_alt1": "हवा का संचार बढ़ाएँ, घना रोपण न करें।",
            "ingredients_alt1": "भीड़ वाले शाखाएँ काटें; पत्तियों को गीला न करें।",
            "organic_solution_alt2": "ट्राइकोडर्मा जैव कवकनाशक उपयोग करें।",
            "ingredients_alt2": "हर 2 सप्ताह मिट्टी में ड्रींच करें।"
        },
        "te": {
            "name": "పౌడరి మిల్డ్యూ",
            "organic_solution": "పోటాషియం బైకార్బోనేట్ లేదా 2% వేపనూనె స్ప్రే చేయండి, ప్రభావిత ఆకు తొలగించండి.",
            "ingredients": "ప్రతి 7–10 రోజుల్లో 1% పొటాషియం బైకార్బోనేట్ లేదా 2% వేపనూనె.",
            "organic_solution_alt1": "గాలి ప్రసరణను మెరుగుపరచండి, ఘనంగా నాటకపు నివారించండి.",
            "ingredients_alt1": "చిత్తడిగిన కొమ్మలను prune చేయండి, ఆకులను తడి చేయవద్దు.",
            "organic_solution_alt2": "ట్రైకోడర్మా బయో-ఫంగిసైడ్ ఉపయోగించండి.",
            "ingredients_alt2": "మట్టి డ్రీంచ్ ప్రతీ 2 వారాలకొకసారి చేయండి."
        }
    },
    "Sooty Mould": {
        "en": {
            "name": "Sooty Mould",
            "organic_solution": "Wash leaves with water to remove mold; control aphids and mealybugs.",
            "ingredients": "Soap solution 5g/L water weekly; neem oil spray.",
            "organic_solution_alt1": "Prune heavily infected branches.",
            "ingredients_alt1": "Remove and burn affected parts.",
            "organic_solution_alt2": "Encourage natural predators like ladybugs.",
            "ingredients_alt2": "Avoid chemical sprays that kill beneficial insects."
        },
        "hi": {
            "name": "सूटी मोल्ड",
            "organic_solution": "पत्तियों को पानी से धोएँ; एफिड और मीलीबग नियंत्रित करें।",
            "ingredients": "साबुन का घोल 5g/L पानी में, साप्ताहिक; नीम तेल छिड़काव।",
            "organic_solution_alt1": "भारी संक्रमित शाखाएँ काटें।",
            "ingredients_alt1": "संक्रमित भाग हटाएँ और जला दें।",
            "organic_solution_alt2": "प्राकृतिक शिकारी जैसे लेडीबग को प्रोत्साहित करें।",
            "ingredients_alt2": "लाभकारी कीट मारने वाले रसायन से बचें।"
        },
        "te": {
            "name": "సూటి మోల్",
            "organic_solution": "ఆకులను నీటితో కడగండి; ఆఫిడ్స్ మరియు మీలీబగ్స్ నియంత్రించండి.",
            "ingredients": "5g/L నీరు సబ్బు ద్రావణం ప్రతి వారం; వేపనూనె స్ప్రే.",
            "organic_solution_alt1": "భారమైన ప్రభావిత కొమ్మలను prune చేయండి.",
            "ingredients_alt1": "ప్రభావిత భాగాలను తొలగించి కాల్చండి.",
            "organic_solution_alt2": "ప్రకృతిక శికారులను ప్రోత్సహించండి, ఉదాహరణకి లేడీబగ్.",
            "ingredients_alt2": "లాభకారి కీట్స్ ను హానిచేయే రసాయనాలు నివారించండి."
        }
    },
    "Healthy": {
        "en": {
            "name": "Healthy Leaf",
            "organic_solution": "Maintain clean orchard, regular care, and balanced nutrition.",
            "ingredients": "Spray 2% neem oil monthly. Apply Panchagavya or Jeevamruth.",
            "organic_solution_alt1": "Prune damaged leaves and branches regularly.",
            "ingredients_alt1": "Remove and compost damaged parts once a month.",
            "organic_solution_alt2": "Encourage beneficial insects for natural pest control.",
            "ingredients_alt2": "Plant flowering companion plants to attract ladybugs and pollinators."
        },
        "hi": {
            "name": "स्वस्थ पत्ता",
            "organic_solution": "ताजा और साफ़ बगीचा रखें, नियमित देखभाल करें और संतुलित पोषण दें।",
            "ingredients": "महीने में 2% नीम तेल छिड़कें। पंचगव्य या जीवामृत का उपयोग करें।",
            "organic_solution_alt1": "नुकसान वाली पत्तियाँ और शाखाएँ नियमित रूप से छाँटें।",
            "ingredients_alt1": "प्रभावित हिस्सों को हटाकर कम्पोस्ट करें, प्रति माह एक बार।",
            "organic_solution_alt2": "प्राकृतिक कीट नियंत्रण के लिए लाभकारी कीटों को प्रोत्साहित करें।",
            "ingredients_alt2": "पंखुड़ी वाले फूलों वाले पौधे लगाएँ ताकि लेडीबग और परागकण आकर्षित हों।"
        },
        "te": {
            "name": "ఆరోగ్యమైన ఆకు",
            "organic_solution": "తోటను శుభ్రంగా ఉంచండి, సరైన సంరక్షణ చేయండి మరియు సమతుల్య పోషణ అందించండి.",
            "ingredients": "నెలకు ఒకసారి 2% వేపనూనె స్ప్రే చేయండి. పంచగవ్య లేదా జీవామృతం ఉపయోగించండి.",
            "organic_solution_alt1": "నష్టపరిచిన ఆకులు మరియు కొమ్మలను pravidha గా prune చేయండి.",
            "ingredients_alt1": "ప్రభావిత భాగాలను తొలగించి కంపోస్ట్ చేయండి, ప్రతి నెల ఒకసారి.",
            "organic_solution_alt2": "ప్రाकृतिक పురుగు నియంత్రణ కోసం లాభకారి పురుగులను ప్రోత్సహించండి.",
            "ingredients_alt2": "పూల తోటి మొక్కలు నాటండి, లేడీబగ్స్ మరియు పరాగకర్తలను ఆకర్షించడానికి."
        }
    }
}

def get_solution(disease_name: str, lang: str = "en"):
    """Fetch all organic solutions for a disease safely in the chosen language."""
    data = DISEASE_SOLUTIONS.get(disease_name, DISEASE_SOLUTIONS["Healthy"]).get(lang, DISEASE_SOLUTIONS["Healthy"]["en"])
    
    # Collect all solutions
    solutions = {
        "name": data.get("name", "Healthy Leaf"),
        "organic_solution": data.get("organic_solution", ""),
        "ingredients": data.get("ingredients", ""),
        "organic_solution_alt1": data.get("organic_solution_alt1", ""),
        "ingredients_alt1": data.get("ingredients_alt1", ""),
        "organic_solution_alt2": data.get("organic_solution_alt2", ""),
        "ingredients_alt2": data.get("ingredients_alt2", "")
    }
    return solutions   
