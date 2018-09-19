class Object:
    def __init__(self, pos=(0,0), vel=(0,0), acc=(0,0), char="x"):
        self.x = pos[0]
        self.y = pos[1]
        self.vx = vel[0]
        self.vy = vel[1]
        self.ax = acc[0]
        self.ay = acc[1]
        self.char = char
        self.dead = False

    def update(self, grain, pos):
        self.vx += self.ax / grain
        self.x += self.vx / grain
        self.vy += self.ay / grain
        self.y += self.vy / grain

        if self.x < 0

    def pos(self):
        return int(self.x), int(self.y)

    def kill(self):
        self.dead = True


class ObjGroup:
    def __init__(self):
        self.objects = []

    def update(self, grain):
        for c, obj in enumerate(self.objects):
            obj.update(grain)
            if obj.dead:
                del self.objects[c]

    def add(self, objs):
        if type(objs) == list:
            for obj in objs:
                self.objects.append(obj)
        else:
            self.objects.append(objs)

    def list(self):
        return self.objects
