from itertools import combinations

START_SCORE = 10
CAP = 9

items = [
    ('r (rifle)',3,25,25),
    ('p',2,15,15),
    ('a (ammo)',2,15,15),
    ('m (medkit)',2,20,20),
    ('i (inhaler)',1,5,5),
    ('k (knife)',1,15,15),
    ('x (axe)',3,20,20),
    ('t (talisman)',1,25,25),
    ('f (flask)',1,15,15),
    ('d (antidot)',1,10,10),
    ('s (supplies)',2,20,20),
    ('c (crossbow)',2,20,20)

]


def combinate(combo):
    points = START_SCORE
    for name, size, bonus, penalty in items:
        if name in combo:
            points += bonus
        else:
            points -= penalty
    return points


def total_size(combo):
    size_sum = 0
    for name, size, bonus, penalty in items:
        if name in combo:
            size_sum += size
    return size_sum


best_combo = None
best_score = float("-inf")
item_names = [item[0] for item in items]


for i in range(len(items)):
    for combo in combinations(item_names, i):
        if total_size(combo) > CAP:
            continue
        score = combinate(combo)

        if score > 0 and score > best_score:
            best_score = score
            best_combo = combo


print("The best combination is:")
for item in best_combo:
    print([item])
print("Best score:", best_score)
print("Amount of things:", len(best_combo))
print(total_size(best_combo), "/", CAP, "slots filled")