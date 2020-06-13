FROM python:3.8

COPY ./CMS/req.txt /srv/www/CMS/
COPY ./CMS/entrypoint.sh /srv/www/CMS/
WORKDIR /srv/www/CMS

RUN chmod +x entrypoint.sh
RUN pip install -r req.txt
