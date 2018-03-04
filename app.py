# -*- coding: utf-8 -*-
"""
Created on Fri Mar 02 10:26:53 2018

@author: nithya
"""

#!/usr/bin/env python

import urllib
import json
import os
import csv

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
            if req.get("result").get("action") == "input-subject-name": && zone == row[0]:
                speech = ("Book Id: " + row[0] + "\n Book Title: " + row[1] + "\n Authors: " + row[2] + "\n Publication: " + row[3] + "\n Rack Number: "+ row[4])

        
        
        print("Response:")
        print(speech)
        return {
                "speech": speech,
                "displayText": speech,
                #"data": {},
                #"contextOut": [],
                "source": "input-subject-name"
               }
    
    elif req.get("result").get("action") == "Complaint_status.Complaint_status-custom":
        result = req.get("result")
        parameters = result.get("parameters")
        zone = parameters.get("Users")
        
        name = {'C0001':'John', 'C0002':'Patterson', 'C0003':'Tim', 'C0004':'Merl', 'C0005':'Robert', 'C0006':'Andrea', 'C0007':'Lucy', 'C0008':'Nicole', 'C0009':'Breanna', 'C0010':'Daniel', 'C0011':'Mason', 'C0012':'Sasha', 'C0013':'Baylee', 'C0014':'Gabrial'}
        cid = {'C0001' :'CW91810', 'C0002' :'CW91811', 'C0003' :'CW91812', 'C0004' :'CW91813', 'C0005' :'CW91814', 'C0006' :'CW91815', 'C0007' :'CW91816', 'C0008' :'CW91817', 'C0009' :'CW91818', 'C0010' :'CW91819', 'C0011' :'CW91820', 'C0012' :'CW91821', 'C0013' :'CW91822', 'C0014' :'CW91823' }
        ctype = {'CW91810' :'Technical', 'CW91811' :'Billing', 'CW91812' :'Plan', 'CW91813' :'Technical', 'CW91814' :'Account', 'CW91815' :'Billing', 'CW91816' :'Technical', 'CW91817' :'Technical', 'CW91818' :'Account', 'CW91819' :'Plan', 'CW91820' :'Plan', 'CW91821' :'Plan', 'CW91822' :'Technical', 'CW91823' :'Plan'  }
        ccomm = {'CW91810' :'No signal', 'CW91811' :'Suspend Billing till May 2018', 'CW91812' :'Change plan to Cricket Infinity', 'CW91813' :'Slow Data Speeds', 'CW91814' :'Account Terminated', 'CW91815' :'Resume Cricket Music Service', 'CW91816' :'Data Services not working', 'CW91817' :'Data Services not working', 'CW91818' :'Unable to access account', 'CW91819' :'Enroll for Cricket Student plan', 'CW91820' :'Enroll for Cricket Family plan', 'CW91821' :'Change plan to Cricket Plus plan', 'CW91822' :'No signal', 'CW91823' :'Change to Cricket Basic plan'  }
        cstat = {'CW91810' :'Resolved', 'CW91811' :'In process', 'CW91812' :'Open', 'CW91813' :'Open', 'CW91814' :'In process', 'CW91815' :'open', 'CW91816' :'Resolved', 'CW91817' :'Resolved', 'CW91818' :'Resolved', 'CW91819' :'Open', 'CW91820' :'In Process', 'CW91821' :'Resolved', 'CW91822' :'Resolved', 'CW91823' :'Resolved'}
        complaint_id = str(cid[zone])
        complaint_type = str(ctype[complaint_id])
        complaint_comment = str(ccomm[complaint_id])
        complaint_status = str(cstat[complaint_id])
        speech = "Hi " + str(name[zone]) +" (" + zone + " ) Complaint id: " + complaint_id + "\n Type of complaint: " + complaint_type + " \n your complaint: " + complaint_comment + " \n Currrent Status: " + complaint_status
        print("Response:")
        print(speech)
        return{
                "speech": speech,
                "displayText": speech,
                #"data": {},
                #"contextOut": [],
                "source": "Complaint_status.Complaint_status-custom"
              }
      
    
    
        
    
    else:
       return{}
if __name__ == '__main__':
    port = int(os.getenv('PORT', 5000))

    print ("Starting app on port %d" %(port))

    app.run(debug=True, port=port, host='0.0.0.0')
