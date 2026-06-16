"""Email/password auth with bcrypt + JWT-style session tokens (stored in st.session_state)."""
import bcrypt
import jwt
import re
from datetime import datetime, timedelta, timezone
import streamlit as st

from utils.database import get_conn, init_db, now_iso

JWT_ALGO = "HS256"
SESSION_TTL_DAYS = 14
EMAIL_RE = re.compile(r"^[^@\s]+@[^@\s]+\.[^@\s]+$")


def _secret() -> str:
    try:
        return st.secrets["JWT_SECRET"]
    except Exception:
        return "atlasands-dev-secret-change-me"


def hash_password(pw: str) -> str:
    return bcrypt.hashpw(pw.encode(), bcrypt.gensalt(rounds=12)).decode()


def verify_password(pw: str, hashed: str) -> bool:
    try:
        return bcrypt.checkpw(pw.encode(), hashed.encode())
    except Exception:
        return False


def make_token(user_id: int, email: str) -> str:
    payload = {
        "sub": user_id,
        "email": email,
        "exp": datetime.now(timezone.utc) + timedelta(days=SESSION_TTL_DAYS),
        "iat": datetime.now(timezone.utc),
    }
    return jwt.encode(payload, _secret(), algorithm=JWT_ALGO)


def decode_token(token: str):
    try:
        return jwt.decode(token, _secret(), algorithms=[JWT_ALGO])
    except Exception:
        return None


def signup(email: str, name: str, password: str):
    email = email.strip().lower()
    name = name.strip()
    if not EMAIL_RE.match(email):
        return False, "Please enter a valid email address."
    if len(name) < 2:
        return False, "Name must be at least 2 characters."
    if len(password) < 8:
        return False, "Password must be at least 8 characters."
    init_db()
    with get_conn() as c:
        existing = c.execute("SELECT id FROM users WHERE email = ?", (email,)).fetchone()
        if existing:
            return False, "An account with this email already exists."
        cur = c.execute(
            "INSERT INTO users (email, name, password_hash, created_at) VALUES (?,?,?,?)",
            (email, name, hash_password(password), now_iso()),
        )
        user_id = cur.lastrowid
    return True, {"id": user_id, "email": email, "name": name}


def login(email: str, password: str):
    email = email.strip().lower()
    init_db()
    with get_conn() as c:
        row = c.execute("SELECT * FROM users WHERE email = ?", (email,)).fetchone()
    if not row or not verify_password(password, row["password_hash"]):
        return False, "Invalid email or password."
    user = {"id": row["id"], "email": row["email"], "name": row["name"]}
    return True, user


def ensure_session():
    """Initialize auth state. Returns user dict or None."""
    init_db()
    if "auth_token" in st.session_state:
        payload = decode_token(st.session_state["auth_token"])
        if payload:
            return {"id": payload["sub"], "email": payload["email"], "name": st.session_state.get("user_name", "")}
        # expired
        st.session_state.pop("auth_token", None)
    return None


def set_session(user: dict):
    st.session_state["auth_token"] = make_token(user["id"], user["email"])
    st.session_state["user_name"] = user["name"]
    st.session_state["user_id"] = user["id"]
    st.session_state["user_email"] = user["email"]


def clear_session():
    for k in ["auth_token", "user_name", "user_id", "user_email"]:
        st.session_state.pop(k, None)


def require_login():
    user = ensure_session()
    if not user:
        st.markdown(
            """
            <div class="glass-strong fade-in" style="text-align:center;margin-top:40px;">
                <div class="eyebrow">Private Lounge</div>
                <h2 style="margin:8px 0 12px;">Sign in to continue</h2>
                <p class="body-soft">This experience is reserved for ATLASANDS members. Please log in or create your account from the home page.</p>
            </div>
            """,
            unsafe_allow_html=True,
        )
        if st.button("Go to Home", key="goto_home_login"):
            st.switch_page("app.py")
        st.stop()
    return user
