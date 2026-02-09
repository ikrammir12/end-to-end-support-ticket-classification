FROM python:3.10

WORKDIR /app

# copy whole app folder
COPY app /app/app

# install dependencies
RUN pip install fastapi uvicorn transformers torch

EXPOSE 8000

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
