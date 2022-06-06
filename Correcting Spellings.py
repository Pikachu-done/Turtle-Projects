from textblob import TextBlob
words = ["Data sciene","Machin Learnin"]
corrected_words = []
for i in words:
    corrected_words.append(TextBlob(i)) #Doubt
print("Wrong Words are: ",words)
print("Corrected Words: ")
for i in corrected_words:
    print(i.correct(),end=" ") #What is End...?