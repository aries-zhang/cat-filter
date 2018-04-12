import requests

class Client:
    def __init__(self, host):
        self.host = host
    
    def get_people(self):
        url = self.host + '/people.json'
        response = requests.get(url)

        if response.status_code != 200:
            print('HTTP ERROR: ' + response.status_code)
            return None
        
        return response.json()
