from app.agents.planner_agent import create_plan
from app.agents.router_agent import RouterAgent
from app.agents.memory_agent import MemoryAgent
from app.agents.title_agent import TitleAgent


class ConversationAgent:
    """
    Main Brain of First-Son.

    Every chat request flows through here.
    """

    def __init__(self):
        self.router = RouterAgent()
        self.memory = MemoryAgent()
        self.title = TitleAgent()

    def chat(self, conversation_id: str, messages: list):
        """
        Pipeline

        User
            ↓
        Memory
            ↓
        Planner
            ↓
        Router / LLM
            ↓
        Save Memory
            ↓
        Generate Title
            ↓
        Response
        """

        # 1. Build conversation context
        context = self.memory.prepare(messages)

        # 2. Decide what model/tools to use
        plan = create_plan(
            messages[-1]["content"],
            len(messages),
        )

        # 3. Generate response
        response = self.router.chat(
            context,
            plan.model,
        )

        # Later
        # self.memory.save(...)
        # self.title.generate(...)

        return response

    def stream(self, conversation_id: str, messages: list):
        """
        Streaming version of the pipeline.
        """

        context = self.memory.prepare(messages)

        plan = create_plan(
            messages[-1]["content"],
            len(messages),
        )

        return self.router.stream(
            context,
            plan.model,
        )