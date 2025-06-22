from flask import Flask, request, jsonify, render_template
from datetime import datetime
from db import get_db_connection
from Femicide import init_db

app = Flask(__name__)
init_db()  # Initialize database

# Cases: Submit a case
@app.route('/api/cases', methods=['POST'])
def submit_case():
    try:
        data = request.get_json()
        incident_date = data.get('incident_date')
        location = data.get('location')
        description = data.get('description')
        age = data.get('age')
        if not all([incident_date, location, description]):
            return jsonify({'error': 'Missing required fields'}), 400
        conn = get_db_connection()
        c = conn.cursor()
        c.execute('''INSERT INTO cases (incident_date, location, description, age, submitted_at)
                     VALUES (?, ?, ?, ?, ?)''',
                  (incident_date, location, description, age, datetime.now()))
        conn.commit()
        conn.close()
        return jsonify({'message': 'Case submitted successfully'}), 201
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# Cases: Get all cases (for admin, optional)
@app.route('/api/cases', methods=['GET'])
def get_cases():
    try:
        conn = get_db_connection()
        c = conn.cursor()
        c.execute('SELECT * FROM cases')
        cases = [dict(row) for row in c.fetchall()]
        conn.close()
        return jsonify(cases), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# Survivor Stories: Submit a story
@app.route('/api/stories', methods=['POST'])
def submit_story():
    try:
        data = request.get_json()
        story = data.get('story')
        if not story:
            return jsonify({'error': 'Story is required'}), 400
        conn = get_db_connection()
        c = conn.cursor()
        c.execute('INSERT INTO survivor_stories (story, submitted_at) VALUES (?, ?)',
                  (story, datetime.now()))
        conn.commit()
        conn.close()
        return jsonify({'message': 'Story submitted for review'}), 201
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# Survivor Stories: Get approved stories
@app.route('/api/stories', methods=['GET'])
def get_stories():
    try:
        conn = get_db_connection()
        c = conn.cursor()
        c.execute('SELECT * FROM survivor_stories WHERE is_approved = 1')
        stories = [dict(row) for row in c.fetchall()]
        conn.close()
        return jsonify(stories), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# Helplines: Get helplines (filter by region)
@app.route('/api/helplines', methods=['GET'])
def get_helplines():
    try:
        region = request.args.get('region')
        conn = get_db_connection()
        c = conn.cursor()
        if region:
            c.execute('SELECT * FROM helplines WHERE region = ?', (region,))
        else:
            c.execute('SELECT * FROM helplines')
        helplines = [dict(row) for row in c.fetchall()]
        conn.close()
        return jsonify(helplines), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# Helplines: Add a helpline
@app.route('/api/helplines', methods=['POST'])
def add_helpline():
    try:
        data = request.get_json()
        organization_name = data.get('organization_name')
        phone_number = data.get('phone_number')
        region = data.get('region')
        description = data.get('description')
        if not all([organization_name, phone_number, region]):
            return jsonify({'error': 'Missing required fields'}), 400
        conn = get_db_connection()
        c = conn.cursor()
        c.execute('INSERT INTO helplines (organization_name, phone_number, region, description) VALUES (?, ?, ?, ?)',
                  (organization_name, phone_number, region, description))
        conn.commit()
        conn.close()
        return jsonify({'message': 'Helpline added successfully'}), 201
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# Community Hub: Get events
@app.route('/api/community/events', methods=['GET'])
def get_events():
    try:
        conn = get_db_connection()
        c = conn.cursor()
        c.execute('SELECT * FROM community_hub')
        events = [dict(row) for row in c.fetchall()]
        conn.close()
        return jsonify(events), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# Community Hub: Add an event
@app.route('/api/community/events', methods=['POST'])
def add_event():
    try:
        data = request.get_json()
        event_name = data.get('event_name')
        description = data.get('description')
        date = data.get('date')
        location = data.get('location')
        if not event_name:
            return jsonify({'error': 'Event name is required'}), 400
        conn = get_db_connection()
        c = conn.cursor()
        c.execute('INSERT INTO community_hub (event_name, description, date, location, created_at) VALUES (?, ?, ?, ?, ?)',
                  (event_name, description, date, location, datetime.now()))
        conn.commit()
        conn.close()
        return jsonify({'message': 'Event added successfully'}), 201
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# Assistance: Get assistance services
@app.route('/api/assistance', methods=['GET'])
def get_assistance():
    try:
        service_type = request.args.get('service_type')
        conn = get_db_connection()
        c = conn.cursor()
        if service_type:
            c.execute('SELECT * FROM assistance WHERE service_type = ?', (service_type,))
        else:
            c.execute('SELECT * FROM assistance')
        assistance = [dict(row) for row in c.fetchall()]
        conn.close()
        return jsonify(assistance), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# Assistance: Add a service
@app.route('/api/assistance', methods=['POST'])
def add_assistance():
    try:
        data = request.get_json()
        service_type = data.get('service_type')
        provider_name = data.get('provider_name')
        contact_info = data.get('contact_info')
        region = data.get('region')
        if not all([service_type, provider_name]):
            return jsonify({'error': 'Missing required fields'}), 400
        conn = get_db_connection()
        c = conn.cursor()
        c.execute('INSERT INTO assistance (service_type, provider_name, contact_info, region) VALUES (?, ?, ?, ?)',
                  (service_type, provider_name, contact_info, region))
        conn.commit()
        conn.close()
        return jsonify({'message': 'Assistance service added successfully'}), 201
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# Fundraising: Get campaigns
@app.route('/api/fundraising', methods=['GET'])
def get_fundraising():
    try:
        conn = get_db_connection()
        c = conn.cursor()
        c.execute('SELECT * FROM fundraising')
        campaigns = [dict(row) for row in c.fetchall()]
        conn.close()
        return jsonify(campaigns), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# Fundraising: Add a campaign
@app.route('/api/fundraising', methods=['POST'])
def add_fundraising():
    try:
        data = request.get_json()
        campaign_name = data.get('campaign_name')
        goal_amount = data.get('goal_amount')
        description = data.get('description')
        if not all([campaign_name, goal_amount]):
            return jsonify({'error': 'Missing required fields'}), 400
        conn = get_db_connection()
        c = conn.cursor()
        c.execute('INSERT INTO fundraising (campaign_name, goal_amount, description, created_at) VALUES (?, ?, ?, ?)',
                  (campaign_name, float(goal_amount), description, datetime.now()))
        conn.commit()
        conn.close()
        return jsonify({'message': 'Fundraising campaign added successfully'}), 201
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# Frontend Routes
@app.route('/cases', methods=['GET'])
def case_form():
    return render_template('report.html')

@app.route('/helplines', methods=['GET'])
def helplines_page():
    return render_template('helplines.html')

@app.route('/stories', methods=['GET'])
def stories_page():
    return render_template('survivor.html')

@app.route('/community', methods=['GET'])
def community_page():
    return render_template('community.html')

@app.route('/assistance', methods=['GET'])
def assistance_page():
    return render_template('assistance.html')

@app.route('/fundraising', methods=['GET'])
def donation_page():
    return render_template('Donation.html')

if __name__ == '__main__':
    app.run(debug=True)