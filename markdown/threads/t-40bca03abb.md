[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# New Wording for EXIT rules.

_1 message · 1 participant · 2001-07_

---

### Re: New Wording for EXIT rules.

- **From:** Richard Plinston <riplin@Azonic.co.nz>
- **Date:** 2001-07-07T11:30:58+01:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3B46E4E2.6FFBB0B9@Azonic.co.nz>`
- **References:** `<4145699b.0106292212.366496bb@posting.google.com> <3B3DFB51.7679F400@iinet.net.au> <tjt407g9fv626@corp.supernews.com> <3b3f186d_2@news2.newsgroups.com> <9hncd1$g95$1@slb2.atl.mindspring.net>`

```
William M. Klein wrote:
> In my opinion, this is a "misunderstanding" of the implicit CONTINUE
> "approach"  (for NEXT SENTENCE, EXIT whatever, etc).  In my opinion, these
> "implicit CONTINUE" statements are virtual (as someone said in an earlier
> note).  

Are they virtually implicit or implicitly virtual ?    ;-)

Will you be changing the wording to reflect that they are virtual and/or
that this is a run-time not compile-time implication ?

> They *never* exist - all they are, are places to go "as if".  In
> other words, it is IMPOSSIBLE to need the CONTINUE associated with NEXT
> SENTENCE and the one for EXIT PROGRAM at the same time - as they exist ONLY
> at run-time and only one of those statements can possibly be "in effect" at
> any one time.

I am not sure how useful to a compiler writer this 'clarification' is. 
If the language was being interpreted at run-time then it may be said
that it is only necessary for one to be 'in effect'.  However the whole
point of compiling, even in languages such as Python, is that these
issues are _not_ left until run-time to be resolved.  The points to
which the GO TOs, NEXT SENTENCEs, EXIT PARAGRAPHs etc are to resume
execution are resolved at _compile_time_.  The whole concept of
'implicit CONTINUEs' is seriously flawed if each time a NEXT PARAGRAPH
is encounted the 'run-time' has to work out where this 'implicit
CONTINUE' should be created, even if it is 'virtual'.

It should be possible for the _compiler_ to generate the equivalent of a
JMP instruction whenever it meets an EXIT PARAGRAPH rather than having
the run-time re-enter a compiling phase to create a new CONTINUE to work
out where it is going.

Fortunately the compilers only have to generate code to simulate what is
written and can ignore the convoluted and pointless mechanism you have
invented (and now re-invented with virtual and run-time requirements).
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
