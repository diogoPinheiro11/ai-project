

from games.mijnlieff.MijnlieffAction import MijnlieffAction
from games.mijnlieff.MijnlieffPlayer import MijnlieffPlayer
from games.mijnlieff.MijnlieffState import MijnlieffState
from games.mijnlieff.MijnlieffPieceType import MijnlieffPieceType


class HumanMijnlieffPlayer(MijnlieffPlayer):

    def __init__(self, name):
        super().__init__(name)

    def get_action(self, state: MijnlieffState):
        state.display()
        last_action = state.get_last_move()
        while True:
            # noinspection PyBroadException

            try:
                piece = int(input(f"Player {state.get_acting_player()}, Choose an Piece (1(S) | 2(D) | 3(H) | 4(L)): "))
                if piece not in range(1, 5):
                    print("Invalid piece. Please choose a piece between 1 and 4.\n")
                    continue

                row = int(input(f"Player {state.get_acting_player()}, Choose an line: "))
                col = int(input(f"Player {state.get_acting_player()}, Choose an column: "))
                action = MijnlieffAction(col, row, list(MijnlieffPieceType)[piece-1])
                # Check if the move is valid based on the last_action
                if last_action is not None and not state.is_valid_move(action):
                    print("Invalid move based on the last played piece. Please try again.\n")
                    continue

                if state.validate_action(action):
                    return action
                else:
                    print("Invalid move. Please try again.\n")
            except Exception:
                continue

    def event_action(self, pos: int, action, new_state: MijnlieffState):
        # ignore
        pass

    def event_end_game(self, final_state: MijnlieffState):
        # ignore
        pass