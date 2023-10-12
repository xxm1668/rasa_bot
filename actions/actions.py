# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import UserUtteranceReverted


class ActionHelloWorld(Action):

    def name(self) -> Text:
        return "action_hello_world"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(text="Hello World!")

        return [UserUtteranceReverted()]


class ActionDefaultFallback(Action):
    """Executes the fallback action and goes back to the previous state
    of the dialogue"""

    def name(self):
        return 'action_default_fallback'

    def run(self, dispatcher, tracker, domain):
        print('-------')
        # 访问图灵机器人API(闲聊)
        text = tracker.latest_message.get('text')
        print(text)
        message = '你好'
        if message is not None:
            dispatcher.utter_message(message)
        else:
            dispatcher.utter_template('utter_default', tracker, silent_fail=True)
        return [UserUtteranceReverted()]
