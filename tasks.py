from textwrap import dedent
from crewai.task import Task
from tools.search_tools import SearchTools
# Define tasks for the TextProcessorAgent
class Tasks():
    def Receive_Text_Input(agent , textInputed):
        return Task(
            description=
            dedent(f"""Find and summarize the Text with the input:{textInputed}"""),
            expected_output='A bullet list summary of the top 5 most important AI news',
            async_execution=True,
            agent=agent,
        )
    
def Clean_and_Normalize_Text(agent,search_tools):
        return Task(
            description=' Cleans and normalizes the text by removing irrelevant characters, formatting inconsistencies, and correcting typos',
            expected_output='A bullet list summary of the top 5 most important AI news',
            async_execution=True,
            agent=agent,
            context=[Tasks.Receive_Text_Input],
            tools=[search_tools]
        )