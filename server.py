from flask import Flask , render_template, url_for, request,redirect
import csv

app = Flask(__name__)
app.debug = True


@app.route("/")
def yikber():
    return render_template('index.html')

@app.route('/<string:page_name>')
def html_page(page_name):
    return render_template(page_name)

def write_to_file(data):
    with open('dataBase.txt', mode='a') as dataBase:
        email = data["email"]
        subject = data["subject"]
        message = data["message"]
        file = dataBase.write(f'\n{email},{subject},{message}')

def write_to_csv(data):
    with open('database.csv', mode='a') as database2:
        email = data["email"]
        subject = data["subject"]
        message = data["message"]
        csv_writer = csv.writer(database2, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow([email,subject,message])

@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == 'POST':
        data = request.form.to_dict()
        write_to_csv(data)
        return redirect('/thankYou.html')
    else:
        return 'something went wrong. try again'






# if __name__ == '__main__':
#     app.run()
if __name__ == '__main__':
    app.run(debug=True, port=5001)  # Try a different port number, e.g., 5001
