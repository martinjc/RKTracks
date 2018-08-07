from urllib.parse import urlencode, quote

from _credentials import client_id, client_secret

def get_auth_url():
# create an authorisation url to copy paste into a browser window
# so we can get an access token to store in _credentials.py

    base_url = "https://runkeeper.com/"
    endpoint = "apps/authorize"
    params = {
        'response_type': 'urlencode',
        'client_id': client_id,
        'redirect_uri': 'http://www.martinjc.com',
    }

    auth_url = base_url + endpoint + "?" + urlencode(params, quote_via=quote)
    return auth_url

if __name__ == '__main__':
    print(get_auth_url())
