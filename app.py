import streamlit as st
import random
from datetime import date


st.header("Welcome to GRAMSAT!")
st.subheader("You will be asked two SAT grammer questions. Answer the first question correctly to move on to the second one. Increase your streak by answering them correctly!")

if "streak" not in st.session_state:
    st.session_state.streak = 0

if "last_userlogin" not in st.session_state:
    st.session_state.last_userlogin = None

if "question_of_day" not in st.session_state:
    st.session_state.question_of_day = []

if "correct_option" not in st.session_state:
    st.session_state.correct_option = []

if "question_number" not in st.session_state:
    st.session_state.question_number = 0

questions = [
    [
        "Each of the new interns ________ responsible for attending the orientation session.",
        "A. are",
        "B. were",
        "C. has been",
        "D. have been"
    ],
    [
        "The company’s recent product launch broke sales records. ________, its marketing campaign was widely praised for creativity.",
        "A. However",
        "B. Therefore",
        "C. In contrast",
        "D. Likewise"
    ],
    [
        "Neither the assistant nor the manager ________ authorized to make hiring decisions.",
        "A. is",
        "B. are",
        "C. be",
        "D. were"
    ],
    [
        "The museum’s collection of modern art, including works by abstract painters, ________ displayed in a newly renovated wing.",
        "A. are",
        "B. is",
        "C. have been",
        "D. were"
    ],
    [
        "The author argues that technology improves communication. ________, she acknowledges that it can also lead to isolation.",
        "A. Nevertheless",
        "B. For example",
        "C. Consequently",
        "D. Likewise"
    ],
    [
        "The debate team, as well as the coaches, ________ traveling to the regional competition this weekend.",
        "A. are",
        "B. is",
        "C. were",
        "D. have"
    ],
    [
        "Unlike her colleagues, who were content with average performance, Maria consistently ________ to exceed expectations.",
        "A. strive",
        "B. strived",
        "C. strives",
        "D. striving"
    ],
    [
        "Social media has drastically changed how people interact. ________, it has also raised concerns about mental health.",
        "A. In conclusion",
        "B. On the other hand",
        "C. Similarly",
        "D. As a result"
    ],
    [
        "The book, along with its sequel, ________ recommended reading in many literature courses.",
        "A. are",
        "B. were",
        "C. is",
        "D. be"
    ],
    [
        "The architect’s original design was rejected. ________, a revised version was accepted after much deliberation.",
        "A. For example",
        "B. However",
        "C. Consequently",
        "D. Meanwhile"
    ],
    [
        "Either the intern or the manager ________ attending the training session.",
        "A. are",
        "B. is",
        "C. have",
        "D. be"
    ],
    [
        "The hikers, exhausted from the steep climb, ________ at the summit before beginning their descent.",
        "A. pause",
        "B. paused",
        "C. pausing",
        "D. has paused"
    ],
    [
        "Some scientists believe climate change is accelerating. ________, others argue that the data is inconclusive.",
        "A. In other words",
        "B. Therefore",
        "C. In contrast",
        "D. As a result"
    ],
    [
        "A number of students ________ interested in joining the robotics club.",
        "A. is",
        "B. are",
        "C. was",
        "D. has been"
    ],
    [
        "The manager, not the assistants, ________ responsible for finalizing the report.",
        "A. are",
        "B. is",
        "C. were",
        "D. be"
    ],
    [
        "Many of the proposals were rejected. ________, one unexpected idea gained overwhelming support.",
        "A. Similarly",
        "B. In contrast",
        "C. Therefore",
        "D. Likewise"
    ],
    [
        "The statue, along with the fountain and garden, ________ part of the city’s historical tour.",
        "A. are",
        "B. is",
        "C. be",
        "D. have"
    ],
    [
        "Neither the essay nor the speech ________ included a clear thesis.",
        "A. was",
        "B. were",
        "C. are",
        "D. be"
    ],
    [
        "He completed the project efficiently and submitted it early. ________, his peers struggled to meet the deadline.",
        "A. Nevertheless",
        "B. For instance",
        "C. Similarly",
        "D. On the contrary"
    ],
    [
        "The university, as well as several research institutions, ________ investigating the new treatment.",
        "A. are",
        "B. is",
        "C. be",
        "D. were"
    ],
    [
        "The team ________ eager to start the match, despite the heavy rain.",
        "A. were",
        "B. was",
        "C. are",
        "D. be"
    ],
    [
        "The scientist published her findings. ________, they sparked a debate among experts.",
        "A. Furthermore",
        "B. In contrast",
        "C. Subsequently",
        "D. Likewise"
    ],
    [
        "A pack of wolves ________ spotted near the forest edge.",
        "A. were",
        "B. have",
        "C. was",
        "D. be"
    ],
    [
        "The council, not the residents, ________ responsible for enforcing the regulation.",
        "A. are",
        "B. is",
        "C. be",
        "D. were"
    ],
    [
        "The company faced backlash for its hiring practices. ________, it began revising its policies to promote diversity.",
        "A. However",
        "B. Consequently",
        "C. In contrast",
        "D. For example"
    ],
    [
        "Neither the laptop nor the tablet ________ compatible with the new software.",
        "A. are",
        "B. were",
        "C. is",
        "D. be"
    ],
    [
        "The athletes, tired but determined, ________ to finish the final lap.",
        "A. continue",
        "B. continues",
        "C. continued",
        "D. continuing"
    ],
    [
        "The engineer reviewed the designs thoroughly. ________, the final product met all safety standards.",
        "A. For instance",
        "B. In contrast",
        "C. As a result",
        "D. Nonetheless"
    ],
    [
        "Each of the dancers ________ a solo performance at the end of the show.",
        "A. perform",
        "B. performs",
        "C. performing",
        "D. have performed"
    ],
    [
        "The report was well-written. ________, it lacked enough data to support its claims.",
        "A. Therefore",
        "B. Likewise",
        "C. Nevertheless",
        "D. Subsequently"
    ]
]

