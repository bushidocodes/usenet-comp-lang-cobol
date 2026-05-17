[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Copybook

_10 messages · 8 participants · 1998-06_

---

### Copybook

- **From:** "roger wong" <ua-author-9710615@usenetarchives.gap>
- **Date:** 1998-06-06T20:00:01+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<6lbrnn$goe$1@lobster.vol.net>`

```

Dear all,

Can anyone answer me the use of 'copybook' method in COBOL programming.

Regards,
Roger
```

#### ↳ Re: Copybook

- **From:** "dave johnson" <ua-author-6589126@usenetarchives.gap>
- **Date:** 1998-06-05T20:00:02+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-99bbb7bada-p2@usenetarchives.gap>`
- **In-Reply-To:** `<6lbrnn$goe$1@lobster.vol.net>`
- **References:** `<6lbrnn$goe$1@lobster.vol.net>`

```


Roger Wong wrote in message <6lbrnn$goe$1.··.@lob··l.net>...
› Dear all,
› 
…[4 more quoted lines elided]…
› 


Is that the 'think first, program later' method?

DaveJ.
```

#### ↳ Re: Copybook

- **From:** "mark0..." <ua-author-750539@usenetarchives.gap>
- **Date:** 1998-06-05T20:00:03+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-99bbb7bada-p3@usenetarchives.gap>`
- **In-Reply-To:** `<6lbrnn$goe$1@lobster.vol.net>`
- **References:** `<6lbrnn$goe$1@lobster.vol.net>`

```

In article <6lbrnn$goe$1.··.@lob··l.net>, "Roger Wong"
writes:

› Can anyone answer me the use of 'copybook' method in COBOL
› programming.

A "copybook" is a reference to code in a copy library or disk file that would
be copied into the program via the COPY directive. Copybooks are frequently
used for record layouts and other data structures and sometimes for procedural
code that is used in many programs.

Copybooks can save a lot of time because when the record layout contains more
than a few fields it is too easy to make mistakes. Also, when the record layout
changes, it is possible to just recompile all the programs that copy in that
structure and then concentrate on additional changes in programs that use the
new, changed, or deleted fields. (Additional changes may be needed if the
record length changes.)

Mark A. Young
```

##### ↳ ↳ Re: Copybook

- **From:** "bill lynch" <ua-author-92065@usenetarchives.gap>
- **Date:** 1998-06-05T20:00:04+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-99bbb7bada-p4@usenetarchives.gap>`
- **In-Reply-To:** `<gap-99bbb7bada-p3@usenetarchives.gap>`
- **References:** `<6lbrnn$goe$1@lobster.vol.net> <gap-99bbb7bada-p3@usenetarchives.gap>`

```

Mark0Young wrote:
› 
› In article <6lbrnn$goe$1.··.@lob··l.net>, "Roger Wong" 
…[17 more quoted lines elided]…
› Mark A. Young

What Mark posted is true. My belief, and standard when I'm in a position
to set one, is that any data structure used by more than one program is
placed into a copy library and brought into your program with a COPY
statement. Sometimes it's a good idea to place the data structure in a
copy library even if only one program uses it - that program may need
multiple instances of the data structure and COPY it in with the
REPLACING option - but that's an advanced lesson.

Where are you in your COBOL training - the phrase "copybook method"
strikes me as odd. I don't think of using COPY code as a "method" of
programming, COBOL or otherwise. BTW, storing source in a copy library
and bringing it into one's program at compile time is not limited to
COBOL, even the primitive Assembler supports the COPY statement (and
others, too).

Bill Lynch

PS: If you're far enough along in your training to be writing code that
requires translation, e.g., CICS or SQL, do you see any problems with
copying in Procedure Division code with a COPY statement?
```

###### ↳ ↳ ↳ Re: Copybook

- **From:** "dave johnson" <ua-author-6589126@usenetarchives.gap>
- **Date:** 1998-06-07T20:00:05+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-99bbb7bada-p5@usenetarchives.gap>`
- **In-Reply-To:** `<gap-99bbb7bada-p4@usenetarchives.gap>`
- **References:** `<6lbrnn$goe$1@lobster.vol.net> <gap-99bbb7bada-p3@usenetarchives.gap> <gap-99bbb7bada-p4@usenetarchives.gap>`

```

Thane Hubbell wrote in message ...
› On Sat, 6 Jun 1998 20:17:49, Bill Lynch 
› wrote:
…[7 more quoted lines elided]…
› 
Tip - if you are having problems with a particular line in your program,
put a star in column 7 and the compiler will sort it out.
DaveJ.
```

###### ↳ ↳ ↳ Re: Copybook

- **From:** "bill lynch" <ua-author-92065@usenetarchives.gap>
- **Date:** 1998-06-07T20:00:06+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-99bbb7bada-p6@usenetarchives.gap>`
- **In-Reply-To:** `<gap-99bbb7bada-p4@usenetarchives.gap>`
- **References:** `<6lbrnn$goe$1@lobster.vol.net> <gap-99bbb7bada-p3@usenetarchives.gap> <gap-99bbb7bada-p4@usenetarchives.gap>`

```

Thane Hubbell wrote:
› 
› On Sat, 6 Jun 1998 20:17:49, Bill Lynch 
…[7 more quoted lines elided]…
› You are a funny guy.

Thanks (I think).

Bill Lynch
```

##### ↳ ↳ Re: Copybook

- **From:** "paul_k..." <ua-author-1388367@usenetarchives.gap>
- **Date:** 1998-06-07T20:00:07+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-99bbb7bada-p7@usenetarchives.gap>`
- **In-Reply-To:** `<gap-99bbb7bada-p3@usenetarchives.gap>`
- **References:** `<6lbrnn$goe$1@lobster.vol.net> <gap-99bbb7bada-p3@usenetarchives.gap>`

```

On 8 Jun 98 14:45:23 GMT, red··.@i··.net (Thane Hubbell) wrote:


› Agreed - change the copy book and just recompile all the programs that
› use it.
…[3 more quoted lines elided]…
› happens if you need to change one?  
 
› You answered this up above.
 
›                                                    Or add some code for just ONE of 
› the programs that uses the copy book.  They can be a nightmare.

If it's too much to code the routine so that the one program will run
the exception code, then just pull the out the code and put it
insteam. What's so difficult? I suppose it's a "nightmare" if you
don't test it enough. Seems to me like a much bigger nightmare if you
put the code insteam only to find you have to change dozens of
programs instead of just one copybook!
```

##### ↳ ↳ Re: Copybook

- **From:** "mixx..." <ua-author-17074640@usenetarchives.gap>
- **Date:** 1998-06-07T20:00:08+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-99bbb7bada-p8@usenetarchives.gap>`
- **In-Reply-To:** `<gap-99bbb7bada-p3@usenetarchives.gap>`
- **References:** `<6lbrnn$goe$1@lobster.vol.net> <gap-99bbb7bada-p3@usenetarchives.gap>`

```

On Mon, 8 Jun 1998 14:45:23, red··.@i··.net (Thane Hubbell) wrote:

› in the procedure division. ... They can be a nightmare

Ya noticed that, didja? (One of my greatest hairpullers in
MVRINV.COB!!)

=Dwight=
X1=L, X2=L & the domain is phonetic
```

#### ↳ Re: Copybook

- **From:** "docd..." <ua-author-514273@usenetarchives.gap>
- **Date:** 1998-06-06T20:00:09+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-99bbb7bada-p9@usenetarchives.gap>`
- **In-Reply-To:** `<6lbrnn$goe$1@lobster.vol.net>`
- **References:** `<6lbrnn$goe$1@lobster.vol.net>`

```

In article <6lbrnn$goe$1.··.@lob··l.net>, Roger Wong wrote:
› Dear all,
›
› Can anyone answer me the use of 'copybook' method in COBOL programming.

Please do your own homework.

DD
```

#### ↳ Re: Copybook

- **From:** "james walker" <ua-author-838022@usenetarchives.gap>
- **Date:** 1998-06-06T20:00:10+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-99bbb7bada-p10@usenetarchives.gap>`
- **In-Reply-To:** `<6lbrnn$goe$1@lobster.vol.net>`
- **References:** `<6lbrnn$goe$1@lobster.vol.net>`

```

sounds like class question

Roger Wong wrote in article
<6lbrnn$goe$1.··.@lob··l.net>...
› Dear all,
› 
…[6 more quoted lines elided]…
›
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
