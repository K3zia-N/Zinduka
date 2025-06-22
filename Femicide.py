import sqlite3

def init_db():
    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS cases (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        incident_date DATE,
        location TEXT NOT NULL,
        description TEXT NOT NULL,
        age INTEGER,
        submitted_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )''')
    c.execute('''CREATE TABLE IF NOT EXISTS survivor_stories (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        story TEXT NOT NULL,
        is_approved BOOLEAN DEFAULT FALSE,
        submitted_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )''')
    c.execute('''CREATE TABLE IF NOT EXISTS helplines (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        organization_name TEXT NOT NULL,
        phone_number TEXT NOT NULL,
        region TEXT NOT NULL,
        description TEXT
    )''')
    c.execute('''CREATE TABLE IF NOT EXISTS community_hub (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        event_name TEXT NOT NULL,
        description TEXT,
        date DATE,
        location TEXT,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )''')
    c.execute('''CREATE TABLE IF NOT EXISTS assistance (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        service_type TEXT NOT NULL,
        provider_name TEXT NOT NULL,
        contact_info TEXT,
        region TEXT
    )''')
    c.execute('''CREATE TABLE IF NOT EXISTS fundraising (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        campaign_name TEXT NOT NULL,
        goal_amount REAL,
        current_amount REAL DEFAULT 0,
        description TEXT,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )''')
    conn.commit()
    conn.close()
    print("Database initialized successfully!")

if __name__ == "__main__":
    init_db()