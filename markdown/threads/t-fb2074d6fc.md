[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# While the Alphabet Thread Rages...

_4 messages · 4 participants · 2003-06_

---

### While the Alphabet Thread Rages...

- **From:** Joe Zitzelberger <joe_zitzelberger@nospam.com>
- **Date:** 2003-06-03T02:03:16-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<joe_zitzelberger-7FC69F.02031603062003@corp.supernews.com>`

```

I was scanning the alphabet thread and its various child, grand-child 
and great-grand-child threads and I started to wonder:

If negative logic is bad, why does Cobol require its use in many perform 
exit conditions?

In some cases it is hard, or unnatural to state the exit condition 
purely.  One is forced to prefix it with a NOT.

Why is there no perform/while?  I think it would be awfully nice to 
write something like:

   PERFORM Lurk-In-Comp-Compilers
     WHILE Alphabets-thread-is-alive

   
instead of:

   PERFORM Surf-Aimlessly
     UNTIL NOT Alphabets-thread-is-alive


Just thinking out loud...
```

#### ↳ Re: While the Alphabet Thread Rages...

- **From:** "Howard Brazee" <howard@brazee.net>
- **Date:** 2003-06-03T14:38:06+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<bbibse$caf$1@peabody.colorado.edu>`
- **References:** `<joe_zitzelberger-7FC69F.02031603062003@corp.supernews.com>`

```

On  3-Jun-2003, Joe Zitzelberger <joe_zitzelberger@nospam.com> wrote:

> If negative logic is bad, why does Cobol require its use in many perform
> exit conditions?
…[14 more quoted lines elided]…
>      UNTIL NOT Alphabets-thread-is-alive

Without arguing your basic "If negative logic is bad", I don't code quite the
same way.

PERFORM process-file
    Until file-eof

PERFORM walk-set
    Until ANY-ERROR-STATUS

Those don't seem to be negative logic to me.
```

#### ↳ Re: While the Alphabet Thread Rages...

- **From:** LX-i <DanielJSNOSPAM@Knology.net>
- **Date:** 2003-06-03T20:35:56-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3EDD4CFC.6060609@Knology.net>`
- **References:** `<joe_zitzelberger-7FC69F.02031603062003@corp.supernews.com>`

```
Joe Zitzelberger wrote:
> In some cases it is hard, or unnatural to state the exit condition 
> purely.  One is forced to prefix it with a NOT.
…[11 more quoted lines elided]…
>      UNTIL NOT Alphabets-thread-is-alive

Or

PERFORM Drum-Fingers
   UNTIL Alphabet-thread-is-dead

That's the thing I like about 88-levels - you can use words to define 
"not" conditions.  Then, even if your name has the word "not" in it, you 
don't have to use NOT logic to use it.  I routinely use

Perform Until WS-Time-to-Go

...for looping in interactive programs.  (Of course, I did actually code 
a "Go to" loop recently, but it was clear what it did...

001-Endless-Loop.
     Do stuff...
     Go to 001-Endless-Loop.
002-Stop-Run.
     Stop Run.

It is a background run that is designed to run whenever the mainframe is 
up, and all it does is send a transaction every 5 minutes (or whatever 
interval is set in the file).  Then, it goes to sleep for 15 seconds, 
wakes up, checks to see if it's time to fire again or if the interval 
has changed, then repeats.)

Having a COBOL programmer do VB can be good (their code is generally 
easier to read, as they're used to indenting and such), but it can also 
render some humorous constructs.  The Do loop in VB allows "While" or 
"Until" as the condition definition.  However, the VB programmers that 
trained me called it a "Do While" loop instead of just a "Do" loop.  So, 
you end up with "Do While Not" loops, which are actually "Do Until" loops.

I wouldn't be opposed to adding the WHILE clause as an acceptable 
modifier for the PERFORM verb though - so there's one vote "for" it.  :)
```

#### ↳ Re: While the Alphabet Thread Rages...

- **From:** "Donald Tees" <Donald_Tees@sympatico.ca>
- **Date:** 2003-06-07T13:00:33-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<dToEa.5630$IR1.809771@news20.bellglobal.com>`
- **References:** `<joe_zitzelberger-7FC69F.02031603062003@corp.supernews.com>`

```
"Joe Zitzelberger" <joe_zitzelberger@nospam.com> wrote in message
news:joe_zitzelberger-7FC69F.02031603062003@corp.supernews.com...
>
> I was scanning the alphabet thread and its various child, grand-child
…[13 more quoted lines elided]…
>

There is ....

        PERFORM LURK-IN-COMP-COMPILERS
            WITH TEST AFTER ..

Donald
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
