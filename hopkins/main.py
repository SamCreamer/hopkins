import chess
from hopkins import Hopkins


def main():
    # Play a chess game against Hopkins
    chess_board = chess.Board()
    hopkins = Hopkins()

    while True:
        # Loop for the chess game
        # For now, Hopkins will only play with black
        # TODO: Fix this
        pass
    # print(hopkins.get_move(STARTING_FEN))


if __name__ == '__main__':
    main()
