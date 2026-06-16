"""ATLASANDS — Streamlit luxury entry point (Home)."""
import streamlit as st
from utils.styles import inject_global_styles, hero, section_header, render_floating_orb, render_theme_toggle
from utils.destinations import DESTINATIONS, CATEGORIES, HERO_SLIDES
from utils.auth import ensure_session, signup, login, set_session, clear_session
from utils.content import TIMELINE_SAMPLE, TESTIMONIALS
from utils.database import init_db, get_conn

st.set_page_config(
    page_title="ATLASANDS · Your World, Your Way",
    page_icon="🌍",
    layout="wide",
    initial_sidebar_state="collapsed",
)

inject_global_styles()
init_db()
render_floating_orb()


# -------- Sidebar (auth + nav) --------
def render_sidebar():
    user = ensure_session()
    with st.sidebar:
        st.markdown(
            """
            <div style="padding:6px 0 14px;">
                <div class="eyebrow">ATLASANDS</div>
                <div style="font-family:'Playfair Display', serif; font-size:30px; color:#D4AF37; font-weight:700; line-height:1;">A T L A S<br/>A N D S</div>
                <div style="color:rgba(245,241,232,0.55); font-style:italic; font-size:12px; margin-top:6px;">Your World, Your Way.</div>
            </div>
            """,
            unsafe_allow_html=True,
        )
        st.markdown('<div class="gold-divider"></div>', unsafe_allow_html=True)

        if user:
            st.markdown(
                f"""
                <div class="glass" style="padding:14px 16px;">
                    <div class="eyebrow" style="font-size:10px;">Signed in</div>
                    <div style="font-family:'Playfair Display', serif; font-size:18px; color:#F5F1E8; margin-top:4px;">{user['name']}</div>
                    <div style="color:rgba(245,241,232,0.55); font-size:12px;">{user['email']}</div>
                </div>
                """,
                unsafe_allow_html=True,
            )
            st.markdown(' ', unsafe_allow_html=True)
            if st.button("Sign Out", key="signout_btn", use_container_width=True):
                clear_session()
                st.rerun()
        else:
            st.markdown('<div class="eyebrow">Members Lounge</div>', unsafe_allow_html=True)
            tab_login, tab_signup = st.tabs(["Sign In", "Create Account"])
            with tab_login:
                with st.form("login_form", clear_on_submit=False):
                    email = st.text_input("Email", key="login_email", placeholder="you@journey.com")
                    pw = st.text_input("Password", type="password", key="login_pw")
                    submitted = st.form_submit_button("Sign In", use_container_width=True)
                    if submitted:
                        ok, res = login(email, pw)
                        if ok:
                            set_session(res)
                            st.success("Welcome back.")
                            st.rerun()
                        else:
                            st.error(res)
            with tab_signup:
                with st.form("signup_form", clear_on_submit=False):
                    name = st.text_input("Full Name", key="su_name")
                    email = st.text_input("Email", key="su_email")
                    pw = st.text_input("Password (8+ chars)", type="password", key="su_pw")
                    submitted = st.form_submit_button("Create Account", use_container_width=True)
                    if submitted:
                        ok, res = signup(email, name, pw)
                        if ok:
                            set_session(res)
                            st.success("Your lounge is ready.")
                            st.rerun()
                        else:
                            st.error(res)

        st.markdown('<div class="gold-divider"></div>', unsafe_allow_html=True)
        render_theme_toggle("home")
        st.markdown(
            """
            <div style="color:rgba(245,241,232,0.55); font-size:12px; line-height:1.7;">
                Use the menu above for AI Concierge, Trip Architect, Budget Intelligence, Smart Packing, Hidden Worlds, Culinary Journey and Memory Journal.
            </div>
            """,
            unsafe_allow_html=True,
        )
    return user


user = render_sidebar()


# -------- Hero --------
hero(
    image_url=HERO_SLIDES[0]["image"],
    eyebrow="ATLASANDS · YOUR WORLD, YOUR WAY",
    title_html="The Art of Travelling India,<br/>Reimagined by AI.",
    subtitle="A digital atelier where intelligent design meets cinematic discovery — fifty destinations, one private concierge, infinite ways to wander.",
)

col_h1, col_h2, _ = st.columns([1, 1, 2])
with col_h1:
    if st.button("Start Your Journey", key="hero_cta_start", use_container_width=True):
        st.switch_page("pages/3_Trip_Architect.py")
with col_h2:
    st.markdown('<div class="ghost">', unsafe_allow_html=True)
    if st.button("Explore India", key="hero_cta_explore", use_container_width=True):
        st.switch_page("pages/1_Destinations.py")
    st.markdown('</div>', unsafe_allow_html=True)


