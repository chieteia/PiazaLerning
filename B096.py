# 方針:爆破後のMapを作成して爆破されたマスを数える

ans = 0
#爆発後のmapの初期化
map = [[0 for j in range(1000)] for i in range(1000)]
#H,Wの取得
input_line = input().split()
height = int(input_line[0])
width = int(input_line[1])
#爆発後のmap作成
for y in range(height):
    input_line = input()
    for x in range(width):
        if '#' == input_line[x]:
            for i in range(height):
                map[i][x] = 1
            for j in range(width):
                map[y][j] = 1
#爆破されたマスを数える
for l in map:
    ans += l.count(1)
#答え
print(ans)