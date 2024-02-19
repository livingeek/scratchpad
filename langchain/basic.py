from langchain_community.llms import Ollama
from langchain_core.output_parsers import StrOutputParser
llm = Ollama(model="llama2")
output_parser = StrOutputParser()

print(llm.invoke("how can langsmith help with testing?"))