import os
from langchain_community.graphs import Neo4jGraph
from langchain.chains import GraphCypherQAChain
from langchain_openai import ChatOpenAI
from langchain.prompts import PromptTemplate

UCL_QA_MODEL = os.getenv("UCL_QA_MODEL")
UCL_CYPHER_MODEL = os.getenv("UCL_CYPHER_MODEL")

NEO4J_URI = os.getenv("NEO4J_URI")
NEO4J_USERNAME = os.getenv("NEO4J_USERNAME")
NEO4J_PASSWORD = os.getenv("NEO4J_PASSWORD")


graph = Neo4jGraph(
    url=NEO4J_URI,
    username=NEO4J_USERNAME,
    password=NEO4J_PASSWORD
)


graph.refresh_schema()


cypher_generation_template = """
Task:
Generate Cypher query for a Neo4j graph database.

Instructions:
Use only the provided relationship types and properties in the schema.
Do not use any other relationship types or properties that are not provided.

Schema:
{schema}

Note:
Do not include any explanations or apologies in your responses.
Do not respond to any questions that might ask anything other than
for you to construct a Cypher statement. Do not include any text except
the generated Cypher statement. Make sure the direction of the relationship is
correct in your queries. Make sure you alias both entities and relationships
properly. Do not run any queries that would add to or delete from
the database. Make sure to alias all statements that follow as with
statement (e.g. WITH t as visit, c.billing_amount as billing_amount)
If you need to divide numbers, make sure to
filter the denominator to be non zero.

Examples:

# How many teams played champion league ?
match(n:Team) return count(n)

#What are the score of all Real Madrid's matches
MATCH(t:Team{{name: "Real Madrid"}})-[r:PLAYED_WITH]->(t2:Team)
return r.date, r.homeScore, r.awayScore, t2.name

# Which teams have played against a specific team and what were the match scores?
MATCH (t1:Team {{name: "TeamName"}})-[r:PLAYED_WITH]-(t2:Team)
RETURN t2.name AS opponent_team,
       r.homeScore AS home_team_score,
       r.awayScore AS away_team_score

# What is the win-loss record of a specific team?
MATCH (t:Team {{name: "TeamName"}})-[r:PLAYED_WITH]->(opponent:Team)
WITH t,
     CASE
         WHEN r.homeScore > r.awayScore THEN 'Win'
         WHEN r.homeScore < r.awayScore THEN 'Loss'
         ELSE 'Draw'
     END AS result
RETURN result, COUNT(result) AS count

Make sure to use IS NULL or IS NOT NULL when analyzing missing properties.
Never return embedding properties in your queries. You must never include the
statement "GROUP BY" in your query. Make sure to alias all statements that
follow as with statement (e.g. WITH v as visit, c.billing_amount as
billing_amount)
If you need to divide numbers, make sure to filter the denominator to be non
zero.

The question is:
{question}
"""

cypher_generation_prompt = PromptTemplate(
    input_variables=["schema", "question"], template=cypher_generation_template
)

qa_generation_template = """You are an assistant that takes the results
from a Neo4j Cypher query and forms a human-readable response. The
query results section contains the results of a Cypher query that was
generated based on a users natural language question. The provided
information is authoritative, you must never doubt it or try to use
your internal knowledge to correct it. Make the answer sound like a
response to the question.

Query Results:
{context}

Question:
{question}

If the provided information is empty, say you don't know the answer.
Empty information looks like this: []

If the information is not empty, you must provide an answer using the
results. If the question involves a time duration, assume the query
results are in units of days unless otherwise specified.

When names are provided in the query results, such as team names,
beware  of any names that have commas or other punctuation in them.
For instance, 'Real, Madrid' is a single team name,
not multiple teams. Make sure you return any list of names in
a way that isn't ambiguous and allows someone to tell what the full
names are.

Never say you don't have the right information if there is data in
the query results. Make sure to show all the relevant query results
if you're asked.

Helpful Answer:
"""

qa_generation_prompt = PromptTemplate(
    input_variables=["context", "question"], template=qa_generation_template
)

ucl_cypher_chain = GraphCypherQAChain.from_llm(
    cypher_llm=ChatOpenAI(model=UCL_CYPHER_MODEL, temperature=0),
    qa_llm=ChatOpenAI(model=UCL_QA_MODEL, temperature=0),
    graph=graph,
    verbose=True,
    qa_prompt=qa_generation_prompt,
    cypher_prompt=cypher_generation_prompt,
    validate_cypher=True,
    top_k=100,
)
