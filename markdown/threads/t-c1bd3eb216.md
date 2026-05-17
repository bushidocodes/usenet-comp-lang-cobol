[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# SPAM RATIO

_9 messages · 4 participants · 1998-07 → 1998-08_

**Topics:** [`Meta: FAQs, group policy, charter`](../topics.md#meta)

---

### SPAM RATIO

- **From:** "donald tees" <ua-author-44233@usenetarchives.gap>
- **Date:** 1998-07-30T20:00:01+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<6pri47$qkv$1@news.igs.net>`

```
proportional fonts and Cobol do not mix well, but
here we are. Jeff, you get the lump of coal (note that
there were dozens and dozens worse but all had less
than 5 posts). And the winner is a Pimp!

NAME POSTS LINES QUOT. ORG BLANK SPAM

RATIO
Jeff Farkas 26 1647 915 503 229 30.54
"Darius Cooper 7 322 173 105 44 32.60
greg 7 468 262 153 53
32.69
ste··e@a··.d 6 333 169 114 50 34.23
Frank Swarbric 6 433 245 151 37 34.87
"Dennis J. Min 36 2120 1117 745 258 35.14
AS-DATA@t-onli 3 576 239 219 118 38.02
Bill Lynch 53 1897 871 763 263 40.22
"Dave Johnson 10 370 166 156 48 42.16
red··.@i··.net 42 1230 448 533 249 43.33
The Goobers 41 1657 633 744 280 44.90
nop06685@mail. 10 538 205 251 82 46.65
"Judson McClen 23 1298 521 616 161 47.45
"Peter Morris" 6 157 45 77 35
49.04
scm@enterprise 22 795 236 392 167 49.30
docdwarf@clark 33 1835 604 915 316 49.86
"Art Perry" 10 387 87 194 106
50.12
cob··t@a··.c 11 446 156 225 65 50.44
"COBOL Frog 10 375 81 198 96 52.80
gpsnav@pacific 8 198 23 105 70 53.03
rip··n@kc··s.g 13 429 136 231 62 53.84
"Rick Smith" 9 538 150 304 84
56.50
RandallBart 27 983 295 571 117 58.08
"Donald Tees" 58 1470 226 890 354 60.54
Knarf Sigruts 11 555 95 350 110 63.06
carloss940@aol 6 79 19 50 10 63.29
cadams@acucorp 6 254 46 165 43 64.96
Ibis redibis n 16 801 134 525 142
65.54
jcj··.@a··.co 9 194 18 129 47
66.49
mark0young@aol 17 760 91 514 155 67.63
"Wayne Womak" 6 306 13 220 73 71.89
kenrward@my-de 7 1958 131 1742 85 88.96
```

#### ↳ Re: SPAM RATIO

- **From:** "mixx..." <ua-author-185833@usenetarchives.gap>
- **Date:** 1998-07-30T20:00:02+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-c1bd3eb216-p2@usenetarchives.gap>`
- **In-Reply-To:** `<6pri47$qkv$1@news.igs.net>`
- **References:** `<6pri47$qkv$1@news.igs.net>`

```
On Fri, 31 Jul 1998 04:45:46, "Donald Tees"
wrote:

›     NAME          POSTS LINES QUOT. ORG BLANK  SPAM
›  
…[6 more quoted lines elided]…
›  kenrward@my-de    7  1958     131        1742         85        88.96

Dang, I didn't even make the cut!
Oh, well, I had already figured out Thane could out talk me!

=Dwight=
X1=L, X2=L & the domain is phonetic
```

#### ↳ Re: SPAM RATIO

- **From:** "donald tees" <ua-author-44233@usenetarchives.gap>
- **Date:** 1998-07-30T20:00:03+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-c1bd3eb216-p3@usenetarchives.gap>`
- **In-Reply-To:** `<6pri47$qkv$1@news.igs.net>`
- **References:** `<6pri47$qkv$1@news.igs.net>`

```
› Just before I run silent and in order to do justice to Jeff, I ought to
› point out that there is a flaw in the method.

Oh yes. More than one, in fact. I'll plead a very crude Version 1.0
that I wrote in four hours. First, I wrote an assembler routine that
took the Outlook database of messages and turned it into a flat
Ascii file. In effect, I simply removed everything that was not CR,LF,
or printable Ascii.

The result was scanned by a basic Cobol program, and built into an
Isam File with the name as the key. Totals were added to. Then I made
a second pass calculating the ratio's with the code shown. The ratios
were declared as an alternate key with duplicates. I then read the file
sequentially by that key, and printed.

Faults. It does not account for non quoted spam (fifteen line sigs, for
example). I think I should also not consider blank lines as spam ... they
are important to make text readable.

Then there are the quote characters. I eyeballed the input file
with a text editor, and checked for what people were using. It is
a four meg file, 75,000 lines. I coded for the ones I saw. The result
was a 275 line report, with the first fifty people posting under one
line per hundred that was a non-quote. Every one of them was
the poster of a single message. I fiddled about a bit, and settled
on a minimum of five posts. I figured those were the regulars. So all
the worst offenders have been omitted.

Last and most serious, the winners are all PURE spam. When you
post garbage by robot, then why would there be ANY quoting? You
will notice, for example, that Jensen is right at the bottom, as are
the agencies. Congrats, BTW, for being in the low end.

It is a start, though, and an interesting conversation piece. I think that
maybe a file of "names to ignore" is probably the next thing that should
be added. Then the pimps can be filtered out. Maybe, as well, a table
of quote characters, or possibly build that table dynamically whenever
the first character of the line is the same for a certain number of lines.

It might also be nice to put it out as an HTML file. Then I could fix the
columns up into looking nice.

Ideas? I can send anybody that wants to play the code. It is probably
a reasonable student exercise.
```

##### ↳ ↳ Re: SPAM RATIO

- **From:** "s..." <ua-author-3115375@usenetarchives.gap>
- **Date:** 1998-07-30T20:00:04+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-c1bd3eb216-p4@usenetarchives.gap>`
- **In-Reply-To:** `<gap-c1bd3eb216-p3@usenetarchives.gap>`
- **References:** `<6pri47$qkv$1@news.igs.net> <gap-c1bd3eb216-p3@usenetarchives.gap>`

```
In article <6psq7b$o7$1.··.@new··s.net>, don··.@wil··k.com says...
› Ideas? I can send anybody that wants to play the code. It is probably
› a reasonable student exercise.

monospaced font would be nice!

Also, how do you discount original text lines from huge sigs?

Shaun
```

###### ↳ ↳ ↳ Re: SPAM RATIO

- **From:** "donald tees" <ua-author-44233@usenetarchives.gap>
- **Date:** 1998-07-30T20:00:05+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-c1bd3eb216-p5@usenetarchives.gap>`
- **In-Reply-To:** `<gap-c1bd3eb216-p4@usenetarchives.gap>`
- **References:** `<6pri47$qkv$1@news.igs.net> <gap-c1bd3eb216-p3@usenetarchives.gap> <gap-c1bd3eb216-p4@usenetarchives.gap>`

```
› monospaced font would be nice!

Well, the program simply writes out Ascii text. The font is selected
by the mail reader. About the only way that I can think of to do it
right would be to write out HTML, put it on a web page, and then
post a pointer to it. I was thinking that tabs might make it a bit more
presentable. Maybe I'll play with that for next month.

› Also, how do you discount original text lines from huge sigs?

I don't. Version 1.0 and all that. Plus the fact that I couldn't see
a way to do it, so it will be real easy to cheat.
```

###### ↳ ↳ ↳ Re: SPAM RATIO

_(reply depth: 4)_

- **From:** "s..." <ua-author-3115375@usenetarchives.gap>
- **Date:** 1998-08-02T20:00:06+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-c1bd3eb216-p6@usenetarchives.gap>`
- **In-Reply-To:** `<gap-c1bd3eb216-p5@usenetarchives.gap>`
- **References:** `<6pri47$qkv$1@news.igs.net> <gap-c1bd3eb216-p3@usenetarchives.gap> <gap-c1bd3eb216-p4@usenetarchives.gap> <gap-c1bd3eb216-p5@usenetarchives.gap>`

```
In article <6ptbca$gto$1.··.@new··s.net>, don··.@wil··k.com says...
› 
›› monospaced font would be nice!
› 
› Well, the program simply writes out Ascii text.  The font is selected
› by the mail reader.
 
› Ah! mail reader getting in the way.
 
› 
›› Also, how do you discount original text lines from huge sigs?
› 
› I don't.  Version 1.0 and all that.  Plus the fact that I couldn't see
› a way to do it, so it will be real easy to cheat.

A common method of delimiting sigs from body text is two minus symbols ie. --
then the sig following.

Shaun
```

#### ↳ Re: SPAM RATIO

- **From:** "donald tees" <ua-author-44233@usenetarchives.gap>
- **Date:** 1998-07-30T20:00:07+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-c1bd3eb216-p7@usenetarchives.gap>`
- **In-Reply-To:** `<6pri47$qkv$1@news.igs.net>`
- **References:** `<6pri47$qkv$1@news.igs.net>`

```
› Donald, what's the computation for the Spam ratio?

COMPUTE SPAM-RATIO = ORIGINAL-LINES / TOTAL-LINES * 100.

CHECK-OUT-POSTED-LINE.
ADD 1 TO TOTAL-LINES.
IF NEWS-LINE IS EQUAL TO SPACE
ADD 1 TO BLANK-LINES
ELSE
IF (FIRST-CHARACTER OF NEWS-LINE IS EQUAL TO ">"
OR
FIRST-CHARACTER OF NEWS-LINE IS EQUAL TO "%"
OR
FIRST-CHARACTER OF NEWS-LINE IS EQUAL TO "#"
OR
FIRST-CHARACTER OF NEWS-LINE IS EQUAL TO ":")
ADD 1 TO LINES-QUOTED
ELSE
ADD 1 TO ORIGINAL-LINES.
```

#### ↳ Re: SPAM RATIO

- **From:** "randallbart" <ua-author-464041@usenetarchives.gap>
- **Date:** 1998-07-31T20:00:08+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-c1bd3eb216-p8@usenetarchives.gap>`
- **In-Reply-To:** `<6pri47$qkv$1@news.igs.net>`
- **References:** `<6pri47$qkv$1@news.igs.net>`

```
Donald Tees wrote:

› RandallBart 27 983 295 571 117 58.08

I think I am getting short shrift from your methodology. I rarely post
something new here, I'm always resonding so I'm always quoting. I snip
long quotes, but as a general rule I want to avoid restating what I've
snipped. Given the choice between two lines of quoted material or one
line of new text to make up for the lost context, I prefer the former.

When a post contains a lot of quoting, I start by just readin the new
text. If that text piques my interest I may read what is quoted. I
read my news threaded, so frequently I just read the quoted material,
and don't need to read it again. I can quickly skip by it and read only
the new text.

At least I get the benefit of my long signature.

BTW, you're misusing the word "spam", though it may be spreading into
meanings like this.

I  |\   Randall Bart
L  |/   mailto:Bar··.@usa··m.net      mailto:Bar··.@att··m.net
o  |\   1-310-542-6013                       Please reply without spam
v  | \  MSMSMSMSMSMS 6/28/107                      Happy Trails To You
e    |\ Can you solve the BBA-CAB-DBB series?
Y    |/                 http://members.aol.com/PanicYr00/Sequence.html
o    |\ The Zeros Are Coming!         http://members.aol.com/PanicYr00
u    |/ The Zeros Are Coming!         http://members.aol.com/PanicYr00
```

##### ↳ ↳ Re: SPAM RATIO

- **From:** "donald tees" <ua-author-44233@usenetarchives.gap>
- **Date:** 1998-07-31T20:00:09+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-c1bd3eb216-p9@usenetarchives.gap>`
- **In-Reply-To:** `<gap-c1bd3eb216-p8@usenetarchives.gap>`
- **References:** `<6pri47$qkv$1@news.igs.net> <gap-c1bd3eb216-p8@usenetarchives.gap>`

```
› I think I am getting short shrift from your methodology.

If its any consolation, I felt the same thing and I wrote
the program. But then the computer is always right ...
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
