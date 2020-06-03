## STORY 0
## greetings
 * greet
  - utter_greet
 * show_tag
  - utter_learn_tag

## STORY 1
## define COVID
 * define_covid_tag
  - utter_define_covid_img_tag
  - utter_define_covid_tag
  - utter_continue_learn

## STORY 2
## prevent COVID
 * prevent_covid_tag
  - utter_prevent_covid_img_tag
  - utter_prevent_covid_tag
  - utter_continue_learn
    
## STORY 3
## symptoms of COVID
 * list_covid_symptoms_tag
  - utter_list_covid_symptoms_img_tag
  - utter_list_covid_symptoms_tag
  - utter_ask_has_covid_symptoms_tag

## STORY 3.1
## no symptom 
 * respond_has_symptoms_none_tag
  - utter_feel_covid_symptoms_none_tag
  - utter_continue_learn

## STORY 3.2  
## all symptoms
 * respond_has_symptoms_all_tag
  - utter_feel_covid_symptoms_all_tag
  - utter_continue_learn

## STORY 3.3
## some symptoms
 * respond_has_symptoms_some_tag
  - utter_feel_covid_symptoms_some_tag
  - utter_continue_learn
  
## STORY 4
## learn more about COVID
 * back_to_learn_tag
  - utter_learn_tag
 
## STORY 5
 * covid_update{"covid_update_names":"update"}
  - slot {"covid_update_names":"update"}
  - action_get_latest_update
 
## RANDOM CORONA QUESTIONS TAGALOG
## origin of covid in tagalog
 * covid_origin_tag
  - utter_covid_origin_tag
  - utter_continue_learn

## cure for covid in tagalog
 * cure_covid_tag
  - utter_cure_covid_tag
  - utter_continue_learn
      
## show covid pic
 * corona_image
  - utter_show_corona_image
  - utter_continue_learn

## counts of cases
 * show_covid_count_of_cases_tag{"count_cases_names":"kaso"}
  - slot {"count_cases_names":"kaso"}
  - utter_searching_for_count_cases_tag
  - action_get_total_cases

## counts of deaths
 * show_covid_count_of_cases_tag{"count_cases_names":"namatay"}
  - slot {"count_cases_names":"namatay"}
  - utter_searching_for_count_cases_tag
  - action_get_total_cases
 
## counts of recoveries
 * show_covid_count_of_cases_tag{"count_cases_names":"gumaling"}
  - slot {"count_cases_names":"gumaling"}
  - utter_searching_for_count_cases_tag
  - action_get_total_cases