# learn — a guarded one-on-one learning coach for pi

> An AI tutor that is **not allowed to explain first**.
> It makes you produce, then tests you, then schedules the review.

[English](README.md) | [中文](README.zh-CN.md)

A [pi](https://github.com/badlogic/pi-mono) skill. Drop it in your skills directory
and it turns a chat session into a structured tutoring loop with persistent state.

---

## The problem: why "AI tutoring" usually fails

Ask an AI to teach you something and you get a well-organised, fluent explanation.
You finish it feeling like you understood. A week later you can't reproduce any of it.

Two mechanisms cause this, and only one of them is about the AI:

**1. The fluency illusion.**
Reading a clear explanation feels like learning. It isn't. Comprehension is not
retrieval. The only way to know whether something is in your memory is to try to
pull it out — and a lecture never asks you to.

**2. The AI crutch.**
This one is now measured. Bastani et al. (2025, *PNAS*) ran a field experiment with
~1,000 high-school maths students and two AI tutors:

| Group | While using the AI | **After the AI was taken away** |
|---|---|---|
| Raw ChatGPT-style assistant | scores **+48%** | **17% *worse* than students who never had access** |
| Tutor with learning guardrails | scores **+127%** | no negative effect |

Unfettered access let students use the model as a crutch: they performed better with
it and then performed worse on their own. The guardrails — Socratic prompting,
refusing to hand over the answer — removed the effect entirely.

**So the failure mode isn't "the AI explained badly". It's "the AI explained".**

---

## Where the design comes from

This skill is not a prompt trick. Every rule in it is tied to a specific finding.
The full evidence base, with citations, lives in
[`references/methods.md`](references/methods.md).

### The load-bearing findings

| Design decision in this skill | Source |
|---|---|
| Never explain before the learner has tried; always ask for a first attempt | Pan & Sana 2021, *JEP: Applied* — pretesting beat posttesting across 5 experiments, n=1,573 |
| Force the learner to explain in their own words | Dunlosky et al. 2013, *Psych. Science in the Public Interest* — self-explanation rated moderate utility |
| Follow with a test; end every session with one | Dunlosky et al. 2013 — practice testing is one of only two techniques rated **high utility** |
| Schedule spaced card reviews with expanding intervals | Dunlosky et al. 2013 — distributed practice, the other high-utility technique |
| Small steps; never more than one idea before stopping | Sweller et al. 2019, *Educational Psychology Review* — working memory is capacity-limited |
| Target ~85% success rate, and adjust when outside 70–95% | Wilson et al. 2019, *Nature Communications* — the optimal training accuracy is ~85.87%, derived for a broad class of learning algorithms |
| Don't advance until mastery is demonstrated | Bloom 1984 — one-to-one tutoring **plus mastery learning** produced the celebrated 2-sigma effect |
| Feedback must state goal / current state / next step; never praise the person | Hattie & Timperley 2007, *Review of Educational Research* |
| Mix topics when reviewing — but not for word lists or expository text | Brunmair & Richter 2019, *Psychological Bulletin* — interleaving helps inductive learning, and its benefits are conditional on material similarity |
| Adapt difficulty by task complexity, not by "harder is better" | 2024, *Quarterly Journal of Experimental Psychology* — reconciles desirable difficulties with cognitive load theory via element interactivity |
| Never ask "does that make sense?" | Rosenshine 2012, *American Educator* — the least effective check for understanding; effective teachers check **all** students |
| Ground every claim in the source; mark gaps explicitly | This repo's own `references/prep.md` — see [Prep mode](#prep-mode-when-you-have-source-material) |

### What this skill deliberately does **not** do

Several popular ideas did not survive contact with the evidence:

| Popular idea | Status |
|---|---|
| Learning styles (visual / auditory / kinaesthetic) | **Debunked.** No effect on learning outcomes. (2026, *Journal of Educational Psychology*; 2023, *Medical Science Educator*) |
| Growth mindset as a general lever | **Downgraded.** Sisk et al. 2018, *Psychological Science*, two meta-analyses (*k*=273, N=365,915): overall effects weak; benefits appear mainly for low-SES / at-risk students |
| Re-reading and highlighting | **Low utility.** Dunlosky et al. 2013 — the two most-used techniques are among the least effective |
| "Summarise it for me" as a study method | **Low utility.** Summarisation is rated low; summarising is also an *output*, so the learner should produce it, not the AI |

### Why an AI tutor can work at all

Kestin et al. (2025, *Scientific Reports*) ran an RCT of an AI tutor **built on the same
pedagogical principles as the in-class lessons**: students learned more than twice as
much in less time than an active-learning class, effect size 0.73–1.3 SD — approaching
Bloom's 2 sigma.

Wang et al. (2024, Tutor CoPilot, 900 tutors / 1,800 students) found that AI assisting
*human* tutors raised student mastery by 4 percentage points, and by **9 pp for the
weakest tutors**. The AI helped most where the human was weakest.

The pattern is consistent: **AI helps when it is constrained by pedagogy, and harms
when it is not.**

---

## How this differs from "just ask the AI to teach me"

| | Typical AI tutoring | This skill |
|---|---|---|
| Who talks first | The AI | **You** — pretesting is mandatory |
| When the answer appears | Immediately | **After you've attempted it** |
| When you get it right by luck | Counted as correct | **The reasoning is interrogated** |
| Session ends when | The explanation runs out | **A test is passed** |
| Remembering next week | Not addressed | Spaced cards with recorded intervals |
| Material you bring | Pasted into context and forgotten | Compiled into a **testable lesson pack** before teaching |
| What it knows about you | Nothing, or whatever is in the current chat | A persistent **learner profile** (vocabulary, knowledge boundaries, working analogies) |
| When it doesn't know | Confabulates | Says so, and records the gap |

---

## How the skill works

### The 8 hard rules

These are enforced, not suggested:

1. **Never give the answer first.** You must guess, say, or attempt — even if you'll be wrong.
2. **One small chunk at a time.** Never more than ~15 lines of explanation, then stop and ask.
3. **Never ask "does that make sense?"** Ask for a restatement or a problem instead.
4. Every new concept must complete the loop: pretest → small explanation → self-explanation → restatement → problems → mastery check.
5. **Every session ends with a test.**
6. **On a wrong answer, first ask "how did you get there?"** — locate the broken step; don't hand over the fix.
7. **Say "I don't know" when you don't.** Never invent facts or sources.
8. **Only use vocabulary and analogies the learner has confirmed.** An analogy from a
   domain they don't know is *adding* something to learn. (This rule was added after a
   real failure — see [Field notes](#field-notes-what-actually-happened).)

### The session loop

```
0. Load state        learner profile → topic map → due cards
1. Review due cards  questions only; the learner answers, then self-grades 1–4
2. Pretest          2–3 questions they cannot yet answer. Record the wrong guesses. Do not correct.
3. Locate           one atomic point. Check prerequisites. If a basic word is missing, add a P0 and teach that instead.
4. Teach            ≤15 lines, concrete example first, then STOP and ask
5. Self-explain     "why does this step hold?" / "what if X changed?"
6. Restate          "close the material. explain it to a 12-year-old." Then: "where is this explanation weakest?"
7. Practice         increasing difficulty; revisit the pretest answers; feedback as goal/current/next
8. Mastery gate     can explain + can apply + can recall, at ~85% accuracy. Otherwise: locate the breakpoint and re-teach only that.
9. Record           update map, cards, session log, and the learner profile
```

The step that does the most work is **step 6**, the follow-up question
*"where is this explanation weakest?"*. In testing, the learner identified a
misconception forming in their own head **before** it set — something no amount of
AI explanation would have caught.

### Prep mode (when you have source material)

If you bring a lecture recording, a textbook, or a transcript, the skill does **not**
paste it into context and start talking. It first compiles a **lesson pack**:

```
source/<material>.lesson.md
```

Every atomic point gets 11 fields: source quote + citation, mechanism, prerequisites,
worked example, misconceptions, boundaries, pretest, practice questions **with answers**,
a transfer question, and mastery criteria.

Three disciplines govern this, and they exist because of a specific failure mode:

1. **Traceability.** Every point must point back to a section number, page, or timestamp.
   If it can't, you made it up.
2. **Three-way labelling.** `[verbatim]` / `[added by me]` / `[unverified]` — never mixed.
   "The lecturer said A" and "I read in a paper that A" are different claims.
3. **Write "gap" when there's a gap.** If the source doesn't explain *why*, say so.
   **Better to leave a hole than to invent a plausible-sounding mechanism.**

The reason is blunt: source material usually has no questions and no answer key. With no
answer key, the AI generates both — and starts *teaching things the source never said*.

### The learner profile

A single global file, `learner.md`, shared across every subject. It is read at the start
of every session and it is **not** a "learning style" questionnaire — it records what you
actually know:

- **Knowledge boundaries**, split into *confirmed* (tested) vs *self-reported* (unverified).
  Self-reports are never used as a prerequisite for teaching.
- **Vocabulary list** — which terms can be used directly, which must be defined.
- **Analogy library** — the domains you're genuinely fluent in. Empty table → the skill is
  restricted to everyday analogies and forbidden from borrowing from technical fields.
- **Calibration record** — tracks self-report vs measured performance over time, so the
  skill learns how much to trust your self-assessment.

---

## Repository layout

```
learn/
├── SKILL.md                  # the main workflow + the 8 rules + known gaps
├── references/
│   ├── methods.md            # full evidence base with citations
│   ├── prep.md               # prep-mode discipline (11 fields, three-way labelling)
│   └── questioning.md        # question bank: cognitive levels, follow-up ladders
├── assets/                   # templates, copied into your data directory
│   ├── learner.md  goal.md  map.md  cards.md  session-log.md  lesson.md
└── scripts/
    └── due.py                # picks due cards out of cards.md (stdlib only)
```

Learner data is written **outside** this repo, under a single configurable root
(`$LEARN_ROOT`):

```
$LEARN_ROOT/
├── learner.md                        # global profile (shared across subjects)
└── <subject>/
    ├── goal.md  map.md  cards.md
    ├── source/<material>.lesson.md   # prep output
    └── log/YYYY-MM-DD.md             # one per session
```

The root is resolved at the start of every session: a `.learn-root` file in the skill
directory wins; otherwise the default `~/.pi/learn/` is used. Nothing is hard-coded.

---

## Install

Copy the skill directory into a location pi scans for skills:

```bash
# user-level
cp -r learn ~/.pi/skills/
# or project-level
cp -r learn .pi/skills/
```

Then `/reload` in an active session, or restart pi. Verify with `/skill:learn`.

**Requirements:** pi. Python 3 for `scripts/due.py` (standard library only). No network
access, no API keys, no external services.

## Use

```
/skill:learn teach me Fourier transforms
/skill:learn I don't understand the borrow checker
/skill:learn review software engineering
/skill:learn continue
```

Or just say it in natural language — the description routes it.

First time on a subject, the skill collects a small amount of context (why you're
learning this, deadline, time budget) and then **pretests you**.

---

## Field notes: what actually happened

This skill has been used to teach a C/embedded engineer software design from scratch
(John Ousterhout's *A Philosophy of Software Design*, compiled into a 38-point lesson pack).
Three things from that run are worth reporting honestly, because each one is a mechanism
firing:

**1. The pretest caught a fatal assumption.**
The lesson pack had been compiled from the cohesion/coupling literature — which is
written almost entirely in Java and C++. The first pretest question used the word "class".
The learner's answer was: *"what is a class?"* He writes C for microcontrollers and had
never used object-oriented code. Without the pretest, an entire session would have been
delivered in a vocabulary the learner did not have.
**Cost of pretesting: one exchange. Cost of not pretesting: the whole lesson.**

**2. Asking for reasoning caught a lucky guess.**
On a question distinguishing control coupling from stamp coupling, the learner picked the
correct option — with a reasoning chain that didn't support it. Standard tutoring records
a ✅ and moves on. Here it was logged as "right answer, wrong reason" and revisited.
**This is the fluency illusion, caught in the act.**

**3. The self-check question found the misconception before it formed.**
After restating the concept, the learner was asked where the explanation felt weakest.
He said: *"the part about passing a whole struct — that feels unclear to me."*
That was exactly the point at which he was about to conclude **"passing a struct = low
coupling"** — a rule that would have been wrong and sticky. He caught it himself.
Two sessions later he independently derived two connections that were never taught
(the mapping between the three complexity symptoms and the known-knowns/known-unknowns
framework, and the identity of "coupling" with "dependency").

### What is **not** verified

Being specific about this matters more than the successes:

- **Long-term retention is unmeasured.** Every "mastered" verdict so far is a same-day
  measurement. The spaced-repetition schedule exists precisely because same-day
  performance is not evidence. Retention data requires weeks.
- **Prep mode has only been tested on structured books**, never on the transcript input
  it was designed for (the highest-risk source class).
- **n = 1.** One learner, one subject. The mechanisms are grounded in published research;
  this skill's *implementation* of them is not itself validated.

---

## Known gaps

Recorded in `SKILL.md` so future sessions don't rediscover them:

- **No skill/practice mode.** Singing, playing an instrument, motor skills and other
  *procedural* abilities need repetition and immediate sensory feedback, not retrieval.
  Restating a pitch is meaningless; you have to sing it. The current loop is
  knowledge-only.
- **No lightweight session path.** A session currently reads 5+ files. Fine for the
  pilot, likely heavy for daily use.
- **External profile gathering is not a first-class flow.** Fetching a learner's public
  background (e.g. a video channel) proved genuinely useful for building the analogy
  library, but it currently interrupts the teaching flow.

---

## License

MIT — see [LICENSE](LICENSE).

## References

The full annotated list is in [`references/methods.md`](references/methods.md).
Key works: Rosenshine 2012 · Dunlosky et al. 2013 · Hattie & Timperley 2007 ·
Sweller et al. 2019 · Bloom 1984 · Wilson et al. 2019 · Pan & Sana 2021 ·
Brunmair & Richter 2019 · Bastani et al. 2025 (*PNAS*) · Kestin et al. 2025
(*Scientific Reports*) · Wang et al. 2024 (Tutor CoPilot).
