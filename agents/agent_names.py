import names

used_names = set()


def __original_agent_name():
    name = names.get_last_name().lower()
    return name if name not in used_names else __original_agent_name()


def new_agent_name():
    agent_name = __original_agent_name()
    used_names.add(agent_name)
    return agent_name
