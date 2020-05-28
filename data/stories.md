## STORY 1
## Language: Tagalog
## Description: Define COVID
 * greet
  - utter_greet
 * show_tag
  - utter_learn_tag
 * define_covid_tag
  - utter_define_covid_tag

## STORY 2
## Language: Tagalog
## Description: Prevent COVID
 * greet
  - utter_greet
 * show_tag
  - utter_learn_tag
 * prevent_covid_tag
  - utter_prevent_covid_tag
  
## STORY 3
## Language: Tagalog
## Description: Symptoms of COVID
## Answer: No symptom
 * greet
  - utter_greet
 * show_tag
  - utter_learn_tag
 * list_covid_symptoms_tag
  - utter_list_covid_symptoms_tag
  - utter_ask_has_covid_symptoms_tag
 * respond_has_symptoms_none_tag
  - utter_feel_covid_symptoms_none_tag
  
## STORY 4
## Language: Tagalog
## Description: Symptoms of COVID
## Answer: All symptoms
 * greet
  - utter_greet
 * show_tag
  - utter_learn_tag
 * list_covid_symptoms_tag
  - utter_list_covid_symptoms_tag
  - utter_ask_has_covid_symptoms_tag
 * respond_has_symptoms_all_tag
  - utter_feel_covid_symptoms_all_tag

## STORY 5
## Language: Tagalog
## Description: Symptoms of COVID
## Answer: Some symptoms
 * greet
  - utter_greet
 * show_tag
  - utter_learn_tag
 * list_covid_symptoms_tag
  - utter_list_covid_symptoms_tag
  - utter_ask_has_covid_symptoms_tag
 * respond_has_symptoms_some_tag
  - utter_feel_covid_symptoms_some_tag
  
  
  
## RANDOM CORONA QUESTIONS

## origin of covid in tagalog
 * covid_origin_tag
  - utter_covid_origin_tag
  
## list covid symptoms in tagalog
 * list_covid_symptoms_tag
  - utter_list_covid_symptoms_tag
  
## cure for covid in tagalog
 * cure_covid_tag
  - utter_cure_covid_tag
  
## prevent covid in tagalog
 * prevent_covid_tag
  - utter_prevent_covid_tag
      
## show covid pic
 * corona_image
  - utter_show_corona_image

## has some symptoms
 * respond_has_symptoms_some_tag
  - utter_feel_covid_symptoms_some_tag


## CHITCHATS  
   
## goodbye
 * goodbye
  - utter_goodbye
   
## thanks
 * thank
  - utter_your_welcome
   
## nice
 * affirm
  - utter_affirm
    
## handle curses
 * curse
  - utter_sorry_for_curse
  
## laugh
 * laugh
  - utter_laugh
  
## default fallback
 * bot
  - action_default_fallback