"""Budget Intelligence — interactive luxury dashboard with Plotly."""
import streamlit as st
import plotly.graph_objects as go
import pandas as pd
from utils.styles import inject_global_styles, hero, section_header, render_floating_orb
from utils.destinations import HERO_SLIDES
from utils.trip_engine import budget_breakdown, affordability_score

st.set_page_config(page_title="Budget Intelligence · ATLASANDS", page_icon="💰", layout="wide", initial_sidebar_state="collapsed")
inject_global_styles()
render_floating_orb()

hero(
    image_url=HERO_SLIDES[5]["image"],
    eyebrow="BUDGET INTELLIGENCE",
    title_html="The Quiet Economics<br/>Of A Beautiful Journey.",
    subtitle="Honest numbers, smart breakdowns, and an affordability score that tells you the truth — before the trip, not after.",
)

st.markdown('<div style="height: 26px;"></div>', unsafe_allow_html=True)

c1, c2, c3, c4 = st.columns(4)
with c1:
    total = st.number_input("Total budget (₹)", min_value=5000, max_value=2000000, value=60000, step=5000, key="bi_total")
with c2:
    days = st.slider("Days", 2, 30, 7, key="bi_days")
with c3:
    travelers = st.number_input("Travelers", 1, 12, 2, key="bi_trav")
with c4:
    style = st.selectbox("Style", ["Backpacker", "Mid-range", "Premium", "Luxury"], index=1, key="bi_style")

breakdown = budget_breakdown(int(total), int(days), style)
score, verdict = affordability_score(int(total), int(days), style)

# Metrics
m1, m2, m3, m4 = st.columns(4)
m1.metric("Per day", f"₹{int(total)//int(days):,}")
m2.metric("Per person/day", f"₹{int(total)//(int(days)*int(travelers)):,}")
m3.metric("Affordability", f"{score}/100")
m4.metric("Style", style)

st.markdown(f'<div class="glass-strong fade-in" style="margin: 20px 0;"><div class="eyebrow">Health Verdict</div><p class="serif-quote" style="margin-top:8px;">{verdict}</p></div>', unsafe_allow_html=True)

# Donut chart
labels = list(breakdown.keys())
values = list(breakdown.values())
colors = ["#D4AF37", "#E8C77A", "#A88B3A", "#5E4F23", "#8C7A3E", "#C9A35A"]

fig = go.Figure(data=[go.Pie(
    labels=labels, values=values, hole=0.55,
    marker=dict(colors=colors, line=dict(color="#0A0A0F", width=2)),
    textinfo="label+percent", textfont=dict(family="Inter", size=13, color="#F5F1E8"),
    hovertemplate="<b>%{label}</b><br>₹%{value:,}<br>%{percent}<extra></extra>",
)])
fig.update_layout(
    paper_bgcolor="rgba(0,0,0,0)",
    plot_bgcolor="rgba(0,0,0,0)",
    font=dict(family="Inter", color="#F5F1E8"),
    showlegend=True,
    legend=dict(font=dict(color="#F5F1E8")),
    margin=dict(l=20, r=20, t=20, b=20),
    height=420,
    annotations=[dict(text=f"<b style='font-family:Playfair Display;font-size:24px;'>₹{int(total):,}</b><br><span style='color:#D4AF37;font-size:11px;letter-spacing:.3em;'>TOTAL</span>",
                      x=0.5, y=0.5, font_size=14, font_color="#F5F1E8", showarrow=False)],
)

bc1, bc2 = st.columns([3, 2])
with bc1:
    st.plotly_chart(fig, use_container_width=True, config={"displayModeBar": False})
with bc2:
    st.markdown('<div class="eyebrow">Breakdown</div>', unsafe_allow_html=True)
    for label, value in breakdown.items():
        pct = int(value / int(total) * 100)
        st.markdown(
            f"""
            <div class="glass fade-in" style="margin-top:10px;">
                <div style="display:flex; justify-content:space-between; align-items:baseline;">
                    <div style="font-family:'Playfair Display', serif; font-size:18px;">{label}</div>
                    <div class="dest-budget">₹{value:,} <span style="color:rgba(245,241,232,0.5); font-size:11px;">({pct}%)</span></div>
                </div>
            </div>
            """,
            unsafe_allow_html=True,
        )

# Saving tips
section_header("Savings Intelligence", "Smart Ways To Travel Lighter.")
tips = [
    ("Book trains 60 days ahead", "IRCTC opens reservations 60 days before departure. Tatkal is 1 day before but usually 30–40% costlier."),
    ("Travel in shoulder season", "March, September and October offer the same beauty as peak months at 30–40% lower hotel rates."),
    ("Choose state heritage hotels", "RTDC (Rajasthan), KTDC (Kerala) and HPTDC (Himachal) offer clean, often heritage rooms at half the chain hotel rate."),
    ("Eat where locals queue", "Family-run restaurants and street stalls cost 70% less than hotel restaurants — and taste better."),
    ("Use shared SUVs in the mountains", "Pangong, Spiti, Munnar — sharing the vehicle drops cost by 60% with zero compromise on experience."),
    ("Skip pre-paid airport taxis", "Use Ola Outstation or local airport metro/express trains — savings of ₹400–1,200 per ride in metros."),
]
tc = st.columns(2)
for i, (head, body) in enumerate(tips):
    with tc[i % 2]:
        st.markdown(
            f"""
            <div class="glass fade-in" style="margin-bottom:14px;">
                <div class="eyebrow">{head}</div>
                <p class="body-soft" style="margin-top:8px;font-size:14px;">{body}</p>
            </div>
            """,
            unsafe_allow_html=True,
        )
