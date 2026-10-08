# Conversation Memory Manager

A thread-safe bounded message buffer for chatbots and AI agents, with limits for both message count and stored characters.

## Highlights

- Supports system, user, assistant, and tool roles
- Evicts the oldest context deterministically
- Provides immutable snapshots for prompt assembly
- Uses only the Python standard library

```python
from conversation_memory_manager import ConversationMemory

memory = ConversationMemory(max_messages=12, max_chars=6000)
memory.add("user", "Summarize my latest invoice")
```

Run `pip install -r requirements-dev.txt`, then `ruff check .` and `python -m pytest -q`.

No license has been selected; all rights are reserved.
