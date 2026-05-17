[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Programming to the "compiler"

_2 messages · 1 participant · 1997-05_

**Topics:** [`Compilers and vendors`](../topics.md#compilers)

---

### Programming to the "compiler"

- **From:** "tea..." <ua-author-801459@usenetarchives.gap>
- **Date:** 1997-05-01T20:00:01+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<19970502225401.SAA07685@ladder01.news.aol.com>`

```

I hope that I'm not openning a "old" can of Worms here...But I've in the
past two months I've really learned alot, about how much I've forgotten
about COBOL. Now for two weeks I've been playing with two different
compilers. Fujitsu COBOL, and Micro Focus Personal COBOL.

Now I write a "program" using SPF/PC... I load it into Fujitsu, and it's
fine. I load it into MF and I get tons of errors.(this is a problem that
isn't important so don't email me on it). Anyway I finally get it loaded
in MF adn it runs "perfect", the same program in Fujitsu I have to tweak
to get to run the same.
example:

000600 WORKING-STORAGE SECTION.
000700
000800 01 THE-MESSAGE PIC X(20).
000900 01 THE-NAME PIC X(10).
001000 01 THE-NUMBER PIC 99.
001100
001200 PROCEDURE DIVISION.
001300
001400 PROGRAM-BEGIN.
001500 MOVE SPACES TO THE-NAME.
001600 DISPLAY "ENTER SOMEONE'S NAME.".
001700 ACCEPT THE-NAME.
001800 MOVE "HELLO" TO THE-MESSAGE.
001900 MOVE 1 TO THE-NUMBER.
002000 DISPLAY "MESSAGE ", THE-NUMBER, ": ", THE-MESSAGE, THE-NAME.
002100 MOVE "SAY GOODNIGHT, " TO THE-MESSAGE.
002200 MOVE 2 TO THE-NUMBER.
002300 DISPLAY "MESSAGE ", THE-NUMBER, ": ", THE-MESSAGE, THE-NAME.
002400
002500 PROGRAM-DONE.
002600 STOP RUN.

If you look at "the-name" in MF anytime you enter a name less than 10
characters long you're fine...But IN Fufitsu you have to add spaces to
your "input' for a total of 10 characters....I wonder what other compilers
"require' a full input?
Robert "Diverdown" Titus

He prayeth best, who loveth best all things both great and small; For the dear God who loveth us, He made and loveth all. "Rime of the Ancient Mariner"
```

#### ↳ Re: Programming to the "compiler"

- **From:** "tea..." <ua-author-801459@usenetarchives.gap>
- **Date:** 1997-05-03T20:00:02+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-dfaa8177af-p2@usenetarchives.gap>`
- **In-Reply-To:** `<19970502225401.SAA07685@ladder01.news.aol.com>`
- **References:** `<19970502225401.SAA07685@ladder01.news.aol.com>`

```

After dicussing this problem with a programmer who had some 20 years
experience...I went to the "manual" for Fujitsu Cobol...Clear back in
chapter 11(only 16 chapters in the manual) you can find that if you use
"ACCEPT varible FROM CONSOLE" then the program will work as expected.



Robert "Diverdown" Titus

He prayeth best, who loveth best all things both great and small; For the dear God who loveth us, He made and loveth all. "Rime of the Ancient Mariner"
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
