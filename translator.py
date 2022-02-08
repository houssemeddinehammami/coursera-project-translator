from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator

authenticator = IAMAuthenticator('{2gF_dEm_XWg9NByUElAT2rXGhw3FweFg4cUGOdxnNy6t}')
language_translator = LanguageTranslatorV3(
    version='{2022-02-08}',
    authenticator=authenticator
)

language_translator.set_service_url('https://api.eu-gb.language-translator.watson.cloud.ibm.com/instances/57bd0f7c-81e3-4db8-b906-0a903b229870')










# Press the green button in the gutter to run the script.
if __name__ == '__main__':

