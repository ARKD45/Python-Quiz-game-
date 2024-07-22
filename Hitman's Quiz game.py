import random
#Question to be asked
quiz_data = [
    {
        "question": "What is Rohit Sharma's highest individual score in One Day Internationals (ODIs)?",
        "options": ["A. 264", "B. 200", "C. 219", "D. 250"],
        "answer": "A"
    },
    {
        "question": "Which team does Rohit Sharma captain in the Indian Premier League (IPL)?",
        "options": ["A. Chennai Super Kings", "B. Mumbai Indians", "C. Kolkata Knight Riders", "D. Royal Challengers Bangalore"],
        "answer": "B"
    },
    {
        "question": "In which year did Rohit Sharma make his debut in international cricket?",
        "options": ["A. 2007", "B. 2008", "C. 2006", "D. 2009"],
        "answer": "A"
    },
    {
        "question": "How many double centuries has Rohit Sharma scored in ODI cricket?",
        "options": ["A. 1", "B. 2", "C. 3", "D. 4"],
        "answer": "C"
    },
    {
        "question": "Rohit Sharma is popularly known by which nickname?",
        "options": ["A. Hitman", "B. The Wall", "C. Captain Cool", "D. The Finisher"],
        "answer": "A"
    },
    {
        "question": "Rohit Sharma scored his first ODI double century against which team?",
        "options": ["A. Australia", "B. South Africa", "C. England", "D. West Indies"],
        "answer": "D"
    }

]
#displaying content
def ask_question(question_data):
    print(question_data["question"])
    for option in question_data["options"]:
        print(option)
    user_answer = input("Enter your answer (A,B,C,D): ").upper()
    if user_answer == question_data["answer"]:
        return True
    else:
        return False
#main body
if __name__=="__main__":
    score=0
    random.shuffle(quiz_data)
    for i in range(1,6):
        print(f'Question {i} of 5')
        if ask_question(quiz_data[i]):
            print("Correct!\n")
            score += 1
        else:
            print(f"Wrong! The correct answer is {quiz_data[i]['answer']}.\n")

    print(f"You scored {score}/5.")