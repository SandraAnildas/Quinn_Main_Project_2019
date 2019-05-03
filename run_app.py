from rasa_core.channels.slack import SlackInput
from rasa_core.channels.socketio import SocketIOInput
from rasa_core.agent import Agent
from rasa_core.interpreter import RasaNLUInterpreter
import yaml
from ga_connector import GoogleConnector
from rasa_core.utils import EndpointConfig


nlu_interpreter = RasaNLUInterpreter('./models/nlu/default/counselingnlu')
action_endpoint = EndpointConfig(url="http://localhost:5055/webhook")
agent = Agent.load('./models/dialogue', interpreter = nlu_interpreter, action_endpoint = action_endpoint)

#input_channel1 = SlackInput('xoxb-582512269238-578793132704-6jm8XLEPtFnHaf8pvW3HieC6')
#input_channel= GoogleConnector()

input_channel = SocketIOInput(
            # event name for messages sent from the user
            user_message_evt="user_uttered",
            # event name for messages sent from the bot
            bot_message_evt="bot_uttered",
            # socket.io namespace to use for the messages
            namespace=None
    )


#agent.handle_channels([input_channel], 5005, serve_forever=True)
agent.handle_channels([input_channel], 5004, serve_forever=True)