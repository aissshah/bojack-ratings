import csv
import math
import pandas as pd
from matplotlib import pyplot as plt
import seaborn as sns

df = pd.read_csv('bojack/bojack_ratingsedit.csv')

def dictionary():
    global highest_index_number, lowest_index_number, index_number
    bojack_ratings = open('bojack/bojack_ratings.csv', 'r')
    reader = csv.reader(bojack_ratings)
    next(reader)
    episodes_dict = {}
    episode_names = []

    for row in reader:
        episodes_dict[row[0]] = {'length': row[1], 'rating': row[2], 'year': row[3], 'month': row[4],
                                 'date': row[5]}
        episode = (row[0])
        episode_names.append(episode)
    #This is just to check that the above code works correctly
    #print(episodes_dict)

    def options():
        #This is the beginning of the terminal output
        option = int(input('What do you want to find out about the show Bojack Horseman?'
                           ' \n 1. Information about a specific episode \n 2. Highest rated episode '
                           '\n 3. Lowest rated episode \n 4. Longest episode \n 5. Shortest episode '
                           '\n 6. Pretty graphs, please \n 7. CSV Output \n 8. Quit\n'))
        if option == 1:
            # can ask people what episode they're interested in and what they want to know.
            # If episode doesnt exist e.g. S1E20, then will get a message "episode not found"
            episode_of_choice = input('What episode do you want to find more information on? S_E_\n')
            if episode_of_choice not in episodes_dict:
                print('\nEpisode not found\n')
                options()
            else:
                fact_of_choice = input('What do you want to find out? Options: length/rating/date\n')
                if fact_of_choice == 'length':
                    length = float(episodes_dict[episode_of_choice][fact_of_choice])
                    seconds_remaining = math.ceil(100*(float(length) - int(length)))
                    print('\nThis episode is', int(length),
                            'minutes and', seconds_remaining, 'seconds long\n')
                elif fact_of_choice == 'rating':
                    print('\nThis episode has a rating of', episodes_dict[episode_of_choice][fact_of_choice], '\n')
                elif fact_of_choice == 'date':
                    print('\nThis episode first aired on', episodes_dict[episode_of_choice]['date'],
                            episodes_dict[episode_of_choice]['month'], episodes_dict[episode_of_choice]['year'],
                            '\n')
                else:
                    print("\nInformation not found, sorry\n")
                options()
        elif option == 2:
            #highest rated episode
            highest_rated = ['0', ]
            for episode in episodes_dict:
                if float(episodes_dict[episode]['rating']) > float(highest_rated[0]):
                    highest_rated.append(float(episodes_dict[episode]['rating']))
                    highest_rated.pop(0)
            for highest_rated_episode in episodes_dict:
                if float(highest_rated[0]) == float(episodes_dict[highest_rated_episode]['rating']):
                    index_number = int(list(episodes_dict).index(highest_rated_episode))
            print('\nThe highest rated episode is', episode_names[index_number], 'with a rating of',
                  highest_rated[0], '\n')
            options()
        elif option == 3:
            #lowest rated episode
            lowest_rated = ['10', ]
            for episode in episodes_dict:
                if float(episodes_dict[episode]['rating']) < float(lowest_rated[0]):
                    lowest_rated.append(float(episodes_dict[episode]['rating']))
                    lowest_rated.pop(0)
            for lowest_rated_episode in episodes_dict:
                if float(lowest_rated[0]) == float(episodes_dict[lowest_rated_episode]['rating']):
                    index_number = int(list(episodes_dict).index(lowest_rated_episode))
            print('\nThe lowest rated episode is', episode_names[index_number], 'with a rating of',
                  lowest_rated[0], '\n')
            options()
        elif option == 4:
            #longest episode
            longest = ['0', ]
            for episode in episodes_dict:
                if float(episodes_dict[episode]['length']) > float(longest[0]):
                    longest.append(float(episodes_dict[episode]['length']))
                    longest.pop(0)
            for longest_episode in episodes_dict:
                if float(longest[0]) == float(episodes_dict[longest_episode]['length']):
                    index_number = int(list(episodes_dict).index(longest_episode))
            remaining_seconds = math.ceil(100*(float(longest[0]) - int(longest[0])))
            print('\nThe longest  episode is', episode_names[index_number], 'which is',
                  int(longest[0]), 'minutes', remaining_seconds, 'seconds long\n')
            options()
        elif option == 5:
            #shortest episode
            shortest = ['30', ]
            for episode in episodes_dict:
                if float(episodes_dict[episode]['length']) < float(shortest[0]):
                    shortest.append(float(episodes_dict[episode]['length']))
                    shortest.pop(0)
            for shortest_episode in episodes_dict:
                if float(shortest[0]) == float(episodes_dict[shortest_episode]['length']):
                    index_number = int(list(episodes_dict).index(shortest_episode))
            remaining_seconds = math.ceil(100*(float(shortest[0]) - int(shortest[0])))
            print('\nThe shortest  episode is', episode_names[index_number], 'which is',
                  int(shortest[0]), 'minutes', remaining_seconds, 'seconds long\n')
            options()
        elif option == 6:
            sns.relplot(x="Episode", y="Rating", hue="Season", kind="line", legend="full", data=df)
            plt.show()
            options()
        elif option == 7:
            with open('bojack/bojack_ratings.csv', 'r') as csv_file:
                spreadsheet = csv.DictReader(csv_file)
                ratingD = []
                for column in spreadsheet:
                    episode_rating = column['rating']
                    ratingD.append(episode_rating)
            with open('bojack/bojack_ratings.csv', 'r') as csv_file:
                spreadsheet = csv.DictReader(csv_file)
                lengthD = []
                for column in spreadsheet:
                    episode_length = column['length']
                    lengthD.append(episode_length)
            highest_rating = max(ratingD)
            lowest_rating = min(ratingD)
            shortest = min(lengthD)
            longest = max(lengthD)
            with open('bojack/bojack_results.csv', 'w+') as csv_file:
                csv_file.write(highest_rating)
                csv_file.write(lowest_rating)
                csv_file.write(shortest)
                csv_file.write(longest)
            options()
        elif option == 8:
            print('\nThank you!')
        else:
            print('\nOption not available\n')
            options()
    options()
    

dictionary()



