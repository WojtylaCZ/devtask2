FROM wojtylacz/pypostal-docker

RUN pip3 install pytest

COPY addressline /app

WORKDIR /app

RUN python3 -m pytest

CMD [ "python3", "/app/main.py" ]
