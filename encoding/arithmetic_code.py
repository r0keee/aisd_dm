import decimal
from math import log2, ceil

decimal.getcontext().prec = 30

input_value = "КОКОТКИНРОДИОНИВАНОВИЧ"

frequencies = {symbol: input_value.count(symbol) for symbol in input_value}

input_len = len(input_value)
probabilities = {symbol: decimal.Decimal(frequencies[symbol]) / input_len for symbol in input_value}

segments = {}
left = decimal.Decimal(0)
for symbol, probabilty in sorted(probabilities.items(), key=lambda x: (-x[1], x[0])):
    right = left + probabilty
    segments[symbol] = (left, right)
    left = right

left = decimal.Decimal(0)
right = decimal.Decimal(1)
for symbol in input_value:
    symbol_left, symbol_right = segments[symbol]
    width = right - left
    right = left + width * symbol_right
    left = left + width * symbol_left
    print(f"{symbol} -> {left} {right}")

print(f"Итоговые границы {left, right}")

factor = 2**(ceil(-log2(decimal.Decimal(right - left))))

print(f"Нормированные границы {decimal.Decimal(factor) * left, decimal.Decimal(factor) * right}")
temp = bin(int(decimal.Decimal(factor) * right))[2:]
if len(temp) == (ceil(-log2(decimal.Decimal(right - left)))) - 1:
    temp = '0' + temp

print(f"Итоговый бинарный код: {temp}")
