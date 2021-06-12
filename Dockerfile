FROM python:3

WORKDIR /usr/src/Projet-VF

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 8050

CMD [ "python", "./projet_vf/graph_paris.py" ]
