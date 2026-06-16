"""100+ Q&A knowledge base for the ATLASANDS AI Concierge with fuzzy keyword matching."""
import re
from difflib import SequenceMatcher

# Each entry has keyword tags (lowercased) and a curated luxury-magazine-style answer.
KNOWLEDGE = [
    # ---------- Greetings & meta ----------
    {"tags":["hi","hello","hey","namaste","good morning","good evening"], "a":"Namaste 🙏 — welcome to ATLASANDS. I'm your AI Concierge, here to design your perfect Indian journey. Where would you like to wander today — Himalayan snows, Kerala backwaters, Rajasthani palaces, or somewhere hidden?"},
    {"tags":["who are you","what are you","about you"], "a":"I'm the ATLASANDS AI Concierge — a digital travel companion trained on hundreds of Indian destinations, budgets and rituals. Ask me anything: from the best season for Spiti, to the cheapest sleeper to Goa, to what to pack for Ladakh in October."},
    {"tags":["help","menu","what can you do","features"], "a":"I can help you with:\n• Destination ideas by mood, season or budget\n• Itinerary skeletons (3, 5, 7, 10 days)\n• Best months & weather for any region\n• Approximate costs and how to save\n• Food, packing, safety and visa basics\n• Hidden gems most travellers miss"},

    # ---------- Best time / weather ----------
    {"tags":["best time","when to visit india","best season india"], "a":"India has three travel windows. **October–March** is the golden season for most of the country — cool, dry, festive. **April–June** is summer; flee to the Himalayas (Ladakh, Spiti, Kashmir, Himachal). **July–September** is monsoon — magical for Kerala, the Western Ghats and Meghalaya, harsh for the plains."},
    {"tags":["best time kashmir","when to visit kashmir","kashmir season"], "a":"Kashmir wears four moods. **April–May** for tulips and almond blossoms, **June–August** for emerald meadows, **September–October** for chinar gold, and **December–February** for snow, Gulmarg gondola and skiing."},
    {"tags":["best time ladakh","when to visit ladakh"], "a":"Ladakh is open by road from **late May to early October**. July and August are warmest and busiest; June and September are the sweet spot. Roads via Manali and Srinagar usually close by mid-October due to snow."},
    {"tags":["best time kerala","when to visit kerala"], "a":"Kerala shines from **September to March**. Monsoon (June–August) is dramatic and romantic — perfect for Ayurveda — but expect heavy rain. Avoid peak Christmas-New Year week for better rates."},
    {"tags":["best time goa","when to visit goa"], "a":"**November to February** is Goa's golden window — perfect beach weather and the famous nightlife in full swing. March is still pleasant. Monsoon (June–September) is hauntingly beautiful but most shacks shut."},
    {"tags":["best time rajasthan","when to visit rajasthan"], "a":"Visit Rajasthan from **October to March**. Days are warm, nights cool, and festivals like Pushkar Camel Fair (Nov) and Jaipur Literature Festival (Jan) animate the cities. April–June is searingly hot."},
    {"tags":["best time himachal","when to visit himachal"], "a":"For snow: **December–February** (Manali, Shimla). For meadows and treks: **April–June**. For Spiti & Lahaul: **June–September** when high passes are open. Monsoon brings landslides — be cautious."},
    {"tags":["best time andaman","when to visit andaman"], "a":"Andaman is best from **October to early May**. The sea is calm, visibility excellent for diving, and skies clear. May–September is monsoon — ferries are unreliable."},
    {"tags":["best time meghalaya","when to visit meghalaya"], "a":"For waterfalls in full roar visit **June–September**, but expect constant rain. For clearer trekking weather and root-bridge hikes, go **October–April**."},
    {"tags":["best time northeast","when to visit northeast india"], "a":"**October to April** is ideal for Assam, Meghalaya, Arunachal, Nagaland and Sikkim — clear skies, festivals (Hornbill in December), and tiger safaris in Kaziranga."},

    # ---------- Budget ----------
    {"tags":["budget india","cost trip india","how much trip cost"], "a":"A comfortable mid-range India trip costs roughly **₹2,500–4,500 per person per day** (hotels, food, transport). Backpackers can manage on **₹1,200–1,800**, while luxury travellers spend **₹15,000+** on heritage palaces and lake-view suites."},
    {"tags":["cheap travel","budget travel","backpacking india"], "a":"Travel cheap by booking **sleeper-class trains** (IRCTC), staying in **Zostel/Goa-style hostels** (₹500–900/night), eating at **local thalis** (₹100–250) and using **state buses or shared cabs**. North India hill stations and Goa off-season are very affordable."},
    {"tags":["budget kashmir","kashmir cost"], "a":"A 5-day Kashmir trip costs around **₹15,000–22,000 per person** including houseboat, Pahalgam/Gulmarg day trips, meals and shared transport. Add ₹5,000 for snow activities in Gulmarg."},
    {"tags":["budget ladakh","ladakh cost"], "a":"7 days in Ladakh runs **₹25,000–35,000 per person** with shared SUV, guesthouses and permits. Solo bikers can do it for less. Add ₹8,000–10,000 for the Pangong + Nubra circuit."},
    {"tags":["budget goa","goa cost"], "a":"A weekend in North Goa: **₹6,000–12,000** depending on the season and hostel vs. boutique stays. Add ₹2,000 for water sports and ₹1,500 for one good seafood dinner with feni cocktails."},
    {"tags":["budget kerala","kerala cost"], "a":"A 6-day Kerala loop (Munnar–Alleppey–Varkala) is around **₹18,000–28,000** with a houseboat night, homestays and meals. Premium houseboats can be ₹15,000+/night alone."},
    {"tags":["budget rajasthan","rajasthan cost"], "a":"A 7-day Jaipur–Jodhpur–Udaipur–Jaisalmer circuit costs **₹20,000–35,000** mid-range. Heritage haveli stays can stretch this to ₹60,000+. Trains between cities are scenic and cheap."},
    {"tags":["save money","money saving","cheaper trip"], "a":"Top tricks: book trains 60 days ahead (Tatkal is pricier), travel **shoulder season** (Mar/Sep/Oct), use **IRCTC food** instead of platform vendors, choose **state-run hotels** (KTDC, RTDC) for clean budget rooms, and **bargain politely** in markets — start at 40%."},

    # ---------- Itineraries ----------
    {"tags":["itinerary 3 days","weekend trip","3 day"], "a":"**3-day micro-escapes:** Goa beaches, Pondicherry French quarter, Rishikesh + Haridwar, Udaipur lakeside, Coorg coffee estates, Hampi ruins, or a Bandhavgarh tiger safari. Three days is perfect for one focused experience, not three cities."},
    {"tags":["itinerary 5 days","5 day trip"], "a":"**5-day routes that sing:** Kashmir (Srinagar–Pahalgam–Gulmarg), Kerala (Kochi–Munnar–Alleppey), Rajasthan (Jaipur–Pushkar–Jodhpur), Himachal (Manali–Solang–Old Manali), or Hampi + Goa combined for ruins-and-beach romance."},
    {"tags":["itinerary 7 days","week long","one week"], "a":"**7-day dreamers:** Ladakh (Leh–Nubra–Pangong–Tso Moriri), Rajasthan grand tour (Jaipur–Jodhpur–Jaisalmer–Udaipur), Kerala (Kochi–Munnar–Thekkady–Alleppey–Varkala), or NE India (Guwahati–Shillong–Cherrapunji–Mawlynnong)."},
    {"tags":["itinerary 10 days","10 day","longer trip"], "a":"**10-day epics:** Golden Triangle + Varanasi + Khajuraho, the entire Konkan coast (Mumbai–Goa–Gokarna–Karwar), Spiti circle from Shimla, or the Andamans deep-dive (Port Blair–Havelock–Neil–Baratang)."},

    # ---------- Hidden gems ----------
    {"tags":["hidden gems","offbeat","unknown places","secret destinations"], "a":"India's best-kept secrets: **Spiti Valley** (cold desert monasteries), **Ziro Valley** (Apatani tribal villages), **Majuli** (world's largest river island), **Chopta** (mini-Switzerland in Uttarakhand), **Dholavira** (Indus civilisation in salt desert), **Mawlynnong** (Asia's cleanest village)."},
    {"tags":["offbeat himalayas","hidden himalayas"], "a":"Skip Manali, choose **Kalpa, Kibber, Pin Valley, Sangla, Chitkul (last Indian village), Munsiyari, Chaukori, or Khirsu**. All offer 7,000-metre views without the crowds."},
    {"tags":["offbeat beaches","hidden beaches"], "a":"Try **Kudle and Om Beach (Gokarna)**, **Tarkarli (Maharashtra)**, **Marari (Kerala)**, **Neil Island (Andaman)**, **Mandvi (Gujarat)** or **Talasari (Odisha)** — all postcards without the crowds."},
    {"tags":["offbeat south india","hidden south"], "a":"Look at **Athirappilly Falls, Vagamon, Valparai, Yelagiri, Belur–Halebidu, Chettinad mansions, and Dhanushkodi** — South India hides some of the country's most cinematic landscapes."},

    # ---------- Food ----------
    {"tags":["food india","famous food","what to eat"], "a":"Eat your way across India: **Delhi chaat, Lucknowi kebabs, Amritsari kulcha, Rajasthani dal-baati-churma, Mumbai vada pav, Goan vindaloo, Hyderabadi biryani, Chettinad chicken, Kerala sadhya, Bengali fish curry, and Assamese pithas**. Each state is a separate cuisine."},
    {"tags":["vegetarian food","vegetarian india"], "a":"India is the world's vegetarian paradise. Try **Gujarati thali (Ahmedabad), South Indian dosa-idli (Chennai), Rajasthani gatte ki sabzi, Banarasi kachori-aloo, Hyderabadi mirchi ka salan**, and the fresh Himachali siddu. Most cities have 90%+ veg-friendly menus."},
    {"tags":["street food","best street food"], "a":"Top street-food cities: **Delhi (Chandni Chowk), Mumbai (Mohammed Ali Road), Kolkata (Park Street kathi rolls), Lucknow (Tunday kebab), Amritsar (Lawrence Road), Hyderabad (Charminar), Jaipur (MI Road) and Indore (Sarafa Bazaar at midnight)**."},
    {"tags":["safe street food","stomach upset"], "a":"Eat where locals queue, choose stalls cooking hot and fresh, avoid pre-cut salads & uncovered chutneys, drink only **sealed bottled water**, and carry ORS sachets. A small probiotic course before the trip helps acclimatise your gut."},
    {"tags":["kashmiri food","kashmir cuisine"], "a":"Kashmiri Wazwan is legendary — try **Rogan Josh, Yakhni, Gushtaba, Tabak Maaz, Kahwa tea with saffron and almonds**, and the heavenly **Sheermal bread**. Vegetarians shouldn't miss **Dum Aloo, Nadru Yakhni** (lotus stem) and **Haak saag**."},
    {"tags":["south indian food","kerala food"], "a":"Kerala's must-eats: **Appam with stew, Karimeen pollichathu (pearl spot fish in banana leaf), Malabar parotta with beef, Puttu-kadala, sadhya banana-leaf feast** and **filter coffee** at any tea stall."},

    # ---------- Transport ----------
    {"tags":["how to travel india","transport india","getting around"], "a":"Within India, **flights** are cheap if booked early (IndiGo, Vistara, Air India), **trains** are scenic and safe (book on irctc.co.in), **state buses & Volvo coaches** connect every town, and apps like **Ola, Uber, Rapido** work in 100+ cities. For mountains, hire a local taxi or shared SUV."},
    {"tags":["train booking","irctc","indian railway"], "a":"Book Indian trains on **irctc.co.in** or the **IRCTC Rail Connect app**. Reservations open 60 days in advance. Tatkal opens 1 day before at 10AM (AC) / 11AM (non-AC). 1AC and 2AC are very comfortable; 3AC is the sweet spot for budget."},
    {"tags":["best train journeys","scenic trains"], "a":"India's most beautiful trains: **Konkan Railway (Mumbai–Mangalore)**, **Kalka–Shimla toy train**, **Darjeeling Himalayan Railway**, **Nilgiri Mountain Railway (Mettupalayam–Ooty)**, **Vivek Express**, and the luxury **Maharajas' Express** and **Palace on Wheels**."},
    {"tags":["domestic flights","cheap flights india"], "a":"Cheapest domestic flights are on **IndiGo** and **Air India Express**, booked 30–60 days ahead. Tuesday/Wednesday flights are usually cheapest. Use **Skyscanner, MakeMyTrip, ixigo** to compare. Carry photo ID — Aadhaar, passport, or driving licence."},
    {"tags":["road trip","self drive","bike trip"], "a":"Legendary Indian road trips: **Manali–Leh Highway**, **Mumbai–Goa Konkan Coast**, **Spiti Loop from Shimla**, **Bangalore–Coorg–Ooty**, **Guwahati–Tawang**, and **Jaipur–Jaisalmer**. Rent bikes from Royal Enfield outlets or apps like Royal Brothers."},

    # ---------- Visa / documents ----------
    {"tags":["visa india","tourist visa","e-visa"], "a":"Most nationalities can get an **Indian e-Visa** at **indianvisaonline.gov.in** — valid 30 days, 1 year or 5 years. Apply 4 days to 4 months before travel. Cost ranges USD 10–80 depending on duration and nationality."},
    {"tags":["documents","what to carry"], "a":"Carry: valid **passport** (6+ months validity), printed **visa & e-tickets**, **vaccination certificate** if asked, an **international debit/credit card**, and **photocopies** kept separately. Indians need only a govt photo ID and confirmed ticket for domestic travel."},
    {"tags":["permit ladakh","inner line permit","ladakh permit"], "a":"Indian citizens need an **Inner Line Permit (ILP)** for Pangong, Nubra, Tso Moriri etc. — apply at the DC office in Leh or online at **lahdclehpermit.in**. Foreign nationals need a **Protected Area Permit (PAP)**, easily arranged via travel agents in Leh."},
    {"tags":["permit sikkim","permit arunachal","permit northeast"], "a":"**Sikkim**: free ILP at the border (Rangpo) or major airports for Indians; foreigners need PAP. **Arunachal Pradesh**: ILP mandatory for all — apply online at **arunachalilp.com**. **Nagaland & Mizoram**: ILP required for Indians too."},

    # ---------- Packing & safety ----------
    {"tags":["what to pack","packing list"], "a":"Universal packing: lightweight cottons, one warm layer (even for tropical India in winter), comfortable walking shoes, sandals, a refillable water bottle, sunscreen SPF 50, sunglasses, mosquito repellent, a power bank, universal adapter (Type C/D/M), and ORS sachets. Add thermals for mountains."},
    {"tags":["packing ladakh","packing himalayas","cold weather packing"], "a":"For Ladakh/Himalayas above 3,000 m: thermals, fleece, down jacket, windproof shell, warm gloves, woollen socks, sunglasses (UV high), SPF 50, lip balm, **Diamox** for altitude sickness (consult doctor), and chocolate/dry fruits for energy."},
    {"tags":["packing kerala","packing monsoon"], "a":"For tropical/monsoon India: quick-dry shirts, light cottons, rain jacket or compact umbrella, waterproof shoes/sandals, dry-bag for electronics, mosquito repellent (DEET 20%+), and Imodium/ORS for the inevitable food adventures."},
    {"tags":["safety india","is india safe","safe to travel"], "a":"India is generally safe for tourists. Use registered cabs (Ola/Uber), avoid empty streets at night, keep valuables in hotel safes, and trust your instincts. Solo female travellers should prefer day trains, women-only train compartments, and stay in well-reviewed hostels/hotels."},
    {"tags":["solo female travel","safe for women"], "a":"India is increasingly welcoming for solo female travellers. Safer regions: **Kerala, Goa, Himachal, Sikkim, Karnataka, Pondicherry**. Wear modest clothing at religious sites, avoid late-night solo walks in big cities, and use trusted hostel chains like **Zostel** and **The Hosteller**."},
    {"tags":["altitude sickness","mountain sickness","ams"], "a":"Above 3,500 m (Leh, Khardung La, Spiti) altitude sickness is real. **Acclimatise** for 24–48 hrs in Leh before high passes, **hydrate** heavily, avoid alcohol on day 1, walk slowly, and consider **Diamox** (consult your doctor). Descend immediately if symptoms worsen."},
    {"tags":["emergency","helpline","police"], "a":"All-India emergency number: **112**. Police: 100, Ambulance: 102, Tourist helpline: **1363** (multi-lingual). Save your country embassy/consulate in Delhi as well. Indian tourist police booths exist at major sites."},

    # ---------- Sim / money / connectivity ----------
    {"tags":["sim card","mobile india","internet"], "a":"Get a **Jio**, **Airtel** or **Vi** tourist SIM at any major airport. Prepaid plans start at ₹239/28 days for 1.5GB/day + calls. Bring passport, visa and one photo. 4G/5G is excellent in cities; patchy in Spiti/Ladakh/NE remote areas."},
    {"tags":["money exchange","currency india","atm"], "a":"India uses the **Indian Rupee (₹)**. ATMs are everywhere in cities; carry ₹2,000–5,000 cash for rural areas. Forex counters at airports give fair rates; avoid hotel exchanges. **UPI/Paytm/GPay** dominate — most stalls accept QR payments."},
    {"tags":["credit card","cards accepted"], "a":"Visa/Mastercard are widely accepted in hotels, restaurants and chains. American Express is patchy. Inform your bank before travel to avoid blocks. Always carry some cash — small towns, autos and roadside dhabas still prefer it."},
    {"tags":["tipping india","tips"], "a":"Tipping is appreciated but not mandatory. **Restaurants**: 5–10% if no service charge. **Hotel staff**: ₹50–100 per bag. **Drivers/guides**: ₹200–500/day for good service. In temples, small donations to priests/pujaris are customary."},

    # ---------- Activities ----------
    {"tags":["trekking india","best treks","hiking"], "a":"India's iconic treks: **Hampta Pass, Kheerganga, Chadar (frozen river), Roopkund (skeleton lake), Valley of Flowers, Goecha La (Sikkim), Sandakphu, Tarsar Marsar (Kashmir), Markha Valley (Ladakh)**. Book via verified operators like **Indiahikes** or **Bikat Adventures**."},
    {"tags":["scuba diving","snorkeling","water sports"], "a":"Best scuba: **Havelock & Neil (Andaman)** — clearest water, certified PADI shops. Other options: **Murudeshwar, Netrani Island, Pondicherry, Goa (Grande Island)**. Best season: November to April."},
    {"tags":["yoga","meditation","ayurveda"], "a":"Spiritual hubs: **Rishikesh** (yoga capital), **Kerala** (Ayurveda — Kovalam, Varkala, Kollam), **Mysore** (Ashtanga yoga), **Bodh Gaya** (Vipassana meditation), and **Auroville/Pondicherry** for integral living."},
    {"tags":["wildlife safari","tiger safari"], "a":"Top tiger reserves: **Bandhavgarh & Kanha (MP)** — highest tiger density, **Ranthambore (Rajasthan)** — fort + tigers, **Tadoba (Maharashtra)**, **Jim Corbett (Uttarakhand)**, **Sundarbans (WB)**. Book safaris on **mponline.gov.in** or via lodges 90+ days ahead."},
    {"tags":["festivals india","best festivals"], "a":"Iconic festivals to plan around: **Diwali (Oct/Nov)** — lights everywhere, **Holi (Mar)** — colours in Mathura/Vrindavan, **Durga Puja (Oct)** in Kolkata, **Pushkar Camel Fair (Nov)**, **Hornbill (Dec)** in Nagaland, **Onam (Aug/Sep)** in Kerala, **Rann Utsav (Nov–Feb)** in Gujarat."},

    # ---------- Specific destinations Q&A ----------
    {"tags":["taj mahal","agra"], "a":"The Taj Mahal opens at **sunrise** (the most magical hour) and closes at sunset. Closed on **Fridays**. Tickets ₹1,100 for foreigners, ₹50 for Indians. Don't miss **Mehtab Bagh** across the Yamuna for the sunset reflection shot."},
    {"tags":["varanasi","banaras","kashi"], "a":"In Varanasi, take a **dawn boat ride** on the Ganga, attend the **Ganga Aarti at Dashashwamedh Ghat** at sunset (arrive 30 min early), wander Vishwanath gali at night, and try **kachori-sabzi, Banarasi paan, and malaiyo** in winter."},
    {"tags":["hampi","vijayanagara"], "a":"Hampi is best explored over **2–3 days by bicycle or moped**. Sunrise at **Matanga Hill**, sunset at **Hemakuta Hill**. Don't miss **Vittala Temple's musical pillars and stone chariot**, **Virupaksha Temple**, and a coracle ride at Sanapur Lake."},
    {"tags":["pushkar","pushkar camel fair"], "a":"Pushkar's lake and Brahma Temple are open year-round, but the **Pushkar Camel Fair (Nov)** is unmissable — 50,000 traders, folk performances, hot-air balloons. Stay at a haveli in the old town."},
    {"tags":["rann of kutch","white desert"], "a":"The **Rann Utsav** runs from November to February — a tent-city festival on the salt flats. **Full-moon nights** turn the desert silver. Pair with **Bhuj** (handicrafts), **Mandvi beach**, and **Dholavira** (Indus civilisation ruins)."},
    {"tags":["spiti valley","spiti"], "a":"Best done as a **7–10 day loop**: Shimla → Kalpa → Tabo → Dhankar → Kaza → Kibber/Komic → Chandratal → Manali. Roads from Manali side open only June–October. Carry cash; ATMs are scarce. Drink lots of water for altitude."},
    {"tags":["valley of flowers"], "a":"**Valley of Flowers** trek is open **July to early September** only — peak bloom is **late July to mid-August**. Base at Govindghat, trek via Ghangaria (13 km). Combine with **Hemkund Sahib** at 4,329 m."},
    {"tags":["dharamshala","mcleodganj"], "a":"Mcleodganj sits above Dharamshala — **Tsuglagkhang complex** (Dalai Lama's residence), **Bhagsu falls**, **Triund trek** (sunrise above the clouds), and **Norbulingka** for Tibetan art. Best months: Mar–Jun & Sep–Nov."},
    {"tags":["alleppey","backwaters","houseboat"], "a":"A **24-hr houseboat from Alleppey** (₹8,000–25,000) drifts through 900 km of palm-lined canals. Book a 1-bedroom premium boat for romance. Best season: Sep–Mar. Combine with Marari beach for a 2-day slow escape."},
    {"tags":["munnar","tea estates"], "a":"In Munnar, stay at a **plantation bungalow** (Tea County, Windermere). Walk **Top Station, Echo Point, Eravikulam (Nilgiri tahr), and Kolukkumalai** — the world's highest tea estate. Best months: Sep–May."},

    # ---------- Eco / responsible travel ----------
    {"tags":["eco travel","responsible travel","sustainable"], "a":"Travel light on the planet: refill bottles (carry a LifeStraw or steel bottle), avoid single-use plastic, support **homestays over chains** in mountain villages, stay on marked trails (especially Valley of Flowers, Spiti), and tip local guides directly."},
    {"tags":["plastic ban","plastic free"], "a":"Sikkim, Himachal Pradesh and many hill stations have **strict plastic bans**. Carry your own cloth bag and steel water bottle. Plastic bottles are confiscated at the entry to Tirthan, Sikkim parks and many Buddhist monasteries."},

    # ---------- Couple / family / solo ----------
    {"tags":["honeymoon india","honeymoon"], "a":"Iconic Indian honeymoons: **Andaman beaches**, **Kerala backwaters**, **Udaipur lake palaces**, **Coorg coffee estates**, **Sikkim & Darjeeling**, **Kashmir houseboat**, **Goa private villa**. Mix one beach + one mountain destination for variety."},
    {"tags":["family trip","with kids","kids friendly"], "a":"Family-friendly picks: **Goa, Kerala (Wonderla + houseboat), Jaipur (forts + elephants), Coorg, Mysore (palace + zoo), Ooty (toy train), Andaman (calm beaches)**. Avoid Ladakh with children under 10 due to altitude."},
    {"tags":["solo travel","solo trip"], "a":"Top solo trips: **Rishikesh, Pondicherry, Kasol-Tosh, Hampi, Goa, Varkala, McLeodganj, Spiti (with shared cab)**. Stay at Zostel/Hosteller for instant community. Carry a journal — India will give you material."},

    # ---------- Generic fallback / clarifiers ----------
    {"tags":["thanks","thank you","appreciated"], "a":"It's my pleasure. May your journey through India be everything you hoped — and a few wonderful things you didn't expect. Tell me where you'd like to go next, and I'll begin shaping the itinerary."},
    {"tags":["bye","goodbye","see you"], "a":"Safe travels, wanderer. Whenever the road calls again, the ATLASANDS lounge is open. 🌍"},
    {"tags":["beach","beaches","ocean","sea"], "a":"India's finest beaches: **Radhanagar (Havelock)**, **Varkala (Kerala)**, **Palolem (Goa South)**, **Om Beach (Gokarna)**, **Marari (Kerala)**, **Mandvi (Gujarat)**, **Tarkarli (Maharashtra)** and **Lakshadweep atolls** for true paradise."},
    {"tags":["mountains","mountain","trek","hills"], "a":"For Himalayan magic: **Ladakh, Spiti, Kashmir, Sikkim, Tawang**. For greener slopes: **Coorg, Munnar, Ooty, Wayanad**. For colonial hill stations: **Shimla, Darjeeling, Kodaikanal, Mussoorie**."},
    {"tags":["snow","snowfall","skiing"], "a":"Best snow experiences: **Gulmarg** (skiing, gondola), **Auli** (slopes + Nanda Devi views), **Manali–Solang**, **Sandakphu** (Singalila trek), and **Tawang** in deep winter."},
    {"tags":["desert","sand","camel"], "a":"India has two great deserts: **Thar (Rajasthan)** — Jaisalmer dunes, camel safaris, desert camps; and **White Rann of Kutch (Gujarat)** — salt flats that turn silver under the moon during Rann Utsav."},
    {"tags":["temple","temples","spiritual"], "a":"Spiritual circuits: **Char Dham** (Yamunotri, Gangotri, Kedarnath, Badrinath) in Uttarakhand; **Golden Temple** (Amritsar); **Tirupati** (Andhra); **Madurai Meenakshi**; **Jagannath Puri**; **Somnath/Dwarka** (Gujarat); **Bodh Gaya** for Buddhists."},
    {"tags":["wildlife","animals","tiger","leopard","elephant"], "a":"Top wildlife parks: **Kaziranga** (one-horned rhino), **Gir** (Asiatic lion), **Bandhavgarh & Kanha** (tigers), **Sundarbans** (Bengal tigers in mangroves), **Periyar** (elephants), **Nagarhole**, **Tadoba**, **Jim Corbett**."},
    {"tags":["adventure sports","adrenaline","extreme"], "a":"Adrenaline India: **Bungee at Rishikesh** (83 m), **paragliding at Bir-Billing**, **rafting on the Ganga & Zanskar**, **scuba in Havelock**, **skiing in Gulmarg**, **chadar trek**, **biking Manali–Leh**, and **trekking Stok Kangri**."},
    {"tags":["water sports","rafting","kayaking"], "a":"For white water, head to **Rishikesh (Ganges Grade III–IV)** and the **Zanskar river (Grade IV–V, Sep)**. Kayaking & SUP: **Goa lagoons, Kerala backwaters**. Surf: **Mulki, Varkala, Kovalam**."},
    {"tags":["nightlife","party","clubs"], "a":"Best Indian nightlife: **Goa** (Tito's lane, Curlies, Sinq), **Bangalore** (Indiranagar pubs, craft beer), **Mumbai** (Bandra, Lower Parel), **Delhi** (Hauz Khas, Aerocity), **Pune** (Koregaon Park)."},
    {"tags":["shopping india","shopping","markets"], "a":"Best shopping: **Jaipur** (block prints, jewellery, blue pottery), **Delhi** (Dilli Haat, Khan Market), **Mumbai** (Colaba Causeway, Linking Road), **Mysore** (silk + sandalwood), **Varanasi** (Banarasi sarees), **Pondicherry** (Auroville crafts)."},
    {"tags":["luxury hotels","best hotels","palace hotels"], "a":"Iconic luxury stays: **Taj Lake Palace (Udaipur)**, **Umaid Bhawan (Jodhpur)**, **Rambagh Palace (Jaipur)**, **The Oberoi Amarvilas (Agra)**, **Wildflower Hall (Shimla)**, **Taj Falaknuma (Hyderabad)**, **Ananda in the Himalayas (Rishikesh)**."},
    {"tags":["budget hotels","cheap stay","hostels"], "a":"Reliable budget chains: **Zostel** and **The Hosteller** (₹500–1,200/night dorms), **OYO** (private rooms from ₹800), **Treebo & FabHotels** (mid-range), and **RTDC/KTDC** state-run heritage hotels (often great value)."},
    {"tags":["homestays","stay with locals"], "a":"India's best homestays: **Kerala backwaters (Marari, Kumarakom)**, **Coorg coffee estates**, **Sikkim villages (Yuksom)**, **Spiti valley (Komic, Langza)**, **Kumaon (Munsiyari, Kasar Devi)**, **Wayanad plantations**. Book via **NotOnMap, Airbnb, Bookalokal**."},
    {"tags":["language","languages india","english"], "a":"India has 22 official languages and 100s of dialects. **English is widely spoken** in hotels, restaurants and tourist sites. **Hindi** is helpful in the north. Learn a few words: namaste (hello), dhanyavaad (thank you), kitna (how much), accha (good)."},
    {"tags":["scams","tourist scams","cheating"], "a":"Common scams to avoid: **fake government tourist offices** near New Delhi Railway Station, **'closed hotel' rickshaw scam**, **gem export scams in Jaipur**, **overpriced taxis from airports** (use prepaid counters), and **'free' temple tours** that end with donation pressure."},
    {"tags":["camera","photography","best photo spots"], "a":"Top photo destinations: **Taj Mahal sunrise**, **Hampi boulders sunset**, **Pangong Lake**, **Varanasi ghats at dawn**, **Jaisalmer dunes**, **Munnar tea estates**, **Athirappilly falls**, **Hawa Mahal facade**, **Mawlynnong root bridges**, **Spiti night sky**."},
    {"tags":["solo female ladakh","women ladakh"], "a":"Ladakh is one of the safest regions in India for solo women. Stay in homestays in Leh (lots of female travellers), join group SUVs for Pangong/Nubra (split costs + safer), and acclimatise 2 days before any high-altitude drive."},
    {"tags":["best month october","october travel"], "a":"October is **the best travel month in India**. Monsoon has cleared, festivals begin, the weather is golden everywhere except very high Himalayas. Top picks: **Ladakh (last week of season), Kashmir (chinar gold), Rajasthan, Kerala, Goa (shoulder)**."},
    {"tags":["best month december","december travel","winter travel"], "a":"December is **peak winter** — perfect for Rajasthan, Kerala, Goa, the South, Andaman. Snow seekers head to **Gulmarg, Auli, Manali, Tawang**. Avoid high Himalayas (closed). Festive: Christmas in Goa, Hornbill in Nagaland."},
    {"tags":["best month july","monsoon travel"], "a":"July is monsoon — head to **Kerala (Ayurveda)**, **Valley of Flowers (Uttarakhand)**, **Meghalaya (waterfalls)**, **Coorg & Wayanad (green ghats)**, **Ladakh & Spiti (high passes open)**. Avoid Mumbai-Goa-Konkan unless you love rain."},
    {"tags":["airport india","main airports"], "a":"Major international airports: **Delhi (DEL), Mumbai (BOM), Bangalore (BLR), Chennai (MAA), Hyderabad (HYD), Kochi (COK), Kolkata (CCU), Goa (GOI/GOX)**. All have prepaid taxi counters and metro/airport-express trains in metros."},
    {"tags":["chai","tea","coffee"], "a":"India runs on chai — **masala chai** with ginger, cardamom and milk. South India loves **filter coffee** (Madras Coffee House, Indian Coffee House chains). Try **Kashmiri Kahwa**, **Tibetan Po cha**, **Sulaimani (Kerala)** for variety."},
    {"tags":["weather february","february travel"], "a":"February is **brilliant for South India, Rajasthan, Goa, Andaman, Kutch, Madhya Pradesh tigers, Khajuraho**. Cooler nights, perfect day temperatures. Snow lovers head to Gulmarg, Auli, Manali."},
    {"tags":["weather may","may travel","summer travel"], "a":"May is hot on the plains — escape to **Himalayas**: Kashmir, Ladakh (open), Spiti, Himachal, Sikkim, Tawang. Or to **South Indian hill stations**: Munnar, Ooty, Kodaikanal, Coorg."},
    {"tags":["sea food","seafood india"], "a":"Best seafood coasts: **Goa** (prawn balchão, fish recheado, crab xec xec), **Kerala** (karimeen, prawn moilee, Mappila biryani), **Mangalore** (neer dosa with fish curry), **Mumbai** (Bombay duck, Koli prawn curry), **Bengal** (ilish bhapa, chingri malai curry)."},
    {"tags":["pets","dog friendly","travel with dog"], "a":"Pet-friendly destinations: **Goa (most beach shacks allow dogs)**, **Coorg & Wayanad homestays**, **Lonavala**, **Mussoorie**, **Mahabaleshwar**. Use **Treebo Pet-Friendly** or **OYO Townhouse** filters. Carry vaccination card."},
    {"tags":["best aurora","stars","night sky","astrophotography"], "a":"India's darkest skies: **Spiti Valley (Kibber, Komic)**, **Ladakh (Hanle observatory — India's first Dark Sky Reserve)**, **Rann of Kutch**, **Coorg**, **Munsiyari**. Best months: Oct–Mar with new moon nights."},
    {"tags":["responsible tourism","ethics","local"], "a":"Travel that helps: stay at **family homestays**, eat at **local kitchens**, hire **local guides**, buy from **artisan cooperatives**, avoid elephant rides and dolphin shows, and respect dress codes at religious sites."},
    {"tags":["dress code","what to wear","clothing"], "a":"Casual cottons work everywhere. Cover shoulders/knees at **temples, mosques, gurdwaras and dargahs**. Carry a scarf for sun and modesty. Beaches and resorts are relaxed; small towns are conservative. Remove shoes before entering homes and most religious sites."},
    {"tags":["plug socket","electricity","adapter"], "a":"India uses **230V, 50Hz** with Type C, D and M sockets. A **universal travel adapter** works fine. Most laptops/phones auto-handle 230V. Carry a power bank — long train journeys and trek days drain devices quickly."},
    {"tags":["customs","what to bring","duty free"], "a":"You can bring 2L alcohol, 100 cigarettes (or 25 cigars), gifts under USD 100, and personal electronics duty-free. Declare cash over USD 5,000 or equivalent. Drone permits are strict — apply via **DGCA Digital Sky** if bringing one."},

    # ---------- Foody specifics ----------
    {"tags":["mithai","sweets india","indian dessert"], "a":"Indian sweets to chase: **Mysore Pak, Rasgulla (Bengal), Mishti Doi, Soan Papdi, Jalebi, Gulab Jamun, Petha (Agra), Bal Mithai (Kumaon), Pootharekulu (Andhra), Belgaum Kunda**. A different mithai for every state."},
    {"tags":["spices","masala","indian spices"], "a":"Indian kitchens revolve around **turmeric, cumin, coriander, cardamom, cloves, cinnamon, mustard, fenugreek, garam masala, and asafoetida (hing)**. Buy fresh whole spices at Khari Baoli (Delhi), Devaraja Market (Mysore), or Pydhonie (Mumbai)."},
    {"tags":["alcohol india","drinking laws","dry state"], "a":"Drinking age varies by state: 18 (Goa, Sikkim, Puducherry), 21 (most), 25 (Delhi, Maharashtra). **Dry states**: Gujarat, Bihar, Mizoram, Nagaland — bring a permit or skip. Try **Indian craft beer (Bira, Simba), feni (Goa), local toddy (Kerala), and Indian single malts (Amrut, Paul John)**."},
]


