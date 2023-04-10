FROM python:latest
WORKDIR /etc/mysyte
COPY . /etc/mysyte
RUN pip3 install -r requirements.txt
CMD ["python3", "main.py"]