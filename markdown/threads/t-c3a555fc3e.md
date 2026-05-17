[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Comparing Modula2 and Cobol

_3 messages · 3 participants · 1994-11 → 1994-12_

---

### Comparing Modula2 and Cobol

- **From:** "bruce..." <ua-author-10849682@usenetarchives.gap>
- **Date:** 1994-12-01T07:43:01+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<ua-fallback-_R8RBXIonec@usenetarchives.gap>`

```
ip-l.··.@lad··c.uk wrote in a message to All:

icuau> I have an assignment to do on Cobol, what
icuau> sort of differences there are between it and other
icuau> languages, i.e. the main features of the language. I know
icuau> Modula2 reasonbly well, but don't know Cobol very well at
icuau> all. Could someone give me some references, ideas on the
icuau> main points /advantages of Cobol.

The two languages are both fairly traditional procedural languages; despite
what anyone else may tell you, the similarities are far greater than the
differences. Both languages have a complement of structured programming
constructs; both have subroutines, local and global variables, modularity,
and so on. That understood, let's go on to the differences.

Philosophically, the languages are different. Modula-2 is a rather
minimalist language; COBOL is large. Modula is terse, with a clean
structure; COBOL is verbose with a fair amount of syntactic and structural
clutter (which makes the language look more English-like, and encourages
people to program when they would perhaps be better off in another field,
such as forestry).

COBOL's strengths are its extensive built-in data types and operations, and
its attractive and readable way of defining data structures (alias records,
alias group fields). Its disadvantages include lack of user-defined data
types, lack of type checking in subroutine calls, method of parameter passing
(by reference or by value) being specified in the wrong place (at the call
rather than at the procedure definition), poor string handling facilities
(many COBOL programmers don't believe this), and a tradition of writing
non-modular, non-structured code (this used to be necessary, but modern COBOL
fixes this. Now, if only the mainstream programmers would catch on...).

Bruce
---------
Fidonet: Bruce Feist 1:109/615
Internet: Bru··.@f61··t.org
```

#### ↳ Re: Comparing Modula2 and Cobol

- **From:** "cf..." <ua-author-16040464@usenetarchives.gap>
- **Date:** 1994-11-29T10:21:02+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-c3a555fc3e-p2@usenetarchives.gap>`
- **In-Reply-To:** `<ua-fallback-_R8RBXIonec@usenetarchives.gap>`
- **References:** `<ua-fallback-_R8RBXIonec@usenetarchives.gap>`

```
In article <199··.@pat··c.uk> ip-l.··.@lad··c.uk (IP Lancaster) writes:
› of England, in my 2nd year. I have an assignment to do on Cobol, what sort of 
› differences there are between it and other languages, i.e. the main features of
› the language. I know Modula2 reasonbly well, but don't know Cobol very well at
› all. Could someone give me some references, ideas on the main points /advantages of Cobol.
› P.S. My assignment has to be in by 16th dec 1994, so not much time!

Ha ha haaa!
I seriously doubt you will learn COBOL in two weeks. You may get your
program running though. It took me several months to "learn" COBOL.

As far as a comparison, the two language aren't very similar.
Modula supports separate compilation, not so for COBOL.
Modula has local variables, again not so for COBOL
Modula is strongly typed, not COBOL.
COBOL is rather fixed format and wordy, not Modula.
etc. etc. etc.

BTW, I use COBOL every day and I actually like it.

--------------------
Colin Foss
Non illigemati carborundum est.
cf··.@nbn··b.ca
c5··.@spi··b.ca
```

#### ↳ Re: Comparing Modula2 and Cobol

- **From:** "don nelson" <ua-author-20234@usenetarchives.gap>
- **Date:** 1994-12-01T13:45:03+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-c3a555fc3e-p3@usenetarchives.gap>`
- **In-Reply-To:** `<ua-fallback-_R8RBXIonec@usenetarchives.gap>`
- **References:** `<ua-fallback-_R8RBXIonec@usenetarchives.gap>`

```
In article Colin Foss, cf··.@gov··b.ca
writes:
› In article <199··.@pat··c.uk>
› ip-l.··.@lad··c.uk 
…[13 more quoted lines elided]…
› program running though.  It took me several months to "learn" COBOL.

You are right here. However, I know people who have learned it
pretty well in a few weeks. Dedication and all that. However, to
try to show the differences when you don't at all understand COBOL
and you have two weeks to accomplish the task is almost impossible.

› As far as a comparison, the two language aren't very similar.
› Modula supports separate compilation, not so for COBOL.
 
› Wrong.  COBOL 85 supports separate compilation.
 
› Modula has local variables, again not so for COBOL

Wrong. COBOL 85 has local variables (and shared ones). See nested
programs in COBOL 85.

› Modula is strongly typed, not COBOL.
 
› Right. However, some strong typing is being added in COBOL 97.
 
› COBOL is rather fixed format and wordy, not Modula.

Right. The fixed format goes in COBOL 97. The wordy part is one of
the strenghts of COBOL (you can actually understand a program you did
not write).

› etc. etc. etc.
›
› BTW, I use COBOL every day and I actually like it.

I would hope you would learn about COBOL 85. A copy of my book (for
a mere $10) would bring you up to date in a couple of hours. E-mail
me for info.

Don Nelson
COBOL Development, Tandem Computers, Inc.
Member, ANSI X3J4 and ISO/IEC JTC1/SC22 WG4 COBOL Committees
Project Editor, 1997 ISO COBOL Standard
Moderator, COBOL Conference, Bix
nel··.@tan··m.com
do··.@b··.com
No clever quotes here
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
