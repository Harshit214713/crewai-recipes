"""
Meeting Notes Summariser Recipe — crew.py

Assembles the CrewAI Crew for meeting transcript analysis and follow-up generation.
"""

from crewai import Crew, Process

from agents import build_agents
from tasks import build_tasks


def build_crew(
    meeting_title: str,
    participants: str,
    transcript: str,
    verbose: bool = False,
) -> Crew:
    """Build and return the meeting notes summariser Crew.

    Args:
        meeting_title: Title or subject of the meeting.
        participants: Attendees and stakeholders present.
        transcript: Raw transcript or notes recorded from the meeting.
        verbose: Enable verbose agent logging.

    Returns:
        A configured Crew instance ready to call .kickoff().
    """
    analyzer_agent, scribe_agent = build_agents()
    tasks = build_tasks(
        analyzer_agent=analyzer_agent,
        scribe_agent=scribe_agent,
        meeting_title=meeting_title,
        participants=participants,
        transcript=transcript,
    )

    return Crew(
        agents=[analyzer_agent, scribe_agent],
        tasks=tasks,
        process=Process.sequential,
        verbose=verbose,
    )
