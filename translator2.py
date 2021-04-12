import json
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator

url_lt = "https://api.eu-gb.language-translator.watson.cloud.ibm.com/instances/fc59df1e-28f2-4dac-86f1-a6ab4deba721"
apikey_lt = "35vzXTWoohUJ2wf7X92eWG3X_lqF3LN2pyKb-vgrQGUz"

version_lt = '2018-05-01'

def english_to_german():
    authenticator = IAMAuthenticator(apikey_lt)
    l_translator = LanguageTranslatorV3(version = version_lt, authenticator = authenticator)
    l_translator.set_service_url(url_lt)

    translation_response = l_translator.translate(\
    text = 'Hello, What are you doing ?', model_id = 'en-de')

    translation = translation_response.get_result()

    german_translation = translation['translations'][0]['translation']
    print(german_translation)

english_to_german()
