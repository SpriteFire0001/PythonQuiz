score = 0
IsOn = False
Name = ""
TopicSelect = 0

#Mathematics Quiz
def MathQuiz():
  MathAnwserQ1 = ""
  score = 0
  print("You have selected: " + Topics[0] + ".")
  print("Question 1, " + QuestionsMathematics[0])
  print("A) " + MathematicsQ1Answers[0])
  print("B) " + MathematicsQ1Answers[1])
  print("C) " + MathematicsQ1Answers[2])
  print("D) " + MathematicsQ1Answers[3])
  
  a1 = MathematicsQ1Answers[0]
  a1 = "a"

  MathAnwserQ1 = input("What is your anwser?")
  
  
  if MathAnwserQ1.lower() == a1.lower():
    score = score + 1
    print("Correct!")
    print(Name + ", " + "your score is now: ")
    print(score)
    MathQuizQ2()
  else:
    print("Incorrect!")

#Question 2 of Mathematics
def MathQuizQ2():
  MathAnwserQ2 = ""
  score = 1
  print("Question 2, " + QuestionsMathematics[1])
  print("A) " + MathematicsQ2Answers[0])
  print("B) " + MathematicsQ2Answers[1])
  print("C) " + MathematicsQ2Answers[2])
  print("D) " + MathematicsQ2Answers[3])
  
  a2 = MathematicsQ2Answers[1]
  a2 = "b"
  
  MathAnwserQ2 = input("What is your anwser?")
  
  if MathAnwserQ2.lower() == a2.lower():
    score = score + 1
    print("Correct!")
    print(Name + ", " + "your score is now: ")
    print(score)
    MathQuizQ3()
  else:
    print("Incorrect!")

#Question 3 of Mathematics
def MathQuizQ3():
  MathAnwserQ3 = ""
  score = 2
  print("Question 3, " + QuestionsMathematics[2])
  print("A) " + MathematicsQ3Answers[0])
  print("B) " + MathematicsQ3Answers[1])
  print("C) " + MathematicsQ3Answers[2])
  print("D) " + MathematicsQ3Answers[3])
  
  a3 = MathematicsQ2Answers[2]
  a3 = "a"
  
  MathAnwserQ3 = input("What is your anwser?")
  
  if MathAnwserQ3.lower() == a3.lower():
    score = score + 1
    print("Correct!")
    print(Name + ", " + "your score is now: ")
    print(score)
    MathQuizQ4()
  else:
    print("Incorrect!")

#Question 4 of Mathematics
def MathQuizQ4():
  MathAnwserQ4 = ""
  score = 3
  print("Question 4, " + QuestionsMathematics[3])
  print("A) " + MathematicsQ4Answers[0])
  print("B) " + MathematicsQ4Answers[1])
  print("C) " + MathematicsQ4Answers[2])
  print("D) " + MathematicsQ4Answers[3])
  
  a4 = MathematicsQ2Answers[2]
  a4 = "b"
  
  MathAnwserQ4 = input("What is your anwser?")

  if MathAnwserQ4.lower() == a4.lower():
    score = score + 1
    print("Correct!")
    print(Name + ", " + "your score is now: ")
    print(score)
    print("You won!")
  else:
    print("Incorrect!")
  
#English Language Quiz
def EngLanQuiz():
  EnglishLanAnwserQ1 = ""
  score = score = 0
  print("You have selected: " + Topics[1] + ".")
  score = 0
  print("Question 1, " + QuestionsEnglishLanguage[0])
  print("A) " + EnglishLanguageQ1Answers[0])
  print("B) " + EnglishLanguageQ1Answers[1])
  print("C) " + EnglishLanguageQ1Answers[2])
  print("D) " + EnglishLanguageQ1Answers[3])
  
  a1 = EnglishLanguageQ1Answers[1]
  a1 = "b"
  
  EnglishLanAnwserQ1 = input("What is your anwser?")
  
  if EnglishLanAnwserQ1.lower() == a1.lower():
    score = score + 1
    print("Correct!")
    print(Name + ", " + "your score is now: ")
    print(score)
    EngLanQuizQ2()
  else:
    print("Incorrect!")
  
