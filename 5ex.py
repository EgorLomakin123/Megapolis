def hash(stroke):
    """"Эта функция генерирует хэш, введеной строки stroke.
    Для преобразования символа строки в число используется встроенная функция ord.

    Описание аргументов:
    stroke - str-значение данной строки

    """
    summ = 0
    k = 1
    for symb in stroke:
        summ += (ord(symb) * k) % (10 ** 9 + 9)
        k *= 67
    return summ


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
answer = ["ID,date,username,verdict"]
for stroke in data:
    to_app = []
    to_app.append(str(hash(" ".join(stroke["name"]))))
    to_app.append(stroke["date"])
    to_app.append(" ".join(stroke["name"]))
    to_app.append(stroke["verdict"])
    answer.append(",".join(to_app))
with open("users_with_hash.csv", "w", encoding="utf-8") as file:
    print("\n".join(answer), file=file)
