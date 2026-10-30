import random
import os


# =========================
# QUESTION BANKS
# =========================

questions = {
    "Math": [
        {
            "question": "What is 15% of 200?",
            "answer": "30",
            "difficulty": "Easy"
        },
        {
            "question": "Solve: 3x + 5 = 20",
            "answer": "5",
            "difficulty": "Easy"
        },
        {
            "question": "What is the slope of y = 4x + 2?",
            "answer": "4",
            "difficulty": "Easy"
        },
        {
            "question": "What is the vertex of y = (x - 3)^2 + 2?",
            "answer": "(3, 2)",
            "difficulty": "Medium"
        },
        {
            "question": "Solve: x^2 - 9 = 0",
            "answer": "3 or -3",
            "difficulty": "Medium"
        },
        {
            "question": "What is sin(90°)?",
            "answer": "1",
            "difficulty": "Easy"
        },
        {
            "question": "If 2x = 18, what is x?",
            "answer": "9",
            "difficulty": "Easy"
        },
        {
            "question": "What is the area of a triangle with base 10 and height 6?",
            "answer": "30",
            "difficulty": "Easy"
        }
    ],

    "Verbal": [
        {
            "question": "Choose the closest meaning of 'legitimate': valid or suspicious?",
            "answer": "valid",
            "difficulty": "Easy"
        },
        {
            "question": "What does 'suppress' mean?",
            "answer": "to prevent or hold back",
            "difficulty": "Medium"
        },
        {
            "question": "What does 'decipher' mean?",
            "answer": "to decode or understand something difficult",
            "difficulty": "Medium"
        },
        {
            "question": "What does 'impenetrable' mean?",
            "answer": "impossible or very difficult to pass through or understand",
            "difficulty": "Hard"
        },
        {
            "question": "Choose the synonym of 'rapid': slow or fast?",
            "answer": "fast",
            "difficulty": "Easy"
        },
        {
            "question": "What does 'remnants' mean?",
            "answer": "remaining parts",
            "difficulty": "Medium"
        }
    ],

    "History": [
        {
            "question": "Who was the first president of Kazakhstan?",
            "answer": "Nursultan Nazarbayev",
            "difficulty": "Easy"
        },
        {
            "question": "In what year did Kazakhstan gain independence?",
            "answer": "1991",
            "difficulty": "Easy"
        },
        {
            "question": "What was the Silk Road?",
            "answer": "a network of trade routes connecting East and West",
            "difficulty": "Medium"
        },
        {
            "question": "What ancient civilization built the pyramids of Giza?",
            "answer": "Ancient Egypt",
            "difficulty": "Easy"
        }
    ],

    "SAT": [
        {
            "question": "If x + 7 = 15, what is x?",
            "answer": "8",
            "difficulty": "Easy"
        },
        {
            "question": "What is the slope of y = 2x + 5?",
            "answer": "2",
            "difficulty": "Easy"
        },
        {
            "question": "If a word means the opposite of 'expand', is it 'contract' or 'increase'?",
            "answer": "contract",
            "difficulty": "Medium"
        },
        {
            "question": "What is 25% of 80?",
            "answer": "20",
            "difficulty": "Easy"
        },
        {
            "question": "What does 'ambiguous' mean?",
            "answer": "unclear or having more than one possible meaning",
            "difficulty": "Medium"
        }
    ],

    "IELTS": [
        {
            "question": "What does 'substantial' mean?",
            "answer": "large or considerable",
            "difficulty": "Medium"
        },
        {
            "question": "What does 'decline' mean?",
            "answer": "to decrease",
            "difficulty": "Easy"
        },
        {
            "question": "What does 'consequently' mean?",
            "answer": "as a result",
            "difficulty": "Medium"
        },
        {
            "question": "What does 'controversial' mean?",
            "answer": "causing disagreement or debate",
            "difficulty": "Medium"
        }
    ]
}


# =========================
# SETTINGS
# =========================

settings = {
    "questions_per_session": 5
}


# =========================
# FILE FUNCTIONS
# =========================

