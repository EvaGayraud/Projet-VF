FROM python:3

WORKDIR /usr/src/Projet-VF

COPY config/requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 8050

CMD [ "python", "./graph_paris.py" ]
