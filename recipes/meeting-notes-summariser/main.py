"""
Meeting Notes Summariser Recipe — main.py

Self-contained runnable sample for meeting notes summarisation.
"""

from crew import build_crew


def main() -> None:
    sample_title = "Sprint 42 Retrospective & Planning"
    sample_participants = "Dev Lead, Scrum Master, Senior Backend Eng"
    sample_transcript = (
        "Lead: Retro went well, but CI was flaky on Ubuntu runners. "
        "Scrum Master: Should we migrate flaky integration tests to nightly? "
        "Lead: Yes, let's move long integration tests to nightly by Thursday. "
        "Senior Backend Eng: I will take that up. Also we must update Python version matrix to 3.12. "
        "Lead: Approved, please push the PR by Wednesday noon."
    )

    print("Running Meeting Notes Summariser Crew...")
    crew = build_crew(
        meeting_title=sample_title,
        participants=sample_participants,
        transcript=sample_transcript,
    )
    result = crew.kickoff()
    print("\nResult:\n", result)


if __name__ == "__main__":
    main()
