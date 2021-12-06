s = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789'
inputFile = "output"
outputFile = "input_recuperat.txt"


for j in range(1, 16):
    key = 'a' * j
    parola_finala = [x for x in range(j)]
    with open(outputFile, "w", encoding="UTF-8") as fout:
        for i in range(0, j):
            Max = 0
            for char in s:
                with open(inputFile, "rb") as fin:
                    key = key[:i] + char + key[i+1:]
                    contor = 0
                    fout.write(f"   Codare cu caracterul {i} din cheie: {key}\n\n")
                    nr_voc = 0
                    content = bytearray(fin.read()).decode("UTF-8")
                    #fout.write(str(ord("ù")))
                    for c in content:
                        #fout.write(str(c)+"\n")
                        if contor == i:
                            temp = chr(ord(c) ^ ord(key[contor]))
                            if temp in "aei":
                                nr_voc += 1

                        contor += 1
                        if (contor == len(key)):
                            contor = 0
                    fout.write(str(nr_voc))
                    if nr_voc > Max:
                        Max = nr_voc
                        parola_finala[i] = char
    print()
    print()
    print(''.join(parola_finala))


