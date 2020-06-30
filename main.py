from operational import basic_mode
import global_variables as gv


def input_command() -> None:
    while True:
        input_style = str(input("Input command: > ")).split()

        if len(input_style) == 3 and input_style[0] == "start":
            p1, p2 = input_style[1], input_style[2]
            player1 = gv.USER if p1 == "user" else gv.EASY if p1 == "easy" else gv.MEDIUM if p1 == "medium" else -1
            player2 = gv.USER if p2 == "user" else gv.EASY if p2 == "easy" else gv.MEDIUM if p2 == "medium" else -1

            if player1 != -1 != player2:
                basic_mode(player1, player2)
            else:
                print("Bad parameters!")

        elif len(input_style) == 1 and input_style[0] == "exit":
            break;
        else:
            print("Bad parameters!")


if __name__ == "__main__":
    input_command()
