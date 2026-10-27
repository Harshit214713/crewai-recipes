"""
Meeting Notes Summariser Recipe — agents.py

Defines the agents for analyzing transcripts and synthesizing action items.
"""

from crewai import Agent

from llm import get_llm


def build_agents() -> tuple[Agent, Agent]:
    """Build and return the meeting analyzer and executive scribe agents.

    Returns:
        A tuple of (analyzer_agent, scribe_agent).
    """
    llm = get_llm()

    analyzer_agent = Agent(
        role="Meeting Transcript Analyst",
        goal=(
            "Extract structured key discussion points, explicit decisions, and open blockers "
            "from raw meeting transcripts without losing critical technical or business context."
        ),
        backstory=(
            "You are a meticulous operations analyst with extensive experience in parsing "
            "complex technical and executive discussions. You cut through conversational filler, "
            "identifying decisive agreements and technical dependencies."
        ),
        verbose=True,
        memory=False,
        llm=llm,
    )

    scribe_agent = Agent(
        role="Executive Scribe & Action Coordinator",
        goal=(
            "Synthesize analyzed meeting outcomes into high-accountability action items with explicit "
            "owners and deadlines, and draft an executive follow-up email ready to dispatch."
        ),
        backstory=(
            "You are an executive chief-of-staff known for crisp communication and clear accountability. "
            "You ensure every decision has next steps and participants have actionable follow-up emails."
        ),
        verbose=True,
        memory=False,
        llm=llm,
    )

    return analyzer_agent, scribe_agent
