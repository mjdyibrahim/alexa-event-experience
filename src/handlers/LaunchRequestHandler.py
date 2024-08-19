class LaunchRequestHandler:
    def handle(self, event, context):
        """Handle the LaunchRequest."""
        return {
            'version': '1.0',
            'response': {
                'outputSpeech': {
                    'type': 'PlainText',
                    'text': 'Welcome to the Event Finder Skill! You can ask me about upcoming events.'
                },
                'shouldEndSession': False
            }
        }