correct_answer_choice = [
    'C', # 1
    'D', # 2
    'A', # 3
    'B', # 4
    'A', # 5
    'B', # 6
    'C', # 7
    'B', # 8
    'C', # 9
    'C', # 10
    'B', # 11
    'B', # 12
    'C', # 13
    'B', # 14
    'B', # 15
    'B', # 16
    'B', # 17
    'A', # 18
    'D', # 19
    'B', # 20
    'B', # 21
    'C', # 22
    'C', # 23
    'B', # 24
    'B', # 25
    'C', # 26
    'C', # 27
    'C', # 28
    'B', # 29
    'C'  # 30
]
today = date.today()
generate_question = st.button("Click me Generate the Questions of the Day!")


if generate_question and st.session_state.last_userlogin != today :
    random_index_1 = random.randrange(0, len(questions))
    random_index_2 = random.randrange(0, len(questions))
    while random_index_2 == random_index_1:
        random_index_2 = random.randrange(0, len(questions))

    st.session_state.question_of_day = []
    st.session_state.correct_option = []

    st.session_state.question_of_day.append(questions[random_index_1])
    st.session_state.question_of_day.append(questions[random_index_2])

    st.session_state.correct_option.append(correct_answer_choice[random_index_1])
    st.session_state.correct_option.append(correct_answer_choice[random_index_2])

    st.session_state.last_userlogin = today

    st.session_state.question_number = 0


if st.session_state.question_of_day is not None and st.session_state.last_userlogin == today:
    qn = st.session_state.question_number
    q = st.session_state.question_of_day[qn]
    st.markdown(f"Question :\n{q[0]}")
    st.markdown("Answer Choices:")

    for choice in q[1:]:
        st.write(choice)
        
    user_answer = st.radio("Select your answer:", ['A','B','C','D'])
    st.write(f"Your answer is : {user_answer}")
    submit_button = st.button("Submit")

    if submit_button:
        if user_answer == st.session_state.correct_option[qn]:
            st.session_state.streak += 1
            st.success(f"Correct! Your streak is now: {st.session_state.streak}")
            st.balloons()
        else:
            st.session_state.streak = 0
            st.error(f"Incorrect, please try again ! Your streak is now: {st.session_state.streak}")

    if qn == 0 and st.session_state.streak > 0:
        if st.button("Next Question", key="next_question"):
            st.session_state.question_number = 1
            st.rerun()
