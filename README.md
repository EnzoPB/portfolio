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
- `DATABASE_URL`: Postgres url to connect to the database (format postgres://username:password@host:port/database)

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