#Question 2 of English Language.
def EngLanQuizQ2():
  EnglishLanAnwserQ2 = ""
  score = 1
  print("Question 2, " + QuestionsEnglishLanguage[1])
  print("A) " + EnglishLanguageQ2Answers[0])
  print("B) " + EnglishLanguageQ2Answers[1])
  print("C) " + EnglishLanguageQ2Answers[2])
  print("D) " + EnglishLanguageQ2Answers[3])
  
  a2 = MathematicsQ2Answers[0]
  a2 = "a"
  
  EnglishLanAnwserQ2 = input("What is your anwser?")

  if EnglishLanAnwserQ2.lower() == a2.lower():
    score = score + 1
    print("Correct!")
    print(Name + ", " + "your score is now: ")
    print(score)
    EngLanQuizQ3()
  else:
    print("Incorrect!")

#Question 3 of English Language.
def EngLanQuizQ3():
  EnglishLanAnwserQ3 = ""
  score = 2
  print("Question 3, " + QuestionsEnglishLanguage[2])
  print("A) " + EnglishLanguageQ3Answers[0])
  print("B) " + EnglishLanguageQ3Answers[1])
  print("C) " + EnglishLanguageQ3Answers[2])
  print("D) " + EnglishLanguageQ3Answers[3])
  
  a3 = MathematicsQ2Answers[1]
  a3 = "b"
  
  EnglishLanAnwserQ3 = input("What is your anwser?")

  if EnglishLanAnwserQ3.lower() == a3.lower():
    score = score + 1
    print("Correct!")
    print(Name + ", " + "your score is now: ")
    print(score)
    EngLanQuizQ4()
  else:
    print("Incorrect!")
  
#Question 4 of English Language
def EngLanQuizQ4():
  EnglishLanAnwserQ4 = ""
  score = 3
  print("Question 4, " + QuestionsEnglishLanguage[3])
  print("A) " + EnglishLanguageQ4Answers[0])
  print("B) " + EnglishLanguageQ4Answers[1])

  a4 = EnglishLanguageQ4Answers[1]
  a4 = "b"
  
  EnglishLanAnwserQ4 = input("What is your anwser?")
  
  if EnglishLanAnwserQ4.lower() == a4.lower():
    score = score + 1
    print("Correct!")
    print(Name + ", " + "your score is now: ")
    print(score)
    print("You won!")
  else:
    print("Incorrect!")

#Infomation Technology Quiz
def ITquiz():
  ITAnwser1 = ""
  score = 0
  print("You have selected: " + Topics[2] + ".")
  print("Question 1, " + QuestionsInfomationTechnology[0])
  print("A) " + InfomationTechnologyQ1Answers[0])
  print("B) " + InfomationTechnologyQ1Answers[1])
  print("C) " + InfomationTechnologyQ1Answers[2])
  print("D) " + InfomationTechnologyQ1Answers[3])
  
  a1 = InfomationTechnologyQ1Answers[0]
  a1 = "a"
  
  ITAnwser1 = input("What is your anwser?")
  
  if ITAnwser1.lower() == a1.lower():
    score = score + 1
    print("Correct!")
    print(Name + ", " + "your score is now: ")
    print(score)
    ITquizQ2()
  else:
    print("Incorrect!")

#Infomation Technology Quiz Question 2
def ITquizQ2():
  ITAnwser2 = ""
  score = 1
  print("Question 2, " + QuestionsInfomationTechnology[1])
  print("A) " + InfomationTechnologyQ2Answers[0])
  print("B) " + InfomationTechnologyQ2Answers[1])
  print("C) " + InfomationTechnologyQ2Answers[2])
  print("D) " + InfomationTechnologyQ2Answers[3])
  
  a2 = InfomationTechnologyQ2Answers[1]
  a2 = "b"
  
  ITAnwser2 = input("What is your anwser?")
  a2.lower()
  
  if ITAnwser2.lower() == a2.lower():
    score = score + 1
    print("Correct!")
    print(Name + ", " + "your score is now: ")
    print(score)
    ITquizQ3()
  else:
    print("Incorrect!")

#Infomation Technology Quiz Question 3
def ITquizQ3():
  ITAnwser3 = ""
  score = 2
  print("Question 3, " + QuestionsInfomationTechnology[2])
  print("A) " + InfomationTechnologyQ3Answers[0])
  print("B) " + InfomationTechnologyQ3Answers[1])
  print("C) " + InfomationTechnologyQ3Answers[2])
  print("D) " + InfomationTechnologyQ3Answers[3])
  
  a3 = InfomationTechnologyQ3Answers[2]
  a3 = "c"
  
  ITAnwser3 = input("What is your anwser?")

  if ITAnwser3.lower() == a3.lower():
    score = score + 1
    print("Correct!")
    print(Name + ", " + "your score is now: ")
    print(score)
    ITquizQ4()
  else:
    print("Incorrect!")

