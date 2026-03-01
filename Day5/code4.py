list = [11, 5, 4, 2]
target = 50
def twonum(list,target):
    for i in range (len(list)):
        for j in range (i+1, len(list)):
            if (list[i]+list[j] == target):
                return [i,j]
            
    return "invalid"

print(twonum(list, target))