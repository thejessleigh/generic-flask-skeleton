FROM python:3.8

RUN useradd -m appuser

WORKDIR /home/appuser 
USER appuser 
COPY ./ /home/appuser
RUN python3 -m venv venv && bash -c 'source venv/bin/activate && pip install poetry && poetry install --no-dev'

CMD ["bash", "startup.sh"]
