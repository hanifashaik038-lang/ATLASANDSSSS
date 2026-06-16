"""Smart Packing Assistant — checklist generator."""
import streamlit as st
from utils.styles import inject_global_styles, hero, section_header, render_floating_orb
from utils.destinations import HERO_SLIDES, CATEGORIES
from utils.trip_engine import generate_packing

st.set_page_config(page_title="Smart Packing · ATLASANDS", page_icon="🎒", layout="wide", initial_sidebar_state="collapsed")
inject_global_styles()
render_floating_orb()

hero(
    image_url=HERO_SLIDES[3]["image"],
    eyebrow="SMART PACKING",
    title_html="What To Carry.<br/>What To Leave Behind.",
    subtitle="A season-aware, activity-specific checklist that thinks about what you'll actually need — and forgets nothing.",
)

st.markdown('<div style="height: 26px;"></div>', unsafe_allow_html=True)

c1, c2, c3 = st.columns(3)
with c1:
    category = st.selectbox("Trip type", CATEGORIES, key="pk_cat")
with c2:
    days = st.slider("Days", 1, 21, 5, key="pk_days")
with c3:
    season = st.selectbox("When", ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"], index=9, key="pk_season")

items = generate_packing(category, days, season)
total = len(items)
st.markdown(f'<div class="eyebrow" style="margin: 24px 0 10px;">{total} items · {category} · {days} days · {season}</div>', unsafe_allow_html=True)

# Initialize check state
key_prefix = f"pk_{category}_{days}_{season}"
if "pk_state" not in st.session_state:
    st.session_state["pk_state"] = {}

cols = st.columns(2)
for i, item in enumerate(items):
    with cols[i % 2]:
        check_key = f"{key_prefix}_{i}"
        checked = st.session_state["pk_state"].get(check_key, False)
        new_val = st.checkbox(item, value=checked, key=f"cb_{check_key}")
        st.session_state["pk_state"][check_key] = new_val

checked_count = sum(1 for k, v in st.session_state["pk_state"].items() if k.startswith(key_prefix) and v)
progress = checked_count / max(1, total)

st.markdown('<div class="gold-divider"></div>', unsafe_allow_html=True)
pc1, pc2 = st.columns([1, 3])
with pc1:
    st.markdown(f'<div class="stat" style="padding:14px 0;"><div class="stat-num" style="font-size:42px;">{checked_count}/{total}</div><div class="stat-label">Packed</div></div>', unsafe_allow_html=True)
with pc2:
    st.markdown('<div class="eyebrow" style="margin-bottom:8px;">Progress</div>', unsafe_allow_html=True)
    st.progress(progress)
    st.markdown(
        '<p class="body-soft" style="margin-top:10px;">Tip: pack the night before, weigh your bag at home, and remember that what you can buy in India easily isn\'t worth carrying.</p>',
        unsafe_allow_html=True,
    )

st.markdown(
    """
    <div class="glass-strong" style="margin-top:30px;">
        <div class="eyebrow">Download</div>
        <p class="body-soft" style="margin-top:8px;">Print or save your checklist.</p>
    </div>
    """,
    unsafe_allow_html=True,
)
st.download_button(
    "Download checklist (.txt)",
    data="\n".join([f"[ ] {item}" for item in items]),
    file_name=f"atlasands_packing_{category.lower()}_{days}d.txt",
)
