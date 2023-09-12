from hanoi_tower import HanoiTower
from output_controller import OutputController

if __name__ == "__main__":
    output_controller = OutputController()
    tower = HanoiTower(5, output_controller)
    tower.solve()