def _normalize(s: str) -> str:
    return re.sub(r"[^a-z0-9\s]", " ", s.lower()).strip()


def _score(query: str, tags: list[str]) -> float:
    q = _normalize(query)
    q_words = set(q.split())
    best = 0.0
    for tag in tags:
        t = _normalize(tag)
        if not t:
            continue
        t_words = t.split()
        n = len(t_words)
        t_set = set(t_words)
        # All tag words appear in query — strong, scaled by tag length (specificity)
        if t_set.issubset(q_words):
            score = 0.80 + min(0.18, 0.06 * n)
            # Phrase contiguous match (e.g. "best time kashmir" appears as substring): bonus
            if n >= 2 and f" {t} " in f" {q} ":
                score = min(1.0, score + 0.05)
            best = max(best, score)
            continue
        # Partial overlap (some tag words match)
        overlap = len(q_words & t_set) / max(1, n)
        ratio = SequenceMatcher(None, q, t).ratio()
        best = max(best, 0.55 * overlap + 0.35 * ratio)
    return best


def find_best_answer(query: str) -> tuple[str, float]:
    """Return (answer, confidence). Confidence in [0,1]."""
    if not query or not query.strip():
        return ("Tell me what you're dreaming about — a region, a season, a budget, or a mood — and I'll begin.", 0.2)
    ranked = []
    for entry in KNOWLEDGE:
        s = _score(query, entry["tags"])
        if s > 0:
            ranked.append((s, entry["a"]))
    if not ranked:
        return (_fallback(query), 0.0)
    ranked.sort(key=lambda x: x[0], reverse=True)
    top_score, top_answer = ranked[0]
    if top_score < 0.32:
        return (_fallback(query), top_score)
    return (top_answer, top_score)


def _fallback(query: str) -> str:
    return (
        "That's an interesting one. I might not have a precise script for it yet — but here's how I can help right now:\n\n"
        "• Ask about a **state or destination** (e.g. *Kerala, Ladakh, Goa, Rajasthan, Sikkim*)\n"
        "• Ask about a **season or month** (e.g. *best month for Kashmir*, *July travel*)\n"
        "• Ask about a **budget** (e.g. *budget Kerala trip*, *cheap travel*)\n"
        "• Ask about a **mood** (e.g. *honeymoon*, *solo travel*, *adventure*, *spiritual*)\n\n"
        "Or open the **Trip Architect** from the menu — give me dates, budget and vibe, and I'll design a day-by-day itinerary."
    )


SUGGESTED_QUESTIONS = [
    "Best time to visit Kashmir",
    "Budget trip to Kerala in 5 days",
    "Hidden gems in Himachal Pradesh",
    "Honeymoon destinations in India",
    "What to pack for Ladakh in September",
    "Best street food in India",
    "Solo female travel safety tips",
    "Cheapest way to see Rajasthan",
    "Top wildlife safaris in India",
    "Goa or Andaman — which is better?",
]
