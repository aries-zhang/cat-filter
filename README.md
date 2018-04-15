# cat-filter

[![Build Status](https://travis-ci.org/aries-zhang/cat-filter.svg?branch=master)](https://travis-ci.org/aries-zhang/cat-filter)

To test: ```python -m test.TransformerTest```

To run:

- as docker container:

    ```bash
    sudo docker run -e PEOPLE_SERVICE_HOST=http://agl-developer-test.azurewebsites.net arieszhang/cat-filter:latest
    ```

- as local python project: (this is not recommented since environment variable ```PEOPLE_SERVICE_HOST``` is needed to be set before you run it)

    ```bash
    export PEOPLE_SERVICE_HOST=http://agl-developer-test.azurewebsites.net
    ```

    ```bash
    pip install -r requirements.txt
    python main.py
    ```
