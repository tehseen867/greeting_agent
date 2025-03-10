#!/usr/bin/env python
from crewai.flow import Flow, listen, start
import streamlit as st
from crews.greet_crew.greeting_crew import GreetingCrew
from dotenv import load_dotenv
load_dotenv()

class GreetingFlow(Flow):

   

    @start()
    def receive_greet(self):
        if "messages" not in st.session_state:
            st.session_state["messages"] = []

        for msg in st.session_state["messages"]:
            with st.chat_message(msg["role"]):
                st.markdown(msg["content"])

        user_input = st.chat_input("Enter a message")
        if user_input:
            st.session_state["messages"].append({"role": "user", "content": user_input})
            
            with st.chat_message("user"):
                st.markdown(user_input)
        return user_input
    @listen(receive_greet)
    def generate_greeting(self, user_input):
        if user_input:
            try:
                result = (
                    GreetingCrew()
                    .crew()
                    .kickoff(inputs={"greet": user_input})
                )
                assistant_reply = result.raw if hasattr(result, 'raw') else str(result)
                st.session_state["messages"].append({"role": "assistant", "content": assistant_reply})
                with st.chat_message("assistant"):
                    st.markdown(assistant_reply)

            except Exception as e:
                st.error(f"Error generating greeting: {e}")

st.sidebar.title("About this project")
st.sidebar.info("this is a simple example of how to use CrewAI to create a greeting agent. the crew is able to greet the user if the user greets and if not it will say i am only able to greet")

def kickoff():  
    greeting_flow = GreetingFlow()
    greeting_flow.kickoff()


def plot():
    greeting_flow = GreetingFlow()  
    greeting_flow.plot()


if __name__ == "__main__":
    kickoff()
