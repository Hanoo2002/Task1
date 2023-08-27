text = input("Enter Text:")
index = 0
i = 0
letters = 0
words = 1
sentences = 0

for i in range(len(text)):
    if (text[i].isalpha()):
        letters += 1
    elif (text[i] == ' ' and text[i+1].isalpha()):
        words += 1
    elif (text[i] == '?' or text[i] == '!' or text[i] == '.'):
        sentences += 1


print(str(sentences) + " " + str(words) +" "+str(letters))      
L = float(letters / words * 100)
S = float(sentences / words * 100)
index = round((float)(0.0588 * L - 0.296 * S - 15.8))
if (index >= 16):
        print('Grade 16+')
elif (index < 1):
        print('Before Grade 1')
else:
        print('Grade ', index)