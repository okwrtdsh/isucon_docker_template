# isucon_docker_template

## docker swarm
```bash
docker service create --name registry --publish published=5000,target=5000 registry:2
docker compose build && docker compose push
docker stack deploy -c docker-compose.yml isucon
```

```bash
docker stack rm isucon
docker stack ps isucon
docker service ls
docker service inspect SERVICE --pretty
docker container ps -a
```


## docker compose (local)
```bash
docker run -d -p 5000:5000 --restart=always --name registry registry:2
docker compose build && docker compose push
docker compose up -d
```
