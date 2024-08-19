from utils.event_fetcher import fetch_upcoming_events

class EventIntentHandler:
    def handle(self, event, context):
        """Handle the EventIntent."""
        # Fetch upcoming events
        events = fetch_upcoming_events()
        
        if not events:
            speech_text = "Sorry, I couldn't find any upcoming events."
        else:
            speech_text = f"Here are some upcoming events: {', '.join(events)}. Would you like to book one?"
        
        return {
            'version': '1.0',
            'response': {
                'outputSpeech': {
                    'type': 'PlainText',
                    'text': speech_text
                },
                'shouldEndSession': False
            }
        }
