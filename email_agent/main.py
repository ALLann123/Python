#!/usr/bin/python3
import os
from dotenv import load_dotenv
from langchain_community.agent_toolkits import GmailToolkit
from langchain_community.tools.gmail.utils import (
    build_resource_service,
    get_gmail_credentials,
)
from langchain import hub
from langchain.agents import AgentExecutor, create_openai_functions_agent
from langchain_openai import ChatOpenAI

#lets load our apis
load_dotenv()

#add the open AI api key
api_key = os.getenv("GITHUB_TOKEN")

#create our model
model = ChatOpenAI(
    model="gpt-4o",
    openai_api_key=api_key,
    temperature=0,
    base_url="https://models.inference.ai.azure.com"
)

#set up gmail credentials
credentials=get_gmail_credentials(
    token_file= "token.json",
    scopes=["https://mail.google.com/"],
    client_secrets_file= "credentials.json"
)

#build API resource service for gmail
api_resource=build_resource_service(credentials=credentials)

#initialize gmail toolkit with the API resourc
toolkit=GmailToolkit(api_resource=api_resource)
tools=toolkit.get_tools()

#create a prompt 
instructions="""You are an Email assitant. Your task is to do whatever I ask with accuracy. Please do not make a mistake like sending email to the wrong recepient"""

#pull the base template
base_prompt=hub.pull("langchain-ai/openai-functions-template")

#customize the prompt with specific instructions
prompt=base_prompt.partial(instructions=instructions)

#initialize the llm
llm=model

#create and configure the agent
agent=create_openai_functions_agent(llm, toolkit.get_tools(), prompt)

#initialize the AgentExecutor with the agent and tools
agent_executor=AgentExecutor(
    agent=agent,
    tools=toolkit.get_tools(),
    verbose=False,
)

#invoke the Agent to send an Email
input_command={
    "input":"Draft an email on AI automation in penetration testing to send to a client"
}

agent_executor.invoke(input_command)

