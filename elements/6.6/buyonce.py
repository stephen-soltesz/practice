#!/usr/bin/python


prices = [310, 315, 275, 295, 260, 270, 290, 230, 255, 250]
results = []
best = 0
b, s = 0, 0


for i, buy in enumerate(prices):
    for j, sell in enumerate(prices[i:]):
        if sell - buy > best:
            best = sell - buy
            b, s = i, i + j


print best
print b, s
print prices[b], prices[s]
