#!/bin/env python3

import json

workouts = []
with open("parse-me.txt", "r") as file:
    workout = []
    for line in file.readlines():
        if len(line) == 1:
            workouts.append(workout)
            workout = []
            continue
        workout.append(line.rstrip().split("\t"))
    workouts.append(workout)

ex = []

for workout in workouts:
    focus = workout[0][0]
    day = int(workout[0][1].split(" ")[1].split(":")[0])
    excercises = []
    for excercise in workout[1:]:
        e_type = excercise[0]
        e_name = excercise[1]
        e_vid_url = excercise[3]
        e_10RM = excercise[5]
        e = '{"type":"%s", "name":"%s", "vid":"%s", "max":"%s"}' % (e_type, e_name, e_vid_url, e_10RM)
        excercises.append(e)
    title = '{"focus":"%s", "execrcises":[%s]}' % (focus, ",".join(excercises))
    ex.append(title)

x = '{"workouts": ['
x += ",".join(ex)
x += ']}'

f = open("workouts.json", "w")
f.write(x)
f.close()

