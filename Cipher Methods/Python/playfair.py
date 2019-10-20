def getPosition(val,key_matrix):
    for i in range(5):
        for j in range(5):
            if key_matrix[i][j] == val:
                return i,j

#text = input("Enter the plain text\n")
#key = input("Enter the key\n")

text = "INSTRUMENTS"
key = "MONARCHY"

key += "ABCDEFGHIKLMNOPQRSTUVWXYZ"


key_matrix = []
key_dict = {}
for i in range(26):
    key_dict[chr(65+i)] = 0

key_index = 0
for i in range(5):
    temp = []
    for j in range(5):
        while(key_dict[key[key_index]] == 1):
            key_index += 1
        key_dict[key[key_index]] = 1
        temp.append(key[key_index])
        key_index+=1
    key_matrix.append(temp)

if(len(text) % 2 != 0):
    text += "Z"

encryptedText = ""

for i in range(0,len(text),2):
    if text[i] == 'J':
        text[i] = 'I'
    if text[i+1] == 'J':
        text[i+1] = 'I'    
    x1,y1 = getPosition(text[i],key_matrix)
    x2,y2 = getPosition(text[i+1],key_matrix)

    if x1 == x2:
        encryptedText += key_matrix[x1][(y1+1) % 5]
        encryptedText += key_matrix[x2][(y2+1) % 5]
    elif y1 == y2:
        encryptedText += key_matrix[(x1+1) % 5][y1]
        encryptedText += key_matrix[(x2+1) % 5][y2]
    else:
        encryptedText += key_matrix[x1][y2]
        encryptedText += key_matrix[x2][y1]

print(encryptedText)

decryptedText = ""

for i in range(0,len(encryptedText),2):
    
    x1,y1 = getPosition(encryptedText[i],key_matrix)
    x2,y2 = getPosition(encryptedText[i+1],key_matrix)

    if x1 == x2:
        decryptedText += key_matrix[x1][(y1-1) % 5]
        decryptedText += key_matrix[x2][(y2-1) % 5]
    elif y1 == y2:
        decryptedText += key_matrix[(x1-1) % 5][y1]
        decryptedText += key_matrix[(x2-1) % 5][y2]
    else:
        decryptedText += key_matrix[x1][y2]
        decryptedText += key_matrix[x2][y1]

print(decryptedText)
