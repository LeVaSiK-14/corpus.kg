FROM python:3

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /app

COPY requirements.txt /app/
ADD wsgi-entrypoint.sh /app/

RUN python -m pip install --upgrade pip
RUN pip install -r requirements.txt

COPY . /app/
EXPOSE 8000

CMD [ "chmod", "+x", "wsgi-entrypoint.sh" ]