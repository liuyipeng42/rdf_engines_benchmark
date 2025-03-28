import requests
import json

BASE_URL = "http://127.0.0.1:9000"
HEADERS = {'Content-Type': 'application/json'}

def load_database(username, password, db_name):
    payload = {
        "operation": "load",
        "username": username,
        "password": password,
        "db_name": db_name
    }
    response = requests.post(BASE_URL, headers=HEADERS, data=json.dumps(payload))
    return response.text

def query_database(username, password, db_name, sparql_query):
    payload = {
        "operation": "query",
        "username": username,
        "password": password,
        "db_name": db_name,
        "format": "json",
        "sparql": sparql_query
    }
    response = requests.post(BASE_URL, headers=HEADERS, data=json.dumps(payload))
    return response.text

if __name__ == "__main__":
    username = "root"
    password = "123456"
    db_name = "watdiv"

    load_response = load_database(username, password, db_name)
    print("Load Response:", load_response)

    sparql_query = """
        SELECT ?v0 ?v4 ?v6 ?v7 WHERE {
            ?v0 <http://schema.org/caption> ?v1 .
            ?v0 <http://schema.org/text> ?v2 .
            ?v0 <http://schema.org/contentRating> ?v3 .
            ?v0 <http://purl.org/stuff/rev#hasReview> ?v4 .
            ?v4 <http://purl.org/stuff/rev#title> ?v5 .
            ?v4 <http://purl.org/stuff/rev#reviewer> ?v6 .
            ?v7 <http://schema.org/actor> ?v6 .
            ?v7 <http://schema.org/language> ?v8 .
        }
    """
    query_response = query_database(username, password, db_name, sparql_query)
    print("Query Response:", query_response)

    query_response = query_database(username, password, db_name, sparql_query)
    print("Query Response:", query_response)
