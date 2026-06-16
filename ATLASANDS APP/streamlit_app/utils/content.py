"""Indian culinary journey database — dishes by region."""

CULINARY = [
    {
        "region": "North India", "states": "Punjab • Delhi • UP • Rajasthan",
        "image": "https://images.unsplash.com/photo-1585937421612-70a008356fbe?w=1400&q=85",
        "signature": ["Butter Chicken", "Dal Makhani", "Sarson da Saag", "Chole Bhature", "Tandoori Kebabs", "Rajma Chawal"],
        "vegetarian": ["Dal Baati Churma", "Paneer Tikka", "Aloo Paratha", "Kachori-Sabzi", "Pyaaz Kachori"],
        "sweet": "Gulab Jamun, Jalebi, Phirni",
        "must_try_city": "Old Delhi's Chandni Chowk at midnight.",
        "note": "Rich, creamy, ghee-laced — North India is for warmth and indulgence."
    },
    {
        "region": "South India", "states": "Tamil Nadu • Kerala • Karnataka • Andhra",
        "image": "https://images.unsplash.com/photo-1630383249896-424e482df921?w=1400&q=85&auto=format&fit=crop",
        "signature": ["Masala Dosa", "Idli-Sambar", "Hyderabadi Biryani", "Karimeen Pollichathu", "Chettinad Chicken", "Appam Stew"],
        "vegetarian": ["Bisi Bele Bath", "Sadhya banana-leaf feast", "Curd Rice", "Pongal", "Mysore Masala Dosa"],
        "sweet": "Mysore Pak, Payasam, Pootharekulu",
        "must_try_city": "Madurai for non-veg; Mysore for vegetarian.",
        "note": "Coconut, curry leaves, tamarind — clean, bright, fiery layers."
    },
    {
        "region": "East India", "states": "Bengal • Odisha • Assam",
        "image": "https://images.unsplash.com/photo-1606491956689-2ea866880c84?w=1400&q=85&auto=format&fit=crop",
        "signature": ["Ilish Bhapa (steamed hilsa)", "Kosha Mangsho", "Macher Jhol", "Pakhala Bhata", "Assamese Duck Curry"],
        "vegetarian": ["Shukto", "Aloo Posto", "Cholar Dal", "Khar (Assam)", "Dalma (Odisha)"],
        "sweet": "Rosogolla, Mishti Doi, Sandesh, Pithas",
        "must_try_city": "Kolkata Park Street for kathi rolls and Bengali fine dining.",
        "note": "Mustard oil, panch phoron, freshwater fish — refined yet rustic."
    },
    {
        "region": "West India", "states": "Maharashtra • Gujarat • Goa",
        "image": "https://images.unsplash.com/photo-1585937421612-70a008356fbe?w=1400&q=85&auto=format&fit=crop",
        "signature": ["Pav Bhaji", "Vada Pav", "Goan Vindaloo", "Sorpotel", "Bombay Duck Fry", "Misal Pav"],
        "vegetarian": ["Gujarati Thali", "Dhokla", "Khaman", "Undhiyu", "Puran Poli", "Thepla"],
        "sweet": "Modak, Shrikhand, Bebinca (Goa), Basundi",
        "must_try_city": "Ahmedabad for vegetarian thalis; Panjim for seafood.",
        "note": "Coastal coconut + Portuguese soul (Goa) meets Gujarati sweet-savoury balance."
    },
    {
        "region": "Northeast India", "states": "Nagaland • Meghalaya • Sikkim • Arunachal",
        "image": "https://images.unsplash.com/photo-1630383249896-424e482df921?w=1400&q=85&auto=format&fit=crop",
        "signature": ["Bamboo Shoot Pork", "Smoked Pork with Akhuni", "Thukpa", "Momos", "Phaksa Paa", "Jadoh (Khasi)"],
        "vegetarian": ["Iromba (Manipur)", "Bamboo Shoot Curry", "Eromba", "Tibetan Tingmo bread"],
        "sweet": "Kheer with red rice, Til Pitha",
        "must_try_city": "Kohima during Hornbill Festival in December.",
        "note": "Smoke, ferment and forest — the cleanest, most unique cuisine in India."
    },
    {
        "region": "Kashmiri Wazwan", "states": "Jammu & Kashmir",
        "image": "https://images.unsplash.com/photo-1631452180519-c014fe946bc7?w=1400&q=85&auto=format&fit=crop",
        "signature": ["Rogan Josh", "Yakhni", "Gushtaba", "Tabak Maaz", "Rista", "Kashmiri Pulao"],
        "vegetarian": ["Dum Aloo", "Nadru Yakhni (lotus stem)", "Haak Saag", "Chaman (paneer)", "Modur Pulao"],
        "sweet": "Phirni, Sheermal, Halwa-Paratha",
        "must_try_city": "Srinagar's heritage homes for a traditional Wazwan feast (36 courses).",
        "note": "Saffron, fennel, dried ginger, Kashmiri red chilli — slow-cooked royalty."
    },
]


