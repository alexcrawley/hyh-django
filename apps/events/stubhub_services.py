import requests

from django.conf import settings


class StubHubService(object):
    def __init__(self, *args, **kwargs):
        self.headers = {
            'Content-Type': 'application/json',
            'Accept': 'application/json',
            'Accept-Encoding': 'application/json',
            'Authorization': 'Bearer ' + settings.STUBHUB_APPLICATION_TOKEN,
        }

        self.base_url = settings.STUBHUB_URL


    def login(self, key, secret, username, password, grant_type='password'):
        auth = b64encode('%s:%s' % (key, secret))
        headers = {
            'Authorization': 'Basic ' + auth,
            'Content-Type': 'application/x-www-form-urlencoded'
        }

        data = {
            'grant_type': grant_type,
            'scope': self.mode,
            'username': username,
            'password': password,
        }

        response = requests.post(self.url + self.login_url, headers=headers, data=data)
        self.auth_info = response.json()
        self.headers['x-stubhub-user-guid'] = response.headers['x-stubhub-user-guid']
        # replease the auth token?
        self.headers['Authentication'] = 'Bearer ' + self.auth_info['access_token']
        return True

    def get_event_dict(self, stubhub_id):
        url = '%s/%s/%s' % (self.base_url, 'catalog/events/v2', stubhub_id)

        response = requests.get(url, headers=self.headers)

        return response
