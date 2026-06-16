"""Trip Architect — AI itinerary generator (deterministic, no LLM needed)."""
import json
from datetime import date
import streamlit as st
from utils.styles import inject_global_styles, hero, section_header, render_floating_orb
from utils.destinations import DESTINATIONS, HERO_SLIDES
from utils.trip_engine import generate_itinerary, budget_breakdown, affordability_score, date_range
from utils.auth import ensure_session
from utils.database import get_conn, init_db, now_iso

st.set_page_config(page_title="Trip Architect · ATLASANDS", page_icon="🗺️", layout="wide", initial_sidebar_state="collapsed")
inject_global_styles()
init_db()
render_floating_orb()
user = ensure_session()

hero(
    image_url=HERO_SLIDES[2]["image"],
    eyebrow="TRIP ARCHITECT",
    title_html="Tell Me The Vibe.<br/>I'll Compose The Days.",
    subtitle="A few quiet questions. One cinematic itinerary. Designed for your dates, your budget, your soul.",
)

st.markdown('<div style="height: 26px;"></div>', unsafe_allow_html=True)

with st.container():
    st.markdown('<div class="eyebrow">Step 1 · Choose your destination</div>', unsafe_allow_html=True)
    dest_options = [f"{d['name']} ({d['state']}) — {d['category']}" for d in DESTINATIONS]
    dest_idx = st.selectbox("Destination", range(len(dest_options)), format_func=lambda i: dest_options[i], key="ta_dest")
    chosen = DESTINATIONS[dest_idx]

st.markdown('<div class="gold-divider"></div>', unsafe_allow_html=True)

with st.container():
    st.markdown('<div class="eyebrow">Step 2 · Shape the journey</div>', unsafe_allow_html=True)
    c1, c2, c3 = st.columns(3)
    with c1:
        start_city = st.text_input("Starting from", value="Delhi", key="ta_origin")
        start_date = st.date_input("Start date", value=date.today(), key="ta_start")
    with c2:
        days = st.slider("Number of days", 2, 21, 5, key="ta_days")
        travelers = st.number_input("Travelers", 1, 12, 2, key="ta_travelers")
    with c3:
        style = st.selectbox("Travel style", ["Backpacker", "Mid-range", "Premium", "Luxury"], index=1, key="ta_style")
        budget = st.number_input("Total budget (₹)", min_value=5000, max_value=2000000, value=40000, step=5000, key="ta_budget")

    vibes = st.multiselect(
        "Travel personality (pick 1–3)",
        ["Slow & Romantic", "Adventure & Adrenaline", "Heritage & Culture", "Foodie", "Wellness & Spiritual", "Family Fun"],
        default=["Heritage & Culture"],
        key="ta_vibes",
    )
    interests = st.multiselect(
        "Special interests",
        ["Photography", "Local food", "Music", "Trekking", "Architecture", "Wildlife", "Wellness", "Shopping", "Nightlife", "Solitude"],
        default=["Photography", "Local food"],
        key="ta_interests",
    )
    adventure = st.select_slider("Adventure level", options=["Slow", "Moderate", "High", "Extreme"], value="Moderate", key="ta_adv")

st.markdown('<div class="gold-divider"></div>', unsafe_allow_html=True)

generate_col1, generate_col2, _ = st.columns([1, 1, 2])
with generate_col1:
    go = st.button("Compose my journey", key="ta_go", use_container_width=True)

if go:
    plan = generate_itinerary(chosen["name"], chosen["category"], days, vibes, int(budget), interests)
    breakdown = budget_breakdown(int(budget), days, style)
    score, verdict = affordability_score(int(budget), days, style)
    dates = date_range(start_date, days)

    st.session_state["last_trip"] = {
        "destination": chosen,
        "start_city": start_city,
        "start_date": start_date.isoformat(),
        "days": days,
        "travelers": travelers,
        "style": style,
        "budget": int(budget),
        "vibes": vibes,
        "interests": interests,
        "adventure": adventure,
        "plan": plan,
        "breakdown": breakdown,
        "score": score,
        "verdict": verdict,
        "dates": [d.isoformat() for d in dates],
    }


