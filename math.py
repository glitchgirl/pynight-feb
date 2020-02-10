x = 2 ** (1 / 2.0)
y = 1 + (1 / 3.0)
x_diff = x - y
y_diff = 0

with open("division.txt") as input:
    sum = 0
    for line in input.readlines():
        divison = line.split('/')
        sum = sum + int(divison[0])//int(divison[1])
    print(sum)

with open("sum.txt") as input:
    sum = 0
    for line in input.readlines():
        hold = line.split("/n")
        sum = int(hold[0]) + sum
    print("sum")
    print(sum)  

with open("numbers.txt") as input:
    mean = 0
    count = 0
    hold = 0
    for line in input.readlines():
        divison = line.split("/n")
        count = count + 1
        hold = hold + int(divison[0])
    mean = int(hold)/count 
    #print("mean")
    #print(mean)

with open("sort.txt") as input:
    holder = []
    for line in input.readlines():
        holder.append(int(line))
    holder.sort()
    #print(holder[99])

with open("temp.txt") as input:
    for item in input.readlines():
        data = item.split(' ')
        hits = data [-4]
        error = data[-2]
        # if(error == "404"):
        #    print(" ")

with open("skip.txt") as input:
    array = []
    i = 0
    for line in input.readlines():
        array.append(int(line))
    array.sort()
    i = array.__len__() - 1
    while i > 0:
        if((array[i] - array[i-1])> 1):
            print(array[i-1])
        i -= 1

import numpy as np
def P1_win_prob_weighted_coin_game(num_games, prob_heads=.5): 
  player_one_wins = 0 
  for n in range(0,num_games): 
    num_flips = 0 
    win = 0
    while win == 0: 
      turn = np.random.uniform(0,1) 
      num_flips += 1 
      if turn <= prob_heads: 
        if num_flips % 2 != 0: 
          player_one_wins += 1 
        win += 1 
  return float(player_one_wins)/float(num_games)