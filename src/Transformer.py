# -*- coding: utf-8 -*-
'''The Transformer class. This class transforms certain input data into desired 
output data.'''
from itertools import groupby

class Transformer:
    def __init__(self):
        '''The initializer. Defines all lambda expressions used to transform data.'''
        self.flatten = lambda l: [pet for pets in l for pet in pets]
        self.key_selector = lambda owner: owner['gender']
        self.resolve_pets = lambda owners: self.flatten([owner['pets'] for owner in owners \
                                           if owner['pets'] != None])
        self.resolve_cat_name = lambda pets: [pet['name'] for pet in pets if pet['type'].lower() == 'cat']

    def transform(self, original_data):
        '''Transforms `original_data` into desired data format.
        
        Args:
            original_data (:obj:`list`): The people list from people service.

        Returns:
            :obj:`dict`: The dictionary contains cats only grouped by key as owner's gender.
        '''
        sorted_data = sorted(original_data, key = self.key_selector)
        return {gender: sorted(self.resolve_cat_name(self.resolve_pets(owners))) \
                    for gender, owners \
                    in groupby(sorted_data, self.key_selector)}
