from utils.util import file2list
import numpy as np


def parse_board(l, start, end):
    ret = np.zeros((5,5), dtype=int)
    for i in range(start, end):
        ret[i-start] = [int(x) for x in l[i].split()]
    return ret

def result(board, hit, winning_num):
    winning_board = np.ma.array(board, mask=hit)
    sum = winning_board.sum()
    return winning_num*sum

def main():
    l = file2list("./4/input.txt")
    nums = [int(x) for x in l[0].split(",")]

    boards = []
    for i in range(2, len(l), 6):
        boards.append(parse_board(l, i, i+5))

    boards = np.array(boards)

    hits = np.array([np.zeros((5,5), dtype=bool)]*len(boards))
    for i in nums:
        hits = np.where(boards == i, hits + 1, hits)
        if hits.all(axis=1).any() or hits.all(axis=2).any():
            winning_num = i
            winning_board_idx = np.where((hits.all(axis=2).any(axis=1) + hits.all(axis=1).any(axis=1)) == True)[0][0]
            print(result(boards[winning_board_idx], hits[winning_board_idx], winning_num))
            break

    hits = np.array([np.zeros((5,5), dtype=bool)]*len(boards))
    for i in nums:
        has_winned = np.ma.masked_where((hits.all(axis=2).any(axis=1) + hits.all(axis=1).any(axis=1)) == True, np.arange(len(boards)))
        hits = np.where(boards == i, hits + 1, hits)
        if ((hits.all(axis=2) + hits.all(axis=1)).any(axis=1).all()):
            last_board_idx = has_winned[~has_winned.mask]
            last_num = i
            print(result(boards[last_board_idx], hits[last_board_idx], last_num))
            break


main()