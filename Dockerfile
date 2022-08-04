FROM selenium/standalone-firefox
USER root
WORKDIR /app

RUN apt-get update
RUN apt-get install -y python3-distutils python3-apt
RUN wget https://bootstrap.pypa.io/get-pip.py
RUN python3 get-pip.py

COPY src/main.py main.py
COPY requirements.txt requirements.txt

RUN python3 -m pip install -r requirements.txt

RUN chown -R seluser:seluser /app
RUN chmod 755 /app

USER seluser
ENTRYPOINT [ "python3", "main.py" ]