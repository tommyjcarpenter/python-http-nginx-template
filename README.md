# Tech Stack
- Swagger
- Connexion
- Flask
- uwsgi
- NGINX
- Python3.6

# A Note About App Structure
I am using https://hub.docker.com/r/tiangolo/uwsgi-nginx-flask/
Big credit to this project: https://github.com/tiangolo/uwsgi-nginx-flask-docker

This is a uwsgi+flask+nginx all in one container. It requires an specific app structure to use, which I'm using.

# Unit Testing
```
cd app/app
tox
open htmlcov/index.html
```

# Running locally
```
cd app/app
pip install --ignore-installed .; ./main.py
```

# Docker
## building
```
docker build -t myapi:X.Y.Z .
```
## running
```
docker run -dt -p 80:80 myapi:X.Y.Z
```

## Test CURLs
NOTE: Change the port from 10000 to 80 depending on whether running locally or not
```
curl -v -H "Content-Type: application/json" -X POST localhost:10000/baz -d '{"query_string" : "amaaaaaaazing"}'
curl localhost:10000/foo/asdf
```
