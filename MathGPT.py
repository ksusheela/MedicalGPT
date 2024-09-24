import streamlit as st
import openai


# st.title("GEN AI Application")
# st.header("Math_GPT")

# set openAI API key

api_key = "Use your openai API key to access this allication."
openai.api_key = api_key

def ask_math_question(question):
    
    # Create a conversation with the user's question and AI responses
    conversation = [
        {"role": "system", "content": "You are a math tutor."}, # AI Role
        {"role": "user", "content": question}
    ]

    # Generate a response from GPT-3 
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=conversation
    )

    # Extract and return the model's reply
    reply = response['choices'][0] ['message']['content']
    return reply

def main():
    st.title("Math GPT - Math Assistant")
    
    # Define a user profile with user-specific settings(language, units, etc.)
    user_profile = {
        "language": "English",
        "preferred_units": "imperial",
        
        #Add more user_specific settings here
        
    }
    
    # Siderbar for user profile customizations
    st.sidebar.header("User profile dettings")
    user_profile["laguage"] = st.selectbox("Language", ["English", "Danish","Hindi","Telugu"])
    user_profile["preferred_units"] = st.selectbox("preferred Units", ["Imperial", "Metriv"])
    
    #user input for math questions
    # question = st.text_imnput("Ask math Questions:")
    
    # User input for math questions
    st.subheader(" Ask a math Questions:")
    
    # Increase the height of the input field by setting the height parameter
    question = st.text_area("", height = 150, key = "math_question")
    
    if st.button("Submit"):
        # Send the userquestion to MATHGPT and get the answer
        answer = ask_math_question(question)
        
        # Display the answer
        st.write(f"**Answer:** {answer}")
        
        
if __name__ == "__main__":  
    main()    



