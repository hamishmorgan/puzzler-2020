# Puzzler 2020

## Rules

Find words by connecting letters

!(puzzle.png)

Rules:

 - Start at any letter in the graph
 - Follow the lines to add letters
 - Can loop back to reuse letters
 - Can’t repeat a letter “in place” (no doubled letters)
 - No minimum or maximum length
 - Validate using word list (`/usr/share/dict/words` or similar)
 - Print out (or equivalent) all words meeting the above requirements

Valid examples: `blob`, `shows`, `role`, `chow`

Invalid examples: `blobby` (doubled `b`), `shout` (no `u`), `ghost` (`s` not connected to `t`)

## Contents

 - `simple` is a fairly straightforward implementation
 - `tiny` is an attempted at smallest Python implementation