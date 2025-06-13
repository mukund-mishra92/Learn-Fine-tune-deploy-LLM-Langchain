from langgraph.graph import StateGraph, START, END
from src.langgraph_agenticAI.state.state import State
from src.langgraph_agenticAI.nodes.basic_chatbot_node import basicChatbotNode





class GraphBuilder:
    def __init__(self, model):
        self.llm = model
        self.graph_builder = StateGraph(State)

    def basic_chatbot_build_graph(self):
        ## building a basic chatbot graph using langgraph

        self.basic_chatbot_node = basicChatbotNode(self.llm)

        self.graph_builder.add_node("chatbot", self.basic_chatbot_node.process)
        self.graph_builder.add_edge(START, 'chatbot')
        self.graph_builder.add_edge('chatbot', END)

    def setup_graph(self, usecase: str):
        ## setup the graph for selected usecase

        if usecase == "Basic Chatbot":
            self. basic_chatbot_build_graph()

            return self.graph_builder.compile()





