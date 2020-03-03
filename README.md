# Python BASIC Tools
A simple utility for working with legacy BASIC code.

## How It (Will) Work
1. The user will select a source code file.
1. pyBT will load the file into a list.
1. The list will be iterated through item by item.
1. For each line, the string will be parsed using a regex to find the opening of a subroutine (e.g., `SUB somesub`)
1. Once an instance of the regex is found each item will be parsed for the regex and for `END SUB`.
1. If a new match to the regex occurs before `END SUB` is found it will replace the previous match.[1]
1. When an `END SUB` is found to match the previously matched regex (e.g., `SUB somesub`):
    - The entire subroutine (including the opening `SUB somesub` and closing `END SUB`) will be written out to a new file.
    - The file will be given the name of the subroutine, e.g. `{somesub}.bas`.
1. The source file will continue being parsed from the end of the previous detected `END SUB`.
1. This process will be repeated until the entire file has been successfully searched.

## What (Will) Be the Output
For each subroutine within the user's selected source code a file will be created with the name of `{subroutine}.bas` and the subroutine's contents included within this file.

In addition, there should be console output providing updates on progress through the file as well as logging any exceptions that occur.

## Built Upon the Shoulders Of...
- [Computer Hope's How To Extract Specific Portions of a Text File Using Python](https://www.computerhope.com/issues/ch001721.htm)

## Footnotes
[^1] This will handle instances where we are looking at a `DECLARE SUB` instead of an actual subroutine. We could have used the regex to filter out for `DECLARE` but there are other instances where we might encounter the opening of a subroutine without its closing (e.g., incorrect or corrupted code) so we are using this method instead which should detect and handle both. Should add some messaging here eventually that will help folks know when one of these exceptions occurs.