FROM kennethreitz/pipenv

WORKDIR /app

COPY * /app/

# RUN pip install pipenv

RUN pipenv install --deploy --system

EXPOSE 8000

CMD ["gunicorn", "hot_wheels:app", "-b", "0.0.0.0:8000"]
