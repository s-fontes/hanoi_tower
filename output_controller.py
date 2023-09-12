import os
from datetime import datetime


class OutputController:
    def __init__(self, file_prefix: str = "hanoi_tower") -> None:
        if not os.path.exists("./output"):
            os.makedirs("./output")
        self.path = f"./output/{file_prefix}_{datetime.now().strftime('%Y%m%d%H%M%S')}.txt"

    def write(self, data):
        print(data)
        with open(self.path, 'a+') as f:
            f.write(f"{data}\n")
