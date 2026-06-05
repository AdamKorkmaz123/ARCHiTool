import sqlite3
import json
from datetime import datetime


DB_NAME = "database/projects.db"


def init_db():
    conn = sqlite3.connect(DB_NAME)
    cur = conn.cursor()

    cur.execute("""
    CREATE TABLE IF NOT EXISTS projects (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        projektname TEXT,
        firma TEXT,
        bauherr TEXT,
        ort TEXT,
        datum TEXT,
        created_at TEXT,
        updated_at TEXT,
        data TEXT
    )
    """)

    conn.commit()
    conn.close()


def save_project(projektname, firma, datum, data_dict):
    conn = sqlite3.connect(DB_NAME)
    cur = conn.cursor()

    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    meta = data_dict.get("meta", {})

    json_data = json.dumps(data_dict, ensure_ascii=False)

    cur.execute("""
    INSERT INTO projects (
        projektname,
        firma,
        bauherr,
        ort,
        datum,
        created_at,
        updated_at,
        data
    )
    VALUES (?, ?, ?, ?, ?, ?, ?, ?)
    """, (
        projektname,
        firma,
        meta.get("Bauherr", ""),
        meta.get("Ort", ""),
        datum,
        now,
        now,
        json_data
    ))

    conn.commit()
    conn.close()


def load_projects():
    conn = sqlite3.connect(DB_NAME)
    cur = conn.cursor()

    cur.execute("""
    SELECT id, projektname, firma, datum
    FROM projects
    ORDER BY id DESC
    """)

    rows = cur.fetchall()
    conn.close()

    return rows


def load_project_data(project_id):
    conn = sqlite3.connect(DB_NAME)
    cur = conn.cursor()

    cur.execute("""
    SELECT data
    FROM projects
    WHERE id = ?
    """, (project_id,))

    row = cur.fetchone()
    conn.close()

    if row:
        return json.loads(row[0])

    return None


def delete_project(project_id):
    conn = sqlite3.connect(DB_NAME)
    cur = conn.cursor()

    cur.execute("""
    DELETE FROM projects
    WHERE id = ?
    """, (project_id,))

    conn.commit()
    conn.close()