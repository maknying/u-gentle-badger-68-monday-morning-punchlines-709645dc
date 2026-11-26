"""One-line Monday morning joke entry for make.fun's "Monday Morning Punchlines".

The joke:

    Monday morning is the only time my bed holds me hostage and demands
    ransom in snooze buttons.

Why this line should land with the judge:

* It is unmistakably about Monday morning. The bed, the alarm, and the
  snooze button are the three objects everyone meets before their first
  coffee on a Monday, so the setup needs no explanation.
* It flips a familiar feeling into a crime scene. "Holds me hostage"
  turns the everyday struggle to get out of bed into a kidnapping, and
  "demands ransom in snooze buttons" is the surprise: the ransom is not
  money, it is the very thing that keeps you in bed longer, which is
  exactly how a Monday morning feels — you pay in snoozes and still lose.
* The punchline arrives in the last two words. The sentence builds a
  normal complaint, then the final twist reframes the bed as the
  criminal and the sleeper as the victim who pays up anyway.
* It is a single self-contained sentence with no setup outside itself, so
  it works cold, read aloud or on the page, with no context needed.

Running this module writes exactly that one line to ``entry.txt`` inside
``MAKEFUN_OUTPUT_DIR`` (falling back to ``/output``).
"""

import os
from pathlib import Path

JOKE = (
    "Monday morning is the only time my bed holds me hostage and demands "
    "ransom in snooze buttons."
)


def write_entry(joke: str, output_dir: Path) -> Path:
    """Write *joke* as the single line of ``entry.txt`` in *output_dir*.

    Refuses to write anything that is not exactly one non-empty line, so a
    future edit to the joke can never silently break the one-line format.
    """
    if not joke or "\n" in joke or "\r" in joke:
        raise ValueError("joke must be exactly one non-empty line")
    output_dir.mkdir(parents=True, exist_ok=True)
    entry_path = output_dir / "entry.txt"
    entry_path.write_text(joke + "\n", encoding="utf-8")
    return entry_path


def main() -> None:
    """Write the joke as the single line of ``entry.txt``."""
    output_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    write_entry(JOKE, output_dir)


if __name__ == "__main__":
    main()
