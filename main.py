import datetime
print("What happened today?")
day_lines = []
date = datetime.datetime.now()
date = datetime.datetime.strftime(date,"%d-%m-%Y")
print(date)
def main():
    while True:
        write()


def write():
    while True:
        action = input()
        if action == "Exit":
            pass
        else:
            day_lines.append(action)

main()