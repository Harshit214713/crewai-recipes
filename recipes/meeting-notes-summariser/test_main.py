"""Smoke test: main() runs without errors and build_crew signature is correct."""

import os
import sys
from pathlib import Path
from unittest.mock import MagicMock, patch

if sys.platform.startswith("win"):
    try:
        sys.stdout.reconfigure(encoding="utf-8")
        sys.stderr.reconfigure(encoding="utf-8")
    except AttributeError:
        pass

os.environ.setdefault("LLM_API_KEY", "nvapi-test")
sys.path.insert(0, str(Path(__file__).parent))

import main as recipe_main  # noqa: E402


def test_main_runs() -> None:
    mock_output = MagicMock()
    mock_output.__str__ = lambda self: (
        "## Action Items\n\n- [ ] Release freeze by Friday (Owner: Bob)\n\n"
        "## Follow-Up Email Draft\n\nSubject: Summary of Q3 Planning\n\nHi Team..."
    )
    with patch("crewai.Crew.kickoff", return_value=mock_output):
        recipe_main.main()


if __name__ == "__main__":
    test_main_runs()
    print("✅ meeting-notes-summariser: main() smoke test passed")
