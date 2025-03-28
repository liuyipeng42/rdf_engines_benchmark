import time
import sys
import requests
from urllib.parse import urlencode
import json


def gstore_query(file_path, output_path, db_name):

    HEADERS = {"Content-Type": "application/json"}
    payload = {
        "operation": "query",
        "username": "root",
        "password": "123456",
        "db_name": db_name,
        "format": "json",
        "sparql": "",
    }

    queries_file = open(file_path, "r")
    output_file = open(output_path, "w")

    queries = []
    for line in queries_file:
        queries.append(line.strip())
    queries_file.close()

    query_number = 0
    for query in queries:
        count = 0

        payload["sparql"] = query

        start_time = time.time()
        response = requests.post(
            "http://localhost:9000", headers=HEADERS, data=json.dumps(payload)
        )
        end_time = time.time()
        elapsed_time = (end_time - start_time) * 1000

        # json_results = json.loads(response.text)
        # for result in json_results["results"]["bindings"]:
        #     count += 1

        print("{0};{1};{2}".format(query_number, count, elapsed_time))
        output_file.write("{0};{1};{2}\n".format(query_number, count, elapsed_time))
        query_number += 1

    output_file.close()


def query(file_path, output_path, url):

    queries_file = open(file_path, "r")
    output_file = open(output_path, "w")

    queries = []
    for line in queries_file:
        queries.append(line.strip())
    queries_file.close()

    query_number = 0
    for query in queries:
        count = 0
        params = {"query": query}
        encoded_params = urlencode(params)

        start_time = time.time()
        response = requests.get(f"{url}/sparql?{encoded_params}")
        end_time = time.time()
        elapsed_time = (end_time - start_time) * 1000

        # json_results = json.loads(response.text)
        # for result in json_results["results"]["bindings"]:
        #     count += 1

        print("{0};{1};{2}".format(query_number, count, elapsed_time))
        output_file.write("{0};{1};{2}\n".format(query_number, count, elapsed_time))
        query_number += 1

    output_file.close()


query_types = {
    "watdiv": [
        "L1.txt",
        "L2.txt",
        "L3.txt",
        "L4.txt",
        "L5.txt",
        "S1.txt",
        "S2.txt",
        "S3.txt",
        "S4.txt",
        "S5.txt",
        "S6.txt",
        "S7.txt",
        "F1.txt",
        "F2.txt",
        "F3.txt",
        "F4.txt",
        "F5.txt",
        "C1.txt",
        "C2.txt",
        "C3.txt",
    ],
    "wgpb": [
        "J3.txt",
        "J4.txt",
        "P2.txt",
        "P3.txt",
        "P4.txt",
        "S1.txt",
        "S2.txt",
        "S3.txt",
        "S4.txt",
        "T2.txt",
        "T3.txt",
        "T4.txt",
        "TI2.txt",
        "TI3.txt",
        "TI4.txt",
        "Tr1.txt",
        "Tr2.txt",
    ],
    "lubm-100": ["Q1.txt", "Q2.txt", "Q3.txt", "Q4.txt", "Q5.txt", "Q6.txt", "Q7.txt"],
    "yago2": ["y1.q", "y2.q", "y3.q", "y4.q"],
}

endpoints = {
    "rdf-tdaa": "http://localhost:8080/rdftdaa",
    "tentris": "http://localhost:8080",
    "jena-ltj": "http://localhost:3030/jena",
    "mdb": "http://localhost:1234",
    "gstore": "http://localhost:9000",
}

queries = {
    "watdiv": "./datasets/queries/watdiv/",
    "wgpb": "./datasets/queries/wgpb/",
    "swdf": "./datasets/queries/swdf_queries.txt",
    "dbpedia": "./datasets/queries/dbpedia_queries.txt",
    "lubm-100": "./datasets/queries/lubm-100/",
    "yago2": "./datasets/queries/yago2/",
}

dataset = sys.argv[1]
rdf_engine = sys.argv[2]

url = endpoints[rdf_engine]
query_file = queries[dataset]
output_dir = "./results/endpoint/" + dataset + "/" + rdf_engine + "/"


if rdf_engine == "gstore":
    HEADERS = {"Content-Type": "application/json"}
    payload = {
        "operation": "load",
        "username": "root",
        "password": "123456",
        "db_name": dataset,
    }
    response = requests.post(url, headers=HEADERS, data=json.dumps(payload))

    if dataset == "dbpedia" or dataset == "swdf":
        gstore_query(query_file, output_dir + "result.txt", dataset)
    else:
        for t in query_types[dataset]:
            print(t)
            gstore_query(query_file + t, output_dir + t, dataset)

    payload["operation"] = "unload"
    response = requests.post(url, headers=HEADERS, data=json.dumps(payload))
else:
    if dataset == "dbpedia" or dataset == "swdf":
        query(query_file, output_dir + "result.txt", url)
    else:
        for t in query_types[dataset]:
            print(t)
            query(query_file + t, output_dir + t, url)
