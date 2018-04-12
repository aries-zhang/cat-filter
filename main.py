import os
from src.Transformer import Transformer
from src.Client import Client


def main():
    host = os.environ['API_HOST']
    original_data = Client(host).get_people()

    if original_data != None:
        transformed_data = Transformer().transform(original_data)
        for gender, cats in transformed_data.iteritems():
            print gender
            for cat in cats:
                print '\t' + cat

if __name__ == '__main__':
    main()