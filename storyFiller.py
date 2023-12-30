# Opens the file in read mode, allowing manipulations with the file using the 'f' variable within this block
with open("story.txt", "r") as f:
    # Reads the content of the file into the 'story' variable and prints it
    story = f.read()
    print("Original Story:\n", story)

# 'set()' is used to store unique words, and 'words' is initialized to store the placeholders
words = set()
start_of_word = -1

# Define the start and end markers for placeholders
target_start = "<"
target_end = ">"

# Loop through each character in the story to find and extract placeholders
for i, char in enumerate(story):
    if char == target_start:
        # Records the start index of a placeholder
        start_of_word = i

    if char == target_end and start_of_word != -1:
        # Extracts the placeholder and adds it to the 'words' set
        word = story[start_of_word: i + 1]
        words.add(word)
        start_of_word = -1

# Dictionary to store user-provided answers for each placeholder
answers = {}

# Prompt the user to input words for each placeholder
for word in words:
    answer = input("Enter the word for" + word + ": ")
    answers[word] = answer

# Replace placeholders in the story with user-provided answers
for word in words:
    story = story.replace(word, answers[word])

# Print the modified story with user-inputted words
print("\nModified Story:\n", story)
