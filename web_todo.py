import streamlit as st
import functions

def add_todo():
    todo =st.session_state["new_todo"] + "\n"
    todos.append(todo)
    functions.write_todos(todos)


todos = functions.get_todos()

st.title("My Todo App")
st.subheader("This are my Todos")
st.write("This app to help track your <b>activities.</b>",
         unsafe_allow_html=True)

for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo,key=todo)
    if checkbox:
        todos.pop(index)
        functions.write_todos(todos)
        del st.session_state[todo]
        st.experimental_rerun()

st.text_input(label=" ",placeholder="Add new todo....",
              on_change=add_todo, key="new_todo")

print("ok")
