FROM python:3-alpine

COPY . /service

WORKDIR /service

RUN pip install -r requirements.txt

EXPOSE 5000/tcp

ENTRYPOINT ["python"]

CMD ["service.py"]