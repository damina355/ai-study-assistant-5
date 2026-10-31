
import streamlit as st
import random
import importlib.util
from pathlib import Path


# -------------------------
# PAGE CONFIGURATION
# -------------------------

st.set_page_config(
    page_title="AI Study Assistant",
    page_icon="📚",
    layout="centered"
)


# -------------------------
# LOAD AI STUDY ASSISTANT 5
# -------------------------

project_folder = Path(__file__).resolve().parent

assistant_folder = (
    project_folder
    / "ai_chatbot"
    / "ai_study_assistant_4"
    / "ai_study_assistant_5"
)

assistant_file = assistant_folder / "main.py"

if not assistant_file.exists():
    st.error("Could not find AI Study Assistant 5.0.")
    st.write("Expected file location:")
    st.code(str(assistant_file))
    st.stop()

spec = importlib.util.spec_from_file_location(
    "assistant_v5",
    assistant_file
)

if spec is None or spec.loader is None:
    st.error("Could not load the original AI Study Assistant.")
    st.stop()

original_app = importlib.util.module_from_spec(spec)
spec.loader.exec_module(original_app)

questions = original_app.questions


# -------------------------
# SESSION DATA
# -------------------------

if "progress" not in st.session_state:
    st.session_state.progress = []

if "mistakes" not in st.session_state:
    st.session_state.mistakes = []

if "quiz" not in st.session_state:
    st.session_state.quiz = None

if "questions_per_session" not in st.session_state:
    st.session_state.questions_per_session = 5


# -------------------------
# HEADER
# -------------------------

st.title("📚 AI Study Assistant 5.0")

st.write(
    "Your personal learning assistant. "
    "Practice, review your mistakes and track your progress."
)

st.divider()


# -------------------------
# SIDEBAR
# -------------------------

st.sidebar.title("Navigation")

page = st.sidebar.radio(
    "Choose a section:",
    [
        "Home",
        "Practice Questions",
        "Study Tips",
        "Study Plan",
        "Practice My Mistakes",
        "My Progress",
        "Settings"
    ]
)


# -------------------------
# HOME
# -------------------------

if page == "Home":

    st.header("Welcome to AI Study Assistant!")

    st.write(
        "Improve your knowledge through regular practice "
        "and personalized learning."
    )

    col1, col2 = st.columns(2)

    with col1:
        st.metric(
            "Practice Sessions",
            len(st.session_state.progress)
        )

    with col2:
        st.metric(
            "Recorded Mistakes",
            len(st.session_state.mistakes)
        )

    st.subheader("What can you do?")

    st.write("📖 Practice questions in different subjects.")
    st.write("💡 Get useful study tips.")
    st.write("📅 Follow a weekly study plan.")
    st.write("🔁 Review your previous mistakes.")
    st.write("📊 Track your learning progress.")


# -------------------------
# PRACTICE QUESTIONS
# -------------------------

