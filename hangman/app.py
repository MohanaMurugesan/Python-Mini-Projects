from random_word import RandomWords
from stages import stage0,stage1,stage2,stage3,stage4,stage5,stage6

current_stage = [stage0, stage1, stage2, stage3, stage4, stage5, stage6]

r = RandomWords()
word = (r.get_random_word()).lower()

if word :
    coded_word = ['_' for _ in word]
    print(coded_word)

    attempt = 0
    max_attempt=6
    guessed_letters=[]

    print("\n😈😈 Your gallow is waiting 😈😈 ")
    print('\n')
    print(stage0)

    while ''.join(coded_word) != word and attempt < 6:
        guess = input("Guess the correct letter : ")
        if len(guess) == 1 and guess.isalpha() and guess not in guessed_letters:
            guessed_letters.append(guess)
            if guess in word:
                for i,val in enumerate(word):
                    if guess == val :
                        coded_word[i] = guess
                print("✔️...Great...✔️")
                print(' '.join(coded_word))
                if ''.join(coded_word) == word:
                    print("🎉...Hurray!!! You won !!!....🎉") 
                    break                          
                                
            else:
                attempt += 1
                print("\n 😈....Wrong guess....😈")
                print("\n ☠️...You're way closer to the death...☠️")
                print(current_stage[attempt])
                print(f"....You have only {max_attempt - attempt} attempt(s) to guess")
            print("Guessed Letters:" , ' , '.join(guessed_letters))

        else:
            print("....Only one letter at a time and it must be a alphabet and should not be already gussed one....")
    
    else :
        print(f"💀 Game Over... The word is '{word}' 💀")


else:
    print("No word exists")