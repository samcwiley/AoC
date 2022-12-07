with open('inputs6.txt') as f:
    line = ''.join([char for char in f])
def findStart(signal, length):
    for i in range(length,len(signal)):
        if len(signal[i-length:i]) == len(set(signal[i-length:i])):
            return(i)
print(f'The packet starts at character {findStart(line,4)}. The message starts at {findStart(line,14)}')