import requests

from rasa_sdk import Action, Tracker
from rasa_sdk.events import SlotSet, AllSlotsReset
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.forms import FormAction

from typing import Text, Any, Dict, List


class ActionJoke(Action):
    def name(self):
        return "action_joke"

    def run(self, dispatcher, tracker, domain):
        """make an api call"""
        request = requests.get('http://api.icndb.com/jokes/random').json()

        """extract a joke from returned json response"""
        joke = request['value']['joke']

        """send the message back to the user"""
        dispatcher.utter_message(text=joke)
        return []


class SalesForm(FormAction):
    """Collects sales information and adds it to the spreadsheet"""

    def name(self) -> Text:
        return "sales_form"

    @staticmethod
    def required_slots(tracker) -> List[Text]:
        return [
            "use_case",
            "company",
            "budget",
            "person_name",
            "job_function",
            "business_email",
        ]

    def submit(
            self,
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any],
    ) -> List[Dict]:
        dispatcher.utter_message("Thanks for getting in touch, we’ll contact you soon")
        return []


class ActionResetAllSlots(Action):
    """Reset Slots of Form"""

    def name(self):
        return "action_reset_all_slots"

    def run(self, dispatcher, tracker, domain):
        return [AllSlotsReset()]


class ActionWeather(Action):
    def name(self):
        return "action_weather"

    def run(self, dispatcher, tracker, domain):
        loc = tracker.get_slot('location')
        params = {
          'access_key': '1309316a5a1b18e34d63d7d9a0a41ba0',
          'query': loc
        }
        api_result = requests.get('http://api.weatherstack.com/current', 
                                    params)
        api_response = api_result.json()
        response = 'Current temperature in %s is %d℃' % (api_response['location']['name'], api_response['current']['temperature'])
        dispatcher.utter_message(response)
        return [SlotSet('location', loc)]