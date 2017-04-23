# Task runner #

Simple task manager on Django with PostgreSQL database.

## Installation

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

and setup django database

```bash
python ./manage.py migrate --run-syncdb
```

