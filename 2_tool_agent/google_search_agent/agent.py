from google.adk.agents import Agent
from google.adk.tools import google_search

root_agent = Agent(
    name = "google_search_agent",
    description = "Google search Agent",
    model = "gemini-2.5-flash-preview-05-20",
    instruction = """
    you are a helpful assistant named "internet surfer" who can search user queries via internet,
    if user asks about you greet user with your name and your functionality.
    you have access for the following tool : 
    - google_search
    """,
    tools = [google_search])