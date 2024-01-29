import sys
input = sys.stdin.readline

n, m = map(int, input().split())

word_list = []
sort_freq = {}
sort_len = {}

for i in range(n):
  temp = input().rstrip()
  if len(temp)>= m:
    #단어 명단에 추가
    if temp not in word_list:
      word_list.append(temp)
    #반복 횟수를 업데이트
    if temp not in sort_freq:
      sort_freq[temp] = 1
    else:
      sort_freq[temp] += 1
    #단어 길이를 업데이트
    if temp not in sort_len:
      sort_len[temp] = len(temp)

print(word_list)
print(sort_freq)
print(sort_len)

print("credit")