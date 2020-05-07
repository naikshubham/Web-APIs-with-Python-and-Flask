from flask import Flask, request, render_template, escape
import json
import pandas as pd
from datetime import datetime

app = Flask(__name__)
# headers = {'content-type':"application/text"}

@app.route('/DH_logdata', methods = ['POST', 'GET'])
def get_ids():
    query_parameters = request.args
    id = query_parameters.get('id')
    date = datetime.today().strftime('%Y-%m-%d-%H:%M:%S')


# @app.route('/', methods = ['POST','GET'])
# def entry():
# 	return render_template('form.html', the_action = '/DH_logdata')

# @app.route('/DH_logdata', methods=['GET', 'POST'])
# def capture():
#     if request.form['submitt'] == 'Logdata': 
#         name=request.form['name']
#         contact=request.form['contact number']
#         print(name, "-- ", contact)
    with open('contacts.txt', 'a') as contact_log:
        print(id, date, request.remote_addr, request.user_agent, file=contact_log, sep='|')
    
    return 'OK'

@app.route('/DivineHarmony')
def view_log()->'html':
	contents=[]
	with open('./contacts.txt','r') as log:
	    for line in log:
	        contents.append([])
	        for item in line.split('|'):
	            contents[-1].append(escape(item))
	titles=('ID','Date', 'Remote_addr','User_agent')
	return render_template('viewlog.html',
	                        the_title='View log',
	                        the_row_titles=titles,
	                        the_data=contents,)


if __name__ == "__main__":
    # app.run(debug=True, port=8080)
    app.run('localhost', debug=True, port=8080)