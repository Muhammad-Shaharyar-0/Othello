import copy

flag_top = flag_down = flag_left = flag_right = flag_right_top = flag_left_top = flag_right_down = flag_left_down = 0


def pass_by_value(f):
    def _f(*args, **kwargs):
        args_copied = copy.deepcopy(args)
        kwargs_copied = copy.deepcopy(kwargs)
        return f(*args_copied, **kwargs_copied)

    return _f


def default_board(grid):
    for p in range(8):
        for q in range(8):
            grid[p][q] == '.'
    grid[3][3] = 'o'
    grid[3][4] = 'x'
    grid[4][3] = 'x'
    grid[4][4] = 'o'


def is_empty(arr):
    num = 0
    for i in range(8):
        for j in range(8):
            if arr[i][j] == '.':
                num += 1
    if num > 0:
        return True
    else:
        return False


def print_board(black_balls, white_balls):
    print(f"- 0 1 2 3 4 5 6 7")
    i = 0
    for item in range(len(board)):
        print(i, *board[item])
        i += 1
    print()
    print(f'x is: {black_balls}   o is: {white_balls}')
    print()


def take_input():
    x = (input(f'Enter row# for your move: '))
    while x < '0' or x > '9':
        x = (input(f'Enter row# for your move: '))
    x=int(x)
    y = (input(f'Enter col# for your move:'))
    while y < '0' or y > r'9':
        y = (input(f'Enter col# for your move: '))
    y = int(y)
    while out_of_bound(x_cord=x, y_cord=y) == False or board[x][y] != '.':
        if out_of_bound(x_cord=x, y_cord=y) == False:
            print('Invalid Input, Out Of Bound Error')
        else:
            print('Invalid Input, there is already a tile in this box')
        print('Re-Enter Co-ordinates')
        x = int(input(f'Enter row# for your move: '))
        y = int(input(f'Enter col# for your move: '))
    return x, y


def compute_score(grid):
    no_of_black_balls = 0
    no_of_white_balls = 0
    for i in range(len(grid)):
        for j in range(8):
            if grid[i][j] == 'x':
                no_of_black_balls += 1
            elif grid[i][j] == 'o':
                no_of_white_balls += 1
    return no_of_black_balls, no_of_white_balls


def out_of_bound(x_cord, y_cord):
    if x_cord < 0 or x_cord > 7 or y_cord < 0 or y_cord > 7:
        return False
    else:
        return True


