from turtle import Turtle

STARTING_POS = [(0,0), (-20, 0), (-40, 0)]
MOVE_DIST = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:
    def __init__(self) -> None:
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        for pos in STARTING_POS:
            self.add_seg(position=pos)
            
    def add_seg(self, position):
        new_seg = Turtle(shape="square")
        new_seg.color("white")
        new_seg.up()
        new_seg.setpos(position)
        self.segments.append(new_seg)


    def extend(self):
        self.add_seg(self.segments[-1].position())
        
    def reset_snake(self):
        for seg in self.segments:
            seg.goto(10000, 10000)
        self.segments.clear()
        self.create_snake()
        self.head = self.segments[0]
    
    def move(self):
        for seg in range(len(self.segments)-1 ,0,-1):
            new_x = self.segments[seg-1].xcor()
            new_y = self.segments[seg-1].ycor()
            self.segments[seg].goto(new_x,new_y)
        self.head.forward(MOVE_DIST)
        
    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)


    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)
    

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    
    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    
