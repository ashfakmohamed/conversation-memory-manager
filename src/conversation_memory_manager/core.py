from dataclasses import dataclass
from threading import RLock


@dataclass(frozen=True)
class Message:
    role: str
    content: str


class ConversationMemory:
    def __init__(self, max_messages: int = 20, max_chars: int = 8_000) -> None:
        if max_messages < 1 or max_chars < 1:
            raise ValueError("memory limits must be positive")
        self.max_messages = max_messages
        self.max_chars = max_chars
        self._messages: list[Message] = []
        self._lock = RLock()

    def add(self, role: str, content: str) -> None:
        if role not in {"system", "user", "assistant", "tool"}:
            raise ValueError("unsupported message role")
        message = Message(role=role, content=content.strip())
        with self._lock:
            self._messages.append(message)
            while len(self._messages) > 1 and (
                len(self._messages) > self.max_messages
                or sum(len(item.content) for item in self._messages) > self.max_chars
            ):
                self._messages.pop(0)

    def snapshot(self) -> tuple[Message, ...]:
        with self._lock:
            return tuple(self._messages)
