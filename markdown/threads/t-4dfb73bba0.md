[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Restructure this!

_1 message · 1 participant · 2003-08_

---

### Re: Restructure this!

- **From:** Richard Plinston <riplin@Azonic.co.nz>
- **Date:** 2003-08-10T07:47:48+12:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<bh3j7m$640$1@aklobs.kc.net.nz>`
- **References:** `<bh1257$tb83u$1@ID-184804.news.uni-berlin.de> <%RWYa.5405$BC2.2463@newsread2.news.atl.earthlink.net> <t31ajvsg887opr4p2nlrb3asa75je0tepk@4ax.com>`

```
Volker Bandke wrote:

> I must be overlooking the obvious.  Where is the difference between
> 
…[6 more quoted lines elided]…
> better readability, but as far as avoiding GO TOs it is not a solution

The point about 'avoiding GOTO' is not the GO TO.  There is absolutely 
nothing wrong with GO TO, it a simple and obvoius statement that is very 
clear about what will happen.

The point about 'avoiding GOTO' is the label, the paragraph name that is 
the target.

When examining a program it is done small bits at a time.  When a part 
includes a label then it must be resolved as to the efeect of that label on 
the flow of logic.  It may be dropped thru from above, be the target of a 
goto, it may terminate the scope of a perform or be the target of a perform.

Other languages use different types of labels for different actions and so 
at any label (or function name etc) it is absolutely clear what will 
happen, and where that may be from, the language guarantees it.

In Cobol in the general case it is necessary to examine the whole program 
in order to be sure what happens at each label.  Some styles use idiomatic 
mechanisms to give confidence that only certian logic flow is used.  eg 
nnn-exit should only ever be used as a drop through or goto from within the 
nnn-name paragraph or section.

However, because this is not checked by the compiler there is actually no 
guarantee that 'perform 3120-name thru 3140-exit' has not been coded either 
deliberately or accidentally, nor that 3150-name does not contain a goto 
3140-exit.  Or, indeed, that there is not a perform 3140-name without the 
required thru.

This means that to check a program in Cobol that contains a PERFORM THRU, 
or a GO TO, or a PERFORMed SECTION, it is necessary to check every path 
through the code for correctness manually.  It is possible to mechanise the 
process and have the idiom so formalised that a program can check it.  
Judson did this with some success allegedly.  In the general case this is 
not viable.

Another way to guarantee (with simple checks) how a program works around 
each label is to eliminate performed sections and perform thru.  This can 
be checked for with grep.  A consequence of this is that goto cannot be 
used (but EXIT PARAGRAPH can).

The aim is _not_ to eliminate GOTO, the aim is to make a program 
understandable in small modules and have this understanding _guaranteed_.  
The mechanisms to do this happens to make goto unavailable.
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
