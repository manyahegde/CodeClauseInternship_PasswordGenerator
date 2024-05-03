import streamlit as st
import random
import string

def generate_password(length, use_numbers, use_symbols):
    characters = string.ascii_letters
    if use_numbers:
        characters += string.digits
    if use_symbols:
        characters += string.punctuation

    password = ''.join(random.choice(characters) for i in range(length))
    return password

def main():
    st.title("Password Generator")

    if 'passwords' not in st.session_state:
        st.session_state['passwords'] = []
        st.session_state['purposes'] = []

    # User input
    length = st.slider("Select password length", min_value=8, max_value=32, value=12)
    use_numbers = st.checkbox("Include numbers")
    use_symbols = st.checkbox("Include symbols")

    # Generate password
    if st.button("Generate Password"):
        password = generate_password(length, use_numbers, use_symbols)
        st.success("Your password: {}".format(password))

        # Update history
        st.session_state.passwords.append(password)
        st.session_state.purposes.append(None)  # Initialize purpose as None
        
        # Add Purpose
        idx = len(st.session_state.passwords) - 1
        new_purpose = st.text_input("Add Purpose for this password:", key=f"purpose_{idx}")
        if new_purpose:
            st.session_state.purposes[idx] = new_purpose

    # Display password history
    st.sidebar.title("Password History")
    for idx, (password, purpose) in enumerate(zip(st.session_state.passwords, st.session_state.purposes)):
        displayed_text = f"{password}"
        if purpose:
            displayed_text = f"{purpose}: {password}"
        st.sidebar.write(displayed_text)
        
        if st.sidebar.button("Delete", key=f"delete_{idx}"):
            st.session_state.passwords.pop(idx)
            st.session_state.purposes.pop(idx)

if __name__ == "__main__":
    main()
