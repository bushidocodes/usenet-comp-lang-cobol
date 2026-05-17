[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Cobol or C/C++?

_9 messages · 7 participants · 1997-02 → 1997-03_

---

### Cobol or C/C++?

- **From:** "uni..." <ua-author-8448916@usenetarchives.gap>
- **Date:** 1997-02-23T19:00:01+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<5es7fu$br6@uwm.edu>`

```

Hello,

I have never studied the Cobol language before, only C and C++. But, I'm
curious to your opinion. Which do you think is easier to learn: Cobol or
C(or C++)?

Jackie


                        ‾*****************************‾
                        ‾ http://www.uwm.edu/‾unicorn ‾
                        ‾*****************************‾
```

#### ↳ Re: Cobol or C/C++?

- **From:** "del archer" <ua-author-6589011@usenetarchives.gap>
- **Date:** 1997-02-23T19:00:02+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-c1f1e3dd60-p2@usenetarchives.gap>`
- **In-Reply-To:** `<5es7fu$br6@uwm.edu>`
- **References:** `<5es7fu$br6@uwm.edu>`

```

Jacqueline Isnani Jacinto wrote:

› I have never studied the Cobol language before, only C and C++. But, I'm
› curious to your opinion. Which do you think is easier to learn: Cobol or
› C(or C++)?

If by "learn", you mean just learning the language syntax, I would say C is the
easiest because of its small set of reserved words. However, knowing the
syntax of a language doesn't mean you really _know_ the language and how to use
it.


Del.
```

##### ↳ ↳ Re: Cobol or C/C++?

- **From:** "jeremy rinderknecht" <ua-author-1876917@usenetarchives.gap>
- **Date:** 1997-02-24T19:00:03+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-c1f1e3dd60-p3@usenetarchives.gap>`
- **In-Reply-To:** `<gap-c1f1e3dd60-p2@usenetarchives.gap>`
- **References:** `<5es7fu$br6@uwm.edu> <gap-c1f1e3dd60-p2@usenetarchives.gap>`

```

There's more to it than just knowing syntax. I know syntax for both C
and COBOL. Which one is easier? COBOL. Why? Because COBOL, while it
has more reserved words, is hands down EASIER to understand. Why?
Because it's so english-like.

Example: If you want to read a record from a file, you would type:
Read [into ws-record name].

I dunno, i guess ultimately it's a matter of opinion. Mine just
happens to sway towards COBOL.

Jeremy
```

###### ↳ ↳ ↳ Re: Cobol or C/C++?

- **From:** "del archer" <ua-author-6589011@usenetarchives.gap>
- **Date:** 1997-02-26T19:00:04+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-c1f1e3dd60-p4@usenetarchives.gap>`
- **In-Reply-To:** `<gap-c1f1e3dd60-p3@usenetarchives.gap>`
- **References:** `<5es7fu$br6@uwm.edu> <gap-c1f1e3dd60-p2@usenetarchives.gap> <gap-c1f1e3dd60-p3@usenetarchives.gap>`

```

Jeremy Rinderknecht wrote:

› There's more to it than just knowing syntax. I know syntax for both C
› and COBOL...


Yes, there is more to PROGRAMMING (using the language) than knowing the syntax;
however, I think it is fair for one to claim that one has learnt the language once
one knows the syntax, and that was the question the original poster asked.


› Which one is easier? COBOL.  Why?  Because COBOL, while it
› has more reserved words, is hands down EASIER to understand.  Why?
…[3 more quoted lines elided]…
›                 Read  [into ws-record name].


I don't really understand the "english-like" argument. Personally, I don't find the
above easier to comprehend than:

fread(&record, sizeof(record), 1, file);

It may look more criptic to those unfamiliar with the language, but that is
irrelevant. If I program in C, I don't worry about those who don't know the
language.

You might argue that for a beginner the C version is more difficult to understand
initially. Well, to start, "fread" is not part of the C language, it is an
additional function. There is no keyword for reading from a file. Therefore,
beginners do not even need to consider how to read from a file until they have
learnt the language. Secondly, languages should not be designed for beginners, as
one is only a beginner for a short time. Languages should be designed to suit those
who will use them regularly.

Now, my intention is not too argue that C is better designed than COBOL. I'm am
simply refuting the "english-like" = "easy-to-understand" argument.


› I dunno, i guess ultimately it's a matter of opinion. Mine just
› happens to sway towards COBOL.


Agreed. A lot of it is opinion and what one considers to be the definition of
learning a language. For instance, you could argue that learning a language means
learning to use it effectively. For me this is too grey a definition. What does
effectively mean? How is it measured?


Del.
```

###### ↳ ↳ ↳ Re: Cobol or C/C++?

_(reply depth: 4)_

- **From:** "warren g. simmons" <ua-author-6589103@usenetarchives.gap>
- **Date:** 1997-02-27T19:00:05+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-c1f1e3dd60-p5@usenetarchives.gap>`
- **In-Reply-To:** `<gap-c1f1e3dd60-p4@usenetarchives.gap>`
- **References:** `<5es7fu$br6@uwm.edu> <gap-c1f1e3dd60-p2@usenetarchives.gap> <gap-c1f1e3dd60-p3@usenetarchives.gap> <gap-c1f1e3dd60-p4@usenetarchives.gap>`

```

History.....from my perspective


Univac I was programmed in machine language called C-10. Other early
computers
used binary. I'm sure there were other variations.

Result: long learning curve, and listings that made no sense.

Early managmenet did not have a clue as to the content or progress of the
efforts
which were very expensive.

Previous card systems could be eyeballed to a degree via card reading,
interpreting,
listings, etc.

HLL simplified both the ratio of code to instruction, but introduced
something management could review. Notice, I said "could."

COBOL being native to most of the early users and somewhat understandable
to managers was an improvement. Even the highly knowledgeable symbolic
coders understand what is written faster when reading English than when
reading something much less so. English is easier for more people, even in
other countries where English is a second language.

Opinion.....again from my perspective

I've just looked at the New IBM Visual Object COBOL samples available on
the net.
I believe that some C programmers will be very happy with the results. I
don't know what COBOL '9X' WILL contain when released, but I am of the
current opinion that some steps backwards may have been taken all in the
name of vendor competitiveness.

Warren Simmons
war··.@inf··d.com
```

###### ↳ ↳ ↳ Re: Cobol or C/C++?

_(reply depth: 4)_

- **From:** "del archer" <ua-author-6589011@usenetarchives.gap>
- **Date:** 1997-03-06T19:00:06+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-c1f1e3dd60-p6@usenetarchives.gap>`
- **In-Reply-To:** `<gap-c1f1e3dd60-p4@usenetarchives.gap>`
- **References:** `<5es7fu$br6@uwm.edu> <gap-c1f1e3dd60-p2@usenetarchives.gap> <gap-c1f1e3dd60-p3@usenetarchives.gap> <gap-c1f1e3dd60-p4@usenetarchives.gap>`

```

Enoch M. Jones wrote:
› 
› Del Archer wrote:
…[15 more quoted lines elided]…
› method, you can manipulate it)...


I do not wish to get into a feature comparison of programming languages, but I think I
should point out that "fread" DOES advance the file pointer automatically, although there
are other library functions to move it manually, if one so desires. The only time the
file pointer would not be advanced is when an i/o error occurs.


› ...Also, what you fail to realize is that
› you can READ  [INTO ws-record-longer-than-record-name].
› What happens in C/C++??  You simply read sizeof(record) chars into storage
› and leave the rest "undefined".  But, in Cobol you know that the workingstorage
› is "blank" or space values (Ascii 0x20 or Ebcdic 0x40).


Yes, this is a feature that I like in COBOL. However, I don't see how this relates to
the original question of which language is easier to learn. Perhaps you could expand on
this.


› The only reason C/C++ is being used is that most university's make this
› the "systems language" for beginning students.  The same is true of Cobol
› --it is the beginning language of most business applications programming
› students...


Well, I'm not sure that's the only reason. These languages must have some merit on their
own, or they would not have caught on or lasted so long. Pascal, for example, is often
used as a teaching language. Yet, it does not have the same level of use outside
universities that C++ and COBOL do.


› ...However, I am an ardent fan of PL/I which combines the best
› of both worlds and nothing beats good ole assembler. Only a wimp needs
› C/C++...


Perhaps... ;)


Del.
```

#### ↳ Re: Cobol or C/C++?

- **From:** "gregory paul amos" <ua-author-17071352@usenetarchives.gap>
- **Date:** 1997-02-24T19:00:07+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-c1f1e3dd60-p7@usenetarchives.gap>`
- **In-Reply-To:** `<5es7fu$br6@uwm.edu>`
- **References:** `<5es7fu$br6@uwm.edu>`

```

In article ,
Lee James wrote:

› 
› 
…[49 more quoted lines elided]…
› 
Visual Cobol will produce EXE's for Win95. It also has a great visual debug system during
animating, youcan have any number of data windows open while animating allowing a very fine
level of monitoring. As for graphics i'm not sure I haven't played with it very much.
Greg Amos
amo··.@ix.··m.com
› 
› Also in C++ you have the options at the top of the editor to compile and
…[12 more quoted lines elided]…
› CC5··.@ntu··c.uk
```

#### ↳ Re: Cobol or C/C++?

- **From:** "thane hubbell" <ua-author-1728640@usenetarchives.gap>
- **Date:** 1997-02-25T19:00:08+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-c1f1e3dd60-p8@usenetarchives.gap>`
- **In-Reply-To:** `<5es7fu$br6@uwm.edu>`
- **References:** `<5es7fu$br6@uwm.edu>`

```




› In those 3 years of COBOL I have never built a .EXE file.
›

The "Real" version of MF COBOL will build an EXE. It will be a LARGE one,
but it will build it. You have to remember that MicroFocus requires paying
a runtime royalty for every copy you distribute. At over $100.00 it kind
of eliminates MF COBOL as a development tool for $49.99 Windows Products.
```

#### ↳ Re: Cobol or C/C++?

- **From:** "inst..." <ua-author-4779510@usenetarchives.gap>
- **Date:** 1997-02-26T19:00:09+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-c1f1e3dd60-p9@usenetarchives.gap>`
- **In-Reply-To:** `<5es7fu$br6@uwm.edu>`
- **References:** `<5es7fu$br6@uwm.edu>`

```

uni··.@alp··m.edu (Jacqueline Isnani Jacinto) writes :

:Hello,

:I have never studied the Cobol language before, only C and C++. But, I'm

:curious to your opinion. Which do you think is easier to learn: Cobol or

:C(or C++)?

:Jackie


COBOL is fairly easy to learn - it was made that way. Many low level
language features like bit-shifting and pointers were intentionally left
out of the langauge. Labels can be 30 characters long so that they can be
meaningful ( fortran used 6 ) but this can be defeated by a determined
enough programmer. COBOL syntax is usually straight forward - C's is not.
In COBOL if I make a statement
IF A = B, it is easy enough to understand what is going on wereas in C
the same statement, if ( A = B) is a bug, not a comparison. Tables
(arrays) are simple to use and you'll never have to worry about seeing
constructs like array[3], 3[array], and *(array + 3) which are all
legal and do the same thing.

I like using C and C++, however, they can be too low-level and detail
oriented to be worth the trouble sometimes. COBOL has excellent file
handling abilities and does accurate decimal math which makes it
invaluable for processing business records. C does not inherently have
these characteristics.

Regards,
InstrJCC
Jim Castro
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