def is_valid_move(grid, x_cord, y_cord, tile):
    global flag_top
    global flag_down
    global flag_left
    global flag_right
    global flag_right_top
    global flag_right_down
    global flag_left_top
    global flag_left_down
    if tile == 'x':
        tile2 = 'o'
    else:
        tile2 = 'x'

    if x_cord - 1 < 0:
        flag_top = 0
        flag_right_top = 0
        flag_left_top = 0
    else:
        flag_top = top_tile_check(arr=grid, x_axis=x_cord - 1, y_axis=y_cord, t=tile)
    if x_cord + 1 > 7:
        flag_down = 0
        flag_right_down = 0
        flag_left_down = 0
    else:
        flag_down = down_tile_check(arr=grid, x_axis=x_cord + 1, y_axis=y_cord, t=tile)
    if y_cord - 1 < 0:
        flag_left = 0
        flag_left_top = 0
        flag_left_down = 0
    else:
        flag_left = left_tile_check(arr=grid, x_axis=x_cord, y_axis=y_cord - 1, t=tile)
    if y_cord + 1 > 7:
        flag_right = 0
        flag_right_top = 0
        flag_right_down = 0
    else:
        flag_right = right_tile_check(arr=grid, x_axis=x_cord, y_axis=y_cord + 1, t=tile)
    if x_cord - 1 >= 0 and y_cord + 1 > 7:
        flag_right_top = 0
    elif x_cord - 1 >= 0 and y_cord + 1 <= 7:
        flag_right_top = right_top_check(arr=grid, x_axis=x_cord - 1, y_axis=y_cord + 1, t=tile)
    if x_cord - 1 >= 0 > y_cord - 1:
        flag_left_top = 0
    elif x_cord - 1 >= 0 <= y_cord - 1:
        flag_left_top = left_top_check(arr=grid, x_axis=x_cord - 1, y_axis=y_cord - 1, t=tile)
    if x_cord + 1 <= 7 < y_cord + 1:
        flag_right_down = 0
    elif x_cord + 1 <= 7 >= y_cord + 1:
        flag_right_down = right_down_check(arr=grid, x_axis=x_cord + 1, y_axis=y_cord + 1, t=tile)
    if x_cord + 1 <= 7 and y_cord - 1 < 0:
        flag_left_down = 0
    elif x_cord + 1 <= 7 and y_cord - 1 >= 0:
        flag_left_down = left_down_check(arr=grid, x_axis=x_cord + 1, y_axis=y_cord - 1, t=tile)
    if y_cord - 1 >= 0 > x_cord - 1:
        flag_left_top = 0
    elif y_cord - 1 >= 0 <= x_cord - 1:
        flag_left_top = left_top_check(arr=grid, x_axis=x_cord - 1, y_axis=y_cord - 1, t=tile)
    if y_cord - 1 >= 0 and x_cord + 1 > 7:
        flag_left_down = 0
    elif y_cord - 1 >= 0 and x_cord + 1 <= 7:
        flag_left_down = left_down_check(arr=grid, x_axis=x_cord + 1, y_axis=y_cord - 1, t=tile)
    if y_cord + 1 <= 7 and x_cord - 1 < 0:
        flag_right_top = 0
    elif y_cord + 1 <= 7 and x_cord - 1 >= 0:
        flag_right_top = right_top_check(arr=grid, x_axis=x_cord - 1, y_axis=y_cord + 1, t=tile)
    if y_cord + 1 <= 7 < x_cord + 1:
        flag_right_down = 0
    elif y_cord + 1 <= 7 >= x_cord + 1:
        flag_right_down = right_down_check(arr=grid, x_axis=x_cord + 1, y_axis=y_cord + 1, t=tile)

    if flag_top in (0, 1) and flag_down in (0, 1) and flag_left in (0, 1) and flag_right in (
            0, 1) and flag_right_top in (0, 1) and flag_right_down in (0, 1) and flag_left_top in (
            0, 1) and flag_left_down in (0, 1):
        return False
    else:
        return True


def top_tile_check(arr, x_axis, y_axis, t):
    if arr[x_axis][y_axis] == '.':
        return 0  # null space
    elif arr[x_axis][y_axis] == t:
        return 1  # same tile
    else:
        temp = 0
        i = x_axis - 1
        if i >= 0:
            if t == 'x':
                other_tile = 'o'
            else:
                other_tile = 'x'
            for item in range(i, -1, -1):
                if arr[item][y_axis] == t:
                    temp = 2
                if arr[item][y_axis] == '.':
                    break
            if temp == 2:
                return 2
            else:
                return 0
        else:
            return 0


def down_tile_check(arr, x_axis, y_axis, t):
    if arr[x_axis][y_axis] == '.':
        return 0  # null space
    elif arr[x_axis][y_axis] == t:
        return 1  # same tile
    else:
        temp = 0
        i = x_axis + 1
        if i <= 7:
            if t == 'x':
                other_tile = 'o'
            else:
                other_tile = 'x'
            for item in range(i, 8, 1):
                if arr[item][y_axis] == t:
                    temp = 2
                if arr[item][y_axis] == '.':
                    break
            if temp == 2:
                return 2
            else:
                return 0
        else:
            return 0


