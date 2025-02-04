FROM tiangolo/uvicorn-gunicorn-fastapi:python3.9

WORKDIR /web_app

COPY ./web_app /web_app
COPY requirements.txt /web_app/requirements.txt

RUN pip install --no-cache-dir -r requirements.txt

ENV PYTHONPATH=/web_app

CMD ["uvicorn", "web_app.main:app", "--host", "0.0.0.0", "--port", "8000"]
