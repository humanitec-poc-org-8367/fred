FROM python:latest

EXPOSE 8443

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

COPY petstore.py petstore.py
CMD ["python3", "petstore.py"]