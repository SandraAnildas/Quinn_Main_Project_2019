from rasa_nlu.training_data import load_data
from rasa_nlu import config
from rasa_nlu.model import Trainer
from rasa_nlu.model import Metadata, Interpreter
#from chatterbot import ChatBot
#from chatterbot.trainers import ChatterBotCorpusTrainer

def train_nlu(data, configs, model_dir):
	training_data = load_data(data)
	trainer = Trainer(config.load(configs))
	#chatbot = ChatBot('Export Example Bot')
	#trainer = ChatterBotCorpusTrainer(chatbot)
	#trainer.train("chatterbot.corpus.english.greetings","chatterbot.corpus.english.conversations")
	#trainer.export_for_training('./my_export.json')
	trainer.train(training_data)
	model_directory = trainer.persist(model_dir, fixed_model_name = 'counselingnlu')
	
def run_nlu(): 
	interpreter = Interpreter.load('./models/nlu/default/counselingnlu')
	print(interpreter.parse(u"I broke with my boyfriend this morning"))
	
if __name__ == '__main__':
	train_nlu('./data/data.md', 'config_spacy.json', './models/nlu')
	run_nlu()