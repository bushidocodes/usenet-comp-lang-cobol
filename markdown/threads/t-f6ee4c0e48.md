[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# IS NUMERIC check for SPACES

_13 messages · 7 participants · 2009-11 → 2009-12_

---

### IS NUMERIC check for SPACES

- **From:** yogi <yogibad@gmail.com>
- **Date:** 2009-11-30T18:49:58-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<ac1c02d1-64a3-400b-9c9a-63989d519a2b@f16g2000yqm.googlegroups.com>`

```
Hi All,
            I had a question regarding blanks or SPACES in numeric
fields. Would SPACES pass the IS NUMERIC test used for checking if the
value is numeric or not. Since SPACES can be compared arithmetically
(> SPACES), I was wondering if it would pass the IS NUMERIC test.

Thanks in advance
```

#### ↳ Re: IS NUMERIC check for SPACES

- **From:** Richard <riplin@Azonic.co.nz>
- **Date:** 2009-11-30T19:01:58-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<96a9f7a8-a3d7-400f-8e0b-97a5b7ef920e@a39g2000pre.googlegroups.com>`
- **References:** `<ac1c02d1-64a3-400b-9c9a-63989d519a2b@f16g2000yqm.googlegroups.com>`

```
On Dec 1, 3:49 pm, yogi <yogi...@gmail.com> wrote:
> Hi All,
>             I had a question regarding blanks or SPACES in numeric
…[4 more quoted lines elided]…
> Thanks in advance

SPACE is not a numeric digit.
```

#### ↳ Re: IS NUMERIC check for SPACES

- **From:** "William M. Klein" <wmklein@nospam.netcom.com>
- **Date:** 2009-11-30T22:21:24-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<bR0Rm.277892$sz1.97428@en-nntp-10.dc1.easynews.com>`
- **References:** `<ac1c02d1-64a3-400b-9c9a-63989d519a2b@f16g2000yqm.googlegroups.com>`

```
Easy answer, when running in "standard conformance" mode, IF NUMERIC will 
fail when a field contains spaces.  It will also have "unpredictable 
results" if a field deinfed as numeric includes spaces when compared to 
SPACERS or anything else - at run-time.

HOWEVER, results with specific ompiler may vary.  In particular, the use of 
the ZWB compiler option (IBM and MF) impacts how USAGE DISPLAY numeric 
fields are treaded when some "bytes" contain spaces.

"yogi" <yogibad@gmail.com> wrote in message 
news:ac1c02d1-64a3-400b-9c9a-63989d519a2b@f16g2000yqm.googlegroups.com...
> Hi All,
>            I had a question regarding blanks or SPACES in numeric
…[4 more quoted lines elided]…
> Thanks in advance
```

##### ↳ ↳ Re: IS NUMERIC check for SPACES

- **From:** Howard Brazee <howard@brazee.net>
- **Date:** 2009-12-01T08:25:56-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<9bdah59bd3mm0f2l55hfssk4bnt3n7ifs6@4ax.com>`
- **References:** `<ac1c02d1-64a3-400b-9c9a-63989d519a2b@f16g2000yqm.googlegroups.com> <bR0Rm.277892$sz1.97428@en-nntp-10.dc1.easynews.com>`

```
On Mon, 30 Nov 2009 22:21:24 -0600, "William M. Klein"
<wmklein@nospam.netcom.com> wrote:

>Easy answer, when running in "standard conformance" mode, IF NUMERIC will 
>fail when a field contains spaces.  It will also have "unpredictable 
>results" if a field deinfed as numeric includes spaces when compared to 
>SPACERS or anything else - at run-time.

I never cared for the definition of IF NUMERIC.
```

###### ↳ ↳ ↳ Re: IS NUMERIC check for SPACES

- **From:** "William M. Klein" <wmklein@nospam.netcom.com>
- **Date:** 2009-12-01T09:40:28-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<NNaRm.292260$uO.92153@en-nntp-09.dc1.easynews.com>`
- **References:** `<ac1c02d1-64a3-400b-9c9a-63989d519a2b@f16g2000yqm.googlegroups.com> <bR0Rm.277892$sz1.97428@en-nntp-10.dc1.easynews.com> <9bdah59bd3mm0f2l55hfssk4bnt3n7ifs6@4ax.com>`

```
One addendum to my original response.  I can't remember (and haven't looked 
it up today) whether the '02 Standard allows an "If numeric" test on a 
numeric-edited field,  If so, then where the picutre string has "Z" or if 
the data definition has "blank when zero", then IF numeric would "pass" when 
spaces were in such a field.  As I say, I don't remember is this is either 
Standard conforming or allowed by any, many, or no compilers - buti it does 
make sense for spaces to be "allowed' where the data definition says they 
are allowed.

