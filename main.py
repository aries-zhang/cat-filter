import requests
import json

def main():
    url = 'http://agl-developer-test.azurewebsites.net/people.json'
    response = requests.get(url)
    if response.status_code == 200:
        print json.dumps(response.json(), sort_keys=True, indent=2)
    else:
        print 'ERROR: ' + response.status_code

if __name__ == '__main__':
    main()