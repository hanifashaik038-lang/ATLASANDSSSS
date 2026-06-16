"""Hidden Worlds — editorial storytelling for lesser-known destinations."""
import streamlit as st
from utils.styles import inject_global_styles, hero, section_header, render_floating_orb
from utils.destinations import HERO_SLIDES
from utils.content import HIDDEN_WORLDS

st.set_page_config(page_title="Hidden Worlds · ATLASANDS", page_icon="🌿", layout="wide", initial_sidebar_state="collapsed")
inject_global_styles()
render_floating_orb()

hero(
    image_url=HERO_SLIDES[1]["image"],
    eyebrow="HIDDEN WORLDS",
    title_html="The India That Guidebooks<br/>Forgot To Print.",
    subtitle="Villages where time slowed, monasteries that still hum, salt deserts that turn silver at full moon. Curated for the few who travel for the story.",
)

st.markdown('<div style="height: 30px;"></div>', unsafe_allow_html=True)

for i, place in enumerate(HIDDEN_WORLDS):
    img_col, text_col = st.columns([1, 1]) if i % 2 == 0 else st.columns([1, 1])
    if i % 2 == 0:
        with img_col:
            st.markdown(
                f"""
                <div class="dest-card fade-in" style="height:520px; margin-bottom:50px;">
                    <img src="{place['image']}" alt="{place['name']}"/>
                    <div class="dest-overlay">
                        <span class="dest-tag">Hidden</span>
                        <div class="dest-title">{place['name']}</div>
                        <div class="dest-meta">{place['state']}</div>
                    </div>
                </div>
                """,
                unsafe_allow_html=True,
            )
        with text_col:
            st.markdown(
                f"""
                <div class="glass fade-in" style="height:520px; margin-bottom:50px; display:flex; flex-direction:column; justify-content:center;">
                    <div class="eyebrow">Why this place is special</div>
                    <h3 style="font-family:'Playfair Display', serif; font-size:32px; margin:10px 0 16px; color:#F5F1E8;">{place['name']}</h3>
                    <p class="serif-quote">"{place['why']}"</p>
                    <div class="gold-divider"></div>
                    <div style="display:flex; gap:24px; flex-wrap:wrap;">
                        <div>
                            <div class="eyebrow">Best time</div>
                            <div style="font-family:'Playfair Display', serif; font-size:18px; margin-top:6px;">{place['best']}</div>
                        </div>
                        <div style="flex:1; min-width:200px;">
                            <div class="eyebrow">The experience</div>
                            <p class="body-soft" style="margin-top:6px;font-size:14px;">{place['experience']}</p>
                        </div>
                    </div>
                </div>
                """,
                unsafe_allow_html=True,
            )
    else:
        with img_col:
            st.markdown(
                f"""
                <div class="glass fade-in" style="height:520px; margin-bottom:50px; display:flex; flex-direction:column; justify-content:center;">
                    <div class="eyebrow">Why this place is special</div>
                    <h3 style="font-family:'Playfair Display', serif; font-size:32px; margin:10px 0 16px; color:#F5F1E8;">{place['name']}</h3>
                    <p class="serif-quote">"{place['why']}"</p>
                    <div class="gold-divider"></div>
                    <div style="display:flex; gap:24px; flex-wrap:wrap;">
                        <div>
                            <div class="eyebrow">Best time</div>
                            <div style="font-family:'Playfair Display', serif; font-size:18px; margin-top:6px;">{place['best']}</div>
                        </div>
                        <div style="flex:1; min-width:200px;">
                            <div class="eyebrow">The experience</div>
                            <p class="body-soft" style="margin-top:6px;font-size:14px;">{place['experience']}</p>
                        </div>
                    </div>
                </div>
                """,
                unsafe_allow_html=True,
            )
        with text_col:
            st.markdown(
                f"""
                <div class="dest-card fade-in" style="height:520px; margin-bottom:50px;">
                    <img src="{place['image']}" alt="{place['name']}"/>
                    <div class="dest-overlay">
                        <span class="dest-tag">Hidden</span>
                        <div class="dest-title">{place['name']}</div>
                        <div class="dest-meta">{place['state']}</div>
                    </div>
                </div>
                """,
                unsafe_allow_html=True,
            )
