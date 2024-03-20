from neo4j import GraphDatabase
import os

NEO4J_URI = os.getenv("NEO4J_URI")
NEO4J_USERNAME = os.getenv("NEO4J_USERNAME")
NEO4J_PASSWORD = os.getenv("NEO4J_PASSWORD")


def insert_teams():
    # Cypher queries
    insert_team_queries = [
        "CREATE (:Team {name: 'Sevilla', country: 'Spain'})", "CREATE (:Team {name: 'Real Sociedad', country: 'Spain'})", "CREATE (:Team {name: 'Barcelona', country: 'Spain'})", "CREATE (:Team {name: 'Real Madrid', country: 'Spain'})", "CREATE (:Team {name: 'Atletico Madrid', country: 'Spain'})", "CREATE (:Team {name: 'Napoli', country: 'Italy'})", "CREATE (:Team {name: 'Inter', country: 'Italy'})", "CREATE (:Team {name: 'Milan', country: 'Italy'})", "CREATE (:Team {name: 'Lazio', country: 'Italy'})", "CREATE (:Team {name: 'Manchester United', country: 'England'})", "CREATE (:Team {name: 'Newcastle United', country: 'England'})", "CREATE (:Team {name: 'Manchester City', country: 'England'})", "CREATE (:Team {name: 'Arsenal', country: 'England'})", "CREATE (:Team {name: 'Union Berlin', country: 'Germany'})", "CREATE (:Team {name: 'Dortmund', country: 'Germany'})", "CREATE (:Team {name: 'Leipzig', country: 'Germany'})", "CREATE (:Team {name: 'Bayern Munich', country: 'Germany'})", "CREATE (:Team {name: 'Porto', country: 'Portugal'})", "CREATE (:Team {name: 'Benfica', country: 'Portugal'})", "CREATE (:Team {name: 'Braga', country: 'Portugal'})", "CREATE (:Team {name: 'Netherlands', country: 'PSV'})", "CREATE (:Team {name: 'Netherlands', country: 'Feyenoord'})", "CREATE (:Team {name: 'Lens', country: 'France'})", "CREATE (:Team {name: 'PSG', country: 'France'})", "CREATE (:Team {name: 'Galatasaray', country: 'Turkey'})", "CREATE (:Team {name: 'Salzburg', country: 'Austria'})", "CREATE (:Team {name: 'Copenhagen', country: 'Denmark'})", "CREATE (:Team {name: 'Celtic', country: 'Scotland'})", "CREATE (:Team {name: 'Young Boys', country: 'Switzerland'})", "CREATE (:Team {name: 'Antwerp', country: 'Belgium'})", "CREATE (:Team {name: 'Red Star FC', country: 'Serbia'})", "CREATE (:Team {name: 'Shakhtar Donetsk', country: 'Ukraine'})"
    ]

    # Function to execute queries
    def execute_queries(driver):
        with driver.session() as session:
            for query in insert_team_queries:
                session.run(query)

    import os

    NEO4J_URI = os.getenv("NEO4J_URI")
    NEO4J_USERNAME = os.getenv("NEO4J_USERNAME")
    NEO4J_PASSWORD = os.getenv("NEO4J_PASSWORD")
    # Connect to Neo4j
    driver = GraphDatabase.driver(
        NEO4J_URI, auth=(NEO4J_USERNAME, NEO4J_PASSWORD))

    # Execute queries
    execute_queries(driver)

    # Close the connection
    driver.close()

    # with GraphDatabase.driver(uri,  auth=(username, password)) as driver:
    #    driver.verify_connectivity()
