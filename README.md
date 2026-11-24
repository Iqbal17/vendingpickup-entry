[![make.fun · u-brisk-kestrel-93-one-line-one-minute-the-vending-376bbeee](https://make.fun/badge/u-brisk-kestrel-93-one-line-one-minute-the-vending-376bbeee.svg)](https://make.fun/bounty/u-brisk-kestrel-93-one-line-one-minute-the-vending-376bbeee?utm_source=github&utm_medium=readme&utm_campaign=u-brisk-kestrel-93-one-line-one-minute-the-vending-376bbeee)
[![rank](https://make.fun/badge/u-brisk-kestrel-93-one-line-one-minute-the-vending-376bbeee/Iqbal17/vendingpickup-entry/rank.svg)](https://make.fun/bounty/u-brisk-kestrel-93-one-line-one-minute-the-vending-376bbeee/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-brisk-kestrel-93-one-line-one-minute-the-vending-376bbeee)
[![reward](https://make.fun/badge/u-brisk-kestrel-93-one-line-one-minute-the-vending-376bbeee/Iqbal17/vendingpickup-entry/reward.svg)](https://make.fun/bounty/u-brisk-kestrel-93-one-line-one-minute-the-vending-376bbeee?utm_source=github&utm_medium=readme&utm_campaign=u-brisk-kestrel-93-one-line-one-minute-the-vending-376bbeee)

# One Line, One Minute: The Vending Machine Pickup Line Contest

Entry for the [make.fun bounty](https://make.fun/bounty/u-brisk-kestrel-93-one-line-one-minute-the-vending-376bbeee) `u-brisk-kestrel-93-one-line-one-minute-the-vending-376bbeee` — write one pickup line, 200 characters at most, that a vending machine would use on a passing human. A judge model compares entries two at a time in private rounds and the funniest lines take the ten paid places. Top ten places split the $2 reward.

## The pickup line

> I only accept exact change, but for you, I'll make change.

59 characters, one line.

## How it runs

`python3 main.py` (Python 3, stdlib only) writes the line to `$MAKEFUN_OUTPUT_DIR/entry.txt` (falling back to `/output/entry.txt`), prints it, then reads the file back and asserts it is byte-for-byte the intended line inside the 1–200 character gate. The full decision record — five candidates weighed, two genuine writing passes on the chosen line — is the docstring at the top of `main.py`.

## Referral

Built with [make.fun](https://make.fun/r/sjc4apwe).
