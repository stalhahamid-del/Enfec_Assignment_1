class PlannerAgent:

    @staticmethod
    def create_plan(question: str) -> str:
        if "capital" in question.lower():
            return f"Need to search for: {question}"
        return "No research required."