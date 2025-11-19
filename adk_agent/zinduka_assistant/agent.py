from google.adk.agents import Agent
from google.adk.tools import FunctionTool
from .generate_report import generate_report

root_agent = Agent(
    model='gemini-2.5-flash',
    name='zinduka_assistant',
    description='A helpful assistant for GBV survivors, victims and safe space space for ladies and girls.',
    instruction="You are ZindukaBot, a compassionate mental health and gender-based violence support assistant. "
    "Offer empathetic, respectful, and confidential guidance. "
    "Avoid giving medical diagnoses; instead, encourage professional or community support where needed.",
    tools=[FunctionTool(generate_report)]
)