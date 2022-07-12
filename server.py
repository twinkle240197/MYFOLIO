from cProfile import run
import email
from email import message
from flask import Flask,render_template, url_for , request ,send_file


app = Flask(__name__)
print(__name__)

@app.route("/")
def my_home():
    return render_template('index.html')

@app.route("/index.html")
def index():
    return render_template('index.html')

@app.route("/about.html")
def about():
    return render_template('about.html')

@app.route("/works.html")
def works():
    return render_template('works.html')

@app.route("/work.html")
def work():
    return render_template('work.html')
@app.route("/work1.html")
def work1():
    return render_template('work1.html')
@app.route("/work2.html")
def work2():
    return render_template('work2.html')

@app.route("/static/power_electronics_project.pdf")
def show_static_pdf():
    with open('/static/power_electronics_project.pdf','rb')as static_file:
      return send_file(static_file,attachment_filename='power_electronics_project.pdf')

@app.route("/contact.html")
def contact():
    return render_template('contact.html')

def write_to_file(data):
    with open('database.txt',mode='a')as database:
     email=data["email"]
     subject=data["subject"]
     message= data["message"]
     file = database.write(f'\n{email},{subject},{message}')



@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
     if request.method =='POST':
        data = request.form.to_dict()
        write_to_file(data)
        return 'form submitted'
     else:
        return 'Something went wrong ,Try again my friend'

