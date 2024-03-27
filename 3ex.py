with open("history_mirror.csv", "r", encoding="utf-8") as file:
    data = []
    first = True
    for stroke in file.readlines():
        if first:
            first = False
        else:
            to_app = {}
            date, name, verdict = stroke.strip().split(",")
            to_app["date"] = date
            to_app["name"] = name.split(" ")
            to_app["verdict"] = verdict
            data.append(to_app)

while True:
    inp = input()
    if inp == "stop":
        break
    else:
        name, family_name = inp.split()
        for elem in data:
            if elem["name"][2] == family_name and elem["name"][1] == name:
                print(f"Предсказание для {elem['name'][0]} {elem['name'][1][0]}.{elem['name'][2][0]}. - {elem['verdict']}")
