
# viix.ai - AI web-tool implemented AI-search, based on text embeddings


## Run django:
```bash
py core/manage.py runserver
```

## Run server (from root directory):
```
uvicorn server.server_api:app --host localhost --port 8001 --reload
```


- DB migrations with migrates:
```bash
py core/manage.py makemigrations
py core/manage.py migrate
```


## Virtual environment:

Create virtual environment using pipenv (Pipfile, Pipefile.lock will be create automatically):
```
pipenv --python 3.10.8
```

Dockerfile should contain the same python-version.

Follow to add all packages versions from **pip list**:
```
pipenv install numpy==1.26.1
pipenv install python-dotenv==1.0.1
pipenv install urllib3==2.0.6
pipenv install beautifulsoup4==4.12.2
pipenv install django==5.0
pipenv install django-environ==0.11.2
pipenv install fastapi==0.110.3
pipenv install uvicorn==0.29.0
pipenv install tensorflow==2.14.0
pipenv install keras==2.14.0
pipenv install faiss-cpu==1.8.0
pipenv install sentence-transformers==3.0.0
pipenv install djangorestframework==3.16.0
```
All this packages will be pushed into file **Pipfile**.
Regeneration **requirements.txt** should perform after every update the Pipfile.


All installed packages listed in Pipfile

### Create/regenerate the requirements.txt:
This necessary file required by Docker
```
pipenv requirements > requirements.txt
```

Removed env:
```
pipenv --rm
```

Path of env for current directory:
```
C:\Users\user\.virtualenvs\viix-ai-uFgYWhcO
```

<div align="left" width="1000" height="480">
  <img src="/imgs/viix-ai.png">
</div>
