x = 0
for i in range(len(s)):
    if s[i:].startswith('bob'):
        x+=1

print("Number of times bob occurs:", x)
