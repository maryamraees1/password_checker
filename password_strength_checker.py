import re
import streamlit as st

def check_password_strength(password):
    score = 0
    messages=[]
    # Length Check
    if len(password) >= 8:
        score += 1
    else:
       messages.append( "❌ Password should be at least 8 characters long.")
    
    # Upper & Lowercase Check
    if re.search(r"[A-Z]", password) and re.search(r"[a-z]", password):
        score += 1
    else:
        messages.append("❌ Include both uppercase and lowercase letters")
    
    # Digit Check
    if re.search(r"\d", password):
        score += 1
    else:
         messages.append( "❌ Add at least one number (0-9).")
    
    # Special Character Check
    if re.search(r"[@*_]", password):
        score += 1
    else:
        messages.append( "❌ Include at least one special character (@*_).")
     
    # Strength Rating
    if score == 4:
        messages.append("✅ Strong Password!")
        st.balloons()
        st.success("GOOD JOB!!!")
         
    elif score == 3:
        messages.append( "⚠️ Moderate Password - Consider adding more security features.")
    else:
        messages.append( "❌ Weak Password - Improve it using the suggestions above.")
    return messages   
 

# UI
st.title("Is Your Password Strong Enough? 🔓")
# Get user input
show_password=st.checkbox("👁️")
password=st.text_input('Enter your password :',type="default" if show_password else "password" )
if st.button("Check Password") and password:
    result = check_password_strength(password)
    for msg in result:
        if "✅" in msg:
            st.success(msg)
        elif "⚠️" in msg:
            st.warning(msg)
        else:
            st.error(msg)
# guidlines of password
with st.container():
    st.subheader("Guidlines for strong Password:")
    st.markdown("""
- ✅ Be at least 8 characters long
- ✅ Contain uppercase & lowercase letters
- ✅ Include at least one digit (0-9)
- ✅ Have one special character (@*_) """)