trip = st.session_state.get("last_trip")
if trip:
    chosen = trip["destination"]
    section_header(
        f"{chosen['name']} · {trip['days']} days",
        f"Composed for {trip['travelers']} traveller{'s' if trip['travelers']>1 else ''}.",
        f"Starting from {trip['start_city']} on {trip['start_date']} · {trip['style']} style · ₹{trip['budget']:,} total.",
    )

    overview_cols = st.columns(4)
    overview_cols[0].metric("Total Budget", f"₹{trip['budget']:,}")
    overview_cols[1].metric("Per Day", f"₹{trip['budget']//trip['days']:,}")
    overview_cols[2].metric("Travelers", trip["travelers"])
    overview_cols[3].metric("Affordability", f"{trip['score']}/100")

    st.markdown(f'<div class="body-soft" style="margin: 16px 0 30px;">💡 {trip["verdict"]}</div>', unsafe_allow_html=True)

    # Day cards
    for d in trip["plan"]:
        st.markdown(
            f"""
            <div class="glass fade-in" style="margin-bottom: 18px;">
                <div style="display:flex; align-items:center; justify-content:space-between;">
                    <div>
                        <div class="eyebrow">Day {d['day']} · {trip['dates'][d['day']-1]}</div>
                        <h3 style="font-family:'Playfair Display', serif; font-size:24px; margin: 6px 0 6px;">{d['theme']}</h3>
                    </div>
                    <div class="dest-budget" style="font-size:15px;">₹{d['budget_inr']:,}</div>
                </div>
                <div class="gold-divider" style="margin: 14px 0;"></div>
                <div style="display:grid; grid-template-columns: repeat(auto-fit, minmax(220px, 1fr)); gap: 16px;">
                    <div><div class="eyebrow">Morning</div><div style="margin-top:6px;">🌅 {d['morning']}</div></div>
                    <div><div class="eyebrow">Afternoon</div><div style="margin-top:6px;">☀️ {d['afternoon']}</div></div>
                    <div><div class="eyebrow">Evening</div><div style="margin-top:6px;">🌙 {d['evening']}</div></div>
                    <div><div class="eyebrow">Stay</div><div style="margin-top:6px;">🏨 {d['stay'].title()}</div></div>
                    <div><div class="eyebrow">Food</div><div style="margin-top:6px;">🍽️ {d['food'].title()}</div></div>
                </div>
            </div>
            """,
            unsafe_allow_html=True,
        )

    # Save / export
    save_col1, save_col2, _ = st.columns([1, 1, 2])
    with save_col1:
        if user and st.button("Save to my lounge", key="ta_save", use_container_width=True):
            with get_conn() as c:
                c.execute(
                    "INSERT INTO trips (user_id, title, payload_json, created_at) VALUES (?,?,?,?)",
                    (user["id"], f"{chosen['name']} · {trip['days']} days", json.dumps(trip, default=str), now_iso()),
                )
            st.success("Saved to your lounge.")
    with save_col2:
        st.download_button(
            "Download itinerary (JSON)",
            data=json.dumps(trip, indent=2, default=str),
            file_name=f"atlasands_{chosen['id']}_{trip['days']}d.json",
            mime="application/json",
            use_container_width=True,
        )

    if not user:
        st.info("Sign in from the home page to save your itineraries to your private lounge.")

# Saved trips
if user:
    st.markdown('<div class="gold-divider" style="margin-top:50px;"></div>', unsafe_allow_html=True)
    section_header("Your Lounge", "Saved Itineraries")
    with get_conn() as c:
        rows = c.execute("SELECT * FROM trips WHERE user_id = ? ORDER BY id DESC LIMIT 8", (user["id"],)).fetchall()
    if rows:
        for r in rows:
            st.markdown(
                f"""
                <div class="glass fade-in" style="margin-bottom:12px;">
                    <div style="display:flex; justify-content:space-between; align-items:center;">
                        <div>
                            <div class="eyebrow">Saved · {r['created_at'][:10]}</div>
                            <div style="font-family:'Playfair Display', serif; font-size:20px;">{r['title']}</div>
                        </div>
                    </div>
                </div>
                """,
                unsafe_allow_html=True,
            )
    else:
        st.markdown('<p class="body-soft">No saved itineraries yet — compose one above.</p>', unsafe_allow_html=True)
