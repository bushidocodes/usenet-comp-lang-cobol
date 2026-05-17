[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# String question

_4 messages · 4 participants · 1996-12_

**Topics:** [`Language features and syntax`](../topics.md#syntax)

---

### String question

- **From:** "john olsen" <ua-author-832094@usenetarchives.gap>
- **Date:** 1996-12-08T19:00:01+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<01bbe57f$5f1c0620$90ec93cf@pole>`

```

I am completing my first intro course in COBOL. As a final assignment,
the
instructor gave us the following problem " Write a program using STRING
statements to read a sentence entered in English and convert it to Pig
Latin." Words beginning with consonants are converted into pig latin as
follows: toy is oytay, zoo is oozay and so on. Words beginning with
vowels
are converted as follows: aunt is auntay, act is actay.
Instructor is unavailable until last class and we are struggling with this
one as it is not is the text. I understand the STRING and UNSTRING
statements but not sure how to convert or read one char at a time. In
Pascal this would be easy.

Any help would be appreciated.

TIA

pls EMail.

John

"Another perfect day"
```

#### ↳ Re: String question

- **From:** "ggr..." <ua-author-1091801@usenetarchives.gap>
- **Date:** 1996-12-08T19:00:02+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-35b5da5ad4-p2@usenetarchives.gap>`
- **In-Reply-To:** `<01bbe57f$5f1c0620$90ec93cf@pole>`
- **References:** `<01bbe57f$5f1c0620$90ec93cf@pole>`

```

"JOHN OLSEN" wrote:

› are converted as follows: aunt is auntay, act is actay.
› Instructor is unavailable until last class and we are struggling with this
› one as it is not is the text.  I understand the STRING and UNSTRING
› statements but not sure how to convert or read one char at a time.  In
› Pascal this would be easy.

Why not make it as easy in COBOL as it is in Pascal?

01 WORDS.
05 THE-WORD pic x(20).
05 word-table redefines the-word occurs 20 times pic x.


MOVE 'AUNT' to THE-WORD.
DISPLAY WORD-TABLE (3).

What is shown is N.
You ought to be able to handle it from there.
```

##### ↳ ↳ Re: String question

- **From:** "guy k. haas" <ua-author-17086610@usenetarchives.gap>
- **Date:** 1996-12-08T19:00:03+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-35b5da5ad4-p3@usenetarchives.gap>`
- **In-Reply-To:** `<gap-35b5da5ad4-p2@usenetarchives.gap>`
- **References:** `<01bbe57f$5f1c0620$90ec93cf@pole> <gap-35b5da5ad4-p2@usenetarchives.gap>`

```

Glenn Grotzinger wrote:
› 
› "JOHN OLSEN"  wrote:
…[19 more quoted lines elided]…
› 

The assignment said to use the STRING statement. I would sort of assume
its intention was also to use the UNSTRING statement.

"Write a program using STRING statements to read a sentence entered in
English and convert it to Pig Latin."

Words beginning with consonants are converted into pig latin as
follows: toy is oytay, zoo is oozay and so on.

Words beginning with vowels are converted as follows: aunt is auntay,
act is actay.

1. You can use UNSTRING to parse text into words, breaking it
at spaces, commas, periods, colons, etc.

2. You can then use UNSTRING on each word, specifying all consonants
as the delimiters

...DELIMITED BY "B" OR "C" OR "D" OR "F" OR etc
INTO PRE-CON DELIMITER IN DEL1,
POST-CON

3. [I don't have the spec handy, but I THINK PRE-CON will be left alone
if
the word began with one of the delimiters ....]

If the PRE-CON is unchanged, then the word began with a consonant,
which is in DEL1, otherwise it began with a vowel.

Eventually, for consonant-beginners you can use STRING to gather up
POST-CON, DEL1, and "AY" into a single string.

[The rest is left to the students......]

Of course, you COULD use the tools Glenn and Arnold suggested for
disassembly,
then just use STRING to organize them... Who knows what the instructor
expected?

[The algorithm given is pretty simple pig-latinization. Is "BRING"
supposed
to become RINGBAY or INGBRAY?.....]

--g

Guy K. Haas, Software Exegete gh··.@net··e.com
Netscape Communications 415-937-3773
501 Middlefield My opinions are mine,
Mountain View, CA 94043 Netscape's are their own.
```

#### ↳ Re: String question

- **From:** "arnold trembley" <ua-author-6588869@usenetarchives.gap>
- **Date:** 1996-12-08T19:00:04+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-35b5da5ad4-p4@usenetarchives.gap>`
- **In-Reply-To:** `<01bbe57f$5f1c0620$90ec93cf@pole>`
- **References:** `<01bbe57f$5f1c0620$90ec93cf@pole>`

```

JOHN OLSEN wrote:
› 
›  I am completing my first intro course in COBOL.  As a final assignment,
…[21 more quoted lines elided]…
› "Another perfect day"

Whenever I want to manipulate a string in COBOL, I generally redefine the
field to something like this:

05 MY-STRING PIC X(16)
05 MY-STRING-TABLE REDEFINES MY-STRING.
10 MY-STRING-BYTE OCCURS 16 TIMES INDEXED BY I PIC X(01).

At this point you can do whatever you want with MY-STRING, because you can
look at each byte using either a subscript or an index. You can set up a
loop to count the number of leading character positions until you encounter a
SPACE character. If you are fortunate enough to have a compiler which
supports reference modification, you could easily add "AY" to the end of
string which begins with a vowel, perhaps like this:

MOVE 'AY' TO MY-STRING (CHAR-COUNT + 1:2).

If you know your string begins with a consonant, you could use reference
modification to copy the initial character to the first space at the end of
the string. I recommend copying the field to a new field as the easiest way
to strip off the initial consonant, but perhaps you can find a slicker way to
do that.

If you don't have a compiler that supports reference modification, it gets a
little harder, but is still possible to do. You just need to redefine your
string field so you can treat it as an array of characters.

If MY-STRING contains "AUNT ", just use a loop to count the characters
before an initial SPACE. CHAR-COUNT should be 4. Add 1 to CHAR-COUNT, and
move "A" to MY-STRING-BYTE (CHAR-COUNT). Add 1 again and move "Y" to
MY-STRING-BYTE (CHAR-COUNT). If you use indexing, set I to CHAR-COUNT, then
move "A" to MY-STRING-BYTE (I + 1), and then move "Y" to MY-STRING-BYTE
(I + 2).

Good luck!
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
