import os
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import load_dotenv

load_dotenv()

apikey = os.environ['apikey']

url = os.environ['url']

authenticator = IAMAuthenticator(apikey)
language_translator = LanguageTranslatorV3(
    version='2018-05-01',
    authenticator=authenticator
)

language_translator.set_service_url(url)

def english_to_french(english_text):
    #write the code here
    try:
        translation=language_translator.translate(
            text=english_text,
            model_id='en-fr').get_result()
    except:
        french_text='Try a different phrase.'
        return french_text
    french_text=translation['translations']
    french_text=french_text[0]
    french_text=french_text['translation']
    return french_text

def french_to_english(french_text):
    #write the code here
    try:
        translation=language_translator.translate(
            text=french_text,
            model_id='fr-en').get_result()
    except:
        english_text='Try a different phrase.'
        return english_text
    english_text=translation['translations']
    english_text=english_text[0]
    english_text=english_text['translation']
    return english_text 
    