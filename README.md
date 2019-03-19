# Tech Stack
- OpenAPI3
- Connexion
- Flask
- uwsgi
- NGINX
- Python3.7

# A Note About App Structure
I am using https://hub.docker.com/r/tiangolo/uwsgi-nginx-flask/
Big credit to this project: https://github.com/tiangolo/uwsgi-nginx-flask-docker

This is a uwsgi+flask+nginx all in one container. It requires an specific app structure to use, which I'm using.

# Changing for a new project
The term `myapi` is present in:
1. `app/app/myapi`
2. `app/app/tox.ini`
3. `app/app/setup.py`
4. `app/app/tests/test_controller.py`
5. The folder in 1/openapi.yaml
Change those to `your_package_name`.

Next, change the version in `app/app/setup.py` accordingly.

Finally, modify the `Changelog.md` accordingly.

# Unit Testing
```
cd app/app
tox
open htmlcov/index.html
```

# Running locally
```
cd app/app
pip install --ignore-installed -e .
./main.py
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
