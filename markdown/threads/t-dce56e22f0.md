[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# ANSI vs ASCII characters

_2 messages · 2 participants · 1999-06_

---

### ANSI vs ASCII characters

- **From:** "William M. Klein" <wmklein@nospam.netcom.com>
- **Date:** 1999-06-24T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7ku9ne$mik@dfw-ixnews3.ix.netcom.com>`

```
Am I the only one who is confused?

In another thread there are several references to ANSI vs ASCII characters.
As someone who follows (reasonably closely) all the relevant Standards, I
don't know what they are talking about.

The ISO Standard for ASCII (which is only a 7-bit, not 8-bit definition) is
identical to the ANSI Standard (which also defines only the 7-bit
characters).  There is ONE (minor) difference and that has to do with the
currency sign symbol - and even that is defined in BOTH as being one of
several "symbols".  (Actually, I think the tilde vs the not-sign are also
"known" variations that both definitions allow.)

When it comes to the 8-bit character sets, then both ANSI and ISO (for
ASCII) are almost completely silent.  In other words, anything in the
"top-half" of an 8-bit character set is "up in the air" and not a part of
any ANSI or ASCII definition (or rather there are LOTS of conflicting
definitions for them).

Given all of this, can someone help me understand what is really meant by
the discussion of "ASCII" vs "ANSI" characters???

P.S.  If we start getting into DBCS (double-byte character sets) including
ISO 10646 or Unicode, or similar "variations" - there is an entire other
discussion - but neither of these would (normally?) be called either ASCII
or ANSI character sets.
```

#### ↳ Re: ANSI vs ASCII characters

- **From:** "Cheesle" <cheesle@online.NoSpamPlease.no>
- **Date:** 1999-06-24T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7kubnv$p4o$1@news.cerf.net>`
- **References:** `<7ku9ne$mik@dfw-ixnews3.ix.netcom.com>`

```

William M. Klein wrote in message <7ku9ne$mik@dfw-ixnews3.ix.netcom.com>...
>Am I the only one who is confused?
>Given all of this, can someone help me understand what is really meant by
>the discussion of "ASCII" vs "ANSI" characters???

I am sorry for probably being one of those to contribute to your confusion,
however, I will hereby try to heal the "damage".

You are absolutely correct that the ASCII is 7 bit. However, outside of USA,
this "label" has been used as the notation of the 8 bit set holding a number
of 256 characters, although it is not technically correct.

The problem we europeans struggle with, is precisely that you americans do
not have to pay attention to the 8 bit set. When the ANSI set where defined,
this was apparently ruled by Americans since the match of the first 7 byte
is (as you point out) almost identical, at least practical identical. The
rest of the letters in the ANSI characterset and the extended "ascii" set is
widely different. This is a big problem for developers targeting the
european market, or any market for that matter that has a character set
which extends the standard ascii. Most older applications in the PC market
dealed well with the characters, because there were national charactersets
on the national computers. Though, problems rose then too, like I mentioned
before, printers were preconfigured for american sheets and character sets
and so on. I can tell you I have been through many nasty printer setups
throughout the years :-)

The predefined printer setup isn't that big issue, if you use the windows
printer spooler, knows to deal with the driver/spooler *and* has a native
windows application. Native in the sense that it is entirely ansi coded and
has ansi data.

Funny things raise when you move applications, I have been into the
following:

    Application coded in ascii, data in ascii

    Application coded in ansi, data in ascii

    Application coded in ascii, data in ansi

All of these needs special preparation to be able to run. They turn
particularly difficult if you are so "lucky" to use an IDE for application
development. Consider loading an existing application coded in ascii into a
fully windows IDE that deals with ANSI only... It really turns out to be a
mess.

It is really amusing to run such programs under windows, whether to screen
or printer. What you expect to get is definitely not what you get.

The problem is our dear european characters, here is my history:

Back in the early days, there were 7 bits computers and printers (some of
the latter actually still in use today in Norway), Norwegian letters then
replaced the [\] and {|}, in other words, sorting were excellent, after all,
end users had rarely use of this characters.

So, the evolution to 8 bit arrived and national characters seemed to be
placed occasionally at best.
The Norwegian special letters ae, oe, aa or AE, OE, AA (I presume I cannot
show them real due too, guess what :-) ). The order I have presented them
above is the standard sort order. However, when put into the extended
character set and ANSI, they were placed in an unsortable order. Look:

Character            Ext Ascii            ANSI
ae                        145                     230
oe                        155                     248
aa                        134                     229
AE                        146                    198
OE                        157                    216
AA                        143                    197

As you can see, developers for the norwegian market does not get anything
free. Same applies to
Germany, France, Spain to mention a few.

So, basically what OemToAnsi and AnsiToOem does is to map back and forth.
These functions are a part of the Windows API, constructed to deal with this
problem.

I hope this cleared out some of your confuseness, if not, please let me know
and I will try again.

Cheesle
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
