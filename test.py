import sqlite3

def insert_test_data():
    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    # Cases
    c.execute("INSERT INTO cases (incident_date, location, description, age) VALUES (?, ?, ?, ?)",
              ('2025-06-10', 'Nairobi', 'Sample case 1', 25))
    # Survivor Stories
    c.execute("INSERT INTO survivor_stories (story, is_approved) VALUES (?, ?)",
              ('A story of resilience', 1))
    # Helplines
    c.execute("INSERT INTO helplines (organization_name, phone_number, region, description) VALUES (?, ?, ?, ?)",
              ('Support Org', '123-456-7890', 'Nairobi', 'Emergency support'))
    # Community Hub
    c.execute("INSERT INTO community_hub (event_name, description, date, location) VALUES (?, ?, ?, ?)",
              ('Awareness Rally', 'Femicide awareness', '2025-07-01', 'Nairobi'))
    # Assistance
    c.execute("INSERT INTO assistance (service_type, provider_name, contact_info, region) VALUES (?, ?, ?, ?)",
              ('Legal', 'Legal Aid Org', '123-4567', 'Nairobi'))
    # Fundraising
    c.execute("INSERT INTO fundraising (campaign_name, goal_amount, description) VALUES (?, ?, ?)",
              ('Survivor Fund', 10000.0, 'Support survivors'))
    conn.commit()
    conn.close()
    print("Test data inserted!")

if __name__ == "__main__":
    insert_test_data()