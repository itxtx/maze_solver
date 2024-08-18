from tkinter import Tk, BOTH, Canvas
import time   

class Window(Tk):
    
    def __init__(self, width=800, height=600):
        super().__init__()
        self.width = width
        self.height = height
        self.__root = Tk("loldbdbdbr")
        self.__root.title()
        self.canvas = Canvas(self.__root, height=self.height, width=self.width)
        self.canvas.pack()
        self.running = False
        
    def redraw(self):
        self.canvas.delete("all")
        self.canvas.create_rectangle(0, 0, self.width, self.height, fill="white")
        self.canvas.create_text(self.width/2, self.height/2, text="Hello, World!")
        
        
    def wait_for_close(self):
        self.running = True
        while self.running:
            self.__root.update_idletasks()
            self.__root.update()
        self.__root.destroy()
        
    def close(self):
        self.running = False
        self.__root.quit()
        
    def draw_line(self, Line, fill_color="black"):
        Line.draw(self.canvas, fill_color)

    
class Point:
    
    def __init__(self, x, y):
        self.x = x
        self.y = y
        
class Line:
    
    def __init__(self, start, end):
        self.start = start
        self.end = end
        
    def draw(self, canvas, fill_color):
        canvas.create_line(self.start.x, self.start.y, self.end.x, self.end.y, fill=fill_color, width=2) 
        

class Cell:
    def __init__(self, x1, y1, x2, y2, win = None):
        # Coordinates of the top-left and bottom-right corners
        self._x1 = x1
        self._y1 = y1
        self._x2 = x2
        self._y2 = y2
        
        # The window or canvas where the cell will be drawn
        self._win = win
        
        # By default, all walls are present
        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True

    def draw(self):
        # Draw the left wall if it exists
        if self.has_left_wall:
            line = Line(Point(self._x1, self._y1), Point(self._x1, self._y2))
            self._win.draw_line(line)
        
        # Draw the top wall if it exists
        if self.has_top_wall:
            line = Line(Point(self._x1, self._y1), Point(self._x2, self._y1))
            self._win.draw_line(line)
        
        # Draw the right wall if it exists
        if self.has_right_wall:
            line = Line(Point(self._x2, self._y1), Point(self._x2, self._y2))
            self._win.draw_line(line)
        
        # Draw the bottom wall if it exists
        if self.has_bottom_wall:
            line = Line(Point(self._x1, self._y2), Point(self._x2, self._y2))
            self._win.draw_line(line)
            
            
    def draw_move(self, to_cell, undo=False):
        center_x_self = (self._x1 + self._x2) / 2
        center_y_self = (self._y1 + self._y2) / 2
        center_point_self = Point(center_x_self, center_y_self)
        
        center_x_to_cell = (to_cell._x1 + to_cell._x2) / 2
        center_y_to_cell = (to_cell._y1 + to_cell._y2) / 2
        center_point_to_cell = Point(center_x_to_cell, center_y_to_cell)
        
        line = Line(center_point_self, center_point_to_cell)
        self._win.draw_line(line, "red")
        
        
  
class Maze:
    
    def __init__(
        self,
        x1,
        y1,
        num_rows,
        num_cols,
        cell_size_x,
        cell_size_y,
        win= None,
    ):
        self._x1 = x1
        self._y1 = y1
        self._num_rows = num_rows   
        self._num_cols = num_cols
        self._cell_size_x = cell_size_x
        self._cell_size_y = cell_size_y
        self._win = win
        
        # Create cells in a matrix (list of lists)
        self._cells = self._create_cells()
        
        # Draw the entire maze initially
        self._draw_cells()
        
        
    def _create_cells(self):
        cells = []
        for i in range(self._num_rows):
            row = []
            for j in range(self._num_cols):
                x1 = self._x1 + j * self._cell_size_x
                y1 = self._y1 + i * self._cell_size_y
                x2 = x1 + self._cell_size_x
                y2 = y1 + self._cell_size_y
                cell = Cell(x1, y1, x2, y2, self._win)
                row.append(cell)
            cells.append(row)
        return cells
        
    def _draw_cells(self):
        for i in range(self._num_rows):
            for j in range(self._num_cols):
                self._draw_cell(i, j)
                
    def _draw_cell(self, i, j):
        # Calculate the position of the cell
        cell = self._cells[i][j]
        cell.draw()
        
        # Animate each cell being drawn
        self._animate()
        
        
    def _animate(self):
        self._win.redraw()
        time.sleep(0.5)
        
        
        
        