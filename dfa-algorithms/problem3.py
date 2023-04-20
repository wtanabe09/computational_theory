#!/usr/bin/env python3
import sys #パイプでcatから受け取るため

read_data = sys.stdin.read()
data = read_data.split('\n')

n_state = int((data[0].split())[0])
sigma = list(data[1]) # index = [0, 1]

delta = []
for i in range(n_state):
  delta.append(data[2+i].split())

current_state = data[-3]
final_state = data[-2].split()
not_accept_state = []

for state in range(1, n_state + 1):
   if str(state) in final_state:
      continue
   else:
      not_accept_state.append(str(state))

# 状態のマーク(current_stateからデルタチェック)
marked_list = []
marked_list.append(current_state)
list_i = 0
while True:
  for mark_state in delta[int(current_state) - 1]:
    if mark_state not in marked_list:
      marked_list.append(mark_state)

  # marked_list の文字をcurrent_stateにしたい．一個ずつでいい
  if list_i < len(marked_list):
    current_state = int(marked_list[list_i])
    list_i += 1
  else:
    break

if any(x in marked_list for x in not_accept_state):
    print('No')
else:
    print('Yes')