# Roadmap

Ideas queued for later, in no particular order.

## Google Forms links
Add links to two Google Forms once they exist:
- "What problems do you have?" (feeds new entries for Fix a problem)
- "Do you have a crewing suggestion?"

Put a button for each on the landing page and in both tools (near Fix a problem and Build a crew).

## "Why did I lose?!" page
Upload the combat log CSV the game exports after a fight. The page reads it and gives a short plain answer, for example:
- "Level discrepancy!"
- "Need more Apex Shred!"
- or a combination of the biggest gaps.

Where the gap is something crew, ship or tech can change, list the officers, ships and tech that help (reuse the Fix a problem matching).

Needed before building: a few real combat log CSV files (a win and a few losses, ideally PvP and a hostile) to learn the format.

## Later, if needed
- Full merge of the two tools into one page (see the Red Alert mockup). Only worth it if maintaining two pages becomes a problem.
- Ranking ships against each other (crowd-sourced).
- A recommended Ra'ul Reaver raiding crew, once the alliance settles on one.
- Rarities for Toryn, Rose Harper and Trelane (stfc.phd doesn't list them).

## Source files
- `src/pvp/`: template and data for `incursion-pvp.html`. Rebuild with `python3 src/pvp/build.py`.
- `crew-guide.html` is edited directly.
