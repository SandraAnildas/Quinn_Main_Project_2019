##story 1
*  greet
	- utter_ask_name
*  intro
	- utter_greet
## story 2
* goodbye
	- utter_goodbye
##story 3
* user_question
	- utter_console
##story 4
* user_input
	- utter_ask_problem
	
##story 5

* mood_unhappy
  - utter_cheer_up
  - utter_did_that_help
* mood_affirm
  - utter_happy


## Generated Story 0
*  greet
	- utter_ask_name
*  intro
	- utter_greet

## Generated Story -4474326349125042510
* user_input{"problem": "unhappy"}
    - slot{"problem": "unhappy"}
    - utter_ask_problem
* user_question
    - action_restart

## Generated Story 5649544396524466680
* user_input
    - utter_ask_problem
* user_question
    - utter_console

## Generated Story 311758365160320290
* user_question
    - utter_console
* goodbye
    - utter_goodbye

## Generated Story 7737292668415394341
* greet
    - utter_ask_name
* intro{"PERSON": "Sanu"}
    - slot{"PERSON": "Sanu"}
    - utter_greet
* gratitude
    - utter_ask_abt_day
* mood_happy
    - utter_ask_abt_day
* mood_happy
    - utter_happy
* goodbye
    - utter_goodbye
* mood_affirm

