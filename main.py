import os

TEXT = "I brought demons for the office, they're in the break room."


def main():
    # Gate: /output/entry.txt must be UTF-8, 1-199 chars, not whitespace-only.
    assert 1 <= len(TEXT) <= 199 and TEXT.strip()
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
