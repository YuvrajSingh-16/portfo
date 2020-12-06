from flask import Flask, render_template, request, redirect
import csv

app = Flask(__name__)

@app.route('/')
def home_page():
    return render_template('index.html')

@app.route('/<string:page_name>')
def html_page(page_name):
    return render_template(page_name)

def write_to_file(data):
    with open('database.txt', 'a') as database:        
        name = data['name']
        email = data['email']
        message = data['message']
        file = database.write(f'\n{name}, {email}, {message}')


def write_to_csv(data):
    with open('database.csv', 'a', newline="") as database:        
        name = data['name']
        email = data['email']
        message = data['message']
        csv_writer = csv.writer(database, delimiter=",", quotechar='"', quoting=csv.QUOTE_MINIMAL)
        csv_file = csv_writer.writerow([name, email, message])

@app.route('/submit_form', methods=['GET', 'POST'])
def submit_form():
    if request.method == "POST":
        try:
            data = request.form.to_dict() 
            write_to_csv(data)
            return redirect('./thankyou.html')
        except:
            return "Did not save to the database !"
    else:
        return "Something went wrong !"