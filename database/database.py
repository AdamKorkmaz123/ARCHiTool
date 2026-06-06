import sqlite3
import json

DB_PATH = "database/projects.db"


def init_db():
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()

    cur.execute("""
    CREATE TABLE IF NOT EXISTS projects (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_id INTEGER,
        projektname TEXT,
        firma TEXT,
        bauherr TEXT,
        datum TEXT,
        json_data TEXT
    )
    """)

    conn.commit()
    conn.close()


def save_project(user_id, projektname, firma, bauherr, datum, json_data):
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()

    cur.execute("""
    INSERT INTO projects (
        user_id,
        projektname,
        firma,
        bauherr,
        datum,
        json_data
    )
    VALUES (?, ?, ?, ?, ?, ?)
    """, (
        user_id,
        projektname,
        firma,
        bauherr,
        datum,
        json.dumps(json_data, ensure_ascii=False)
    ))

    conn.commit()
    conn.close()


def load_projects(user_id=None):
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()

    if user_id:
        cur.execute("""
        SELECT id, projektname, firma, datum
        FROM projects
        WHERE user_id = ?
        ORDER BY id DESC
        """, (user_id,))
    else:
        cur.execute("""
        SELECT id, projektname, firma, datum
        FROM projects
        ORDER BY id DESC
        """)

    rows = cur.fetchall()
    conn.close()

    return rows


def load_project_data(project_id, user_id=None):
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()

    if user_id:
        cur.execute("""
        SELECT json_data
        FROM projects
        WHERE id = ? AND user_id = ?
        """, (project_id, user_id))
    else:
        cur.execute("""
        SELECT json_data
        FROM projects
        WHERE id = ?
        """, (project_id,))

    row = cur.fetchone()
    conn.close()

    if row:
        return json.loads(row[0])

    return None


def delete_project(project_id, user_id=None):
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()

    if user_id:
        cur.execute("""
        DELETE FROM projects
        WHERE id = ? AND user_id = ?
        """, (project_id, user_id))
    else:
        cur.execute("""
        DELETE FROM projects
        WHERE id = ?
        """, (project_id,))

    conn.commit()
    conn.close()