from stack import Stack
from output_controller import OutputController


class HanoiTower:
    source: Stack
    auxiliary: Stack
    destiny: Stack
    moves: int
    output_controller: OutputController

    def __init__(self, number_of_elements: int, output_controller: OutputController) -> None:
        self.source = Stack()
        self.auxiliary = Stack()
        self.destiny = Stack()
        self.moves = 0
        self.output_controller = output_controller

        for element in range(1, number_of_elements + 1)[::-1]:
            self.source.push(element)

    def __move__(self, source: Stack, destiny: Stack) -> None:
        if destiny.peek() == 0 or source.peek() < destiny.peek():
            destiny.push(source.pop())
            self.moves += 1
            self.output_controller.write("=====================================")
            self.output_controller.write(self)
        else:
            raise Exception("Invalid move")

    def __recursively_solver__(self, number_of_elements: int, source: Stack, auxiliary: Stack, destiny: Stack) -> None:
        if number_of_elements == 1:
            self.__move__(source, destiny)
        else:
            self.__recursively_solver__(number_of_elements - 1, source, destiny, auxiliary)
            self.__move__(source, destiny)
            self.__recursively_solver__(number_of_elements - 1, auxiliary, source, destiny)

    def solve(self) -> None:
        self.output_controller.write("=====================================")
        self.output_controller.write(self)
        self.__recursively_solver__(self.source.size(), self.source, self.auxiliary, self.destiny)
        self.output_controller.write("=====================================")
        self.output_controller.write(f"Number of moves: {self.number_of_moves()}")

    def number_of_moves(self) -> int:
        return self.moves

    def __str__(self) -> str:
        return f"   source: {self.source}\nauxiliary: {self.auxiliary}\n  destiny: {self.destiny}"
