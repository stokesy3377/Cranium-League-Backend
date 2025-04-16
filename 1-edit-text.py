with open('rawtext.txt', 'r') as file:
    lines = file.readlines()

with open('rawtext.txt', 'w') as file:
    
    for line in lines:
        parts = line.split(':', 2)
        if len(parts) > 2:
            file.write(':'.join(parts[2:]).strip() + '\n')
        else:
            file.write(line.strip() + '\n')
