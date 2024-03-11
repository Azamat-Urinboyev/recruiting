From python:3.12

WORKDIR .

COPY requirements.txt .

RUN pip install  --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 8000

CMD [ "python", "manage.py", "runserver", "ip address:8000"]



