"""
Meeting Notes Summariser Recipe — tasks.py

Defines tasks for extracting meeting highlights and producing action summaries.
"""

from crewai import Agent, Task


def build_tasks(
    analyzer_agent: Agent,
    scribe_agent: Agent,
    meeting_title: str,
    participants: str,
    transcript: str,
) -> list[Task]:
    """Build and return the tasks for meeting notes summarisation.

    Args:
        analyzer_agent: Agent that analyzes transcripts.
        scribe_agent: Agent that drafts action items and follow-up.
        meeting_title: Meeting subject.
        participants: Attendees list.
        transcript: Raw transcript text.

    Returns:
        Ordered list of Task instances.
    """
    analysis_task = Task(
        description=(
            f"Analyze the following meeting transcript for '{meeting_title}'.\n"
            f"Attendees: {participants}\n\n"
            f"Transcript:\n{transcript}\n\n"
            "Identify:\n"
            "1. Major topics discussed.\n"
            "2. Key decisions reached by consensus.\n"
            "3. Blockers, risks, or pending questions raised."
        ),
        expected_output=(
            "A structured breakdown containing:\n"
            "- Discussion Highlights (bullet points)\n"
            "- Decisions Reached (numbered list)\n"
            "- Unresolved Questions / Risks (bullet points)"
        ),
        agent=analyzer_agent,
    )

    synthesis_task = Task(
        description=(
            f"Using the analysis from the previous task for '{meeting_title}', synthesize the final deliverables:\n"
            f"1. Action Items Table/List: Each item must have [Action Item], [Owner], and [Deadline/Timeline].\n"
            f"2. Stakeholder Follow-Up Email: Draft a clean, professional email addressed to '{participants}' "
            "summarizing the outcome, next steps, and expressing thanks for their time."
        ),
        expected_output=(
            "A comprehensive markdown report with two sections:\n"
            "## Action Items\n"
            "List of actionable tasks with explicit owner and timeline.\n\n"
            "## Follow-Up Email Draft\n"
            "Subject line and email body ready to be sent to attendees."
        ),
        agent=scribe_agent,
    )

    return [analysis_task, synthesis_task]
