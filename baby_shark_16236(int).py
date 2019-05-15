'''
1. 아기상어의 현재 위치에서 먹을 수 있는 가장 가까운 물고기를 찾는다.
2. 만약 먹을 수 있는 물고기가 없으면 종료
3. 아니라면, 해당 물고기 위치로 이동한다.
4. 아기상어가 커질 수 있으면 커진다.
5. 1번부터 반복한다
'''

import queue
import time

class BabyShark:
    def __init__(self, board, shark_no, shark_size):
        self.board = board
        self.shark_size = shark_size
        self.shark_no = shark_no
        self.fish_cnt, self.fish_cnt_tot, self.move_cnt = 0, 0, 0

        self.set_shark_pos()

    def print_info(self):
        print('self.board :')
        for i in self.board:
            print(i)

    #     print('self.shark_size :', self.shark_size)
    #     print('self.fish_cnt :', self.fish_cnt)
    #     print('self.fish_cnt_tot :', self.fish_cnt_tot)
    #     print('self.move_cnt :', self.move_cnt)
    #     print('')
        

    def set_shark_pos(self):
        board_len = len(self.board)
        for r in range(board_len):
            for c in range(board_len):
                if board[r][c] == self.shark_no:
                    self.shark_pos = [r, c]
                    break


    # 아기상어 크기보다 작은 물고기가 있는지
    def is_exists_eatable_fish(self):
        is_exists = False

        for r in self.board:
            for c in r:
                if self.shark_size > c:
                    is_exists = True
                    break

        return is_exists


    def get_move_one(self, pos):
        r, c= pos[0], pos[1]
        board_len = len(self.board)
        m = list()

        if r-1 >= 0 and board[r-1][c] <= self.shark_size and [r-1, c] != self.shark_pos:
            m.append([r-1, c])
        
        if r+1 <= board_len-1 and board[r+1][c] <= self.shark_size and [r+1, c] != self.shark_pos:
            m.append([r+1, c])

        if c-1 >= 0 and board[r][c-1] <= self.shark_size and [r, c-1] != self.shark_pos:
            m.append([r, c-1])

        if c+1 <= board_len-1 and board[r][c+1] <= self.shark_size and [r, c+1] != self.shark_pos:
            m.append([r, c+1])

        return m


    def get_pick_one(self, pos):
        if not pos:
            return pos
        else:
            pos.sort()
            return pos[0]


    def get_next_fish_info(self):
        # print('\n==========================================')
        next_fish_pos, move = list(), 0

        # if self.is_exists_eatable_fish():
        std_pos = [self.shark_pos, 0]

        visited_pos = list()
        visited_pos.append(self.shark_pos)

        q = queue.Queue()
        q.put_nowait(std_pos)

        same_move = 0

        while(q.qsize()>0):
            
            p = q.get_nowait()
            l = p[1]

            # print('next_fish_pos : ', next_fish_pos)
            # print('l : ', l)
            # print('same_move : ', same_move)

            if next_fish_pos and l == same_move:
                break

            try:
                fish_pos = self.get_move_one(p[0])
                fish_pos.sort()

                for fp in fish_pos:
                    # print('fp ', fp)
                    a, b = fp[0], fp[1]
                    if board[a][b] < self.shark_size and board[a][b] > 0:
                        next_fish_pos.append(fp)
                        move = l+1
                        same_move = move
                        # break
                
                if not next_fish_pos:   # next_fish_pos가 없으면
                    
                    for fp in fish_pos:
                        if fp not in visited_pos:
                            # print('fp ', fp)
                            q.put_nowait([fp, l+1])
                            visited_pos.append(fp)
             

            except Exception as e:
                # print('더 이상 없음 :', e)
                break
        # print('next_fish_pos, move', next_fish_pos, move)
        # print('==========================================\n')

        return self.get_pick_one(next_fish_pos), move

                        
    def move(self, pos, move):
        r, c = self.shark_pos[0], self.shark_pos[1]
        r2, c2 = pos[0], pos[1]
        self.board[r][c] = 0
        self.shark_pos = pos
        self.board[r2][c2] = self.shark_no
        self.move_cnt += move

        self.fish_cnt += 1
        self.fish_cnt_tot += 1

        if self.shark_size == self.fish_cnt:
            self.shark_size += 1
            self.fish_cnt = 0

        

if __name__ == '__main__':

    n = 6
    board = [
[5, 4, 3, 2, 3, 4],
[4, 3, 2, 3, 4, 5],
[3, 2, 9, 5, 6, 6],
[2, 1, 2, 3, 4, 5],
[3, 2, 1, 6, 5, 4],
[6, 6, 6, 6, 6, 6]
    ]

    shark_no = 9
    shark_size = 2

    n = int(input())
    board = []
    for i in range(n):
        board.append(list(map(int, input().split(' '))))

    # start_time = time.time() 

    
    bs = BabyShark(board, shark_no, shark_size)

    next_fish_pos, move = bs.get_next_fish_info()    

    while(next_fish_pos):
        bs.move(next_fish_pos, move)
        # bs.print_info()
        next_fish_pos, move = bs.get_next_fish_info()
        
    print(bs.move_cnt)



    # end_time = time.time()
    # print("WorkingTime: {} sec".format(end_time-start_time))
