## corona tracker happy path
* greet
  - utter_greet
* show_the_list
  - utter_show_the_list
* corona_state
  - action_corona_tracker
  - utter_did_that_help
* affirm
  - utter_happy
* feedback
  - utter_feedback

## corona tracker happy path 2
* greet
  - utter_greet
* corona_state
  - action_corona_tracker
  - utter_did_that_help
* affirm
  - utter_happy
* feedback
  - utter_feedback

## corona tracker happy path 3
* greet
  - utter_greet
* corona_state
  - action_corona_tracker
  - utter_did_that_help
* show_the_list
  - utter_show_the_list
* affirm
  - utter_happy
  - utter_feedback

## corona tracker sad path
* greet
  - utter_greet
* show_the_list
  - utter_show_the_list
* corona_state
  - action_corona_tracker
  - utter_did_that_help
* deny
  - utter_sorry
  - utter_feedback

## happy path
* greet
  - utter_greet
* mood_great
  - utter_happy

## sad path 1
* greet
  - utter_greet
* mood_unhappy
  - utter_cheer_up
  - utter_did_that_help
* affirm
  - utter_happy

## sad path 2
* greet
  - utter_greet
* mood_unhappy
  - utter_cheer_up
  - utter_did_that_help
* deny
  - utter_goodbye

## say goodbye
* goodbye
  - utter_goodbye

## bot challenge
* bot_challenge
  - utter_iamabot

