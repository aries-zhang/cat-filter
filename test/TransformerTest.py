import unittest
import json
from src.Transformer import Transformer

class TransformerTest(unittest.TestCase):
    def test_key_selector_should_work(self):
        person = {'gender':'Male', 'name':'Aries'}
        self.assertEqual(Transformer().key_selector(person), 'Male')

    def test_resolve_pets_should_work(self):
        person = '''[{
                        "name": "Bob",
                        "gender": "Male",
                        "age": 23,
                        "pets": [{
                            "name": "Garfield",
                            "type": "Cat"
                        }, {
                            "name": "Fido",
                            "type": "Dog"
                        }]
                    }]'''
        pets = Transformer().resolve_pets(json.loads(person))
        self.assertEqual(2, len(pets))

    
    def test_resolve_pets_of_multiple_owners_should_work(self):
        person = '''[{
                        "name": "Bob",
                        "gender": "Male",
                        "age": 23,
                        "pets": [{
                            "name": "Garfield",
                            "type": "Cat"
                        }, {
                            "name": "Fido",
                            "type": "Dog"
                        }]
                    },{
                        "name": "Lily",
                        "gender": "Female",
                        "age": 23,
                        "pets": [{
                            "name": "Garfield",
                            "type": "Cat"
                        }]
                    }]'''
        pets = Transformer().resolve_pets(json.loads(person))
        self.assertEqual(3, len(pets))

    def test_resolve_none_pets_should_work(self):
        person = '''[{
                        "name": "Aries",
                        "gender": "Male",
                        "age": 32,
                        "pets": null
                    }]'''

        pets = Transformer().resolve_pets(json.loads(person))
        self.assertEqual(0, len(pets))

    def test_resolve_empty_pets_should_work(self):
        person = '''[{
                        "name": "Aries",
                        "gender": "Male",
                        "age": 32,
                        "pets": []
                    }]'''

        pets = Transformer().resolve_pets(json.loads(person))
        self.assertEqual(0, len(pets))

    def test_resolve_cat_name_should_work(self):
        pets = '''[{
                    "name": "Garfield",
                    "type": "Cat"
                }, {
                    "name": "Fido",
                    "type": "Dog"
                }]'''

        pets = Transformer().resolve_cat_name(json.loads(pets))
        self.assertEqual(1, len(pets))
        self.assertEqual('Garfield', pets[0])

    def test_resolve_cat_name_with_empty_list_should_work(self):
        pets = []

        pets = Transformer().resolve_cat_name(pets)
        self.assertEqual(0, len(pets))

    def test_resolve_cat_name_with_lower_case_should_work(self):
        pets = '''[{
                    "name": "Garfield",
                    "type": "cat"
                }, {
                    "name": "Fido",
                    "type": "Dog"
                }]'''

        pets = Transformer().resolve_cat_name(json.loads(pets))
        self.assertEqual(1, len(pets))
        self.assertEqual('Garfield', pets[0])

    def test_flatten_should_work(self):
        pets = '''[[{
                    "name": "Garfield",
                    "type": "cat"
                }, {
                    "name": "Fido",
                    "type": "Dog"
                }],[{
                    "name": "Momo",
                    "type": "Dog"
                }]]'''

        pets = Transformer().flatten(json.loads(pets))
        self.assertEqual(3, len(pets))

    def test_flatten_empty_should_work(self):
        pets = []

        pets = Transformer().flatten(pets)
        self.assertEqual(0, len(pets))

    def test_cats_name_should_be_sorted(self):
        people = '''[{
                        "name": "Bob",
                        "gender": "Male",
                        "age": 23,
                        "pets": [{
                            "name": "Arfield",
                            "type": "Cat"
                        }, {
                            "name": "Fido",
                            "type": "Dog"
                        }]
                    }, {
                        "name": "Jennifer",
                        "gender": "Male",
                        "age": 18,
                        "pets": [{
                            "name": "Garfield",
                            "type": "Cat"
                        }]
                    }]'''
    
        cats = Transformer().transform(json.loads(people))['Male']
        self.assertEqual('Arfield', cats[0])
        self.assertEqual('Garfield', cats[1])

if __name__ == '__main__':
    unittest.main()