def save_mistake(subject, question, correct_answer, user_answer):
    with open("mistakes.txt", "a", encoding="utf-8") as file:
        file.write(f"Subject: {subject}\n")
        file.write(f"Question: {question}\n")
        file.write(f"Your answer: {user_answer}\n")
        file.write(f"Correct answer: {correct_answer}\n")
        file.write("-" * 40 + "\n")


def read_mistakes():
    if not os.path.exists("mistakes.txt"):
        return "No mistakes recorded yet."

    with open("mistakes.txt", "r", encoding="utf-8") as file:
        content = file.read()

    if content.strip() == "":
        return "No mistakes recorded yet."

    return content


def save_progress(subject, score, total):
    percentage = (score / total) * 100

    with open("progress.txt", "a", encoding="utf-8") as file:
        file.write(
            f"{subject} | Score: {score}/{total} | "
            f"Percentage: {percentage:.1f}%\n"
        )


def read_progress():
    if not os.path.exists("progress.txt"):
        return "No progress recorded yet."

    with open("progress.txt", "r", encoding="utf-8") as file:
        content = file.read()

    if content.strip() == "":
        return "No progress recorded yet."

    return content


# =========================
# PRACTICE QUESTIONS
# =========================

def practice(subject):
    print("\n" + "=" * 50)
    print(f"{subject} PRACTICE")
    print("=" * 50)

    available_questions = questions[subject].copy()

    random.shuffle(available_questions)

    number_of_questions = min(
        settings["questions_per_session"],
        len(available_questions)
    )

    selected_questions = available_questions[:number_of_questions]

    score = 0

    for number, item in enumerate(selected_questions, start=1):

        print(f"\nQuestion {number}/{number_of_questions}")
        print(f"Difficulty: {item['difficulty']}")
        print(item["question"])

        user_answer = input("Your answer: ").strip()

        correct_answer = item["answer"]

        # Allow a few different forms of the same answer
        user_clean = user_answer.lower().strip()
        correct_clean = correct_answer.lower().strip()

        if user_clean == correct_clean:
            print("Correct!")
            score += 1
        else:
            print("Incorrect.")
            print(f"Correct answer: {correct_answer}")

            save_mistake(
                subject,
                item["question"],
                correct_answer,
                user_answer
            )

    percentage = (score / number_of_questions) * 100

    print("\n" + "-" * 50)
    print("SESSION COMPLETE")
    print(f"Score: {score}/{number_of_questions}")
    print(f"Percentage: {percentage:.1f}%")
    print("-" * 50)

    if percentage >= 90:
        print("Excellent work! You have a strong understanding.")
    elif percentage >= 70:
        print("Good job! Keep practicing to become more consistent.")
    elif percentage >= 50:
        print("You are making progress. Review your mistakes.")
    else:
        print("Keep going. Focus on the topics you find difficult.")

    save_progress(subject, score, number_of_questions)

    input("\nPress Enter to return to the menu...")


# =========================
# PRACTICE MISTAKES
# =========================

def practice_mistakes():
    print("\n" + "=" * 50)
    print("PRACTICE YOUR MISTAKES")
    print("=" * 50)

    if not os.path.exists("mistakes.txt"):
        print("You do not have any recorded mistakes yet.")
        input("\nPress Enter to return...")
        return

    with open("mistakes.txt", "r", encoding="utf-8") as file:
        lines = file.readlines()

    mistakes = []

    current = {}

    for line in lines:
        line = line.strip()

        if line.startswith("Subject:"):
            current["subject"] = line.replace("Subject:", "").strip()

        elif line.startswith("Question:"):
            current["question"] = line.replace("Question:", "").strip()

        elif line.startswith("Your answer:"):
            current["user_answer"] = line.replace(
                "Your answer:", ""
            ).strip()

        elif line.startswith("Correct answer:"):
            current["correct_answer"] = line.replace(
                "Correct answer:", ""
            ).strip()

        elif line.startswith("-") and current:
            mistakes.append(current)
            current = {}

    if current:
        mistakes.append(current)

    if not mistakes:
        print("No mistakes found.")
        input("\nPress Enter to return...")
        return

    random.shuffle(mistakes)

    score = 0

    print(f"\nYou have {len(mistakes)} recorded mistake(s).")

    for number, mistake in enumerate(mistakes, start=1):

        print("\n" + "-" * 50)
        print(f"Question {number}")
        print(f"Subject: {mistake['subject']}")
        print(mistake["question"])

        answer = input("Your answer: ").strip()

        if answer.lower() == mistake["correct_answer"].lower():
            print("Correct! You fixed this mistake.")
            score += 1
        else:
            print("Not quite.")
            print(f"Correct answer: {mistake['correct_answer']}")

    print("\n" + "=" * 50)
    print("MISTAKE PRACTICE COMPLETE")
    print(f"Score: {score}/{len(mistakes)}")
    print("=" * 50)

    input("\nPress Enter to return...")


