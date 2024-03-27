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
for elem_ind in range(len(data) - 1, -1, -1):
    second_ind = elem_ind + 1
    while second_ind < len(data):
        if data[second_ind - 1]["verdict"] > data[second_ind]["verdict"]:
            buff = data[second_ind].copy()
            data[second_ind] = data[second_ind - 1].copy()
            data[second_ind - 1] = buff.copy()
        else:
            break
        second_ind += 1
print("\n".join([f"{i['date']}-{' '.join(i['name'])}-{i['verdict']}" for i in data[:4]]))
