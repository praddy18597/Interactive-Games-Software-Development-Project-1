## string concatenation (Aka how to put strings together)
## suppose we want to create a stirng that says "Subscribe to_____"
# youtuber = "Pradeep Kamble" # some string variable

## few ways to do this
# print("Subscribe to " + youtuber)
# print(f"Subscribe to {youtuber}")

adj = input("Adjective: ")
verb1 = input("Verb: ")
verb2 = input("Verb: ")
famous_person = input("Famous Person: ")

madlib = f"Computer Programming is so {adj}! It makes me so excited all the time beacause \
I love to {verb1}. Stay hydrated and {verb2} like you are {famous_person}!"

print(madlib)