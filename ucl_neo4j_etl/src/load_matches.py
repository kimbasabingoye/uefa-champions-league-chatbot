from neo4j import GraphDatabase


def insert_matches():

    count = 0

    queries = [
        "MATCH (team1:Team {name: 'Galatasaray'}), (team2:Team {name: 'Copenhagen'}) CREATE (team1)-[:PLAYED_WITH {date: date('2023-09-20'), homeScore: 2, awayScore: 2}]->(team2)",
        "MATCH (team1:Team {name: 'Bayern Munich'}), (team2:Team {name: 'Manchester United'}) CREATE (team1)-[:PLAYED_WITH {date: date('2023-09-20'), homeScore: 4, awayScore: 3}]->(team2)",
        "MATCH (team1:Team {name: 'Manchester United'}), (team2:Team {name: 'Galatasaray'}) CREATE (team1)-[:PLAYED_WITH {date: date('2023-10-03'), homeScore: 2, awayScore: 3}]->(team2)",
        "MATCH (team1:Team {name: 'Copenhagen'}), (team2:Team {name: 'Bayern Munich'}) CREATE (team1)-[:PLAYED_WITH {date: date('2023-10-03'), homeScore: 1, awayScore: 2}]->(team2)",
        "MATCH (team1:Team {name: 'Galatasaray'}), (team2:Team {name: 'Bayern Munich'}) CREATE (team1)-[:PLAYED_WITH {date: date('2023-10-24'), homeScore: 1, awayScore: 3}]->(team2)",
        "MATCH (team1:Team {name: 'Manchester United'}), (team2:Team {name: 'Copenhagen'}) CREATE (team1)-[:PLAYED_WITH {date: date('2023-10-24'), homeScore: 1, awayScore: 0}]->(team2)",
        "MATCH (team1:Team {name: 'Bayern Munich'}), (team2:Team {name: 'Galatasaray'}) CREATE (team1)-[:PLAYED_WITH {date: date('2023-11-08'), homeScore: 2, awayScore: 1}]->(team2)",
        "MATCH (team1:Team {name: 'Copenhagen'}), (team2:Team {name: 'Manchester United'}) CREATE (team1)-[:PLAYED_WITH {date: date('2023-11-08'), homeScore: 4, awayScore: 3}]->(team2)",
        "MATCH (team1:Team {name: 'Galatasaray'}), (team2:Team {name: 'Manchester United'}) CREATE (team1)-[:PLAYED_WITH {date: date('2023-11-29'), homeScore: 3, awayScore: 3}]->(team2)",
        "MATCH (team1:Team {name: 'Bayern Munich'}), (team2:Team {name: 'Copenhagen'}) CREATE (team1)-[:PLAYED_WITH {date: date('2023-11-29'), homeScore: 0, awayScore: 0}]->(team2)",
        "MATCH (team1:Team {name: 'Manchester United'}), (team2:Team {name: 'Bayern Munich'}) CREATE (team1)-[:PLAYED_WITH {date: date('2023-12-12'), homeScore: 0, awayScore: 1}]->(team2)",
        "MATCH (team1:Team {name: 'Copenhagen'}), (team2:Team {name: 'Galatasaray'}) CREATE (team1)-[:PLAYED_WITH {date: date('2023-12-12'), homeScore: 1, awayScore: 0}]->(team2)",
        "MATCH (team1:Team {name: 'Sevilla'}), (team2:Team {name: 'Lens'}) CREATE (team1)-[:PLAYED_WITH {date: date('2023-09-20'), homeScore: 1, awayScore: 1}]->(team2)",
        "MATCH (team1:Team {name: 'Arsenal'}), (team2:Team {name: 'PSV'}) CREATE (team1)-[:PLAYED_WITH {date: date('2023-09-20'), homeScore: 4, awayScore: 0}]->(team2)",
        "MATCH (team1:Team {name: 'Lens'}), (team2:Team {name: 'Arsenal'}) CREATE (team1)-[:PLAYED_WITH {date: date('2023-10-03'), homeScore: 2, awayScore: 1}]->(team2)",
        "MATCH (team1:Team {name: 'PSV'}), (team2:Team {name: 'Sevilla'}) CREATE (team1)-[:PLAYED_WITH {date: date('2023-10-03'), homeScore: 2, awayScore: 2}]->(team2)",
        "MATCH (team1:Team {name: 'Sevilla'}), (team2:Team {name: 'Arsenal'}) CREATE (team1)-[:PLAYED_WITH {date: date('2023-10-24'), homeScore: 1, awayScore: 2}]->(team2)",
        "MATCH (team1:Team {name: 'Lens'}), (team2:Team {name: 'PSV'}) CREATE (team1)-[:PLAYED_WITH {date: date('2023-10-24'), homeScore: 1, awayScore: 1}]->(team2)",
        "MATCH (team1:Team {name: 'Arsenal'}), (team2:Team {name: 'Sevilla'}) CREATE (team1)-[:PLAYED_WITH {date: date('2023-11-08'), homeScore: 2, awayScore: 0}]->(team2)",
        "MATCH (team1:Team {name: 'PSV'}), (team2:Team {name: 'Lens'}) CREATE (team1)-[:PLAYED_WITH {date: date('2023-11-08'), homeScore: 1, awayScore: 0}]->(team2)",
        "MATCH (team1:Team {name: 'Sevilla'}), (team2:Team {name: 'PSV'}) CREATE (team1)-[:PLAYED_WITH {date: date('2023-11-29'), homeScore: 2, awayScore: 3}]->(team2)",
        "MATCH (team1:Team {name: 'Arsenal'}), (team2:Team {name: 'Lens'}) CREATE (team1)-[:PLAYED_WITH {date: date('2023-11-29'), homeScore: 6, awayScore: 0}]->(team2)",
        "MATCH (team1:Team {name: 'Lens'}), (team2:Team {name: 'Sevilla'}) CREATE (team1)-[:PLAYED_WITH {date: date('2023-12-12'), homeScore: 2, awayScore: 1}]->(team2)",
        "MATCH (team1:Team {name: 'PSV'}), (team2:Team {name: 'Arsenal'}) CREATE (team1)-[:PLAYED_WITH {date: date('2023-12-12'), homeScore: 1, awayScore: 1}]->(team2)",
        "MATCH (team1:Team {name: 'Real Madrid'}), (team2:Team {name: 'Union Berlin'}) CREATE (team1)-[:PLAYED_WITH {date: date('2023-09-20'), homeScore: 1, awayScore: 0}]->(team2)",
        "MATCH (team1:Team {name: 'Braga'}), (team2:Team {name: 'Napoli'}) CREATE (team1)-[:PLAYED_WITH {date: date('2023-09-20'), homeScore: 1, awayScore: 2}]->(team2)",
        "MATCH (team1:Team {name: 'Union Berlin'}), (team2:Team {name: 'Braga'}) CREATE (team1)-[:PLAYED_WITH {date: date('2023-10-03'), homeScore: 2, awayScore: 3}]->(team2)",
        "MATCH (team1:Team {name: 'Napoli'}), (team2:Team {name: 'Real Madrid'}) CREATE (team1)-[:PLAYED_WITH {date: date('2023-10-03'), homeScore: 2, awayScore: 3}]->(team2)",
        "MATCH (team1:Team {name: 'Braga'}), (team2:Team {name: 'Real Madrid'}) CREATE (team1)-[:PLAYED_WITH {date: date('2023-10-24'), homeScore: 1, awayScore: 2}]->(team2)",
        "MATCH (team1:Team {name: 'Union Berlin'}), (team2:Team {name: 'Napoli'}) CREATE (team1)-[:PLAYED_WITH {date: date('2023-10-24'), homeScore: 0, awayScore: 1}]->(team2)",
        "MATCH (team1:Team {name: 'Napoli'}), (team2:Team {name: 'Union Berlin'}) CREATE (team1)-[:PLAYED_WITH {date: date('2023-11-08'), homeScore: 1, awayScore: 1}]->(team2)",
        "MATCH (team1:Team {name: 'Real Madrid'}), (team2:Team {name: 'Braga'}) CREATE (team1)-[:PLAYED_WITH {date: date('2023-11-08'), homeScore: 3, awayScore: 0}]->(team2)",
        "MATCH (team1:Team {name: 'Real Madrid'}), (team2:Team {name: 'Napoli'}) CREATE (team1)-[:PLAYED_WITH {date: date('2023-11-29'), homeScore: 4, awayScore: 2}]->(team2)",
        "MATCH (team1:Team {name: 'Braga'}), (team2:Team {name: 'Union Berlin'}) CREATE (team1)-[:PLAYED_WITH {date: date('2023-11-29'), homeScore: 1, awayScore: 1}]->(team2)",
        "MATCH (team1:Team {name: 'Napoli'}), (team2:Team {name: 'Braga'}) CREATE (team1)-[:PLAYED_WITH {date: date('2023-12-12'), homeScore: 2, awayScore: 0}]->(team2)",
        "MATCH (team1:Team {name: 'Union Berlin'}), (team2:Team {name: 'Real Madrid'}) CREATE (team1)-[:PLAYED_WITH {date: date('2023-12-12'), homeScore: 2, awayScore: 3}]->(team2)",
        "MATCH (team1:Team {name: 'Real Sociedad'}), (team2:Team {name: 'Inter'}) CREATE (team1)-[:PLAYED_WITH {date: date('2023-09-20'), homeScore: 1, awayScore: 1}]->(team2)",
        "MATCH (team1:Team {name: 'Benfica'}), (team2:Team {name: 'Salzburg'}) CREATE (team1)-[:PLAYED_WITH {date: date('2023-09-20'), homeScore: 0, awayScore: 2}]->(team2)",
        "MATCH (team1:Team {name: 'Salzburg'}), (team2:Team {name: 'Real Sociedad'}) CREATE (team1)-[:PLAYED_WITH {date: date('2023-10-03'), homeScore: 0, awayScore: 2}]->(team2)",
        "MATCH (team1:Team {name: 'Inter'}), (team2:Team {name: 'Benfica'}) CREATE (team1)-[:PLAYED_WITH {date: date('2023-10-03'), homeScore: 1, awayScore: 0}]->(team2)",
        "MATCH (team1:Team {name: 'Inter'}), (team2:Team {name: 'Salzburg'}) CREATE (team1)-[:PLAYED_WITH {date: date('2023-10-24'), homeScore: 2, awayScore: 1}]->(team2)",
        "MATCH (team1:Team {name: 'Benfica'}), (team2:Team {name: 'Real Sociedad'}) CREATE (team1)-[:PLAYED_WITH {date: date('2023-10-24'), homeScore: 0, awayScore: 1}]->(team2)",
        "MATCH (team1:Team {name: 'Real Sociedad'}), (team2:Team {name: 'Benfica'}) CREATE (team1)-[:PLAYED_WITH {date: date('2023-11-08'), homeScore: 3, awayScore: 1}]->(team2)",
        "MATCH (team1:Team {name: 'Salzburg'}), (team2:Team {name: 'Inter'}) CREATE (team1)-[:PLAYED_WITH {date: date('2023-11-08'), homeScore: 0, awayScore: 1}]->(team2)",
        "MATCH (team1:Team {name: 'Benfica'}), (team2:Team {name: 'Inter'}) CREATE (team1)-[:PLAYED_WITH {date: date('2023-11-29'), homeScore: 3, awayScore: 3}]->(team2)",
        "MATCH (team1:Team {name: 'Real Sociedad'}), (team2:Team {name: 'Salzburg'}) CREATE (team1)-[:PLAYED_WITH {date: date('2023-11-29'), homeScore: 0, awayScore: 0}]->(team2)",
        "MATCH (team1:Team {name: 'Inter'}), (team2:Team {name: 'Real Sociedad'}) CREATE (team1)-[:PLAYED_WITH {date: date('2023-12-12'), homeScore: 0, awayScore: 0}]->(team2)",
        "MATCH (team1:Team {name: 'Salzburg'}), (team2:Team {name: 'Benfica'}) CREATE (team1)-[:PLAYED_WITH {date: date('2023-12-12'), homeScore: 1, awayScore: 3}]->(team2)",
        "MATCH (team1:Team {name: 'Feyenoord'}), (team2:Team {name: 'Celtic'}) CREATE (team1)-[:PLAYED_WITH {date: date('2023-09-19'), homeScore: 2, awayScore: 0}]->(team2)",
        "MATCH (team1:Team {name: 'Lazio'}), (team2:Team {name: 'Atletico Madrid'}) CREATE (team1)-[:PLAYED_WITH {date: date('2023-09-19'), homeScore: 1, awayScore: 1}]->(team2)",
        "MATCH (team1:Team {name: 'Atletico Madrid'}), (team2:Team {name: 'Feyenoord'}) CREATE (team1)-[:PLAYED_WITH {date: date('2023-10-04'), homeScore: 3, awayScore: 2}]->(team2)",
        "MATCH (team1:Team {name: 'Celtic'}), (team2:Team {name: 'Lazio'}) CREATE (team1)-[:PLAYED_WITH {date: date('2023-10-04'), homeScore: 1, awayScore: 2}]->(team2)",
        "MATCH (team1:Team {name: 'Feyenoord'}), (team2:Team {name: 'Lazio'}) CREATE (team1)-[:PLAYED_WITH {date: date('2023-10-25'), homeScore: 3, awayScore: 1}]->(team2)",
        "MATCH (team1:Team {name: 'Celtic'}), (team2:Team {name: 'Atletico Madrid'}) CREATE (team1)-[:PLAYED_WITH {date: date('2023-10-25'), homeScore: 2, awayScore: 2}]->(team2)",
        "MATCH (team1:Team {name: 'Atletico Madrid'}), (team2:Team {name: 'Celtic'}) CREATE (team1)-[:PLAYED_WITH {date: date('2023-11-07'), homeScore: 6, awayScore: 0}]->(team2)",
        "MATCH (team1:Team {name: 'Lazio'}), (team2:Team {name: 'Feyenoord'}) CREATE (team1)-[:PLAYED_WITH {date: date('2023-11-07'), homeScore: 1, awayScore: 0}]->(team2)",
        "MATCH (team1:Team {name: 'Lazio'}), (team2:Team {name: 'Celtic'}) CREATE (team1)-[:PLAYED_WITH {date: date('2023-11-28'), homeScore: 2, awayScore: 0}]->(team2)",
        "MATCH (team1:Team {name: 'Feyenoord'}), (team2:Team {name: 'Atletico Madrid'}) CREATE (team1)-[:PLAYED_WITH {date: date('2023-11-28'), homeScore: 1, awayScore: 3}]->(team2)",
        "MATCH (team1:Team {name: 'Atletico Madrid'}), (team2:Team {name: 'Lazio'}) CREATE (team1)-[:PLAYED_WITH {date: date('2023-12-13'), homeScore: 2, awayScore: 0}]->(team2)",
        "MATCH (team1:Team {name: 'Celtic'}), (team2:Team {name: 'Feyenoord'}) CREATE (team1)-[:PLAYED_WITH {date: date('2023-12-13'), homeScore: 2, awayScore: 1}]->(team2)",
        "MATCH (team1:Team {name: 'Milan'}), (team2:Team {name: 'Newcastle United'}) CREATE (team1)-[:PLAYED_WITH {date: date('2023-09-19'), homeScore: 0, awayScore: 0}]->(team2)",
        "MATCH (team1:Team {name: 'PSG'}), (team2:Team {name: 'Dortmund'}) CREATE (team1)-[:PLAYED_WITH {date: date('2023-09-19'), homeScore: 2, awayScore: 0}]->(team2)",
        "MATCH (team1:Team {name: 'Dortmund'}), (team2:Team {name: 'Milan'}) CREATE (team1)-[:PLAYED_WITH {date: date('2023-10-04'), homeScore: 0, awayScore: 0}]->(team2)",
        "MATCH (team1:Team {name: 'Newcastle United'}), (team2:Team {name: 'PSG'}) CREATE (team1)-[:PLAYED_WITH {date: date('2023-10-04'), homeScore: 4, awayScore: 1}]->(team2)",
        "MATCH (team1:Team {name: 'PSG'}), (team2:Team {name: 'Milan'}) CREATE (team1)-[:PLAYED_WITH {date: date('2023-10-25'), homeScore: 3, awayScore: 0}]->(team2)",
        "MATCH (team1:Team {name: 'Newcastle United'}), (team2:Team {name: 'Dortmund'}) CREATE (team1)-[:PLAYED_WITH {date: date('2023-10-25'), homeScore: 0, awayScore: 1}]->(team2)",
        "MATCH (team1:Team {name: 'Dortmund'}), (team2:Team {name: 'Newcastle United'}) CREATE (team1)-[:PLAYED_WITH {date: date('2023-11-07'), homeScore: 2, awayScore: 0}]->(team2)",
        "MATCH (team1:Team {name: 'Milan'}), (team2:Team {name: 'PSG'}) CREATE (team1)-[:PLAYED_WITH {date: date('2023-11-07'), homeScore: 2, awayScore: 1}]->(team2)",
        "MATCH (team1:Team {name: 'PSG'}), (team2:Team {name: 'Newcastle United'}) CREATE (team1)-[:PLAYED_WITH {date: date('2023-11-28'), homeScore: 1, awayScore: 1}]->(team2)",
        "MATCH (team1:Team {name: 'Milan'}), (team2:Team {name: 'Dortmund'}) CREATE (team1)-[:PLAYED_WITH {date: date('2023-11-28'), homeScore: 1, awayScore: 3}]->(team2)",
        "MATCH (team1:Team {name: 'Dortmund'}), (team2:Team {name: 'PSG'}) CREATE (team1)-[:PLAYED_WITH {date: date('2023-12-13'), homeScore: 1, awayScore: 1}]->(team2)",
        "MATCH (team1:Team {name: 'Newcastle United'}), (team2:Team {name: 'Milan'}) CREATE (team1)-[:PLAYED_WITH {date: date('2023-12-13'), homeScore: 1, awayScore: 2}]->(team2)",
        "MATCH (team1:Team {name: 'Young Boys'}), (team2:Team {name: 'Leipzig'}) CREATE (team1)-[:PLAYED_WITH {date: date('2023-09-19'), homeScore: 1, awayScore: 3}]->(team2)",
        "MATCH (team1:Team {name: 'Manchester City'}), (team2:Team {name: 'Red Star FC'}) CREATE (team1)-[:PLAYED_WITH {date: date('2023-09-19'), homeScore: 3, awayScore: 1}]->(team2)",
        "MATCH (team1:Team {name: 'Leipzig'}), (team2:Team {name: 'Manchester City'}) CREATE (team1)-[:PLAYED_WITH {date: date('2023-10-04'), homeScore: 1, awayScore: 3}]->(team2)",
        "MATCH (team1:Team {name: 'Red Star FC'}), (team2:Team {name: 'Young Boys'}) CREATE (team1)-[:PLAYED_WITH {date: date('2023-10-04'), homeScore: 2, awayScore: 2}]->(team2)",
        "MATCH (team1:Team {name: 'Leipzig'}), (team2:Team {name: 'Red Star FC'}) CREATE (team1)-[:PLAYED_WITH {date: date('2023-10-25'), homeScore: 3, awayScore: 1}]->(team2)",
        "MATCH (team1:Team {name: 'Young Boys'}), (team2:Team {name: 'Manchester City'}) CREATE (team1)-[:PLAYED_WITH {date: date('2023-10-25'), homeScore: 1, awayScore: 3}]->(team2)",
        "MATCH (team1:Team {name: 'Manchester City'}), (team2:Team {name: 'Young Boys'}) CREATE (team1)-[:PLAYED_WITH {date: date('2023-11-07'), homeScore: 3, awayScore: 0}]->(team2)",
        "MATCH (team1:Team {name: 'Red Star FC'}), (team2:Team {name: 'Leipzig'}) CREATE (team1)-[:PLAYED_WITH {date: date('2023-11-07'), homeScore: 1, awayScore: 2}]->(team2)",
        "MATCH (team1:Team {name: 'Manchester City'}), (team2:Team {name: 'Leipzig'}) CREATE (team1)-[:PLAYED_WITH {date: date('2023-11-28'), homeScore: 3, awayScore: 2}]->(team2)",
        "MATCH (team1:Team {name: 'Young Boys'}), (team2:Team {name: 'Red Star FC'}) CREATE (team1)-[:PLAYED_WITH {date: date('2023-11-28'), homeScore: 2, awayScore: 0}]->(team2)",
        "MATCH (team1:Team {name: 'Leipzig'}), (team2:Team {name: 'Young Boys'}) CREATE (team1)-[:PLAYED_WITH {date: date('2023-12-13'), homeScore: 2, awayScore: 1}]->(team2)",
        "MATCH (team1:Team {name: 'Red Star FC'}), (team2:Team {name: 'Manchester City'}) CREATE (team1)-[:PLAYED_WITH {date: date('2023-12-13'), homeScore: 2, awayScore: 3}]->(team2)",
        "MATCH (team1:Team {name: 'Barcelona'}), (team2:Team {name: 'Antwerp'}) CREATE (team1)-[:PLAYED_WITH {date: date('2023-09-19'), homeScore: 5, awayScore: 0}]->(team2)",
        "MATCH (team1:Team {name: 'Shakhtar Donetsk'}), (team2:Team {name: 'Porto'}) CREATE (team1)-[:PLAYED_WITH {date: date('2023-09-19'), homeScore: 1, awayScore: 3}]->(team2)",
        "MATCH (team1:Team {name: 'Antwerp'}), (team2:Team {name: 'Shakhtar Donetsk'}) CREATE (team1)-[:PLAYED_WITH {date: date('2023-10-04'), homeScore: 2, awayScore: 3}]->(team2)",
        "MATCH (team1:Team {name: 'Porto'}), (team2:Team {name: 'Barcelona'}) CREATE (team1)-[:PLAYED_WITH {date: date('2023-10-04'), homeScore: 0, awayScore: 1}]->(team2)",
        "MATCH (team1:Team {name: 'Barcelona'}), (team2:Team {name: 'Shakhtar Donetsk'}) CREATE (team1)-[:PLAYED_WITH {date: date('2023-10-25'), homeScore: 2, awayScore: 1}]->(team2)",
        "MATCH (team1:Team {name: 'Antwerp'}), (team2:Team {name: 'Porto'}) CREATE (team1)-[:PLAYED_WITH {date: date('2023-10-25'), homeScore: 1, awayScore: 4}]->(team2)",
        "MATCH (team1:Team {name: 'Shakhtar Donetsk'}), (team2:Team {name: 'Barcelona'}) CREATE (team1)-[:PLAYED_WITH {date: date('2023-11-07'), homeScore: 1, awayScore: 0}]->(team2)",
        "MATCH (team1:Team {name: 'Porto'}), (team2:Team {name: 'Antwerp'}) CREATE (team1)-[:PLAYED_WITH {date: date('2023-11-07'), homeScore: 2, awayScore: 0}]->(team2)",
        "MATCH (team1:Team {name: 'Shakhtar Donetsk'}), (team2:Team {name: 'Antwerp'}) CREATE (team1)-[:PLAYED_WITH {date: date('2023-11-28'), homeScore: 1, awayScore: 0}]->(team2)",
        "MATCH (team1:Team {name: 'Barcelona'}), (team2:Team {name: 'Porto'}) CREATE (team1)-[:PLAYED_WITH {date: date('2023-11-28'), homeScore: 2, awayScore: 1}]->(team2)",
        "MATCH (team1:Team {name: 'Porto'}), (team2:Team {name: 'Shakhtar Donetsk'}) CREATE (team1)-[:PLAYED_WITH {date: date('2023-12-13'), homeScore: 5, awayScore: 3}]->(team2)",
        "MATCH (team1:Team {name: 'Antwerp'}), (team2:Team {name: 'Barcelona'}) CREATE (team1)-[:PLAYED_WITH {date: date('2023-12-13'), homeScore: 3, awayScore: 2}]->(team2)"
    ]

    # Function to execute queries

    def execute_queries(driver):
        count = 0
        with driver.session() as session:
            for query in queries:
                session.run(query)
                count += 1
            return count

    import os

    NEO4J_URI = os.getenv("NEO4J_URI")
    NEO4J_USERNAME = os.getenv("NEO4J_USERNAME")
    NEO4J_PASSWORD = os.getenv("NEO4J_PASSWORD")
    # Connect to Neo4j
    driver = GraphDatabase.driver(
        NEO4J_URI, auth=(NEO4J_USERNAME, NEO4J_PASSWORD))

    # Execute queries
    count = execute_queries(driver)

    # Close the connection
    driver.close()

    print(count)  # 356

    # with GraphDatabase.driver(uri,  auth=(username, password)) as driver:
    #    driver.verify_connectivity()