elif page == "Practice Questions":

    st.header("Practice Questions")

    quiz = st.session_state.quiz

    # Start a new session
    if quiz is None:

        subject = st.selectbox(
            "Choose a subject:",
            list(questions.keys())
        )

        difficulty = st.selectbox(
            "Choose difficulty:",
            ["All", "Easy", "Medium", "Hard"]
        )

        available = [
            item for item in questions[subject]
            if difficulty == "All"
            or item.get("difficulty") == difficulty
        ]

        st.write(f"Available questions: {len(available)}")

        if not available:

            st.warning(
                "No questions available for this difficulty."
            )

        elif st.button("Start Practice", type="primary"):

            selected = random.sample(
                available,
                min(
                    st.session_state.questions_per_session,
                    len(available)
                )
            )

            st.session_state.quiz = {
                "subject": subject,
                "questions": selected,
                "index": 0,
                "score": 0,
                "feedback": None,
                "completed": False,
                "percentage": 0
            }

            st.rerun()

    else:

        quiz = st.session_state.quiz

        total = len(quiz["questions"])

        # -------------------------
        # COMPLETED SESSION
        # -------------------------

        if quiz["completed"]:

            st.header("Practice Complete!")

            st.success("You have finished your practice session.")

            st.write(f"Subject: **{quiz['subject']}**")

            st.metric(
                "Your Score",
                f"{quiz['score']}/{total}"
            )

            st.metric(
                "Percentage",
                f"{quiz['percentage']:.1f}%"
            )

            if quiz["feedback"] is not None:

                if quiz["feedback"]["correct"]:
                    st.success("Your final answer was correct!")
                else:
                    st.info(
                        "Your final answer was incorrect. "
                        "Review the correct answer below."
                    )

                    st.write(
                        "Correct answer:",
                        quiz["feedback"]["answer"]
                    )

            if quiz["percentage"] >= 90:

                st.success("Excellent work!")

            elif quiz["percentage"] >= 70:

                st.success("Good job! Keep practicing.")

            elif quiz["percentage"] >= 50:

                st.info("You are making progress!")

            else:

                st.info(
                    "Review your mistakes and try again."
                )

            st.divider()

            if st.button("Start Another Session", type="primary"):

                st.session_state.quiz = None
                st.rerun()

        # -------------------------
        # ACTIVE SESSION
        # -------------------------

        else:

            index = quiz["index"]
            item = quiz["questions"][index]

            st.write(f"Subject: **{quiz['subject']}**")
            st.write(f"Difficulty: **{item.get('difficulty', 'Not specified')}**")

            st.progress((index + 1) / total)

            st.write(f"Question {index + 1} of {total}")

            st.subheader(item["question"])

            # Answer has not been submitted yet
            if quiz["feedback"] is None:

                with st.form(key=f"answer_form_{index}"):

                    user_answer = st.text_input("Your answer:")

                    submitted = st.form_submit_button(
                        "Check Answer"
                    )

                if submitted:

                    if not user_answer.strip():

                        st.warning("Please enter your answer.")

                    else:

                        correct_answer = str(item["answer"])

                        is_correct = (
                            user_answer.strip().lower()
                            == correct_answer.strip().lower()
                        )

                        quiz["feedback"] = {
                            "correct": is_correct,
                            "answer": correct_answer
                        }

                        if is_correct:

                            quiz["score"] += 1

                        else:

                            st.session_state.mistakes.append({
                                "subject": quiz["subject"],
                                "question": item["question"],
                                "your_answer": user_answer,
                                "correct_answer": correct_answer
                            })

                        # Finish the session after the last question
                        if index == total - 1:

                            quiz["completed"] = True

                            quiz["percentage"] = (
                                quiz["score"] / total
                            ) * 100

                            st.session_state.progress.append({
                                "Subject": quiz["subject"],
                                "Score": f"{quiz['score']}/{total}",
                                "Percentage": round(
                                    quiz["percentage"], 1
                                )
                            })

                        st.rerun()

            # Answer has been submitted
            else:

                if quiz["feedback"]["correct"]:

                    st.success("Correct! Great job!")

                else:

                    st.error("Incorrect. Keep learning!")

                    st.write(
                        "Correct answer:",
                        quiz["feedback"]["answer"]
                    )

                if st.button("Next Question", type="primary"):

                    quiz["index"] += 1
                    quiz["feedback"] = None

                    st.rerun()


# -------------------------
# STUDY TIPS
# -------------------------

elif page == "Study Tips":

    st.header("Study Tips")

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
            "Review why an answer is correct."
        ]
    }

    subject = st.selectbox(
        "Choose a subject:",
        list(tips.keys())
    )

    st.subheader(f"Tips for {subject}")

    for tip in tips[subject]:
        st.write("💡 " + tip)


# -------------------------
# STUDY PLAN
# -------------------------

