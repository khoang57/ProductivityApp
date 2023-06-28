from HabitsMode import *
from WorkMode import *
from ProductivityUtils import *
import datetime
import streamlit as st
import threading
from PIL import Image

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    st.set_page_config(
        page_title="Productivity",
        layout="wide",
        initial_sidebar_state="expanded"
    )

    st.markdown("""
            <style>
                   .css-18e3th9 {
                        padding-top: 0rem;
                        padding-bottom: 10rem;
                        padding-left: 5rem;
                        padding-right: 5rem;
                    }
                   .css-1d391kg {
                        padding-top: 3.5rem;
                        padding-right: 1rem;
                        padding-bottom: 3.5rem;
                        padding-left: 1rem;
                    }
            </style>
            """, unsafe_allow_html=True)

    m = st.markdown("""
    <style>
    div.stButton > button:first-child {
        background-color: #2e86c5;
        height:3em;
        width:13em;
    
    }
    button:focus{background-color: #ffffff ;}
    </style>""", unsafe_allow_html=True)

    # Set modes based on buttons
    if st.sidebar.button("Default Mode"):
        st.session_state.Mode = "Default"
    if st.sidebar.button("Work Mode"):
        st.session_state.Mode = "Work"
    if st.sidebar.button("Workout Mode"):
        st.session_state.Mode = "Workout"
    if st.sidebar.button("Calendar Mode"):
        st.session_state.Mode = "Calendar"

    if 'Mode' not in st.session_state:
        st.session_state.Mode = "Default"

    col1, col2 = st.columns(2)
    with col1:
        #Date
        st.title(datetime.datetime.now().strftime("%A, %B %d"))
        #Time
        st.title(datetime.datetime.now().strftime("%I:%M %p"))
        #clock = st.container()
        #Temperature
        #st.metric(label="Temperature", value="70 °F", delta="1.2 °F")

########################
##### DEFAULT MODE #####
########################

    ##### Initialize default state #####
    if st.session_state.Mode == "Default":
        if "DefaultMode" not in st.session_state:
            st.session_state.DefaultMode = "Default"
        if 'QuoteID' not in st.session_state:
            st.session_state.QuoteID = "Empty"
        if 'QuoteLines' not in st.session_state:
            st.session_state.QuoteLines = "Empty"

    ##### Set modes based on buttons #####
        if st.session_state.Mode == "Default":
             with col1:
                if st.button("Default"):
                    st.session_state.DefaultMode = "Default"
                if st.button("Morning Reflection"):
                    st.session_state.DefaultMode = "Morning"
                if st.button("Evening Reflection"):
                    st.session_state.DefaultMode = "Evening"

    ##### Set outputs based on modes #####

        ### Mode 1 - Morning ###
        if st.session_state.DefaultMode == "Morning":
            with col2:
                st.title("Morning Reflection")
                st.caption("1. What must be done today for you to feel satisfied?")
                st.caption("2. What opportunities do you have to improve on specific virtues?")
                st.caption("3. What resources do you have to face these challenges? (Reminders/checklists)")


        ### Mode 2 - Evening ###
        if st.session_state.DefaultMode == "Evening":
            with col2:
                st.title("Evening Reflection")
                st.caption("1. What have you done poorly?")
                st.caption("2. What have you done well?")
                st.caption("3. What opportunities did you miss to exercise virtue?")

        ### Mode 3 - Default ###
        if st.session_state.DefaultMode == "Default":
            with col2:
                tab1, tab2, tab3 = st.tabs(["Quote","Values","Reminders"])
                with tab1:
                    if st.session_state.QuoteID == "Empty":
                        quote, num_lines = quotes()
                        st.session_state.QuoteID = quote
                        st.session_state.QuoteLines = num_lines
                    for j in st.session_state.QuoteID:
                        if st.session_state.QuoteLines > 5:
                            st.subheader(j)
                        else:
                            st.header(j)
                with tab2:
                    with st.expander("Wisdom"):
                        st.caption("I want to be able to give others good advice")
                        st.caption("I want to make good decisions ")
                        st.caption("I want to be an example for others")
                        st.caption("I want to address adversity with patience")
                        st.caption("I want to focus on what is in my control, and care less about other things")
                        st.caption("I want to work to build with others")
                    with st.expander("Kindness"):
                        st.caption("I want to be patient and understanding of others")
                        st.caption("I want to ease people's concerns")
                        st.caption("I want to be a role model in the world I want to see")
                    with st.expander("Integrity"):
                        st.caption("I want to be able to make decisions I can be proud of")
                        st.caption("I want to always uphold a high standard and avoid cutting corners")
                        st.caption("I want to use wisdom to determine when and where I should make a stand")
                    with st.expander("Resolution"):
                        st.caption("Admirably purposeful, determined, unwavering")
                        st.caption("No wasted days")
                with tab3:
                    st.header("Patience")
                    st.caption("Listen, Don't Interrupt - First, try to understand other's viewpoints")
                    st.caption("Discipline of Assent - Choose your reaction")
                    st.caption("Don't get overly excited")
                    st.header("Excellence")
                    st.caption("Be Resolute - admirably purposeful, unwavering, and determined")
                    st.caption("Be Industrious - don't let time waste away idling")
                    st.header("Charisma")
                    st.caption("Maintain eye contact")
                    st.caption("Control your speech")
                    st.caption("Control your body - eyes/unnecessary movement")



