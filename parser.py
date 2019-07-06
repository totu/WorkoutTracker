#!/bin/env python3
import json

def get_focus(day):
    day = int(day.split(" ")[1].split(":")[0])
    if day == 1:
        return "Chest"
    elif day == 2:
        return "Quads"
    elif day == 3:
        return "Back"
    elif day == 4:
        return "Glute & Ham"
    elif day == 5:
        return "Shoulders & Arms"
    else:
        return "Nothing..."

workouts = []
with open("week1.txt", "r") as file:
    workout = []
    day = None
    for line in file.readlines():
        if line.startswith("Week") or line.startswith("Exercise"):
            continue
        if line.startswith("Day"):
            if day:
                workouts.append(workout)
                workout = []
            day = line.rstrip()
            continue
        l = line.rstrip().split("\t")
        l.append(day)
        workout.append(l)
    workouts.append(workout)

ex = []

for workout in workouts:
    exercises = []
    for exercise in workout:
        name = exercise[0]
        _set = exercise[1]
        kg = exercise[2]
        reps = exercise[3]
        day = exercise[4]
        focus = get_focus(day)
        e = '{"name":"%s", "kg":"%s", "sets":"%s"}' % (name, kg, _set)
        exercises.append(e)
    title = '{"focus":"%s", "exercises":[%s]}' % (focus, ",".join(exercises))
    ex.append(title)


x = '{"workouts": ['
x += ",".join(ex)
x += ']}'

f = open("week1.json", "w")
f.write(x)
f.close()
print(x)

