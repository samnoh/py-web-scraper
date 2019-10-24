import csv


class Output:
    """ Output Definition """

    @staticmethod
    def console_output(name, data, **kwargs):
        print(f"{str(name).capitalize()} {len(data)} jobs")
        print(data)

    @staticmethod
    def csv_output(name, rows, **kwargs):
        file = open(f"{name}_jobs.csv", mode="w")
        writer = csv.writer(file)
        if "first_row" in kwargs:
            writer.writerow(kwargs["first_row"])
        for row in rows:
            writer.writerow(row.values())
