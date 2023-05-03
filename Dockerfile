FROM python:3.11
WORKDIR /app
COPY requirements.txt ./
RUN pip3 install -r requirements.txt
COPY ./teacher_panel ./teacher_panel
CMD flask --app teacher_panel run --port 80 --host 0.0.0.0
