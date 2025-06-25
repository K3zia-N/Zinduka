from flask import Flask,redirect,render_template,request
import pymysql


app=Flask(__name__)


connection=pymysql.connect(
    host='localhost',
    user='root',
    password='',
    database='Zinduka'
)

cur = connection.cursor()

@app.route('/')
def index():
    return render_template('zinduka3.html')


@app.route('/donate', methods=['GET', 'POST'])
def donate():
    return render_template('Donation.html')


@app.route('/survivor', methods=['GET', 'POST'])
def survivor():
    return render_template('survivor.html')


@app.route('/report', methods=['GET', 'POST'])
def report():
    return render_template('report.html')


@app.route('/volunteer', methods=['GET', 'POST'])
def volunteer():
    return render_template('volunteer.html')



if __name__=="__main__":
    app.run(debug=True)