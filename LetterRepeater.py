def LetterRepeater(times,word) :
    word1=''
    for letters in word:
        word1 += letters * times
    print(word1)

word=input('Write down the word you want to dublicate the letters :   ')
times=int(input('How many times you want to replicate the letters ?    '))
LetterRepeater(times,word)



