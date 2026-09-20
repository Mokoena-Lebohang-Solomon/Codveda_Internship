def create_board(n):
    return [
        ["."] * n
        for _ in range(n)
    ]


def is_safe(board, row, col, n):

    # Check column
    for i in range(row):
        if board[i][col] == "Q":
            return False

    # Check upper-left diagonal
    i = row - 1
    j = col - 1

    while i >= 0 and j >= 0:

        if board[i][j] == "Q":
            return False

        i -= 1
        j -= 1

    # Check upper-right diagonal
    i = row - 1
    j = col + 1

    while i >= 0 and j < n:

        if board[i][j] == "Q":
            return False

        i -= 1
        j += 1

    return True


def solve_n_queens(board, row, n):

    # All queens have been placed
    if row == n:
        return True

    # Try every column
    for col in range(n):

        if is_safe(
            board,
            row,
            col,
            n
        ):

            # Place queen
            board[row][col] = "Q"

            # Recursively place next queen
            if solve_n_queens(
                board,
                row + 1,
                n
            ):
                return True

            # Backtrack
            board[row][col] = "."

    return False


def print_board(board):

    print("\nChessboard:")

    for row in board:
        print(" ".join(row))


def main():

    print("=" * 40)
    print("          N-QUEENS PROBLEM")
    print("=" * 40)

    try:

        n = int(
            input(
                "Enter the number of queens: "
            )
        )

        if n < 1:
            print(
                "Number of queens must be at least 1."
            )
            return

    except ValueError:

        print(
            "Please enter a valid whole number."
        )
        return

    board = create_board(n)

    if solve_n_queens(
        board,
        0,
        n
    ):

        print(
            f"\nA solution was found for {n} queens."
        )

        print_board(board)

    else:

        print(
            f"\nNo solution exists for {n} queens."
        )


if __name__ == "__main__":
    main()