#!/usr/bin/env python3
import sys #パイプでcatから受け取るため

read_data = sys.stdin.read()
data = read_data.split('\n')

state = int((data[0].split())[0]) # 状態数
sigma = list(data[1]) # index = [0, 1]

delta = [] # i = 0, 1, ..., n_state, j = 0, 1
for i in range(state): # i = 0, 1, 2?
  delta.append(list(data[2+i].split(' ')))

current_state = data[-5]
final_state = data[-4].split(' ')

word = list(data[-1])

for current_char in word:
  i = int(current_state)
  j = int(sigma.index(current_char))
  current_state = delta[i-1][j]

if current_state in final_state:
  sys.stdout.write('yes')
else:
  sys.stdout.write('no')