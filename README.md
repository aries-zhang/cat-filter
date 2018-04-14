# cat-filter

[![Build Status](https://travis-ci.org/aries-zhang/cat-filter.svg?branch=master)](https://travis-ci.org/aries-zhang/cat-filter)

To test: ```python -m test.TransformerTest```

To run:

- as docker container:

    ```bash
    sudo docker run -e API_HOST=http://agl-developer-test.azurewebsites.net arieszhang/cat-filter:latest
    ```

- as local python project: (this is not recommented since environment variable ```API_HOST``` is needed to be set before you run it)

    ```bash
    pip install -r requirements.txt
    python main.py
    ```
