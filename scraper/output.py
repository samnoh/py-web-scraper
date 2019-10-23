import csv


class Output:
    """ Output Definition """

    @staticmethod
    def console_output(data):
        print(data)

    @staticmethod
    def csv_output(name, rows, first_row=None):
        file = open(f"{name}_jobs.csv", mode="w")
        writer = csv.writer(file)
        if first_row:
            writer.writerow(first_row)
        for row in rows:
            writer.writerow(row.values())
