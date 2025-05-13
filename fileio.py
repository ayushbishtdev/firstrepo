f = open ("poem.txt")

content = f.read()

if ("Python" in content):
    print("The word python is present in the poem.")
else:
    print("The word python is not present in the poem.")
    
f.close()