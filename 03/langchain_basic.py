from langchain_openai import ChatOpenAI
llm = ChatOpenAI()

result = llm.invoke("Was ist die Hauptstadt von Deutschland?")
print(result.content)