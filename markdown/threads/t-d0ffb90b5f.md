[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Hardware support for decimal (was something else)

_1 message · 1 participant · 2003-04_

---

### Re: Hardware support for decimal (was something else)

- **From:** robert@wagner.net (Robert Wagner)
- **Date:** 2003-04-07T22:31:03+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3e91f9a0.89046780@news.optonline.net>`
- **References:** `<3e7c2b28.237800105@news.optonline.net> <3E8D9230.58CD45BB@istar.ca> <3e8e7d37.5785621@news.optonline.net> <b6ng5o$g6c$2@aklobs.kc.net.nz> <3e8f504f.59833942@news.optonline.net> <b6octq$oq$1@aklobs.kc.net.nz> <i6d39vsbsfk08ms3vj7l2ldmass033d1tq@4ax.com>`

```
Michael Todd <mikltodd@comcast.net> wrote:

>On Mon, 07 Apr 2003 05:10:49 +1200, Richard Plinston <riplin@Azonic.co.nz>
wrote:
>
>Note, S9(9) binary (however you specify it) uses 32 bit math.  S9(10)v999
…[3 more quoted lines elided]…
>whether addressability was assigned to a register by a previous verb)

Correct so far. 

>while ADD +1 TO (64 bit binary) requires 15 to 18 instructions.

No, it requires one additional instruction: 

LM  1,2,thenumber
AL   2,=F'1'
ALC 1,=F'0' 
STM 1,2,thenumber

>Even on machines supporting 64 bit binary math, IBM COBOL isn't using those 64
>bit instructions.

They would save two instructions:

LA      1,1(thenumber)
STG    1,thenumber

As you probably know, a 32-bit Intel processor requires two instructions to add
1 to a 64-bit number: 

add   word ptr thenumber+2, 1
adc   word ptr thenumbr, 0

That's twice as many as adding 1 to a 16-bit number, not to mention an inc is
(used to be) faster than an add with immediate value. I don't understand why my
benchmark showed times exactly the same. I suspect the cpu is optimizing out the
adc when there is no overflow, which will occur only 1 time out of 64K. 

>>Robert Wagner wrote:
>>
…[17 more quoted lines elided]…
>>
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
