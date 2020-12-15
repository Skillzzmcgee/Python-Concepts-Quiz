"""
Program: Python Concepts Quiz
Date: 12/4/2020
Author: Trent Johnson
Description: This program consists of a breezypythongui based interface, which initially prompts the user of
the directions/instructions of the quiz, followed by the quiz beginning once the instructions box is closed and the
"Begin" button has been selected. A current time clock is displayed to the user in the top right corner of the program which is
utilzed with the time module to record the users amount of time taken to complete the quiz. The quiz is multiple-choice based and
consists of 10 questions based on Python concepts, which uses a text file to read the questions from. The user will select the radio-button
answer in which they believe is the correct answer to the question displayed, followed by selecting the "Submit" button. If the users answer
to the question was correct it will be displayed as either "Correct!", or "Incorrect!" within the results box. Once all 10 questions have been
answered, the user will be prompted the quiz is now completed and their score out of 10(for example 6/10, 4/10, 9/10, etc), their letter grade
achieved, the amount of time it took them to complete the quiz, and a prompt presenting a statement reflecting their score acquired will be
displayed to the user.
"""



#Importing the breezypythongui, tkinter, tkinter.font, random, and time modules.

from breezypythongui import *
from tkinter import *
import tkinter.font as tkFont
import random
import time



#Setting of the PyQuiz class and the init function to initialize the variables, and empty lists.
#Setting of the for loop to open and read the text file holding the quiz questions to loop through and pop each question.

class PyQuiz(EasyFrame):
    

    def __init__(self):

        self.Started = False

        self.question_count = 0

        self.curr_score = 0

        self.letter_Grade = ("")

        self.final_score = ("")

        self.questionList = []

        question_list = open("Questions.txt", "r")
        for line in question_list:
            self.questionList.append(line)
        self.question = self.questionList[0]
        self.questionList.pop(0)

#Creation of the dictionary holding the user prompts, the nested list for holding the question answers,
#and the list holding the correct answers.

        self.prompts = {"wel_mes":'Greetings, and welcome to the Python Concepts Quiz! The quiz consists of \
10 differing Python concept questions in a multiple choice format.\n\nFor each answer you enter you will be \
prompted if you were either correct or incorrect, followed by your total score/questions answered correctly out of 10, the amount of time it took \
you to complete the quiz, and your letter grade achieved at the end of the quiz.\n\nTo unlock and begin the quiz, simply select the "Begin" button.\
\n\nGood Luck!',"cor":"           Correct!", "wro":"           Incorrect!", "g":"       Letter grade: ", "a_score":"Outstanding job!", "b_score":"Great job!"\
, "c_score":"Nice job!", "d_score":"Not bad! However, we might need to review a bit!", "f_score":"It looks like we might need to brush up and \
study these concepts a tad bit more!"}

        self.q_answers = [
                    ["dictionaries and lists","strings and tuples","lists and variables"],
                    ["10","20","30"],
                    ["[10, 20, 30]","[20, 30]","[0, 30]"],
                    ["1","2","0"],
                    ["[10, 60, 80]","[10, 20, 30, 40, 50]","[10, 20, 40, 60]"],
                    ["[5, 20, 30]","[10, 5, 30]","[5, 10, 15]"],
                    ["[15, 10, 20, 30]","[10, 15, 30]","[10, 15, 20, 30]"],
                    ['("name","age")','["name","age"]','{"name", "age"}'],
                    ['"knitting"',"None","1000"],
                    ["delete","pop","remove"]
                    ]

                    
        self.correct_answers = ["strings and tuples","20","[20, 30]","1","[10, 20, 30, 40, 50]","[10, 5, 30]",
                                "[10, 15, 20, 30]",'["name","age"]',"None","pop"]


