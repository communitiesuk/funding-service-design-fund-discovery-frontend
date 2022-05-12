FROM python:3.10-slim-bullseye

RUN pip install --upgrade pip

WORKDIR /app
COPY . /app
RUN pip --no-cache-dir install --ignore-installed distlib -r requirements.txt
RUN python3 build.py

CMD ["flask", "run", "--host=0.0.0.0"]
