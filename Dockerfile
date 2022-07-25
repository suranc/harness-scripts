FROM python:3

ADD requirements.txt /work/requirements.txt
WORKDIR /work
RUN pip install -r requirements.txt

ADD script.py /work/script.py

CMD python3 /work/script.py