def left_tile_check(arr, x_axis, y_axis, t):
    if arr[x_axis][y_axis] == '.':
        return 0  # null space
    elif arr[x_axis][y_axis] == t:
        return 1  # same tile
    else:
        temp = 0
        j = y_axis - 1
        if j >= 0:
            if t == 'x':
                other_tile = 'o'
            else:
                other_tile = 'x'
            for item in range(j, -1, -1):
                if arr[x_axis][item] == t:
                    temp = 2
                if arr[x_axis][item] == '.':
                    break
            if temp == 2:
                return 2
            else:
                return 0
        else:
            return 0


def right_tile_check(arr, x_axis, y_axis, t):
    if arr[x_axis][y_axis] == '.':
        return 0  # null space
    elif arr[x_axis][y_axis] == t:
        return 1  # same tile
    else:
        temp = 0
        j = y_axis + 1
        if j <= 7:
            if t == 'x':
                other_tile = 'o'
            else:
                other_tile = 'x'
            for item in range(j, 8, 1):
                if arr[x_axis][item] == t:
                    temp = 2
                if arr[x_axis][item] == '.':
                    break
            if temp == 2:
                return 2
            else:
                return 0
        else:
            return 0


def right_top_check(arr, x_axis, y_axis, t):
    if arr[x_axis][y_axis] == '.':
        return 0  # null space
    elif arr[x_axis][y_axis] == t:
        return 1  # same tile
    else:
        temp = 0
        i = x_axis - 1
        j = y_axis + 1
        if i >= 0 and j <= 7:
            if t == 'x':
                other_tile = 'o'
            else:
                other_tile = 'x'
            for item in range(i, -1, -1):
                if arr[item][j] == '.':
                    break
                if arr[item][j] == t:
                    temp = 2
                    j += 1
                    if j > 7:
                        break
                else:
                    j += 1
                    if j > 7:
                        break
            if temp == 2:
                return 2
            else:
                return 0
        else:
            return 0


def right_down_check(arr, x_axis, y_axis, t):
    if arr[x_axis][y_axis] == '.':
        return 0  # null space
    elif arr[x_axis][y_axis] == t:
        return 1  # same tile
    else:
        temp = 0
        i = x_axis + 1
        j = y_axis + 1
        if i <= 7 and j <= 7:
            if t == 'x':
                other_tile = 'o'
            else:
                other_tile = 'x'
            for item in range(i, 8, 1):
                if arr[item][j] == '.':
                    break
                if arr[item][j] == t:
                    temp = 2
                    j += 1
                    if j > 7:
                        break
                else:
                    j += 1
                    if j > 7:
                        break
            if temp == 2:
                return 2
            else:
                return 0
        else:
            return 0


def left_top_check(arr, x_axis, y_axis, t):
    if arr[x_axis][y_axis] == '.':
        return 0  # null space
    elif arr[x_axis][y_axis] == t:
        return 1  # same tile
    else:
        temp = 0
        i = x_axis - 1
        j = y_axis - 1
        if i >= 0 and j >= 0:
            if t == 'x':
                other_tile = 'o'
            else:
                other_tile = 'x'
            for item in range(i, -1, -1):
                if arr[item][j] == '.':
                    break
                if arr[item][j] == t:
                    temp = 2
                    j -= 1
                    if j < 0:
                        break
                else:
                    j -= 1
                    if j < 0:
                        break
            if temp == 2:
                return 2
            else:
                return 0
        else:
            return 0


def left_down_check(arr, x_axis, y_axis, t):
    if arr[x_axis][y_axis] == '.':
        return 0  # null space
    elif arr[x_axis][y_axis] == t:
        return 1  # same tile
    else:
        temp = 0
        i = x_axis + 1
        j = y_axis - 1
        if i <= 7 and j >= 0:
            if t == 'x':
                other_tile = 'o'
            else:
                other_tile = 'x'
            for item in range(i, 8, 1):
                if arr[item][j] == '.':
                    break
                if arr[item][j] == t:
                    temp = 2
                    j -= 1
                    if j < 0:
                        break
                else:
                    j -= 1
                    if j < 0:
                        break
            if temp == 2:
                return 2
            else:
                return 0
        else:
            return 0


