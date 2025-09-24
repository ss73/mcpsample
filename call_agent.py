from azure.ai.projects import AIProjectClient
from azure.identity import DefaultAzureCredential
from azure.ai.agents.models import ListSortOrder

class AgentCaller:
    def __init__(self, endpoint: str, agent_id: str):
        self.project = AIProjectClient(
            credential=DefaultAzureCredential(),
            endpoint=endpoint
        )
        self.agent = self.project.agents.get_agent(agent_id)

    def ask(self, prompt: str) -> str:
        thread = self.project.agents.threads.create()
        self.project.agents.messages.create(
            thread_id=thread.id,
            role="user",
            content=prompt
        )
        run = self.project.agents.runs.create_and_process(
            thread_id=thread.id,
            agent_id=self.agent.id
        )
        if run.status == "failed":
            return f"Run failed: {run.last_error}"
        messages = self.project.agents.messages.list(thread_id=thread.id, order=ListSortOrder.ASCENDING)
        for message in messages:
            if message.role == "assistant" and message.text_messages:
                return message.text_messages[-1].text.value
        return "No response from agent."

# Example usage:
# agent_caller = AgentCaller(
#     endpoint="https://coarch-resource.services.ai.azure.com/api/projects/coarch",
#     agent_id="asst_WCW9rE22OnLr4FgCOhqOekRy"
# )
# response = agent_caller.ask("What are the best practices for calling an SDP service?")
# print(response)