elif page == "Study Plan":

    st.header("Personalized Study Plan")

    plan = {
        "Monday": [
            "Math practice",
            "Review mistakes",
            "Vocabulary"
        ],

        "Tuesday": [
            "IELTS reading",
            "Korean study",
            "Short SAT practice"
        ],

        "Wednesday": [
            "SAT Math",
            "Review difficult topics",
            "Vocabulary"
        ],

        "Thursday": [
            "IELTS practice",
            "Korean study",
            "Review mistakes"
        ],

        "Friday": [
            "SAT Verbal",
            "Math practice",
            "Weekly review"
        ],

        "Saturday": [
            "Longer SAT/IELTS practice session",
            "Review mistakes",
            "Work on weak areas"
        ],

        "Sunday": [
            "Light review",
            "Vocabulary",
            "Plan the next week",
            "Rest"
        ]
    }

    for day, tasks in plan.items():

        with st.expander(day):

            for task in tasks:

                st.checkbox(
                    task,
                    key=f"{day}_{task}"
                )


# -------------------------
# PRACTICE MY MISTAKES
# -------------------------

elif page == "Practice My Mistakes":

    st.header("Practice My Mistakes")

    mistakes = st.session_state.mistakes

    if not mistakes:

        st.info(
            "You have no recorded mistakes yet. "
            "Complete a practice session first."
        )

    else:

        st.write(f"Recorded mistakes: {len(mistakes)}")

        mistake_number = st.selectbox(
            "Choose a question to review:",
            range(len(mistakes)),
            format_func=lambda i: (
                f"{mistakes[i]['subject']} - "
                f"{mistakes[i]['question'][:45]}"
            )
        )

        mistake = mistakes[mistake_number]

        st.subheader(mistake["question"])

        answer = st.text_input(
            "Try answering again:",
            key=f"mistake_answer_{mistake_number}"
        )

        if st.button("Check My Answer"):

            if not answer.strip():

                st.warning("Please enter an answer.")

            elif (
                answer.strip().lower()
                == mistake["correct_answer"].strip().lower()
            ):

                st.success(
                    "Correct! You have improved on this question."
                )

            else:

                st.error("Not quite. Try reviewing the answer.")

                st.write(
                    "Correct answer:",
                    mistake["correct_answer"]
                )


# -------------------------
# MY PROGRESS
# -------------------------

elif page == "My Progress":

    st.header("My Learning Progress")

    progress = st.session_state.progress

    if not progress:

        st.info(
            "No progress recorded yet. "
            "Complete a practice session to see your results."
        )

    else:

        st.subheader("Practice History")

        st.dataframe(
            progress,
            use_container_width=True
        )

        averages = {}

        for result in progress:

            subject = result["Subject"]

            averages.setdefault(subject, [])

            averages[subject].append(
                result["Percentage"]
            )

        average_scores = {
            subject: round(sum(scores) / len(scores), 1)
            for subject, scores in averages.items()
        }

        st.subheader("Average Score by Subject")

        st.bar_chart(average_scores)

        weakest = min(
            average_scores,
            key=average_scores.get
        )

        strongest = max(
            average_scores,
            key=average_scores.get
        )

        col1, col2 = st.columns(2)

        with col1:

            st.metric(
                "Strongest Subject",
                strongest,
                f"{average_scores[strongest]}%"
            )

        with col2:

            st.metric(
                "Subject to Improve",
                weakest,
                f"{average_scores[weakest]}%"
            )


# -------------------------
# SETTINGS
# -------------------------

elif page == "Settings":

    st.header("Settings")

    st.write("Choose how many questions you want per session.")

    number = st.selectbox(
        "Questions per session:",
        [3, 5, 10],
        index=[3, 5, 10].index(
            st.session_state.questions_per_session
        )
    )

    st.session_state.questions_per_session = number

    st.success(
        f"Your practice sessions will have {number} questions."
    )


# -------------------------
# FOOTER
# -------------------------

st.divider()

st.caption(
    "AI Study Assistant 5.0 | Keep learning and improving!"
)
