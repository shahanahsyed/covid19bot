# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/core/actions/#custom-actions/


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List
#
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
import requests
#
# class ActionHelloWorld(Action):
#
#     def name(self) -> Text:
#         return "action_hello_world"
#
#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
#
#         dispatcher.utter_message(text="Hello World!")
#
#         return []
class ActionCoronaTracker(Action):
    def name(self) -> Text:
        return "action_corona_tracker"
    def run(self, dispatcher: CollectingDispatcher,
    tracker: Tracker,
    domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        s= tracker.get_slot("state")
        a=" done"
        response=  requests.get("https://api.covid19india.org/data.json").json()
      
        entities= tracker.latest_message['entities']
    
        states_list_in_api=[]
        for i in range(0,len(response["statewise"])):
            states_list_in_api.append(response["statewise"][i]["state"])
        # user_input_state= tracker.latest_message.text
        user_input_state= (tracker.latest_message)['text']
        message="dummy"
        #print(user_input_state.lower())
        if user_input_state.lower() =='india':
            message= "State: " + response["statewise"][0]["state"] + "\nConfirmed: "+ response["statewise"][0]["confirmed"]+"\nActive: " + response["statewise"][0]["active"]+"\nRecovered: " + response["statewise"][0]["recovered"]+"\nDeath: "+ response["statewise"][0]["deaths"]+"\nLast updated: "+ response["statewise"][0]["lastupdatedtime"]+"\nSource: https://api.covid19india.org/"
        else:
            for j in range(0,len(states_list_in_api)):
            # print(states_list_in_api[j].lower)
                if(user_input_state.lower()==states_list_in_api[j].lower()):
                    message= "State: " + response["statewise"][j]["state"]+"\nConfirmed: "+ response["statewise"][j]["confirmed"]+"\nActive: " + response["statewise"][j]["active"]+ "\nRecovered: " + response["statewise"][j]["recovered"]+ "\nDeath: "+ response["statewise"][j]["deaths"]+ "\nLast updated: "+ response["statewise"][j]["lastupdatedtime"]+ "\nSource: https://api.covid19india.org/"
       # state= None
        #print("line 3")
       # for e in entities:
       #     print("line 4")
       #     if e['entity']=="state":
       #         print("line 5\n")
       #         state= e['value']
       #         print(state)
       # message="Please enter the state name correctly."

        #if state == "india":
            #state= "Total"
        #for data in response["statewise"]:
            #if data["state"] == state.state():
                #message= "Active: " + data["active"] + "Confirmed: " + data["confirmed"] + "Recovered: " + data["recovered"] + "Last updated: " + data["lastupdatedtime"]
        dispatcher.utter_message(message)
        return []