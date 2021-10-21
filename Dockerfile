FROM python:3.8.5-slim-buster
WORKDIR /usr/src/app
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
RUN pip install pipenv==v2021.5.29 --no-cache-dir
COPY Pipfile* ./
RUN pipenv install --dev --system --deploy
COPY . .
EXPOSE 80

##CMD [ "uvicorn", "app.main:app", "--host", "0.0.0.0", "--reload" ]