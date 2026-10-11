import streamlit as st
import random
from datetime import date
from sqlalchemy import text
import pandas as pd

st.set_page_config(page_title="SAT English Practice App", page_icon="📚", layout = "centered")

conn=st.connection("gramsat_db", type= "sql")
analytics = conn.query("SELECT * FROM dbo.ANALYTICS")

st.image("title_image.webp", width=300)
st.header("Welcome to GRAMSAT WHERE YOU CAN PRACTICE QUESTIONS ON THE SAT ENGLISH PORTION!")
st.subheader("You can asnwer up to two SAT (English) questions per day. Increase your streak by answering all the questions correctly and view your performance after answering all questions in the end!")
st.subheader("Please come back tomorrow for a new set of questions and to see your performance trend!")

if "streak" not in st.session_state:
    st.session_state.streak = -1

if "last_userlogin" not in st.session_state:
    st.session_state.last_userlogin = None

if "question_of_day" not in st.session_state:
    st.session_state.question_of_day = []

if "correct_option" not in st.session_state:
    st.session_state.correct_option = []

if "question_number" not in st.session_state:
    st.session_state.question_number = 0

if "username" not in st.session_state:
    st.session_state.username = ""


st.text_input("Enter your username:", key="username")

if "generate_disabled" not in st.session_state:
    st.session_state.generate_disabled = False

if "submit_disabled" not in st.session_state:
    st.session_state.submit_disabled = False


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

st.markdown("Please indicate whether this is your first time visiting this app or if you have visited before.\n If this is your first time, please enter a new username and remember your username for future logins to retrieve your performance data.\n If you have visited before, please enter your username you have used until now.")
user_visit_status = st.radio("Are you a new user or a returning user?", ["New User", "Returning User"])

generate_question = st.button("Click me Generate the Questions of the Day!", disabled=st.session_state.generate_disabled)

if generate_question:
    st.session_state.generate_disabled = True
    if not st.session_state.username:
        st.error("Please enter your username before generating questions.")
        st.session_state.generate_disabled = False
        st.stop()
    elif user_visit_status == "Returning User" and st.session_state.username not in analytics['USERNAME'].values:
        st.error("Username not found. Please enter a valid username or select 'New User' if you are a new user.")
        st.session_state.generate_disabled = False
        st.stop()
    elif user_visit_status == "New User" and st.session_state.username in analytics['USERNAME'].values:
        st.error(f"Username {st.session_state.username} already exists. Please enter a different username or select 'Returning User' if you have visited before with this username.")
        st.session_state.generate_disabled = False
        st.stop()
    else:
        user_logtimes = conn.query("Select LOGIN_TIME from dbo.ANALYTICS where USERNAME = :username", params={'username': st.session_state.username},ttl=0)
        with conn.session as s:
            if today not in user_logtimes['LOGIN_TIME'].values:
                s.execute(
                    text("INSERT INTO dbo.ANALYTICS (USERNAME, LOGIN_TIME) VALUES(:username, :login_time);"),
                    params={"username": st.session_state.username, "login_time": today}
                )
                s.commit()

    st.session_state.last_userlogin = conn.query("Select LOGIN_TIME from dbo.ANALYTICS where USERNAME = :username", params={'username': st.session_state.username},ttl=0)

    check_questions = conn.query("Select Q1, Q2 from dbo.ANALYTICS where USERNAME = :username and LOGIN_TIME = :login_time", params={'username': st.session_state.username, 'login_time': today},ttl=0)

    if not check_questions.empty and not check_questions.iloc[0].isna().any():
        st.write(f"Welcome back {st.session_state.username}! You have already generated the questions for today. Please answer them below.")

    if check_questions.empty or check_questions.iloc[0].isna().any(): 
        random_index_1 = random.randrange(0, len(questions))
        random_index_2 = random.randrange(0, len(questions))
        while random_index_2 == random_index_1:
            random_index_2 = random.randrange(0, len(questions))
        with conn.session as s:
            s.execute(
                text("UPDATE dbo.ANALYTICS SET Q1 = :q1, Q2 = :q2 WHERE USERNAME = :username AND LOGIN_TIME = :login_time;"),
                params={"q1": random_index_1, "q2": random_index_2, "username": st.session_state.username, "login_time": today}
            )
            s.commit()
    else:
        random_index_1 = check_questions.iloc[0]['Q1']
        random_index_2 = check_questions.iloc[0]['Q2']
        
    st.session_state.question_of_day = []
    st.session_state.correct_option = []

    st.session_state.question_of_day.append(questions[random_index_1])
    st.session_state.question_of_day.append(questions[random_index_2])

    st.session_state.correct_option.append(correct_answer_choice[random_index_1])
    st.session_state.correct_option.append(correct_answer_choice[random_index_2])

    st.session_state.question_number = 0


