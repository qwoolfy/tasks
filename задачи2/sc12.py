def double(st):
    for i in range(len(st)):
        if st[i].lower() == st[i+1].lower():return True
    return 0
print(double("мировоззрение"))