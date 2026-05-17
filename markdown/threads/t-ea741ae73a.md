[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Do someone know the reason for this error?

_6 messages · 4 participants · 1998-05_

---

### Do someone know the reason for this error?

- **From:** "irene jacobsen" <ua-author-17074419@usenetarchives.gap>
- **Date:** 1998-05-03T20:00:01+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<01bd776e$b7d88450$9a017a94@fou-lm-11103>`

```

Hey again.

I am thankful for having the possibility to ask you about my questions, and
getting good help.

This time i have a strange error-situation.

I produce a big file concisting of BIG records (about 2500 byte's each) and
transfer the result to a unix server.

When looking at the result it seems that places in the record get wrong
information.
After looking through my program not finding any errors, i started wander
about if some "buffers" or something like that was being destroyed because
of the big data it should contain....

I tried an experiment. Every time i wrote a record to my file, i replicated
the line, so that i would get two and two records similar ( i thought) if
everything was ok. My result was quite different;

The very first line is blank, giving the oportunity to have an header.
(that's ok)

The result is: 1 blank line, the first data-line, 1 blank line, the second
data-line, 1 blank line, the 3rd, blank, 4th, blank, 5th, blank, 6th, copy
of 1th data-line, ...... It looks as i get a copy/shift with 6 (or was it
8, but a constant number) difference.....

The program is produced in that way that when a line is written to the
file, the content of the line never get the same content later in the
program......

I am frustrated. What in H.... can produce such a problem....
- yes i know, it looks better if i dont have duplicated write-statements,
but this error must be a symptom for another error. I couldn't get this
result if everything was right in the beginning.....

With a hope of some strains of help:
Yours faithfully
Irene Jacobsen.
```

#### ↳ Re: Do someone know the reason for this error?

- **From:** "william m. klein" <ua-author-3041905@usenetarchives.gap>
- **Date:** 1998-05-03T20:00:02+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-ea741ae73a-p2@usenetarchives.gap>`
- **In-Reply-To:** `<01bd776e$b7d88450$9a017a94@fou-lm-11103>`
- **References:** `<01bd776e$b7d88450$9a017a94@fou-lm-11103>`

```

It is hard to know exactly what is happening, but I think we (in the
newsgroup) can help you better if you post the FD (and record definitions)
and the OPEN and WRITE statements that you are using. (Maybe also the
SELECT/ASSIGN if you have an "organization" specified.)

One thing I can say without seeing the code is that doing two writes to see
what is happening will NOT (necessarily) work unless you are doing WRITE
FROM statements. (In other words if you build your record in
Working-Storage, then it should work - if you build it in the FD, then it
MAY NOT.) This is because what happens to a record after a WRITE is
undefined and some compilers "mess it up" and some do not.

One other question for you to think about is whether the data in each record
MIGHT ever have a "CR/LF" (carriage return/line feed) in it. If the data
has this, then the symptom you are seeing when looking at your output might
make sense.

Again, post the relevant parts of your code and we may be able to give
better help.
```

#### ↳ Re: Do someone know the reason for this error?

- **From:** "chip ling" <ua-author-6589301@usenetarchives.gap>
- **Date:** 1998-05-04T14:03:03+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-ea741ae73a-p3@usenetarchives.gap>`
- **In-Reply-To:** `<01bd776e$b7d88450$9a017a94@fou-lm-11103>`
- **References:** `<01bd776e$b7d88450$9a017a94@fou-lm-11103>`

```

Irene Jacobsen wrote:
› 
› Hey again.
…[38 more quoted lines elided]…
› Irene Jacobsen.

The first step is to identify which part went wrong.

Since your work include two platforms. If I were you,
I will check the result at the same platform that creating
it. Make sure the error is not because of the transfer.

If your editor can read line over 2500 char per line use it.
If not write a simple program to read your output and display
the record.

Rgds,
Chip Ling
```

#### ↳ Re: Do someone know the reason for this error?

- **From:** "irene jacobsen" <ua-author-17074419@usenetarchives.gap>
- **Date:** 1998-05-04T20:00:04+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-ea741ae73a-p4@usenetarchives.gap>`
- **In-Reply-To:** `<01bd776e$b7d88450$9a017a94@fou-lm-11103>`
- **References:** `<01bd776e$b7d88450$9a017a94@fou-lm-11103>`

```

If it makes something any clearer:
I get the right content but it comes in wrong position in the record, and
the reason is not (at least not always) because i have put the content in
wrong place.....

Yours faithfully
Irene Jacobsen.
```

#### ↳ Re: Do someone know the reason for this error?

- **From:** "irene jacobsen" <ua-author-17074419@usenetarchives.gap>
- **Date:** 1998-05-04T20:00:05+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-ea741ae73a-p5@usenetarchives.gap>`
- **In-Reply-To:** `<01bd776e$b7d88450$9a017a94@fou-lm-11103>`
- **References:** `<01bd776e$b7d88450$9a017a94@fou-lm-11103>`

```

› This time i have a strange error-situation.
› 
…[37 more quoted lines elided]…
› Irene Jacobsen.

I am thankful for you trying to help me with the problem. I have read what
you say Chip Ling, and i will try to write the record out on my "sysout",
and display it, to see if i can se the problem also here. I do not think
the problem is "hidden cr's" or characters transfering wrong when changing
from ebcdic to ascii, the contents is to be only letters and numbers.
I found characters with hex:00, but after changing them to hex:40 with an
inspect statement i still get the same error. I have now stated that the
error occurs in my output-file before transfer to Unix....

I got a question about specifying better, and here you have what seem to me
you are wanting:

I am working on the MVS platform, using the version of cobol called cobol2.

My select statement:
SELECT TAB-A-FIL ASSIGN TO QPR001.

My file definition:
FD TAB-A-FIL
LABEL RECORD STANDARD
RECORDING MODE IS F
RECORD CONTAINS 2426 CHARACTERS
BLOCK CONTAINS 0 RECORDS.
01 TAB-A-POST PIC X(2426).

My open file statement:
OPEN OUTPUT TAB-A-FIL.
MOVE SPACES TO TAB-A-POST.
WRITE TAB-A-POST.

My (now) write to file statement: (the '.' is missing because this is taken
from within an IF statement魹ｽ) W-U-A-POST is where i build up the
output-record. This is therefore done in Working storage.
MOVE W-U-A-POST TO TAB-A-POST

WRITE TAB-A-POST

WRITE TAB-A-POST

This is from my JCL-file (i'm not good at jcl, i get someone else to write
the first, and then i do some changes according to changes in my file
definition魹ｽ)

This is where the program is run, does the region make any problem when
this program handles this big record, one in the file, and one in the
working storage?
//****************************************************************

//S020 EXEC PGM=&P,REGION=2048K

//****************************************************************


This is the definition of my file in the jcl. I am told to put in lrecl =
number of characters in the record, and make my computer calculate the
blksize. The cylinder try of specifying space was skipped, and i put in a
more specific definition. This didn't seem to make any difference in my
result.
//QPR001 DD DSN=&BIB.031P.SR007.S020.TABA,DISP=(NEW,CATLG),

// DCB=(RECFM=FB,LRECL=2426,BLKSIZE=7278),

// SPACE=(7278,(2000,200),RLSE)

//* SPACE=(CYL,(10),,,ROUND)



I also construct other files, just with smaller records, and they don't
give me any problem in the transfer....

Yours faithfully
Irene Jacobsen.
```

#### ↳ Re: Do someone know the reason for this error?

- **From:** "tt..." <ua-author-3333436@usenetarchives.gap>
- **Date:** 1998-05-05T15:27:06+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-ea741ae73a-p6@usenetarchives.gap>`
- **In-Reply-To:** `<01bd776e$b7d88450$9a017a94@fou-lm-11103>`
- **References:** `<01bd776e$b7d88450$9a017a94@fou-lm-11103>`

```

In article <01bd783c$8e341230$9a017a94@fou-lm-11103>#1/2,
"Irene Jacobsen" wrote:
› 
 
›› 
›› The result is: 1 blank line, the first data-line, 1 blank line, the
› second
›› data-line, 1 blank line, the 3rd, blank, 4th, blank, 5th, blank, 6th,
› copy
 
›            MOVE W-U-A-POST TO TAB-A-POST
› 
…[3 more quoted lines elided]…
› 
Irene,

I can't speak to your other problems (the content shift?), but your blank
lines are the result of having two write statements. When the second one
executes, the content of the FD record (TAB-A-POST) is undefined. You
might also consider using "WRITE TAB-A-POST FROM W-U-A-POST".

Tom

-----== Posted via Deja News, The Leader in Internet Discussion ==-----
http://www.dejanews.com/ Now offering spam-free web-based newsreading
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
