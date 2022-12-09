def calc(list, dict):
    score = 0
    if dict[list[1]] != list[0]: #user input != elf (not draw)
        if dict[list[0]] == list[1]: #user input won elf (won)
            score = 6
    else:
        score =3
    return score

basic = ["A", "B", "C"]
check = {"X":"A", "Y":"B", "Z":"C", "A":"Y", "B":"Z", "C":"X"}
# 0-2 case of equal, 3-5 case of player won 
f = open("day_2.txt", "r").read().splitlines()
score = [calc(i.split(), check) for i in f]
base = [basic.index(check[i.split()[1]])+1 for i in f]

totalscore = sum(score) + sum(base)
print(totalscore)

def calc2(a, b):
    elf = {"A": {"X": 3,"Y":1,"Z":2}, "B": {"X":1,"Y":2,"Z":3}, "C": {"X":2,"Y":3,"Z":1}}
    result = {"X":0, "Y":3, "Z":6}
    score = elf[a][b] + result[b]
    return score  

totalscore2 = sum([calc2(i.split()[0], i.split()[1]) for i in f])
print(totalscore2)