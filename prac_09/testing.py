string = 'abcdef'
position = 1
print(string[:position+1])
print(string[position+1].upper())
print(string[position+2:])
new_string = string[:position+1] + string[position+1].upper() + string[position+2:]
print(new_string)

new_name = 'TheGreatnessOfOurGod'

new_name = new_name.replace(" ", "_").replace(".TXT", ".txt")
print(new_name)
position = 0
for char in new_name:
    if char.isupper():
        if position != 0:
            if new_name[position - 1] not in ['_', '(']:
                new_name = new_name[:position] + '_' + new_name[position:]
                position += 1
    if char == '_':
        new_name = new_name[:position + 1] + new_name[position + 1].upper() + new_name[position + 2:]

    position += 1

print(new_name)