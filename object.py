class Object:
    def __init__(self, pos=(0,0), vel=(0,0), acc=(0,0), char="x"):
        self.x = pos[0]
        self.y = pos[1]
        self.vx = vel[0]
        self.vy = vel[1]
        self.ax = acc[0]
        self.ay = acc[1]
        self.char = char

    def update(self, grain):
        self.vx += self.ax / grain
        self.x += self.vx / grain
        self.vy += self.ay / grain
        self.y += self.vy / grain

