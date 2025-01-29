from langchain_openai import ChatOpenAI
from langsmith.wrappers import wrap_openai
from langsmith import traceable
import os
from dotenv import load_dotenv

load_dotenv()

os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")
os.environ["LANGCHAIN_API_KEY"] = os.getenv("LANGCHAIN_API_KEY")
os.environ["LANGCHAIN_TRACING_V2"] = os.getenv("LANGCHAIN_TRACING_V2")
os.environ["LANGCHAIN_PROJECT"] = os.getenv("LANGCHAIN_PROJECT")


@traceable  # Auto-trace this function
def run():
    llm = ChatOpenAI(model="gpt-4o-mini")
    for i in range(5):
        response = llm.invoke("Tell me a dad joke. The joke should be in a story format.")
        print(response.content)
        print("/n")

run()
