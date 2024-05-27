print("Welcome to my computer quiz!")

playing = input("Do you want to play? ").lower()

if playing != "yes":
    quit()

print("Okay, let's play :)")
score = 0

qa_pairs = {
    "What does CPU stands for? ":"central processing unit",
    "What does GPU stands for? ":"graphics processing unit",
    "What does RAM stands for? ":"random access memory",
    "What does PSU stands for? ":"power supply"
    }

for question, correct_answer in qa_pairs.items():   
    answer = input(question).lower()
    if answer == correct_answer:
        print("Correct!")
        score += 1
    else:
        print("Incorrect!")

print(f"You got {score} questions correct!")
print(f"You got {(score/len(qa_pairs)) * 100} %.")