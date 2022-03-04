import turtle as t

# Pattern
# 3 sides is 120
# 4 sides is 90
# 5 sides is 72

def draw_polygon(sides_num, sides_length):
    turn_degree = 360 // sides_num

    for i in range(sides_num):
        t.forward(sides_length)
        t.right(turn_degree)

draw_polygon(8, 25)
