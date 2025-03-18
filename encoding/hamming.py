binary = "0110110000110011100110110011010111010011011111001100011100110111100"

l = len(binary)
controls = 0
while (2**controls < l + controls + 1):
    controls += 1

result = []
j, k, res_len = 0, 0, l + controls
for i in range(1, res_len + 1):
    if i == 2**k:
        result.append(0)
        k += 1
    else:
        result.append(int(binary[j]))
        j += 1

for i in range(controls):
    pos = 2**i
    tmp = 0
    for j in range(1, res_len + 1):
        if j & pos and j != pos:
            tmp ^= result[j - 1]
    result[pos - 1] = tmp

print(f"Последовательность битов с помощью кода Хемминга {result}")
print(f"Rate {len(binary)/len(result)}")