(I am out of town and can't easiy est or research this.  If I get a "better" 
answer later in the week, I will post that)

"Howard Brazee" <howard@brazee.net> wrote in message 
news:9bdah59bd3mm0f2l55hfssk4bnt3n7ifs6@4ax.com...
> On Mon, 30 Nov 2009 22:21:24 -0600, "William M. Klein"
> <wmklein@nospam.netcom.com> wrote:
…[13 more quoted lines elided]…
> - James Madison
```

#### ↳ Re: IS NUMERIC check for SPACES

- **From:** spambait@milmac.com (Doug Miller)
- **Date:** 2009-12-02T04:24:34+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<hf4q6j$n1m$4@news.eternal-september.org>`
- **References:** `<ac1c02d1-64a3-400b-9c9a-63989d519a2b@f16g2000yqm.googlegroups.com>`

```
In article <ac1c02d1-64a3-400b-9c9a-63989d519a2b@f16g2000yqm.googlegroups.com>, yogi <yogibad@gmail.com> wrote:
>Hi All,
>            I had a question regarding blanks or SPACES in numeric
>fields. 

In the time it took you to post this question and read the responses, you 
could have written, compiled, and tested a program that would show you the 
answer -- and you'd have learned a lot more from doing so than you will by 
reading the responses here. Having said that... here are the answers to your 
questions:

>Would SPACES pass the IS NUMERIC test used for checking if the
>value is numeric or not. 

No. Performing the IS NUMERIC test on a field that contains spaces will 
generate an exception.

>Since SPACES can be compared arithmetically

No, it can't.

>(> SPACES), 

That's a lexical comparison, *not* an arithmetic comparison. That simply tests 
to see whether a particular byte falls before, or after, space in the 
collating sequence.

>I was wondering if it would pass the IS NUMERIC test.

Of course not. SPACE is not a numeric digit. Numeric digits are 0 through 9.
```

##### ↳ ↳ Re: IS NUMERIC check for SPACES

- **From:** Richard <riplin@Azonic.co.nz>
- **Date:** 2009-12-01T23:01:40-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<603d52d3-a595-4e19-a954-154aba429fdd@c34g2000yqn.googlegroups.com>`
- **References:** `<ac1c02d1-64a3-400b-9c9a-63989d519a2b@f16g2000yqm.googlegroups.com> <hf4q6j$n1m$4@news.eternal-september.org>`

```
On Dec 2, 5:24 pm, spamb...@milmac.com (Doug Miller) wrote:
> In article <ac1c02d1-64a3-400b-9c9a-63989d519...@f16g2000yqm.googlegroups.com>, yogi <yogi...@gmail.com> wrote:
>
…[14 more quoted lines elided]…
> generate an exception.

The result of the test will be 'false'. 'Generating an exception'
would rather defeat to purpose of doing the test (which can be to
avoid an exception).

>
> >Since SPACES can be compared arithmetically
…[11 more quoted lines elided]…
> Of course not. SPACE is not a numeric digit. Numeric digits are 0 through 9.

