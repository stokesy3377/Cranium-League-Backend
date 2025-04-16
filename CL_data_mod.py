import re

# List of participants
participants = ['AT', 'DA', 'IJ', 'MR', 'MK', 'NK', 'RK', 'SR', 'VS']

# Initialize a dictionary for scores
scores = {participant: -10000 for participant in participants}

# Define regex pattern to extract scores
pattern = r'\b\d+\b'

# Function to extract team name from a line
def extract_team_name(line):
    last_space_index = line.rfind(' ')
    if last_space_index == -1:
        return line.strip()
    return line[last_space_index + 1:].strip()

# Get the winning team from user input
winning_team = input('Which team won today?: ').strip()

# Open the file and read line by line
with open('rawtext.txt', 'r') as file:
    for line in file:
        line = line.strip()
        
        # Iterate over participants
        for participant in participants:
            # Check if line starts with the participant's initials
            if line.startswith(participant):
                # Extract the score using regex
                match = re.search(pattern, line)
                if match:
                    score = int(match.group())
                    
                    # Negate the score if the team does not match the winning team
                    team_name = extract_team_name(line)
                    if team_name != winning_team:
                        score = -1 * score
                    
                    # Update the participant's score
                    scores[participant] = score

# Print the scores
for participant, score in scores.items():
    print(f"{participant}: {score}")

A=B=C=D=E=F=G=H=I=J=K=L=-10000
lst1 = [A,B,C,D,E,F,G,H,I,J,K,L]

x=0

for parti, scor in scores.items():
    lst1[x] = scor
    x+=1

print(lst1)    