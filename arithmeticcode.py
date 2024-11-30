from decimal import *

def arithmeticcode(inputs, probabilities):
    left = Decimal(0.0)
    right = Decimal(1.0)

    getcontext().prec = 35

    for char in inputs:
        interval = right - left
        char_left, char_right = map(Decimal, probabilities[char])

        right = left + interval * char_right
        left = left + interval * char_left
        
        print(f"|{char} | {left} | {right} |")

    return left, right

def calcprob(s):
    char_cnt = {}
    for char in s:
        char_cnt[char] = char_cnt.get(char, 0) + 1

    numofchsr = sum(char_cnt.values())
    probabilities = {}
    previossum = 0.0

    for char in sorted(char_cnt.keys()):
        char_prob = char_cnt[char] / numofchsr
        probabilities[char] = (previossum, previossum + char_prob)
        previossum += char_prob

    return probabilities 

s = "наумовавладавладимировна"
print(f"|    | Левая граница                                                   | Правая граница                                                |")
print(f"|    | 0                                                                              | 1                                                                              |")
probabilities = calcprob(s)

left, right = arithmeticcode(s, probabilities)

q = 75
print("p =",round(min(left*2**q,right*2**q)))
p = round(min(left * 2**q, right * 2**q))
code = bin(p)[2:] 
print("Бинарное представление:", code)
print("Колличество битов:",len(code))




