import streamlit as st
import random
import string

def generate_password(length, use_numbers, use_symbols):
    characters = string.ascii_letters
    if use_numbers:
        characters += string.digits
    if use_symbols:
        characters += string.punctuation

    password = ''.join(random.choice(characters) for _ in range(length))
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
        st.session_state.purposes.append("")  # Initialize purpose as an empty string

    # Display password history
    st.sidebar.title("Password History")
    for idx, (password, purpose) in enumerate(zip(st.session_state.passwords, st.session_state.purposes)):
        displayed_text = f"{password}"
        if purpose:
            displayed_text = f"{password} ({purpose})"
        st.sidebar.write(displayed_text)

        # Add Purpose forms and Delete button
        if not purpose:  # Only show the input box if purpose is not set
            with st.sidebar:
                with st.form(key=f"purpose_form_{idx}"):
                    new_purpose = st.text_input(f"Add Purpose for password {idx + 1}:", value=st.session_state.purposes[idx])
                    submit_purpose = st.form_submit_button("Submit")
                    if submit_purpose:
                        st.session_state.purposes[idx] = new_purpose
                        st.experimental_rerun()  # Rerun to update the sidebar

        with st.sidebar:
            if st.button(f"Delete {idx}", key=f"delete_{idx}"):
                st.session_state.passwords.pop(idx)
                st.session_state.purposes.pop(idx)
                st.experimental_rerun()  # Rerun the app to refresh the sidebar

if __name__ == "__main__":
    main()
