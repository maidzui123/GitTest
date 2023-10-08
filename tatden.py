N = 4
lights = [1,0,1,0]
distance = [2,3,3,4]
active_cost = [3,1,2,3]
dict = {}
total = 0

for i in range(1, N+1):
    arr = []
    for j in range(i, distance[i-1]+1):
        arr.append(j)   
    dict.setdefault(i, arr)
for i in range(1, N+1):
    arr1 = []
    arr2 = []
    if(lights[i-1] == 1):
        for key, value in dict.items():
            if i in value:
                arr1.append(active_cost[key-1])
                arr2.append(key)
                min_cost = min(arr1)
            continue
        for j in range(0, len(arr1)):
                if(arr1[j] == min_cost):
                    for k in range(len(dict.get(arr2[j]))):
                        if(lights[dict.get(arr2[j])[k] - 1] == 1):
                            lights[dict.get(arr2[j])[k] - 1] = 0
                        else:
                            lights[dict.get(arr2[j])[k] - 1] = 1
        print()
        min_cost = min(arr1)
        total += min_cost
                
print(total)

