# Hacker News "Who Is Hiring?" Parser

Using the Hacker News API, parses a "Who Is Hiring" feed and produces a clean list (one opportunity per line).
Useful when combined with grep.

## Usage:

python whoishiring.py \[id]

python whoishiring.py 12202865 | grep -i python | grep -i remote \> jerbs.txt

## Requirements:

1. Python 2.6+ ('json' library)