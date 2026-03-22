from flask import Flask, request, jsonify, render_template,flash,redirect,url_for
from datetime import datetime
from db import get_db_connection


app = Flask(__name__, template_folder='Zinduka/ZINDUKA/templates', static_folder='Zinduka/ZINDUKA/static')
app.secret_key = '2025'

def submit_case():
    """Handle case form submission"""
    userName = request.form.get('username')
    contactNumber = request.form['contactNumber']
    address = request.form['address']
    email = request.form['email']
    country = request.form['country']
    city = request.form['city']
    caseType = request.form['caseType']
    message = request.form['message']
    
    if not all([userName, contactNumber, address, email, country, city, caseType, message]):
        flash('Missing required fields', 'error')
        return redirect(url_for('case_form'))
    
    try:        
        conn = get_db_connection()
        c = conn.cursor()
        c.execute('INSERT INTO cases(userName, contactNumber, address, email, country, city, caseType, message) VALUES (%s,%s,%s,%s,%s,%s,%s,%s)', (userName, contactNumber, address, email, country, city, caseType, message))
        conn.commit()
        conn.close()
        flash('Case submitted successfully!', 'success')
        return redirect(url_for('homepage'))
    except Exception as e:
        print(f"Database Error: {e}")
        flash('There was a problem submitting your case.', 'error')
        return redirect(url_for('case_form'))

def submit_story():
    """Handle survivor story form submission"""
    name = request.form['name']
    yourStory = request.form['yourStory']
    digitalSignature = request.form['digitalSignature']

    if not all([name, yourStory, digitalSignature]):
        flash('Missing required fields', 'error')
        return redirect(url_for('stories_page'))
    
    try:    
        conn = get_db_connection()
        c = conn.cursor()
        c.execute('INSERT INTO survivorstories (name, yourStory, digitalSignature) VALUES (%s, %s, %s)', (name, yourStory, digitalSignature))
        conn.commit()
        conn.close()
        flash('Story submitted successfully!', 'success')
        return redirect(url_for('homepage'))
    except Exception as e:
        flash(f'Database Error: {e}', 'error')
        return redirect(url_for('stories_page'))
    

def donate():
    """Handle donation form submission"""
    donationAmount = request.form['donationAmount']
    fullName = request.form['fullName']
    emailAddress = request.form['emailAddress']
    paymentMethod = request.form['paymentMethod']
    message = request.form['message']

    if not all([donationAmount, fullName, emailAddress, paymentMethod, message]):
        flash('Missing required fields', 'error')
        return redirect(url_for('donation_page'))
    
    try:   
        conn = get_db_connection()
        c = conn.cursor()
        c.execute('INSERT INTO donation (donationAmount, fullName, emailAddress, paymentMethod, message) VALUES (%s, %s, %s, %s, %s)', (donationAmount, fullName, emailAddress, paymentMethod, message))
        conn.commit()
        conn.close()
        flash('Thank you for your donation!', 'success')
        return redirect(url_for('homepage'))   
    except Exception as e:
        flash(f'Database Error: {e}', 'error')
        return redirect(url_for('donation_page'))
      


# Form submission routes
@app.route('/submit-case', methods=['POST'])
def submit_case_route():
    return submit_case()

@app.route('/submit-story', methods=['POST'])
def submit_story_route():
    return submit_story()

@app.route('/submit-donation', methods=['POST'])
def submit_donation_route():
    return donate()

# Frontend Routes

@app.route('/')
def homepage():
    return render_template('mainpage.html')

@app.route('/report', methods=['GET', 'POST'])
def case_form():
    if request.method == 'POST':
        return submit_case()
    return render_template('report.html')

@app.route('/survivor', methods=['GET', 'POST'])
def stories_page():
    if request.method == 'POST':
        return submit_story()
    return render_template('survivor.html')

@app.route('/donate', methods=['GET', 'POST'])
def donation_page():
    if request.method == 'POST':
        return donate()
    return render_template('Donation2.html')

@app.route('/program')
def program():
    return render_template('program.html')

@app.route('/anonymous')
def anonymous():
    return render_template('anonymous.html')

@app.route('/maria')
def maria():
    return render_template('MariaK.html')

@app.route('/jamila')
def jamila():
    return render_template('jamila.html')

@app.route('/hub')
def communityHub():
    return render_template('hub.html')

if __name__ == '__main__':
    app.run(debug=True)