if st.session_state.question_of_day:
    qn = st.session_state.question_number
    q = st.session_state.question_of_day[qn]
    st.markdown(f"Question :\n{q[0]}")
    st.markdown("Answer Choices:")

    for choice in q[1:]:
        st.write(choice)
        
    user_answer = st.radio("Select your answer:", ['A','B','C','D'])
    st.write(f"Your answer is : {user_answer}")
    submit_button = st.button("Submit", disabled = st.session_state.submit_disabled)

    user_trial = conn.query("SELECT QUESTIONS_ATTEMPTED FROM dbo.ANALYTICS WHERE USERNAME = :username AND LOGIN_TIME = :login_time", params={'username': st.session_state.username, 'login_time': today}, ttl=0)
    if user_trial.iloc[0].isna().any():
        with conn.session as s:
            s.execute(
                text("UPDATE dbo.ANALYTICS SET QUESTIONS_ATTEMPTED = 0 WHERE USERNAME = :username AND LOGIN_TIME = :login_time;"),
                params={'username': st.session_state.username, 'login_time': today}
            )
            s.commit()
    if submit_button and user_trial.iloc[0]['QUESTIONS_ATTEMPTED'] < 2:
        st.session_state.submit_disabled = True
        if st.session_state.streak == -1:
            st.session_state.streak = 0
        if user_answer == st.session_state.correct_option[qn]:
            
            st.session_state.streak += 1
            st.success(f"Correct! Your streak is now: {st.session_state.streak}")
            st.balloons()
            
        else:
            st.error(f"Incorrect, Your streak is now: {st.session_state.streak}")

        with conn.session as s:
            s.execute(
                text("UPDATE dbo.ANALYTICS SET QUESTIONS_CORRECT = :streak WHERE USERNAME = :username AND LOGIN_TIME = :login_time;"),
                params={"streak": st.session_state.streak, "username": st.session_state.username, "login_time": today}
            )
            s.commit()
        #tracking the number of questions answered
        if qn == 0 and st.session_state.streak != -1:
            with conn.session as s:
                s.execute(
                    text("UPDATE dbo.ANALYTICS SET QUESTIONS_ATTEMPTED = 1 WHERE USERNAME = :username AND LOGIN_TIME = :login_time;"),
                    params={"username": st.session_state.username, "login_time": today}
                )
                s.commit()
        elif qn == 1 and st.session_state.streak != -1:
            with conn.session as s:
                s.execute(
                    text("UPDATE dbo.ANALYTICS SET QUESTIONS_ATTEMPTED = 2 WHERE USERNAME = :username AND LOGIN_TIME = :login_time;"),
                    params={"username": st.session_state.username, "login_time": today}
                )
                s.execute(
                    text("UPDATE dbo.ANALYTICS SET SCORE = :score WHERE USERNAME = :username AND LOGIN_TIME = :login_time;"),params={"score": st.session_state.streak/2 *100, "username": st.session_state.username, "login_time": today}
                )
                s.commit()
            
    elif submit_button and user_trial.iloc[0]['QUESTIONS_ATTEMPTED'] == 2:
        st.warning("You have already submitted your answers for today. Please come back tomorrow for new questions.")
        st.write("Click the 'Your Performance' button below to view your performance data in the present and past attempts.")

    if qn == 0 and st.session_state.streak >= 0:
        if st.button("Next Question", key="next_question"):
            st.session_state.submit_disabled = False
            st.session_state.question_number = 1
            st.rerun()

    if submit_button and qn == 1:
        st.write("You have completed today's questions. Please come back tomorrow for new questions.")
        st.write("Click the 'Your Performance' button below to view your performance data in the present and past attempts.")
    
    performance_button = False
    user_trial_completed = conn.query("SELECT QUESTIONS_ATTEMPTED FROM dbo.ANALYTICS WHERE USERNAME = :username AND LOGIN_TIME = :login_time", params={'username': st.session_state.username, 'login_time': today}, ttl=0)
    if user_trial_completed.iloc[0]['QUESTIONS_ATTEMPTED'] == 2:
        performance_button = st.button("Your Performance")
    if performance_button:
        score_data = conn.query("SELECT SCORE, LOGIN_TIME FROM dbo.ANALYTICS WHERE USERNAME = :username AND SCORE IS NOT NULL ORDER BY LOGIN_TIME ASC", params={"username": st.session_state.username},ttl=0)
        performance_df = pd.DataFrame({"Score": score_data["SCORE"].values}, index=pd.to_datetime(score_data["LOGIN_TIME"]).dt.strftime('%Y-%m-%d').values)
        print(performance_df)
        st.write("Your Performance Data:")
        if performance_df.size == 1:
            st.warning("Since this is your first time logging in, please hover your cursor over the chart to view your score. You will be able to clearly see the trend of your performance as you continue to answer questions in the future!")
            st.write("PLEASE COME BACK TOMORROW FOR NEW QUESTIONS TO SEE YOUR PERFORMANCE TREND!")
        st.line_chart(performance_df)
