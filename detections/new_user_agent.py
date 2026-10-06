def detect_new_user_agent(event, known_user_agents):
    user_agent = event["user_agent"]

    if user_agent not in known_user_agents:
        return True, user_agent

    return False, user_agent
