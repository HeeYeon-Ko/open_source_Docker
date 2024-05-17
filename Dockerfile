FROM python:3.10.2
RUN pip3 install django
WORKDIR /usr/src/app
COPY . .
WORKDIR ./TodoList
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
EXPOSE 8000