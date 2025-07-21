from flask import Flask, request, jsonify, render_template,flash,redirect,url_for
from datetime import datetime
from db import get_db_connection


app = Flask(__name__)
app.secret_key = '2025'

# Cases: Submit a case
@app.route('/submit_case', methods=['POST','GET'])
def submit_case():
    if request.method=="POST":
        userName = request.form.get('username')
        contactNumber = request.form['contactNumber']
        address = request.form['address']
        email =request.form['email']
        country = request.form['country']
        city =request.form['city']
        caseType = request.form['caseType']
        message =request.form['message']
        if not all([userName, contactNumber, address, email, country, city, caseType, message]):
            flash('error','Fill in all the required fields')
            return render_template('report.html',
                                   username=userName,
                                   contactNumber=contactNumber,
                                   email=email,
                                   country=country,
                                   city=city,
                                   caseType=caseType,
                                   message=message)
        try:        
            conn = get_db_connection()
            c = conn.cursor()
            c.execute('INSERT INTO cases(userName, contactNumber, address, email, country, city, caseType, message)VALUES (%s,%s,%s,%s,%s,%s,%s,%s)',(userName, contactNumber, address, email, country, city, caseType, message))
            conn.commit()
            conn.close()
            return redirect(url_for('home'))
        except Exception as e:
            print(f"Database Error: {e}")
            flash('There was a problem submitting your case. Please try again.', 'error')
            # return redirect(request.url)
            return render_template('report.html',
                           username=userName, 
                           contactNumber=contactNumber, 
                           address=address, 
                           email=email, 
                           country=country, 
                           city=city, 
                           caseType=caseType, 
                           message=message)
        return render_template('report.html')

"""
@app.route('/home')
def home():
    return render_template('home.html') 
"""

# Survivor Stories: Submit a story
@app.route('/submit_story', methods=['POST','GET'])
def submit_story():
    if request.method=="POST":
        name=request.form['name']
        yourStory=request.form['yourStory']
        digitalSignature=request.form['digitalSignature']

        if not all([name, yourStory, digitalSignature]):
            flash('Missing required fields','error',)
            return render_template('survivor.html', 
                                   name=name, 
                                   yourStory=yourStory, 
                                   digitalSignature=digitalSignature)
        try:    
           conn = get_db_connection()
           c = conn.cursor()
           c.execute('INSERT INTO survivorstories (name, yourStory, digitalSignature) VALUES (%s, %s, %s)',
                  (name, yourStory, digitalSignature))
           conn.commit()
           conn.close()
           flash('Your story has been submitted successfully!', 'success')
           return redirect(url_for('home'))
        except Exception as e:
            flash(f'Database Error: {e}', 'error')
            #return redirect(request.url)
            return render_template('survivor.html', 
                                   name=name, 
                                   yourStory=yourStory, 
                                   digitalSignature=digitalSignature)
    return render_template('survivor.html')
    

# Donation : donate
@app.route('/donate', methods=['GET','POST'])
def donate():
    if request.method=="POST":
        donationAmount=request.form['donationAmount']
        fullName=request.form['fullName']
        emailAddress=request.form['emailAddress']
        paymentMethod=request.form['paymentMethod']
        message=request.form['message']

        if not all([donationAmount, fullName, emailAddress, paymentMethod, message]):
            flash('Missing required fields', 'error')
            return render_template('Donation.html', 
                                   donationAmount=donationAmount, 
                                   fullName=fullName,
                                   emailAddress=emailAddress, 
                                   paymentMethod=paymentMethod, 
                                   message=message)
            #return redirect(request.url)
        try:   
           conn = get_db_connection()
           c = conn.cursor()
           c.execute('INSERT INTO donation (donationAmount, fullName, emailAddress, paymentMethod, message) VALUES (%s, %s, %s, %s,%s)',(donationAmount, fullName, emailAddress, paymentMethod, message))
           conn.commit()
           conn.close()
           flash('Thank you for your donation!', 'success')
           return redirect(url_for('home'))   
        
        except Exception as e:
            flash(f'Database Error: {e}', 'error')
            return render_template('Donation.html', 
                                   donationAmount=donationAmount, 
                                   fullName=fullName,
                                   emailAddress=emailAddress, 
                                   paymentMethod=paymentMethod, 
                                   message=message)
            # return redirect(request.url)
        
    return render_template('donation.html')
      


# Frontend Routes

@app.route('/')
def homepage():
    return render_template('mainpage.html')

@app.route('/home')
def home():
    return render_template('home.html') 
"""
@app.route('/report', methods=['GET'])
def case_form():
    return render_template('report.html')

@app.route('/survivor', methods=['GET'])
def stories_page():
    return render_template('survivor.html')

@app.route('/donate', methods=['GET'])
def donation_page():
    return render_template('Donation.html')
"""
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

if __name__ == '__main__':
    app.run(debug=True)
