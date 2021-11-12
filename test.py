'''
a_list = [1, 14, 24, 43, 9, 10]
b_list = [42, 9, 23, 6, 5, 14]

print(set(a_list) & set(b_list))

# set을 쓰면 동일한게 나옴 {9, 14}
'''

'''
te = 'asdaaaaasrkaaalsd'

print(te)

for i in te:
    if i == 'a':
        te = te.replace(i, '', 1)

print(te)
# 문자열 내 a 제거
'''

'''
te = 'sajhd-234!78..$_*#9'
print(te)
for w in te:
    if w.isalnum() or w == '-' or w == '_' or w == '.':
        pass
    else:
        te = te.replace(w, '', 1)

print(te)

#알파벳 숫자 - _ . 이 아니면 제거
'''
'''
iasd = 'sadjha'
print(len(iasd))
if len(iasd) >= 5:
    iasd = iasd[:4]

print(iasd)
print(len(iasd))
while len(iasd) < 8:
    iasd += iasd[-1]

print(iasd, len(iasd))

#뒤에 붙이기
'''

'''
n = 4
matrix = [[0 for c in range(n)] for r in range(n)]
print(matrix)
#n x n 행렬
print(len(matrix))
print(matrix[0][0])
'''
'''
r=1
bas = [1,1,1,1]
while r < len(bas):
    if bas[r-1] == bas[r]:
        bas = bas[:r-1] + bas[r+1:]
        r=0
    r += 1

print(bas)
#뿌요뿌요 겹치는값 지우기
'''

'''
b = [[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]]

print(b[3][3])
b[3][3] = 0
print(b)
'''
a = 162 % 192
print(a)
