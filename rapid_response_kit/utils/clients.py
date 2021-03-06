from flask import current_app as app
from parse_rest.connection import register
from twilio.rest import TwilioRestClient


def twilio():
    return TwilioRestClient(app.config['TWILIO_ACCOUNT_SID'],
                            app.config['TWILIO_AUTH_TOKEN'])


def parse_connect(config=None):
    if config is None:
        config = app.config

    app_id = config.get('PARSE_APP_ID', None)
    rest_key = config.get('PARSE_REST_KEY', None)

    if not (app_id and rest_key):
        return False

    try:
        register(app_id, rest_key)
        return True
    except:
        return False