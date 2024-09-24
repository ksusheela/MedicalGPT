import streamlit as st
import openai
import os

# Make sure to securely manage your OpenAI API key in production
# Example: openai.api_key = os.getenv('OPENAI_API_KEY')
openai.api_key = "Use your Openai API Key"
def ask_medical_question(question):
    """Sends the user question to the OpenAI API and returns the AI's response."""
    
    # The system message ensures the AI acts as a medical expert, but it reminds users to seek professional help
    conversation = [
        {"role": "system", "content": "You are a medical expert providing general medical advice. "
                                      "Remember to give clear, concise answers and always recommend seeing a healthcare provider for serious or uncertain concerns."},
        {"role": "user", "content": question}
    ]
    
    # Sending the question to OpenAI's GPT-3.5-turbo model
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=conversation
    )
    
    # Extracting and returning the AI's response
    reply = response['choices'][0]['message']['content']
    return reply

def main():
    # Setting up the main title and disclaimers
    st.title("MedicalGPT - Your AI Medical Assistant")
    
    # Displaying a disclaimer
    st.markdown("""
        **Disclaimer:** The advice provided by MedicalGPT is for informational purposes only.
        It is not a substitute for professional medical advice, diagnosis, or treatment.
        Always consult with a qualified healthcare provider for serious or uncertain medical concerns.
    """)

    # Sidebar for user profile settings
    st.sidebar.header("User Profile Settings")
    
    # Defining default user profile settings
    #user_profile = {
     #   "language": st.sidebar.selectbox("Language", ["English", "Spanish", "French", "Hindi", "Chinese"]),
     #   "preferred_units": st.sidebar.selectbox("Preferred Units", ["Metric", "Imperial"])
    #}
    
    # Input area for the user to ask medical questions
    st.subheader("Ask Your Medical Question:")
    question = st.text_area("Enter your medical question here:", height=150)
    
    # Handling the 'Submit' button click event
    if st.button("Submit"):
        if question.strip() == "":
            st.error("Please enter a medical question.")
        else:
            # Sending the user question to the OpenAI API and retrieving the response
            answer = ask_medical_question(question)
            
            # Displaying the answer from the AI
            st.write(f"**Answer:** {answer}")
            
            # Additional disclaimer after the answer
            st.markdown("""
                **Note:** The information provided by MedicalGPT is not a substitute for professional medical advice.
                Always consult a healthcare provider for serious or concerning health issues.
            """)

# Run the app
if __name__ == "__main__":  
    main()