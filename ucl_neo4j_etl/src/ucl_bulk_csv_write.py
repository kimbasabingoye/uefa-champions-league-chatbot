import os
import logging
from retry import retry
from neo4j import GraphDatabase
from load_teams import insert_teams
from load_players import insert_players
from load_matches import insert_matches
from load_player_teams import insert_affiliation


# Neo4j config
NEO4J_URI = os.getenv("NEO4J_URI")
NEO4J_USERNAME = os.getenv("NEO4J_USERNAME")
NEO4J_PASSWORD = os.getenv("NEO4J_PASSWORD")

# Configure the logging module
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s]: %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
)


LOGGER = logging.getLogger(__name__)

NODES = ["Team", "Player"]


def _set_uniqueness_constraints(tx, node):
    query = f"""CREATE CONSTRAINT IF NOT EXISTS FOR (n:{node})
        REQUIRE n.id IS UNIQUE;"""
    _ = tx.run(query, {})


@retry(tries=100, delay=5)
def load_ucl_graph_data() -> None:
    """Load UCL data into Neo4j"""

    driver = GraphDatabase.driver(
        NEO4J_URI, auth=(NEO4J_USERNAME, NEO4J_PASSWORD)
    )

    LOGGER.info("Setting uniqueness constraints on nodes")
    with driver.session(database="neo4j") as session:
        for node in NODES:
            session.execute_write(_set_uniqueness_constraints, node)

    LOGGER.info("Loading Team nodes")
    insert_teams()

    LOGGER.info("Loading payer nodes")
    insert_players()

    LOGGER.info("Loading Players affiliation")
    insert_affiliation()

    LOGGER.info("Loading matches")
    insert_matches()


if __name__ == "__main__":
    load_ucl_graph_data()
