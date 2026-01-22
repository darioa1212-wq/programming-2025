# CSV File Prob
# Author: Dario
# 20 November

def main():
    # Open file

    with open("data/sfu_best_cmpt120.csv") as f:
        # remove first line from filestream
        _ = f.readline()

        # fave healthy food
        natures = 0
        chopped = 0
        subway = 0
        veggie = 0
        steves = 0

        for line in f:
            # get vote
            info = line.split(",")
            fave_healthy_food = info[-1].lower().strip()

            # add to bucket
            if fave_healthy_food == "nature's garden":
                natures += 1
            elif fave_healthy_food == "chopped leaf":
                chopped += 1

            # print(line)

        print("----------------------")
        print("Results: ")
        print(f"Nature's Garden: {natures} votes")
        print(f"Chopped Leaf: {chopped} votes")
        print("----------------------")

if __name__ == "__main__":
    main()
