FROM python:3.12-slim

ENV PYTHONUNBUFFERED=1

WORKDIR /app

COPY src/ src/

ENV PORT=8080
EXPOSE 8080

USER 1000:1000

CMD ["python3", "src/server.py"]
