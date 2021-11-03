# about pandas

## iterrows와 iteritems
DataFrame형태의 data가 있을 때, 그 data의 행 또는 열을 반복하여 접근하고 싶을 때 사용할 수 있는 method입니다.
iterrows는 row에 대해 반복하고, iteritems는 column에 대해 반복합니다.

df라는 이름의 다음과 같은 DataFrame이 있을 때, df.iterrows()와 df.iteritems() 예시 코드입니다.

|  | a | b | c | d 
--- | --- | --- | --- | ---
0  | 1 | 2 | 3 | 4
1  | 5 | 6 | 7 | 8
2  | 9 | 10 | 11 | 12

```Python
for idx, row in df.iterrows():
  print(idx, end = ' ')
```
결과 -> 0 1 2

```Python
for idx, column in df.iteritems():
  print(idx, end = ' ')
```
결과 -> a b c d
