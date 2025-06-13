from configparser import ConfigParser

class Config:
    def __init__(self, config_file="/Users/balmukundmishra/Desktop/Learn-Fine-tune-deploy-LLM-Langchain/Project_1/src/langgraph_agenticAI/Ui/uiconfigfile.ini"):
        self.config = ConfigParser()
        self.config.read(config_file)

    def get_llmoptions(self):
        return self.config['DEFAULT'].get("LLM_OPTIONS").split(", ")
    
    def get_usecaseoptions(self):
        return self.config['DEFAULT'].get("USECASE_OPTIONS").split(", ")
    
    def groq_model_options(self):
        return self.config['DEFAULT'].get("GROQ_MODEL_OPTIONS").split(", ")
    
    def openai_model_options(self):
        return self.config['DEFAULT'].get("OPENAI_MODEL_OPTIONS").split(", ")
    
    def get_pagetitle(self):
        return self.config['DEFAULT'].get("PAGE_TITLE")


