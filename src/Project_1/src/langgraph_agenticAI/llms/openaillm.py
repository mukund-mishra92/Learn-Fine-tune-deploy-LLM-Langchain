import os
import streamlit as st
from langchain_openai import ChatOpenAI


class OpenAILLM:
    def __init__(self, user_controls_input):
        self.user_controls_input = user_controls_input

    def get_llm_model(self):
        try:
            openai_api_key = self.user_controls_input['OpenAI_API_Key']
            selected_groq_model = self.user_controls_input['selected_openai_model']
            if openai_api_key=='' and os.environ['OpenAI_API_Key']=='':
                st.error("Please enter the groq api key")
            
            llm = ChatOpenAI(api_key=openai_api_key, model=selected_groq_model)
        except Exception as e:
            raise ValueError(f"Error occured with Exception : {e} ")
        
        return llm





