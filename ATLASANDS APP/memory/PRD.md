# PRD — ATLASANDS · Your World, Your Way

## Original problem statement
Build a luxury AI-powered Indian travel platform called **ATLASANDS** with tagline **"Your World, Your Way."** — full-stack experience covering homepage, AI Concierge, Trip Architect, Budget Intelligence, Smart Packing, Hidden Worlds, Culinary Journey, Memory Journal. Premium design (Playfair / Cormorant / Inter), cinematic hero, dark luxury palette with champagne gold accents, 50+ Indian destinations, glassmorphism, animations.

**User constraints** (explicit choices):
- Platform: Streamlit only (deployable via GitHub + Streamlit Cloud)
- AI Concierge: 100% static 100+ Q&A knowledge base (no LLM API dependency)
- Scope: Full app (8 pages) for first version
- Auth: Email/password with JWT-style session

## Architecture & stack
- **Frontend & Backend**: Streamlit 1.40+ (single Python app, multipage)
- **Database**: SQLite (file-based, zero setup) — users, favorites, trips, journals, chat_history
- **Auth**: bcrypt password hashing + PyJWT session tokens (14-day TTL) in `st.session_state`
- **Charts**: Plotly (donut chart for budget)
- **Styling**: 700+ lines of custom CSS with Playfair Display + Cormorant Garamond + Inter, glassmorphism, Ken Burns hero animation, gold/cream palette
- **Images**: 37 verified Unsplash India-themed photo IDs (all return HTTP 200), assigned per category
- **Knowledge base**: 111 curated Q&A entries with weighted keyword + phrase matching (no external API)

## What's implemented (2026-02-16)
- ✅ Homepage with Ken Burns cinematic hero, AI orb teaser, 8 destination preview cards, 11 feature pills, 4-day timeline, animated stats, 4 testimonials, luxury footer
- ✅ Destinations page — 61 curated Indian places with search/filter by name, state, category, sort by budget
- ✅ AI Concierge with floating gold orb, 10 suggested-question pills, chat transcript, 111 Q&A backend
- ✅ Trip Architect — deterministic itinerary engine (day-by-day with morning/afternoon/evening/stay/food), saves to user account, JSON export
- ✅ Budget Intelligence — interactive Plotly donut, affordability score (0–100), 6 savings tips
- ✅ Smart Packing — season+activity-aware checklist (10+ base + 8–10 category-specific items), progress bar, text download
- ✅ Hidden Worlds — editorial storytelling for 10 lesser-known Indian destinations
- ✅ Culinary Journey — 6 regional Indian cuisines (North, South, East, West, NE, Kashmiri Wazwan)
- ✅ Memory Journal — login-required, auto-generates editorial-style stories from raw entries
- ✅ Email/password auth with bcrypt + JWT-style sessions
- ✅ Complete README.md with Streamlit Cloud deployment instructions
- ✅ `.gitignore`, `secrets.toml.example`, `requirements.txt`

## File map
```
/app/streamlit_app/
├── app.py                              Homepage
├── requirements.txt                    Streamlit + bcrypt + PyJWT + plotly + Pillow
├── README.md                           Deployment guide
├── .gitignore
├── .streamlit/
│   ├── config.toml                     Dark luxury theme
│   └── secrets.toml.example            JWT secret template
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
    ├── styles.py                       700+ lines of premium CSS
    ├── destinations.py                 61 destinations, 8 categories, verified Unsplash images
    ├── knowledge_base.py               111 Q&A entries, fuzzy keyword matcher
    ├── trip_engine.py                  Itinerary, packing, budget, journal generators
    ├── content.py                      6 culinary regions, 10 hidden worlds, testimonials
    ├── auth.py                         bcrypt + JWT session helpers
    └── database.py                     SQLite schema + connection helpers
```

## Verification done
- All 9 routes return HTTP 200
- Auth: signup/login/wrong-password verified programmatically
- Knowledge base: 111 entries, scoring tested on 14 representative queries (>90% return correct answers)
- Itinerary generation: deterministic, produces day-by-day plan
- Budget engine: 4 styles × adjusted weights, total matches input
- Packing generator: 22 items for 7-day mountain trip
- Visual verification: hero (Manali Himalayas), Destinations (Taj Mahal), AI Concierge (snowy peaks), Trip Architect (Goa beach) — all rendered cinematically with elegant typography

## Backlog (P1)
- Floating chat orb on home (not just on Concierge page)
- Save favourites action on destination cards
- Light-mode toggle (currently dark-only)
- Lottie animations for hero loading
- Multi-image carousel for hero instead of single image

## Backlog (P2)
- Real LLM integration (Emergent Universal Key) with 100 Q&A fallback
- Newsletter signup capturing emails to SQLite
- Social sharing meta tags for itineraries
- PDF export of itineraries
- Google Translate for international visitors

## Known limitations
- Streamlit cannot replicate the full cinematic React experience of the reference site (cinematic-trips-4.emergent.host). Best possible within Streamlit's iframe-based component model.
- SQLite is ephemeral on Streamlit Cloud's free tier (resets on container restart). For persistence in production, migrate to Postgres (Supabase/Neon free tier) — code changes localised to `utils/database.py`.

## Updates (2026-02-16, iteration 2 — P1 features)
- ✅ **Floating AI Concierge orb on every page** (bottom-right, breathing animation, gold glow, hover tooltip, navigates to Concierge)
- ✅ **Light/Dark mode toggle** (in sidebar; persists in session; full luxury light palette with ivory bg, deep navy text, gold accents)
- ✅ **Save-to-favourites** on destination cards (♡ button; toggles state; new sort option "♡ Favourites first"; saved-count badge & list shown in Destinations sidebar)
- ✅ New "favorites" SQLite table populated via `toggle_favorite(user_id, destination_id)`
- ✅ Theme-aware CSS variables (40+) — all components automatically respond to theme switch
