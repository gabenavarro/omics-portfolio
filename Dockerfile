FROM python:3.11.5-slim-bookworm

COPY . /app/
WORKDIR /app
RUN pip install --upgrade pip && \
    pip install -r requirements.txt

CMD ["gunicorn", "--workers=16", "--threads=4", "-b 0.0.0.0:80", "cloud:server", "--timeout 120"]