FROM python:2.7

COPY ./run.py /run.py

CMD ["sh", "-c", "/run.py"]
