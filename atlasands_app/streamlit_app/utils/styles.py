"""Premium luxury CSS injection for ATLASANDS — supports dark & light themes."""
import streamlit as st


THEMES = {
    "dark": {
        "gold": "#D4AF37", "gold_soft": "#E8C77A", "gold_dim": "#8C7A3E",
        "ivory": "#F5F1E8", "pearl": "#ECE6D8",
        "bg_grad": "radial-gradient(1200px 800px at 80% -10%, rgba(212,175,55,0.08), transparent 60%), radial-gradient(900px 700px at -10% 30%, rgba(14,23,51,0.55), transparent 60%), linear-gradient(180deg, #07070D 0%, #0A0A0F 60%, #0B0B14 100%)",
        "text": "#F5F1E8", "text_soft": "rgba(245,241,232,0.72)", "text_dim": "rgba(245,241,232,0.55)",
        "glass": "rgba(255, 255, 255, 0.04)", "glass_strong": "rgba(255, 255, 255, 0.07)",
        "border": "rgba(212, 175, 55, 0.22)", "border_soft": "rgba(255,255,255,0.06)",
        "shadow": "0 30px 60px -20px rgba(0,0,0,0.55), 0 18px 36px -18px rgba(0,0,0,0.4)",
        "input_bg": "rgba(255,255,255,0.04)", "input_border": "rgba(245,241,232,0.12)",
        "sidebar_bg": "linear-gradient(180deg, #07070D 0%, #0A0A14 100%)",
        "scroll_track": "#07070D", "scroll_thumb": "linear-gradient(180deg, #2A2A38, #1A1A24)",
        "display_grad": "linear-gradient(180deg, #FFF7E1 0%, #D4AF37 70%, #8C7A3E 100%)",
    },
    "light": {
        "gold": "#B8860B", "gold_soft": "#D4AF37", "gold_dim": "#8C6510",
        "ivory": "#0E1733", "pearl": "#1A2440",
        "bg_grad": "radial-gradient(1100px 700px at 80% -10%, rgba(184,134,11,0.10), transparent 60%), radial-gradient(900px 700px at -10% 30%, rgba(212,175,55,0.06), transparent 60%), linear-gradient(180deg, #FDF8EE 0%, #F6EFE0 60%, #EEE5D2 100%)",
        "text": "#0E1733", "text_soft": "rgba(14,23,51,0.72)", "text_dim": "rgba(14,23,51,0.55)",
        "glass": "rgba(255,255,255,0.55)", "glass_strong": "rgba(255,255,255,0.78)",
        "border": "rgba(184,134,11,0.28)", "border_soft": "rgba(14,23,51,0.08)",
        "shadow": "0 22px 50px -20px rgba(14,23,51,0.18), 0 10px 28px -14px rgba(14,23,51,0.12)",
        "input_bg": "rgba(255,255,255,0.7)", "input_border": "rgba(14,23,51,0.15)",
        "sidebar_bg": "linear-gradient(180deg, #F8F1E0 0%, #EEE5D2 100%)",
        "scroll_track": "#EEE5D2", "scroll_thumb": "linear-gradient(180deg, #B8860B, #8C6510)",
        "display_grad": "linear-gradient(180deg, #1A2440 0%, #B8860B 60%, #8C6510 100%)",
    },
}


def get_theme() -> str:
    return st.session_state.get("theme", "dark")


def set_theme(t: str):
    if t in THEMES:
        st.session_state["theme"] = t


