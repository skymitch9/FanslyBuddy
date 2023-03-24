import rasa
import rasa.utils.io as io_utils
from rasa.nlu.model import Interpreter

interpreter = Interpreter.load(io_utils.resolve_model_path("models/nlu"))

def process_message(message):
    # Process user input with NLP model and generate response
    result = interpreter.parse(message)
    response = result['intent']['name']
    return response
