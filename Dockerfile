FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

ARG INSTALL_JUPYTER=false
RUN if [ "$INSTALL_JUPYTER" = "true" ]; then pip install jupyter; fi
