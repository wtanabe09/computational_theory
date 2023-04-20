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


def get_reachable(delta, current_state):
  # 到達したStateをチェック．記録
  marked_list = [current_state]
  list_i = 0
  while True:
    for mark_state in delta[int(current_state)-1]:
      if mark_state not in marked_list:
        marked_list.append(mark_state)
    if list_i+1 < len(marked_list):
      current_state = int(marked_list[list_i])
      list_i += 1
    else:
      break
  return marked_list

reachable_state = get_reachable(delta, current_state)

word = '111'
for state in range(1, n_state):
  state = str(state)
  if state not in reachable_state:
    continue
  for symbol in word:
    i = int(state)
    j = int(sigma.index(symbol))
    state = delta[i-1][j]

reachable_from_current_state = get_reachable(delta, state)

if any(x in reachable_from_current_state for x in final_state):
    print('Yes')
    sys.exit()
print('No')