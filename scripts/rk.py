import os
import json
import requests

from urllib.parse import urlencode, quote

from _credentials import client_id, client_secret, access_token

DATA_DIR = os.path.join(os.getcwd(), 'scripts', 'data')

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
    print(r.status_code)
    if r.status_code != 200:
        print(r.json())
        return None
    return r.json()

def get_fitness_activities():
# store activity URIs separately
    with open('activities.json', 'w') as activities_output_file, open('activity_uris.json', 'w') as uri_output_file:

        activities = []
        activity_uris = []
        activity_data = get_data('fitnessActivities')

        num_activities = activity_data['size']
        num_calls = int(num_activities / 25)
        call_count = 0

        if activity_data.get('items'):
            activities.extend(activity_data['items'])
            print(call_count, len(activity_data['items']), len(activities))
            for activity in activity_data['items']:
                activity_uris.append(activity['uri'])

        while activity_data.get('next') and call_count < num_calls:
            activity_data = get_data(activity_data['next'])
            call_count += 1

            if activity_data.get('items'):
                activities.extend(activity_data['items'])
                print(call_count, len(activity_data['items']), len(activities))
                for activity in activity_data['items']:
                    activity_uris.append(activity['uri'])

        json.dump(activities, activities_output_file)
        json.dump(activity_uris, uri_output_file)


def download_activities(activity_list):

    for activity_uri in activity_list[0:100]:

        id_str = activity_uri.replace('/fitnessActivities/', '')
        filename = os.path.join(DATA_DIR, '%s.json' % id_str)
        if not os.path.exists(filename):
            activity_data = get_data(activity_uri)
            if activity_data is not None:
                with open(filename, 'w') as output_file:
                    json.dump(activity_data, output_file)



if __name__ == '__main__':
    # print(get_auth_url())
    # get_fitness_activities()
    with open('activity_uris.json', 'r') as input_file:
        activity_uris = json.load(input_file)
        download_activities(activity_uris)
