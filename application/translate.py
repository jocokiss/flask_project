from google.cloud import translate_v2

def translate(text, source_language, target_language):
    credentials_path = '/Users/jocokiss/flask_project/microblog_translate.json' # update with your own path
    client = translate_v2.Client.from_service_account_json(credentials_path)

    result = client.translate(text,source_language=source_language, target_language=target_language)
    return result['translatedText']