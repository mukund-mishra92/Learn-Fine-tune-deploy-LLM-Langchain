from src.langgraph_agenticAI.state.state import State




class basicChatbotNode:
    ## Basic chatbot node implementation
    def __init__(self, model):
        self.llm = model

    def process(self, state:State)->dict:

        return {"message":self.llm.invoke(state["message"])}


