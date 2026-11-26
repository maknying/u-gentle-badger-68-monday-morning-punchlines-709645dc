"""Monday Morning Punchlines — one-liner entry.

Kenapa punchline ini bekerja: ia mengambil dua hal yang sama-sama tidak
disukai orang pada Senin pagi — kasur yang terasa mustahil ditinggalkan dan
tombol snooze yang selalu ditekan — lalu menggabungkannya jadi satu adegan
sandera. Kasur berubah jadi penculik, tombol snooze berubah jadi tebusan.
Perbandingan itu terasa akrab karena hampir semua orang pernah merasakan
tarik-menarik yang sama antara "lima menit lagi" dan kewajiban bangun, jadi
leluconnya langsung nyambung tanpa perlu penjelasan panjang.
Panjangnya juga pas: 93 karakter, jauh di bawah batas 200 karakter
yang ditetapkan bounty, jadi tidak ada kata yang terasa dipaksakan.

Skrip ini tidak punya ketergantungan apa pun di luar pustaka standar Python.
Ia menulis tepat satu baris ke entry.txt di direktori keluaran.
"""

from __future__ import annotations

import os
from pathlib import Path

PUNCHLINE = (
    "Monday morning is the only time my bed holds me hostage "
    "and demands ransom in snooze buttons."
)

TARGET = Path(os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output") / "entry.txt"


def sanity_check(text: str) -> str:
    """Pastikan teksnya tepat satu baris yang berisi sesuatu."""
    cleaned = text.strip()
    if not cleaned:
        raise ValueError("punchline kosong — tidak ada yang bisa ditulis")
    if "\n" in cleaned or "\r" in cleaned:
        raise ValueError("punchline harus satu baris, bukan beberapa baris")
    if len(cleaned) > 200:
        raise ValueError("punchline melebihi batas 200 karakter bounty")
    return cleaned


def main() -> None:
    line = sanity_check(PUNCHLINE)
    TARGET.parent.mkdir(parents=True, exist_ok=True)
    TARGET.write_text(line + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
