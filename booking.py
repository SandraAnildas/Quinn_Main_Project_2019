from __future__ import absolute_import
from __future__ import division
from __future__ import unicode_literals

from rasa_core_sdk import Action
from rasa_core_sdk.events import SlotSet

import pymysql

class BookAppointment(Action):
	def name(self):
		return 'action_book_appointment'
		
	def run(self, dispatcher, tracker, domain):
		
		app_date = tracker.get_slot('date')
		
		#return token
		response = """Your appointment on {} is confirmed. """.format(app_date)						
		dispatcher.utter_message(response)
		return [SlotSet('date',date)]