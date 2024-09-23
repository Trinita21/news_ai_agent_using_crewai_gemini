from dotenv import load_dotenv
from crewai_tools import SerperDevTool # Google search API (cheap, free for 2500 queries.
import os

load_dotenv() # To load the API keys from .env

os.environ['SERPER_API_KEY'] = os.getenv('SERPER_API_KEY')

# Initialize the tool for internet searching capabilities of the Agents created
tool = SerperDevTool()