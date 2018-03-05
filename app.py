#!/usr/bin/env python

import urllib
import json
import os
import csv
import pandas as pd
from var import UnQstn, ArrayOfQuestions
UQ = UnQstn("","","","")

from flask import Flask
from flask import request
from flask import make_response

# Flask app should start in global layout
app = Flask(__name__)


@app.route('/webhook', methods=['POST'])
def webhook():
    req = request.get_json(silent=True, force=True)

    print("Request:")
    print(json.dumps(req, indent=4))

    res = makeWebhookResult(req)

    res = json.dumps(res, indent=4)
    print(res)
    r = make_response(res)
    r.headers['Content-Type'] = 'application/json'
    return r

def makeWebhookResult(req):
    if req.get("result").get("action") == "input-subject-name":
        
        result = req.get("result")
        parameters = result.get("parameters")
        zone = parameters.get("subject_name")
    
        csv_file = csv.reader(open('books1.csv'), delimiter=",")
       
        for row in csv_file:    
            if zone == row[1]:
                speech = ("\n\nBook Id: " + row[0] + "\n Book Title: " + row[1] + "\n Authors: " + row[2] + "\n Publication: " + row[3] + "\n Rack Number:" + row[4])
        
        print(speech)
        
        
        print("Response:")
        print(speech)
        return {
                "speech": speech,
                "displayText": speech,
                #"data": {},
                #"contextOut": [],
                "source": "input-subject-name"
               }
    
    elif req.get("result").get("action") == "input-publication":
        
        result = req.get("result")
        parameters = result.get("parameters")
        zone = parameters.get("publication_names")
    
        csv_file = csv.reader(open('books1.csv'), delimiter=",")
       
        for row in csv_file:    
            if zone == row[3]:
                speech = ("\n\nBook Id: " + row[0] + "\n Book Title: " + row[1] + "\n Authors: " + row[2] + "\n Publication: " + row[3] + "\n Rack Number:" + row[4])
        
        print(speech)
        
        
        print("Response:")
        print(speech)
        return {
                "speech": speech,
                "displayText": speech,
                #"data": {},
                #"contextOut": [],
                "source": "input-publication"
               }
    
    elif req.get("result").get("action") == "issue-input":
        
        result = req.get("result")
        parameters = result.get("parameters")
        pub_name = parameters.get("publication_names")
        sub_name = parameters.get("subject_name")
        user_id = parameters.get("user_id")
        status = "yes"
        yes = "yes"
        no = "no"
    
        csv_file = csv.reader(open('issue.csv'), delimiter=",")
        
        for row in csv_file:
            if user_id == row[0] and no == row[12]:
        
         
                UQ.user = user_id
                UQ.question = sub_name
                UQ.answer = pub_name
                UQ.status = status
                print("\n You are eligible to issue books")
    
    
                with open('issue1.csv', 'a') as Ques_Ans:
                    writer = csv.writer(Ques_Ans)
                    writer.writerow([UQ.user,UQ.question, UQ.answer,UQ.status])    
                    print("\nThe Book has been issued to your name!")
   
        
        
        print("Response:")
        print(speech)
        return {
                "speech": speech,
                "displayText": speech,
                #"data": {},
                #"contextOut": [],
                "source": "issue-input"
               }
    
        
    
    else:
       return{}
if __name__ == '__main__':
    port = int(os.getenv('PORT', 5000))

    print ("Starting app on port %d" %(port))

    app.run(debug=True, port=port, host='0.0.0.0')
