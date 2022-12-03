f = open("day_1.txt", "r").read().splitlines()

n = [i for i, x in enumerate(f, 1) if x == '']
elfs = [f[i:j]for i, j in zip([0]+ n, n)]
cal = [sum(list(map(int, i[:-1]))) for i in elfs]

#max
print(cal.index(max(cal)), max(cal))

#top three sum
print(sum(sorted(cal)[-3:]))

        