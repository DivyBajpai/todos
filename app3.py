pip install streamlit
streamlit run app3.py



import streamlit as st
import time

# Set up the page configuration
st.set_page_config(page_title="To-Do List", page_icon="📝")

# Initialize the task list in session state
if 'tasks' not in st.session_state:
    st.session_state.tasks = []
    
if 'completed_tasks' not in st.session_state:
    st.session_state.completed_tasks = []

# Function to add a task
def add_task(task):
    st.session_state.tasks.append(task)

# Function to mark a task as completed
def complete_task(task):
    st.session_state.tasks.remove(task)
    st.session_state.completed_tasks.append(task)
    st.balloons()  # Add a confetti animation when a task is completed

# Display title
st.title("To-Do List App")

# Display instructions
st.markdown("""
    Welcome to your To-Do list! 
    - **Add** a task below.
    - **Mark** tasks as completed.
""")

# Task input form
with st.form(key="task_form"):
    task_input = st.text_input("Add a new task:")
    submit_button = st.form_submit_button(label="Add Task")
    
    if submit_button and task_input:
        add_task(task_input)
        st.success(f"Task '{task_input}' added!")

# Display existing tasks
if st.session_state.tasks:
    st.subheader("Pending Tasks")
    for task in st.session_state.tasks:
        col1, col2 = st.columns([4, 1])
        with col1:
            st.write(f"- {task}")
        with col2:
            if st.button(f"Mark '{task}' as Completed"):
                complete_task(task)

# Display completed tasks with animation
if st.session_state.completed_tasks:
    st.subheader("Completed Tasks")
    for task in st.session_state.completed_tasks:
        st.write(f"- {task}")

# Include a refresh option to update the list
if st.button("Refresh List"):
    time.sleep(0.5)  # Delay to trigger the animation
    st.experimental_rerun()

