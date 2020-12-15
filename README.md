# Python-Concepts-Quiz

This program uses the Python programming language, with the modules tkinter, tkinter.font, breezypythongui, time, and random.

This program consists of a breezypythongui based interface, which initially prompts the user of the directions/instructions of the quiz, followed by the quiz beginning once the instructions box is closed and the "Begin" button has been selected. 

A current time clock is displayed to the user in the top right corner of the program which is utilized with the time module to record the users amount of time taken to complete the quiz. The quiz is multiple-choice based and consists of 10 questions based on Python concepts, which uses a text file to read the questions from. 

The user will select the radio-button answer in which they believe is the correct answer to the question displayed, followed by selecting the "Submit" button. If the users answer to the question was correct it will be displayed as either "Correct!", or "Incorrect!" within the results box.

Once all 10 questions have been answered, the user will be prompted the quiz is now completed and their score out of 10(for example 6/10, 4/10, 9/10, etc), their letter grade achieved, the amount of time it took them to complete the quiz, and a prompt presenting a statement reflecting their score acquired will be displayed to the user.

The class created is called PyQuiz, and uses 7 methods that run within PyQuiz. The seven methods are called “calc”, “timer”, “scramble”, “begin”, “next_Answer”, “check_Answer”, and “questions”.

Various for-loops were used throughout the program in differing functions to perform a set of defined tasks, such as reading from the text file, among many others. Multiple lists were created and used to store information to be used in the program such as storing the lists/nested lists of answers for the questions. A dictionary was created and used to store user prompts to be displayed to the user throughout the program, and quite a bit of if/elif/else statements were created and used throughout the methods/program to determine different situations that would occur. The “time” module is used to create a clock and a timer to time the user of their quiz time.

