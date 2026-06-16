"""AI Concierge — 100+ Q&A static knowledge base, never fails."""
import streamlit as st
from utils.styles import inject_global_styles, hero
from utils.knowledge_base import find_best_answer, SUGGESTED_QUESTIONS
from utils.destinations import HERO_SLIDES
from utils.auth import ensure_session
from utils.database import get_conn, init_db, now_iso

st.set_page_config(page_title="AI Concierge · ATLASANDS", page_icon="🤖", layout="wide", initial_sidebar_state="collapsed")
inject_global_styles()
init_db()

user = ensure_session()

hero(
    image_url=HERO_SLIDES[1]["image"],
    eyebrow="AI CONCIERGE · ALWAYS ON",
    title_html="A Quiet Intelligence,<br/>For The Loudest Continent.",
    subtitle="Ask anything — destinations, seasons, costs, hidden corners. Trained on 100+ curated answers, the concierge never goes silent.",
)


if "chat" not in st.session_state:
    st.session_state.chat = [
        {"role": "bot", "content": "Namaste 🙏 I'm your ATLASANDS concierge. Whisper a destination, a budget or a feeling — let's begin shaping your journey."},
    ]


# ------- Concierge orb header -------
oc1, oc2 = st.columns([1, 2])
with oc1:
    st.markdown(
        """
        <div class="glass-strong" style="text-align:center;">
            <div class="orb-wrap"><div class="ai-orb"></div></div>
            <div class="eyebrow" style="margin-top:14px;">ATLAS · The Concierge</div>
            <p class="body-soft" style="margin-top:6px;">Online · responding instantly</p>
        </div>
        """,
        unsafe_allow_html=True,
    )
with oc2:
    st.markdown('<div class="eyebrow">Try asking</div>', unsafe_allow_html=True)
    qcols = st.columns(2)
    for i, sug in enumerate(SUGGESTED_QUESTIONS):
        with qcols[i % 2]:
            if st.button(sug, key=f"sug_{i}", use_container_width=True):
                st.session_state.chat.append({"role": "user", "content": sug})
                ans, _ = find_best_answer(sug)
                st.session_state.chat.append({"role": "bot", "content": ans})
                if user:
                    with get_conn() as c:
                        c.execute("INSERT INTO chat_history (user_id, role, content, created_at) VALUES (?,?,?,?)", (user["id"], "user", sug, now_iso()))
                        c.execute("INSERT INTO chat_history (user_id, role, content, created_at) VALUES (?,?,?,?)", (user["id"], "bot", ans, now_iso()))
                st.rerun()


st.markdown('<div class="gold-divider"></div>', unsafe_allow_html=True)


# ------- Chat transcript -------
chat_container = st.container()
with chat_container:
    for msg in st.session_state.chat:
        if msg["role"] == "user":
            st.markdown(
                f"""
                <div class="chat-row" style="justify-content:flex-end;">
                    <div class="chat-bubble chat-user">{msg['content']}</div>
                </div>
                """,
                unsafe_allow_html=True,
            )
        else:
            st.markdown(
                f"""
                <div class="chat-row">
                    <div class="chat-avatar"></div>
                    <div class="chat-bubble chat-bot">{msg['content']}</div>
                </div>
                """,
                unsafe_allow_html=True,
            )


# ------- Input -------
with st.form("chat_form", clear_on_submit=True):
    cols = st.columns([8, 1, 1])
    with cols[0]:
        prompt = st.text_input("Type your question", label_visibility="collapsed", placeholder="e.g. Best time for Spiti? Budget Kerala trip in 5 days?", key="chat_input")
    with cols[1]:
        send = st.form_submit_button("Send", use_container_width=True)
    with cols[2]:
        clear = st.form_submit_button("Clear", use_container_width=True)

if send and prompt and prompt.strip():
    st.session_state.chat.append({"role": "user", "content": prompt.strip()})
    answer, conf = find_best_answer(prompt.strip())
    st.session_state.chat.append({"role": "bot", "content": answer})
    if user:
        with get_conn() as c:
            c.execute("INSERT INTO chat_history (user_id, role, content, created_at) VALUES (?,?,?,?)", (user["id"], "user", prompt.strip(), now_iso()))
            c.execute("INSERT INTO chat_history (user_id, role, content, created_at) VALUES (?,?,?,?)", (user["id"], "bot", answer, now_iso()))
    st.rerun()

if clear:
    st.session_state.chat = [{"role": "bot", "content": "Cleared. Let's start fresh — where would you like to wander?"}]
    st.rerun()


st.markdown('<div class="gold-divider" style="margin-top:50px;"></div>', unsafe_allow_html=True)
st.markdown(
    """
    <div class="glass" style="margin-top:30px;">
        <div class="eyebrow">Concierge Notes</div>
        <p class="body-soft" style="margin-top:8px;">
            ATLAS is powered by a curated 100+ answer knowledge base — completely offline, never fails, and always honest.
            For day-by-day itineraries, open the <strong>Trip Architect</strong>; for budgets, open <strong>Budget Intelligence</strong>.
        </p>
    </div>
    """,
    unsafe_allow_html=True,
)
