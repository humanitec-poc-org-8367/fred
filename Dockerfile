FROM python:latest

EXPOSE 8443

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

COPY time.py time.py
CMD ["python3", "time.py"]