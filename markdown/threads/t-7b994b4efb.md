[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Time sensitive programming?

_5 messages · 5 participants · 2000-02 → 2000-03_

---

### Time sensitive programming?

- **From:** hancock4@bbs.cpcn.com (Lisa nor Jeff)
- **Date:** 2000-02-27T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<89a9od$9pu@netaxs.com>`

```
I understand in early machines (such as the MICR example mentioned
above), the programming had to be time sensitive, that is, certain
things happened in real time and the program had to be aware of
that.

What confuses me about such systems is why they were time dependent
at all, instead, why didn't the machines set some sort of flag that
could be tested.  In reading 1401/1410 documentation, it appears
there were bit indicators that could be tested to verify an I/O
operation was completed--this was necessary when using the CPU
overlap feature.

What kinds of COBOL applications on what machines were time
dependent?  What happened when they wanted to migrate to
different hardware (either the peripheral or the CPU)--did
the whole thing have to be re-written?
```

#### ↳ Re: Time sensitive programming?

- **From:** sff5ky@aol.comxxx123 (Sff5ky)
- **Date:** 2000-02-27T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<20000227004633.06851.00000196@nso-fb.aol.com>`
- **References:** `<89a9od$9pu@netaxs.com>`

```
In article <89a9od$9pu@netaxs.com>, hancock4@bbs.cpcn.com (Lisa nor Jeff)
writes:

>
>What confuses me about such systems is why they were time dependent
…[10 more quoted lines elided]…
>

The timing issues are related to the amount of time it takes a document
to move from the 'read' location to a 'commit point'.  The program must have 
a pocket designation back to the device before the document reaches
the 'commit point' or SSSHHHRREEEEDDDD!  In the older MICR Readers
that used metal sleeves, if the document got to the commit point before the
'pocket select' decision, checks would be cut in half (length ways).  Later 
machines would dump everything to the Reject pocket while still other 
machines would sling the checks all the way to the last pocket on the machine.
```

##### ↳ ↳ Re: Time sensitive programming?

- **From:** Ed Guy <ed_guy@NOSPAMguysoftware.com>
- **Date:** 2000-02-26T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<38B8CFFB.3283@NOSPAMguysoftware.com>`
- **References:** `<89a9od$9pu@netaxs.com> <20000227004633.06851.00000196@nso-fb.aol.com>`

```
Sff5ky wrote:
> 
> In article <89a9od$9pu@netaxs.com>, hancock4@bbs.cpcn.com (Lisa nor Jeff)
…[23 more quoted lines elided]…
> machines would sling the checks all the way to the last pocket on the machine.

Or in the case of the 1418 optical reader I mentioned, the documents weren't damaged.  
You just had a stack of a few thousand meter reading cards and you knew half a dozen 
hadn't read properly, but you didn't know WHICH half dozen.

It says a lot for the early machines that an 8k 1401 could drive the 1418 reader while 
simultaneously doing a totally unrelated print job on its 1403.

How would a programmer be intimately aware of what the operators had the machines doing? 
 In England in the 1960s, lots of office buildings had no air conditioning expect in the 
computer room, so on a hot summer day we had a tendency to schedule "Witnessed Tests".
```

##### ↳ ↳ Re: Time sensitive programming?

- **From:** "David Olson" <dqolson@fastdial.net>
- **Date:** 2000-03-07T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<sca7oef6bi722@corp.supernews.com>`
- **References:** `<89a9od$9pu@netaxs.com> <20000227004633.06851.00000196@nso-fb.aol.com>`

```
> The timing issues are related to the amount of time it takes a document
> to move from the 'read' location to a 'commit point'.  The program must
have
> a pocket designation back to the device before the document reaches
> the 'commit point' or SSSHHHRREEEEDDDD!  In the older MICR Readers
> that used metal sleeves, if the document got to the commit point before
the
> 'pocket select' decision, checks would be cut in half (length ways).
Later
> machines would dump everything to the Reject pocket while still other
> machines would sling the checks all the way to the last pocket on the
machine.
>
>

Even more "interesting" was a similar problem with GE check sorter-readers.
When they didn't get a command fast enough, they did a "bogie reset" ...in
other words took all the feed rollers up from the document path. The result
was a literal blizzard of checks:) The problem was, which three of them had
already been read when the storm started:) And before you say solving that
problem is easy, this was before the days when check numbers were routinely
encoded on the checks:)

Ahhhh...the memories are fading....
```

#### ↳ Re: Time sensitive programming?

- **From:** "Jerry P" <bismail@bisusa.com>
- **Date:** 2000-02-27T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<z_nu4.451$z92.12339@news.swbell.net>`
- **References:** `<89a9od$9pu@netaxs.com>`

```
There were (are) two reasons for time dependency:

1. Something must happen before an already-started physical event
needs the answer. Read a card and decide into which pocket to put the
card before the card reaches the pocket is one example.

2. Multiple processors. We had an array processor with 8 cpus. To
perform arithmetic operations on an array (say, convert 2-byte integer
to 4-byte, then turn on the high-order bit), the 2nd process must not
start too soon or it could catch up and pass the first process. But it
would be an awful waste to wait for the 1st process to complete before
starting the 2nd.

Lisa nor Jeff <hancock4@bbs.cpcn.com> wrote in message
news:89a9od$9pu@netaxs.com...
> I understand in early machines (such as the MICR example mentioned
> above), the programming had to be time sensitive, that is, certain
…[13 more quoted lines elided]…
> the whole thing have to be re-written?
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
