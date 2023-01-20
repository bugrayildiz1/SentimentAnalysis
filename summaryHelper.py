# Open the text file
with open('/Users/bugrayildiz/PycharmProjects/SentimentAnalysis/outputshort.txt', 'r') as f:
    # Read the contents of the file
    text = f.read()

# Specify the string to search for
search_string = "POSITIVE"

# Count the occurrences of the search string
count = text.count(search_string)

# Print the count
print(f"The string '{search_string}' appears {count} times in the text.")