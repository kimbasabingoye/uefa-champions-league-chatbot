from neo4j import GraphDatabase
import re
import csv

# Function to insert data from CSV into Neo4j


def insert_data_from_csv(driver, csv_file_path):
    with open(csv_file_path, 'r', newline='') as csvfile:
        csv_reader = csv.DictReader(csvfile)
        for row in csv_reader:
            # Cypher query to create Player nodes
            cypher_query = (
                "CREATE (:Player {"
                "name: $name, "
                "position: $position, "
                "number: toInteger($number), "
                "age: toInteger($age), "
                "goals: toInteger($goals)"
                "})"
            )
            with driver.session() as session:
                session.run(cypher_query, row)


def insert_players():
    # Specify the file path
    input_file_path = 'players_data.txt'
    output_file_path = 'players_data.csv'

    count = 0
    # Open the file in read mode
    with open(input_file_path, 'r') as input_file, open(output_file_path, 'w', newline='') as output_file:
        # Read each line in the input_file
        for line in input_file:
            # Cypher query
            # cypher_query = "CREATE (:Player {name: 'Aaron Ramsdale', position: 'Goalkeeper', number: 1, age: 25, goals: 0})"
            cypher_query = line

            # Regular expression pattern
            pattern = r"name:\s*'(?P<name>.*?)',\s*position:\s*'(?P<position>.*?)',\s*number:\s*(?P<number>\d+),\s*age:\s*(?P<age>\d+),\s*goals:\s*(?P<goals>\d+)"

            # Create a CSV writer
            csv_writer = csv.writer(output_file)

            # Write headers to the CSV file
            csv_writer.writerow(["name", "position", "number", "age", "goals"])

            # Extract information using regular expression
            match = re.search(pattern, cypher_query)

            if match:
                name = match.group("name")
                position = match.group("position")
                number = match.group("number")
                age = match.group("age")
                goals = match.group("goals")

                csv_writer.writerow([name, position, number, age, goals])

                """
                print("Name:", name)
                print("Position:", position)
                print("Number:", number)
                print("Age:", age)
                print("Goals:", goals)"""
                count += 1
            else:
                print("No match found.")
                print(line)

    print(count)  # 689

    import os

    NEO4J_URI = os.getenv("NEO4J_URI")
    NEO4J_USERNAME = os.getenv("NEO4J_USERNAME")
    NEO4J_PASSWORD = os.getenv("NEO4J_PASSWORD")
    # Connect to Neo4j
    driver = GraphDatabase.driver(
        NEO4J_URI, auth=(NEO4J_USERNAME, NEO4J_PASSWORD))

    # Insert data from CSV into Neo4j
    insert_data_from_csv(driver, output_file_path)

    # Close the connection
    driver.close()
