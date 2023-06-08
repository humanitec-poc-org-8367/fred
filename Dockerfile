FROM python:latest

EXPOSE 8443

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

COPY time-svc.py time-svc.py
CMD ["python3", "time-svc.py"]