def inject_global_styles():
    theme = get_theme()
    t = THEMES[theme]
    st.markdown(
        f"""
        <link rel="preconnect" href="https://fonts.googleapis.com">
        <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
        <link href="https://fonts.googleapis.com/css2?family=Playfair+Display:ital,wght@0,400;0,500;0,600;0,700;0,800;1,400&family=Cormorant+Garamond:ital,wght@0,300;0,400;0,500;0,600;0,700;1,400&family=Inter:wght@300;400;500;600;700&display=swap" rel="stylesheet">

        <style>
        :root {{
            --gold: {t['gold']};
            --gold-soft: {t['gold_soft']};
            --gold-dim: {t['gold_dim']};
            --ivory: {t['ivory']};
            --pearl: {t['pearl']};
            --text: {t['text']};
            --text-soft: {t['text_soft']};
            --text-dim: {t['text_dim']};
            --glass: {t['glass']};
            --glass-strong: {t['glass_strong']};
            --border: {t['border']};
            --border-soft: {t['border_soft']};
            --shadow: {t['shadow']};
            --input-bg: {t['input_bg']};
            --input-border: {t['input_border']};
        }}

        html, body, [class*="stApp"] {{
            background: {t['bg_grad']} !important;
            color: var(--text) !important;
            font-family: 'Inter', sans-serif !important;
            letter-spacing: 0.01em;
        }}

        #MainMenu, footer {{ visibility: hidden; }}
        header [data-testid="stHeader"] {{ background: transparent; }}
        .stDeployButton {{ display: none; }}

        h1, h2, h3, .editorial {{
            font-family: 'Playfair Display', serif !important;
            color: var(--text) !important;
            letter-spacing: -0.01em;
            line-height: 1.05;
        }}
        h1 {{ font-weight: 700 !important; }}
        .display-1 {{
            font-family: 'Playfair Display', serif;
            font-size: clamp(48px, 7vw, 96px);
            font-weight: 700;
            line-height: 1.02;
            background: {t['display_grad']};
            -webkit-background-clip: text;
            background-clip: text;
            color: transparent;
            text-shadow: 0 8px 40px rgba(212,175,55,0.15);
        }}
        .eyebrow {{
            font-family: 'Inter', sans-serif;
            text-transform: uppercase;
            letter-spacing: 0.42em;
            font-size: 11px;
            color: var(--gold);
            font-weight: 500;
        }}
        .serif-quote {{
            font-family: 'Cormorant Garamond', serif;
            font-style: italic;
            font-weight: 400;
            font-size: 22px;
            color: var(--text-soft);
            line-height: 1.55;
        }}
        .body-soft {{ color: var(--text-soft); font-size: 15px; line-height: 1.7; }}

        .stButton > button, .stDownloadButton > button, .stFormSubmitButton > button {{
            background: linear-gradient(135deg, var(--gold-soft) 0%, var(--gold-dim) 100%) !important;
            color: #0A0A0F !important;
            border: 1px solid rgba(212,175,55,0.4) !important;
            border-radius: 999px !important;
            padding: 0.7rem 1.6rem !important;
            font-family: 'Inter', sans-serif !important;
            font-weight: 600 !important;
            letter-spacing: 0.08em !important;
            text-transform: uppercase !important;
            font-size: 12px !important;
            box-shadow: 0 10px 30px -10px rgba(212,175,55,0.55), inset 0 1px 0 rgba(255,255,255,0.25);
            transition: transform .35s cubic-bezier(.2,.8,.2,1), box-shadow .35s, filter .35s;
        }}
        .stButton > button:hover, .stDownloadButton > button:hover, .stFormSubmitButton > button:hover {{
            transform: translateY(-2px) scale(1.02);
            box-shadow: 0 18px 45px -12px rgba(212,175,55,0.75);
            filter: brightness(1.08);
        }}
        .ghost .stButton > button {{
            background: transparent !important;
            color: var(--text) !important;
            border: 1px solid var(--input-border) !important;
            box-shadow: none !important;
        }}
        .ghost .stButton > button:hover {{
            border-color: var(--gold) !important;
            color: var(--gold) !important;
        }}

        .stTextInput input, .stTextArea textarea, .stNumberInput input, .stDateInput input,
        .stSelectbox [data-baseweb="select"] > div, .stMultiSelect [data-baseweb="select"] > div {{
            background: var(--input-bg) !important;
            color: var(--text) !important;
            border: 1px solid var(--input-border) !important;
            border-radius: 14px !important;
            backdrop-filter: blur(14px);
        }}
        .stTextInput input:focus, .stTextArea textarea:focus, .stNumberInput input:focus {{
            border-color: var(--gold) !important;
            box-shadow: 0 0 0 3px rgba(212,175,55,0.18) !important;
        }}
        label, .stMarkdown label {{ color: var(--text-soft) !important; font-weight: 500; letter-spacing: 0.04em; }}

        .glass {{
            background: var(--glass);
            border: 1px solid var(--border-soft);
            border-radius: 22px;
            padding: 28px;
            backdrop-filter: blur(22px);
            -webkit-backdrop-filter: blur(22px);
            box-shadow: var(--shadow);
            transition: transform .5s cubic-bezier(.2,.8,.2,1), border-color .5s, box-shadow .5s;
        }}
        .glass:hover {{
            transform: translateY(-4px);
            border-color: var(--border);
        }}
        .glass-strong {{
            background: var(--glass-strong);
            border: 1px solid var(--border);
            border-radius: 22px;
            padding: 28px;
            backdrop-filter: blur(22px);
            box-shadow: var(--shadow);
        }}
        .gold-divider {{
            height: 1px;
            background: linear-gradient(90deg, transparent, var(--gold), transparent);
            margin: 28px 0;
            opacity: 0.6;
        }}

        .dest-card {{
            position: relative;
            border-radius: 22px;
            overflow: hidden;
            height: 420px;
            box-shadow: var(--shadow);
            border: 1px solid var(--border-soft);
            transition: transform .6s cubic-bezier(.2,.8,.2,1), box-shadow .6s;
            cursor: pointer;
        }}
        .dest-card:hover {{ transform: translateY(-6px); box-shadow: 0 40px 70px -20px rgba(0,0,0,0.7); }}
        .dest-card img {{
            width: 100%; height: 100%; object-fit: cover;
            transition: transform 1.4s cubic-bezier(.2,.8,.2,1), filter .6s;
            filter: saturate(1.05) contrast(1.02);
        }}
        .dest-card:hover img {{ transform: scale(1.08); filter: saturate(1.15); }}
        .dest-overlay {{
            position: absolute; inset: 0;
            background: linear-gradient(180deg, rgba(7,7,13,0.05) 35%, rgba(7,7,13,0.85) 95%);
            display: flex; flex-direction: column; justify-content: flex-end;
            padding: 24px; gap: 6px;
        }}
        .dest-tag {{
            display: inline-block; padding: 4px 10px; border-radius: 999px;
            background: rgba(212,175,55,0.15); color: var(--gold);
            font-size: 10px; letter-spacing: 0.2em; text-transform: uppercase;
            border: 1px solid rgba(212,175,55,0.35); width: fit-content;
        }}
        .dest-title {{ font-family: 'Playfair Display', serif; font-size: 26px; color: #F5F1E8; font-weight: 600; line-height: 1.15; }}
        .dest-meta {{ color: rgba(245,241,232,0.7); font-size: 13px; }}
        .dest-budget {{ color: var(--gold); font-weight: 600; font-size: 13px; letter-spacing: 0.08em; }}
        .fav-badge {{
            position: absolute; top: 16px; right: 16px; z-index: 2;
            width: 38px; height: 38px; border-radius: 50%;
            background: rgba(0,0,0,0.45); backdrop-filter: blur(10px);
            border: 1px solid rgba(212,175,55,0.5);
            display: flex; align-items: center; justify-content: center;
            color: var(--gold); font-size: 16px;
        }}
        .fav-badge.saved {{ background: rgba(212,175,55,0.85); color: #0A0A0F; }}

        .hero-wrap {{
            position: relative; border-radius: 28px; overflow: hidden;
            min-height: 78vh; padding: 60px 40px;
            border: 1px solid var(--border-soft);
            box-shadow: var(--shadow);
        }}
        .hero-bg-img {{
            position: absolute; inset: 0; width: 100%; height: 100%;
            object-fit: cover;
            transform: scale(1.05);
            animation: kenburns 22s ease-in-out infinite alternate;
            filter: brightness(0.55) saturate(1.1);
            z-index: 0;
        }}
        .hero-grain {{ position:absolute; inset:0; background-image: url("data:image/svg+xml;utf8,<svg xmlns='http://www.w3.org/2000/svg' width='160' height='160' viewBox='0 0 160 160'><filter id='n'><feTurbulence type='fractalNoise' baseFrequency='0.9' numOctaves='2' stitchTiles='stitch'/><feColorMatrix values='0 0 0 0 1 0 0 0 0 1 0 0 0 0 1 0 0 0 0.18 0'/></filter><rect width='100%' height='100%' filter='url(%23n)'/></svg>"); mix-blend-mode: overlay; opacity:.5; pointer-events:none; }}
        .hero-vignette {{
            position:absolute; inset:0;
            background: radial-gradient(circle at 50% 60%, transparent 30%, rgba(7,7,13,0.85) 100%);
            pointer-events:none;
        }}
        .hero-inner {{ position: relative; z-index: 2; max-width: 880px; }}
        .hero-inner .display-1 {{
            color: #FFF7E1 !important;
            background: linear-gradient(180deg, #FFF7E1 0%, #E8C77A 70%, #8C7A3E 100%);
            -webkit-background-clip: text; background-clip: text;
        }}
        .hero-inner .serif-quote {{ color: rgba(255,247,225,0.85); }}
        @keyframes kenburns {{
            0% {{ transform: scale(1.05) translate(0,0); }}
            100% {{ transform: scale(1.16) translate(-1.5%, -1%); }}
        }}

        .feature-pill {{
            display:flex; align-items:center; gap:14px;
            padding: 18px 20px; border-radius: 18px;
            background: var(--glass);
            border: 1px solid var(--border-soft);
            transition: all .4s ease;
            cursor: default;
        }}
        .feature-pill:hover {{ border-color: var(--border); background: var(--glass-strong); transform: translateY(-3px); }}
        .feature-icon {{
            width: 46px; height: 46px; border-radius: 14px;
            background: linear-gradient(135deg, rgba(212,175,55,0.25), rgba(212,175,55,0.05));
            border: 1px solid rgba(212,175,55,0.4);
            display:flex; align-items:center; justify-content:center;
            color: var(--gold); font-size: 20px;
        }}
        .feature-title {{ font-family: 'Playfair Display', serif; font-size: 18px; color: var(--text); }}
        .feature-desc {{ color: var(--text-dim); font-size: 13px; line-height:1.5; }}

        .stat {{ text-align:center; padding: 26px 12px; }}
        .stat-num {{
            font-family: 'Playfair Display', serif; font-size: 56px; font-weight: 700;
            background: {t['display_grad']};
            -webkit-background-clip: text; background-clip: text; color: transparent;
            line-height: 1;
        }}
        .stat-label {{ color: var(--text-dim); letter-spacing: 0.25em; text-transform: uppercase; font-size: 11px; margin-top: 10px; }}

        .orb-wrap {{ display:flex; justify-content:center; padding: 12px 0; }}
        .ai-orb {{
            width: 110px; height: 110px; border-radius: 50%;
            background: radial-gradient(circle at 30% 30%, #F8E7A3, #D4AF37 45%, #5a4715 80%);
            box-shadow: 0 0 60px rgba(212,175,55,0.55), inset 0 0 30px rgba(255,255,255,0.25);
            animation: breathe 4s ease-in-out infinite, float 7s ease-in-out infinite;
            position: relative;
        }}
        .ai-orb::after {{
            content:""; position:absolute; inset:-14px; border-radius:50%;
            border: 1px dashed rgba(212,175,55,0.4);
            animation: spin 18s linear infinite;
        }}
        @keyframes breathe {{ 0%,100%{{ transform: scale(1); }} 50%{{ transform: scale(1.05); }} }}
        @keyframes float {{ 0%,100%{{ translate: 0 0; }} 50%{{ translate: 0 -6px; }} }}
        @keyframes spin {{ to {{ transform: rotate(360deg); }} }}

        /* Floating concierge orb (every page, bottom-right) */
        .floating-orb {{
            position: fixed; bottom: 28px; right: 28px; z-index: 9998;
            width: 64px; height: 64px; border-radius: 50%;
            background: radial-gradient(circle at 30% 30%, #F8E7A3, #D4AF37 50%, #5a4715 85%);
            box-shadow: 0 0 40px rgba(212,175,55,0.55), 0 12px 28px -8px rgba(0,0,0,0.55), inset 0 0 18px rgba(255,255,255,0.25);
            animation: breathe 4s ease-in-out infinite, float 7s ease-in-out infinite;
            display: flex; align-items: center; justify-content: center;
            color: #0A0A0F; font-size: 26px;
            text-decoration: none !important;
            transition: transform .35s cubic-bezier(.2,.8,.2,1), box-shadow .35s;
            cursor: pointer;
        }}
        .floating-orb:hover {{
            transform: scale(1.08);
            box-shadow: 0 0 60px rgba(212,175,55,0.75), 0 14px 32px -8px rgba(0,0,0,0.7);
        }}
        .floating-orb::after {{
            content:""; position:absolute; inset:-10px; border-radius:50%;
            border: 1px dashed rgba(212,175,55,0.35);
            animation: spin 18s linear infinite;
            pointer-events:none;
        }}
        .floating-orb .orb-tooltip {{
            position: absolute; right: 78px; top: 50%; transform: translateY(-50%) translateX(8px);
            background: rgba(10,10,15,0.92); color: #F5F1E8;
            padding: 9px 14px; border-radius: 999px;
            font-family: 'Inter', sans-serif; font-size: 11px; letter-spacing: 0.18em;
            text-transform: uppercase; border: 1px solid rgba(212,175,55,0.35);
            opacity: 0; pointer-events: none; transition: opacity .3s, transform .3s; white-space: nowrap;
        }}
        .floating-orb:hover .orb-tooltip {{ opacity: 1; transform: translateY(-50%) translateX(0); }}

        .chat-row {{ display:flex; gap:12px; margin: 10px 0; }}
        .chat-bubble {{
            padding: 14px 18px; border-radius: 18px; max-width: 78%;
            font-size: 15px; line-height: 1.55;
            backdrop-filter: blur(16px);
            border: 1px solid var(--border-soft);
            animation: bubbleIn .45s cubic-bezier(.2,.8,.2,1);
        }}
        @keyframes bubbleIn {{ from {{ opacity:0; transform: translateY(8px);}} to {{ opacity:1; transform:none; }} }}
        .chat-user {{ margin-left:auto; background: linear-gradient(135deg, rgba(212,175,55,0.18), rgba(212,175,55,0.06)); color: var(--text); border-color: rgba(212,175,55,0.3); }}
        .chat-bot {{ margin-right:auto; background: var(--glass-strong); color: var(--text); }}
        .chat-avatar {{
            width:34px; height:34px; border-radius:50%;
            background: radial-gradient(circle at 30% 30%, #F8E7A3, #8C7A3E);
            flex-shrink:0;
        }}

        [data-testid="stSidebar"] {{
            background: {t['sidebar_bg']} !important;
            border-right: 1px solid var(--border-soft);
        }}
        [data-testid="stSidebar"] * {{ color: var(--text); }}
        [data-testid="stSidebar"] .stMarkdown h1,
        [data-testid="stSidebar"] .stMarkdown h2 {{ color: var(--gold) !important; }}

        .stTabs [data-baseweb="tab-list"] {{ gap: 6px; }}
        .stTabs [data-baseweb="tab"] {{
            background: var(--glass); border-radius: 999px;
            padding: 8px 18px; color: var(--text-soft);
            border: 1px solid var(--border-soft);
        }}
        .stTabs [aria-selected="true"] {{
            background: linear-gradient(135deg, rgba(212,175,55,0.25), rgba(212,175,55,0.08));
            color: var(--gold) !important;
            border-color: rgba(212,175,55,0.45) !important;
        }}

        [data-testid="stMetricValue"] {{
            font-family: 'Playfair Display', serif !important;
            color: var(--gold) !important;
            font-weight: 600 !important;
        }}
        .stProgress > div > div > div > div {{ background: linear-gradient(90deg, var(--gold), var(--gold-soft)) !important; }}

        .fade-in {{ animation: fadeIn 1.1s cubic-bezier(.2,.8,.2,1) both; }}
        @keyframes fadeIn {{ from {{ opacity:0; transform: translateY(14px); }} to {{ opacity:1; transform:none; }} }}
        .delay-1 {{ animation-delay: .15s; }}
        .delay-2 {{ animation-delay: .3s; }}
        .delay-3 {{ animation-delay: .45s; }}

        .block-container {{ padding-top: 2rem !important; padding-bottom: 4rem !important; max-width: 1280px; }}

        .streamlit-expanderHeader, [data-testid="stExpander"] details summary {{
            background: var(--glass) !important;
            border-radius: 14px !important;
            color: var(--text) !important;
        }}

        .auth-card {{
            max-width: 460px; margin: 0 auto; padding: 36px;
            background: var(--glass-strong);
            border: 1px solid var(--border);
            border-radius: 26px;
            backdrop-filter: blur(24px);
            box-shadow: var(--shadow);
        }}

        ::-webkit-scrollbar {{ width: 10px; height: 10px; }}
        ::-webkit-scrollbar-track {{ background: {t['scroll_track']}; }}
        ::-webkit-scrollbar-thumb {{ background: {t['scroll_thumb']}; border-radius: 999px; }}
        ::-webkit-scrollbar-thumb:hover {{ background: linear-gradient(180deg, #D4AF37, #8C7A3E); }}

        @media (max-width: 760px) {{
            .display-1 {{ font-size: 44px; }}
            .hero-wrap {{ padding: 36px 22px; min-height: 70vh; }}
            .dest-card {{ height: 360px; }}
            .floating-orb {{ width: 56px; height: 56px; bottom: 18px; right: 18px; font-size: 22px; }}
        }}
        </style>
        """,
        unsafe_allow_html=True,
    )


