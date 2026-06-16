# 🌍 ATLASANDS — Your World, Your Way

A luxury AI-powered Indian travel platform, built end-to-end in **Streamlit**.

> Live preview locally: `streamlit run app.py`
> Deploy free in 5 minutes via **GitHub + Streamlit Community Cloud**.

---

## ✨ What's inside

| Feature | Description |
|---|---|
| 🏠 **Cinematic Homepage** | Full-screen Ken Burns hero, 50+ destinations preview, glass-morphism stats, testimonial gallery |
| 🌍 **Destinations** | 50+ curated Indian destinations with filters by category, name, budget |
| 🤖 **AI Concierge** | 100+ curated Q&A static knowledge base — works **forever, offline, never fails** |
| 🗺️ **Trip Architect** | Day-by-day itinerary generator (deterministic engine — no LLM key required) |
| 💰 **Budget Intelligence** | Interactive Plotly donut chart, breakdown, savings tips, affordability score |
| 🎒 **Smart Packing** | Season + activity-aware checklist with progress tracker & download |
| 🌿 **Hidden Worlds** | Editorial storytelling for 10 lesser-known Indian places |
| 🍲 **Culinary Journey** | Regional Indian food atlas (6 cuisines) |
| 📖 **Memory Journal** | Save trip memories; auto-weave editorial-style stories |
| 🔐 **Auth** | Email/password with bcrypt + JWT session, SQLite storage |

---

## 🚀 Quick start (local)

```bash
cd streamlit_app
pip install -r requirements.txt
streamlit run app.py
```

Open `http://localhost:8501` — that's it.

---

## ☁️ Deploy free on Streamlit Cloud (via GitHub)

### Step 1 — Push to GitHub

```bash
cd streamlit_app
git init
git add .
git commit -m "ATLASANDS · initial commit"
git branch -M main
git remote add origin https://github.com/<your-username>/atlasands.git
git push -u origin main
```

### Step 2 — Deploy

1. Visit **https://share.streamlit.io**
2. Sign in with GitHub
3. Click **"New app"**
4. Fill:
   - **Repository**: `your-username/atlasands`
   - **Branch**: `main`
   - **Main file path**: `app.py`
5. Click **"Advanced settings"** → **"Secrets"** and paste:
   ```toml
   JWT_SECRET = "paste-a-long-random-string-here-min-32-chars"
   APP_NAME = "ATLASANDS"
   ```
6. Click **Deploy** 🚀

In ~2 minutes you'll have a URL like `https://atlasands-xxxxx.streamlit.app`.

### Step 3 — Custom domain (optional)

Streamlit Cloud lets you set a custom domain in Settings → Custom Domains.

---

## 🗂️ Project structure

```
streamlit_app/
├── app.py                      # Homepage (cinematic hero, destinations, features)
├── requirements.txt
├── README.md
├── .streamlit/
│   ├── config.toml             # Theme (dark luxury)
│   └── secrets.toml.example    # JWT secret template
├── pages/
│   ├── 1_Destinations.py
│   ├── 2_AI_Concierge.py
│   ├── 3_Trip_Architect.py
│   ├── 4_Budget_Intelligence.py
│   ├── 5_Smart_Packing.py
│   ├── 6_Hidden_Worlds.py
│   ├── 7_Culinary_Journey.py
│   └── 8_Memory_Journal.py
└── utils/
    ├── styles.py               # 700+ lines of premium CSS injection
    ├── destinations.py         # 50+ destinations data
    ├── knowledge_base.py       # 100+ Q&A for AI Concierge
    ├── trip_engine.py          # Itinerary / packing / budget / journal engines
    ├── content.py              # Culinary, hidden worlds, testimonials
    ├── auth.py                 # bcrypt + JWT session auth
    └── database.py             # SQLite schema & helpers
```

---

## 🔒 Why this won't break

- **No external LLM API** — the AI Concierge uses a curated 100+ Q&A with fuzzy keyword matching. It will **never** return an API error.
- **No paid integrations** — everything works on Streamlit Cloud's free tier.
- **No database setup** — SQLite file is created automatically.
- **High-res Unsplash images** — embedded via CDN URLs, no asset uploads.

---

## 🛠️ Customise

| Want to change… | Edit |
|---|---|
| Add a destination | `utils/destinations.py` → `DESTINATIONS` list |
| Add a Q&A | `utils/knowledge_base.py` → `KNOWLEDGE` list |
| Change colours / fonts | `utils/styles.py` (CSS variables at top) |
| Add a culinary region | `utils/content.py` → `CULINARY` list |
| Add a hidden world | `utils/content.py` → `HIDDEN_WORLDS` list |

---

## 📜 License

Crafted for personal & commercial use. Travel responsibly.

— ATLASANDS · Your World, Your Way · 2026
