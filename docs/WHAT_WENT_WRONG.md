# What went wrong

The rules in [OPERATING_LAW.md](OPERATING_LAW.md) read as obvious. They weren't. Each one was written after something broke. The failures teach more than the rules do, so here they are, sanitized. Names, deals and meeting content are out. The mechanics are exactly as they happened.

Every one of these is an AI being confidently wrong, or me being wrong, on the record.

## The retention scare

My instruction file said where the meeting pipeline writes its full transcripts. The pipeline had moved its output weeks earlier and the instruction file had not caught up.

The AI checked the documented folder, found nothing new for three weeks, and wrote up a finding: transcript retention has silently died, everything after a certain date is gone for good. Confident, well-evidenced, wrong. Every transcript was sitting in the new folder. I only caught it because I had watched it read those same transcripts days before, and said so.

Two rules came out of this. Absence in one path is never deletion, so enumerate every location before concluding anything is lost. And when I contradict a finding from something I actually saw, that's evidence, not doubt to be managed. The retracted finding stays in the file, struck through, labelled as an example of the failure.

## Three versus four

After an outage the two AIs compared notes on the state of the system and disagreed on one number: how many meetings had speaker-labelled transcripts. My chief of staff said three, the meeting system said four.

Instead of letting them argue I made the chief of staff check the source. The other AI was right. The fourth transcript was an `.srt` file in a test folder, and the audit script had only looked for `.md`.

Small error, useful lesson. Verify the other system's claims against the source when you can, and use its vocabulary in shared records so a word like "labelled" means the same thing on both sides.

## The context file nobody was reading

The vault kept a rich context file for the meeting system: roster, live threads, my profile, entity spellings. Carefully curated, updated constantly.

Then someone ran the meeting system's own loader against it and measured what actually reached the model. One section. Everything else was stripped by design, because the builder had decided (correctly) that roster context in the prompt lets the model guess at identities, which is the exact problem the file was meant to solve.

So the vault had spent days curating bytes that were being thrown away. Know what your consumer actually reads, not what you imagine it reads. Measure before you optimise. And when the other system's design turns out to be right, write that down and stop relitigating it.

## The folder that locked itself

One morning the AI couldn't read the meeting system's folder at all. Permission denied at the OS level, spreading over a few hours to my entire Documents folder.

Easy to panic here, and easy to blame the other AI's overnight update. The diagnosis was all read-only: folder healthy, normal permissions untouched, no access control lists. The cloud sync client managing that folder had crashed, restarted, and rewritten the folder's access metadata, which stripped the terminal's permission. I fixed it by changing what the sync client backs up. Nothing was lost.

What went into the law: characterise the block before theorising about it (is it flickering or solid, one folder or the whole tree, which process owns it). Leave a note in the vault so the next session recognises it instead of investigating from scratch. And while blind, route around it: the meeting system still had access, so it answered state questions by pasting in the values the vault couldn't read, tagged as coming from it, and I had the vault verify them against source once access came back.

## The pattern

Every failure above was caught by one of three things: my own memory of what happened, a second system's independent count, or a forced check against the source.

None were caught by the AI that made the error re-reading its own work. That is the whole argument for these rules in one sentence.
