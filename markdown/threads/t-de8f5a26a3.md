[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Procedure Division Question

_12 messages · 10 participants · 1998-02 → 1998-03_

---

### Procedure Division Question

- **From:** "mo..." <ua-author-4537810@usenetarchives.gap>
- **Date:** 1998-02-27T19:00:01+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<34f9071b.3112819@news.gate.net>`

```

Can you tell me if there is a command similar to display that writes
alphanumeric text from procedure division to a file or printer
automatically, without having to place it in working storage first.
I dont want to display it on screen, i want it to appear in output
file.
```

#### ↳ Re: Procedure Division Question

- **From:** "the goobers" <ua-author-1837635@usenetarchives.gap>
- **Date:** 1998-02-27T19:00:02+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-de8f5a26a3-p2@usenetarchives.gap>`
- **In-Reply-To:** `<34f9071b.3112819@news.gate.net>`
- **References:** `<34f9071b.3112819@news.gate.net>`

```

M.M. wrote:
› 
› Can you  tell me if there is a command similar to display that writes
…[3 more quoted lines elided]…
› file.

This one's for free: WRITE. Now, *please* attend to your own
assignments?

DD
```

##### ↳ ↳ Re: Procedure Division Question

- **From:** "william m. klein" <ua-author-3041905@usenetarchives.gap>
- **Date:** 1998-02-27T19:00:03+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-de8f5a26a3-p3@usenetarchives.gap>`
- **In-Reply-To:** `<gap-de8f5a26a3-p2@usenetarchives.gap>`
- **References:** `<34f9071b.3112819@news.gate.net> <gap-de8f5a26a3-p2@usenetarchives.gap>`

```

The Goobers wrote in message <34F··.@er··s.com>...
› M.M. wrote:
›› 
…[9 more quoted lines elided]…
› DD

Even easier, I think it sounds like
DISPLAY "literal"
or more pointedly
Display "Please, do your own homework"
```

#### ↳ Re: Procedure Division Question

- **From:** "rene..." <ua-author-6375353@usenetarchives.gap>
- **Date:** 1998-02-27T19:00:04+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-de8f5a26a3-p4@usenetarchives.gap>`
- **In-Reply-To:** `<34f9071b.3112819@news.gate.net>`
- **References:** `<34f9071b.3112819@news.gate.net>`

```

All of a sudden, mo··.@ga··e.net (M.M.) wrote:

› Can you  tell me if there is a command similar to display that writes
› alphanumeric text from procedure division to a file or printer
› automatically, without having to place it in working storage first.
› I dont want to display it on screen,  i want it to appear in output
› file.

More homework?

Check out WRITE FROM....

Dave


You may e-mail replies to: renegade at (@) dwx dot (.) com
```

#### ↳ Re: Procedure Division Question

- **From:** "stev..." <ua-author-17074205@usenetarchives.gap>
- **Date:** 1998-02-28T19:00:05+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-de8f5a26a3-p5@usenetarchives.gap>`
- **In-Reply-To:** `<34f9071b.3112819@news.gate.net>`
- **References:** `<34f9071b.3112819@news.gate.net>`

```

On Sat, 28 Feb 1998 12:52:27 GMT, mo··.@ga··e.net (M.M.) wrote:

› Can you  tell me if there is a command similar to display that writes
› alphanumeric text from procedure division to a file or printer
› automatically, without having to place it in working storage first.
› I dont want to display it on screen,  i want it to appear in output
› file.


Unless I'm mistaking, the DISPLAY command writes data to SYSLST. To
get it to appear on the console you have to say DISPLAY "text" UPON
CONSOLE.



////
(o o)
-oOO--(_)--OOo-

Here's Looking at ya!
Steve
```

##### ↳ ↳ Re: Procedure Division Question

- **From:** "john l. mindock" <ua-author-6588931@usenetarchives.gap>
- **Date:** 1998-03-03T19:00:06+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-de8f5a26a3-p6@usenetarchives.gap>`
- **In-Reply-To:** `<gap-de8f5a26a3-p5@usenetarchives.gap>`
- **References:** `<34f9071b.3112819@news.gate.net> <gap-de8f5a26a3-p5@usenetarchives.gap>`

```

Skippy PB wrote:
› 
› On Sat, 28 Feb 1998 12:52:27 GMT, mo··.@ga··e.net (M.M.) wrote:
…[6 more quoted lines elided]…
› 
I wonder if this question really is asking:
I have a CICS program and want to see some data that is 'inside' the
program. But not on the screen, I want to see it in a file or on a
printer. Thus I need a command similar to the batch 'DISPLAY'.

If this is the real question, there are CICS commands that send data to
files and printers (see Transient Data in the CICS manual).

(Not sure what the equivalent is on non-IBM mainframe COBOL stuff).
Just a guess after re-reading the question.

John
```

#### ↳ Re: Procedure Division Question

- **From:** "chip ling" <ua-author-6589301@usenetarchives.gap>
- **Date:** 1998-03-02T19:00:07+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-de8f5a26a3-p7@usenetarchives.gap>`
- **In-Reply-To:** `<34f9071b.3112819@news.gate.net>`
- **References:** `<34f9071b.3112819@news.gate.net>`

```

M.M. wrote:
› 
› Can you  tell me if there is a command similar to display that writes
…[3 more quoted lines elided]…
› file.

It's easy, follow the steps below
1. stop using DISPLAY statement within your COBOL program.
2. define your output file (refer to chapters on FILE-CONTROL and
FILE SECTION)
3. change all those display output to your output file.
(refer to chapters on SEQUENTIAL FILE PROCESSING).

Tell us the result when you have it done. Have fun!!!

Rgds,
Chip Ling
chi··.@sym··o.ca
(PS. More hints: FILE-CONTROL should under the heading of ENVIRONMENT
DIVISION, INPUT-OUTPUT SECTION. And FILE SECTION should under the
heading of DATA DIVISION.)
```

#### ↳ Re: Procedure Division Question

- **From:** "cobol frog (huib klink)" <ua-author-4414632@usenetarchives.gap>
- **Date:** 1998-03-02T19:00:08+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-de8f5a26a3-p8@usenetarchives.gap>`
- **In-Reply-To:** `<34f9071b.3112819@news.gate.net>`
- **References:** `<34f9071b.3112819@news.gate.net>`

```

M.M. (mister mystery?),

you want to know WITHOUT HAVING TO PLACE IT IN WS.
You probably want:
FD SOMEFILE.
01 SOMERECINSOMEFILE ...
and then
WRITE SOMERECINSOMEFILE FROM "HELLO WORLD"?

You can look this up in TFM. Read it.

(This is a more explaining translation of: "do your own homework".)

The Cobol Frog jumped.
```

#### ↳ Re: Procedure Division Question

- **From:** "randallbart" <ua-author-464041@usenetarchives.gap>
- **Date:** 1998-03-05T19:00:09+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-de8f5a26a3-p9@usenetarchives.gap>`
- **In-Reply-To:** `<34f9071b.3112819@news.gate.net>`
- **References:** `<34f9071b.3112819@news.gate.net>`

```

M.M. wrote:
› 
› Can you  tell me if there is a command similar to display that writes
…[3 more quoted lines elided]…
› file.

While programmers in C and Fortran and Basic cavalierly string bytes
onto the output file, in Cobol we declare an output record somewhere in
the DATA DIVISION, so that we know what our output looks like.

If you don't care enough about your data to declare its layout, why are
you bothering to write it?

Cobol -- The programming language for people who care about their data.

I  |\   Randall Bart                      mailto:Bar··.@usa··m.net
L  |/   
o  |\        Bar··.@wor··m.net  Bar··.@hot··m.com
v  | \  1-310-542-6013                       Please reply without spam
e    |\ 
Y    |/ Panic in the Year Zero Zero:  http://members.aol.com/PanicYr00
o    |\ The puzzle too hard for human beings:
u    |/                 http://members.aol.com/PanicYr00/Sequence.html
```

##### ↳ ↳ Re: Procedure Division Question

- **From:** "rene..." <ua-author-6375353@usenetarchives.gap>
- **Date:** 1998-03-07T19:00:10+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-de8f5a26a3-p10@usenetarchives.gap>`
- **In-Reply-To:** `<gap-de8f5a26a3-p9@usenetarchives.gap>`
- **References:** `<34f9071b.3112819@news.gate.net> <gap-de8f5a26a3-p9@usenetarchives.gap>`

```

All of a sudden, RandallBart wrote:

› M.M. wrote:
›› 
…[14 more quoted lines elided]…
›  
[Sniffle, sniff....]

Can't you just feel the LOVE in this room for our data.....

[humming "we are the world" softly]

Dave


You may e-mail replies to: renegade at (@) dwx dot (.) com
```

###### ↳ ↳ ↳ Re: Procedure Division Question

- **From:** "randallbart" <ua-author-464041@usenetarchives.gap>
- **Date:** 1998-03-07T19:00:11+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-de8f5a26a3-p11@usenetarchives.gap>`
- **In-Reply-To:** `<gap-de8f5a26a3-p10@usenetarchives.gap>`
- **References:** `<34f9071b.3112819@news.gate.net> <gap-de8f5a26a3-p9@usenetarchives.gap> <gap-de8f5a26a3-p10@usenetarchives.gap>`

```

Renegade wrote:
› 
› All of a sudden, RandallBart  wrote:
…[7 more quoted lines elided]…
› [humming "we are the world" softly]

Damn right! We Cobol programmers love our data. We would never subject
a field to the indignities of a haphazard %d. We love our data so much
we give each field its own line of code, just so it feels safe and
secure.

Show your data you really care: Give it COBOL!

I  |\   Randall Bart                      mailto:Bar··.@usa··m.net
L  |/   
o  |\        Bar··.@wor··m.net  Bar··.@hot··m.com
v  | \  1-310-542-6013                       Please reply without spam
e    |\ 
Y    |/ Panic in the Year Zero Zero:  http://members.aol.com/PanicYr00
o    |\ The puzzle too hard for human beings:
u    |/                 http://members.aol.com/PanicYr00/Sequence.html
```

##### ↳ ↳ Re: Procedure Division Question

- **From:** "pknu..." <ua-author-1468510@usenetarchives.gap>
- **Date:** 1998-03-08T19:00:12+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-de8f5a26a3-p12@usenetarchives.gap>`
- **In-Reply-To:** `<gap-de8f5a26a3-p9@usenetarchives.gap>`
- **References:** `<34f9071b.3112819@news.gate.net> <gap-de8f5a26a3-p9@usenetarchives.gap>`

```

On Fri, 06 Mar 1998 19:56:35 -0800, RandallBart
wrote:

› M.M. wrote:
›› 
…[9 more quoted lines elided]…
› 
That's because in the past we had no choice. Now that there's
reference modification you'll start to see a lot more stringing. Hell
I've already been (slightly) guilty.
---------------------------------------------------------------
Ever Notice....

....how quickly "pay later" comes when you "buy now"?
....the weaker the arguments, the stronger the words?
....the first piece of luggage out of the airport baggage chute never belongs to anybody?
....the shortest line becomes the slowest line once you choose it?
....the last key in the bunch usually opens the lock?
....the first person to get off a crowded eleveator is always standing in the back?
....immediately after you buy an item, you find a coupon for it?
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
