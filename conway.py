"""
conway.py
Author: <your name here>
Credit: <list sources used, if any>
Assignment:
Write and submit a program that plays Conway's Game of Life, per 
https://github.com/HHS-IntroProgramming/Conway-Life
        RULES:
    Any live cell with fewer than two live neighbors dies, as if by underpopulation.
    Any live cell with two or three live neighbors lives on to the next generation.
    Any live cell with more than three live neighbors dies, as if by overpopulation.
    Any dead cell with exactly three live neighbors becomes a live cell, as if by reproduction.
"""

from ggame import App, Color, LineStyle, Sprite, RectangleAsset

day1 = Color(0xffffff, 1.0)
day2 = Color(0xC0C0C0, 1.0)
grey = Color(0xC0C0C0, 1.0)
gridgrey = LineStyle(1, grey)
noline = LineStyle(0, grey)

class Cell(Sprite):
    """
    Cell outline
    """
    asset = RectangleAsset(20, 20, gridgrey, day2)

    def mouseClick(self, event):
        Cell((event.x,event.y))

    def __init__(self, position):
        super().__init__(Cell.asset, position)
        ConwayLife.listenMouseEvent("click", mouseClick)
        self.fxcenter = self.fycenter = 0.5
        self.thrust = 0
        self.thrustframe = 1




class ConwayLife(App):
    """
    Game setup
    """
    def __init__(self):
        super().__init__()
        # Background
        bg_asset = RectangleAsset(self.width, self.height, noline, grey)
        bg = Sprite(bg_asset, (0,0))
        Cell((111,111))

    def step(self):
        for cell in self.getSpritesbyClass(Cell):
            cell.step()


ConwayLife().run()