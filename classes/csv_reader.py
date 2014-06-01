import csv


def login(username, password):
    with open("../csv_files/users.csv") as f:
        f_csv = csv.DictReader(f)
        for row in f_csv:
            if row["username"] == username and row["password"] == password:
                return "You can login"
        return "Not a user"

def csv_reader(file):
    with open(file) as f:
        f_csv = csv.DictReader(f)
        for row in f_csv:
            print row

if __name__ == "__main__":
    csv_reader("../csv_files/users.csv")
    print "\n\n"
    csv_reader("../csv_files/goals.csv")

    print "\n\n"
    tests = [("crazcalm", "pass1234"), ("crazcalm", "none")]
    for username, password in tests:
        print username, password
        print login(username, password)
