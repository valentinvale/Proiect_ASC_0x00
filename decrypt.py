import sys
i_name, parola, o_name = sys.argv[1:4]

fout = open(o_name, "w")
with open(i_name, "rb") as fin:
    while True:
        chunk = fin.read(len(parola))
        for i in range(len(chunk)):
            fout.write(chr(ord(parola[i]) ^ chunk[i]))

        if len(chunk) < len(parola):
            break

fout.close()

