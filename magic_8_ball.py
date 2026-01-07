import random
name = input("Enter your name: ")
num_questions = input("How many questions would you like to ask the Magic 8-ball: ")
num_questions = int(num_questions)
responses = ["Yes, definitely!","Ask again later.","No way!","Without a doubt!","Better not tell you now.","It is certain.","Try again soon.","My sources say no.","Signs point to yes.","Absolutely not!"]
print("You may now ask your questions to the all knowing Magic 8-Ball!")
for i in range(num_questions):
    question = input("Ask your yes/no question:")
    print(f"-----------------------------\n" "Hello",name,"\n" "You asked:", question, "\n" "The Magic 8-Ball says:", random.choice(responses), "\n" "-----------------------------\n")
