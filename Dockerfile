FROM python:3.8.5

COPY ./requirements.txt /requirements.txt
RUN pip install -r /requirements.txt

RUN mkdir /crack-my-password
WORKDIR /crack-my-password
COPY ./app /crack-my-password


RUN adduser user
USER user


ENTRYPOINT ["python"]
CMD ["backend/server.py"]


