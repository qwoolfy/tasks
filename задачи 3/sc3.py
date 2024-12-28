def is_bust(card_values):
    total = sum(card_values)
    return total > 21
card_values = [10, 5, 5] 
result = is_bust(card_values)
print(result)