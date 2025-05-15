from dataclasses import dataclass, field
from typing import List

@dataclass
class User:
    name: str
    tags: List[str] = field(default_factory=list)

u = User("Geetha")
u.tags.append("python")
print(u)