#Creation of the GUI box, holding all of the text fields, buttons, and radio button options within the quiz,
#as well as the prompt to begin the quiz, and the alert box to generate to inform the user of the directions of the quiz.
#The timer method and scramble method are called from here to randomize the question answer options and record the time
#taken to complete the quiz.

        EasyFrame.__init__(self, title = "Python Concepts Quiz!", height = 700, width = 1500)
        self.messageBox(height = 20, width = 50, message = (self.prompts["wel_mes"]))

        self.addLabel(row = 0, column = 0, text = "~ Chapter 5 Review Questions ~", font = "Arial")

        self.question_Prompt = self.addLabel(row = 1, column = 0, text = 'Please select the "Begin" button as soon as you are ready to start the quiz.', font = "Georgia")
        

        self.addLabel(text = "Select(one):", row = 3, column = 0, font = "Arial")

        self.rGroup = self.addRadiobuttonGroup(row = 4, column = 0, columnspan = 5)

        
        self.default_Button = self.rGroup.addRadiobutton(text = " A.___________")
        self.rGroup.setSelectedButton(self.default_Button)

        self.button_2 = self.rGroup.addRadiobutton(text = " B.___________")
        self.button_3 = self.rGroup.addRadiobutton(text = " C.___________")


        panel1 = self.addPanel(row = 5, column = 0, columnspan = 8)
        self.begin_Button = self.addButton(text="Begin", row = 0, column = 3, command = self.begin)
        self.submit_Button = panel1.addButton(text = "Submit", row = 5, column = 0, state = "disabled", command = self.questions)
        self.results = panel1.addLabel(text = "- Result", row = 5, column = 5, font = "Georgia")
        self.result_Field = panel1.addTextField(text = "", row = 5, column = 4, state = "readonly")

        
        self.total_score = panel1.addLabel(text = "- Total Score", row = 5, column = 8, font = "Georgia")
        self.total_scorefield = panel1.addTextField(text = "", row = 5, column = 7, state = "readonly")
        self.Grade = panel1.addLabel(text = "- Grade", row = 5, column = 10, font = "Georgia")
        self.letter_G = panel1.addTextField(text = "", row = 5, column = 9, state = "readonly")

        self.time_it = True
        self.timer()
        self.timing = False
        self.scramble()


#Creation of the calc method which will time the users amount of time taken to complete the quiz w/
#the use of if/else statements and boolean values.

#NOTE: THE TIME MODULE WAS IMPLEMENTED AND USED HERE TO SATISFY THE REQUIREMENTS OF THE NEED TO
#USE ONE PYTHON CONCEPT WHICH WAS NOT EXPLORED/USED/LEARNED WITHIN CLASS.

    def calc(self):
        if self.timing == False:
            self.begin = self.now
            self.timing = True
            return

        else:
            self.end = self.now
            ending = self.end.split(":")
            beginning = self.begin.split(":")

            ending.pop(0)
            beginning.pop(0)
            ending = (int(ending[0]) * 60) + int(ending[1])
            beginning = (int(beginning[0]) * 60) + int(beginning[1])
            self.time_it = False
            
            
            
            total = int(ending) - int(beginning)
            self.end_time = total

            self.mins = 0
            self.secs = 0

            if self.end_time >=60:
                self.mins = self.end_time // 60
                self.secs = self.end_time % 60

            else:
                self.mins = 0
                self.secs = total

#Creation of the timer method which will display the current time "clock" within the
#top right corner of the screen, and also be utilized with the calc function to
#calculate the total amount of time taken to complete the quiz.

#NOTE: THE TIME MODULE WAS IMPLEMENTED AND USED HERE TO SATISFY THE REQUIREMENTS OF THE NEED TO
#USE ONE PYTHON CONCEPT WHICH WAS NOT EXPLORED/USED/LEARNED WITHIN CLASS.

    def timer(self):
        
        
            
        self.now = time.strftime("%H:%M:%S")
        self.time = self.addLabel(text=self.now, row = 0, column = 4, font = "Arial")
        self.after(1000, self.timer)


#Creation of the scramble method which takes the question answer list, and scrambles
#the potential radio button options to be displayed on the quiz with the use of a for loop.
        
    def scramble(self):
        for x in self.q_answers:
            for y in x:
                random.shuffle(x)
        

#Creation of the begin method which is responsible for beginning the quiz with a button.
#This method is also utilized to use with the calc method to time the users quiz time,
#as well as with the next_Answer method to begin displaying the quiz questions. Once the
#quiz has begun by selecting the "begin" button, the "submit button becomes active, and the
#"begin button becomes deactivated.

    def begin(self):
        self.calc()
        self.testing = True
        self.Started = True
        question_Prompt = self.addLabel(row = 1, column = 0, text = self.question, font = "Georgia")
        self.next_Answer()
        self.begin_Button["state"] = "disabled"
        self.submit_Button["state"] = "active"
        

