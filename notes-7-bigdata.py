# Big Data
# Author: Dario
# 17 November

# Process files
# Ingest large data
# Make sense of data

def main():
    # Get the file
    path = "data/sfu_best_cmpt120.csv"
    file = open(path)

    # print the first line of the file
    header_row = file.readline()

    # Get information about the fave pizza place
    uncle_fatihs = 0
    club_ilia = 0
    pizza_hut = 0

    # Fave burrito place
    guadalupe = 0
    quesada = 0

    for line in file:
        # fave pizza is in column 5 (4th ind)
        # a line is a string
        # convert the string to a list
        # split the line wherever a , is
        info = line.split(",")
        fave_pizza = info[4]
        fave_burrito = info[5]

        if fave_pizza == "Uncle Fatih's":
            uncle_fatihs += 1
        elif fave_pizza == "Club Ilia":
            club_ilia += 1
        elif fave_pizza == "Pizza Hut":
            pizza_hut += 1

        if fave_burrito == "Guadalupe (MBC)":
            guadalupe += 1
        elif fave_burrito == "Quesada (Cornerstone)":
            quesada += 1

    # Display Results
    print(f"Uncle Fatih's Votes: {uncle_fatihs}")
    print(f"Club Ilia votes: {club_ilia}")
    print(f"Pizza Hut votes: {pizza_hut}")

    # Display the most popular burrito place
    if guadalupe > quesada:
        print("Guadalupe is the most popular burrito place.")
    elif guadalupe == quesada:
        print("It's a tie! Guadalupe and Quesada both win!")
    else:
        print("Quesada is the most popular burrito place.")

    file.close()


if __name__ == "__main__":
    main()
