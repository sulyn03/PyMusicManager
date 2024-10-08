import random


# Function to read lines from text file.
def read_lines():
    with open('musicInfo_21032255.txt', 'r', encoding='utf-8-sig') as file:
        lines = file.readlines()
    return lines


# Function to print song information in a neat manner.
def print_album_details(line):
    # Strips any white space and splits each line into a list of strings using the / as a separator.
    category = line.strip().split('/')
    print((f"\nAlbum: {category[0]}"
           f"\nArtist: {category[1]}"
           f"\nSong: {category[2]}"
           f"\nComposers: {category[3]}"
           f"\nGenre: {category[4]}"
           f"\nRelease date: {category[5]}"
           f"\nFormat: {category[6]}"))


# Function to prompt users if they would like to return to the main menu.
def return_main():
    while True:
        confirm = input("Would you like to return to the main menu? (Y/N): ")
        if confirm.upper() == "Y":
            main()
            break
        elif confirm.upper() == "N":
            print("Exiting program...")
            break
        else:
            print("Invalid choice. Please enter Y or N.")


# Function to add song to the text file.
def add_song():
    continue_adding = True
    while continue_adding:
        print("Add a song by entering the following information.")

        # Creates a list containing questions for the user.
        questions = ["Enter album name: ", "Enter artist name: ", "Enter song title: ", "Enter composer name: ",
                     "Enter genre: ", "Enter release date (eg: 22 March 2023): ",
                     "Enter album format (physical/digital): "]

        # Empty list to hold answers.
        answers = []

        # Loops through the questions in the list to prompt the users.
        for question in questions:
            while True:
                if question == "Enter album format (physical/digital): ":
                    answer = input(question).title()
                    # Error message when album format is not Physical or Digital.
                    if answer not in ["Physical", "Digital"]:
                        print("Invalid album format. Please enter either 'physical' or 'digital'.")
                        continue
                else:
                    answer = input(question)

                # Error message when answers are blank.
                if not answer:
                    print("Answers cannot be blank. Please enter a valid input.")
                    continue

                # Adds the user's input to the answer list
                else:
                    answers.append(answer)
                    break

        # Combines user input into a single string with / as a separator.
        song_info = '/'.join(answers) + '\n'

        # Tries to open the file in append mode and writes the new song into the file.
        try:
            with open('musicInfo_21032255.txt', 'a', encoding='utf-8-sig') as file:
                file.write(song_info)

        # If an error occurs, display an error message to the user.
        except IOError:
            print("Error writing to file. Please check file permissions and try again.")

        print("Song successfully added!")

        # Calls the read_lines function and sorts it alphabetically (uppercase followed by lowercase).
        lines = read_lines()
        lines.sort()

        # Tries to open the file in write mode and writes the lines that were sorted back into the file.
        try:
            with open('musicInfo_21032255.txt', 'w', encoding='utf-8-sig') as file:
                for line in lines:
                    file.write(line)
        except IOError:
            print("Error writing to file. Please check file permissions and try again.")

        # Loop to prompt users if they would like to add a new song.
        while True:
            confirm = input("Would you like to add another song? (Y/N): ")
            if confirm.upper() == "Y":
                break
            elif confirm.upper() == "N":
                continue_adding = False
                print("Returning to main menu...")
                main()
                break
            else:
                print("Invalid choice. Please enter Y or N.")


# Function to delete song from the text file.
def delete_song():
    continue_deleting = True

    while continue_deleting:
        lines = read_lines()

        # Prompts the user for the song title to be deleted.
        song_title = input("Enter song title to be deleted: ")

        # Opens the text file in write mode.
        with open('musicInfo_21032255.txt', 'w', encoding='utf-8-sig') as file:
            song_found = False
            for line in lines:
                category = line.strip().split('/')
                # Checks if user input matches the song title in the text file
                if song_title.lower() == category[2].lower():
                    song_found = True
                    # Calls the print_album_details function to print the song information in a neat format.
                    print_album_details(line)

                    # Confirms with the user if the user would like to delete the song.
                    confirm = input(f"Would you like to delete {song_title}? (Y/N): ")
                    if confirm.upper() == "Y":
                        print("Song has been successfully deleted.")
                        continue
                    elif confirm.upper() == "N":
                        print("Action cancelled")
                        file.write(line)
                        continue
                else:
                    file.write(line)
            if not song_found:
                print("Song could not be found.")

        while True:
            confirm = input("Would you like to delete another song? (Y/N): ")
            if confirm.upper() == "Y":
                break
            elif confirm.upper() == "N":
                continue_deleting = False
                print("Returning to main menu...")
                main()
                break
            else:
                print("Invalid choice. Please enter Y or N.")


