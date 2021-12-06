

input = open("input.txt", "r").read()
output = open("output", "rb").read()

for i in range(100):
    print(str(chr(ord(input[i]) ^ output[i])), end='')


