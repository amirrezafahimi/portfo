from flask import Flask, render_template, \
    request, redirect
import csv
import smtplib
import statics
from flask_mail import Mail, Message

app = Flask(__name__)
app.config.update(
    MAIL_SERVER='smtp.gmail.com',
    MAIL_PORT=465,
    MAIN_USE_SSL=True,
    MAIN_USERNAME=statics.username,
    MAIN_PASSWORD=statics.password
)
mail = Mail(app)
print(__name__)


@app.route('/')
def my_home():
    return render_template('index.html')


@app.route('/<string:page_name>')
def html_page(page_name):
    return render_template(page_name)


# def write_to_file(data):
#     with open('database.txt', mode='a') as database:
#         email = data['email']
#         subject = data['subject']
#         message = data['message']
#         file = database.write(f'\n{email},{subject},{message}')


def write_to_csv(data):
    with open('database.csv', mode='a') as database:
        email = data['email']
        subject = data['subject']
        message = data['message']
        csv_writer = csv.writer(database, newline='', delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow([email, subject, message])


@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == 'POST':
        data = request.form.to_dict()
        send_email(data)
        # write_to_file(data)
        # write_to_csv(data)
        return redirect('/thankyou.html')
    else:
        return 'something went wrong'


def send_email(data):
    msg = mail.send(
        message=data['email'] + '\n' + data['subject'] + '\n' + data['message']
    )
    return msg
