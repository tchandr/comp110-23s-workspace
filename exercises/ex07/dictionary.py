"""EX07 - Dictionary Utilities."""


__author__ = "730564179"


def invert(inp: dict[str, str]) -> dict[str, str]:
    """Inverts keys and values."""
    for i in inp:
        keys.append(i)
        values.append(inp[i])
    for i in range(0, len(inp)):
        if values[i] in out:
            raise KeyError("Duplicate Keys")
        out[values[i]] = keys[i]
    return out


def favorite_color(inp: dict[str, str]) -> str:
    """Returns color that is present most."""
    color_dict: dict[str, int] = dict()
    max: int = 0
    for i in inp:
        color_dict[inp[i]] = 0
    for i in inp:
        color_dict[i] += 1
    for i in color_dict:
        if color_dict[i] > max:
            max = color_dict[i]
    for i in color_dict:
        if color_dict[i] == max:
            return i


def count(inp: list[str]) -> dict[str, int]:
    """Counts each string with counter value."""
    out: dict[str, int] = dict()
    for i in inp:
        out[i] = 0
    for i in inp:
        if i in out:
            out[i] += 1
    return out