#####################
##### WORK MODE #####
#####################

    ##### Initialize default state ####
    if st.session_state.Mode == "Work":
        if "WorkMode" not in st.session_state:
            st.session_state.WorkMode = "Focus"
        if 'Pomodoro_Count' not in st.session_state:
            st.session_state.Pomodoro_Count = 0
        if 'Distractions_Count' not in st.session_state:
            st.session_state.Distractions_Count = 0

    ##### Set modes based on buttons ####
        with col1:
            if st.button("Focus Mode"):
                st.session_state.WorkMode = "Focus"
            if st.button("Meeting Mode"):
                st.session_state.WorkMode = "Meeting"
            if st.button("Presentation Checklist"):
                st.session_state.WorkMode = "Presentation"

    ##### Output based on modes #####

        ### Mode 1 - Focus ###
            if st.session_state.WorkMode == "Focus":
                with col2:
                    tab1, tab2 = st.tabs(["Timer", "Settings"])
                    work_minutes = 25
                with tab1:
                    if st.button("Work Timer"):
                        pass
                    if st.button("Break Timer"):
                        st.session_state.Pomodoro_Count += 1
                    if st.button("Distractions Count"):
                        st.session_state.Distractions_Count += 1
                    if st.button("Reset"):
                        st.session_state.Pomodoro_Count = 0
                        st.session_state.Distractions_Count = 0
                    st.metric(label="Pomodoro Count", value=st.session_state.Pomodoro_Count)
                    st.metric(label="Distractions_Count", value=st.session_state.Distractions_Count)
                with tab2:
                    work_minutes = st.number_input("Enter work time in minutes: ", min_value=1, value=25)
                    work_seconds = work_minutes * 60
                    break_minutes = st.number_input("Enter break time in minutes: ", min_value=1, value=10)
                    break_seconds = break_minutes * 60

        #### Mode 2 - Meeting ###
            if st.session_state.WorkMode == "Meeting":
                with col2:
                    #for idx in range(0, len(meetingPrep())):
                    #    st.subheader(meetingPrep()[idx, 0])
                    st.subheader("Listen")
                    st.write("Wait for others to finish speaking")
                    st.write("Withhold Judgement")
                    st.subheader("Speak with Intention and Poise")
                    st.write("Think before you speak")
                    st.write("Speak slowly and clearly")
                    st.write("No filler words")
                    st.write("Acknowledge - Clarify and repeat")
                    st.subheader("Body Language")
                    st.write("Don't nod too often")
                    st.write("Don't make too many movements")


        ### Mode 3 - Presentation ###
            if st.session_state.WorkMode == "Presentation":
                with col2:
                     st.subheader("Is there a key takeaway highlighted?")
                     st.subheader("Are supporting graphics maximized?")
                     st.subheader("Is wordiness minimized?")