def place_tile(grid, x_cord, y_cord, tile, dict_f):
    grid[x_cord][y_cord] = tile
    if tile == 'x':
        if flag_top == 2 or dict_f[3] == 2:
            flip_tiles_top(arr=grid, x=x_cord, y=y_cord, tilee=tile)
        if flag_down == 2 or dict_f[4] == 2:
            flip_tiles_down(arr=grid, x=x_cord, y=y_cord, tilee=tile)
        if flag_left == 2 or dict_f[6] == 2:
            flip_tiles_left(arr=grid, x=x_cord, y=y_cord, tilee=tile)
        if flag_right == 2 or dict_f[5] == 2:
            flip_tiles_right(arr=grid, x=x_cord, y=y_cord, tilee=tile)
        if flag_left_top == 2 or dict_f[9] == 2:
            flip_tiles_left_top(arr=grid, x=x_cord, y=y_cord, tilee=tile)
        if flag_left_down == 2 or dict_f[10] == 2:
            flip_tiles_left_down(arr=grid, x=x_cord, y=y_cord, tilee=tile)
        if flag_right_top == 2 or dict_f[7] == 2:
            flip_tiles_right_top(arr=grid, x=x_cord, y=y_cord, tilee=tile)
        if flag_right_down == 2 or dict_f[8] == 2:
            flip_tiles_right_down(arr=grid, x=x_cord, y=y_cord, tilee=tile)
    elif tile == 'o':
        if dict_f[3] == 2:
            flip_tiles_top(arr=grid, x=x_cord, y=y_cord, tilee=tile)
        if dict_f[4] == 2:
            flip_tiles_down(arr=grid, x=x_cord, y=y_cord, tilee=tile)
        if dict_f[6] == 2:
            flip_tiles_left(arr=grid, x=x_cord, y=y_cord, tilee=tile)
        if dict_f[5] == 2:
            flip_tiles_right(arr=grid, x=x_cord, y=y_cord, tilee=tile)
        if dict_f[9] == 2:
            flip_tiles_left_top(arr=grid, x=x_cord, y=y_cord, tilee=tile)
        if dict_f[10] == 2:
            flip_tiles_left_down(arr=grid, x=x_cord, y=y_cord, tilee=tile)
        if dict_f[7] == 2:
            flip_tiles_right_top(arr=grid, x=x_cord, y=y_cord, tilee=tile)
        if dict_f[8] == 2:
            flip_tiles_right_down(arr=grid, x=x_cord, y=y_cord, tilee=tile)


def flip_tiles_top(arr, x, y, tilee):
    i = x - 1
    if i >= 0:
        if tilee == 'x':
            other_tile = 'o'
        else:
            other_tile = 'x'
        for item in range(i, -1, -1):
            if arr[item][y] == other_tile:
                arr[item][y] = tilee
            else:
                break


def flip_tiles_down(arr, x, y, tilee):
    i = x + 1
    if i <= 7:
        if tilee == 'x':
            other_tile = 'o'
        else:
            other_tile = 'x'
        for item in range(i, 8, 1):
            if arr[item][y] == other_tile:
                arr[item][y] = tilee
            else:
                break


def flip_tiles_left(arr, x, y, tilee):
    j = y - 1
    if j >= 0:
        if tilee == 'x':
            other_tile = 'o'
        else:
            other_tile = 'x'
        for item in range(j, -1, -1):
            if arr[x][item] == other_tile:
                arr[x][item] = tilee
            else:
                break


def flip_tiles_right(arr, x, y, tilee):
    j = y + 1
    if j <= 7:
        if tilee == 'x':
            other_tile = 'o'
        else:
            other_tile = 'x'
        for item in range(j, 8, 1):
            if arr[x][item] == other_tile:
                arr[x][item] = tilee
            else:
                break


