#!/usr/bin/env python3
from os import listdir
from os.path import isdir, isfile, join

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

def parse_workout(workout_file):
    workouts = []
    with open(workout_file, "r") as file:
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
        title = '{"focus":"%s", "exercises":[%s], "reps":"%s"}' % (focus, ",".join(exercises), reps)
        ex.append(title)

    x = '{"workouts": ['
    x += ",".join(ex)
    x += ']}'

    return x

def write_to_file(file_name, content):
    f = open(file_name, "w")
    f.write(content)
    f.close()

def main():
    cycles = [d for d in listdir(".") if isdir(join(".", d)) and d.startswith("cycle")]
    for cycle in cycles:
        print("parsing %s" % cycle)
        workouts = ["%s/%s" % (cycle, f) for f in listdir(cycle) if isfile(join(cycle, f))]
        for workout in workouts:
            print("  workout : %s" % workout)
            parsed_workout = parse_workout(workout)
            file_name = "%s/json/%s" % (cycle, workout.split("/")[1].replace(".txt", ".json"))
            write_to_file(file_name, parsed_workout)
    print("done")

if __name__ == "__main__":
    main()
