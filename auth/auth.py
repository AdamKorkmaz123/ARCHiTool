import sqlite3
import hashlib
import os


DB_PATH = "database/users.db"


def hash_password(password):
    salt = os.urandom(16)
    hashed = hashlib.pbkdf2_hmac(
        "sha256",
        password.encode(),
        salt,
        100000
    )
    return salt.hex() + ":" + hashed.hex()


def verify_password(password, stored_password):
    salt_hex, hash_hex = stored_password.split(":")
    salt = bytes.fromhex(salt_hex)
    hashed = hashlib.pbkdf2_hmac(
        "sha256",
        password.encode(),
        salt,
        100000
    )
    return hashed.hex() == hash_hex


def init_auth_db():
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()

    cur.execute("""
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        email TEXT UNIQUE,
        password TEXT
    )
    """)

    conn.commit()
    conn.close()


def register_user(name, email, password):
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()

    try:
        cur.execute("""
        INSERT INTO users (name, email, password)
        VALUES (?, ?, ?)
        """, (
            name,
            email,
            hash_password(password)
        ))

        conn.commit()
        return True, "Benutzer erfolgreich registriert."

    except sqlite3.IntegrityError:
        return False, "Diese E-Mail ist bereits registriert."

    finally:
        conn.close()


def login_user(email, password):
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()

    cur.execute("""
    SELECT id, name, email, password
    FROM users
    WHERE email = ?
    """, (email,))

    user = cur.fetchone()
    conn.close()

    if not user:
        return False, None, "Benutzer nicht gefunden."

    user_id, name, email, stored_password = user

    if verify_password(password, stored_password):
        return True, {
            "id": user_id,
            "name": name,
            "email": email
        }, "Login erfolgreich."

    return False, None, "Passwort ist falsch."

def save_user_settings(user_id, dark_mode, primary_color):
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()

    cur.execute("""
    CREATE TABLE IF NOT EXISTS user_settings (
        user_id INTEGER PRIMARY KEY,
        dark_mode INTEGER,
        primary_color TEXT
    )
    """)

    cur.execute("""
    INSERT OR REPLACE INTO user_settings (
        user_id, dark_mode, primary_color
    )
    VALUES (?, ?, ?)
    """, (
        user_id,
        int(dark_mode),
        primary_color
    ))

    conn.commit()
    conn.close()


def load_user_settings(user_id):
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()

    cur.execute("""
    CREATE TABLE IF NOT EXISTS user_settings (
        user_id INTEGER PRIMARY KEY,
        dark_mode INTEGER,
        primary_color TEXT
    )
    """)

    cur.execute("""
    SELECT dark_mode, primary_color
    FROM user_settings
    WHERE user_id = ?
    """, (user_id,))

    row = cur.fetchone()
    conn.close()

    if row:
        return {
            "dark_mode": bool(row[0]),
            "primary_color": row[1]
        }

    return {
        "dark_mode": False,
        "primary_color": "#1e3a8a"
    }