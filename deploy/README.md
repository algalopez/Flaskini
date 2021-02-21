# DEV ENVIRONMENT

##Compose up

```docker-compose -f deploy/docker-compose.dev.yml up --build -d```

##Compose down

```docker-compose -f deploy/docker-compose.dev.yml down --remove-orphans.```

##Wait for database

```./database/wait-for-database.sh url=127.0.0.1 port=3306 user=user pass=pass```

##Migrate

**Build image**

```docker build -f database/Dockerfile.flyway -t flaskini-flyway .```

**Create the database**

```docker run --rm --name flaskini-flyway --net=host flaskini-flyway clean migrate```

**Create and populate the database**

```docker run --rm --name flaskini-flyway --net=host flaskini-flyway -configFiles=/flyway/conf/flyway-pre.conf clean migrate```


