from itertools import groupby

class Transformer:
    def __init__(self):
        self.key_selector = lambda owner: owner['gender']
        self.resolve_pets = lambda owners: [owner['pets'] for owner in owners if owner['pets'] != None]
        self.resolve_cat_name = lambda pets: [pet['name'] for pet in pets if pet['type'].lower() == 'cat']
        self.flatten = lambda l: [pet for pets in l for pet in pets]

    def transform(self, original_data):
        sorted_data = sorted(original_data, key = self.key_selector)
        return {gender: sorted(self.resolve_cat_name(self.flatten(self.resolve_pets(owners)))) \
                    for gender, owners \
                    in groupby(sorted_data, self.key_selector)}

        