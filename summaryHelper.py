# # Open the text file
# with open('/Users/bugrayildiz/PycharmProjects/SentimentAnalysis/outputshort.txt', 'r') as f:
#     # Read the contents of the file
#     text = f.read()
#
# # Specify the string to search for
# search_string = "POSITIVE"
#
# # Count the occurrences of the search string
# count = text.count(search_string)
#
# # Print the count
# print(f"The string '{search_string}' appears {count} times in the text.")

# import json
# import pandas as pd
#
# # Open the text file
# with open('/Users/bugrayildiz/PycharmProjects/SentimentAnalysis/sentanaloutput.txt', 'r') as f:
#     # Read the contents of the file
#     text = f.read()
#
# # Convert the text to a dictionary
# data = {"text": text}
#
# # Convert the dictionary to a json file
# with open("data.json", "w") as json_file:
#     json.dump(data, json_file)
#
# # Load the json file into a pandas dataframe
# df = pd.read_json("data.json")
#
# # Print the dataframe
# print(df)



import json
import pandas as pd

# Open the text file
with open('sentanaloutput.txt', 'r') as f:
    # Read the contents of the file
    text = f.read()

# Convert the text to a dictionary
data = {"text": text}

# Convert the dictionary to a json file
with open("data.json", "w") as json_file:
    json.dump(data, json_file)