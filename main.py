import nltk
sent = []
text = "One Dos. Dos Dos Tres. Cuatro"
tokens = nltk.word_tokenize(text)
sentences = 0
finalList = []
tmp = []
counts = dict()
for word in tokens:
    if(word != "."):
        sent.append(word)
        #print(word, sentences)
    if(word == "."):
        sentences += 1
        counts.clear()
        for word in sent:
            #print(sentences)
            if word in counts:
                counts[word] += 1
            else:
                counts[word] = 1
                #counts[word] = str(sentences)
        tmp.append(counts)
        tmp.append(sentences)
          
        #print(counts)
print(tmp)        
 
 
 
 
 
 
for i in range(len (tmp)):
    if (i %2 ==0):
        for key,val in tmp[0].items():
            print (key, ":", val, tmp[i+1])
    else: 
        continue
