from flask import Flask, render_template,url_for,request,redirect

import csv

app=Flask(__name__)




@app.route('/')
def hello_world(username=None):
	return render_template('index.html')

##@app.route('/')

##def index():
##	return '<h1>Hello!!!!</h1>'


@app.route('/<string:page_name>')

def html_page(page_name):
	return render_template(page_name)


# def write_to_file(data):
# 	with open('database.txt', mode='a') as database:
# 		email= data["email"]
# 		subject=data["subject"]
# 		message=data["message"]
# 		file = database.write(f'\n{email},{subject},{message}')




def write_to_csv(data):
	with open('database.csv', mode='a') as database2:
		email= data["email"]
		subject=data["subject"]
		message=data["message"]
		csv_writer = csv.writer(database2,delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
		csv_writer.writerow([email,subject,message])

@app.route('/_submit_form_', methods=['POST', 'GET'])## post- sending data to the server ad get method means viewing already stored data
def submit_form():
  
    if request.method=='POST':
    	data = request.form.to_dict()
    	write_to_csv(data)
    	return redirect('/thanku.html')

    else:
    	return 'something went wrong'
    	


