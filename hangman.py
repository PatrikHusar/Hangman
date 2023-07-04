from faker import Faker
from turtle import*
import time

class hangman():
    def __init__(self) -> None:
        self.__spaceBetweenPlaces = 10
        self.__y = -250
        self.__part = 0
        self.__guessIndex = 0
        self.__x = 350 - self.__spaceBetweenPlaces
        self.__polomer = 75
        self.__hangmanX = -200
        self.__hangmanY = -250
        self.__faker = Faker()
        self.__word = self.__faker.word()
        self.__lettersInWord = len(self.__word)
        self.__widthOfOnePlace = (self.__x - (self.__lettersInWord - 1) * self.__spaceBetweenPlaces) / self.__lettersInWord
        self.__lengthOfBody = 75
        self.__lengthOfArm = 40
        self.__lengthOfLeg = 50
        self.__usedLettersXset = 0
        self.__usedLettersX = self.__usedLettersXset
        self.__usedLettersY = 275
        self.__goodGuesses = []
        self.__win = 1
        for a in range(len(self.__word)):
            self.__goodGuesses.append(0)
        self.__shorterLine = 125
        color('black')
        pensize(2)
        penup()
        goto(self.__x, self.__y)
        pendown()
        self.__showLenOfWord()

    def __showLenOfWord(self):
        for a in range(self.__lettersInWord):
            penup()
            self.__x -= self.__spaceBetweenPlaces
            goto(self.__x, self.__y)
            pendown()
            self.__x -= self.__widthOfOnePlace
            goto(self.__x, self.__y)
        while True:
            self.__yourGuess()
            for index in range(len(self.__word)):
                if self.__goodGuesses[index] == 1:
                    self.__win = 1
                else:
                    self.__win = 0
                    break

            if self.__win == 1:
                goto(-250, 250)
                write('you won!!!', align='right', font=150)
                time.sleep(3)
                break

            if self.__part == 11:
                goto(-250, 250)
                write('you lose :(.\nThe correct word was: \n' + self.__word, align='left', font=150)
                time.sleep(3)
                break

    def __yourGuess(self):
        self.__guess = textinput('ERROR' , 'enter your guess:')
        if not self.__guess == None:
            self.__correct = self.__word.count(self.__guess)
            if self.__correct == 0:
                self.__creatingHangman()
                self.__usedLetters()
            else:
                penup()
                self.__goodGuesses += self.__guess
                if len(self.__guess) == 1:
                    self.__letter = 'a'
                    for a in range(self.__correct):
                        if self.__letter == 'a':
                            self.__letter = self.__word.find(self.__guess)
                        else:
                            self.__letter = self.__word.find(self.__guess, self.__letter + 1)
                        self.__Write(self.__letter)

                else:
                    goto(self.__x, self.__y)
                    self.__guessIndex = 0
                    for a in range(len(self.__guess)):
                        for index in range(len(self.__word)):
                            if self.__guess[self.__guessIndex] == self.__word[index]:
                                self.__Write(index)
                                self.__guessIndex += 1
                                break

    def __usedLetters(self):
        penup()
        goto(self.__usedLettersX, self.__usedLettersY)
        write(self.__guess + ',', align='left', font=150)
        self.__usedLettersX += len(self.__guess) * 13 + 5
        if self.__usedLettersX > 300:
            self.__usedLettersY -= 20
            self.__usedLettersX = self.__usedLettersXset

    def __Write(self, index):
        goto(self.__x, self.__y)
        goto((self.__spaceBetweenPlaces + self.__widthOfOnePlace) * index + self.__widthOfOnePlace / 2, self.__y)
        write(self.__word[index], align='right', font=150)
        self.__goodGuesses[index] = 1

    def __creatingHangman(self):
        if self.__part == 0:
            penup()
            goto(self.__hangmanX, self.__hangmanY)
            pendown()
            left(90)
            circle(self.__polomer, 180)
            self.__part = 1

        elif self.__part == 1:
            penup()
            self.__hangmanX -= self.__polomer
            self.__hangmanY += self.__polomer
            goto(self.__hangmanX, self.__hangmanY)
            pendown()
            self.__hangmanY += self.__shorterLine * 2
            goto(self.__hangmanX, self.__hangmanY)
            self.__part = 2

        elif self.__part == 2:
            penup()
            goto(self.__hangmanX, self.__hangmanY)
            pendown()
            self.__hangmanX += self.__shorterLine
            goto(self.__hangmanX, self.__hangmanY)
            self.__part = 3

        elif self.__part == 3:
            penup()
            self.__hangmanX -= self.__shorterLine / 2
            goto(self.__hangmanX, self.__hangmanY)
            pendown()
            self.__hangmanX -= self.__shorterLine / 2
            self.__hangmanY -= self.__shorterLine / 2
            goto(self.__hangmanX, self.__hangmanY)
            self.__hangmanX += self.__shorterLine
            self.__hangmanY += self.__shorterLine / 2
            self.__part = 4

        elif self.__part == 4:
            penup()
            goto(self.__hangmanX, self.__hangmanY)
            pendown()
            self.__hangmanY -= 75
            goto(self.__hangmanX, self.__hangmanY)
            self.__part = 5

        elif self.__part == 5:
            penup()
            goto(self.__hangmanX, self.__hangmanY)
            right(90)
            pendown()
            circle(self.__polomer / 2.8)
            self.__part = 6

        elif self.__part == 6:
            penup()
            self.__hangmanY -= self.__polomer / 2.8 * 2
            goto(self.__hangmanX, self.__hangmanY)
            pendown()
            self.__hangmanY -= self.__lengthOfBody
            goto(self.__hangmanX, self.__hangmanY)
            self.__part = 7

        elif self.__part == 7:
            penup()
            self.__hangmanY += self.__lengthOfBody - 15
            goto(self.__hangmanX, self.__hangmanY)
            pendown()
            self.__hangmanX -= self.__lengthOfArm
            goto(self.__hangmanX, self.__hangmanY)
            self.__part = 8

        elif self.__part == 8:
            penup()
            goto(self.__hangmanX, self.__hangmanY)
            pendown()
            self.__hangmanX += self.__lengthOfArm * 2
            goto(self.__hangmanX, self.__hangmanY)
            self.__part = 9

        elif self.__part == 9:
            penup()
            self.__hangmanX -= self.__lengthOfArm
            self.__hangmanY -= self.__lengthOfBody - 15
            goto(self.__hangmanX, self.__hangmanY)
            pendown()
            self.__hangmanX -= self.__lengthOfLeg / 2
            self.__hangmanY -= self.__lengthOfLeg
            goto(self.__hangmanX, self.__hangmanY)
            self.__part = 10

        elif self.__part == 10:
            penup()
            self.__hangmanX += self.__lengthOfLeg / 2
            self.__hangmanY += self.__lengthOfLeg
            goto(self.__hangmanX, self.__hangmanY)
            pendown()
            self.__hangmanX += self.__lengthOfLeg / 2
            self.__hangmanY -= self.__lengthOfLeg
            goto(self.__hangmanX, self.__hangmanY)
            self.__part = 11

hangman()