# -------- AI Concierge orb teaser --------
st.markdown('<div style="height: 36px;"></div>', unsafe_allow_html=True)
ai_col1, ai_col2 = st.columns([1, 2])
with ai_col1:
    st.markdown(
        """
        <div class="glass-strong fade-in" style="text-align:center;">
            <div class="orb-wrap"><div class="ai-orb"></div></div>
            <div class="eyebrow" style="margin-top:18px;">AI Concierge</div>
            <h3 style="font-family:'Playfair Display', serif; font-size:28px; margin:8px 0 10px;">Meet your digital travel companion.</h3>
            <p class="body-soft">A breathing intelligence that remembers your taste, designs your days and whispers the secrets locals usually keep.</p>
        </div>
        """,
        unsafe_allow_html=True,
    )
    if st.button("Open Concierge", key="open_concierge_home", use_container_width=True):
        st.switch_page("pages/2_AI_Concierge.py")

with ai_col2:
    st.markdown(
        """
        <div class="glass fade-in" style="height:100%;">
            <div class="eyebrow">A few things I can help with</div>
            <h3 style="font-family:'Playfair Display', serif; font-size:26px; margin:8px 0 14px;">Ask me anything about Indian travel.</h3>
            <div style="display:grid; grid-template-columns: 1fr 1fr; gap:12px;">
                <div class="feature-pill"><div class="feature-icon">🗺️</div><div><div class="feature-title">Itineraries</div><div class="feature-desc">3 to 21 days, hand-crafted for your vibe.</div></div></div>
                <div class="feature-pill"><div class="feature-icon">💰</div><div><div class="feature-title">Budget guidance</div><div class="feature-desc">Honest costs, smart savings, no surprises.</div></div></div>
                <div class="feature-pill"><div class="feature-icon">🎒</div><div><div class="feature-title">Packing lists</div><div class="feature-desc">Season-aware, activity-specific.</div></div></div>
                <div class="feature-pill"><div class="feature-icon">🍲</div><div><div class="feature-title">Local cuisine</div><div class="feature-desc">What to eat, where to find it.</div></div></div>
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )


# -------- Featured Destinations preview (8) --------
section_header(
    "Featured Destinations",
    "India, In Fifty Cinematic Frames.",
    "From Himalayan monasteries to Andaman atolls — explore curated experiences across the subcontinent.",
)

featured = DESTINATIONS[:8]
cols = st.columns(4)
for i, d in enumerate(featured):
    with cols[i % 4]:
        st.markdown(
            f"""
            <div class="dest-card fade-in" style="margin-bottom: 22px;">
                <img src="{d['image']}" alt="{d['name']}"/>
                <div class="dest-overlay">
                    <span class="dest-tag">{d['category']}</span>
                    <div class="dest-title">{d['name']}</div>
                    <div class="dest-meta">{d['state']} · {d['season']}</div>
                    <div class="dest-budget">From {d['budget']}</div>
                </div>
            </div>
            """,
            unsafe_allow_html=True,
        )

cta_col1, cta_col2, cta_col3 = st.columns([1, 1, 1])
with cta_col2:
    if st.button("View All 50+ Destinations", key="view_all_dest", use_container_width=True):
        st.switch_page("pages/1_Destinations.py")


# -------- AI Features Universe --------
section_header(
    "The ATLASANDS Universe",
    "Eleven Quiet Superpowers.",
    "Each tool was designed for one purpose — to remove friction from the dream of travel.",
)

features = [
    ("🤖", "AI Itinerary Generator", "Tell me a vibe; I'll design the days."),
    ("💰", "Budget Intelligence", "Smart breakdowns, honest forecasts."),
    ("🗺️", "Hidden Gem Discovery", "Places guidebooks haven't found yet."),
    ("🎒", "Smart Packing Assistant", "Season-aware, activity-specific checklists."),
    ("🍲", "Culinary Explorer", "A regional map of India's flavours."),
    ("🏨", "Hotel Suggestions", "From hostels to heritage palaces."),
    ("📸", "Scenic Spot Finder", "The light, the angle, the perfect hour."),
    ("📖", "AI Travel Journal", "Your memories, written like an editorial."),
    ("🌱", "Eco Travel Score", "Travel light, leave only footprints."),
    ("🛡️", "Safety Assistant", "Local intel, emergency lines, smart routes."),
    ("🚗", "Route Intelligence", "Scenic detours and quietest roads."),
]
fcols = st.columns(3)
for i, (icon, title, desc) in enumerate(features):
    with fcols[i % 3]:
        st.markdown(
            f"""
            <div class="feature-pill fade-in" style="margin-bottom: 14px;">
                <div class="feature-icon">{icon}</div>
                <div>
                    <div class="feature-title">{title}</div>
                    <div class="feature-desc">{desc}</div>
                </div>
            </div>
            """,
            unsafe_allow_html=True,
        )


# -------- Journey timeline --------
section_header(
    "Your Journey, Choreographed.",
    "Four Days, Four Acts.",
    "Every ATLASANDS itinerary is composed like a film — arrival, adventure, depth, reflection.",
)
tcols = st.columns(4)
for i, day in enumerate(TIMELINE_SAMPLE):
    with tcols[i]:
        st.markdown(
            f"""
            <div class="glass fade-in" style="height:100%;">
                <div class="eyebrow">Day {day['day']}</div>
                <h3 style="font-family:'Playfair Display', serif; font-size:22px; margin:8px 0 10px;">{day['title']}</h3>
                <p class="body-soft" style="font-size:14px;">{day['desc']}</p>
            </div>
            """,
            unsafe_allow_html=True,
        )


# -------- Stats --------
section_header(
    "Quiet Numbers, Loud Stories.",
    "An Atelier With A Reach.",
)
scols = st.columns(4)
stats = [
    ("10,000+", "Journeys Planned"),
    ("500+", "Destinations Covered"),
    ("1M+", "AI Recommendations"),
    ("99%", "Traveler Happiness"),
]
for i, (num, label) in enumerate(stats):
    with scols[i]:
        st.markdown(
            f"""
            <div class="glass-strong stat fade-in">
                <div class="stat-num">{num}</div>
                <div class="stat-label">{label}</div>
            </div>
            """,
            unsafe_allow_html=True,
        )


# -------- Testimonials --------
section_header(
    "Traveler Stories",
    "Voices From The Road.",
)
tscols = st.columns(2)
for i, t in enumerate(TESTIMONIALS):
    with tscols[i % 2]:
        stars = "★" * t["rating"] + "☆" * (5 - t["rating"])
        st.markdown(
            f"""
            <div class="glass fade-in" style="margin-bottom:20px;">
                <div style="display:flex; gap:14px; align-items:center;">
                    <img src="{t['image']}" alt="{t['name']}" style="width:54px;height:54px;border-radius:50%; object-fit:cover; border: 1px solid rgba(212,175,55,0.4);"/>
                    <div>
                        <div style="font-family:'Playfair Display', serif; font-size:18px;">{t['name']}</div>
                        <div style="color:rgba(245,241,232,0.55); font-size:13px;">{t['city']}</div>
                        <div style="color:#D4AF37; font-size:13px; letter-spacing:.3em;">{stars}</div>
                    </div>
                </div>
                <p class="serif-quote" style="margin-top:18px;">"{t['quote']}"</p>
            </div>
            """,
            unsafe_allow_html=True,
        )


# -------- Footer --------
st.markdown('<div class="gold-divider" style="margin-top:60px;"></div>', unsafe_allow_html=True)
st.markdown(
    """
    <div style="display:flex; flex-wrap:wrap; gap:24px; justify-content:space-between; align-items:flex-start; margin: 30px 0 10px;">
        <div style="flex:1; min-width:220px;">
            <div style="font-family:'Playfair Display', serif; font-size:26px; color:#D4AF37;">ATLASANDS</div>
            <div style="color:rgba(245,241,232,0.55); font-size:13px; font-style:italic; margin-top:6px;">Your World, Your Way.</div>
            <p class="body-soft" style="margin-top:14px; max-width:280px;">An AI-powered atelier for travel across India. Built for travellers who want their journeys to feel as beautiful as the places themselves.</p>
        </div>
        <div style="flex:1; min-width:160px;">
            <div class="eyebrow">Explore</div>
            <ul style="list-style:none; padding:0; margin:14px 0; color:rgba(245,241,232,0.7); line-height:2;">
                <li>Destinations</li><li>AI Concierge</li><li>Trip Architect</li><li>Hidden Worlds</li>
            </ul>
        </div>
        <div style="flex:1; min-width:160px;">
            <div class="eyebrow">Tools</div>
            <ul style="list-style:none; padding:0; margin:14px 0; color:rgba(245,241,232,0.7); line-height:2;">
                <li>Budget Intelligence</li><li>Smart Packing</li><li>Culinary Journey</li><li>Memory Journal</li>
            </ul>
        </div>
        <div style="flex:1; min-width:220px;">
            <div class="eyebrow">Newsletter</div>
            <p class="body-soft" style="margin:14px 0;">A monthly dispatch of hidden Indian destinations and seasonal travel notes.</p>
        </div>
    </div>
    <div class="gold-divider"></div>
    <div style="text-align:center; color:rgba(245,241,232,0.4); font-size:12px; padding:10px 0 30px;">
        © 2026 ATLASANDS · Crafted with intention.
    </div>
    """,
    unsafe_allow_html=True,
)
