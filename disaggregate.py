import csv

def main(filename):
    with open(filename) as csvFile:
        reader = csv.DictReader(csvFile, delimiter=';')

        with open(filename + ".out", "w") as outputFile:
            writer = csv.DictWriter(outputFile, delimiter=';', fieldnames=reader.fieldnames)

            for row in reader:
                count = row['count']
                for i in range(int(count)):
                    writer.writerow(row)


if __name__ == "__main__":
    main("data/educationEnglish.csv")
