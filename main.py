import time
import object
import os


class Main:
    def __init__(self):
        self.running = True
        self.framerate = 10
        self.time_grain = 20
        self.r = Renderer((90, 25), (6, 6))
        self.obj1 = object.Object(vel=(20, 10), acc=(0, -3))
        self.obj2 = object.Object(vel=(15, 7), acc=(0, -3), char="o")
        self.objs = [self.obj1, self.obj2]

    def loop(self):
        while self.running:
            time_initial = time.time()
            self.r.update(self.objs)
            for obj in self.objs:
                obj.update(self.time_grain)
            self.r.render()

            # print(self.obj.x, self.obj.y)

            difference = time.time() - time_initial
            sleep_time = (1 / self.framerate) - difference
            if sleep_time < 0:
                sleep_time = 0
            time.sleep(sleep_time)


class Renderer:
    def __init__(self, dim, scale):
        self.dim = dim
        self.scale = scale
        self.grid = []
        self.clear()

    def render(self):
        os.system("clear")
        print("=" * (self.dim[0] + 2))
        for x in self.grid:
            print("|", end="")
            for y in x:
                print(y, end="")
            print("|")
        print("=" * (self.dim[0] + 2))

    def update(self, objs):
        # self.clear()
        for obj in objs:
            if 0 <= obj.x < self.dim[0] and 0 <= obj.y <= self.dim[1]:
                self.grid[self.dim[1] - 1 - int(obj.y)][int(obj.x)] = obj.char

    def clear(self):
        self.grid = []
        for y in range(self.dim[1]):
            self.grid.append([])
            for x in range(self.dim[0]):
                self.grid[y].append(" ")


main = Main()
main.loop()
