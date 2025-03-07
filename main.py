import datetime


class Diary:
    def __init__(self):

        self.wrote = "no"
        print("What happened today?")
        self.day_lines = []
        date = datetime.datetime.now()
        self.date = datetime.datetime.strftime(date,"%d-%m-%Y")
        self.path = f"Diary/{self.date}.txt"
        while True:
            query = input("Do you have something to write?")
            if query == "yes":
                self.write()
            elif query == "no":
                if self.wrote == "yes":
                    self.save()
                break




    def write(self):
        self.day_lines = [self.date]
        while True:
            action = input()
            if action == "Exit":
                self.wrote = "yes"
                break
            else:
                self.day_lines.append(action)

    def save(self):
        exist = self.check_file()
        with open(self.path,exist) as file:
            file.writelines(self.day_lines)

    def check_file(self):
        try:
            with open(self.path,"r") as file:
                file.readlines()
        except FileNotFoundError:
            return "w"
        else:
            return "a"

Diary()