import turtle

screen = turtle.Screen()

image = "Brazilian_States.gif"
screen.bgpic(image)


def get_mouse_click_coor(x, y):
    where = [x, y]
    return where


state_count = 0

# while state_count <= 27:
coordinates = turtle.onscreenclick(get_mouse_click_coor)
print(coordinates)


screen.exitonclick()