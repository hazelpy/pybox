class Camera:
    x: float
    x_min: float
    x_max: float

    y: float
    y_min: float
    y_max: float

    w: float
    h: float

    def __init__(self, x=0, y=0, w=1024, h=576, x_min=0, x_max=0, y_min=0, y_max=0):
        self.x, self.x_min, self.x_max = x, x_min, x_max
        self.y, self.y_min, self.y_max = y, y_min, y_max
        self.w = w
        self.h = h

    def move(self, dir: str, amt: float):
        if dir.lower() == "left":
            if self.x - amt > self.x_min:
                self.x = self.x - amt
            else:
                self.x = self.x_min
        elif dir.lower() == "right":
            if self.x + amt < self.x_max:
                self.x = self.x + amt
            else:
                self.x = self.x_max
        elif dir.lower() == "up":
            if self.y - amt > self.y_min:
                self.y = self.y - amt
            else:
                self.y = self.y_min
        elif dir.lower() == "down":
            if self.y + amt < self.y_max:
                self.y = self.y + amt
            else:
                self.y = self.y_max

    def moveto(self, pos: tuple):
        if pos[0] > self.x_min:
            if pos[0] < self.x_max:
                self.x = pos[0]
            else:
                self.x = self.x_max
        else:
            self.x = self.x_min

        if pos[1] > self.y_min:
            if pos[1] < self.y_max:
                self.y = pos[1]
            else:
                self.y = self.y_max
        else:
            self.y = self.y_min


def make_camera(x: float=0, y: float=0, x_min: float=0, y_min: float=0, x_max: float=0, y_max: float=0, w: float=1024, h: float=576):
    return Camera(x, y, w, h, x_min, x_max, y_min, y_max)
