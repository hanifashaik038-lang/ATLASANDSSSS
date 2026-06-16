"""SQLite-backed storage for users, journals, saved trips, favorites."""
import sqlite3
from contextlib import contextmanager
from pathlib import Path
from datetime import datetime, timezone

DB_PATH = Path(__file__).parent.parent / "atlasands.db"


@contextmanager
def get_conn():
    conn = sqlite3.connect(str(DB_PATH), check_same_thread=False)
    conn.row_factory = sqlite3.Row
    try:
        yield conn
        conn.commit()
    finally:
        conn.close()


def init_db():
    with get_conn() as c:
        c.executescript(
            """
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                email TEXT UNIQUE NOT NULL,
                name TEXT NOT NULL,
                password_hash TEXT NOT NULL,
                created_at TEXT NOT NULL
            );
            CREATE TABLE IF NOT EXISTS favorites (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                user_id INTEGER NOT NULL,
                destination_id TEXT NOT NULL,
                created_at TEXT NOT NULL,
                UNIQUE(user_id, destination_id),
                FOREIGN KEY (user_id) REFERENCES users(id)
            );
            CREATE TABLE IF NOT EXISTS trips (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                user_id INTEGER NOT NULL,
                title TEXT NOT NULL,
                payload_json TEXT NOT NULL,
                created_at TEXT NOT NULL,
                FOREIGN KEY (user_id) REFERENCES users(id)
            );
            CREATE TABLE IF NOT EXISTS journals (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                user_id INTEGER NOT NULL,
                title TEXT NOT NULL,
                location TEXT,
                date TEXT,
                body TEXT NOT NULL,
                ai_story TEXT,
                created_at TEXT NOT NULL,
                FOREIGN KEY (user_id) REFERENCES users(id)
            );
            CREATE TABLE IF NOT EXISTS chat_history (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                user_id INTEGER NOT NULL,
                role TEXT NOT NULL,
                content TEXT NOT NULL,
                created_at TEXT NOT NULL,
                FOREIGN KEY (user_id) REFERENCES users(id)
            );
            """
        )


def now_iso() -> str:
    return datetime.now(timezone.utc).isoformat()


# ----- Favorites helpers -----
def get_favorites(user_id: int) -> set[str]:
    with get_conn() as c:
        rows = c.execute("SELECT destination_id FROM favorites WHERE user_id = ?", (user_id,)).fetchall()
    return {r["destination_id"] for r in rows}


def toggle_favorite(user_id: int, destination_id: str) -> bool:
    """Returns True if now favorited, False if removed."""
    with get_conn() as c:
        row = c.execute(
            "SELECT id FROM favorites WHERE user_id = ? AND destination_id = ?",
            (user_id, destination_id),
        ).fetchone()
        if row:
            c.execute("DELETE FROM favorites WHERE id = ?", (row["id"],))
            return False
        c.execute(
            "INSERT INTO favorites (user_id, destination_id, created_at) VALUES (?,?,?)",
            (user_id, destination_id, now_iso()),
        )
        return True
