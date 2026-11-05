# Basic Python Examples

Small Python exercises from first-year university study. These are learning examples, not finished applications.

## What's here

| File | Exercise |
| --- | --- |
| `Interactive Calculator.py` | Add or subtract two whole numbers. |
| `PigLatin.py` | Move the first letter of a word to the end and add `ay`. |
| `Rock Paper Scissors.py` | Play repeated rounds against a random computer choice. |
| `Rock Paper Scissors (Extended).py` | Keep scores across three non-tied rounds. |
| `BinarySearch.py` | An unfinished word-search exercise. See the limits below. |

## Run an example

Install Python 3, download the files and open a terminal in their folder. Run one script at a time:

```sh
python3 "Interactive Calculator.py"
```

On Windows, use `py` instead of `python3` if that is how Python is installed. Keep the quotes around filenames with spaces. These scripts use Python's built-in libraries; no extra packages are needed. Press Ctrl+C to stop a repeating game.

## Learning-project limits

- The calculator accepts whole numbers and `+` or `-`, with spaces between the two numbers and the operator, such as `4 + 5`.
- The Pig Latin exercise expects a non-empty word and does not implement full language rules.
- The basic rock-paper-scissors game repeats until stopped and expects lowercase choices.
- `BinarySearch.py` is not a correct binary-search implementation. It moves through a sorted list one position at a time and can fail on empty input or a missing word. Do not use it as a reliable search routine.

This documentation describes the source as it stands. It does not claim a fresh test run or change the original exercises.
