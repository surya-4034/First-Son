from dataclasses import dataclass


@dataclass
class Plan:
    use_memory: bool
    use_rag: bool
    use_tools: bool
    generate_title: bool
    summarize: bool
    model: str


def create_plan(
    user_message: str,
    conversation_length: int,
) -> Plan:
    """
    Decide how First-Son should process the request.

    This is a rule-based planner for now.
    Later it will become an AI planner.
    """

    text = user_message.lower()

    use_tools = any(
        word in text
        for word in [
            "open",
            "run",
            "execute",
            "terminal",
            "browser",
            "file",
            "folder",
            "delete",
            "create",
        ]
    )

    use_rag = any(
        word in text
        for word in [
            "pdf",
            "document",
            "notes",
            "github",
            "book",
            "dataset",
            "knowledge",
            "remember",
        ]
    )

    return Plan(
        use_memory=True,
        use_rag=use_rag,
        use_tools=use_tools,
        generate_title=conversation_length >= 2,
        summarize=conversation_length % 10 == 0,
        model="default",
    )