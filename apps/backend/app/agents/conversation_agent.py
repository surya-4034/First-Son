from app.agents.planner_agent import create_plan
from app.agents.router_agent import RouterAgent
from app.agents.memory_agent import MemoryAgent


class ConversationAgent:

    def __init__(self):
        self.router = RouterAgent()
        self.memory = MemoryAgent()

    def chat(self, messages):

        plan = create_plan(
            messages[-1]["content"],
            len(messages),
        )

        context = self.memory.prepare(
            messages
        )

        return self.router.chat(
            context,
            plan.model,
        )

    def stream(self, messages):

        plan = create_plan(
            messages[-1]["content"],
            len(messages),
        )

        context = self.memory.prepare(
            messages
        )

        return self.router.stream(
            context,
            plan.model,
        )