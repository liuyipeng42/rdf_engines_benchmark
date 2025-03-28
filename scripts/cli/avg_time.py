import sys

watdiv_quries = [
    "L1",
    "L2",
    "L3",
    "L4",
    "L5",
    "S1",
    "S2",
    "S3",
    "S4",
    "S5",
    "S6",
    "S7",
    "F1",
    "F2",
    "F3",
    "F4",
    "F5",
    "C1",
    "C2",
    "C3",
]

wgpb_quries = [
    "J3",
    "J4",
    "P2",
    "P3",
    "P4",
    "S1",
    "S2",
    "S3",
    "S4",
    "T2",
    "T3",
    "T4",
    "TI2",
    "TI3",
    "TI4",
    "Tr1",
    "Tr2",
]

lubm_quries = [
    "Q1",
    "Q2",
    "Q3",
    "Q4",
    "Q5",
    "Q6",
    "Q7",
]

yago2_queries = [
    "y1.q",
    "y2.q",
    "y3.q",
    "y4.q",
]

dataset = sys.argv[1]
rdf_engine = sys.argv[2]

folder = "./results/cli/" + dataset + "/" + rdf_engine + "/"

if dataset == "watdiv":
    if rdf_engine == "rdf-tdaa":
        for i in range(1, 4):
            print("---------------------")
            for t in watdiv_quries:
                time_sum = 0
                with open(folder + str(i) + "/" + t + ".txt") as f:
                    for line in f.readlines():
                        time_sum += eval(line.split(" ")[-2])
                print(round(time_sum / 5, 3))

    if rdf_engine == "rdf-3x":
        for i in range(1, 4):
            print("---------------------")
            for t in watdiv_quries:
                time_sum = 0
                with open(folder + str(i) + "/" + t) as f:
                    for line in f.readlines():
                        time_sum += eval(line)
                print(round(time_sum / 5, 3))

    if rdf_engine == "ring":
        for i in range(1, 4):
            print("---------------------")
            for t in watdiv_quries:
                time_sum = 0
                with open(folder + str(i) + "/" + t) as f:
                    for line in f.readlines():
                        time_sum += eval(line.split(";")[-1])
                print(round(time_sum / 5 / 1000000, 3))


if dataset == "wgpb":
    if rdf_engine == "ring":
        for i in range(1, 4):
            print("---------------------")
            for t in wgpb_quries:
                time_sum = 0
                with open(folder + str(i) + "/" + t) as f:
                    for line in f.readlines():
                        time_sum += eval(line.split(";")[-1])
                print(round(time_sum / 50 / 1000000, 3))

if dataset == "lubm-1000" or dataset == "lubm-100":
    if rdf_engine == "rdf-tdaa":
        for i in range(1, 4):
            print("---------------------")
            for t in lubm_quries:
                time_sum = 0
                with open(folder + str(i) + "/" + t + ".txt") as f:
                    for line in f.readlines():
                        time_sum += eval(line.split(" ")[-2])
                print(round(time_sum / 5, 3))

    if rdf_engine == "rdf-3x":
        for i in range(1, 4):
            print("---------------------")
            for t in lubm_quries:
                time_sum = 0
                with open(folder + str(i) + "/" + t) as f:
                    for line in f.readlines():
                        time_sum += eval(line)
                print(round(time_sum / 5, 3))

    if rdf_engine == "ring":
        for i in range(1, 4):
            print("---------------------")
            for t in lubm_quries:
                time_sum = 0
                with open(folder + str(i) + "/" + t) as f:
                    for line in f.readlines():
                        time_sum += eval(line.split(";")[-1])
                print(round(time_sum / 5 / 1000000, 3))

if dataset == "yago2":
    if rdf_engine == "rdf-tdaa":
        for i in range(1, 4):
            print("---------------------")
            for t in yago2_queries:
                time_sum = 0
                with open(folder + str(i) + "/" + t) as f:
                    for line in f.readlines():
                        time_sum += eval(line.split(" ")[-2])
                print(round(time_sum / 5, 3))

    if rdf_engine == "rdf-3x":
        for i in range(1, 4):
            print("---------------------")
            for t in yago2_queries:
                time_sum = 0
                with open(folder + str(i) + "/" + t) as f:
                    for line in f.readlines():
                        time_sum += eval(line)
                print(round(time_sum / 5, 3))

    if rdf_engine == "ring":
        for i in range(1, 4):
            print("---------------------")
            for t in yago2_queries:
                time_sum = 0
                with open(folder + str(i) + "/" + t) as f:
                    for line in f.readlines():
                        time_sum += eval(line.split(";")[-1])
                print(round(time_sum / 5 / 1000000, 3))
if dataset == "swdf":
    if rdf_engine == "rdf-tdaa":
        for i in range(1, 4):
            time_sum = 0
            with open(folder + str(i) + ".txt") as f:
                for line in f.readlines():
                    if line.startswith("query cost"):
                        time_sum += eval(line.split(" ")[-2])
            print(round(time_sum / 14740, 3))

    if rdf_engine == "ring":
        for i in range(1, 4):
            time_sum = 0
            with open(folder + str(i) + ".txt") as f:
                for line in f.readlines():
                    time_sum += eval(line.split(";")[-1])
            print(round(time_sum / 14740 / 1000000, 3))

    if rdf_engine == "rdf-3x":
        for i in range(1, 4):
            time_sum = 0
            with open(folder + str(i) + ".txt") as f:
                for line in f.readlines():
                    time_sum += eval(line)
            print(round(time_sum / 14740, 3))

