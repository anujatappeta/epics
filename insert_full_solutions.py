import sqlite3

# Connect to database
conn = sqlite3.connect("solutions.db")
cur = conn.cursor()

# DATA: All 8 diseases × 3 languages (FULL detailed text)
data = [

    # --------------------- ANTHRACNOSE ---------------------
    ("Anthracnose", "en",
     "Prune and burn dead twigs and infected leaves. Spray Pseudomonas fluorescens or neem-based solution weekly. Maintain open canopy for airflow and good nutrition. Ensure regular monitoring to remove new infections. Avoid waterlogging on leaves to prevent fungus.",
     "Neem oil 10ml + Water 1L or Pseudomonas fluorescens solution"),

    ("Anthracnose", "hi",
     "मृत शाखाओं और संक्रमित पत्तों को काटें और जला दें। हर सप्ताह Pseudomonas fluorescens या निम घोल छिड़कें। पेड़ की खुली छत्र बनाए रखें और पोषण सुनिश्चित करें। नए संक्रमण को हटाने के लिए नियमित निगरानी करें। पत्तियों पर पानी जमा न होने दें।",
     "निम तेल 10ml + पानी 1L या Pseudomonas fluorescens घोल"),

    ("Anthracnose", "te",
     "చెక్కిన మరియు పార్టైన ఆకులను కత్తిరించి కాల్చండి. ప్రతి వారానికి Pseudomonas fluorescens లేదా నిమ్ ద్రావణాన్ని స్ప్రే చేయండి. చెట్టు బ్రాంచుల మధ్య గాలి ప్రవాహం కోసం పొలం తెరిచి ఉంచండి. కొత్త ఇన్ఫెక్షన్లు కనుగొంటే తొలగించండి. ఆకులపై నీరు నిలవనివ్వండి.",
     "నిమ్ ఆయిల్ 10ml + నీరు 1L లేదా Pseudomonas fluorescens ద్రావణం"),

    # --------------------- BACTERIAL CANKER ---------------------
    ("Bacterial Canker", "en",
     "Cut and burn infected branches immediately. Spray neem extract weekly to reduce bacterial spread. Keep foliage dry and avoid overhead watering. Monitor regularly for new infections. Maintain proper sanitation of tools before use.",
     "Neem extract 50ml + Water 1L"),

    ("Bacterial Canker", "hi",
     "संक्रमित शाखाओं को तुरंत काटें और जला दें। रोग फैलाव कम करने के लिए हर सप्ताह निम अर्क छिड़कें। पत्तियों को सूखा रखें, ऊपर से पानी न दें। नए संक्रमण के लिए नियमित जाँच करें। उपकरणों को इस्तेमाल से पहले साफ रखें।",
     "निम अर्क 50ml + पानी 1L"),

    ("Bacterial Canker", "te",
     "పాడైన కొమ్ములను వెంటనే కత్తిరించి కాల్చండి. బాక్టీరియాను తగ్గించడానికి వారానికి ఒకసారి నిమ్ ద్రావణం స్ప్రే చేయండి. ఆకులు పొడి ఉంచండి, పై నుండి నీరు ఇవ్వవద్దు. కొత్త ఇన్ఫెక్షన్లను గుర్తించడానికి నియమితంగా పరిశీలించండి. పరికరాలను ఉపయోగించేముందు శుభ్రం చేయండి.",
     "నిమ్ ఎక్స్ట్రాక్ట్ 50ml + నీరు 1L"),

    # --------------------- CUTTING WEEVIL ---------------------
    ("Cutting Weevil", "en",
     "Remove and destroy infected leaves. Spray neem oil weekly to reduce larvae. Use sticky traps for adult weevils. Apply garlic-chili water on shoots weekly. Monitor crop regularly for new damage.",
     "Neem oil 10ml + Water 1L, Garlic 5g + Chili 5g + Water 1L"),

    ("Cutting Weevil", "hi",
     "संक्रमित पत्ते हटाएँ और नष्ट करें। कीट कम करने के लिए सप्ताह में एक बार निम तेल छिड़कें। वयस्क कीड़ों के लिए चिपकने वाले ट्रैप लगाएँ। शाखाओं पर लहसुन-मिर्च पानी छिड़कें। फसल में नई क्षति के लिए नियमित निगरानी करें।",
     "निम तेल 10ml + पानी 1L, लहसुन 5g + मिर्च 5g + पानी 1L"),

    ("Cutting Weevil", "te",
     "పాడైన ఆకులను తొలగించి నాశనం చేయండి. లార్వాలను తగ్గించడానికి వారానికి ఒకసారి నిమ్ ఆయిల్ స్ప్రే చేయండి. వయస్క వీవీలు కోసం స్టికీ ట్రాప్‌లు వాడండి. కొమ్మలపై వెల్లుల్లి-మిరప చారు నీటిని వారానికి స్ప్రే చేయండి. పంటలో కొత్త నష్టాన్ని పరిశీలించండి.",
     "నిమ్ ఆయిల్ 10ml + నీరు 1L, వెల్లుల్లి 5g + మిరప 5g + నీరు 1L"),

    # --------------------- DIE BACK ---------------------
    ("Die Back", "en",
     "Prune affected branches weekly. Spray neem oil to prevent spread. Remove dead wood from trees. Apply organic compost at the tree base. Ensure proper sunlight and airflow around trees.",
     "Neem oil 10ml + Water 1L, Compost 1kg per tree"),

    ("Die Back", "hi",
     "संक्रमित शाखाओं को सप्ताह में काटें। फैलाव रोकने के लिए निम तेल छिड़कें। पेड़ से मृत लकड़ी हटाएँ। पेड़ के आधार पर कार्बनिक खाद डालें। धूप और हवा का ध्यान रखें।",
     "निम तेल 10ml + पानी 1L, 1kg प्रति पेड़"),

    ("Die Back", "te",
     "ప్రభావిత కొమ్ములను వారానికి కత్తిరించండి. వ్యాప్తి నివారణకు నిమ్ ఆయిల్ స్ప్రే చేయండి. చెట్టు నుండి మృత చెక్కను తొలగించండి. చెట్టు అడుగున ఆర్గానిక్ కాంపోస్ట్ వేయండి. సరైన సూర్యకాంతి మరియు గాలి ప్రవాహం ఉండేలా చూడండి.",
     "నిమ్ ఆయిల్ 10ml + నీరు 1L, 1kg ప్రతి చెట్టు"),

    # --------------------- GALL MIDGE ---------------------
    ("Gall Midge", "en",
     "Remove affected shoots and buds. Spray neem oil weekly to control larvae. Introduce natural predators like wasps. Apply garlic-chili water weekly on young shoots. Monitor flowers regularly for infestation.",
     "Neem oil 10ml + Water 1L, Garlic 5g + Chili 5g + Water 1L"),

    ("Gall Midge", "hi",
     "संक्रमित कलियों और शाखाओं को हटाएँ। लार्वा नियंत्रण के लिए सप्ताह में एक बार निम तेल छिड़कें। प्राकृतिक शिकारी (जैसे ततैया) छोड़ें। युवा शाखाओं पर लहसुन-मिर्च पानी छिड़कें। कलियों की नियमित जाँच करें।",
     "निम तेल 10ml + पानी 1L, लहसुन 5g + मिर्च 5g + पानी 1L"),

    ("Gall Midge", "te",
     "ప్రభావిత కొమ్మలు మరియు పూలను తొలగించండి. లార్వా నియంత్రణ కోసం వారానికి ఒకసారి నిమ్ ఆయిల్ స్ప్రే చేయండి. సహజ శత్రువులను (వాస్ప్స్) పరిచయం చేయండి. యువ కొమ్మలపై వెల్లుల్లి-మిరప చారు నీటిని స్ప్రే చేయండి. పువ్వులను తరచూ పరిశీలించండి.",
     "నిమ్ ఆయిల్ 10ml + నీరు 1L, వెల్లుల్లి 5g + మిరప 5g + నీరు 1L"),

    # --------------------- POWDERY MILDEW ---------------------
    ("Powdery Mildew", "en",
     "Prune malformed panicles and infected leaves. Spray potassium bicarbonate solution weekly. Apply neem oil every 7 days to prevent spread. Maintain open spacing and good airflow. Avoid wet leaves; water soil only.",
     "Potassium bicarbonate 10g + Water 1L, Neem oil 10ml + Water 1L"),

    ("Powdery Mildew", "hi",
     "असामान्य फूलों और संक्रमित पत्तों को काटें। सप्ताह में एक बार पोटैशियम बाइकार्बोनेट का घोल छिड़कें। निम तेल हर 7 दिन छिड़कें। खुला रोपण और हवा का ध्यान रखें। गीली पत्तियाँ न रखें, केवल मिट्टी को पानी दें।",
     "पोटैशियम बाइकार्बोनेट 10g + पानी 1L, निम तेल 10ml + पानी 1L"),

    ("Powdery Mildew", "te",
     "పాడైన పానికల్ మరియు ఆకులను తొలగించండి. వారానికి ఒకసారి పొటాషియం బైకార్బోనేట్ ద్రావణం స్ప్రే చేయండి. ప్రతి 7 రోజులకోసారి నిమ్ ఆయిల్ స్ప్రే చేయండి. గాలి ప్రవాహం ఉండేలా చూడండి. ఆకులు తడిగా ఉండనీయండి.",
     "పొటాషియం బైకార్బోనేట్ 10g + నీరు 1L, నిమ్ ఆయిల్ 10ml + నీరు 1L"),

    # --------------------- SOOTY MOULD ---------------------
    ("Sooty Mould", "en",
     "Prune and destroy heavily infected branches. Spray water to wash honeydew off leaves. Apply neem oil weekly to prevent mould. Introduce ladybugs to control sap-sucking pests. Maintain tree spacing for good airflow.",
     "Neem oil 10ml + Water 1L, 10–20 ladybugs per tree"),

    ("Sooty Mould", "hi",
     "भारी संक्रमित शाखाओं को काटें और नष्ट करें। पत्तियों से हनीड्यू धोने के लिए पानी छिड़कें। सप्ताह में एक बार निम तेल छिड़कें। हनीड्यू वाले कीटों को नियंत्रित करने के लिए लेडीबग छोड़ें। पेड़ों के बीच दूरी बनाए रखें।",
     "निम तेल 10ml + पानी 1L, प्रति पेड़ 10–20 लेडीबग"),

    ("Sooty Mould", "te",
     "తీవ్రంగా పాడైన కొమ్ములను కత్తిరించి తొలగించండి. ఆకులపై హనిడ్యూ తొలగించడానికి నీరు స్ప్రే చేయండి. వారానికి ఒకసారి నిమ్ ఆయిల్ స్ప్రే చేయండి. హనిడ్యూ కీటకాలను నియంత్రించడానికి లేడీబగ్స్ విడుదల చేయండి. చెట్ల మధ్య దూరం ఉంచండి.",
     "నిమ్ ఆయిల్ 10ml + నీరు 1L, ప్రతి చెట్టు 10–20 లేడీబగ్స్"),

    # --------------------- HEALTHY ---------------------
    ("Healthy", "en",
     "Plant is healthy. Continue regular watering and sunlight. Maintain soil fertility with compost. Monitor leaves weekly for early signs of disease. Maintain proper tree spacing and airflow. Remove weeds to prevent pests.",
     "Water, sunlight, compost"),

    ("Healthy", "hi",
     "पौधा स्वस्थ है। नियमित पानी और धूप दें। मिट्टी की उर्वरता बनाए रखने के लिए खाद दें। रोग के शुरुआती लक्षण के लिए पत्तियों की जाँच करें। पेड़ों के बीच दूरी और हवा बनाए रखें। कीट रोकने के लिए खरपतवार हटाएँ।",
     "पानी, धूप, खाद"),

    ("Healthy", "te",
     "మొక్క ఆరోగ్యంగా ఉంది. నియమితంగా నీరు మరియు సూర్యకాంతి ఇవ్వండి. మట్టిలో పోషకత్వం కోసం కాంపోస్ట్ ఉపయోగించండి. ఏవైనా లక్షణాల కోసం ఆకులను తనిఖీ చేయండి. చెట్ల మధ్య సరైన దూరం ఉంచండి. పురుగులను తగ్గించడానికి చెత్త మొక్కలను తొలగించండి.",
     "నీరు, సూర్యకాంతి, కాంపోస్ట్"),
]

# Insert all records
cur.executemany("INSERT INTO solutions VALUES (?, ?, ?, ?)", data)
conn.commit()
conn.close()

print("All disease solutions inserted successfully!")
