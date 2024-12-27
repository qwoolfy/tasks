def enemy(x):
    result = []
    a = ['Ronaldo', 'Barca', "Liverpool"]
    for i in x:
        if i not in a:
            result.append(i)
    return (result)
print(enemy(['Mbappe', 'Ronaldo', "realmadrid", 'Valverde', "Messi", "Barca", "Liverpool"]))