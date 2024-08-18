from tkinter import Tk, BOTH, Canvas
import time
from maze import Window, Point, Line, Cell

def main():
    window = Window(800, 600)
    window.redraw()
    
    # Create a Cell and draw it
    cell = Cell(50, 50, 100, 100, window)
    cell.draw()
    cell2 = Cell(100, 50, 150, 100, window)
    cell2.draw()
    cell.draw_move(cell2)
    window.wait_for_close()

        
 


main()


