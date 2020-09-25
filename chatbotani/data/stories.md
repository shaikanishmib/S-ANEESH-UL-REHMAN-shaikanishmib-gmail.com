 ## happy path
* greet
  - utter_greet

## say goodbye
* goodbye
  - utter_goodbye

## ask for a pizza
* greet
  - utter_greet
* pizza
  - utter_pizza_list
  - utter_ask_for_pizza
* pizza_type
  - utter_pizza_size
  - utter_ask_for_size
* pizza_size
  - utter_Name
* Name
  - slot{"Name":"Anish"}
  - utter_selected_pizza
* Selected_Pizza
  - slot{"pizza":"Margharita"}
  - utter_mobile_no
*mobile_no
  - slot{"mobile_no":"7893976672"}
  - action_confirm_order
  - utter_issue_order_id
* thanks
  - utter_thanks
  - utter_goodbye
## ask for a type of pizza
* greet
  - utter_greet
* pizza_and_type
  - utter_pizza_size
  - utter_ask_for_size
* pizza_size
   - utter_Name
* Name
  - slot{"Name":"Anish"}
  - utter_selected_pizza
* Selected_Pizza
  - slot{"pizza":"Margharita"}
  - utter_mobile_no
*mobile_no
  - slot{"mobile_no":"7893976672"}
  - action_confirm_order
  - utter_issue_order_id
* thanks
  - utter_thanks
  - utter_goodbye
## ask for a particular size of pizza
* greet
  - utter_greet
* pizza_size
- utter_pizza_list
  - utter_ask_for_pizza
* pizza_type
  - utter_Name
* Name
  - slot{"Name":"Anish"}
  - utter_selected_pizza
* Selected_Pizza
  - slot{"pizza":"Margharita"}
  - utter_mobile_no
*mobile_no
  - slot{"mobile_no":"7893976672"}
  - action_confirm_order
  - utter_issue_order_id
* thanks
  - utter_thanks
  - utter_goodbye
## track order id
* greet 
  - utter_greet
* track_order
  - slot{"order_id":"7858585858"}
  - utter_ask_for_order_id
  - action_order_status
* thanks
  - utter_thanks
  - utter_goodbye
