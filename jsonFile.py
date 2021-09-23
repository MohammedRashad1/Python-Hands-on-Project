import json

college = {
    "college": "MEA Engineering College",
    "objectives": "Computer Engineering and Mechanical Engineering",
    "departments": {
        "dep1": "Computer",
        "dep2": "Mechanical"
    },
    "years": [
        "year1",
        "year2",
        "year3",
        "year4"
    ],
    "numbers": [1, 2, 3, 4],
    "ID": [10, 20, 30, 40]
}
json.dump(college, open("college.json", "w"))

new_college = json.load(open("college.json", "r"))
print(new_college)
