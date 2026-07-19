from dataclasses import dataclass


@dataclass
class Plan:
    use_memory: bool
    use_tools: bool
    generate_title: bool
    summarize: bool
    model: str


def create_plan(
    user_message: str,
    conversation_length: int,
) -> Plan:
    """
    Decide how First-Son should handle
    the user's request.

    This is intentionally simple.
    Later we'll replace it with a much
    smarter planner.
    """

    return Plan(
        use_memory=True,
        use_tools=False,
        generate_title=conversation_length >= 2,
        summarize=conversation_length % 10 == 0,
        model="default",
    )