# Function to search for song based on album or artist or song title.
def search():
    results = []
    while True:
        # Prompt users to select search criteria.
        print("Search by: \n[1] Album \n[2] Artist \n[3] Song Title")
        user_input = input("Enter choice: ")

        # Ensures user enters either 1, 2 or 3.
        if user_input not in ['1', '2', '3']:
            print("Invalid choice. Please enter a number between 1 and 3.")
            continue

        # Search for album
        if user_input == "1":
            user_search = input("Please enter the name of the album: ")
            lines = read_lines()

            # Search for the album and appends results to the line list.
            results = []
            for line in lines:
                album_info = line.strip().split('/')
                # User's input of the album name has to match the album name in the text file.
                album_name = album_info[0]
                if user_search.lower() in album_name.lower():
                    results.append(line)

            # If results found, display the results with a number at the side in order.
            if results:
                print(f"Search results for {user_search}:")
                for i, result in enumerate(results):
                    print(f"[{i + 1}] {result.strip()}")

            else:
                print("Album not found")
                continue

        # Search for artist.
        elif user_input == '2':
            user_search = input("Please enter the name of the artist: ")
            lines = read_lines()

            results = []
            for line in lines:
                album_info = line.strip().split('/')
                artist = album_info[1]
                if user_search.lower() in artist.lower():
                    results.append(line)

            if results:
                print(f"Search results for {user_search}:")
                for i, result in enumerate(results):
                    print(f"[{i + 1}] {result.strip()}")

            else:
                print("Artist not found")
                continue

        # Search for song title.
        elif user_input == '3':
            user_search = input("Please enter the name of the song: ")
            lines = read_lines()

            results = []
            for line in lines:
                album_info = line.strip().split('/')
                song_title = album_info[2]
                if user_search.lower() in song_title.lower():
                    results.append(line)

            if results:
                print(f"Search results for {user_search}:")
                for i, result in enumerate(results):
                    print(f"[{i + 1}] {result.strip()}")

            else:
                print("Song not found")
                continue

        # If there are results from the search, pass them to update_info function
        if results:
            update_info(results)
        break


# Function to update song information into text file.
def update_info(results):
    while True:
        try:
            # Prompts user to select a song information to update based on the results list.
            user_input = int(input("Select the song that you would like to update: "))

            # Checks to see if the user input is valid.
            if 1 <= user_input <= len(results):
                # Splits the string from the selected result using / as the separator into a list.
                category = results[user_input - 1].strip().split('/')
                print(f"\nSong information as shown below:")
                print_album_details(results[user_input - 1])

                # Loop to prompt users to select a category to update.
                for i in range(len(results)):
                    data = results[i].strip().split('/')

                    # Checks if the selected song matches the song in the text file.
                    # This ensures that the album, artist and song title are the same for accuracy.
                    if data[2] == category[2] and data[1] == category[1] and data[0] == category[0]:
                        print("Which category would you like to update?"
                              "\n[1] Album"
                              "\n[2] Artist"
                              "\n[3] Song"
                              "\n[4] Composers"
                              "\n[5] Genre"
                              "\n[6] Release date"
                              "\n[7] Format")

                        while True:
                            try:
                                # Prompts user to select a category.
                                category_choice = int(input("Enter choice: "))

                                # Checks if user input is valid.
                                if 1 <= category_choice <= len(category):
                                    # Prints the existing information and prompts user to enter updated info.
                                    print(f"Existing information: {category[category_choice - 1]}")
                                    edited_info = input(f"\nEnter updated information: ")
                                    category[category_choice - 1] = edited_info

                                    # Prints the information with the updated changes.
                                    print(f"Updated info")
                                    print_album_details('/'.join(category))
                                else:
                                    raise ValueError
                                break
                            # Prints error message when user enters a number beyond the number of categories.
                            except ValueError:
                                print("Invalid choice. Please enter a number between 1 and", len(category))

                lines = read_lines()
                with open('musicInfo_21032255.txt', 'w', encoding='utf-8-sig') as file:
                    for line in lines:
                        tf_category = line.strip().split('/')

                        # Calculates number of matching elements between the song in the file and the modified song.
                        matches = sum(x == y for x, y in zip(tf_category, category))

                        # If 6 of the elements match, the song will be updated in the text file
                        # To prevent modifying the wrong song if for example the artist and song have the same names
                        if matches >= 6:
                            # Update the song information in the text file using the modified list.
                            tf_category[0] = category[0]
                            tf_category[1] = category[1]
                            tf_category[2] = category[2]
                            tf_category[3] = category[3]
                            tf_category[4] = category[4]
                            tf_category[5] = category[5]
                            tf_category[6] = category[6]

                            # Join the elements of the updated split line with / as a separator
                            file.write('/'.join(tf_category) + '\n')
                            print("Information updated successfully.")
                        # Else rewrite the original lines to the text file.
                        else:
                            file.write(line)
                    break
            else:
                raise ValueError
        # Prints error message when user enters a number beyond the number of results provided.
        except ValueError:
            print("Invalid choice. Please enter a number between 1 and", len(results))


