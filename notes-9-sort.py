# Intro to Sort
# Author: Dario
# 4 December

import helper_spotify

# Sorting Algorithms
# We'll implement selection sort in two ways
#     * implement basic version using the example from yesterday
#     * implement sort with songs based on YouTube views in descending order

def selection_sort(l: list[int], ascending=True) -> list[int]:
    """Sorts a given list using selection sort
    Params:
        l - list of numbers to sort
        ascending - True if sorting in ascending order
    Returns:
        a sorted list
    """
    num_items = len(l)

    # starting at the beginning of the list
    for i in range(num_items):
        candidate_num = l[i]
        candidate_index = i

        # check the rest of the list
        for j in range(i+1, num_items):
            if ascending:
                if l[j] < candidate_num:
                    candidate_num = l[j]
                    candidate_index = j
            else:
                if l[j] > candidate_num:
                    candidate_num = l[j]
                    candidate_index = j

        # swap the current number with the number at the
        # lowest index
        l[i], l[candidate_index] = l[candidate_index], l[i]

    return l

def sort_songs(songs: list[list[str]], col: int, ascending=True) -> list[list[str]]:
    """Sort a list of spotify songs in place

    Params:
        songs - list of songs
        col - column to sort
        ascending - will sort ascending by default

    Returns: sorted list"""
    # Use Selection Sort to sort songs
    num_songs = len(songs)

    for i in range(num_songs):
        # This value is the candidate
        candidate_val = helper_spotify.string_to_num(songs[i][col])
        candidate_idx = i

        # Check the rest of the list
        for j in range(i+1, num_songs):
            this_songs_val = helper_spotify.string_to_num(songs[j][col])
            if ascending:
                if this_songs_val < candidate_val:
                    candidate_val = this_songs_val
                    candidate_idx = j
            else:
                if this_songs_val > candidate_val:
                    candidate_val = this_songs_val
                    candidate_idx = j

        # Swap the candidate with the current index
        songs[i], songs[candidate_idx] = songs[candidate_idx], songs[i]

    return songs



if __name__ == "__main__":
    # Get a list of all songs from "Taylor Swift"
    taylors_songs = helper_spotify.songs_by_artist("data/spotify2024.csv", "Taylor Swift")
    # artist -> col 11
    sorted_ytview_songs = sort_songs(taylors_songs, 11, ascending=True)

    print("Taylor's Songs")
    print("---------------")
    for song in sorted_ytview_songs:
        print(song[0], "\t", song[11])