# =========================
# STUDY TIPS
# =========================

def study_tips():
    tips = {
        "Math": [
            "Practice a small number of problems every day.",
            "Write down the steps instead of only looking at the answer.",
            "Review mistakes and identify why you made them.",
            "Use Desmos to check graphs and functions when appropriate."
        ],

        "Verbal": [
            "Learn words in context rather than memorizing isolated definitions.",
            "Write your own example sentence for new vocabulary.",
            "Review difficult words several times during the week.",
            "Look for context clues before choosing an answer."
        ],

        "History": [
            "Create timelines for important events.",
            "Connect events to their causes and consequences.",
            "Use active recall instead of only rereading notes."
        ],

        "SAT": [
            "Practice under timed conditions.",
            "Keep a mistake log.",
            "Review grammar rules regularly.",
            "For math, learn the concepts behind formulas."
        ],

        "IELTS": [
            "Read articles from different topics.",
            "Keep a vocabulary notebook.",
            "Practice identifying the main idea quickly.",
            "Review why an answer is correct, not only the answer itself."
        ]
    }

    print("\n" + "=" * 50)
    print("STUDY TIPS")
    print("=" * 50)

    print("\nChoose a subject:")

    subjects = list(tips.keys())

    for i, subject in enumerate(subjects, start=1):
        print(f"{i}. {subject}")

    choice = input("\nChoose: ").strip()

    if choice.isdigit() and 1 <= int(choice) <= len(subjects):
        subject = subjects[int(choice) - 1]

        print(f"\nTips for {subject}:")

        for tip in tips[subject]:
            print(f"• {tip}")

    else:
        print("Invalid choice.")

    input("\nPress Enter to return...")


# =========================
# STUDY PLAN
# =========================

def study_plan():
    print("\n" + "=" * 50)
    print("PERSONALIZED STUDY PLAN")
    print("=" * 50)

    print("""
Monday
• Math practice
• Review mistakes
• Vocabulary

Tuesday
• IELTS reading
• Korean study
• Short SAT practice

Wednesday
• SAT Math
• Review difficult topics
• Vocabulary

Thursday
• IELTS practice
• Korean study
• Review mistakes

Friday
• SAT Verbal
• Math practice
• Weekly review

Saturday
• Longer SAT/IELTS practice session
• Review mistakes
• Work on weak areas

Sunday
• Light review
• Vocabulary
• Plan the next week
• Rest
""")

    input("Press Enter to return...")


# =========================
# PROGRESS
# =========================

def view_progress():
    print("\n" + "=" * 50)
    print("YOUR PROGRESS")
    print("=" * 50)

    print(read_progress())

    input("\nPress Enter to return...")


def calculate_averages():
    if not os.path.exists("progress.txt"):
        return {}

    results = {}

    with open("progress.txt", "r", encoding="utf-8") as file:
        lines = file.readlines()

    for line in lines:

        if "|" not in line:
            continue

        parts = line.split("|")

        subject = parts[0].strip()

        if "Percentage:" in line:
            percentage_text = line.split("Percentage:")[1]
            percentage_text = percentage_text.replace("%", "").strip()

            try:
                percentage = float(percentage_text)

                if subject not in results:
                    results[subject] = []

                results[subject].append(percentage)

            except ValueError:
                pass

    averages = {}

    for subject, scores in results.items():
        if scores:
            averages[subject] = sum(scores) / len(scores)

    return averages


# =========================
# DETAILED PROGRESS
# =========================

