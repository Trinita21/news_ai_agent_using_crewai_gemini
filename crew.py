from crewai import Crew,Process
from tasks import research_task,write_task
from agents import news_researcher,news_writer

## Forming the tech focused crew with some enhanced configuration
crew=Crew(
    agents=[news_researcher,news_writer],
    tasks=[research_task,write_task],
    process=Process.sequential, # Sequestiontial communication between agents, researcher does its own research, sends the output to writer, writer writes the output blog, which is the final output.

)

## starting the task execution process with enhanced feedback

result=crew.kickoff(inputs={'topic':'Continual Learning'})
print(result)