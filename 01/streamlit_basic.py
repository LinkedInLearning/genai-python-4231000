import streamlit as st

if "user_inputs" not in st.session_state:
    st.session_state["user_inputs"] = []

st.title("Streamlit-Beispiel")

st.session_state["text"] = "Hallo Welt!"
st.write(st.session_state["text"])

st.chat_message("assistant", avatar="🌿").write("Hallo Welt!")
st.chat_message("user", avatar="🌍").write("Hallo Wäldchen!")

# Zeige alle vorherigen Nutzer-Nachrichten an
for msg in st.session_state["user_inputs"]:
    st.chat_message("user", avatar="🐱").write(msg)

if prompt := st.chat_input(placeholder="Schreib was!"):
    st.session_state["user_inputs"].append(prompt)
    st.chat_message("user", avatar="🐱").write(prompt)