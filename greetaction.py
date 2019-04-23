from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

import logging
import requests
import urllib.request
import json
from rasa_core_sdk import Action
from rasa_core_sdk.executor import CollectingDispatcher
from rasa_core_sdk.forms import FormAction, REQUESTED_SLOT
from rasa_core_sdk.events import SlotSet, UserUtteranceReverted, \
                                 ConversationPaused

logger = logging.getLogger(__name__)

class ActionGreet(Action):

	def name(self):
		return "action_greet"

	def run(self, dispatcher, tracker, domain):
		
		person_name = next(tracker.get_latest_entity_values('PERSON'), None)
		dispatcher.utter_message("Nice to meet you "+ person_name+ " How can I help you ?")
		
		return [SlotSet("PERSON", person_name)]

class ActionBye(Action):

	def name(self):
		return "action_bye"

	def run(self, dispatcher, tracker, domain):
		person_name = tracker.get_slot('PERSON')
		dispatcher.utter_message("See you soon "+ person_name)
		
		return []

