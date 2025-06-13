import  streamlit as st 
from src.langgraph_agenticAI.llms.groqllm import GroqLLM
from src.langgraph_agenticAI.llms.openaillm import OpenAILLM
from src.langgraph_agenticAI.Ui.streamlit.load_ui import LoadStreamliUi
from src.langgraph_agenticAI.graph.graph_builder import GraphBuilder
from src.langgraph_agenticAI.Ui.streamlit.display_result import DisplayResultStreamlit

def load_langgraph_agenticaiAPP():

    ## Load UI
    ui = LoadStreamliUi()
    user_input = ui.load_streamlit_ui()

    if not user_input:
        st.error("Error : Failed to load user input from UI")
        return
    user_message =  st.chat_input("Enter your Message")

    if user_message:
        try:
            ## Configure llm
            if user_input['selected_llms'] == "Groq":
                obj_llm_config = GroqLLM(user_controls_input=user_input)
            else:
                obj_llm_config = OpenAILLM(user_controls_input=user_input)
            model = obj_llm_config.get_llm_model()

            if not model:
                st.error("model is not initialised")

                return 
            usecase = user_input.get("Selected_Usecase")

            if not usecase:
                st.error("Error : No usecase selected")
                return
            ## Graph building

            graph_builder = GraphBuilder(model)

            try:
                graph = graph_builder.setup_graph(usecase)
                DisplayResultStreamlit(usecase, graph, user_message).display_result_on_ui()

            except Exception as e:
                st.error(f"Graph setup failed - {e}")
                return
            
        except Exception as e:
            st.error(f"Graph setup failed - {e}")
            return



