with open("./queries.txt", "r") as f:
    c = 1
    for sparql in f.readlines():
        with open("./swdf/" + str(c), "w") as f_w:
            f_w.write(sparql)
        c += 1
        print(c)
