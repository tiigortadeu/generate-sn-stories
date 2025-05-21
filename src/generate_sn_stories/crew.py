from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from crewai_tools import WebsiteSearchTool
from crewai_tools import SerperDevTool
from crewai.memory import ShortTermMemory
from crewai.memory.storage.rag_storage import RAGStorage
from crewai.memory.storage.ltm_sqlite_storage import LTMSQLiteStorage
from crewai.agents.agent_builder.base_agent import BaseAgent
from typing import List
import os
# If you want to run a snippet of code before or after the crew starts,
# you can use the @before_kickoff and @after_kickoff decorators
# https://docs.crewai.com/concepts/crews#example-crew-class-with-decorators

@CrewBase
class GenerateSnStories():
    """GenerateSnStories crew"""

    agents: List[BaseAgent]
    tasks: List[Task]
    tool = WebsiteSearchTool(
    config=dict(
        llm=dict(
            provider="google", # or google, openai, anthropic, llama2, ...
            config=dict(
                model="gemini/gemini-2.0-flash",
                # temperature=0.5,
                # top_p=1,
                # stream=true,
            ),
        ),
        embedder=dict(
            provider="google", # or openai, ollama, ...
            config=dict(
                model="models/embedding-001",
                task_type="retrieval_document",
                # title="Embeddings",
            ),
        ),
            )
        )
    # Learn more about YAML configuration files here:
    # Agents: https://docs.crewai.com/concepts/agents#yaml-configuration-recommended
    # Tasks: https://docs.crewai.com/concepts/tasks#yaml-configuration-recommended
    
    # If you would like to add tools to your agents, you can learn more about it here:
    # https://docs.crewai.com/concepts/agents#agent-tools
    @agent
    def requirement_analyst(self) -> Agent:
        
        return Agent(
            config=self.agents_config['requirement_analyst'], # type: ignore[index]
            tools=[self.tool],
            verbose=True
        )

    
    
    @agent
    def sn_expert(self) -> Agent:
        return Agent(
            config=self.agents_config['sn_expert'], # type: ignore[index]
            tools=[self.tool],
            verbose=True
        )

    @agent
    def product_owner(self) -> Agent:

        
        return Agent(
            config=self.agents_config['product_owner'], # type: ignore[index]
            tools=[self.tool],
            verbose=True
        )
    # To learn more about structured task outputs,
    # task dependencies, and task callbacks, check out the documentation:
    # https://docs.crewai.com/concepts/tasks#overview-of-a-task
    @task
    def identify_requirements(self) -> Task:
        return Task(    
            config=self.tasks_config['identify_requirements']  # type: ignore[index]
        )

    @task
    def find_sn_solution(self) -> Task:
        return Task(
            config=self.tasks_config['find_sn_solution'], # type: ignore[index]
            output_file='report.md'
        )

    @task
    def develop_solution(self) -> Task:
        return Task(
            config=self.tasks_config['develop_solution'], # type: ignore[index]
        )

    @task
    def create_user_story(self) -> Task:
        return Task(
            config=self.tasks_config['create_user_story'], # type: ignore[index]
        )
    @crew
    def crew(self) -> Crew:
        """Creates the GenerateSnStories crew"""
        # To learn how to add knowledge sources to your crew, check out the documentation:
        # https://docs.crewai.com/concepts/knowledge#what-is-knowledge

        return Crew(
            agents=self.agents,  # Automatically created by the @agent decorator
            tasks=self.tasks,  # Automatically created by the @task decorator
            process=Process.sequential,
            memory=True,
            verbose=True,
            embedder={
                "provider": "google",
                "config": {
                    "api_key": os.getenv("GEMINI_API_KEY"),
                    "model": "gemini/gemini-2.0-flash"
                }   
            },
            short_term_memory = ShortTermMemory(
                storage = RAGStorage(
                embedder_config={
                    "provider": "google",
                    "config": {
                        "api_key": os.getenv("GEMINI_API_KEY"),
                        "model": 'gemini/gemini-2.0-flash'
                    }
                },
                type="short_term",
                path="memory"
                )
            ),
            
            
            #    process=Process.hierarchical, # In case you wanna use that instead https://docs.crewai.com/how-to/Hierarchical/
        )
