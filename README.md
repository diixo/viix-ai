
# viix.ai - AI web-tool implemented AI-search, based on text embeddings

```bash
py core/manage.py runserver
```


- DB migrations with migrates:
```bash
py core/manage.py makemigrations
py core/manage.py migrate
```


Run server from root directory.
```
uvicorn server.server_api:app --host localhost --port 8001 --reload
```
