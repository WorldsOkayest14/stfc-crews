# Roadmap

Ideas queued for later, in no particular order.

## Google Forms links
Add links to two Google Forms once they exist:
- "What problems do you have?" (feeds new entries for Fix a problem)
- "Do you have a crewing suggestion?"

Put a button for each on the landing page and in both tools (near Fix a problem and Build a crew).

## "Why did I lose?!" page: built
Live as `lose.html`. Possible next steps:
- Spot the battle triangle (wrong ship type for the opponent) once ship types are matched from the log's ship names.
- Read the log's Hull/Shield "Remaining" across rounds to say which round the fight was lost in.
- Test against more PvP losses; the first version was tuned on 4 Breen Warship fights and 1 PvP win.

## Later, if needed
- Full merge of the two tools into one page (see the Red Alert mockup). Only worth it if maintaining two pages becomes a problem.
- Ranking ships against each other (crowd-sourced).
- A recommended Ra'ul Reaver raiding crew, once the alliance settles on one.
- Rarities for Toryn, Rose Harper and Trelane (stfc.phd doesn't list them).

## Source files
- `src/pvp/`: template and data for `incursion-pvp.html`. Rebuild with `python3 src/pvp/build.py`.
- `crew-guide.html` is edited directly.
