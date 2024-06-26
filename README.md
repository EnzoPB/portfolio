# Portfolio

Simple showcase & portfolio website, made in with Django.

## Build & deploy

Create a virtual environment and activate it:
```bash
python3 -m venv .
source bin/activate
```

Create a .env file with the following values:
- [`DEBUG`](https://docs.djangoproject.com/en/4.2/ref/settings/#debug)
- [`ALLOWED_HOSTS`](https://docs.djangoproject.com/en/4.2/ref/settings/#allowed-hosts)
- `DISCORD_WEBHOOK_URL`: A Discord webhook to send the messages sent from the contact form
- [`SECRET_KEY`](https://docs.djangoproject.com/en/4.2/ref/settings/#secret-key)
- MySQL credentials:
  - DATABASE_DB
  - DATABASE_USERNAME
  - DATABASE_PASSWORD
  - DATABASE_HOST
  - DATABASE_PORT
- AWS S3 credentials:
  - S3_ACCESS_KEY
  - S3_SECRET
  - S3_BUCKET_NAME


Create the database:
```bash
./manage.py migrate
```

Start the server:
```bash
gunicorn enzopbme.wsgi
```

## License

[MIT](https://github.com/EnzoPB/portfolio/blob/master/LICENSE)
