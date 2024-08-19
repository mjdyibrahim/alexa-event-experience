import logging
from handlers.LaunchRequestHandler import LaunchRequestHandler
from handlers.EventIntentHandler import EventIntentHandler

logger = logging.getLogger()
logger.setLevel(logging.INFO)

def lambda_handler(event, context):
    """Lambda function entry point."""
    # Initialize the request handler
    handler = EventIntentHandler()
    
    # Determine which handler to use based on the incoming request
    if event['request']['type'] == 'LaunchRequest':
        return LaunchRequestHandler().handle(event, context)
    elif event['request']['type'] == 'IntentRequest':
        return EventIntentHandler().handle(event, context)
    else:
        return {
            'version': '1.0',
            'response': {
                'outputSpeech': {
                    'type': 'PlainText',
                    'text': 'Sorry, I can only handle LaunchRequest and IntentRequest.'
                },
                'shouldEndSession': True
            }
        }

