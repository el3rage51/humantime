"""Parse compact durations such as 1h30m2s."""
from __future__ import annotations

import re

_UNIT = {"d": 86400, "h": 3600, "m": 60, "s": 1}
_RE = re.compile(r"(?:\d+[dhms])+\Z")
_PART = re.compile(r"(\d+)([dhms])")


def parse_duration(text: str) -> int:
    raw = (text or "").strip()
    if not raw or not _RE.fullmatch(raw):
        raise ValueError(f"无法解析时长: {text}")
    total = 0
    seen: set[str] = set()
    for number, unit in _PART.findall(raw):
        if unit in seen:
            raise ValueError(f"单位重复: {unit}")
        seen.add(unit)
        total += int(number) * _UNIT[unit]
    return total


def format_duration(seconds: int) -> str:
    if seconds < 0:
        raise ValueError("时长不能为负")
    if seconds == 0:
        return "0s"
    parts = []
    left = seconds
    for unit, size in (("d", 86400), ("h", 3600), ("m", 60), ("s", 1)):
        count, left = divmod(left, size)
        if count:
            parts.append(f"{count}{unit}")
    return "".join(parts)


def shorter_than(left: str, right: str) -> bool:
    return parse_duration(left) < parse_duration(right)


def longest(*texts: str) -> str:
    if not texts:
        raise ValueError("至少一段时长")
    return format_duration(max(parse_duration(text) for text in texts))


def add_durations(*texts: str) -> str:
    if not texts:
        raise ValueError("至少一段时长")
    return format_duration(sum(parse_duration(text) for text in texts))
