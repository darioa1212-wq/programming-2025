# Intro to Search
# Author: Dario
# 25 November

import csv

# Introduction to search algorithms
# Search for all songs by "Kendrick"
# Display all the YouTube and TikTok views
# Sort by either YouTube or TikTok views

def main():
    song_name_col = 0
    artist_col = 2
    yt_views_col = 11
    tiktok_views_col = 15
    artist = "Kendrick Lamar"

    kendrick_songs = []

    # open the file
    with open("data/spotify2024.csv") as f:
        # get rid of the header row
        _ = f.readline()

        # create a reader object
        r = csv.reader(f)

        # go through reader line by line
        for info in r:
            # if the current artist is "Kendrick"
            if info[artist_col] == artist:
                kendrick_songs.append(info)

        # Heading
        print(f"Track Name\t\tYouTube Views\t\tTikTok Views")
        for song in kendrick_songs:
            current_track = song[song_name_col]
            current_ytviews = song[yt_views_col]
            current_tiktokviews = song[tiktok_views_col]

            print(f"{current_track}\t\t{current_ytviews}\t\t{current_tiktokviews}")

        print(f"Number of Kendrick Songs: {len(kendrick_songs)}")

if __name__ == "__main__":
    main()
