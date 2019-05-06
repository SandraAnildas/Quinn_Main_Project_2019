from bot_server_channel import BotServerInputChannel
from rasa_core.agent import Agent
from rasa_core.interpreter import RasaNLUInterpreter
from rasa_core.utils import EndpointConfig
from bot_server_channel import BotServerInputChannel

	
	
nlu_interpreter = RasaNLUInterpreter('C:/Users/Hp/Desktop/Quinn/models/nlu/default/counselingnlu')
action_endpoint = EndpointConfig(url="http://localhost:5055/webhook")
agent = Agent.load('C:/Users/Hp/Desktop/Quinn/models/dialogue', interpreter = nlu_interpreter, action_endpoint = action_endpoint)
channel = BotServerInputChannel(agent, port=5004)
agent.handle_channels([channel], 5004, serve_forever=True)






