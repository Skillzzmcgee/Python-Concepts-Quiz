"""
Program: Python Concepts Quiz
Date: 12/4/2020
Author: Trent Johnson
Description: This program consists of a breezypythongui based interface, which initially prompts the user of
the directions/instructions of the game, followed by the quiz beginning once the instructions box is closed.
The quiz is multiple-choice based and consists of 10 questions based on Python concepts, which uses a text file
to read the questions from. The user will select the radio-button answer in which they believe is the correct
answer to the question displayed, followed by selecting the "submit" button. If the users answer to the question
was correct it will be displayed as either "Correct", or "Incorrect" within the results box. Once all 10 questions
have been answered, the user will be prompted of their score out of 10(for example 6/10, 4/10, 9/10, etc).
"""

from breezypythongui import *
from tkinter import *
import random

class PyQuiz(EasyFrame):
    


    def __init__(self):

        question_count = 0

        self.questionList = []

        question_list = open("Answers.txt", "r")
        for line in question_list:
            self.questionList.append(line)
        self.question = self.questionList[0]
        self.questionList.pop(0)


        prompts = {"wel_mes":"Greetings, and welcome to the Python Concepts Quiz! The quiz consists of \
10 differing Python concept questions in a multiple choice format.\n\nFor each answer you enter you will be \
prompted if you were correct or incorrect, followed by your total score achieved out of 10 at the end of \
the quiz.\n\nGood Luck!","cor":"Correct!", "wro":"Incorrect!"}



        EasyFrame.__init__(self, title = "Python Concepts Quiz")

        self.messageBox(height = 20, width = 50, message = (prompts["wel_mes"]))

        self.addLabel(row = 0, column = 1, text = "Python Concepts Quiz!")
        

        self.addLabel(row = 1, column = 0, text = self.question)
        

        self.addLabel(text = "Select(one)", row = 3, column = 0)
        self.rGroup = self.addRadiobuttonGroup(row = 4, column = 0, columnspan = 5)

        defaultRB = self.rGroup.addRadiobutton(text = "A")

        self.rGroup.setSelectedButton(defaultRB)
        self.rGroup.addRadiobutton(text = "B")
        self.rGroup.addRadiobutton(text = "C")


        panel1 = self.addPanel(row = 5, column = 0, columnspan = 5)
        panel1.addButton(text = "Submit", row = 5, column = 0, command = self.questions)
        panel1.addLabel(text = " - Result", row = 5, column = 3)
        self.result_Field = panel1.addTextField(text = "", row = 5, column = 2)

        
        

    def questions(self):
        if self.questionList == []:
            print("Complete")
        else:
            self.addLabel(row = 1, column = 0, text = self.questionList[0])
            self.questionList.pop(0)


        

    #def submit_Answer(self):
        #question_count += 1
            
            

        

        

def main():
    PyQuiz().mainloop()

if __name__ == "__main__":
    main()
