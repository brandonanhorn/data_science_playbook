

Original source

https://hackernoon.com/dont-install-postgres-docker-pull-postgres-bee20e200198



First get the Postgres image

```
docker pull postgres
```

Make directory for data

```
mkdir -p $HOME/docker/volumes/postgres
```

Actually build the container

```
docker run --rm --name pgdatabase -e POSTGRES_PASSWORD=squeegee1 -d -p 5432:5432 -v $HOME/docker/volumes/postgres:/var/lib/postgresql/data postgres
```

