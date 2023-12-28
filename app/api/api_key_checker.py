import dotenv

SECRET_API_HEADER_KEY = dotenv.dotenv_values().get("API_HEADER_KEY")
SECRET_API_KEY = dotenv.dotenv_values().get("SECRET_API_KEY")

def check_api_key(request_headers):
    if SECRET_API_HEADER_KEY not in request_headers:
        return False, {'error': 'API key missing'}, 401

    provided_api_key = request_headers[SECRET_API_HEADER_KEY]
    if provided_api_key != SECRET_API_KEY:
        return False, {'error': 'Invalid API key'}, 401

    return True, None, None
