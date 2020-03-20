# https://www.cricapi.com/how-to-use.aspx
# api key=UXw3bu1qj6NILINft6eYVGvTWS12
# https://cricapi.com/api/matches/?apikey=UXw3bu1qj6NILINft6eYVGvTWS12
# unique_id : 1194108     from crickbuzz
# api_key : UXw3bu1qj6NILINft6eYVGvTWS12
# score_api : https://cricapi.com/api/cricketScore/
# To get details:
# score_api : https://cricapi.com/api/cricketScore?unique_id=1194108&apikey=UXw3bu1qj6NILINft6eYVGvTWS12
#  

from tkinter import *
import time
import requests
import json

root=Tk()

root.geometry("900x500")

match_data=requests.get('https://cricapi.com/api/cricketScore?unique_id=1194108&apikey=UXw3bu1qj6NILINft6eYVGvTWS12')
# converting into json so that we can manipulate it
json_data=match_data.json()

def times():
    curr_score=json_data['stat']
    score.configure(text="current score : " +curr_score)
    score.after(200,times)



score=Label(root,font=("time",15,"bold"),bg="white")
score.grid(row=2,column=2,pady=2,padx=100)
times()

root.mainloop()