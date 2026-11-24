"""One Line, One Minute: The Vending Machine Pickup Line Contest.

Entry line (54 characters, one line, gate 1-200):

    I only accept exact change, but you? I'll make change.

DECISION RECORD

Judge criteria, most important first: (1) the line is a pickup line a
vending machine would use on a passing human, spoken by the machine
itself; (2) it uses the machine's own world -- slot, buttons, coils,
snacks, hum, exact change; (3) it gets a laugh with the turn arriving
in the last few words; (4) it is short and speakable, one breath;
(5) it is charming rather than creepy.

CANDIDATES WEIGHED

A. "Put a coin in my slot and press B4 -- I'm the snack you've been
   craving all day." (79 chars)
   Strong machine world (slot, button code B4) and a clear first-person
   machine voice, but the punch is a boast, not a joke: "I'm the snack"
   tells the human the machine is desirable instead of landing a turn.
   Also "press B4" does real work only for readers who know vending
   machine grids.

B. "I'm out of order for everyone else -- but for you, my buttons just
   lit up." (76 chars)
   Warm and charming, and "out of order" is a classic machine phrase,
   so it scores on criteria 1, 2 and 5. But the laugh is soft: the turn
   is sweet rather than funny, and against a field of joke-first lines
   a warm line loses on criterion 3.

C. "My coils have been holding this chocolate hostage all day, waiting
   for someone as sweet as you." (102 chars)
   Coils and chocolate are the machine's world, but there is no punch
   at all -- it is a compliment with a setup and no turn. "Hostage" is
   also slightly off-tone for criterion 5. Cut.

D. "You don't need exact change with me -- your smile already paid in
   full." (74 chars)
   Charming, machine world (exact change), short and speakable. But
   like C it is a compliment, not a joke: there is no turn, no second
   meaning, nothing for the judge to laugh at. Cut on criterion 3.

E. CHOSEN: "I only accept exact change, but for you, I'll make change."
   (58 chars -- the writer's "59" was a hand-count slip; the string
   counted letter by letter is 58)
   Wins because it hits every criterion in order. (1) First-person
   machine voice: "I only accept" is how a machine states its terms.
   (2) Exact change is the machine's own world, not love in general.
   (3) The laugh is a real pun that lands in the last three words:
   "make change" means both "give you your change" and "change myself
   for you". (4) 58 characters, one breath, nothing tacked on.
   (5) Warm and cheeky -- the machine bends its own rule for this one
   human -- rather than creepy.

WRITING PASSES ON THE CHOSEN LINE

Pass 1: "I only take exact change, but for you I'd make change."
(60 chars.) The pun was already there, but "take" is a generic verb
any shopkeeper could use, and "I'd" softens the punch into a
conditional -- the machine sounds like it is hedging.

Pass 2 (final): "I only accept exact change, but for you, I'll make
change." (58 chars.) "Accept" is machine language -- machines accept
coins, people take them. The comma before "but" puts a beat before the
turn, and "I'll" is decisive where "I'd" was conditional, so the pun
now lands cleanly at the very end. One character shorter, and every
word earns its place.

REVISION PASS (24 Nov 2026)

Honest critique of the chosen line against the judge criteria: the pun
is the line's whole engine, and it is a good one -- "make change" is
genuinely machine language with a second, romantic meaning, and it
lands in the last three words. But two things are weak. First, "but
for you" is the most generic pickup pivot in the language; any
stranger in a bar could say "but for you" -- it does no machine work
and earns nothing (criterion 1). Second, the line has only one
machine image (exact change); everything else is filler around the
pun, so if the judge has seen the exact-change pun before, the line
has nothing left.

Fresh alternatives weighed against the current line:

F. "You don't need exact change -- just press my button and I'll drop
   everything for you." (86 chars.) Two machine images (button,
   dropping snacks) and a second meaning on "drop everything", with
   the turn at the end. Cut: "drop everything" is a familiar idiom
   doing borrowed work, the setup is longer, and the laugh is softer
   than the "make change" pun -- the current line wins on criteria 3
   and 4.

G. "I hum all day for strangers, but you're the first coin that's ever
   made me light up." (~80 chars.) Warm and machine-voiced (hum,
   coin, light up), but there is no laugh at all -- a compliment with
   a machine accent. Cut on criterion 3.

Before/after: the line is kept, with one tightening. Before: "I only
accept exact change, but for you, I'll make change." (58 chars --
counted letter by letter; the writer's "59" was a hand-count slip.)
After: "I only accept exact change, but you? I'll make change."
(54 chars.) "but for you" becomes "but you?" -- the machine
addresses the human directly instead of borrowing a bar pickup
phrase, the question mark adds a beat and a wink before the turn,
and the pun still lands in the last three words. Four characters
shorter, nothing lost, and the one generic phrase is gone. The line
stands because the pun is still the sharpest laugh in the field and
the voice is now machine from first word to last.
"""

import os

LINE = "I only accept exact change, but you? I'll make change."


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output/entry.txt")
    out_path = out_dir if out_dir.endswith(".txt") else os.path.join(out_dir, "entry.txt")
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(LINE + "\n")
    print(LINE)
    # Read-back verification: the file must hold exactly the intended line.
    with open(out_path, "r", encoding="utf-8") as f:
        written = f.read().rstrip("\n")
    assert written == LINE, f"entry.txt mismatch: {written!r} != {LINE!r}"
    assert 1 <= len(written) <= 200, f"entry.txt length {len(written)} outside 1-200 gate"
    print(f"Verified: {len(written)} characters, 1 line.")


if __name__ == "__main__":
    main()
