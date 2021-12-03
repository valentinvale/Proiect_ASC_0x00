import sys
parola, i_name, o_name = sys.argv[1:4]

fout = open(o_name, "wb")
with open(i_name, "r") as fin:
    while True:
        chunk = fin.read(len(parola))
        for i in range(len(chunk)):
            aux = chr(ord(parola[i]) ^ ord(chunk[i]))
            aux1 = aux.encode('ascii')
            fout.write(aux1)

        if len(chunk) < len(parola):
            break

fout.close()