Note, however, that the sign representation may lead to other
characters in the field, usually an 'overpunched' digit on the leading
or trailing character or a + or - if 'sign separate'.
```

###### ↳ ↳ ↳ Re: IS NUMERIC check for SPACES

- **From:** spambait@milmac.com (Doug Miller)
- **Date:** 2009-12-03T19:49:26+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<hf94oi$aql$1@news.eternal-september.org>`
- **References:** `<ac1c02d1-64a3-400b-9c9a-63989d519a2b@f16g2000yqm.googlegroups.com> <hf4q6j$n1m$4@news.eternal-september.org> <603d52d3-a595-4e19-a954-154aba429fdd@c34g2000yqn.googlegroups.com>`

```
In article <603d52d3-a595-4e19-a954-154aba429fdd@c34g2000yqn.googlegroups.com>, Richard <riplin@Azonic.co.nz> wrote:
>On Dec 2, 5:24=A0pm, spamb...@milmac.com (Doug Miller) wrote:
>> In article <ac1c02d1-64a3-400b-9c9a-63989d519...@f16g2000yqm.googlegroups=
…[24 more quoted lines elided]…
>avoid an exception).

You are of course correct. Serves me right for posting so late at night.
>
>>
…[19 more quoted lines elided]…
>
```

##### ↳ ↳ Re: IS NUMERIC check for SPACES

- **From:** docdwarf@panix.com ()
- **Date:** 2009-12-02T14:21:49+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<hf5t5t$og3$1@reader1.panix.com>`
- **References:** `<ac1c02d1-64a3-400b-9c9a-63989d519a2b@f16g2000yqm.googlegroups.com> <hf4q6j$n1m$4@news.eternal-september.org>`

```
In article <hf4q6j$n1m$4@news.eternal-september.org>,
Doug Miller <spambait@milmac.com> wrote:

[snip]

>Of course not. SPACE is not a numeric digit. Numeric digits are 0 through 9.

Ow... Mr Miller, it might be best to stay with the question of 'will 
(thing) pass an IS NUMERIC test?' and avoid the depths of what constitutes 
'numeric digits'.  The characters 0 through 9 are, as we all know, 
represted in DISPLAY format by the hexadecimal characters X'F0' through 
X'F9' (unless one is dealing with ASCII, in which case they are X'C0' 
through X'C9') or the binary equivalents 1111 0000 through 1111 1111 (or 
ASCII 1100 0000 through 1100 1001).

Now my memory is, admittedly, porous but I recall that IBM mainframe 
compilers (IKFCBL00 and IGYCRCTL) will successfully test COMP-3 (packed 
decimal format) fields with IS NUMERIC... and as a COMP-3 field, in my 
experience, often has its least significant nibble reserved for the 
field's sign (usually C for positive, D for negative) then a COMP-3 field 
containing X'123D' may pass an IS NUMERIC test while not, by your 
standard, containing an numeric digit.

Next week... Are Other Representational Systems Numeric or Not?  After 
All, This *is* the XXIth Century!

DD
```

###### ↳ ↳ ↳ Re: IS NUMERIC check for SPACES

- **From:** spambait@milmac.com (Doug Miller)
- **Date:** 2009-12-03T19:51:27+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<hf94sb$aql$2@news.eternal-september.org>`
- **References:** `<ac1c02d1-64a3-400b-9c9a-63989d519a2b@f16g2000yqm.googlegroups.com> <hf4q6j$n1m$4@news.eternal-september.org> <hf5t5t$og3$1@reader1.panix.com>`

```
In article <hf5t5t$og3$1@reader1.panix.com>, docdwarf@panix.com () wrote:
>Now my memory is, admittedly, porous but I recall that IBM mainframe 
>compilers (IKFCBL00 and IGYCRCTL) will successfully test COMP-3 (packed 
…[4 more quoted lines elided]…
>standard, containing an numeric digit.

1, 2, and 3 are numeric digits, no? The sign nybble is ignored.
```

###### ↳ ↳ ↳ Re: IS NUMERIC check for SPACES

