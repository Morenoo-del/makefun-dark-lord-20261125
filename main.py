"""The Tired Dark Lord: a 100-word villain monologue.

Writes the monologue to /output/entry.txt when run.
"""

MONOLOGUE = (
    "Heroes. Sit. Don't kneel, the floor is damp, I've just had it mopped, "
    "and kneeling only makes the speeches longer. You came for the Ember "
    "Crown. Everyone does. I forged it myself, in the winter the river "
    "froze black, wore it three hundred years, and all it ever did was "
    "pinch. So take it. Take the crown, take the tower, take the ravens. "
    "The ravens especially. They gossip. I'll keep the kettle. You want a "
    "final battle? You'll have to settle for a final cup of tea. The "
    "kettle's already on. The crown's heavier than it looks. You'll see."
)


import os


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(MONOLOGUE + "\n")


if __name__ == "__main__":
    main()
