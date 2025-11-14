# collaboration_patterns.py

class Agent:
    def __init__(self, name):
        self.name = name

    def process(self, query):
        return f"{self.name} processed query: {query}"


class HRAgent(Agent):
    def __init__(self):
        super().__init__("HR Agent")


class TechAgent(Agent):
    def __init__(self):
        super().__init__("Tech Agent")


# Role assignment
roles = {
    "HR": HRAgent(),
    "Tech": TechAgent(),
}


def delegate_task(query):
    # Naive delegation based on keywords
    hr_keywords = ["hr", "salary", "benefit", "leave"]
    if any(word in query.lower() for word in hr_keywords):
        agent = roles["HR"]
    else:
        agent = roles["Tech"]
    return agent.process(query)


def conversational_handoff(context, agent_name):
    agent = roles.get(agent_name)
    if not agent:
        return "Unknown agent"
    # Maintain context in a simple way
    return f"{agent.name} continues context: {context}"


if __name__ == "__main__":
    # Example usage
    print(delegate_task("What is the leave policy?"))
    print(conversational_handoff("Previous conversation context", "Tech"))
