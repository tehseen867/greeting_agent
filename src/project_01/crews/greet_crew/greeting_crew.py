from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from dotenv import load_dotenv
load_dotenv()

# If you want to run a snippet of code before or after the crew starts,
# you can use the @before_kickoff and @after_kickoff decorators
# https://docs.crewai.com/concepts/crews#example-crew-class-with-decorators


@CrewBase
class GreetingCrew:
    """Greeting Crew"""


    agents_config = "config/agents.yaml"
    tasks_config = "config/tasks.yaml"

    @agent
    def message_checker_agent(self) -> Agent:
        return Agent(
            config=self.agents_config["message_checker_agent"],
            verbose=True,
        )

    @agent
    def greeting_agent(self) -> Agent:
        return Agent(
        config=self.agents_config["greeting_agent"],
        verbose=True,

        )

    @task
    def check_message(self) -> Task:
        return Task(
            config=self.tasks_config["check_message"],
            verbose=True,
        )

    @task
    def greet_user(self) -> Task:
        return Task(
        config=self.tasks_config["greet_user"],
        verbose=True,
        )

    @crew
    def crew(self) -> Crew:
        """Creates the Research Crew"""
        # To learn how to add knowledge sources to your crew, check out the documentation:
        # https://docs.crewai.com/concepts/knowledge#what-is-knowledge

        return Crew(
            agents=self.agents,  # Automatically created by the @agent decorator
            tasks=self.tasks,  # Automatically created by the @task decorator
            process=Process.sequential,
            verbose=True,
        )
