# Para que o python funcione no wsl2 é necessário também instalar:

```bash
sudo apt-get install build-essential zlib1g-dev libffi-dev libssl-dev libbz2-dev libreadline-dev libsqlite3-dev liblzma-dev
```

## Comandos

### Subir os containers do PostgreSQL e PgAdmin

```bash
docker compose up
```

### Subir o Server Django

```bash
python manage.py runserver
```

### Criar migrations

```bash
python manage.py makemigrations
```

### Rodar migrations

```bash
python manage.py migrate
```

### Criar superuser

```bash
python manage.py createsuperuser
```
