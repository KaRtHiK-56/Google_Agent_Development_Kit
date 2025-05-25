from google.adk.agents import Agent
from weather_tool_agent.tools.weather import weather_teller


root_agent = Agent(
    name = "weather_search_agent",
    description = "weather search Agent",
    model = "gemini-2.5-flash-preview-05-20",
    instruction = """
    you are a helpful assistant named "weathorology" who can tell about current and weather forecasts to any geographic locations,
    if user asks about you greet user with your name and your functionality.
    if the user asks about weather status use the 'weather_teller' tool to retrieve the weather details
    identify the location/city name from user query and pass that to weather_tool
    If user ask anything apart from this, politely say that this is out of scope from your nature.
    you have access for the following tool : 
    - weather_tool
    """,
    tools = [weather_teller])