HIDDEN_WORLDS = [
    {
        "name": "Ziro Valley", "state": "Arunachal Pradesh",
        "image": "https://images.unsplash.com/photo-1532664189809-02133fee698d?w=1600&q=85&auto=format&fit=crop",
        "why": "Home of the Apatani tribe and the world's most beautiful rice-fish cultivation, Ziro hosts an annual indie music festival every September that turns the valley into India's secret Glastonbury.",
        "best": "September (festival) or April–October",
        "experience": "Stay with Apatani families, walk paddy bunds at dawn, hear bamboo flutes echo across the valley."
    },
    {
        "name": "Majuli Island", "state": "Assam",
        "image": "https://images.unsplash.com/photo-1605649487212-47bdab064df7?w=1600&q=85&auto=format&fit=crop",
        "why": "The world's largest river island sits on the Brahmaputra — home to neo-Vaishnavite Satras (monasteries) preserving 500-year-old dance and mask-making traditions.",
        "best": "November–March",
        "experience": "Cycle between Satras, watch Bhaona theatre, sleep in stilted bamboo cottages."
    },
    {
        "name": "Khonoma", "state": "Nagaland",
        "image": "https://images.unsplash.com/photo-1626621341517-bbf3d9990a23?w=1600&q=85&auto=format&fit=crop",
        "why": "Asia's first green village — Angami warriors converted their hunting grounds into a wildlife sanctuary. Stone-walled terraces climb 1,000 metres into mist.",
        "best": "October–April",
        "experience": "Walk with hunter-turned-conservationist guides; sleep in heritage Angami homes."
    },
    {
        "name": "Dholavira", "state": "Gujarat",
        "image": "https://images.unsplash.com/photo-1599661046289-e31897846e41?w=1600&q=85&auto=format&fit=crop",
        "why": "A 5,000-year-old Indus Valley city in the middle of the Great Rann of Kutch — UNESCO World Heritage, almost no tourists, surrounded by a salt desert that turns silver under the moon.",
        "best": "November–February",
        "experience": "Sunrise at the citadel, full-moon walk on the Rann salt flats, stay at Evoke Dholavira."
    },
    {
        "name": "Mawlynnong", "state": "Meghalaya",
        "image": "https://images.unsplash.com/photo-1531251445707-1f000e1e87d0?w=1600&q=85&auto=format&fit=crop",
        "why": "Asia's cleanest village (officially) — Khasi matrilineal community, living root bridges in the surrounding jungle, and a sky-walk made of bamboo.",
        "best": "October–April",
        "experience": "Trek to the double-decker root bridge in Nongriat; stay in stilted bamboo homestays."
    },
    {
        "name": "Chitkul", "state": "Himachal Pradesh",
        "image": "https://images.unsplash.com/photo-1469854523086-cc02fe5d8800?w=1600&q=85&auto=format&fit=crop",
        "why": "The last inhabited village before the Tibet border in the Sangla valley — wooden houses, prayer flags, and the Baspa river racing through deodar forests.",
        "best": "May–October",
        "experience": "Sleep in a 200-year-old wooden home, drink butter tea, walk to the army's last outpost."
    },
    {
        "name": "Gurez Valley", "state": "Kashmir",
        "image": "https://images.unsplash.com/photo-1593181629936-11c609b8db9b?w=1600&q=85&auto=format&fit=crop",
        "why": "The Kishanganga river carves through Habba Khatoon peak in a valley that was on the old Silk Route. Opened to civilians only recently.",
        "best": "May–September",
        "experience": "Stay in Dawar village log huts, ride horses to remote hamlets, watch trout fishermen at dawn."
    },
    {
        "name": "Patan Stepwell (Rani ki Vav)", "state": "Gujarat",
        "image": "https://images.unsplash.com/photo-1564507592333-c60657eea523?w=1600&q=85&auto=format&fit=crop",
        "why": "An 11th-century underground stepwell — seven storeys of carved sculpture descending into the earth like an inverted temple. UNESCO Heritage, barely visited.",
        "best": "October–March",
        "experience": "Visit at golden hour when light shafts hit the carvings; pair with Modhera Sun Temple."
    },
    {
        "name": "Bhimbetka Caves", "state": "Madhya Pradesh",
        "image": "https://images.unsplash.com/photo-1524492412937-b28074a5d7da?w=1600&q=85&auto=format&fit=crop",
        "why": "30,000-year-old rock paintings — one of the oldest art galleries on Earth — hidden in sandstone shelters in the Vindhya hills.",
        "best": "October–March",
        "experience": "Walk the painted shelters with a local archaeologist, then drive to Bhojpur and Sanchi."
    },
    {
        "name": "Cherrapunji's Living Root Bridges", "state": "Meghalaya",
        "image": "https://images.unsplash.com/photo-1518002171953-a080ee817e1f?w=1600&q=85&auto=format&fit=crop",
        "why": "Bridges grown — not built — by training the roots of rubber fig trees across rivers for 200+ years. The Nongriat double-decker is unique to Earth.",
        "best": "October–April",
        "experience": "3,500-step trek down to Nongriat, swim in turquoise plunge pools, stay overnight in the village."
    },
]


