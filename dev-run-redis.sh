docker rm tekateki-redis 2>/dev/null
docker run --name tekateki-redis -d -p 6379:6379 redis
