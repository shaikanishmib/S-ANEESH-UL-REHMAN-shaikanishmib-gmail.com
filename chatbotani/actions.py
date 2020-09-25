# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/core/actions/#custom-actions/


# This is a simple example for a custom action which utters "Hello World!"

# from typing import Any, Text, Dict, List
#
 from rasa_sdk import Action, Tracker
 from rasa_sdk.executor import CollectingDispatcher
 from rasa_sdk.events import SlotSet
 from db-connect import DataUpdate
 import random
 order_statuses = {1: "being prepared", 2: "being packed", 3: "out for delivery", 4: "delivered"}  
 class ActionConfirmOrder(Action):

     def name(self) -> Text:
         return "action_confirm_orderd"

     def run(self, dispatcher: CollectingDispatcher,
             tracker: Tracker,
             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
             name=tracker.get_slot("Name")
             pizza=tracker.getslot("pizza")
             size=tracker.get_slot("size")
             mobile=tracker.get_slot("mobile_no")
             message="{} have order an {} {} pizza.the following is order id{}".format(name,size,pizza,mobile)
             print(message)

         dispatcher.utter_message(text=message)
         DataUpdate(tracker.get_slot("Name"),tracker.get_slot("pizza"),tracker.get_slot("mobile_no"))

         return [SlotSet('Name',tracker.latest_message['text']),SlotSet('pizza',tracker.latest_message['text']),SlotSet('mobile_no',tracker.latest_message['text']),SlotSet('size',tracker.latest_message['text'])]
 
 class ActionHelloWorld(Action):

     def name(self) -> Text:
         return "action_odrer_status"

     def run(self, dispatcher: CollectingDispatcher,
             tracker: Tracker,
             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
             order_id=tracker.get_slot("order_id")
             if order_id.length==10:
                 order_num=random.randint(0,3)
             else:
                 print("wrong order id")
             if order_num == 0:

                 order_status = order_statuses.get(1)
             elif order_num == 1:
                 order_status = order_statuses.get(2)
            elif order_num == 2:
                 order_status = order_statuses.get(3)
            else:
                 order_status = order_statuses.get(4)
            

         dispatcher.utter_message(text=order_status)

         return []