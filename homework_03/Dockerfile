# docker run -p 8000:8000 -it app
FROM python:3.11.6-bookworm

ENV PYTHONUNBUFFERED=1

WORKDIR /app

RUN pip install --upgrade pip "poetry==1.6.1"
RUN poetry config virtualenvs.create false --local

COPY poetry.lock pyproject.toml ./

RUN poetry install

COPY . .

EXPOSE 8000

CMD ["uvicorn", "main:app", "--host", "0.0.0.0"]

