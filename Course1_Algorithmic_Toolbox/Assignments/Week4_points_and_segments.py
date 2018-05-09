# Uses python3

def fast_count_segments(starts, ends, points):
    cnt = [0] * len(points)
    #write your code here
    all_points = []
    for point in starts:
        all_points.append({'type': 0, 'value': point})
    for point in ends:
        all_points.append({'type': 2, 'value': point})
    for index, point in enumerate(points):
        all_points.append({'type': 1, 'value': point, 'index': index})
    all_points_sorted = sorted(all_points, key = lambda point: (point['value'], point['type']))
    p = 0
    p = 0
    for point in all_points_sorted:
        if point['type'] == 0:
            p += 1
        if point['type'] == 2:
            p -= 1
        if point['type'] == 1:
            cnt[point['index']] = p
    return cnt

def naive_count_segments(starts, ends, points):
    cnt = [0] * len(points)
    for i in range(len(points)):
        for j in range(len(starts)):
            if starts[j] <= points[i] <= ends[j]:
                cnt[i] += 1
    return cnt

s, p = list(map(int, input().split()))
starts = s*[0]
ends = s*[0]
for i in range(s):
    starts[i], ends[i] = list(map(int, input().split()))
points = list(map(int, input().split()))
#use fast_count_segments
cnt = fast_count_segments(starts, ends, points)
for x in cnt:
    print(x, end=' ')
