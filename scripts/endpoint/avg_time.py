import sys

watdiv_queries = [
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

wgpb_queries = [
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

lubm_queries = [
    "Q1.txt",
    "Q2.txt",
    "Q3.txt",
    "Q4.txt",
    "Q5.txt",
    "Q6.txt",
    "Q7.txt",
]

yago2_queries = [
    "y1.q",
    "y2.q",
    "y3.q",
    "y4.q",
]

dataset = sys.argv[1]
rdf_engine = sys.argv[2]

folder = "./results/endpoint/" + dataset + "/" + rdf_engine + "/"


if dataset != "dbpedia":
    if dataset != "swdf":
        query_cnt = 0
        query_types = []
        if dataset.startswith("watdiv"):
            query_cnt = 5
            query_types = watdiv_queries
        if dataset == "lubm-1000" or dataset == "lubm-100":
            query_cnt = 5
            query_types = lubm_queries
        if dataset == "yago2":
            query_cnt = 5
            query_types = yago2_queries
        if dataset == "wgpb":
            query_cnt = 50
            query_types = wgpb_queries
        for i in range(1, 4):
            print("---------------------")
            for t in query_types:
                time_sum = 0
                with open(folder + str(i) + "/" + t) as f:
                    for line in f.readlines():
                        time_sum += eval(line.split(";")[-1])
                print(round(time_sum / query_cnt, 3))
    else:
        for i in range(1, 4):
            time_sum = 0
            time_outs = 0
            cnt = 1
            with open(folder + str(i) + ".txt") as f:
                for line in f.readlines():
                    time = eval(line.split(";")[-1])
                    if time < 20:
                        time_sum += time
                    else:
                        time_outs += 1
                        # print(cnt)
                    cnt += 1
            print(round(time_sum / 14740, 3), time_outs)
else:
    for i in range(1, 4):
        time_sum = 0
        time_outs = 0
        with open(folder + str(i) + ".txt") as f:
            for line in f.readlines():
                time = eval(line.split(";")[-1])
                if time < 5000:
                    time_sum += time
                else:
                    time_outs += 1
        print(round(time_sum / 554, 3), time_outs)
