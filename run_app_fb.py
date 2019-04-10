from rasa_core.channels.facebook import FacebookInput
from rasa_core.agent import Agent
from rasa_core.interpreter import RegexInterpreter
from rasa_core.interpreter import RasaNLUInterpreter
from rasa_core.utils import EndpointConfig

nlu_interpreter = RasaNLUInterpreter('./models/nlu/default/counselingnlu')
action_endpoint = EndpointConfig(url="http://localhost:5055/webhook")
agent = Agent.load('./models/dialogue', interpreter = nlu_interpreter, action_endpoint = action_endpoint)

input_channel = FacebookInput(
	fb_verify="quinn",
	# you need tell facebook this token, to confirm your URL
	fb_secret="●●●●●●●●",  # your app secret
	fb_access_token="EAARrOyV0FaMBAIDpuUwCm6lUfdaDLMkxrkrC2ZBPZAjckLGF7ZCJEwe0IZCrpt3G6wuVFra5t8iBLSNcsTJrHRvZAzFTasBH9UOKpGZBgfU7ZBHYjaXXPFIF9eKZBRuDZA1u2mxneruSsTZAAQvwdI1k5ZBYpZA9ZBHJmu879b9C4KKFBIgZDZD"
	# token for the page you subscribed to
   )
# set serve_forever=True if you want to keep the server running


s = agent.handle_channels([input_channel], 5004, serve_forever=True)