ex = '''$ cd /
$ ls
dir a
14848514 b.txt
8504156 c.dat
dir d
$ cd a
$ ls
dir e
29116 f
2557 g
62596 h.lst
$ cd e
$ ls
584 i
$ cd ..
$ cd ..
$ cd d
$ ls
4060174 j
8033020 d.log
5626152 d.ext
7214296 k'''

files = {}
path = []

def nested_set(dic, keys, value, create_missing=True): #allegedly adds to dictionary given a list of indices (keys)
    d = dic
    #print(keys)
    for key in keys[:-1]:
        if key in d:
            d = d[key]
        elif create_missing:
            d = d.setdefault(key, {})
        else:
            return dic
    if keys[-1] in d or create_missing:
        d[keys[-1]] = value
    return dic

'''test = {'A':{'B':1}}
newDirectoryName = 'C'
path = ['A']
newPath = path
newPath.append(newDirectoryName)
print(newPath)
test = nested_set(test, newPath, {}, True)
print(test)'''

def findSize(dict): #recursively gets the size of all of the files inside the dictionary
    total = 0
    for key in dict:
        if dict[key].isnumeric():
            total += dict[key]
        if isinstance(dict[key],dict):
            total += findSize(dict[key])
    return total



for instruction in ex.split('\n'):
    print(f'Path is currently: {path}')
    if instruction.startswith('$ cd'): 
        if instruction.split()[2] == '..': #gets rid of outermost folder in path
            path.pop()
        else:
            path.append(instruction.split()[2]) #adds new folder name to path list
    if instruction.startswith('$ ls'):
        pass
    if instruction.startswith('dir'): #adds empty directory
        newDirectoryName = instruction.split()[1]
        newPath = path
        newPath.append(newDirectoryName)
        files = nested_set(files, newPath, {}, create_missing=True) 
    if instruction[0].isnumeric(): #adds {fileName:fileSize} to current directory
        fileName = instruction.split()[1]
        fileSize = instruction.split()[0]
        newPath = path
        newPath.append(fileName)
        files = nested_set(files, newPath, fileSize, create_missing=True)

print(findSize(files))