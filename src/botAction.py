getKeys = open('../keys/keys.txt', 'r')
display_keys = getKeys.read()

for line in display_keys:
    print(line, end='')

getKeys.close()