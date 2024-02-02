import streamlit as st
import functions as fn

todos = fn.read_file_contents()


def add_todo():
    new_todo = st.session_state['todo'] + '\n'
    todos.append(new_todo)
    fn.write_file_contents(todos)


st.title('My ToDo App')
st.subheader('This is my todo app.')
st.write('This app is to increase your productivity.')

for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=todo)
    if checkbox:
        todos.pop(index)
        fn.write_file_contents(todos)
        del st.session_state[todo]
        st.rerun()

st.text_input('', placeholder='Enter a todo...',
              on_change=add_todo, key='todo')