_(reply depth: 4)_

- **From:** docdwarf@panix.com ()
- **Date:** 2009-12-03T20:16:43+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<hf96bb$q98$9@reader1.panix.com>`
- **References:** `<ac1c02d1-64a3-400b-9c9a-63989d519a2b@f16g2000yqm.googlegroups.com> <hf4q6j$n1m$4@news.eternal-september.org> <hf5t5t$og3$1@reader1.panix.com> <hf94sb$aql$2@news.eternal-september.org>`

```
In article <hf94sb$aql$2@news.eternal-september.org>,
Doug Miller <spambait@milmac.com> wrote:
>In article <hf5t5t$og3$1@reader1.panix.com>, docdwarf@panix.com () wrote:
>>Now my memory is, admittedly, porous but I recall that IBM mainframe 
…[7 more quoted lines elided]…
>1, 2, and 3 are numeric digits, no? The sign nybble is ignored.

If the sign is ignored then a COMP-3 field containing X'0000' would pass 
an IS NUMERIC test... and as I recall - porous memory and all - it 
doesn't.  COMP (binary) fields, no problem... but COMP-3 needs a valid 
sign.

Perhaps some testing is in order.

DD
```

###### ↳ ↳ ↳ Re: IS NUMERIC check for SPACES

_(reply depth: 5)_

- **From:** slade <jnjsle1@optonline.net>
- **Date:** 2009-12-11T19:47:58-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<2a82e1bc-8e40-4704-8206-c76ee94a5f0a@n13g2000vbe.googlegroups.com>`
- **References:** `<ac1c02d1-64a3-400b-9c9a-63989d519a2b@f16g2000yqm.googlegroups.com> <hf4q6j$n1m$4@news.eternal-september.org> <hf5t5t$og3$1@reader1.panix.com> <hf94sb$aql$2@news.eternal-september.org> <hf96bb$q98$9@reader1.panix.com>`

```
On Dec 3, 3:16 pm, docdw...@panix.com () wrote:
> In article <hf94sb$aq...@news.eternal-september.org>,
>
…[19 more quoted lines elided]…
> DD

In an IBM mainframe environment, depending on the NUMPROC/NUMCLS COBOL
compiler options selected, your sign choices are limited, at best, to
X'A" thru X'F'; at worst, to X'F'.  Any other nybble will result in a
"FALSE" return from IF NUMERIC.

So, as Doc said, the sign for numeric DISPLAY (and COMP-3) fields is
not ignored; X'F1F203' will generate a "FALSE" return.

If the item is defined w/SIGN IS SEPARATE (not an issue here,
apparently) there are other criteria.
```

###### ↳ ↳ ↳ Re: IS NUMERIC check for SPACES

_(reply depth: 6)_

- **From:** docdwarf@panix.com ()
- **Date:** 2009-12-12T16:00:21+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<hg0eml$6ak$2@reader1.panix.com>`
- **References:** `<ac1c02d1-64a3-400b-9c9a-63989d519a2b@f16g2000yqm.googlegroups.com> <hf94sb$aql$2@news.eternal-september.org> <hf96bb$q98$9@reader1.panix.com> <2a82e1bc-8e40-4704-8206-c76ee94a5f0a@n13g2000vbe.googlegroups.com>`

```
In article <2a82e1bc-8e40-4704-8206-c76ee94a5f0a@n13g2000vbe.googlegroups.com>,
slade  <jnjsle1@optonline.net> wrote:
>On Dec 3, 3:16?pm, docdw...@panix.com () wrote:
>> In article <hf94sb$aq...@news.eternal-september.org>,
…[26 more quoted lines elided]…
>not ignored; X'F1F203' will generate a "FALSE" return.

That's as I recall it, aye... but it was from Long Ago and perhaps things 
had changed.  Has anyone done any testing?  If so, might they post the 
code and results, so that experiment's reproducibility be verified?

DD
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
