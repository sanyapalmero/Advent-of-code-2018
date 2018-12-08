import re
from datetime import datetime

SLEEP = "fallsasleep"
WAKEUP = "wakesup"

def find_id(records):
    # --- part 1 ---- #
    # make set of ids
    id_set = set()
    for record in records:
        id_set.add(record["guard_id"])

    # count sleep time
    final_list = []
    for id_guard in id_set:
        sleep = datetime(1518, 3, 1, 0, 0)
        total = 0
        total_sleep = {}

        for record in records:
            if record["guard_id"] == id_guard and record["status"] == SLEEP:
                sleep = record["date"]
            if record["guard_id"] == id_guard and record["status"] == WAKEUP:
                wakeup = record["date"]
                total += wakeup.minute - sleep.minute

        total_sleep["guard_id"] = id_guard
        total_sleep["total"] = total
        final_list.append(total_sleep)

    # find dict where max sleep time
    max_sleep = max(final_list, key=lambda x: x["total"])

    # make list of all sleeping minutes
    minutes_list = []
    sleep = datetime(1518, 3, 1, 0, 0)
    for record in records:
        if record["guard_id"] == max_sleep["guard_id"] and record["status"] == SLEEP:
            sleep = record["date"]
        if record["guard_id"] == max_sleep["guard_id"] and record["status"] == WAKEUP:
            wakeup = record["date"]
            minutes = wakeup.minute - sleep.minute
            for i in range(minutes):
                minutes_list.append(sleep.minute + i)

    # make dict of count every minutes
    minutes_count = {}
    for elem in minutes_list:
        minutes_count[elem] = minutes_list.count(elem)

    # find minute which have max count
    max_minute = max(minutes_count, key=lambda x: minutes_count[x])
    max_sleep["double_minute"] = max_minute

    part_one = max_sleep["double_minute"] * max_sleep["guard_id"]

    # --- part 2 ---- #
    # make common list with every id and list of sleep minutes
    common_list = []
    for id_guard in id_set:
        sleep = datetime(1518, 3, 1, 0, 0)
        common_dict = {}
        minutes_list = []
        for record in records:
            if record["guard_id"] == id_guard and record["status"] == SLEEP:
                sleep = record["date"]
            if record["guard_id"] == id_guard and record["status"] == WAKEUP:
                wakeup = record["date"]
                minutes = wakeup.minute - sleep.minute
                for i in range(minutes):
                    minutes_list.append(sleep.minute + i)

        common_dict["guard_id"] = id_guard
        if minutes_list:
            common_dict["minutes"] = minutes_list
        else:
            common_dict["minutes"] = [0]
        common_list.append(common_dict)

    # make list of dicts with id and count of every minute
    max_list = []
    for line in common_list:
        max_dict = {}
        temp = {}
        max_dict["guard_id"] = line["guard_id"]
        for minute in line["minutes"]:
            temp[minute] = line["minutes"].count(minute)
            max_dict["count_minutes"] = temp
        max_list.append(max_dict)

    # make list of dicts with max values
    max_minute_list = []
    for line in max_list:
        max_minute_dict = {}
        max_minute = max(line["count_minutes"].items(), key = lambda x: x[1])
        max_minute_dict["guard_id"] = line["guard_id"]
        max_minute_dict["minute"] = max_minute[0]
        max_minute_dict["max_count"] = max_minute[1]
        max_minute_list.append(max_minute_dict)

    # find max count in list
    max_count = max(max_minute_list, key=lambda x: x["max_count"])
    part_two = max_count["minute"] * max_count["guard_id"]

    return part_one, part_two


def parse(records):
    parsed = []
    # parse input
    for line in records:
        record = {}
        if "#" in line:
            splited = list(re.split(r'[\[\]#]', line[1:-1]))
            status = (splited[2].split(" "))
            guard_id = int(status[0])
            record["guard_id"] = guard_id
            record["date"] = datetime.strptime(splited[0], "%Y-%m-%d %H:%M")
            record["status"] = status[1] + status[2]
            parsed.append(record)
        else:
            splited = list(re.split(r'[\[\]]', line[1:-1]))
            date = (splited[0].split(" "))
            status = (splited[1].split(" ")[1:])
            record["guard_id"] = None
            record["date"] = datetime.strptime(splited[0], "%Y-%m-%d %H:%M")
            record["status"] = status[0] + status[1]
            parsed.append(record)

    # sort by time
    sort = sorted(parsed, key=lambda x: x['date'])

    # add id
    temp_id = 0
    for record in sort:
        if record["guard_id"]:
            temp_id = record["guard_id"]
        else:
            record["guard_id"] = temp_id

    return sort


def main():
    records = []
    file = open("records.txt")

    for line in file:
        records.append(str(line))

    parsed = parse(records)
    res = find_id(parsed)
    print(res)

if __name__ == '__main__':
    main()
