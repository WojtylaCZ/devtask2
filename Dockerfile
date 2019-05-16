FROM riordan/docker-jupyter-scipy-notebook-libpostal

RUN pip install pytest

COPY addressline /app

WORKDIR /app

RUN python3 -m pytest

CMD [ "python3", "/app/main.py" ]
