from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
import csv
from datetime import datetime
import sys

currentDate = datetime.today().strftime('%m/%d/%Y')
fileTracker = "C:/Users/R/PycharmProjects/anyabot/data/lookups/case_summary.csv"


def get_count(types):
    with open(fileTracker) as f:
        reader = csv.reader(f)
        for row in reader:
            if row[0] == currentDate:
                casesCount = row[1]
                deathsCount = row[2]
                recoveriesCount = row[3]
                break
    f.close()

    if types == "cases":
        count = casesCount
    elif types == "deaths":
        count = deathsCount
    elif types == "recovered":
        count = recoveriesCount

    return count


class ActionGetCoronaCases(Action):

    def name(self) -> Text:
        return "action_get_total_cases"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        countCases = tracker.get_slot("count_cases_names")
        countCases = countCases.replace(" ", "")
        returnCount = "ERROR"

        if countCases == "kaso":
            returnCount = get_count("cases")
            countCases = "🏥 kaso"
            returnCorrect = True
        elif countCases == "namatay":
            returnCount = get_count("deaths")
            countCases = "😵 namatay"
            returnCorrect = True
        elif countCases == "gumaling":
            returnCount = get_count("recovered")
            countCases = "💪 gumaling"
            returnCorrect = True
        else:
            returnCorrect = False

        if returnCorrect:
            dispatcher.utter_message(text="Ang bilang ng {} ay {}.".format(countCases, returnCount))
        else:
            dispatcher.utter_message(text="Pasensya. Hindi ko mahanap ang datos ng {}. Paki-ulit ang tanong gamit ang "
                                          "salitang 'kaso', 'namatay', 'gumaling'.".format(countCases))

        return []


class ActionGetCoronaUpdates(Action):

    def name(self) -> Text:
        return "action_get_latest_update"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        countCases = tracker.get_slot("covid_update_names")
        countCases = countCases.replace(" ", "")

        if countCases == "update":
            returnCountCase = get_count("cases")
            returnCountDeaths = get_count("deaths")
            returnCountRecovered = get_count("recovered")
            summary = 'Total na bilang ng kaso : {}\nTotal na bilang ng namatay : {}\nTotal na bilang ng gumaling: {}'.format(returnCountCase, returnCountDeaths, returnCountRecovered)
            returnCorrect = True
        else:
            returnCorrect = False

        if returnCorrect:
            dispatcher.utter_message(text="{}".format(summary))
        else:
            dispatcher.utter_message(text="Pasensya. Hindi ko maintindihan ang iyong nais. Pakiulit ang tanong.")

        return []

class ActionDefaultAskAffirmation(Action):
    """Asks for an affirmation of the intent if NLU threshold is not met."""

    def name(self):
        return "action_default_ask_affirmation"

    def __init__(self):
        self.intent_mappings = {}
        # read the mapping from a csv and store it in a dictionary
        with open('data/lookups/intent_mapping.csv', newline='', encoding='utf-8') as file:
            csv_reader = csv.reader(file)
            for row in csv_reader:
                self.intent_mappings[row[0]] = row[1]

    def run(self, dispatcher, tracker, domain):
        # get the most likely intent
        last_intent_name = tracker.latest_message['intent']['name']

        # get the prompt for the intent
        intent_prompt = self.intent_mappings[last_intent_name]

        # Create the affirmation message and add two buttons to it.
        # Use '/<intent_name>' as payload to directly trigger '<intent_name>'
        # when the button is clicked.
        message = "Sa tingin ko ay {}".format(intent_prompt)
        buttons = [{'title': 'Tama',
                    'payload': '/{}'.format(last_intent_name)},
                   {'title': 'Hindi',
                    'payload': '/out_of_scope'}]
        dispatcher.utter_message(message, buttons=buttons)

        return []