def render_floating_orb():
    """Floating AI Concierge orb visible on every page. Clicking opens the Concierge."""
    st.markdown(
        """
        <a class="floating-orb" href="/AI_Concierge" target="_top" aria-label="Open AI Concierge">
            <span style="filter: drop-shadow(0 1px 2px rgba(0,0,0,0.3));">✦</span>
            <span class="orb-tooltip">Ask the Concierge</span>
        </a>
        """,
        unsafe_allow_html=True,
    )


def render_theme_toggle(key_suffix: str = "main"):
    """Theme toggle to be placed in the sidebar."""
    current = get_theme()
    label = "☾  Dark Mode" if current == "dark" else "☀  Light Mode"
    if st.button(label, key=f"theme_toggle_{key_suffix}", use_container_width=True):
        set_theme("light" if current == "dark" else "dark")
        st.rerun()


def hero(image_url: str, eyebrow: str, title_html: str, subtitle: str):
    st.markdown(
        f"""
        <div class="hero-wrap fade-in">
            <img class="hero-bg-img" src="{image_url}" alt=""/>
            <div class="hero-grain"></div>
            <div class="hero-vignette"></div>
            <div class="hero-inner">
                <div class="eyebrow fade-in delay-1" style="color:#E8C77A;">{eyebrow}</div>
                <h1 class="display-1 fade-in delay-2" style="margin: 18px 0 22px;">{title_html}</h1>
                <p class="serif-quote fade-in delay-3" style="max-width:640px;">{subtitle}</p>
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )


def section_header(eyebrow: str, title: str, subtitle: str = ""):
    sub = f'<p class="body-soft" style="max-width:640px;margin-top:10px;">{subtitle}</p>' if subtitle else ""
    st.markdown(
        f"""
        <div class="fade-in" style="margin: 60px 0 28px;">
            <div class="eyebrow">{eyebrow}</div>
            <h2 style="font-size: clamp(32px, 4.4vw, 52px); margin: 12px 0 0;">{title}</h2>
            {sub}
            <div class="gold-divider" style="margin-top:18px;"></div>
        </div>
        """,
        unsafe_allow_html=True,
    )
