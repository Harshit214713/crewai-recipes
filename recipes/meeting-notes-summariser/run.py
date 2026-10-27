"""
Meeting Notes Summariser Recipe — run.py

CLI entry point for running the meeting notes summariser recipe.
"""

import argparse
import os
import sys

from dotenv import load_dotenv

load_dotenv()

from crew import build_crew  # noqa: E402


def check_env() -> None:
    """Preflight environment check for required API key."""
    api_key = os.getenv("LLM_API_KEY") or os.getenv("NVIDIA_API_KEY")
    if not api_key:
        print("❌ Error: Missing API key.", file=sys.stderr)
        print(
            "   Please set LLM_API_KEY or NVIDIA_API_KEY in your .env file or environment.",
            file=sys.stderr,
        )
        print("   Get a free key at https://build.nvidia.com", file=sys.stderr)
        sys.exit(1)


def main() -> None:
    """Parse CLI arguments and run the meeting notes summariser crew."""
    parser = argparse.ArgumentParser(
        description="Summarise meeting transcripts into decisions, action items, and follow-up emails."
    )
    parser.add_argument(
        "--meeting-title",
        type=str,
        default="Q3 Engineering Roadmap & Release Planning",
        help="Subject or title of the meeting",
    )
    parser.add_argument(
        "--participants",
        type=str,
        default="Alice (Tech Lead), Bob (PM), Charlie (DevOps), Dana (Backend)",
        help="Meeting attendees and stakeholders",
    )
    parser.add_argument(
        "--transcript",
        type=str,
        default=(
            "Bob: We need to freeze feature branch releases by Friday for Q3 launch. "
            "Alice: Agreed, but we have two critical PRs for DB migration pending review. "
            "Charlie: I can run staging load tests once migrations land on Wednesday. "
            "Dana: I will finish DB migration tests by Tuesday 3 PM. "
            "Alice: Perfect. Bob: Let us also cut the release notes on Thursday. "
            "Charlie: I will monitor infra alerts during deployment on Friday."
        ),
        help="Raw transcript or notes from the meeting",
    )
    parser.add_argument(
        "--verbose",
        action="store_true",
        default=False,
        help="Enable verbose output from agents",
    )

    args = parser.parse_args()
    check_env()

    print("\n🚀  Meeting Notes Summariser — Processing Transcript\n")
    print(f"   Meeting Title: {args.meeting_title}")
    print(f"   Participants:  {args.participants}\n")
    print("─" * 60)

    crew = build_crew(
        meeting_title=args.meeting_title,
        participants=args.participants,
        transcript=args.transcript,
        verbose=args.verbose,
    )
    result = crew.kickoff()

    print("\n" + "═" * 60)
    print("📋 SUMMARY & ACTION ITEMS")
    print("═" * 60)
    print(result)
    print("═" * 60 + "\n")


if __name__ == "__main__":
    main()
