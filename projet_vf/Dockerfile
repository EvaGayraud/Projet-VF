FROM python:3

WORKDIR /usr/src/Projet-VF

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY ./ ./

WORKDIR /usr/src/Projet-VF/projet_vf

EXPOSE 8050

CMD [ "gunicorn", "-b", "0.0.0.0:8050", "graph_paris:server" ]
