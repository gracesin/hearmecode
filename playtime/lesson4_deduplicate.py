# Challenge level: Beginner

# Scenario: You have two files containing a list of email addresses of people who attended your events.
#       File 1: People who attended your Film Screening event
#       https://github.com/shannonturner/python-lessons/blob/master/section_09_(functions)/film_screening_attendees.txt
#
#       File 2: People who attended your Happy hour
#       https://github.com/shannonturner/python-lessons/blob/master/section_09_(functions)/happy_hour_attendees.txt
#
def read_file(filename):
    with open(filename, "r") as text_file:
        text = text_file.read().split("\n")
    return text
    
# Note: You should create functions to accomplish your goals.
# Goal 1: You want to get a de-duplicated list of all of the people who have come to your events.
film = read_file("film_screening_attendees.txt")
happy = read_file("happy_hour_attendees.txt")
#print film
#print happy
all_p = happy
for f in film:
    if f not in all_p:
        all_p.append(f)
all_p.sort()
print all_p
# Goal 2: Who came to *both* your Film Screening and your Happy hour?
both = []
for h in happy:
    if h in film:
        both.append(h)
both.sort()
print both
