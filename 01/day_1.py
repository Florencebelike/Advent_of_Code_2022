f = open("day_1.txt", "r").read().splitlines() #open file-->list

n = [i for i, x in enumerate(f, 1) if x == ''] # find all space
elfs = [f[i:j]for i, j in zip([0]+ n, n)] #list--> sublists
cal = [sum(list(map(int, i[:-1]))) for i in elfs] #list of sum of each

print(cal.index(max(cal)), max(cal)) #max
print(sum(sorted(cal)[-3:])) #top three sum
