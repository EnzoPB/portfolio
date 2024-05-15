FROM python:3

WORKDIR /usr/src/app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt
RUN apt update -y
RUN apt install gettext -y

COPY . .

EXPOSE 8000

CMD [ "./start.sh" ]
