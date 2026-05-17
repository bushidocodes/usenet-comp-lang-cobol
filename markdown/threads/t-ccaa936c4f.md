[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# PowerCOBOL - where to from here?

_1 message · 1 participant · 2015-03_

---

### PowerCOBOL - where to from here?

- **From:** "dashwood" <ua-author-2154790@usenetarchives.gap>
- **Date:** 2015-03-16T19:13:01+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<cmp6d9F2n7vU1@mid.individual.net>`

```
Back in the day, Fujitsu offered PowerCOBOL as a "Quick Build" GUI for
COBOL.

It was (and is...) an excellent way to build Windows applications driven by
COBOL.

It was also a very good way for COBOL developers to get a toe into the world
of event driven programming, and, simultaneously, get some insight into the
world of objects.
(PowerCOBOL is completely Object Oriented under the covers and deals with
forms and screen controls which Windows considers to be "objects"; however,
you don't need OO COBOL knowledge to use it, as the complexity is abstracted
away by the system.)

Many people (self included...) jumped into this and learned about objects
and events...

You could knock up a PowerCOBOL form in a few minutes using the IDE provided
and you could drop controls on it and process the events they raised (things
like mouse clicks...) very easily. Unlike Micro Focus' similar "Panels"
technology, the event processing could be "scripted" in COBOL, rather than a
proprietary scripting language.

You could wrap your application as a Fujitsu PowerCOBOL project and the
screens and scripts it used, along with any other resources you wanted,
could be managed through the Project IDE.

The results were very satisfying and it was nice to see COBOL taking its
place in the world of GUIs, events, and objects...

But, time moves on. Fujitsu COBOL changed vendors, the focus moved to the
new CLI generating compilers (COBOL for .Net) and PowerCOBOL was largely
forgotten about. People could do the same kind of development using Visual
Studio with .Net controls (VS also has a "design surface" where you can
create forms and drag and drop controls on them, and it is much richer than
the one provided in the PowerCOBOL IDE, also, it is FREE...). Similarly, you
can "wire up" the events in your VS form to code in a .Net language (I use
C#) and get better overall choice and functionality than is available
through PowerCOBOL.

So the PowerCOBOL community needed a "Migration Path" to modernize their
PowerCOBOL applications and give them options about whether they would stay
with COBOL or not.

Unfortunately, no such path has been provided by Fujitsu. The question of
where to go with PowerCOBOL raises a resounding silence.

I started looking at this a couple of years ago and it has been a "back
burner" project for me until the present.

I'm pleased to say that the problem of getting PowerCOBOL screens to
"describe themselves" (so they can be "equivalenced" in .Net...) has been
solved and it is now possible to generate a Windows Form from a PowerCOBOL
one. The next step is to obtain all the existing scriptlets for event
processing from the PowerCOBOL project and get them into a form where they
would be acceptable for wiring into the Windows Form. (In .Net, this is
referred to as "code-behind"). I'm currently working on this and expect to
have a releasable solution within the next few weeks.

The aim is to have an automated process that will analyze your existing
PowerCOBOL Forms, and generate Windows Forms equivalents with the events all
wired to your existing scriptlets. This means you can continue to maintain
your PowerCOBOL applications WITHOUT them being tied to PowerCOBOL projects.
You have a richer choice of available controls and you can script the
code-behind using COBOL (as at present), OR a .Net language, or even a
mixture of both. You simply move out of the PowerCOBOL IDE and into the
.Net one, with the process automated for bringing your existing
applications.

Watch this space...

Pete.
"I used to write COBOL...now I can do anything."
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
