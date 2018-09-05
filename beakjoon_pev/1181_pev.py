import operator

case = input()
case = int(case)
worddict = {}
while case > 0:
    word= input()
    worddict[word] = len(word)
    case= case-1
sorted_word = sorted(worddict.items(), key=operator.itemgetter(1,0))
for x in sorted_word:
    a = x
    print(a[0])