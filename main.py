from langchain_groq import ChatGroq
from crewai import Agent, Task , Crew
from langchain_community.llms import Ollama
from langchain.tools import tool 
from tasks import Tasks
from agents import TextProcessorAgent



agent = TextProcessorAgent()
task = Tasks()

print("## Welcome to the Scraper")
print('-------------------------------')

textInputed = input("Enter the text that you want to scrap \n")

# Create Agents
Text_scrapper_agent = agent.text_scraper(text=textInputed)

# Create Tasks
Text_scraping_task = Tasks.Receive_Text_Input(agent=Text_scrapper_agent) 

# Create Crew responsible for Copy
Scraping_Crew = Crew(
    agents=[
        Text_scrapper_agent
    ],
    tasks=[
        Text_scraping_task
    ],
    verbose=True
)

txt_copy = Scraping_Crew.kickoff()

# Print results
print("\n\n########################")
print("## Here is the result")
print("########################\n")
print("Your post copy:")
print(txt_copy)