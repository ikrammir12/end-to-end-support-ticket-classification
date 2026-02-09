FROM python:3.10

WORKDIR /app

COPY app /app/app

RUN pip install --no-cache-dir fastapi uvicorn transformers \
    && pip install --no-cache-dir torch --index-url https://download.pytorch.org/whl/cpu

EXPOSE 8000

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