#Infomation Technology Quiz Question 4
def ITquizQ4():
  ITAnwser4 = ""
  score = 3
  print("Question 4, " + QuestionsInfomationTechnology[3])
  print("A) " + InfomationTechnologyQ4Answers[0])
  print("B) " + InfomationTechnologyQ4Answers[1])
  print("C) " + InfomationTechnologyQ4Answers[2])
  print("D) " + InfomationTechnologyQ4Answers[3])

  a4 = InfomationTechnologyQ4Answers[2]
  a4 = "c"
  
  ITAnwser4 = input("What is your anwser?")
  
  if ITAnwser4.lower() == a4.lower():
    score = score + 1
    print("Correct!")
    print(Name + ", " + "your score is now: ")
    print(score)
    print("You won!")
  else:
    print("Incorrect!")

#Topics which the end-user selects once.
Topics = ["Mathematics", 
          "English Language", 
          "Infomation Technology"]

#The Questions of the Mathematics topic.
QuestionsMathematics = ["What is the first two-digit number?", 
                        "How do you find out that a year is a leap year?", 
                        "How many pence are there in a £?", 
                        "What letters are used for two-dimensions?"]

#The Questions of the English Language topic.
QuestionsEnglishLanguage = ["What type of word is used to add detail to a noun?", 
                            "What makes a simple sentence?", 
                            "Which of those sentences is an example of a simile?",
                            "Which is bigger? A novella or a novel?"]

#The Questions of the Infomation Technology topic.
QuestionsInfomationTechnology = ["What language does a computer have as their first language?",
                                 "What variable is used to store a single character?",
                                 "Who invented the World Wide Web?",
                                 "Who is Bjarne Stroustrup?"]
                                 
#The Answers of the Mathematic topic.
MathematicsQ1Answers = ["10", 
                         "9", 
                        "42", 
                         "0"]

MathematicsQ2Answers = ["By calculating the number to days until your birthday" , 
                        "By dividing the year by 4", 
                        "By uttering all the letters in the English Alphabet", 
                        "By singing in a very drunk state before the Prime Minister"]

MathematicsQ3Answers = ["100 Pennies" , 
                        "20 Shillings", 
                        "12 Sovereigns", 
                        "10 £5 banknotes"]

MathematicsQ4Answers = ["A, B and C", 
                        "X and Y", 
                        "1, 2 and 3", 
                        "X, Y and Z"]


#The Answers of the English Language topic.
EnglishLanguageQ1Answers = ["verb", 
                            "adjective", 
                            "noun", 
                            "adverb"]
                            
EnglishLanguageQ2Answers = ["A noun and a verb", 
                            "An adjective", 
                            "An interjection", 
                            "A noun and an adjective"]

EnglishLanguageQ3Answers = ["I read, I write and I prosper.", 
                            "The skyscraper was as titanic as Victoria Falls.", 
                            "Those ravens are crafty knaves.", 
                            "Demented dogs."]

EnglishLanguageQ4Answers = ["Novella", 
                            "Novel"]

#The Answers of the Infomation Technology topic.
InfomationTechnologyQ1Answers = ["Binary", 
                                 "Shakespearean English", 
                                 "Latin",
                                 "Sign language"]
                                 
InfomationTechnologyQ2Answers = ["string", 
                                 "char", 
                                 "int",
                                 "decimal"]
                                 
InfomationTechnologyQ2Answers = ["string", 
                                 "char", 
                                 "int",
                                 "decimal"]
                                 
InfomationTechnologyQ3Answers = ["Alan Turing", 
                                 "Elon Musk", 
                                 "Tim Berners-Lee",
                                 "Mark Zuckerberg"]
                                 
InfomationTechnologyQ4Answers = ["An artist", 
                                 "A mathematician", 
                                 "The inventor of the C++ programming language", 
                                 "A historian"]
                                 

Name = str(input("Before you start a new game, what is your name?"))

#Main Menu
while (IsOn != True):
    try:
      TopicSelect = int(input("Select a topic. 1 is for " + Topics[0] + "," + " 2 is for " +  Topics[1] + " and 3 is for " + Topics[2] + "." + " Also, you can use 4 to exit the application."))
      if TopicSelect == 1:
        MathQuiz()
      elif TopicSelect == 2:
          EngLanQuiz()
      elif TopicSelect == 3:
          ITquiz()
      elif TopicSelect == 4:
          IsOn = True
      else:
          print("Use a number between 1 to 4")
          
    except ValueError:
      print("Only use integer values.")

print("Software Terminated.")