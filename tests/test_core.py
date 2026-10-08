import pytest

from conversation_memory_manager import ConversationMemory


def test_evicts_oldest_messages_to_fit_limits():
    memory = ConversationMemory(max_messages=2, max_chars=20)
    memory.add("user", "first")
    memory.add("assistant", "second")
    memory.add("user", "third")
    assert [item.content for item in memory.snapshot()] == ["second", "third"]


def test_rejects_unknown_roles():
    with pytest.raises(ValueError):
        ConversationMemory().add("unknown", "message")