# Function to display all songs from text file by their respective headers.
def display():
    lines = read_lines()
    # Create a list of column headers
    headers = ["Album", "Artist", "Song Title", "Composer", "Genre", "Release Date", "Format"]

    # Create a list of lists to hold the information for each song.
    rows = []
    for line in lines:
        line = line.strip()
        fields = line.split("/")
        # Add the fields to the list of rows.
        rows.append(fields)

    # Transpose the rows list to get a list of columns.
    columns = []
    for i in range(len(rows[0])):
        column = []
        for row in rows:
            column.append(row[i])
        columns.append(column)

    # Determine the maximum length of each column.
    max_lengths = []
    for column in columns:
        max_length = 0
        for value in column:
            if len(value) > max_length:
                max_length = len(value)
        max_lengths.append(max_length)

    # Print the table header.
    for i in range(len(headers)):
        header = headers[i]
        max_length = max_lengths[i]
        # Left justify and pad the header to the maximum length for the column.
        padded_header = header.ljust(max_length)
        print(padded_header, end="  ")

    # Print the dotted line separator.
    total_length = sum(max_lengths) + (len(max_lengths) - 1) * 2
    print("\n" + "-" * total_length)

    # Print the table rows.
    for row in rows:
        for i in range(len(row)):
            value = row[i]
            max_length = max_lengths[i]
            padded_value = value.ljust(max_length)
            print(padded_value, end="  ")
        print()


# Function to generate a random playlist of 10 songs.
def generate_playlist():
    while True:
        songs = read_lines()

        # Shuffles the songs list to randomise the order.
        random.shuffle(songs)

        print("Random Playlist:")

        # Print the first 10 songs in the shuffled list.
        count = 1
        for song in songs[:10]:
            print(f"Song {count}", end=' ')
            print_album_details(song)
            print()
            count += 1

        # Ask the user if they want to generate another playlist
        confirm = input("Would you like to generate another playlist? (Y/N):")
        if confirm.upper() == "Y":
            continue
        elif confirm.upper() == "N":
            break
        else:
            print("Invalid choice. Please enter Y or N.")


# Function to prompt users to exit the program.
def exit_program():
    while True:
        confirm = input("Would you like to exit the program?"
                        "\nChanges made will be saved."
                        "\nEnter (Y/N): ")
        # Exits program
        if confirm.upper() == "Y":
            print("Exiting program...")
            exit(1)
        # Returns to main menu
        elif confirm.upper() == "N":
            main()
        else:
            print("Invalid choice. Please enter Y or N.")


# Function for the main menu that prompts user to select the action.
def main():
    print("Please choose an action by entering the corresponding number:"
          "\n[1] Add songs"
          "\n[2] Delete songs"
          "\n[3] Update/Edit information"
          "\n[4] Display"
          "\n[5] Generate playlist"
          "\n[6] Exit")
    user_input = input("Enter choice: ")

    # Checking the user input and executing the corresponding function
    if user_input == "1":
        add_song()
    elif user_input == "2":
        delete_song()
    elif user_input == "3":
        search()
        return_main()
    elif user_input == "4":
        display()
        return_main()
    elif user_input == "5":
        generate_playlist()
        return_main()
    elif user_input == "6":
        exit_program()


# Calls the main function.
main()
