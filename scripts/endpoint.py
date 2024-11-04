import time
import sys
import requests
from urllib.parse import urlencode
import json


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

        json_results = json.loads(response.text)
        for result in json_results["results"]["bindings"]:
            count += 1

        print("{0};{1};{2}".format(query_number, count, elapsed_time))
        output_file.write("{0};{1};{2}\n".format(query_number, count, elapsed_time))
        query_number += 1

    output_file.close()


wgpb_quries = [
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
]

watdiv_quries = [
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
]

endpoints = {
    "rdf-tdaa": "http://127.0.0.1:8080/rdftdaa",
    "tentris": "http://127.0.0.1:8080",
    "jena-ltj": "http://localhost:3030/jena",
}

queries = {
    "watdiv": "./datasets/queries/watdiv/",
    "wgpb": "./datasets/queries/wgpb/",
    "dbpedia": "./datasets/queries/dbpedia_queries.txt",
}

dataset = sys.argv[1]
rdf_system = sys.argv[2]

url = endpoints[rdf_system]
query_file = queries[dataset]
output_dir = "./results/endpoint/" + dataset + "/" + rdf_system + "/"

if dataset == "watdiv":
    for t in watdiv_quries:
        print(t)
        query(query_file + t, output_dir + t, url)

if dataset == "wgpb":
    for t in wgpb_quries:
        print(t)
        query(query_file + t, output_dir + t, url)

if dataset == "dbpedia":
    query(query_file, output_dir, url)
