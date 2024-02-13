import streamlit as st

# code from tutorial and video from streamlit site.
# First section demonstrates the basics of session_state.


st.title("Session State Basics")

"st.session_state object:", st.session_state

# if "a_counter" not in st.session_state:
#     st.session_state['a_counter'] = 0

# if 'boolean' not in st.session_state:
#     st.session_state.boolean = False

# st.write(st.session_state)

# st.write("a_counter is: ", st.session_state['a_counter'])
# st.write("boolean is: ", st.session_state.boolean)

# for the_key in st.session_state.keys():
#     st.write(the_key)

# for the_values in st.session_state.values():
#     st.write(the_values)

# for item in st.session_state.items():
#     item

# button = st.button("Update State")
# "before pressing button", st.session_state

# if button:
#     st.session_state['a_counter'] += 1
#     st.session_state.boolean = not st.session_state.boolean
#     "after pressing button", st.session_state

# for key in st.session_state.keys():
#     del st.session_state[key]


# Section 2 here gives further demo of session state
## this works with all widgets!

# number = st.slider("A number", 1, 10, key="slider")

# st.write(st.session_state)

# col1, buff, col2 = st.columns([1, 0.5, 3])

# option_names = ["a", "b", "c"]

# next_opt = st.button("Next Option")

# if next_opt:
#     if st.session_state["radio_option"] == 'a':
#         st.session_state.radio_option = 'b'
#     elif st.session_state["radio_option"] == 'b':
#         st.session_state.radio_option = 'c'
#     else:
#         st.session_state.radio_option = 'a'

# option = col1.radio("Pick an option", option_names, key="radio_option")
# st.session_state

# if option == 'a':
#     col2.write("You picked 'a' :smile:")
# elif option == 'b':
#     col2.write("You picked 'b' :heart:")
# else:
#     col2.write("You picked 'c' :rocket:")


# Section 3 demos the on_change callback functionality

def lbs_to_kg():
    st.session_state.kg = st.session_state.lbs/2.2046

def kg_to_lbs():
    st.session_state.lbs = st.session_state.kg*2.2046

col1, buff, col2 = st.columns([2,1,2])
with col1:
    pounds = st.number_input("Pounds:", key="lbs",
                             on_change=lbs_to_kg)

with col2:
    kilograms = st.number_input("Kiligrams:", key="kg",
                                on_change=kg_to_lbs)