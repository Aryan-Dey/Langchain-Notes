from langchain_groq import ChatGroq
from langchain_core.messages import SystemMessage, HumanMessage, AIMessage
from dotenv import load_dotenv

load_dotenv()

model = ChatGroq(model="deepseek-r1-distill-llama-70b")

chat_history = [
    SystemMessage(content="You are a Helpful Assistant that can answer questions and help with knowledge base tasks.")
]

while True:
    user_input = input("You:")
    chat_history.append(HumanMessage(content=user_input))

    if user_input.lower() == "exit":
        break

    result = model.invoke(chat_history)
    chat_history.append(AIMessage(content=result.content))
    print(f"Assistant: {result.content}")


print("Chat History:", chat_history)