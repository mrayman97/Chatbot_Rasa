# ############      ACTIONS     ############

## tell_joke
* tell_joke  
  - action_joke
    
## sales_form
* greet
  - utter_greet
* contact_sales
  - action_reset_all_slots
  - sales_form
  - form{"name": "sales_form"}
  - form{"name": null}
 
# ###########     WEATHER ##################

## story_001
* greet
  - utter_greet
* inquire
  - utter_ask_location
* inquire
  - slot{"location":"action_weather"}
  - action_weather

# ###########       utter       ############ 
 
## say_hello
* greet
  - utter_greet
  
## introduction
* introduction
  - utter_introduction 

## reply
* reply
  - utter_reply
  
## answer_question
* answer_question
  - utter_answer_question  
  
## out_of_strenghts
* out_of_strenghts
  - utter_out_of_strenghts

## tell_gender
* tell_gender
  - utter_tell_gender
  
## eat
* eat
  - utter_eat  
  
## other_bots
* other_bots
  - utter_other_bots
  
## no_opinion
* no_opinion
  - utter_no_opinion
  
## who_is_beautiful
* who_is_beautiful
  - utter_who_is_beautiful
  
## about_tech
* about_tech
  - utter_about_tech

## follow_heart
* follow_heart
  - utter_follow_heart
  
## chat_with_me
* chat_with_me
  - utter_chat_with_me

## different_answer
* different_answer
  - utter_different_answer
  
## angry
* angry
  - utter_angry
  
## sing
* sing
  - utter_sing  
  
## wish_happy_day
* wish_happy_day
  - utter_wish_happy_day

## do_you_know_me
* do_you_know_me
  - utter_do_you_know_me  

## user_hungry
* user_hungry
  - utter_user_hungry
  
## user_tired
* user_tired
  - utter_user_tired
  
## say_anything_else
* anything_else
  - utter_anything_else
  
## say_goodbye
* goodbye
  - utter_goodbye

## happy_path
* greet
  - utter_greet
* happy
  - utter_happy
* goodbye
  - utter_goodbye

## sad_path
* greet
  - utter_greet
* unhappy
  - utter_unhappy
* goodbye
  - utter_goodbye
  
## bot_challenge
* bot_challenge
  - utter_bot_challenge

## affirmation
* affirm
  - utter_affirm
  
## deny
* deny
  - utter_deny

## faq_leyton_details
* leyton_faq
  - utter_leyton_faq
  
## telling_age
* age
  - utter_age
  
## beautiful
* beautiful
  - utter_beautiful  
  
## smart_agent
* smart
  - utter_smart
   
## agent_busy
* agent_busy
  - utter_agent_busy
  
## agent_funny
* agent_funny
  - utter_agent_funny

