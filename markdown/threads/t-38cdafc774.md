[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Macro assembler written in cobol

_11 messages · 6 participants · 2017-05 → 2017-06_

---

### Macro assembler written in cobol

- **From:** "surplus.parts.by.ron" <ua-author-14501820@usenetarchives.gap>
- **Date:** 2017-05-09T18:22:01+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<79996620-225d-48f3-b200-9ebeb0c29f73@googlegroups.com>`

```
Looking to see if there is a macro assembler written entirely in cobol someone would share. I am wanting to customize it for an old NCR computer. Thanks Ron.
```

#### ↳ Re: Macro assembler written in cobol

- **From:** "kerryliles" <ua-author-11668611@usenetarchives.gap>
- **Date:** 2017-05-10T11:22:02+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-38cdafc774-p2@usenetarchives.gap>`
- **In-Reply-To:** `<79996620-225d-48f3-b200-9ebeb0c29f73@googlegroups.com>`
- **References:** `<79996620-225d-48f3-b200-9ebeb0c29f73@googlegroups.com>`

```
On Tue May 09,2017 6:22 PM, sur··n@gm··l.com wrote:
› Looking to see if there is a macro assembler written entirely in cobol someone would share. I am wanting to customize it for an old NCR computer. Thanks Ron.
›

Unfortunately, I do not have any such thing - but I hope one turns up
because that would be extremely cool...

On the other hand, I have been wondering what choices are out there for
a *pre-processor* for COBOL (open source preferred; free is nice if not
open source). There are many occasions where I would love to use a
pre-processor to augment the COBOL source program ... anyone have any
recommendations? (the request for a macro assembler sparked my memory of
my request... I suspect the main problem in any implementation would be
the details of reading the COBOL source and outputing the 'tweaked'
source - that sort of thing is usually very implementation specific... :(
```

##### ↳ ↳ Re: Macro assembler written in cobol

- **From:** "bwtiffin" <ua-author-14501766@usenetarchives.gap>
- **Date:** 2017-05-11T03:07:03+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-38cdafc774-p3@usenetarchives.gap>`
- **In-Reply-To:** `<gap-38cdafc774-p2@usenetarchives.gap>`
- **References:** `<79996620-225d-48f3-b200-9ebeb0c29f73@googlegroups.com> <gap-38cdafc774-p2@usenetarchives.gap>`

```
On Wednesday, May 10, 2017 at 11:22:16 AM UTC-4, Kerry Liles wrote:

› On the other hand, I have been wondering what choices are out there for
› a *pre-processor* for COBOL (open source preferred; free is nice if not
› open source).

You might try COBOLMAC by Robert Mills. Handles a few keywords used by HP COBOL II/XL along with the core replacements. You'll likely need to run GnuCOBOL to get an executable, but after that, cobolmac will probably handle most COBOL sources you might want to throw at it.

https://open-cobol.sourceforge.io/faq/index.html#does-gnucobol-support-source-code-macros

Have good,
Brian
```

###### ↳ ↳ ↳ Re: Macro assembler written in cobol

- **From:** "kerryliles" <ua-author-11668611@usenetarchives.gap>
- **Date:** 2017-05-11T10:43:04+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-38cdafc774-p4@usenetarchives.gap>`
- **In-Reply-To:** `<gap-38cdafc774-p3@usenetarchives.gap>`
- **References:** `<79996620-225d-48f3-b200-9ebeb0c29f73@googlegroups.com> <gap-38cdafc774-p2@usenetarchives.gap> <gap-38cdafc774-p3@usenetarchives.gap>`

```
On Thu May 11,2017 3:07 AM, bwt··n@gm··l.com wrote:
› On Wednesday, May 10, 2017 at 11:22:16 AM UTC-4, Kerry Liles wrote:
› 
…[10 more quoted lines elided]…
› 

Thanks very much! I keep forgetting to poke around with GNUCobol (my
bad) and every time I revisit it I decide to look at it 'real soon now'

Kerry Liles
```

#### ↳ Re: Macro assembler written in cobol

- **From:** "robin.vowels" <ua-author-13497444@usenetarchives.gap>
- **Date:** 2017-05-13T08:53:05+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-38cdafc774-p5@usenetarchives.gap>`
- **In-Reply-To:** `<79996620-225d-48f3-b200-9ebeb0c29f73@googlegroups.com>`
- **References:** `<79996620-225d-48f3-b200-9ebeb0c29f73@googlegroups.com>`

```
On Wednesday, May 10, 2017 at 8:22:16 AM UTC+10, sur··.@gm··l.com wrote:
› Looking to see if there is a macro assembler written entirely in cobol
› someone would share. I am wanting to customize it for an old NCR computer.

Something like that is more likely to have been written in a language such as
PL/I that has been designed specifically for text processing.

If not in a HLL, it would have been written in the assembly language for the
machine in question.
```

#### ↳ Re: Macro assembler written in cobol

- **From:** "dashwood" <ua-author-14501808@usenetarchives.gap>
- **Date:** 2017-05-15T04:57:06+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-38cdafc774-p6@usenetarchives.gap>`
- **In-Reply-To:** `<79996620-225d-48f3-b200-9ebeb0c29f73@googlegroups.com>`
- **References:** `<79996620-225d-48f3-b200-9ebeb0c29f73@googlegroups.com>`

```
On 10/05/17 10:22 AM, sur··n@gm··l.com wrote:
› Looking to see if there is a macro assembler written entirely in cobol someone would share. I am wanting to customize it for an old NCR computer. Thanks Ron.
›
Is the machine a 315 or 500?

I used COBOL and NEAT on the 315 and machine code (before they produced
the SLIP assembler) for the 500, back in 1965. Later, they released
NEAT3 for the "new range" which replaced the beautiful old 315.

It would be very easy to write the NCR 500 machine code in COBOL (it
really just comes down to some serious templating, as it was a fixed
length 4-address instruction set) and would be fun to do.

Sorry, I don't have it to hand, and I don't have time at the moment for
what would be an interesting diversion, but I'll gladly help with
advice and review if you need it.

Pete.

I used to write COBOL; now I can do anything...
```

##### ↳ ↳ Re: Macro assembler written in cobol

- **From:** "surplus.parts.by.ron" <ua-author-14501820@usenetarchives.gap>
- **Date:** 2017-05-15T12:39:07+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-38cdafc774-p7@usenetarchives.gap>`
- **In-Reply-To:** `<gap-38cdafc774-p6@usenetarchives.gap>`
- **References:** `<79996620-225d-48f3-b200-9ebeb0c29f73@googlegroups.com> <gap-38cdafc774-p6@usenetarchives.gap>`

```
I want to create an basic assembler and simulator for the NCR century series. Make use of my packrat tapes of ncr century and ti 990 tapes. Ron. I also have COBOL 315 experience. Still have some 10K of old slab core cards and a few 7 track 315 tapes.
```

###### ↳ ↳ ↳ Re: Macro assembler written in cobol

- **From:** "dashwood" <ua-author-14501808@usenetarchives.gap>
- **Date:** 2017-05-20T09:11:08+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-38cdafc774-p8@usenetarchives.gap>`
- **In-Reply-To:** `<gap-38cdafc774-p7@usenetarchives.gap>`
- **References:** `<79996620-225d-48f3-b200-9ebeb0c29f73@googlegroups.com> <gap-38cdafc774-p6@usenetarchives.gap> <gap-38cdafc774-p7@usenetarchives.gap>`

```
On 16/05/17 4:39 AM, sur··n@gm··l.com wrote:
› I want to create an basic assembler and simulator for the NCR century series. Make use of my packrat tapes of ncr century and ti 990 tapes. Ron. I also have COBOL 315 experience. Still have some 10K of old slab core cards and a few 7 track 315 tapes.
›
Do you have a copy of the Century Assembler? (or are you planning to
write a JIT style Translator for it?) I'm not familiar with Century
series low-level code as I only ever saw NEAT3 being used on it, and I
was told at the time that NEAT3 (unlike the NEAT Autocode for 315) was a
"High level" language...

Pete.
I used to write COBOL; now I can do anything...
```

###### ↳ ↳ ↳ Re: Macro assembler written in cobol

_(reply depth: 4)_

- **From:** "surplus.parts.by.ron" <ua-author-14501820@usenetarchives.gap>
- **Date:** 2017-05-27T21:56:09+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-38cdafc774-p9@usenetarchives.gap>`
- **In-Reply-To:** `<gap-38cdafc774-p8@usenetarchives.gap>`
- **References:** `<79996620-225d-48f3-b200-9ebeb0c29f73@googlegroups.com> <gap-38cdafc774-p6@usenetarchives.gap> <gap-38cdafc774-p7@usenetarchives.gap> <gap-38cdafc774-p8@usenetarchives.gap>`

```
I hope to recover from 9 tracks an usable operationing system that includes neat/3, COBOL 68 & 74, RPG ii, and maybe some type of FORTRAN. Neat/3 assembler had 3 levels; high, medium and low or hardware level assembler. I am writing a basic hardware level assembler that I will post the source code. I only have 19 Opcode's to assemble and emulate. Tapes were captured about 1978 so i will see how reable the tapes are. I would like to locate a century 100 boot card for the 655 disk drive as it is just one binary card used to get the system loaded. Photo copy of the card would work. Ron
```

###### ↳ ↳ ↳ Re: Macro assembler written in cobol

_(reply depth: 5)_

- **From:** "docdwarf" <ua-author-6588713@usenetarchives.gap>
- **Date:** 2017-05-28T08:36:10+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-38cdafc774-p10@usenetarchives.gap>`
- **In-Reply-To:** `<gap-38cdafc774-p9@usenetarchives.gap>`
- **References:** `<79996620-225d-48f3-b200-9ebeb0c29f73@googlegroups.com> <gap-38cdafc774-p6@usenetarchives.gap> <gap-38cdafc774-p7@usenetarchives.gap> <gap-38cdafc774-p8@usenetarchives.gap> <gap-38cdafc774-p9@usenetarchives.gap>`

```
In article <27e6ea79-306b-41bc-8927-135··3@goo··s.com>,
wrote:
› I hope to recover from 9 tracks an usable operationing system that
› includes neat/3, COBOL 68 & 74, RPG ii, and maybe some type of FORTRAN. 
…[6 more quoted lines elided]…
› the card would work.  Ron

Do you live anywhere near a computer museum?

DD
```

###### ↳ ↳ ↳ Re: Macro assembler written in cobol

_(reply depth: 6)_

- **From:** "surplus.parts.by.ron" <ua-author-14501820@usenetarchives.gap>
- **Date:** 2017-06-29T02:12:11+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-38cdafc774-p11@usenetarchives.gap>`
- **In-Reply-To:** `<gap-38cdafc774-p10@usenetarchives.gap>`
- **References:** `<79996620-225d-48f3-b200-9ebeb0c29f73@googlegroups.com> <gap-38cdafc774-p6@usenetarchives.gap> <gap-38cdafc774-p7@usenetarchives.gap> <gap-38cdafc774-p8@usenetarchives.gap> <gap-38cdafc774-p9@usenetarchives.gap> <gap-38cdafc774-p10@usenetarchives.gap>`

```
I live in Dallas area. Have about half of an assembler written. Ron
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
