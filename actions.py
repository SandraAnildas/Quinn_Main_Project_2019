from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

import logging
import requests
import urllib.request
import json
import smtplib
import pymysql
from rasa_core_sdk import Action
from rasa_core_sdk.executor import CollectingDispatcher
from rasa_core_sdk.forms import FormAction, REQUESTED_SLOT
from rasa_core_sdk.events import SlotSet, UserUtteranceReverted, \
                                 ConversationPaused

logger = logging.getLogger(__name__)

class ActionGreet(FormAction):

	def name(self):
		return "action_greet"

	def run(self, dispatcher, tracker, domain):
		
		person_name = next(tracker.get_latest_entity_values('PERSON'), None)
		dispatcher.utter_message("Nice to meet you!!! "+ person_name+ "! What's up?")
		return [SlotSet("PERSON", person_name)]

class ActionBye(Action):

	def name(self):
		return "action_bye"

	def run(self, dispatcher, tracker, domain):
		person_name = tracker.get_slot('PERSON')
		dispatcher.utter_message("See you soon "+ person_name)
		
		return []
		
class ActionMail(Action):

	def name(self):
		return 'sendmail'
		
	def run(self, dispatcher, tracker, domain):
		person_name = tracker.get_slot('PERSON')
		server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
		server.login("quinnmentalcounselor@gmail.com", "qwerty@123")
		server.sendmail("quinnmentalcounselor@gmail.com","sandraanildas1995@gmail.com","Your patient "+person_name+" is having suicidal thoughts")
		server.quit()
		
		return []
class BookAppointment(Action):
	def name(self):
		return 'booking'
		
	def run(self, dispatcher, tracker, domain):
		
		
		
		db = pymysql.connect('localhost', 'root','','quinn_doctor')
		#dispatcher.utter_message(db)	
		cursor = db.cursor()
		app_date = str(tracker.get_slot('date'))
		person_name = str(tracker.get_slot('PERSON'))
		
		
		sql = ("""INSERT INTO appointment(patient_name,date) VALUES(%s,%s)""",(person_name,app_date))
		#cursor.execute(*sql)
	
		try:
			if(cursor.execute(*sql)):
				db.commit()
				sql1=("""Select token from appointment where patient_name=%s and date=%s""",(person_name,app_date))
				if(cursor.execute(*sql1)):
					value = cursor.fetchone()
					token= str(value[0])
					response="""Your appointment on {} is confirmed. Your token is {}...""".format(app_date,token)
					dispatcher.utter_message(response)
					return [SlotSet('date',date)]
				else:
					response="""Sorry your appointment can't be made on {}. Kindly specify another date""".format(app_date)
					dispatcher.utter_template('utter_ask_date',tracker)
					dispatcher.utter_message(response)
					return [SlotSet('date',None)]				
			else:
				response="""Sorry your appointment can't be made on {}. Kindly specify another date""".format(app_date)
				dispatcher.utter_message(response)				
				dispatcher.utter_template('utter_ask_date',tracker)
				return [SlotSet('date',None)]
		except:
			dispatcher.utter_message("Error...")
			return [SlotSet('date',None)]
		finally:
			db.close()
			
		return []
		
		

