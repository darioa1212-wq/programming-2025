# Data Analysis
# Author: Dario Androsevic
# November 2025

# Analyse the data provided in class
import csv
def main():
    file_path = "data/nyc-weather.txt"
    file = open(file_path, "r")
    reader = csv.reader(file)

    header = next(reader)

    row_count = 0
    total_rainfall = 0
    rainfall_count = 0

    total_min_temp = 0
    miin_temp_count = 0

    june_max_temp_total = 0
    june_max_temp_count = 0

    for row in reader:
        row_count += 1

        date = row[0]
        precipitation = row[1]
        min_temp = row[4]
        max_temp = row[5]

        if precipitation != "":
            total_rainfall += float(precipitation)
            rainfall_count += 1

        if min_temp != "":
            total_min_temp += float(min_temp)
            miin_temp_count += 1

        if date.startswith("06") and max_temp != "":
            june_max_temp_total += float(max_temp)
            june_max_temp_count += 1

    if rainfall_count > 0:
        average_rainfall = total_rainfall / rainfall_count
    else:
        average_rainfall = 0

    if miin_temp_count > 0:
        average_min_temp = total_min_temp / miin_temp_count
    else:
        average_min_temp = 0

    if june_max_temp_count > 0:
        average_june_max_temp = june_max_temp_total / june_max_temp_count
    else:
        average_june_max_temp = 0

    print(f"Average rainfall: {average_rainfall:.2f} inches")
    print(f"Average minimum temperature: {average_min_temp:.2f} degrees")
    print(f"Average maximum temperature in June: {average_june_max_temp:.2f} degrees")

    file.close()



    pass

if __name__ == "__main__":
    main()
