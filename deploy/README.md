# DEV ENVIRONMENT

Compose up

```docker-compose -f deploy/docker-compose.dev.yml up -d```

Compose down

```docker-compose -f deploy/docker-compose.dev.yml down --remove-orphans.```

Wait for database

```sh database/wait-for-database.sh url=127.0.0.1 port=3306 user=user pass=pass```
