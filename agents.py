import os
from crewai import Agent
from langchain_groq import ChatGroq
from crewai_tools import (
    SerperDevTool,
)

search_tool = SerperDevTool()
from tools.search_tools import SearchTools

class TextProcessorAgent():
    
    def text_processor(self): 
      return Agent(
      role='Text Processor',
      goal='Extract actionable insights',
      backstory=""" You're a Web Scraper at a large company.
                        You're responsible for analyzing data from websites and give the data from that website
                        You're currently working on a project to get the scrape data from the websites needed """,
      verbose=True,  
      llm=ChatGroq(
            api_key=os.getenv('GROQ_API_KEY'),
            model="llama3-70b-8192"
        ),
      allow_delegation=False, 
      cache=True
    )

    def text_scraper(self,text):
       return Agent(
          role='WebScraper',
          goal="Extract actionable insights",
          backstory= """You're a Web Scraper at a large company.
                        You're responsible for analyzing data from websites and give the data from that website
                        You're currently working on a project to get the scrape data from the websites needed""",
          verbose=True,
          tools=[
                SearchTools.web_scrapper(txt=text),
            ], 
          llm=ChatGroq(
            api_key=os.getenv('GROQ_API_KEY'),
            model="llama3-70b-8192"
        ), 
          allow_delegation=False, 
      )