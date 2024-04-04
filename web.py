import streamlit as st
import functions

todos = functions.get_todos()
def add_todo():
    todo = st.session_state["new_todo"] + "\n" # Para obtener el valor que escribamos en la text box que tiene la key "new_todo"
    todos.append(todo)
    functions.write_todos(todos)
    st.session_state["new_todo"] = ""


st.title("My todo App")
st.subheader("This is my todo app")
st.write("This app is to increase your productivity.")

for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=todo)
    if checkbox:
        todos.pop(index)
        functions.write_todos(todos)
        del st.session_state[todo]
        st.rerun()


# "on_change" es una función, "key=" es un identificador para este elemento.
st.text_input(label=" ", placeholder="Add new todo...", on_change=add_todo, key="new_todo")
