FROM python:3

ADD new.py /

RUN pip install numpy

CMD [ "python", "new.py" ]