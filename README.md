# Task runner #

Simple task manager on Python 3 Django with PostgreSQL database and Celery.

## Installation

### Create Enviroment

```python
virtualenv -p python3 env
source ./env/bin/activate
pip install -r requirements.txt
```

### Create database (PostgreSQL 9.3)

Setup PostgreSQL container and create database:

```bash
$ docker run -it --name runner-psql-db -e POSTGRES_USER=runner -e POSTGRES_PASSWORD=cYTiCOIO -p 5432:5432 -d postgres:9.3
$ docker exec -it runner-psql-db bash
root@ee5aa253df6d:/# psql -U postgres
psql (9.3.16)
Type "help" for help.

postgres=# CREATE DATABASE runner_db WITH OWNER runner ENCODING 'utf-8';
CREATE DATABASE
postgres=# \q
root@d51c3c54e339:/# exit
exit
```

and sync

```bash
python manage.py migrate --run-syncdb
```

## Run

### Run celery
```python
python manage.py celeryd
```

### Run UI
```python
python manage.py runserver 127.0.0.1:8080
```

