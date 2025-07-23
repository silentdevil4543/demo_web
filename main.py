import streamlit as st

# st.title("Welcome to my profile")
# st.header("python")
# st.header("java")
# st.markdown("I love python")
# st.code("""for i in range(2,21,2):
#            print(i)
#         """)
name= st.text_input("Enter your name")
fname = st.text_input("enter your Father name")
adr = st.text_area("enter your text:")
classdata = st.selectbox("enter your class  :",(1,2,3,4,5,6,7,8,9))
button = st.button("done")
if button:
    st.markdown(f"""
    Name : {name},
    Father name: {fname},
    address : {adr},
    class :{classdata} """)

