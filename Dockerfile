FROM python:3.9.4
WORKDIR /app
COPY . .
RUN pip install -r requirements.txt
CMD fastapi run api.py
