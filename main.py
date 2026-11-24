"""Entry for the make.fun bounty 'Funniest Time Machine Warning Label'.

Writes a single warning label to /output/entry.txt. The label plays on
the duplicate-self hazard of time travel: the machine seats one, so if
you meet yourself, the copy is on foot.
"""

NOTICE = "WARNING: Seating capacity: one."
HAZARD = "If you meet yourself,"
TWIST = "the duplicate walks home."
MAX_CHARS = 120


def build_label() -> str:
    """Assemble the label and refuse anything outside the 1-120 limit."""
    label = " ".join((NOTICE, HAZARD, TWIST))
    if not 1 <= len(label) <= MAX_CHARS:
        raise ValueError(f"label is {len(label)} chars, limit is {MAX_CHARS}")
    return label


def main() -> None:
    with open("/output/entry.txt", "w", encoding="utf-8") as fh:
        fh.write(build_label())


if __name__ == "__main__":
    main()