def flip_tiles_left_top(arr, x, y, tilee):
    i = x - 1
    j = y - 1
    if i >= 0 and j >= 0:
        if tilee == 'x':
            other_tile = 'o'
        else:
            other_tile = 'x'
        for item in range(i, -1, -1):
            if arr[item][j] == other_tile:
                arr[item][j] = tilee
                j -= 1
                if j < 0:
                    break
            else:
                break


def flip_tiles_left_down(arr, x, y, tilee):
    i = x + 1
    j = y - 1
    if i <= 7 and j >= 0:
        if tilee == 'x':
            other_tile = 'o'
        else:
            other_tile = 'x'
        for item in range(i, 8, 1):
            if arr[item][j] == other_tile:
                arr[item][j] = tilee
                j -= 1
                if j < 0:
                    break
            else:
                break


def flip_tiles_right_top(arr, x, y, tilee):
    i = x - 1
    j = y + 1
    if i >= 0 and j <= 7:
        if tilee == 'x':
            other_tile = 'o'
        else:
            other_tile = 'x'
        for item in range(i, -1, -1):
            if arr[item][j] == other_tile:
                arr[item][j] = tilee
                j += 1
                if j > 7:
                    break
            else:
                break


def flip_tiles_right_down(arr, x, y, tilee):
    i = x + 1
    j = y + 1
    if i <= 7 and j <= 7:
        if tilee == 'x':
            other_tile = 'o'
        else:
            other_tile = 'x'
        for item in range(i, 8, 1):
            if arr[item][j] == other_tile:
                arr[item][j] = tilee
                j += 1
                if j > 7:
                    break
            else:
                break


@pass_by_value
def all_valid_moves(grid, t):
    dict_indexes = {}
    dup_board = grid
    k = 0
    for i in range(8):
        for j in range(8):
            if dup_board[i][j] == '.':
                temp = is_valid_move(grid=grid, x_cord=i, y_cord=j, tile=t)
                if temp:
                    dict_1 = {0: i, 1: j, 2: -999, 3: flag_top, 4: flag_down, 5: flag_right, 6: flag_left,
                              7: flag_right_top, 8: flag_right_down, 9: flag_left_top, 10: flag_left_down}
                    dict_indexes[k] = dict_1
                    k += 1
    return dict_indexes


@pass_by_value
def best_move(grid, t, mode, depth_, dict_):
    dup_board = copy.deepcopy(grid)
    new_duplicate = copy.deepcopy(grid)
    if t == 'o':
        ot = 'x'
    else:
        ot = 'o'
    if mode == 'E':
        for item in dict_:
            dup_board = copy.deepcopy(grid)
            x = dict_[item][0]
            y = dict_[item][1]
            place_tile(dup_board, x_cord=x, y_cord=y, tile=t, dict_f=dict_[item])
            dict_[item][2] = evaluation_function(copy_board=dup_board)
        t = maximum(dict_i=dict_)
        return dict_[t]
    elif mode == 'H':
        for item in dict_:
            new_duplicate = copy.deepcopy(grid)
            x = dict_[item][0]
            y = dict_[item][1]
            a = -9999
            b = 9999
            place_tile(new_duplicate, x_cord=x, y_cord=y, tile=t, dict_f=dict_[item])
            val = alpha_beta(current_board=new_duplicate, alpha=a, beta=b, d=depth_, tile_=ot)
            dict_[item][2] = val
        t = maximum(dict_i=dict_)
        return dict_[t]


