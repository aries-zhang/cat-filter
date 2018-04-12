FROM python:2.7-slim-jessie
WORKDIR /cat-filter
COPY . /cat-filter
RUN cd /cat-filter && pip install -r requirements.txt
CMD ["python", "main.py"]