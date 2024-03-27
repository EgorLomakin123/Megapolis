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
years = {}
for stroke in data:
    year, month, day = stroke["date"].split("-")
    if year in years:
        years[year].append(stroke)
    else:
        years[year] = [stroke]
for key in years:
    print(f"В {key} году зеркало было использовано {len(years[key])}.")