TIMELINE_SAMPLE = [
    {"day": 1, "title": "Arrival & First Impressions",
     "desc": "Land softly, settle into your stay, take an unhurried evening walk and let the destination introduce itself."},
    {"day": 2, "title": "Adventure & Discovery",
     "desc": "Lace your shoes and chase the views. A signature trek, drive or activity that earns the evening's celebration."},
    {"day": 3, "title": "Culture & Heritage",
     "desc": "Slow morning. Local market. A handcraft workshop or a heritage site you'll think about long after."},
    {"day": 4, "title": "Relaxation & Memories",
     "desc": "Sleep in. A spa or a quiet café. Pack with images, scents and stories that will outlast the suitcase."},
]


TESTIMONIALS = [
    {"name": "Ananya Iyer", "city": "Bangalore → Kashmir",
     "image": "https://images.unsplash.com/photo-1544005313-94ddf0286df2?w=400&q=85&auto=format&fit=crop",
     "rating": 5,
     "quote": "ATLASANDS didn't plan a trip — it composed a memory. From the houseboat at dawn to the Gulmarg gondola at golden hour, every detail felt curated for me."},
    {"name": "Rohan Mehta", "city": "Mumbai → Ladakh",
     "image": "https://images.unsplash.com/photo-1507003211169-0a1dd7228f2d?w=400&q=85&auto=format&fit=crop",
     "rating": 5,
     "quote": "The AI Concierge knew which side of the SUV had the better view of Pangong. It knew when to be quiet. I'll never plan a trip alone again."},
    {"name": "Sara Khan", "city": "Delhi → Kerala",
     "image": "https://images.unsplash.com/photo-1438761681033-6461ffad8d80?w=400&q=85&auto=format&fit=crop",
     "rating": 5,
     "quote": "I told them I wanted backwaters and silence. They gave me a houseboat, a chef called Ravi, and a sunset that I still see when I close my eyes."},
    {"name": "Aarav Sharma", "city": "Chennai → Meghalaya",
     "image": "https://images.unsplash.com/photo-1500648767791-00dcc994a43e?w=400&q=85&auto=format&fit=crop",
     "rating": 5,
     "quote": "Living root bridges, double-decker waterfalls, and a homestay that fed me the best pork curry of my life. ATLASANDS finds places guidebooks miss."},
]
