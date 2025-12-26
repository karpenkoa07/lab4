from itertools import combinations

START_SCORE = 10
CAP = 9

items = [
    ('r',3,25,25),
    ('p',2,15,15),
    ('a',2,15,15),
    ('m',2,20,20),
    ('i',1,5,5),
    ('k',1,15,15),
    ('x',3,20,20),
    ('t',1,25,25),
    ('f',1,15,15),
    ('d',1,10,10),
    ('s',2,20,20),
    ('c',2,20,20)

]

best_combo = None
best_score = float("-inf")

for i in range(len(items)):
    for combo in combinations(items, i):
        size = sum(item[1] for item in combo)
        if size > CAP:
            continue


        points = START_SCORE
        for name, weight, bonus, penalty in items:
            if any(item[0] == name for item in combo):
                points += bonus
            else:
                points -= penalty

        if points > best_score:
            best_score = points
            best_combo = combo


cells = []
for name, size, b, p in best_combo:
    cells.extend([name] * size)

while len(cells) < CAP:
    cells.append(' ')

for i in range(3):
    print(cells[i * 3:(i + 1) * 3])