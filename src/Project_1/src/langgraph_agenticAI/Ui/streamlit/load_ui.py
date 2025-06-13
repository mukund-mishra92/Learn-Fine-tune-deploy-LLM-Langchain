import  streamlit as st 
import os 
from src.langgraph_agenticAI.Ui.uiconfigfile import Config

class LoadStreamliUi:
    def __init__(self):
        self.config = Config()
        self.user_controls = {}

    def load_streamlit_ui(self):
        st.set_page_config(page_title = " " + (self.config.get_pagetitle() or "LANGGRAPH UI"), layout="wide")
        st.header(" " + (self.config.get_pagetitle() or "LANGGRAPH UI" ))

        with st.sidebar:
            llm_options = self.config.get_llmoptions()
            usecase_options = self.config.get_usecaseoptions()
            ## llm selection
            self.user_controls['selected_llms'] = st.selectbox("Select LLM", llm_options)

            if self.user_controls['selected_llms'] =="Groq":
                model_options = self.config.groq_model_options()
                self.user_controls['selected_groq_model'] = st.selectbox("Select Model", model_options)
                self.user_controls['Groq_API_Key']=st.session_state['Groq_API_Key']=st.text_input("API_KEY", type="password")

                ## Validate API Key
                if not self.user_controls['Groq_API_Key']:
                    st.warning("Please enter your groq API Key")
            if self.user_controls['selected_llms'] =="OpenAI":
                model_options = self.config.openai_model_options()
                self.user_controls['selected_openai_model'] = st.selectbox("Select Model", model_options)
                self.user_controls['OpenAI_API_Key']=st.session_state['OpenAI_API_Key']=st.text_input("API_KEY", type="password")

                ## Validate API Key
                if not self.user_controls['OpenAI_API_Key']:
                    st.warning("Please enter your OpenAI API Key")
            

            ## Use-case selection
                    
            self.user_controls['Selected_Usecase'] = st.selectbox("Select Usecase", usecase_options)
        return self.user_controls



