
n, k = map(int, input().split())
hards = list(map(int, input().split()))
robots = [-1] * (2*n)
step = 1


def rotate_belt_robot():
    hard_last = hards[2*n-1]
    robot_last = robots[2*n-1]
    for i in range(2*n-1, 0, -1):
        hards[i] = hards[i-1]
        robots[i] = robots[i-1]
    hards[0] = hard_last
    robots[0] = robot_last
    if robots[n-1] >= 0:
        robots[n-1] = -1


def move_robots():
    tmp_robots = []
    for idx, val in enumerate(robots):
        if val >= 0:
            tmp_robots.append((idx, val))
    tmp_robots.sort(key=lambda x: -x[1])
    for idx, val in tmp_robots:
        next_idx = (idx+1) % (2*n)
        if robots[next_idx] < 0 and hards[next_idx] > 0:
            robots[next_idx] = val
            robots[idx] = -1
            hards[next_idx] -= 1
            if next_idx == n-1:
                robots[next_idx] = -1


def add_robot():
    if hards[0] > 0:
        robots[0] = 0
        hards[0] -= 1


def check_hards():
    return hards.count(0)


def update_robots():
    for i, v in enumerate(robots):
        if v >= 0:
            robots[i] += 1


while True:
    # 1. 벨트와 로봇 회전
    rotate_belt_robot()
    # 2. 로봇 이동
    move_robots()
    # 3. 로봇 올리기
    if step == 31:
        pass
    add_robot()
    # 4. 내구도 확인
    cnt = check_hards()
    if cnt >= k:
        break
    update_robots()
    step += 1

print(step)