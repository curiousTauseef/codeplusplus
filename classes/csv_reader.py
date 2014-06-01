import csv

def csv_reader(file):
    with open(file) as f:
        f_csv = csv.DictReader(f)
        for row in f_csv:
            print row

if __name__ == "__main__":
    csv_reader("../csv_files/users.csv")
    print "\n\n"
    csv_reader("../csv_files/goals.csv")
