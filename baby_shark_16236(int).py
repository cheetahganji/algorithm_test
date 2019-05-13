'''
bs = [pos:(), size:2, move:0]


'''

class Node:
    def __init__(self, pos, lv):
        self.pos = pos
        self.lv = lv
        self.next = None

    


class Queue:
    def __init__(self):
        self.head = None
        self.tail = None

    def is_empty(self):
        if not self.head:
            return True
        else:
            return False

    def enqueue(self, node):
        if self.is_empty():
            self.head = node
            self.tail = node
        else:
            self.tail.next = node
            self.tail = node

    def dequeue(self):
        if self.is_empty():
            return None

        ret_node = self.head
        self.head = self.head.next
        return ret_node

    def peek(self):
        if self.is_empty():
            return None

        return self.head



class BabyShark:
    def __init__(self, board):
        self.pos = [0, 0]
        self.move_cnt = 0
        self.size = 2
        self.board = board
        self.set_bs_stat()

    def set_bs_stat(self):
        for i, v in enumerate(self.board):
            if 9 in v:
                self.pos =[i, v.index(9)]

    def next_fish_pos(self):
        board_len = len(self.board)
        eatable_fish_pos = []

        for r in range(board_len):
            for c in range(board_len):
                if self.board[r][c] < self.size and self.board[r][c] in range(1,7):
                    eatable_fish_pos.append([r,c])
        
        print('eatable_fish_pos :', eatable_fish_pos)

        num_of_pos = len(eatable_fish_pos)
        if num_of_pos == 0:
            return None
        elif num_of_pos == 1:
            return eatable_fish_pos[0]
        else:
            return self.get_shortest_pos(eatable_fish_pos)


    def get_shortest_pos(self, eatable_fish_pos):
        tmp_shark_pos = self.pos
        # #temp
        # 1: 한 번 움직였을 때 
        # 2: 1에서 한번 움직여서 갈 수 있는 위치
        # dp[n] : n번 움직여서 갈 수 있는 위치
        # dp[n] : dp[n-1] + ( [-1,0], [1,0], [0,-1],[0,1] )

        return [-1, -1]


    def get_next_pos(self, pos):
        print('pos :', pos)
        r, c= pos[0], pos[1]
        board_len = len(self.board)

        m = list()
        if r-1 >= 0 and board[r-1][c] <= self.size:
            m.append([r-1, c])
        
        if r+1 <= board_len-1 and board[r+1][c] <= self.size:
            m.append([r+1, c])

        if c-1 >= 0 and board[r][c-1] <= self.size:
            m.append([r, c-1])

        if c+1 <= board_len-1 and board[r][c+1] <= self.size:
            m.append([r, c+1])

        return m



if __name__ == '__main__':
    n = 4
    board = [
        [4, 3, 2, 1],
        [0, 0, 0, 0],
        [0, 0, 9, 0],
        [1, 2, 3, 4]
    ]

    for i in board:
        print(i)


    bs = BabyShark(board)
    print(bs.next_fish_pos())

    print(bs.get_next_pos([1, 2]))


    q = Queue()

    
    q.enqueue(Node((1,2), 1))
    q.enqueue(Node((1,3), 1))


    print(q.peek())

