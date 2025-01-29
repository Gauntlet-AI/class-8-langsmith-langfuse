import openai
from langsmith.wrappers import wrap_openai
from langsmith import traceable
import os
from dotenv import load_dotenv

load_dotenv()

os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")
os.environ["LANGCHAIN_API_KEY"] = os.getenv("LANGCHAIN_API_KEY")
os.environ["LANGCHAIN_TRACING_V2"] = os.getenv("LANGCHAIN_TRACING_V2")
os.environ["LANGCHAIN_PROJECT"] = os.getenv("LANGCHAIN_PROJECT")

# Auto-trace LLM calls in-context
client = wrap_openai(openai.Client())

@traceable # Auto-trace this function
def pipeline(user_input: str):
	result = client.chat.completions.create(
		messages=[{"role": "user", "content":
			user_input}],
		model="gpt-4o-mini")
	return result.choices[0].message.content

print(pipeline("Hello, world!"))
