import streamlit as st
import re

st.set_page_config(page_title="Password Strenth Meter", page_icon="🛅")

st.title("🔐 Password Strenth Checker")
st.markdown("""
### Welcome to the Password Strength Checker!👋
use this simple tool the check the strenght of your password and get suggestions on how to make stronger.
            we will give you helpfull way to create a **Strong Password** 🔒""")

password = st.text_input("Enter your Password", type="password")

feedback = []

score = 0

if password:
    if len(password) >= 8:
        score += 1
    else :
        feedback.append("❌password should be at least 8 chracter long.")
    if re.search(r'[A-Z]', password) and re.search(r'[a-z]', password):
        score += 1
    else:
        feedback.append("❌ Password should contain both upper and lower case characters.")
    if re.search(r'\d', password):
        score += 1
    else:
        feedback.append("❌ Password should be contain one didgit.") 
    if re.search(r'[!@#$%&*]', password):
        score += 1
        feedback.append("❌ Password should contain at least one special character(!@#$%&*).")
    if score == 4:
        feedback.append("✅ your password is strong!🎉")
    elif score == 3:
        feedback.append("your password is medium strenght. it could be stronger.")
    else:
        feedback.append("your password is weak. please make it stronger.")
    
    if feedback:
        st.markdown("## Improvement Suggestion")
        for tip in feedback:
            st.write(tip)
else:
    st.info("please enter your password and get started.")
        

