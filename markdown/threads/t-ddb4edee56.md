[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# ATTN: DD

_3 messages · 2 participants · 2007-06_

---

### ATTN: DD

- **From:** Alistair <alistair@ld50macca.demon.co.uk>
- **Date:** 2007-06-02T15:06:46-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1180822006.061423.92230@o5g2000hsb.googlegroups.com>`

```
Just thought you might like to know:

My booz'm chum (this is a Saturday night) says that he likes your
solution to the two simultaneous reads of one file problem and that he
is now extending it to read three invocations of the same file
simultaneously. He thinks it is rather neat.

Me, I'm too pissed to remember what the original solution was!
```

#### ↳ Re: ATTN: DD

- **From:** docdwarf@panix.com ()
- **Date:** 2007-06-03T01:53:01+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<f3t6tt$h2a$1@reader2.panix.com>`
- **References:** `<1180822006.061423.92230@o5g2000hsb.googlegroups.com>`

```
In article <1180822006.061423.92230@o5g2000hsb.googlegroups.com>,
Alistair  <alistair@ld50macca.demon.co.uk> wrote:
>Just thought you might like to know:
>
…[5 more quoted lines elided]…
>Me, I'm too pissed to remember what the original solution was!

I didn't remember it either until you just mentioned it now... I believe 
it had to do with addressing the same dataset by two different internal 
names, as in

SELECT FILE01 ASSIGN TO FILE01.
SELECT FILE02 ASSIGN TO FILE02.

... and the JCL (or however that platform related internal to external 
names) would be along the lines of:

//FILE01  DD  DSN=SOME.DATASET.NAME,DISP=SHR
//FILE02  DD  DSN=SOME.DATASET.NAME,DISP=SHR

... so that when, say, SOME.DATASET.NAME contained the following records:

0010
0020
0030
0040
0050

... then code similar to:

PERFORM 4 TIMES
    READ FILE01
    END-READ
END-PERFORM
READ FILE02
END-READ
DISPLAY 'FILE01-REC = ', FILE01-REC
DISPLAY 'FILE02-REC = ', FILE02-REC

... would (assuming a bunch of other stuff, such as FDs and the like) give 
output of

FILE01-REC = 0040
FILE02-REC = 0010

... where both records came out of the same dataset.

Now, it seems, he wants to do it again... and this reinforces Yet Another
Prejudice of mine, similar to the one against solutions which are prefaced
by 'All ya gotta do is...' ... and that Prejudice is against someone who
tells me 'We'll only need this once, just this once...'

... because - especially with computers, being the kind of devices they 
are - If Something Can Be Done Once Then That Something Can Be Done 
Forever.  An ugly, wretched, cobbled-together 'do it just this one time, 
no matter how' chunk of code becomes a part of the Production System... 
and then, as the System grows, this chunk of code is stretched beyond its 
design limits and starts to do Bad Things... and someone is sure to say 
'Who wrote this crap, *anyone* can see it isn't fit to run...' ... when 
the circumstances of its current running are far, far different than those 
for which it was originally designed... which were to be '... once, just 
this once.'

DD
```

##### ↳ ↳ Re: ATTN: DD

- **From:** Alistair <alistair@ld50macca.demon.co.uk>
- **Date:** 2007-06-03T07:59:08-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1180882748.595714.234120@o5g2000hsb.googlegroups.com>`
- **In-Reply-To:** `<f3t6tt$h2a$1@reader2.panix.com>`
- **References:** `<1180822006.061423.92230@o5g2000hsb.googlegroups.com> <f3t6tt$h2a$1@reader2.panix.com>`

```
On 3 Jun, 02:53, docdw...@panix.com () wrote:
> In article <1180822006.061423.92...@o5g2000hsb.googlegroups.com>,
>
…[66 more quoted lines elided]…
> DD

I think that we have all been there with the run-once developments
that get further developed and become permanent solutions.
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