def detailed_progress():
    print("\n" + "=" * 50)
    print("DETAILED PROGRESS")
    print("=" * 50)

    averages = calculate_averages()

    if not averages:
        print("There is not enough progress data yet.")
        print("Complete some practice sessions first.")
        input("\nPress Enter to return...")
        return

    print("\nYour average scores:")

    for subject, average in averages.items():
        print(f"{subject}: {average:.1f}%")

    weakest_subject = min(averages, key=averages.get)
    strongest_subject = max(averages, key=averages.get)

    print("\n" + "-" * 50)

    print(
        f"Strongest area: {strongest_subject} "
        f"({averages[strongest_subject]:.1f}%)"
    )

    print(
        f"Area to focus on: {weakest_subject} "
        f"({averages[weakest_subject]:.1f}%)"
    )

    print("\nPERSONALIZED RECOMMENDATION")

    weakest_score = averages[weakest_subject]

    if weakest_score < 50:
        print(
            f"Spend extra time on {weakest_subject}. "
            "Focus on basic concepts and review your mistakes."
        )

    elif weakest_score < 70:
        print(
            f"Your {weakest_subject} needs more practice. "
            "Practice regularly and review every mistake."
        )

    elif weakest_score < 85:
        print(
            f"You are doing well in {weakest_subject}. "
            "Focus on consistency and harder questions."
        )

    else:
        print(
            f"You are performing strongly in {weakest_subject}. "
            "Challenge yourself with more difficult questions."
        )

    input("\nPress Enter to return...")


# =========================
# SETTINGS
# =========================

def settings_menu():
    print("\n" + "=" * 50)
    print("SETTINGS")
    print("=" * 50)

    print(
        f"\nQuestions per practice session: "
        f"{settings['questions_per_session']}"
    )

    print("\n1. Set 3 questions")
    print("2. Set 5 questions")
    print("3. Set 10 questions")
    print("4. Back")

    choice = input("\nChoose: ").strip()

    if choice == "1":
        settings["questions_per_session"] = 3
        print("Practice sessions will now have 3 questions.")

    elif choice == "2":
        settings["questions_per_session"] = 5
        print("Practice sessions will now have 5 questions.")

    elif choice == "3":
        settings["questions_per_session"] = 10
        print("Practice sessions will now have 10 questions.")

    elif choice == "4":
        return

    else:
        print("Invalid choice.")

    input("\nPress Enter to return...")


# =========================
# SUBJECT MENU
# =========================

def practice_menu():

    subjects = list(questions.keys())

    while True:

        print("\n" + "=" * 50)
        print("PRACTICE QUESTIONS")
        print("=" * 50)

        for i, subject in enumerate(subjects, start=1):
            print(f"{i}. {subject}")

        print(f"{len(subjects) + 1}. Back")

        choice = input("\nChoose a subject: ").strip()

        if choice.isdigit():

            number = int(choice)

            if 1 <= number <= len(subjects):
                subject = subjects[number - 1]
                practice(subject)

            elif number == len(subjects) + 1:
                break

            else:
                print("Invalid choice.")

        else:
            print("Please enter a number.")


# =========================
# MAIN MENU
# =========================

def main():

    while True:

        print("\n")
        print("=" * 50)
        print("        AI STUDY ASSISTANT 5.0")
        print("=" * 50)

        print("1. Practice Questions")
        print("2. Study Tips")
        print("3. Study Plan")
        print("4. View Progress")
        print("5. Practice Mistakes")
        print("6. Detailed Progress")
        print("7. Settings / Extra Feature")
        print("8. Exit")

        choice = input("\nChoose an option: ").strip()

        if choice == "1":
            practice_menu()

        elif choice == "2":
            study_tips()

        elif choice == "3":
            study_plan()

        elif choice == "4":
            view_progress()

        elif choice == "5":
            practice_mistakes()

        elif choice == "6":
            detailed_progress()

        elif choice == "7":
            settings_menu()

        elif choice == "8":
            print("\n" + "=" * 50)
            print("Thank you for using AI Study Assistant 5.0!")
            print("Keep learning and improving!")
            print("=" * 50)
            break

        else:
            print("\nInvalid choice. Please try again.")


# =========================
# START PROGRAM
# =========================

if __name__ == "__main__":
    main()