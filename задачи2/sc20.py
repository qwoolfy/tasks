def vosr(x):
    for i in range(len(x)-1):
        if x[i] < x[i+1]:
            result = 1
        else:
            result = 0
    if result == 1:
        print('возрастают')
    if result == 0:
        print('уменьшаются')
vosr([10,8,6,4,2,1])
vosr([1,2,4,6,8,10])