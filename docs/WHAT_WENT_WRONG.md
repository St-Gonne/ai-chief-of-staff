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

## Four wrong claims in three days (July)

The worst of them: the AI said the previous day's briefing didn't exist. Both that day's and the next day's files were on disk and committed. It had read a folder listing earlier in the session and reported it as current.

None of the four was a tool failing. Each was the step from a result to what it means. A more careful-sounding AI doesn't fix that, so the rule became a procedure: call the first result an observation, run a second check that can fail in a different way, and show the file, command and count so I can re-run it myself.

## Two checks that were really one (September)

Asked how much of an old file archive was safely backed up, the AI reported about 1% and recommended acting on it. Its file listing only walked my own Drive, not the files shared with me, and its fingerprint match can't work on documents whose bytes change when exported. It then ran a filename check and called it independent confirmation. That check failed on the same exported documents.

I asked it to look up 30 random files by hand. All 30 were there. The real answer was that almost nothing was missing, but three quarters of it lived in an account I don't own. What went into the procedure: two checks that share a failure mode are one check.

## The stale list that hid most of the list (August)

The morning briefing showed at most five stale to-dos, oldest first. It looked disciplined. When a counting script finally ran at session start, there were 31 stale items and the briefing had been hiding 26, including the largest unpaid invoice I'm owed. Stale items now show newest first with the total always printed, and money, legal and health items can't drop out of sight.

## The briefing I stopped opening (October)

Saved briefings went from 17 in July to 11 in August, 6 in September and none in October. The briefing reported on every open item, opened with what wasn't done, and scored me against goals I had moved off. Shorter versions of the same thing didn't help. What I use now is one screen: the date, one move for the main project, one move for money, today's calendar, sleep and energy.

## Words I couldn't follow (August)

I rejected two polished drafts of a rule before I could say what was wrong. It wasn't the rhythm, it was words I don't use, like escalation and cadence. The AI also kept pointing at things ("the last one", "rung 5") instead of naming them. The rule was in its instructions, it read it, and a week later it broke it anyway. So the fix is a check, not another rule: every name in a reply is one I've used, or it's explained in the same sentence.

## The pattern

Every failure above was caught by one of three things: my own memory of what happened, a second system's independent count, or a forced check against the source.

None were caught by the AI that made the error re-reading its own work. That is the whole argument for these rules in one sentence.