#Creation of the next_Answer method which is used to correlate and assign the quiz question answers from
#the question answers nested list. The nested list index of 0 is then popped, assigning the next
#randomized nested list answer options to the properly correlated question.
        
    def next_Answer(self):

        self.rGroup = self.addRadiobuttonGroup(row = 4, column = 0, columnspan = 5)

        self.default_Button = self.rGroup.addRadiobutton(text = self.q_answers[0][0])
        self.rGroup.setSelectedButton(self.default_Button)

        self.button_2 = self.rGroup.addRadiobutton(text = self.q_answers[0][1])
        self.button_3 = self.rGroup.addRadiobutton(text = self.q_answers[0][2])
        self.q_answers.pop(0)
        
#Creation of the check_Answer method which is used to compare the value of the submitted button answer option
#to the correct specific answer to the question. The dictionary prompts of "correct" or "incorrect" are then
#utilzed to prompt the users result of their answer within results text field, then popping the 0 index of
#the correct_answers list, bringing in the next correct answer to this index of the next correlated question.
        
    def check_Answer(self):
        x = str(self.rGroup.getSelectedButton()["text"])
        y = str(self.correct_answers[0])
        if x == y:
            self.curr_score += 1
            self.result_Field.setText(self.prompts["cor"])

        else:
            self.result_Field.setText(self.prompts["wro"])
                
        self.correct_answers.pop(0)
            

#Creation of the questions method which is used with if/elif/else statements, to determine if the quiz continues to
#cycle through to the next question, or if the quiz is now completed. If the quiz is completed, the user is prompted of this and
#dictionary prompts are used to display the users score out of 10, as well as dislay the users grade letter achieved on the quiz.
        

#If/elif/else statements are used once the quiz is completed to determine the users letter grade and correlate it
#to the correct dictionary prompts to be displayed regarding their scores, of both their grade letter, and also
#give/display a statement regarding their specific score earned(how well they did).

#The submit button is deactivated here once the quiz is completed.
            
    def questions(self):
        if self.question_count == 10 or self.Started == False:
            self.calc()
            self.total_scorefield.setText(f"    You scored: {self.curr_score}/10!")
            if self.curr_score >= 9:
                self.letter_Grade = "A"
            elif self.curr_score == 8:
                self.letter_Grade = "B"
            elif self.curr_score == 7:
                self.letter_Grade = "C"
            elif self.curr_score == 6:
                self.letter_Grade = "D"
            else:
                self.letter_Grade = "F"


            if self.letter_Grade == "A":
                self.addLabel(row = 2, column = 0, font = "Courier", text = (self.prompts["a_score"]))
            elif self.letter_Grade == "B":
                self.addLabel(row = 2, column = 0, font = "Courier", text = (self.prompts["b_score"]))
            elif self.letter_Grade == "C":
                self.addLabel(row = 2, column = 0, font = "Courier", text = (self.prompts["c_score"]))
            elif self.letter_Grade == "D":
                self.addLabel(row = 2, column = 0, font = "Courier", text = (self.prompts["d_score"]))
            else:
                self.addLabel(row = 2, column = 0, font = "Courier", text = (self.prompts["f_score"]))
                
            self.question_Prompt = self.addLabel(row = 1, column = 0, text = f'Thank you for your participation! This concludes the current "Concepts of Python Quiz". Please refer to your score/achieved grade of  " {self.curr_score}/10  -  {self.letter_Grade} " taken within {self.mins} minute(s) and {self.secs} seconds.', font = "Georgia")
            

            self.letter_G.setText(self.prompts["g"]+(self.letter_Grade))
            
            self.submit_Button["state"] = "disabled"
            
#The else statement is used here if the quiz is not completed yet, along with a try/except method to handle an IndexError exception,
#to set the next question from the question list by popping the current question of index 0, in the question list.
#The quiz is then continued by adding 1 to the question count, and calling the check_Answer and questions methods.


        else:

            try:
                

                self.addLabel(row = 1, column = 0, text = self.questionList[0], font = "Georgia")
                self.questionList.pop(0)
                self.check_Answer()
                self.next_Answer()

            except IndexError:

                self.addLabel(row = 1, column = 0, text = "", font = "Georgia")
                self.question_count += 1
                self.check_Answer()
                self.questions()
                
                
            self.question_count += 1
            
        

        
def main():
    PyQuiz().mainloop()

if __name__ == "__main__":
    main()






