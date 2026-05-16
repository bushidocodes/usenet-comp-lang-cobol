[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Occurs Depending On question

_5 messages · 3 participants · 1999-02_

**Topics:** [`Language features and syntax`](../topics.md#syntax)

---

### Occurs Depending On question

- **From:** NoLonger@ix.netcom.com (OldUncleMe)
- **Date:** 1999-02-02T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<36b72251.2368648@news>`

```
Will either of these two ways of stating the pic clause for the depending field work?
the first is the way all the examples I can find work, but they usually have two or
more divisions of the 02 item 'some-repl' as subsequent 04 level items.  It seems
like when not needing to further subdivide the field, just make a table sized
dependent on occurence that method two would work.    Thanks,   TS

      *....................
       FD  some-file.
       01  some-rec.
           02 some-1                pic x(7).
           02 some-2                pic x(7).
           02 some-3                pic x(7).
           02 some-group        pic 99.
           02 some-repl           occurs 1 to 20 times
                                              depending on some-group.
              04 some-group-type    pic x(8).

      *....................alternate
       FD  some-file.
       01  some-rec.
           02 some-1                    pic x(7).
           02 some-2                    pic x(7).
           02 some-3                    pic x(7).
           02 some-group            pic 99.
           02 some-repl                pic x(8) occurs 1 to 20 times
                                                   depending on some-group.


"Come to think of it, there are already a million monkeys on a million
 typewriters, and Usenet is NOTHING like Shakespeare." Blair Houghton
***********entia non sunt multiplicanda praeter necessitate***********
++++++****tauceti****@****abraxis****.****com****for***email****++++++
```

#### ↳ Re: Occurs Depending On question

- **From:** "Judson McClendon" <judmc123@bellsouth.net>
- **Date:** 1999-02-02T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<WqGt2.2579$Xl5.3035284@news1.mia>`
- **References:** `<36b72251.2368648@news>`

```
Micro Focus COBOL 3.2 compiles both of them without a blip, except
that the last line in your second example extends past column 72
and 'some-group.' gets truncated.  I shifted it to the left a few
spaces and it compiled fine.
```

##### ↳ ↳ Re: Occurs Depending On question

- **From:** NoLonger@ix.netcom.com (OldUncleMe)
- **Date:** 1999-02-02T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<36b73f81.9841288@news>`
- **References:** `<36b72251.2368648@news> <WqGt2.2579$Xl5.3035284@news1.mia>`

```
On Tue, 02 Feb 1999 17:17:42 GMT ""Judson McClendon" <judmc123@bellsouth.net>" posted
to "comp.lang.cobol" about: "Re: Occurs Depending On question" :

-->Micro Focus COBOL 3.2 compiles both of them without a blip, except
-->that the last line in your second example extends past column 72
-->and 'some-group.' gets truncated.  I shifted it to the left a few
-->spaces and it compiled fine.
-->--
-->Judson McClendon      judmc123@bellsouth.net  (remove numbers)
-->Sun Valley Systems    http://personal.bhm.bellsouth.net/~judmc
-->"For God so loved the world that He gave His only begotten Son, that
-->whoever believes in Him should not perish but have everlasting life."
-->
-->OldUncleMe wrote:
-->>Will either of these two ways of stating the pic clause for the depending field
work?
-->>The first is the way all the examples I can find work, but they usually have two
or
-->>more divisions of the 02 item 'some-repl' as subsequent 04 level items.  It seems
-->>like when not needing to further subdivide the field, just make a table sized
-->>dependent on occurence that method two would work.    Thanks,   TS
-->>
-->>      *....................
-->>       FD  some-file.
-->>       01  some-rec.
-->>           02 some-1                pic x(7).
-->>           02 some-2                pic x(7).
-->>           02 some-3                pic x(7).
-->>           02 some-group        pic 99.
-->>           02 some-repl           occurs 1 to 20 times
-->>                                              depending on some-group.
-->>              04 some-group-type    pic x(8).
-->>
-->>      *....................alternate
-->>       FD  some-file.
-->>       01  some-rec.
-->>           02 some-1                    pic x(7).
-->>           02 some-2                    pic x(7).
-->>           02 some-3                    pic x(7).
-->>           02 some-group            pic 99.
-->>           02 some-repl                pic x(8) occurs 1 to 20 times
-->>                           depending on some-group.     <<<corrected

I shifted the line in my compulsive attempt at clarity in the example by lining up
with the other source...(In my text editor, it lines up ok before shifting, but the
difference in fonts, etc, between programs, and I shifted)

I do appreciate the answer though!  Having no more examples than of the first method,
I didn't even think to compile and test it, so especially thanks for the trouble.
(Think I'll try it too, with Fujitsu v.3, just for fun)      TS

PS:  do you keep a skeletal template for quick testing of code/w-s snatches and rapid
        startup of totally new programs?  Do people often write new from scratch or 
        is most work encountered maintenance, Y2K fixing, and addition of features to

        old programs?


"Come to think of it, there are already a million monkeys on a million
 typewriters, and Usenet is NOTHING like Shakespeare." Blair Houghton
***********entia non sunt multiplicanda praeter necessitate***********
++++++****tauceti****@****abraxis****.****com****for***email****++++++
```

###### ↳ ↳ ↳ Re: Occurs Depending On question

- **From:** "Judson McClendon" <judmc123@bellsouth.net>
- **Date:** 1999-02-02T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<4VHt2.2598$Xl5.3087594@news1.mia>`
- **References:** `<36b72251.2368648@news> <WqGt2.2579$Xl5.3035284@news1.mia> <36b73f81.9841288@news>`

```
OldUncleMe wrote:
>
>PS:  do you keep a skeletal template for quick testing of code/w-s
> snatches and rapid startup of totally new programs?

Yes.  I call it TESTBED.COB:

       IDENTIFICATION DIVISION.
       PROGRAM-ID.    TESTBED.
       ENVIRONMENT DIVISION.
       CONFIGURATION SECTION.
       INPUT-OUTPUT SECTION.
       FILE-CONTROL.
       I-O-CONTROL.
       DATA DIVISION.
       FILE SECTION.
       WORKING-STORAGE SECTION.
       PROCEDURE DIVISION.
       000000-CONTROL.
       000000-EXIT.
           STOP RUN.

>Do people often write new from scratch or is most work encountered
>maintenance, Y2K fixing, and addition of features to old programs?


Most definitely the latter.  But even in new development, which I do
most of the time, it is rare for someone to start out a new program
from scratch.  In practice COBOL programmers select a program which
is fairly close in structure to what they are about to write, then
modify it as necessary.  It is also good practice to reuse code a
lot, and good COBOL programmers write code in such a way that it is
easy to reuse and modify.
```

###### ↳ ↳ ↳ Re: Occurs Depending On question

- **From:** redsky@ibm.net (Thane Hubbell)
- **Date:** 1999-02-03T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<36b7d9ce.738180@news1.ibm.net>`
- **References:** `<36b72251.2368648@news> <WqGt2.2579$Xl5.3035284@news1.mia> <36b73f81.9841288@news>`

```
On Tue, 02 Feb 1999 18:30:37 GMT, NoLonger@ix.netcom.com (OldUncleMe)
wrote:


>PS:  do you keep a skeletal template for quick testing of code/w-s snatches and rapid
>        startup of totally new programs?  Do people often write new from scratch or 
>        is most work encountered maintenance, Y2K fixing, and addition of features to
>
>        old programs?

You might try the Template built into the Fujitsu Editor.  Choose EDIT
then TEMPLATE in the editor.  Play with it a bit.  It's very
interesting.
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
