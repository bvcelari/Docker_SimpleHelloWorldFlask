FROM python:3.6
MAINTAINER Juan Perez "bvcelari@gmail.com"
COPY . /app
WORKDIR /app
RUN pip install flask
ENTRYPOINT ["python"]
CMD ["app.py"]
