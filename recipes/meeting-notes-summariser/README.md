# Meeting Notes Summariser

A specialized two-agent CrewAI recipe that transforms unstructured meeting transcripts or rough notes into structured executive summaries, categorized action items with owners and deadlines, and ready-to-send follow-up emails for attendees.

---

## 🎯 What it does

Post-meeting workflows often stall because turning recorded discussions into clear next steps requires tedious manual summarisation. This recipe solves that by running a multi-agent pipeline:

1. **Meeting Transcript Analyst**:
   - Parses conversational transcripts and filters out conversational filler.
   - Extracts core topics discussed, technical decisions confirmed, and pending questions or risks.

2. **Executive Scribe & Action Coordinator**:
   - Compiles decisions into an explicit Action Items matrix with owners and deadlines.
   - Generates a polished, professional follow-up email addressed to participants summarizing the meeting's outcomes.

---

## 🏗 Architecture

```
Meeting Transcript + Attendees
           │
           ▼
┌──────────────────────────────────────┐
│   Meeting Transcript Analyst Agent   │
│   (extracts decisions & blockers)    │
└──────────────────┬───────────────────┘
                   │
                   ▼
┌──────────────────────────────────────┐
│  Executive Scribe & Coordinator      │
│  (action items + follow-up email)    │
└──────────────────┬───────────────────┘
                   │
                   ▼
Structured Action Items & Email Draft
```

---

## ⚡ Quickstart

### 1. Set your API key

Copy `.env.example` to `.env` and configure your NVIDIA NIM API key:

```bash
cp .env.example .env
```

Edit `.env`:

```env
LLM_API_KEY=nvapi-your-key-here
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Run the CLI

```bash
python run.py \
  --meeting-title "Q3 Engineering Roadmap" \
  --participants "Alice (Tech Lead), Bob (PM), Charlie (DevOps)" \
  --transcript "Bob: We need to freeze releases by Friday. Alice: Agreed. Charlie: I'll test staging on Wednesday."
```

---

## 📋 Inputs

| Field | Type | Description |
|---|---|---|
| `meeting_title` | `str` | Title or subject matter of the meeting |
| `participants` | `str` | Attendees and key stakeholders present |
| `transcript` | `str` | Raw meeting notes or transcript text |

---

## 🧪 Testing

Run unit tests with mocked LLM calls:

```bash
pytest test_main.py test_llm_retries.py -v
```
