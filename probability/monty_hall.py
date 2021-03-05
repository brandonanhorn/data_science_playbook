import random

#### WIP

number_of_doors = 100
doors_to_open = 90
doors = list(range(number_of_doors))

prize_door = random.choice(doors)

my_door = 3

possible_doors = [d for d in doors if d not in (my_door, prize_door)]

opened_doors = random.sample(possible_doors, k=doors_to_open)

doors_left = [d for d in doors if d not in opened_doors]

switch = True

if switch:
    switchable = [d for d in doors_left if d != my_door]
    my_door = random.choice(switchable)

my_door == prize_door

#### functionizing

def monty_hall(my_door, switch=True, number_of_doors=100, doors_to_open=98):
    doors = list(range(number_of_doors))
    prize_door = random.choice(doors)
    possible_doors = [d for d in doors if d not in (my_door, prize_door)]
    opened_doors = random.sample(possible_doors, k=doors_to_open)
    doors_left = [d for d in doors if d not in opened_doors]
    if switch:
        switchable = [d for d in doors_left if d != my_door]
        my_door = random.choice(switchable)
    return my_door == prize_door

N = 10000
sims = [monty_hall(14, switch=True) for _ in range(N)]
sum(sims) / N

N = 10000
sims = []
for _ in range(N):
    my_door = random.choice([0, 1, 2])
    sim =  monty_hall(my_door, switch=True, number_of_doors=3, doors_to_open=1)
    sims.append(sim)

sum(sims) / N