@pass_by_value
def alpha_beta(current_board, alpha, beta, d, tile_):
    if d == 0:
        return evaluation_function(copy_board=current_board)
    if tile_ == 'o':  # Max
        o_tile = 'x'
        dict_temp = all_valid_moves(grid=current_board, t=tile_)
        for item in dict_temp:
            new_dup = copy.deepcopy(current_board)
            row = dict_temp[item][0]
            col = dict_temp[item][1]
            place_tile(grid=new_dup, x_cord=row, y_cord=col, tile=tile_, dict_f=dict_temp[item])
            value = alpha_beta(current_board=new_dup, alpha=alpha, beta=beta, d=d - 1, tile_=o_tile)
            if alpha <= value:
                alpha = value
            if alpha >= beta:  # prune
                break
        return alpha
    elif tile_ == 'x':  # Min
        o_tile = 'o'
        dict_temp1 = all_valid_moves(grid=current_board, t=tile_)
        for item in dict_temp1:
            new_dup = copy.deepcopy(current_board)
            row = dict_temp1[item][0]
            col = dict_temp1[item][1]
            place_tile(grid=new_dup, x_cord=row, y_cord=col, tile=tile_, dict_f=dict_temp1[item])
            value = alpha_beta(current_board=new_dup, alpha=alpha, beta=beta, d=d - 1, tile_=o_tile)
            if value <= beta:
                beta = value
            if beta <= alpha:
                break
        return beta


def maximum(dict_i):
    maxi_ = -9999
    i = -1
    for item in dict_i:
        if maxi_ < dict_i[item][2]:
            maxi_ = dict_i[item][2]
            i = item
    return i


def evaluation_function(copy_board):
    x, o = compute_score(copy_board)
    return o - x


# main

board = [['.'] * 8 for _ in range(8)]

default_board(grid=board)

x, o = compute_score(grid=board)

print_board(black_balls=x, white_balls=o)

# x represents no of black balls
# y represents no of white balls

turn = 'x'
m = input('Which mode do you wanna play?Enter, (E) for Easy and (H) for Hard:')
m = m.upper()
while m != 'E' and m!= 'H':
    m = input('Which mode do you wanna play?Enter, (E) for Easy and (H) for Hard:')
    m = m.upper()
empty = True
player = 0
computer = 0

while True:
    if turn == 'x':
        dict_para1 = {0: 0, 1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0, 10: 0}
        dict_flag = all_valid_moves(grid=board, t=turn)
        if not bool(dict_flag):
            computer = 1
            break
        x, y = take_input()
        answer = is_valid_move(grid=board, x_cord=x, y_cord=y, tile=turn)
        while answer == False:
            print('Invalid Input Co-ordinates. Read the rules and Enter again')
            x, y = take_input()
            answer = is_valid_move(grid=board, x_cord=x, y_cord=y, tile=turn)
        if answer:
            place_tile(grid=board, x_cord=x, y_cord=y, tile=turn, dict_f=dict_para1)
            empty = is_empty(arr=board)
            if empty == False:
                break
            turn = 'o'
    elif turn == 'o':
        dict_para = {}
        dict_para = all_valid_moves(grid=board, t=turn)
        if not bool(dict_para):
            player = 1
            break
        dict_para1 = best_move(grid=board, t=turn, mode=m, depth_=2, dict_=dict_para)
        place_tile(grid=board, x_cord=dict_para1[0], y_cord=dict_para1[1], tile=turn, dict_f=dict_para1)
        empty = is_empty(arr=board)
        if empty == False:
            break
        turn = 'x'
    x, o = compute_score(grid=board)
    print_board(black_balls=x, white_balls=o)
if empty == False:
    print('Board is Full')
    x, o = compute_score(grid=board)
    if x > o:
        print_board(black_balls=x, white_balls=o)
        print(f'User has won. # of Black Balls are: {x}. # of White Balls are: {o}')
    elif x < o:
        print_board(black_balls=x, white_balls=o)
        print(f'Computer has won. # of White Balls are: {o}. # of Black Balls are: {x}')
    elif x == o:
        print_board(black_balls=x, white_balls=o)
        print(f'Match is a tie. # of Black Balls are: {x}. # of White Balls are: {o}')
else:
    if computer == 1:
        print_board(black_balls=x, white_balls=o)
        print(f'Computer has won. # of White Balls are: {o}. # of Black Balls are: {x}')
    elif player == 1:
        print_board(black_balls=x, white_balls=o)
        print(f'User has won. # of Black Balls are: {x}. # of White Balls are: {o}')