import helper_spotify

def filter_non_explicit(songs: list[list[str]]) -> list[list[str]]:
    """Return only songs that are not explicit (helper filter)."""
    return [s for s in songs if s[10].strip().lower() not in ["true", "yes", "1"]]

def print_songs(songs: list[list[str]], name_col=0, col_to_show=None, label=""):
    """Helper function to display songs with optional numeric column."""
    print(label)
    print("-" * len(label))
    for song in songs:
        if col_to_show is not None:
            print(f"{song[name_col]} \t {song[col_to_show]}")
        else:
            print(f"{song[name_col]}")
    print("\n")

if __name__ == "__main__":

    ed_songs = helper_spotify.songs_by_artist("data/spotify2024.csv", "Ed Sheeran")
    ed_songs = filter_non_explicit(ed_songs)  # Only non-explicit
    print_songs(ed_songs, name_col=0, col_to_show=11, label="Task 1: Ed Sheeran Songs (YouTube Views)")

    sorted_yt_asc = helper_spotify.sort_songs(ed_songs, 11, ascending=True)
    print_songs(sorted_yt_asc, name_col=0, col_to_show=11, label="Task 2: Ed Sheeran Songs Sorted by YouTube Views (Ascending)")

    sorted_tt_desc = helper_spotify.sort_songs(ed_songs, 12, ascending=False)
    print_songs(sorted_tt_desc, name_col=0, col_to_show=12, label="Task 3: Ed Sheeran Songs Sorted by TikTok Views (Descending)")

    the_songs = helper_spotify.songs_by_track_name("data/spotify2024.csv", "the")
    the_songs = filter_non_explicit(the_songs)
    print_songs(the_songs, name_col=0, col_to_show=1, label='Task 4: Songs with "the" in track name (Non-Explicit)')

    sorted_tt_again = helper_spotify.sort_songs(sorted_tt_desc, 12, ascending=False)
    print_songs(sorted_tt_again, name_col=0, col_to_show=12, label="Task 5: Task 3 Results Re-Sorted by TikTok Views")
