# -*- coding: utf-8 -*-
'''The main entrance'''
import os
from src.Transformer import Transformer
from src.PeopleServiceClient import PeopleServiceClient


def main():
    '''Calls the API, calls the transform method, and print the 
    transformed data
    '''
    host = os.environ['API_HOST']
    original_data = PeopleServiceClient(host).get_people()

    if original_data != None:
        transformed_data = Transformer().transform(original_data)
        for gender, cats in transformed_data.iteritems():
            print gender
            for cat in cats:
                print '\t' + cat

if __name__ == '__main__':
    main()