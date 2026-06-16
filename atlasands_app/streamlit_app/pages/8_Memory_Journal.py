"""Memory Journal — write entries, generate editorial AI stories."""
import streamlit as st
from utils.styles import inject_global_styles, hero, section_header, render_floating_orb
from utils.destinations import HERO_SLIDES
from utils.trip_engine import journal_story
from utils.auth import require_login
from utils.database import get_conn, init_db, now_iso

st.set_page_config(page_title="Memory Journal · ATLASANDS", page_icon="📖", layout="wide", initial_sidebar_state="collapsed")
inject_global_styles()
init_db()
render_floating_orb()
user = require_login()

hero(
    image_url=HERO_SLIDES[3]["image"],
    eyebrow="MEMORY JOURNAL",
    title_html="Travel Twice.<br/>Once In The World, Once In Words.",
    subtitle="Write down what you felt. The journal weaves it into a quiet editorial — so the memory survives the suitcase.",
)

st.markdown('<div style="height: 26px;"></div>', unsafe_allow_html=True)

tab_write, tab_browse = st.tabs(["Write a new entry", "Your journal"])

with tab_write:
    with st.form("journal_form", clear_on_submit=False):
        c1, c2, c3 = st.columns([2, 1, 1])
        with c1:
            title = st.text_input("Title", placeholder="The day the Pangong turned violet", key="j_title")
        with c2:
            location = st.text_input("Location", placeholder="Pangong Tso, Ladakh", key="j_location")
        with c3:
            jdate = st.date_input("Date", key="j_date")
        body = st.text_area("Tell the story", height=180, placeholder="What did you see? Smell? Hear? Who did you meet? What surprised you?", key="j_body")
        submitted = st.form_submit_button("Save & weave the story", use_container_width=True)

    if submitted:
        if not title.strip() or not body.strip():
            st.error("Please give your entry a title and a few lines.")
        else:
            story = journal_story(title.strip(), location.strip(), body.strip())
            with get_conn() as c:
                c.execute(
                    "INSERT INTO journals (user_id, title, location, date, body, ai_story, created_at) VALUES (?,?,?,?,?,?,?)",
                    (user["id"], title.strip(), location.strip(), jdate.isoformat(), body.strip(), story, now_iso()),
                )
            st.success("Your memory has been woven and saved.")
            st.markdown(
                f"""
                <div class="glass-strong fade-in" style="margin-top:20px;">
                    <div class="eyebrow">Generated story</div>
                    <div style="font-family:'Cormorant Garamond', serif; font-size: 19px; line-height: 1.7; margin-top:10px; color:#F5F1E8; white-space: pre-wrap;">{story}</div>
                </div>
                """,
                unsafe_allow_html=True,
            )

with tab_browse:
    with get_conn() as c:
        rows = c.execute("SELECT * FROM journals WHERE user_id = ? ORDER BY id DESC", (user["id"],)).fetchall()
    if not rows:
        st.markdown('<p class="body-soft" style="margin-top:24px;">Your journal is empty. Write your first entry above.</p>', unsafe_allow_html=True)
    else:
        for r in rows:
            st.markdown(
                f"""
                <div class="glass fade-in" style="margin-bottom:18px;">
                    <div style="display:flex; justify-content:space-between; align-items:baseline; flex-wrap:wrap;">
                        <div>
                            <div class="eyebrow">{r['location'] or '—'} · {r['date']}</div>
                            <h3 style="font-family:'Playfair Display', serif; font-size:24px; margin:6px 0 8px;">{r['title']}</h3>
                        </div>
                        <div style="color:rgba(245,241,232,0.4); font-size:12px;">saved {r['created_at'][:10]}</div>
                    </div>
                    <div style="font-family:'Cormorant Garamond', serif; font-size:17px; line-height:1.7; color:rgba(245,241,232,0.85); white-space:pre-wrap;">{r['ai_story']}</div>
                </div>
                """,
                unsafe_allow_html=True,
            )
