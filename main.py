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
    if 'Mode' not in st.session_state:
        st.session_state.Mode = "Default"
    if 'Pomodoro_Count' not in st.session_state:
        st.session_state.Pomodoro_Count = 0
    if 'Distractions_Count' not in st.session_state:
        st.session_state.Distractions_Count = 0
    if 'Reflection' not in st.session_state:
        st.session_state.Reflection = "Default"
    if 'QuoteID' not in st.session_state:
        st.session_state.QuoteID = "Empty"
    if 'QuoteLines' not in st.session_state:
        st.session_state.QuoteLines = "Empty"

    #Remember session state
    if st.sidebar.button("Default Mode"):
        st.session_state.Mode = "Default"
    if st.sidebar.button("Work Mode"):
        st.session_state.Mode = "Work"
    if st.sidebar.button("Workout Mode"):
        st.session_state.Mode = "Workout"
    if st.sidebar.button("Calendar Mode"):
        st.session_state.Mode = "Calendar"

########################
##### DEFAULT MODE #####
########################
    col1, col2 = st.columns(2)
    with col1:
        #Date
        st.title(datetime.datetime.now().strftime("%A, %B %d"))

        #Time
        #st.title(current_time().strftime("%I:%M %p"))
        clock = st.container()
        #st.metric(label="Temperature", value="70 °F", delta="1.2 °F")
    if st.session_state.Mode == "Default":
         with col1:
            if st.button("Morning Reflection"):
                st.session_state.Reflection = "Morning"
                with col2:
                    tab1, tab2 = st.tabs(["Reflection", "Reminders"])
                    with tab1:
                        st.title("Morning Reflection")
                        st.caption("1. What must be done today?")
                        st.caption("2. What specific virtues should you improve on?")
                        st.caption("3. What do you have within you to face these challenges?")
                    with tab2:
                        st.header("Patience")
                        st.caption("Listen - First, try to understand other's viewpoints")
                        st.caption("Judge people by intention")
                        st.caption("Discipline of Assent - Choose your reaction")
                        st.header("Excellence")
                        st.caption("Be Resolute - admirably purposeful, unwavering, and determined")
                        st.caption("Be Industrious - don't let time waste away idling")


            if st.button("Evening Reflection"):
                st.session_state.Reflection = "Evening"
                with col2:
                    st.title("Evening Reflection")
                    st.caption("1. What have you done poorly?")
                    st.caption("2. What have you done well?")
                    st.caption("3. What opportunities did you miss to exercise virtue?")


            if st.button("Default"):
                st.session_state.Reflection = "Default"
            if st.session_state.Reflection == "Default":
                with col2:
                    tab1, tab2 = st.tabs(["Quote","Values"])
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
                            st.caption("I want to be a role model of a calm person")
                            st.caption("I want to address adversity with patience")
                            st.caption("I want to remember what is in my control")
                            st.caption("I want to avoid conflict with others when necessary and build cooperation")
                        with st.expander("Integrity"):
                            st.caption("I want to be able to give others good advice")
                            st.caption("I want to make good decisions")
                            st.caption("I want to be a role model of a calm person")
                            st.caption("I want to address adversity with patience")
                            st.caption("I want to quickly understand what is in my control")
                            st.caption("I want to avoid conflict with others when necessary and build cooperation")
                        with st.expander("Integrity"):
                            st.caption("I want to be able to make decisions I can be proud of")
                            st.caption("I want to always uphold a high standard")
                            st.caption("I want to avoid cutting corners")
                            st.caption("I want to use wisdom to determine when and where I should make a stand")
                        with st.expander("Resolution"):
                            st.caption("Admirably purposeful, determined, unwavering")
                            st.caption("No wasted days")


#####################
##### WORK MODE #####
#####################
    if st.session_state.Mode == "Work":
        with col1:
            st.button("Focus Mode")
            if st.button("Meeting Mode"):
                with col2:
                    for idx in range(0, len(meetingPrep())):
                        st.header(meetingPrep()[idx, 0])
            if st.button("Presentation Checklist"):
                with col2:
                    st.write("Is there a key takeaway highlighted?")
                    st.write("Is there a key takeaway highlighted?")
            if st.button("Record Mode"):
                pass
                # TODO: Record buffered meeting interaction
            else:
                with col2:
                    tab1,tab2 = st.tabs(["Timer", "Settings"])
                    work_minutes = 25
                    with tab1:
                        if st.button("Work Timer"):
                            pass
                        if st.button("Break Timer"):
                            st.session_state.Pomodoro_Count +=1
                        if st.button("Distractions Count"):
                            st.session_state.Distractions_Count +=1
                        if st.button("Reset"):
                            st.session_state.Pomodoro_Count = 0
                            st.session_state.Distractions_Count = 0
                        st.metric(label="Pomodoro Count", value=st.session_state.Pomodoro_Count)
                        st.metric(label="Distractions_Count", value=st.session_state.Distractions_Count)
                    with tab2:
                        work_minutes = st.number_input("Enter work time in minutes: ", min_value = 1, value = 25)
                        work_seconds = work_minutes*60
                        break_minutes = st.number_input("Enter break time in minutes: ", min_value=1, value=10)
                        break_seconds = break_minutes * 60



########################
##### WORKOUT MODE #####
########################

    if st.session_state.Mode == "Workout":
        with col1:
            pass
        with col2:
            image = Image.open('elmo.jpg')
            st.image(image)
            st.metric(label="Next Set Time", value=(datetime.datetime.now()+datetime.timedelta(minutes=2)).strftime("%I:%M:%S %p"), delta="2 min")
            st.number_input("Sets Completed", min_value=0, max_value=5, step=1, value=0)



#########################
##### CALENDAR MODE #####
#########################
    if st.session_state.Mode == "Calendar":
        with col1:
            st.button("Save Results")
            # TODO: Store results
            st.button("View Results")
            # TODO: View results

        with col2:
            tab1,tab2,tab3 = st.tabs(["Mandatory","Tasks","Growth"])
            with tab1:
                mandatory_scored = st.number_input("Mandatory Points Scored", min_value=1, max_value=100, step=1, value = 1)
                mandatory_failed = st.number_input("Mandatory Points Failed", min_value=0, max_value=100, step=1, value = 0)
                st.metric(label="Score", value=str(mandatory_scored) + "/"+ str(mandatory_failed+mandatory_scored))
                st.metric(label="Percentage", value=str(mandatory_scored / (mandatory_failed + mandatory_scored)*100) +"%")
            with tab2:
                tasks_scored = st.number_input("Tasks Points Scored", min_value=1, max_value=100, step=1, value = 1)
                tasks_failed = st.number_input("Tasks Points Failed", min_value=0, max_value=100, step=1, value = 0)
                st.metric(label="Score", value=str(tasks_scored) + "/"+ str(tasks_failed+tasks_scored))
                st.metric(label="Percentage", value=str(tasks_scored / (tasks_failed + tasks_scored)*100) +"%")
            with tab3:
                growth_scored = st.number_input("Growth Points Scored", min_value=1, max_value=100, step=1, value = 1)
                growth_failed = st.number_input("Growth Points Failed", min_value=0, max_value=100, step=1, value = 0)
                st.metric(label="Score", value=str(growth_scored) + "/"+ str(growth_failed+growth_scored))
                st.metric(label="Percentage", value=str(growth_scored / (growth_failed + growth_scored)*100) +"%")
    with clock:
        #asyncio.run(current_time(clock))
        pass

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
