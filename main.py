from turtle import Turtle, Screen
import pandas

screen = Screen()
new_shape = "poland_map.gif"
screen.register_shape(new_shape)

turtle = Turtle()
turtle.shape(new_shape)

number_of_provinces = 16
guessed_provinces = []

# read the data from file
data = pandas.read_csv("provinces.csv")
provinces = data["province"].to_list()  # list of provinces
print(provinces)

game_is_on = True

while game_is_on:
    answer = screen.textinput(title=f"{len(guessed_provinces)}/{number_of_provinces} Provinces Correct",
                              prompt="What province you know?").lower()
    if answer == "stop":
        break

    if answer in provinces and answer not in guessed_provinces:
        t = Turtle()
        t.hideturtle()
        t.penup()
        province_data = data[data.province == answer]  # get info about row with province user guessed
        t.goto(float(province_data.x), float(province_data.y))  # we know te 'x' and 'y' cors, but we need to cast it
        t.write(answer)
        guessed_provinces.append(answer)

screen.exitonclick()

# Make csv file with provinces user doesn't guess
file_output = []
for province in provinces:
    if province not in guessed_provinces:
        file_output.append(province)

data_frame_output = pandas.DataFrame(file_output)
data_frame_output.to_csv("file_output")