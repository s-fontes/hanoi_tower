from time import time

from hanoi_tower import HanoiTower
from output_controller import OutputController

if __name__ == "__main__":
    output_controller = OutputController()
    tower = HanoiTower(5, output_controller)
    initial_time = time()
    tower.solve()
    output_controller.write("=====================================")
    output_controller.write("Execution time: %.4f" % (time() - initial_time))


