FROM python:3.8

COPY ./CMS /srv/www/CMS
WORKDIR /srv/www/CMS

RUN pip install -r req.txt
