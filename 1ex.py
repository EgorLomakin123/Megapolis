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
answer = []
with open("mirror_error.csv", "w", encoding="utf-8") as file:
    to_write = ["date,username"]
    for elem in data:
        if elem["verdict"] == "Победа над смертью":
            answer.append(elem)
            to_write.append(f"{elem['date']},{' '.join(elem['name'])}")
    print("\n".join(to_write), file=file)
print(f"Сообщение было зафиксировано: {answer[0]['date']} у пользователя {answer[0]['name'][0]} {answer[0]['name'][1][0]}.{answer[0]['name'][2][0]}.")