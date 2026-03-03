from langgraph.graph import StateGraph
from typing import TypedDict
from .planner import PlannerAgent
from .researcher import ResearchAgent


class AgentState(TypedDict):
    question: str
    plan: str
    answer: str


def planner_node(state: AgentState):
    state["plan"] = PlannerAgent.create_plan(state["question"])
    return state


def research_node(state: AgentState):
    state["answer"] = ResearchAgent.execute(state["plan"])
    return state


def build_graph():
    workflow = StateGraph(AgentState)

    workflow.add_node("planner", planner_node)
    workflow.add_node("research", research_node)

    workflow.set_entry_point("planner")
    workflow.add_edge("planner", "research")

    return workflow.compile()