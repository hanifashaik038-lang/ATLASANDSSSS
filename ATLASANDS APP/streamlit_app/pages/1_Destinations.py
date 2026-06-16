"""Destinations — gallery of 50+ Indian places with filters and save-to-favourites."""
import streamlit as st
from utils.styles import inject_global_styles, hero, section_header, render_floating_orb, render_theme_toggle
from utils.destinations import DESTINATIONS, CATEGORIES, HERO_SLIDES, find
from utils.auth import ensure_session
from utils.database import init_db, get_favorites, toggle_favorite

st.set_page_config(page_title="Destinations · ATLASANDS", page_icon="🌍", layout="wide", initial_sidebar_state="collapsed")
inject_global_styles()
init_db()
render_floating_orb()
user = ensure_session()

# Sidebar with theme toggle and favorites list
with st.sidebar:
    st.markdown('<div class="eyebrow">ATLASANDS</div>', unsafe_allow_html=True)
    st.markdown('<div style="font-family:\'Playfair Display\', serif; font-size:24px; color:var(--gold); margin: 4px 0 18px;">Destinations</div>', unsafe_allow_html=True)
    render_theme_toggle("dest")
    st.markdown('<div class="gold-divider"></div>', unsafe_allow_html=True)
    if user:
        favs = get_favorites(user["id"])
        st.markdown(f'<div class="eyebrow">Saved ({len(favs)})</div>', unsafe_allow_html=True)
        if favs:
            for fid in list(favs)[:10]:
                d = find(fid)
                if d:
                    st.markdown(f'<div style="margin:8px 0;font-family:\'Playfair Display\', serif;font-size:15px;color:var(--text);">{d["name"]}<br/><span style="font-size:11px;color:var(--text-dim);">{d["state"]}</span></div>', unsafe_allow_html=True)
        else:
            st.markdown('<p class="body-soft" style="font-size:13px;">No saved places yet — tap ♡ on any card.</p>', unsafe_allow_html=True)
    else:
        st.markdown('<p class="body-soft" style="font-size:13px;">Sign in from the home page to save your favourite destinations.</p>', unsafe_allow_html=True)


hero(
    image_url=HERO_SLIDES[4]["image"],
    eyebrow="DESTINATIONS",
    title_html="Fifty Frames of India,<br/>One Atlas.",
    subtitle="Filter by mood, season or category. Every destination is a story waiting to be opened.",
)

# Filter bar
st.markdown('<div style="height: 30px;"></div>', unsafe_allow_html=True)
fc1, fc2, fc3 = st.columns([2, 1, 1])
with fc1:
    q = st.text_input("Search by name, state or vibe", placeholder="e.g. Kashmir, lake, monastery, desert…", key="dest_search")
with fc2:
    cat = st.selectbox("Category", ["All"] + CATEGORIES, key="dest_cat")
with fc3:
    sort_by = st.selectbox("Sort by", ["Curated", "Budget (Low → High)", "Budget (High → Low)", "Name (A–Z)", "♡ Favourites first"], key="dest_sort")


def _budget_int(s: str) -> int:
    return int("".join(ch for ch in s if ch.isdigit()) or 0)


user_favs = get_favorites(user["id"]) if user else set()

filtered = DESTINATIONS
if q:
    qn = q.lower().strip()
    filtered = [d for d in filtered if qn in d["name"].lower()
                or qn in d["state"].lower()
                or qn in d["category"].lower()
                or qn in d["desc"].lower()]
if cat != "All":
    filtered = [d for d in filtered if d["category"] == cat]
if sort_by == "Budget (Low → High)":
    filtered = sorted(filtered, key=lambda d: _budget_int(d["budget"]))
elif sort_by == "Budget (High → Low)":
    filtered = sorted(filtered, key=lambda d: -_budget_int(d["budget"]))
elif sort_by == "Name (A–Z)":
    filtered = sorted(filtered, key=lambda d: d["name"])
elif sort_by == "♡ Favourites first":
    filtered = sorted(filtered, key=lambda d: (d["id"] not in user_favs, d["name"]))

st.markdown(
    f'<div class="eyebrow" style="margin: 24px 0 4px;">{len(filtered)} destinations</div>',
    unsafe_allow_html=True,
)

# Grid (3 columns of cards, with a save button under each)
cols = st.columns(3)
for i, d in enumerate(filtered):
    is_fav = d["id"] in user_favs
    badge_class = "fav-badge saved" if is_fav else "fav-badge"
    badge_icon = "♥" if is_fav else "♡"
    with cols[i % 3]:
        st.markdown(
            f"""
            <div class="dest-card fade-in" style="margin-bottom: 12px;">
                <div class="{badge_class}">{badge_icon}</div>
                <img src="{d['image']}" alt="{d['name']}"/>
                <div class="dest-overlay">
                    <span class="dest-tag">{d['category']}</span>
                    <div class="dest-title">{d['name']}</div>
                    <div class="dest-meta">{d['state']} · Best: {d['season']}</div>
                    <div class="dest-budget">From {d['budget']} pp</div>
                    <div style="color:rgba(245,241,232,0.78);margin-top:8px;font-size:13px;line-height:1.5;">{d['desc']}</div>
                </div>
            </div>
            """,
            unsafe_allow_html=True,
        )
        # Save button below the card
        btn_label = "♥  Saved" if is_fav else "♡  Save to lounge"
        if st.button(btn_label, key=f"fav_{d['id']}", use_container_width=True):
            if not user:
                st.toast("Sign in from the home page to save destinations.", icon="🔒")
            else:
                now_fav = toggle_favorite(user["id"], d["id"])
                st.toast(f"{'Saved' if now_fav else 'Removed'}: {d['name']}", icon="♥" if now_fav else "♡")
                st.rerun()

if not filtered:
    st.markdown(
        """
        <div class="glass-strong" style="text-align:center; margin: 40px 0;">
            <h3>No destinations match that filter.</h3>
            <p class="body-soft">Try a different keyword or open the AI Concierge for a tailored recommendation.</p>
        </div>
        """,
        unsafe_allow_html=True,
    )

st.markdown('<div class="gold-divider" style="margin-top:40px;"></div>', unsafe_allow_html=True)
cta1, cta2, cta3 = st.columns([1, 1, 1])
with cta2:
    if st.button("Design my trip with AI →", key="dest_cta", use_container_width=True):
        st.switch_page("pages/3_Trip_Architect.py")