########################
##### WORKOUT MODE #####
########################
    ##### Initialize default state ####
    if st.session_state.Mode == "Workout":
        if "NextSetTime" not in st.session_state:
            st.session_state.NextSetTime = 0

    ##### Set modes based on buttons ####

    ##### Output based on modes #####

        with col1:
            with st.expander("Chest & Triceps"):
                st.write("Incline Bench: 12/10/10/8 at 35- (IMPROVE FORM, consider lowering)")
                st.write("Bench: 12/10/10/8 at 40 (Improve amount)") ## 12/10/10/8
                st.write("Bench Flys: 3x12 at 25 (correct form)")
                st.write("Tricep Kickback 3x12 at 22.5 (IMPROVE FORM)")

            with st.expander("Back and Biceps"):
                st.write("One Arm Dumbbell Row: 12/10/10/8/6 at 45+")
                st.write("Standing Dumbell Row: 12/10/10/8/6 at 35 (Squeeze shoulders - 12x5)")
                st.write("Dumbell Pullover: 12/10 at 40-")
                st.write("Incline Dumbbell Curl: 3x10+ at 17.5 (do 12-- now)")
                st.write("Standing Dumbbell Curl: 3x10+ at 17.5 (do 12-- now)")
                st.write("Cross Body Hammer Curl: 2x10+ at 17.5 (do 12-- now)")


            with st.expander("Legs and Shoulders"):
                st.write("Dumbbell Lunge: 12/10/10/8 at 15+")
                st.write("Dumbell Standing Calf Raise: 12/10 at 15")
                st.write("Dumbbell Step Up: 3x12 at 30")
                st.write("Dumbbell Squat Flys: 12/10/10/8 at 15+")
                st.write("Dumbbell Stiff Leg Deadlift: 12/10/10/8 at 15+")
                st.write("Seated Dumbbell Calf Raise: 15/12 at 15+")


        with col2:
            image = Image.open('elmo.jpg')
            st.image(image)
            st.metric(label="Next Set Time", value=(datetime.datetime.now()+datetime.timedelta(minutes=2)).strftime("%I:%M:%S %p"), delta="2 min")
            st.session_state.NextSetTime = st.number_input("Sets Completed", min_value=0, max_value=5, step=1, value=0)






#########################
##### CALENDAR MODE #####
#########################

    ##### Initialize default state ####
    if st.session_state.Mode == "Calendar":
        if "CalendarMode" not in st.session_state:
            st.session_state.CalendarMode = "Calendar"
        pass
    ##### Set modes based on buttons ####
        with col1:
            if st.button("Calendar"):
                st.session_state.CalendarMode = "Calendar"
            if st.button("Productivity Calculator"):
                st.session_state.CalendarMode = "Calculator"

    ##### Set outputs based on modes #####

        ### Mode 1 - Calendar ###

        ### Mode 2 - Calculator ###
        if st.session_state.CalendarMode == "Calculator":
            with col2:
                tab1,tab2,tab3 = st.tabs(["Mandatory","Tasks","Growth"])
                with tab1:
                    mandatory_scored = st.number_input("Mandatory Points Scored", min_value=1, max_value=100, step=1, value = 1)
                    mandatory_failed = st.number_input("Mandatory Points Failed", min_value=0, max_value=100, step=1, value = 0)
                    st.metric(label="Percentage", value=str(mandatory_scored / (mandatory_failed + mandatory_scored)*100) +"%")
                    st.metric(label="Score", value=str(mandatory_scored) + "/"+ str(mandatory_failed+mandatory_scored))
                with tab2:
                    tasks_scored = st.number_input("Tasks Points Scored", min_value=1, max_value=100, step=1, value = 1)
                    tasks_failed = st.number_input("Tasks Points Failed", min_value=0, max_value=100, step=1, value = 0)
                    st.metric(label="Percentage", value=str(tasks_scored / (tasks_failed + tasks_scored)*100) +"%")
                    st.metric(label="Score", value=str(tasks_scored) + "/"+ str(tasks_failed+tasks_scored))
                with tab3:
                    growth_scored = st.number_input("Growth Points Scored", min_value=1, max_value=100, step=1, value = 1)
                    growth_failed = st.number_input("Growth Points Failed", min_value=0, max_value=100, step=1, value = 0)
                    st.metric(label="Percentage", value=str(growth_scored / (growth_failed + growth_scored)*100) +"%")
                    st.metric(label="Score", value=str(growth_scored) + "/"+ str(growth_failed+growth_scored))
                st.button("Save Results")
                # TODO: Store results
                st.button("View Results")
                # TODO: View results
                st.button("Reset Results")
                # TODO: Reset results

    #with clock:
        #asyncio.run(current_time(clock))
        #pass

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
