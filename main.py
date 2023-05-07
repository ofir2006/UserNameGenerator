with open("users.txt",'r') as f:
    for line in f.readlines():
        firstname = line.strip().split(' ')[0]
        lastname = line.strip().split(' ')[1]
        print(firstname[0] + lastname)
        print(firstname + lastname[0])
        print(firstname + "." + lastname)
        print(firstname[0]+ "." + lastname)
