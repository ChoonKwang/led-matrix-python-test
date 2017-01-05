from rgbmatrix import graphics

global fx, fy, font

class Character():
    def __init__(self, cfx, cfy, cfont):
        global fx, fy, font
        fx = cfx
        fy = cfy
        font = cfont

    def two(self, canvas, x, y, color):
        y_mp = y + (fy-1)/2;
        x_max = x + fx - 2; 
        y_max = y + fy - 1;
        space = font + 1;
        for i in range(0,3):
            graphics.DrawLine(canvas, x, y+(i*space), x_max, y+(i*space), color)
            graphics.DrawLine(canvas, x_max, y, x_max, y_mp, color)
            graphics.DrawLine(canvas, x, y_mp, x, y_max, color)


