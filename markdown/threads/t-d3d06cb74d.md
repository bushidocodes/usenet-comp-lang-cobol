[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Display help!

_5 messages · 4 participants · 1996-07_

---

### Display help!

- **From:** "fswar..." <ua-author-17071290@usenetarchives.gap>
- **Date:** 1996-07-09T20:00:01+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1040134136-960709191200@hms.com>`

```

I have this program:

identification division.
program-id. disptest.
environment division.
data division.
working-storage section.
01 line1 pic x(60) value all "X".
01 line2.
03 filler pic x(60) value all "Y".

procedure division.
main-para.
display spaces with blank screen
display "1-" line1
display "2-" line2
display "3-" at line 3 column 1
display line1 at line 3 column 3
display "4-" at line 4 column 1
display line2 at line 4 column 3
stop run.

It clears the screen and then prints the following at the top of the
screen.

1-XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
2-YYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYY
3-XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
4-


My question is, why doesn't it print 60 Y's on the forth line of the
screen???

I'm just learning, so there may be a simple answer, but I don't get
it. I'm using MF Personal Cobol 2.0.2.

Thanks,
Frank

... No one can hear when you're Screaming in Digital!
___ Blue Wave/QWK v2.12
+-------------------------------------------------------------------------+
| Disclaimer: The views of this user are strictly his/her own and do not |
| necessarily reflect the views of the systems through which this message |
| passes. For problems: email (politely) to ro··.@h··.com. |
+-------------------------------------------------------------------------+
```

#### ↳ Re: Display help!

- **From:** "bert leest" <ua-author-14626649@usenetarchives.gap>
- **Date:** 1996-07-09T20:00:02+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-d3d06cb74d-p2@usenetarchives.gap>`
- **In-Reply-To:** `<1040134136-960709191200@hms.com>`
- **References:** `<1040134136-960709191200@hms.com>`

```

Frank Swarbrick wrote:
›
 
› My question is, why doesn't it print 60 Y's on the forth line of the
› screen???
›


The last DISPLAY statement is a so-called Format 3 (LINE/COLUMN)
statement.
The documentation (v3.1) states for the Format 3:

If identifier-1 is a group item and no MODE IS BLOCK phrase
exists, those elementary subordinate items which have names
other he FILLER are displayed. (etc)

When you write the last DISPLAY statement as follows:

display line2 at line 4 column 3 MODE IS BLOCK

then your little program works perfect ...

Cheers, and good luck with Cobol
```

#### ↳ Re: Display help!

- **From:** "bert leest" <ua-author-14626649@usenetarchives.gap>
- **Date:** 1996-07-09T20:00:03+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-d3d06cb74d-p3@usenetarchives.gap>`
- **In-Reply-To:** `<1040134136-960709191200@hms.com>`
- **References:** `<1040134136-960709191200@hms.com>`

```

Frank Swarbrick wrote:
›
 
› My question is, why doesn't it print 60 Y's on the forth line of the
› screen???
›


The last DISPLAY statement is a so-called Format 3 (LINE/COLUMN)
statement.
The documentation (v3.1) states for the Format 3:

If identifier-1 is a group item and no MODE IS BLOCK phrase
exists, those elementary subordinate items which have names
other he FILLER are displayed. (etc)

When you write the last DISPLAY statement as follows:

display line2 at line 4 column 3 MODE IS BLOCK

then your little program works perfect ...

Cheers, and good luck with Cobol
```

#### ↳ Re: Display help!

- **From:** "kevin digweed" <ua-author-6588872@usenetarchives.gap>
- **Date:** 1996-07-09T20:00:04+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-d3d06cb74d-p4@usenetarchives.gap>`
- **In-Reply-To:** `<1040134136-960709191200@hms.com>`
- **References:** `<1040134136-960709191200@hms.com>`

```

fsw··.@h··.com (Frank Swarbrick) wrote:
› I have this program:
› 
…[30 more quoted lines elided]…
› screen???

Hi Frank.

This is due to an historic feature of MF COBOL. Any FILLER (or unnamed in
ANSI 85) fields have only their size but NOT their contents considered
when they are used in full-screen ACCEPT or DISPLAY statements.

This was used to allow full-screen multi-field "form" ACCEPTs. For example:

01 screen-prompt.
03 prompt-01 pic x(17) value "Enter your name: ".
03 filler pic x(33).
03 prompt-02 pic x(16) value "Enter your age: ".
03 filler pic x(14).

01 screen-fields.
03 filler pic x(17).
03 thename pic x(33).
03 filler pic x(16).
03 theage pic 99.
03 filler pic x(12).

Now, using the following two statements, you can do a multi-field ACCEPT:

DISPLAY screen-prompt AT 0101
ACCEPT screen-fields AT 0101

During the accept, use the tab key to move from the name field to the age
field. Note that I`ve specified a line exactly 80 characters, so you could
display and accept a whole screen of information at once. Notice that the
ACCEPT doesn`t destroy the prompt text because of the filler fields.

These days, the SCREEN SECTION lets you do all this and more, but that old
way of working is still there for old programs that expect it. If you have
FORMS-2 (I`m not sure if you get it with Personal COBOL) then it expects
this behaviour, whereas the newer screen painting tool, SCREENS, outputs
source that uses the SCREEN SECTION.

Anyway, enough of the history lesson, the way to stop this from happening
is to add the MODE IS BLOCK phrase to your DISPLAY, ie:

display line-2 at line 4 column 3 mode is block

This is all documented under "Format 3" of the "DISPLAY statement" in your
Language Reference Manual.

Cheers, Kev.
```

#### ↳ Re: Display help!

- **From:** "jra..." <ua-author-1103086@usenetarchives.gap>
- **Date:** 1996-07-10T20:00:05+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-d3d06cb74d-p5@usenetarchives.gap>`
- **In-Reply-To:** `<1040134136-960709191200@hms.com>`
- **References:** `<1040134136-960709191200@hms.com>`

```

fsw··.@h··.com (Frank Swarbrick) wrote:

› I have this program:
 
›       identification division.
›       program-id. disptest.
…[5 more quoted lines elided]…
›           03  filler      pic x(60) value all "Y".
 
›       procedure division.
›       main-para.
…[7 more quoted lines elided]…
›           stop run.
 
› It clears the screen and then prints the following at the top of the
› screen.
 
› 1-XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
› 2-YYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYY
› 3-XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
› 4-
 
 
› My question is, why doesn't it print 60 Y's on the forth line of the
› screen???
 
› I'm just learning, so there may be a simple answer, but I don't get
› it.  I'm using MF Personal Cobol 2.0.2.
 
› Thanks,
›        Frank

Nothing obvious is wrong from the sample..
Try this
display "4-" at line 4 column 1
display line2 "+++" at line 4 column 3
and see where the +++ goes.

Luck

JR


and stir with a Runcible spoon...
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
