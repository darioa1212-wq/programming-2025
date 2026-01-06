# Numbers and Operations
# Author: Ubial
# 5 November 2025

# Create an algorithm to gather
# data to find the most popular
# bubble tea place around us

import os

NUM_VOTERS = 10

# Version 1
def vote_listed_choices():
    """Display all voting choices
    5 users vote for their choice
    Results will be printed"""
    CHOICES = [
        "A. CoCo",
        "B. Chatime",
        "C. BUBBLE WAFFEL",
        "D. gong cha"
    ]

    # Buckets to hold all the votes
    coco = 0
    chatime = 0
    bubble_waffel = 0
    gong_cha = 0
    spoiled_votes = 0

    for _ in range(NUM_VOTERS):
        # Clear the screen for the voter
        os.system("clear")
        print("Vote for your favourite from the list.")
        print("Give the letter of your choice.")
        for choice in CHOICES:
            print(choice)

        vote = input("Your vote: ").lower().strip(",.?! ")

        # Add their vote to a running tally
        if vote == "a":
            coco += 1
        elif vote == "b":
            chatime += 1
        elif vote == "c":
            bubble_waffel += 1
        elif vote == "d":
            gong_cha += 1
        else:
            spoiled_votes += 1

    # Show the scores of coco, ..., etc.
    print(f"CoCo votes: {coco}")
    print(f"Chatime votes: {chatime}")
    print(f"BUBBLE WAFFEL votes: {bubble_waffel}")
    print(f"Gong Cha votes: {gong_cha}")
    print(f"Spoiled votes: {spoiled_votes}")

    # Give score as a percentage
    coco_percentage = coco / (coco + chatime + bubble_waffel + gong_cha + spoiled_votes)
    print(f"CoCo Percentage: {coco_percentage * 100}%")
    chatime_percentage = chatime / (coco + chatime + bubble_waffel + gong_cha + spoiled_votes)
    print(f"Chatime Percentage: {chatime_percentage * 100}%")
    bubble_waffel_percentage = bubble_waffel / (coco + chatime + bubble_waffel + gong_cha + spoiled_votes)
    print(f"Bubble Waffel Percentage: {bubble_waffel_percentage * 100}%")
    gong_cha_percentage = gong_cha / (coco + chatime + bubble_waffel + gong_cha + spoiled_votes)
    print(f"Gong Cha Percentage: {gong_cha_percentage * 100}%")

# Version 2
def vote_open_choice():
    """Keeps track dynamically of user's choice.
    Note: choices must match text exactly (case is not sensitive)"""

    votes = {}          # holds vote information    key     -> value
                        #                           place   -> num votes

    for _ in range(NUM_VOTERS):
        # Ask the user what their fave
        os.system("clear")
        cur_vote = input("What's your favourite local bubbble tea cafe? ").lower().strip(",.?! ")

        # Checks if current place is in the votes dictionary
        # If it doesn't exist, initialize the key-value pair
        if cur_vote not in votes:
            votes[cur_vote] = 1
        else:
            votes[cur_vote] += 1

    # Print the results
    print("-------------------------------------")
    print("Results:")

    # By default, iterating over a dictionary gives you the keys
    for place in votes:
        # Print the raw score and percentage for each key in the dictionary
        percentage = votes[place] / NUM_VOTERS * 100

        print(f"{place.capitalize()} votes: {votes[place]} | percentage: {percentage}% of the vote")

    print("-------------------------------------")

def chip_rater():
    """Help gather data about chip crispness
    and quality."""
    # Create a list of questions
    questions = [
        "How crispy is the chip out of 5? 0 is mushy, 5 is super crisp.",
        "How would you rate the taste out of 5? 0 is unpalatable, 5 is the most delicious thing you've ever eaten.",
        "How fresh would you rate the chip out of 5? 0 is stale, 5 is super fresh.",
        "How would you rate the size of the chip? 0 is terrible, 5 is perfect."
    ]

    # Rating total
    total = 0

    # Give user instructions
    print("Take one chip from the bag.")
    print("Eat it mindfully.")
    print("Give your rating.")

    # Ask the user questions
    for question in questions:
        print(question)
        # For each question, get their rating
        # out of five
        rating = int(input("Your rating: ").strip(",.?! "))

        # Update total
        total += rating

    # Print the average rating out of five
    average = total / len(questions)

    print(f"The average rating for this chip is: {average}.")


def main():
    # vote_listed_choices()
    # chip_rater()
    vote_open_choice()

if __name__ == "__main__":
    main()
