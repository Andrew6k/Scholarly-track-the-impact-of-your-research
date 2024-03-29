import mysql.connector

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="scholar"
)

cursor = conn.cursor()

# table_create_query = """
# CREATE TABLE test (
#     id INT AUTO_INCREMENT PRIMARY KEY,
#     name VARCHAR(255),
#     age INT
# )
# """

table_create = """
CREATE TABLE authors (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255),
    affiliation VARCHAR(255),
    email_domain VARCHAR(255),
    citations INT,
    mail VARCHAR(255) NOT NULL,
    password VARCHAR(255) NOT NULL,
    isadmin BOOLEAN DEFAULT 0
)
"""
cursor.execute(table_create)
conn.commit()

table_create = """
CREATE TABLE publications (
    id INT AUTO_INCREMENT PRIMARY KEY,
    title VARCHAR(255),
    year YEAR,
    conference VARCHAR(255),
    summary VARCHAR(1200),
    citations INT,
    link VARCHAR(255)
)
"""
cursor.execute(table_create)
conn.commit()


table_create = """
CREATE TABLE author_publications (
    author_id INT,
    publication_id INT,
    PRIMARY KEY (author_id, publication_id),
    FOREIGN KEY (author_id) REFERENCES authors(id),
    FOREIGN KEY (publication_id) REFERENCES publications(id)
)
"""
cursor.execute(table_create)
conn.commit()


table_create = """
CREATE TABLE domains (
    id INT AUTO_INCREMENT PRIMARY KEY,
    domain VARCHAR(255)
)
"""

cursor.execute(table_create)
conn.commit()

table_create = """
CREATE TABLE author_domains (
    author_id INT,
    domain_id INT,
    PRIMARY KEY (author_id, domain_id),
    FOREIGN KEY (author_id) REFERENCES authors(id),
    FOREIGN KEY (domain_id) REFERENCES domains(id)
)
"""

cursor.execute(table_create)
conn.commit()

table_create = """
CREATE TABLE conferences (
    nr_reg INT,
    title VARCHAR(255),
    acronym VARCHAR(255),
    year VARCHAR(20),
    rank VARCHAR(20),
    hasData VARCHAR(20),
    primary_for INT,
    comments VARCHAR(20),
    avg_rating VARCHAR(20)
)
"""
cursor.execute(table_create)
conn.commit()

table_create = """
CREATE TABLE journals (
    title VARCHAR(255),
    ISSN VARCHAR(20),
    eISSN VARCHAR(20),
    subdomeniu VARCHAR(255),
    rank VARCHAR(20),
    Loc_in_zona INT,
    year VARCHAR(20)
)
"""
#one more for journals-IF
cursor.execute(table_create)
conn.commit()
# ALTER TABLE conferences ADD COLUMN rank_value INT;
# UPDATE conferences SET rank_value = 
# CASE 
#     WHEN rank = 'A*' THEN 10 
#     WHEN rank = 'A' THEN 9 
#     WHEN rank = 'B' THEN 8 
#     WHEN rank = 'C' THEN 7 
#     WHEN rank = 'D' THEN 6 
#     ELSE '0' 
# END;

table_create = """
CREATE TABLE citations (
    id INT AUTO_INCREMENT PRIMARY KEY,
    title VARCHAR(255),
    link VARCHAR(255),
    FOREIGN KEY (publication_id) REFERENCES publications(id)
)
"""

table_create = """
CREATE TABLE author_citations (
    author_id INT,
    citation_id INT,
    type VARCHAR(20),
    PRIMARY KEY (author_id, citation_id),
    FOREIGN KEY (author_id) REFERENCES authors(id),
    FOREIGN KEY (citation_id) REFERENCES citations(id)
)
"""

cursor.execute(table_create)
conn.commit()


cursor.close()
conn.close()