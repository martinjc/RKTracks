import json
import requests

from urllib.parse import urlencode, quote

from _credentials import client_id, client_secret, access_token

def get_auth_url():
# create an authorisation url to copy paste into a browser window
# so we can get an access token to store in _credentials.py

    base_url = "https://runkeeper.com/"
    endpoint = "apps/authorize"
    params = {
        'response_type': 'code',
        'client_id': client_id,
        'redirect_uri': 'http://www.martinjc.com',
    }

    auth_url = base_url + endpoint + "?" + urlencode(params, quote_via=quote)
    return auth_url

def do_auth():

    base_url = "https://runkeeper.com/"
    endpoint = "apps/token"
    params = {
        'grant_type': 'authorization_code',
        'code': code,
        'client_id': client_id,
        'client_secret': client_secret,
        'redirect_uri': 'http://www.martinjc.com',
    }

    r = requests.post(base_url + endpoint, params)
    print(r.json())

def get_data(endpoint, params=None):

    base_url = "https://api.runkeeper.com/"
    endpoint = endpoint

    headers = {
        'Authorization': 'Bearer ' + access_token
    }

    r = requests.get(base_url + endpoint, params=params, headers=headers)
    return r.json()

def get_fitness_activities():

    with open('activies.json', 'w') as output_file:

        activities = []
        activity_data = get_data('fitnessActivities')

        num_activities = activity_data['size']
        num_calls = int(num_activities / 25)
        call_count = 0

        if activity_data.get('items'):
            activities.extend(activity_data['items'])
            print(call_count, len(activity_data['items']), len(activities))

        while activity_data.get('next') and call_count < num_calls:
            activity_data = get_data(activity_data['next'])
            call_count += 1

            if activity_data.get('items'):
                activities.extend(activity_data['items'])
                print(call_count, len(activity_data['items']), len(activities))

            json.dump(activities, output_file)




if __name__ == '__main__':
    # print(get_auth_url())
    get_fitness_activities()
