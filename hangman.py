import random
from words import words
import time
def play():
    # name= input("hello what is your name? \n")
    # print('hello '+ name + ' welcome to HANGMAN. LEts Play!!!!!! \n')
    # print("GAME STARTS NOW \n GOOD LUCK!!!!\n")
    
    HANGMAN = ['''
               +---+
                   |
                   |
                   |
                  ===''', '''
               +---+
               O   |
                   |
                   |
                  ===''', '''
               +---+
               O   |
               |   |
                   |
                  ===''', '''
               +---+
               O   |
              /|   |
                   |
                  ===''', '''
               +---+
               O   |
              /|\  |
                   |
                  ===''', '''
               +---+
               O   |
              /|\  |
              /    |
                  ===''', '''
               +---+
               O   |
              /|\  |
              / \  |
                  ===''']

    # GET RANDOM WORDS FROM words.py AND PRINT IT IN UPPER CASE
    # def get_word(words):
    #         word=random.choice(words)
    #         return word.upper()

    a=random.choice(words)
    word=a.upper()
    # print(word)

    #DASH FOR THE RANDOM WORD
    dashed_words= '_ ' * len(word)
    print(dashed_words)
    print(word)

    chances=len(HANGMAN)-1

    #wrong guess count
    wrong_guess=0

    #guessed word
    guessed_words=[]

    #logic
    while (dashed_words.replace(" ", "")!=word and wrong_guess<chances):
        print(HANGMAN[wrong_guess])
        guess=input("enter your guess word:")
        guess=guess.upper()

        if guess not in word:
            print('incorrect guess')
            wrong_guess=wrong_guess+1

        if guess in guessed_words:
            print('you have already guessed that word')
            wrong_guess=wrong_guess-1
        else:
            guessed_words.append(guess)
            for i in range(0,len(word)):
                if word[i]==guess:
                    dashed_words=dashed_words[0:2*i]+guess+dashed_words[2*i+1:]
        print("you have guessed the following words: ",guessed_words)
        if(dashed_words.replace(" ", "")==word):
            print("congratulations, the word was "+ word)
            return
        else:
            print("so far the word is",dashed_words)


        if(wrong_guess==chances):
            print("opps! man was hanged")
            print("the word was :" +word )

        
    again=int(input("do you want to play again? type 1 for yes or 2 for no?: "))
    if(again==1):
        play()
    return




if __name__=="__main__":
    play()
    







    


