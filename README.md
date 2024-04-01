# uefa-champions-league-chatbot
This chatbot interfaces with a [LangChain](https://python.langchain.com/docs/get_started/introduction) agent designed to answer questions about 2023-2024 UEFA Champions League.


# How to run the app

0. Set environment variables

```
NEO4J_URI
NEO4J_USERNAME
NEO4J_PASSWORD
OPENAI_API_KEY
CHATBOT_URL
UCL_AGENT_MODEL
UCL_CYPHER_MODEL
UCL_QA_MODEL
```

1. Start and docker instance Neo4j with APOC plugin 

We assume that you already have docker in your machine


```
docker run -p 7474:7474 -p 7687:7687 -v $PWD/data:/data -v $PWD/plugins:/plugins --name neo4j-apoc \
    -e NEO4J_AUTH=neo4j/Kalimba10$ \
    -e NEO4J_apoc_export_file_enabled=true \
    -e NEO4J_apoc_import_file_enabled=true \
    -e NEO4J_apoc_import_file_use__neo4j__config=true \
    -e NEO4J_PLUGINS=\[\"apoc-extended\"\] \
    neo4j:5.16
```

2. Set a virtual env

Go to root directory of the project.
Create a virtual env

```
python -m venv venv
```


3. Start the API

```
. venv/bin/activate

cd chatbot_api

python -m pip install .

cd src

uvicorn main:app
```

4. Start the frontend


```
. venv/bin/activate

cd chatbot_frontend

python -m pip install .

cd src

streamlit run  main.py
```

