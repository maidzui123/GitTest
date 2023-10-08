 for j in range(0, len(arr1)):
                if(arr1[j] == min_cost):
                    for k in range(len(dict.get(arr2[j]))):
                        if(lights[dict.get(arr2[j])[k] - 1] == 1):
                            lights[dict.get(arr2[j])[k] - 1] = 0
                        else:
                            lights[dict.get(arr2[j])[k] - 1] = 1
        print(lights)
        min_cost = min(arr1)
        total += min_cost
                
print(total)