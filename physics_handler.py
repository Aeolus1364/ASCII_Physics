import os
import platform
import time
import subprocess
import object
import random
import string
import keyboard


class Handler:
    def __init__(self, fps=30, grain=10, screen_size=None, border=False):
        self.running = True
        self.framerate = fps
        self.grain = grain
        self.objs = object.ObjGroup()

        if screen_size:
            self.screen_size = screen_size
        else:
            try:
                self.screen_size = [int(v) for v in subprocess.Popen(["stty", "size"], stdout=subprocess.PIPE).communicate()[0].split()][::-1]
                # I'm pretty proud of that list comprehension
            except:
                print("Screen size could not be found, resorting to default.")
                self.screen_size = [30, 15]
        if border:
            self.screen_size = [self.screen_size[0] - 2, self.screen_size[1] - 2]
        self.screen_size[1] -= 1

        self.border = border
        for i in range(2):
            self.objs.add(object.Object(pos=(random.randint(0, self.screen_size[0]-1), random.randint(0,self.screen_size[1]-1)), vel=(random.uniform(-10, 10), random.uniform(-10, 10)), acc=(0, 3), char=random.choice(string.ascii_letters)))
        self.r = Renderer(self.screen_size, border)

    def main_loop(self):
        while self.running:
            time_init = time.time()  # time at start of frame

            self.r.render()
            # self.r.draw_pixel((1, 1), "h")
            self.object_handler()

            diff = time.time() - time_init  # elapsed time
            sleep_time = (1 / self.framerate) - diff  # wait time to meet framerate
            if not sleep_time < 0:  # if frame takes too long, don't sleep
                time.sleep(sleep_time)

    def object_handler(self):
        for obj in self.objs.list():
            self.r.draw_pixel(obj.pos(), obj.char)
            obj.update(self.grain, self.screen_size)
            # print(abs(obj.vy))
            # print(obj.x, obj.y)
            # print(obj.pos())
            # print(obj.vx, obj.vy)
            # print(self.screen_size)

        # print(len(self.objs.list()))


class Renderer:
    def __init__(self, size, border):
        self.size = size
        self.disp = []
        self.border = border
        self.s_char = "|"
        self.t_char = "-"
        self.c_char = "+"

        self.system = platform.system()  # setting terminal clear command for different oses
        if self.system == "Linux":
            self.command = "clear"
        elif self.system == "Windows":
            self.command = "cls"

        self.clear_disp()

    def render(self):
        self.clear_screen()  # terminal cleared before print
        text = ""
        if self.border:
            text += self.c_char + self.t_char * (self.size[0]) + self.c_char + "\n"  # border formatting
            for y in self.disp:
                text += self.s_char
                for x in y:
                    text += x
                text += self.s_char + "\n"
            text += self.c_char + self.t_char * (self.size[0]) + self.c_char
        else:
            for y in self.disp:
                for x in y:
                    text += x
        print(text)  # all data added to a single string to reduce prints per frame
        self.clear_disp()  # display array reset for new frame

    def draw_pixel(self, coords, value):
        if type(coords) == tuple:  # support for single coordinate
            coords = [coords]
        for px in coords:
            if 0 <= px[0] < self.size[0] and 0 <= px[1] < self.size[1]:  # render only within frame
                self.disp[px[1]][px[0]] = value

    def clear_disp(self):
        self.disp = []
        for y in range(self.size[1]):  # generating empty array
            self.disp.append([])
            for x in range(self.size[0]):
                self.disp[y].append(" ")

    def clear_screen(self):
        os.system(self.command)
