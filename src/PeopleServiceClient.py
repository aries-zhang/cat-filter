# -*- coding: utf-8 -*-
'''The people service client class. This class encapsulates the people 
service(s).
'''
import requests

class PeopleServiceClient:
    def __init__(self, host):
        '''Initializer

        Args:
            host (str): The host of people service.
        '''
        self.host = host
    
    def get_people(self):
        '''Calls people service and returns a list of people.
        
        Returns:
            :obj:`list`: A list of people or None if http call fails.
        '''
        url = self.host + '/people.json'
        response = requests.get(url)

        if response.status_code != 200:
            print('HTTP ERROR: ' + response.status_code)
            return None
        
        return response.json()
