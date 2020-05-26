## happy path 1 (C:\Users\R\AppData\Local\Temp\tmpep2vxh9j\fb39f93f8aa24b7890567c6b49798095_conversation_tests.md)
* greet: hello there!
    - utter_greet
* mood_great: amazing
    - utter_happy   <!-- predicted: utter_greet_ilokano -->


## happy path 2 (C:\Users\R\AppData\Local\Temp\tmpep2vxh9j\fb39f93f8aa24b7890567c6b49798095_conversation_tests.md)
* greet: hello there!
    - utter_greet
* mood_great: amazing
    - utter_happy   <!-- predicted: utter_greet_ilokano -->
* goodbye: bye-bye!
    - utter_goodbye


## sad path 1 (C:\Users\R\AppData\Local\Temp\tmpep2vxh9j\fb39f93f8aa24b7890567c6b49798095_conversation_tests.md)
* greet: hello
    - utter_greet
* mood_unhappy: not good   <!-- predicted: deny: not good -->
    - utter_cheer_up   <!-- predicted: utter_greet_ilokano -->
    - utter_did_that_help   <!-- predicted: action_listen -->
* affirm: yes
    - utter_happy   <!-- predicted: utter_greet_tagalog -->


## sad path 2 (C:\Users\R\AppData\Local\Temp\tmpep2vxh9j\fb39f93f8aa24b7890567c6b49798095_conversation_tests.md)
* greet: hello
    - utter_greet
* mood_unhappy: not good   <!-- predicted: deny: not good -->
    - utter_cheer_up   <!-- predicted: utter_greet_ilokano -->
    - utter_did_that_help   <!-- predicted: action_listen -->
* deny: not really
    - utter_goodbye   <!-- predicted: utter_greet_tagalog -->


## sad path 3 (C:\Users\R\AppData\Local\Temp\tmpep2vxh9j\fb39f93f8aa24b7890567c6b49798095_conversation_tests.md)
* greet: hi
    - utter_greet
* mood_unhappy: very terrible
    - utter_cheer_up   <!-- predicted: utter_greet_ilokano -->
    - utter_did_that_help   <!-- predicted: action_listen -->
* deny: no
    - utter_goodbye   <!-- predicted: utter_greet_tagalog -->


## bot challenge (C:\Users\R\AppData\Local\Temp\tmpep2vxh9j\fb39f93f8aa24b7890567c6b49798095_conversation_tests.md)
* bot_challenge: are you a bot?
    - utter_iamabot   <!-- predicted: utter_goodbye -->


