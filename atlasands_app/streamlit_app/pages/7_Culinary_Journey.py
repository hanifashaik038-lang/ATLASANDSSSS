"""Culinary Journey — Indian food by region."""
import streamlit as st
from utils.styles import inject_global_styles, hero, section_header, render_floating_orb
from utils.destinations import HERO_SLIDES
from utils.content import CULINARY

st.set_page_config(page_title="Culinary Journey · ATLASANDS", page_icon="🍲", layout="wide", initial_sidebar_state="collapsed")
inject_global_styles()
render_floating_orb()

hero(
    image_url=HERO_SLIDES[2]["image"],
    eyebrow="CULINARY JOURNEY",
    title_html="A Subcontinent<br/>Tastes Different In Six Acts.",
    subtitle="From Kashmiri Wazwan to Chettinad chicken, from Bengali fish to Naga smoked pork — a regional atlas of Indian flavour.",
)

st.markdown('<div style="height: 30px;"></div>', unsafe_allow_html=True)

for i, region in enumerate(CULINARY):
    st.markdown(
        f"""
        <div class="glass fade-in" style="margin-bottom: 28px; padding:0; overflow:hidden;">
            <div style="display:grid; grid-template-columns: 1fr 1.4fr; gap:0;">
                <img src="{region['image']}" alt="{region['region']}" style="width:100%; height:100%; min-height:380px; object-fit:cover;"/>
                <div style="padding: 32px;">
                    <div class="eyebrow">Region · {region['states']}</div>
                    <h3 style="font-family:'Playfair Display', serif; font-size:34px; margin:8px 0 16px; color:#F5F1E8;">{region['region']}</h3>
                    <p class="serif-quote">{region['note']}</p>
                    <div class="gold-divider"></div>
                    <div class="eyebrow">Signature dishes</div>
                    <p class="body-soft" style="margin: 8px 0 14px;">{' · '.join(region['signature'])}</p>
                    <div class="eyebrow">Vegetarian highlights</div>
                    <p class="body-soft" style="margin: 8px 0 14px;">{' · '.join(region['vegetarian'])}</p>
                    <div class="eyebrow">Sweet finish</div>
                    <p class="body-soft" style="margin: 8px 0 14px;">{region['sweet']}</p>
                    <div class="eyebrow">Where to taste it</div>
                    <p class="body-soft" style="margin: 8px 0 0;">📍 {region['must_try_city']}</p>
                </div>
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

st.markdown('<div class="gold-divider" style="margin-top:30px;"></div>', unsafe_allow_html=True)
st.markdown(
    """
    <div class="glass-strong fade-in" style="text-align:center; margin-top:20px;">
        <div class="eyebrow">A Note From The Concierge</div>
        <p class="serif-quote" style="max-width:680px; margin: 12px auto;">
            "Food is the fastest passport in India. Eat where the locals queue, sit on the floor when invited, and never refuse a second helping. The meal is the country."
        </p>
    </div>
    """,
    unsafe_allow_html=True,
)
