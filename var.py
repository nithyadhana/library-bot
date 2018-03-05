# -*- coding: utf-8 -*-
"""
Created on Mon Mar 05 14:54:32 2018

@author: Surya
"""

class UnQstn:
    def __init__(self, user, question, answer, status):
        self.user = user
        self.question = question
        self.answer = answer
        self.status = status
        

UnknownQuery_one = UnQstn("user","question","answer","status")
                          
ArrayOfQuestions = [UnknownQuery_one] 