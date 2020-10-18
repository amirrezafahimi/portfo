from flask import Flask, render_template, \
    request, redirect
import spreadsheet

app = Flask(__name__)


@app.route('/')
def my_home():
    return render_template('index.html')


@app.route('/<string:page_name>')
def html_page(page_name):
    return render_template(page_name)


@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == 'POST':
        data = request.form.to_dict()
        csv_writer = spreadsheet.WriteToSpreadSheet(data)
        csv_writer.write_data()
        return redirect('/thankyou.html')
    else:
        return 'something went wrong'
