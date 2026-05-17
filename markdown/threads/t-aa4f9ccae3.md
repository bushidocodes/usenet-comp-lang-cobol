[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# A Word about all of the new GUI COBOL tools.

_13 messages · 7 participants · 1998-05_

---

### A Word about all of the new GUI COBOL tools.

- **From:** "thane hubbell" <ua-author-1728640@usenetarchives.gap>
- **Date:** 1998-05-11T20:00:01+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<35586BC0.5F75@ibm.net>`

```
This is very interesting. There are COBOL programming tools coming out
of the woodwork. Some are very good, others are not so hot. I just
wanted to editorialize about this for a minute.

I have seen some really stunning code generators, repositories, and
program creators. This is really neat stuff. I tried out several of
them. I have experience with the GUI tools provided by Micro Focus and
Fujitsu with their compilers. (Dialog with Micro Focus, Power COBOL
with Fujitsu). I played a little with Power COBOL, but worked heavily
with MF's Dialog system for years.

All of these systems have one thing in common. They are geared toward
new development. Any kind of conversion of an existing system with
these very nice tools is a MAJOR headache. I know, my Dialog task was
to convert a DOS based system to Windows. It was a total rewrite.
Event driven logic changes the picture, and it is why Object Orientation
seems so popular.

I think for new development these things are great. However, I think
there is a bigger need for CONVERSION of existing COBOL applications to
the new user interface. For that (and for my new development) I have
been using COBOL SP2 from Flexus. Their tool is the ONLY Gui tool I
have found that allows conversion with relative ease. In fact, it is
the ONLY one I have used that allowed me to keep my procedural source
code in tact and actually convert systems. I'm not an employee, I don't
get a cut, I just like the tool. In an hour last night - I was timing
myself - I wrote a program for my wife. She needed to capture some
archival data from a news group on the net. She wanted to cut and paste
the data, but using a word processor is a pain, and she wanted to do it
fairly fast. I wrote her a program where she could copy what she wanted
to the clipboard, then on a 4 button window, click PASTE and append a
text file, with a separator line between the messages. The other
buttons are EXIT, Settings and view. With settings she can change the
file name being saved, or change the separator line.

View shows her either what is waiting to be pasted or what has just been
pasted, so she can see if she did just paste that thing she copied or
not.

Works very well! Fairly simple application, but neat. Gui. Windows.

Anyway, I'm attaching the source. If you use SP2 or want to go to the
FLEXUS page (http://www.flexus.com) and try it, e-mail me and I'll send
you the panel file.

The program is Realia specific in the area of the "sequential" file
access. For MicroFocus or Fujitsu change the file access to RECORD
SEQUENTIAL and remove the [B] that gets stuck on the end of the file
name.

Also the linkage section should be removed, and the program name changed
to something different. What's here is what Realia needs to compile.

Anyway, I thought with all the advertising of these tools going on, I
would comment and show you some code. You can see how this stayed
procedural and that the COBOL is isolated from the interface. Flexus
will support virtually all the PC compilers, so go to their home page,
get the demo, and try it out. It works.
IDENTIFICATION DIVISION.
PROGRAM-ID. 'P_Winmain'.
* copyright 1998 - Thane Hubbell red··.@i··.net
* portions copyright Flexus International
* for other compilers change the program id, and remove the
* linkage section. This one is for Ca-Realia COBOL.
* TITLE - Capture
* DESCRIPTION - Capture

ENVIRONMENT DIVISION.
CONFIGURATION SECTION.
SOURCE-COMPUTER. IBM-PC.
OBJECT-COMPUTER. IBM-PC.
INPUT-OUTPUT SECTION.
FILE-CONTROL.
SELECT DATA-FILE ASSIGN TO VARYING THE-FILE-NAME
FILE STATUS IS DATA-STAT.
SELECT SETT-FILE ASSIGN TO "settings.fil"
FILE STATUS IS SETTINGS-STAT.
DATA DIVISION.
FILE SECTION.
FD DATA-FILE.
01 DATA-REC PIC X.
FD SETT-FILE.
01 SETTINGS-REC.
05 SETTINGS-NAME PIC X(8).
05 SETTINGS-SEP PIC X(80).
WORKING-STORAGE SECTION.

COPY "settings.cpy".
COPY "capture.cpy".
COPY "topaste.cpy".
COPY "sp2use.cpy".
01 ED-NUM PIC 9(5).
01 THE-FILE-NAME PIC X(15) VALUE SPACES.
01 CON-FLAG PIC X VALUE SPACES.
88 CON-EXIT VALUE "Y".
01 P-CON-FLAG PIC X VALUE SPACES.
88 P-CON-EXIT VALUE "Y".
01 S-CON-FLAG PIC X VALUE SPACES.
88 S-CON-EXIT VALUE "Y".
01 CNTR PIC 9(5) VALUE ZEROS.
01 CNTR1 PIC 9(5) VALUE ZEROS.
01 SETTINGS-STAT PIC XX.
01 DATA-STAT PIC XX.
01 LAST-PASTED PIC X(30000) VALUE SPACES.
LINKAGE SECTION.
01 INSTANCE PIC 9(4) BINARY.
01 PREV-INSTANCE PIC 9(4) BINARY.
01 CMD-LINE PIC X(120).
01 CMD-SHOW PIC 9(4) BINARY.

PROCEDURE DIVISION USING
BY CONTENT INSTANCE PREV-INSTANCE
BY REFERENCE CMD-LINE
BY CONTENT CMD-SHOW.

MAINLINE.
******************
* MAINLINE LOGIC *
******************
PERFORM PROC-OPEN-FILE.
MOVE LOW-VALUES TO capture-DATA.
MOVE "capture" TO capture-NEXT-PANEL.
MOVE "y" TO capture-NEW-WINDOW.
MOVE LOW-VALUES TO capture-COLRS.
MOVE LOW-VALUES TO capture-TYPES.
PERFORM PROC-CON-capture.
PERFORM PROC-CLOSE-WINDOW.
PERFORM PROC-CLOSE-FILE.
PERFORM PROC-END-SESSION.
STOP RUN.

PROC-OPEN-FILE.
*****************
* OPEN SP2 FILE *
*****************
MOVE LOW-VALUES TO SP2-FI-DATA.
MOVE "DARLENE.PAN" TO SP2-FI-NAME.
CALL "SP2" USING SP2-OPEN-FILE SP2-FILE-DEF.

PROC-CON-capture.
******************
* CONVERSE PANEL *
******************
PERFORM WITH TEST AFTER UNTIL CON-EXIT
CALL "SP2" USING SP2-CONVERSE-PANEL capture-CONVERSE-DATA
MOVE LOW-VALUE TO capture-NEW-WINDOW
EVALUATE TRUE
WHEN CAPTURE-PASTE-PB-HIT
PERFORM PASTE-APPEND
WHEN CAPTURE-VIEW-PB-HIT
PERFORM VIEW-WINDOW
WHEN CAPTURE-SETTINGS-PB-HIT
PERFORM SETTINGS-WINDOW
WHEN CAPTURE-EXIT-PB-HIT
SET CON-EXIT TO TRUE
WHEN CAPTURE-KEY = SP2-KEY-CLOSE
SET CON-EXIT TO TRUE
END-EVALUATE
END-PERFORM
.
PROC-CON-TOPASTE.
******************
* CONVERSE PANEL *
******************
MOVE SPACE TO P-CON-FLAG
MOVE SPACES TO TOPASTE-THE-TEXT
PERFORM WITH TEST AFTER UNTIL P-CON-EXIT
CALL "SP2" USING SP2-CONVERSE-PANEL TOPASTE-CONVERSE-DATA
MOVE LOW-VALUE TO TOPASTE-NEW-WINDOW
EVALUATE TRUE
WHEN TOPASTE-LAST-PB-HIT
PERFORM SHOW-LAST
WHEN TOPASTE-WAITING-PB-HIT
PERFORM SHOW-WAITING
WHEN OTHER
SET P-CON-EXIT TO TRUE
END-EVALUATE
END-PERFORM
.
SHOW-LAST.
MOVE LAST-PASTED TO TOPASTE-THE-TEXT.
SHOW-WAITING.
COMPUTE SP2-CB-VAR-LEN = 0 + 30000
COMPUTE SP2-CB-TEXT-LEN = 0 + 30000
CALL "SP2" USING SP2-GET-CLIPBOARD SP2-CLIPBOARD-DATA
MOVE SPACES TO TOPASTE-THE-TEXT
MOVE SP2-CB-TEXT (1:SP2-CB-TEXT-LEN) TO
TOPASTE-THE-TEXT
.
PROC-CON-SETTINGS.
******************
* CONVERSE PANEL *
******************
MOVE SPACE TO S-CON-FLAG
PERFORM GET-SETTINGS-1
* this seems funky, but I might add more buttons later.
PERFORM WITH TEST AFTER UNTIL S-CON-EXIT
CALL "SP2" USING SP2-CONVERSE-PANEL SETTINGS-CONVERSE-DATA
MOVE LOW-VALUE TO SETTINGS-NEW-WINDOW
PERFORM UPDATE-SETTINGS
SET S-CON-EXIT TO TRUE
END-PERFORM
.
UPDATE-SETTINGS.
OPEN OUTPUT SETT-FILE
MOVE SETTINGS-FILE TO SETTINGS-NAME
MOVE SETTINGS-SEPARATOR TO SETTINGS-SEP
WRITE SETTINGS-REC
CLOSE SETT-FILE
.
GET-SETTINGS.
OPEN INPUT SETT-FILE
IF SETTINGS-STAT NOT = "00"
CLOSE SETT-FILE
OPEN OUTPUT SETT-FILE
MOVE "SAMPLE" TO SETTINGS-NAME
MOVE "----------------------------------------"
TO SETTINGS-SEP
WRITE SETTINGS-REC
CLOSE SETT-FILE
PERFORM SETTINGS-WINDOW
OPEN INPUT SETT-FILE
END-IF
READ SETT-FILE
CLOSE SETT-FILE
MOVE SPACES TO THE-FILE-NAME
STRING SETTINGS-NAME DELIMITED BY SPACE
".TXT[B]" DELIMITED BY SIZE
INTO THE-FILE-NAME
.
GET-SETTINGS-1.
OPEN INPUT SETT-FILE
IF SETTINGS-STAT NOT = "00"
CLOSE SETT-FILE
OPEN OUTPUT SETT-FILE
MOVE "SAMPLE" TO SETTINGS-NAME
MOVE "----------------------------------------"
TO SETTINGS-SEP
WRITE SETTINGS-REC
CLOSE SETT-FILE
OPEN INPUT SETT-FILE
END-IF
READ SETT-FILE
MOVE SETTINGS-NAME TO SETTINGS-FILE
MOVE SETTINGS-SEP TO SETTINGS-SEPARATOR
CLOSE SETT-FILE
.
SETTINGS-WINDOW.
MOVE LOW-VALUES TO SETTINGS-DATA
MOVE "settings" TO SETTINGS-NEXT-PANEL
MOVE "y" TO SETTINGS-NEW-WINDOW
MOVE LOW-VALUES TO SETTINGS-COLRS
MOVE LOW-VALUES TO SETTINGS-TYPES
PERFORM PROC-CON-SETTINGS
PERFORM PROC-CLOSE-WINDOW
.
VIEW-WINDOW.
MOVE LOW-VALUES TO TOPASTE-DATA
MOVE "topaste" TO TOPASTE-NEXT-PANEL
MOVE "y" TO TOPASTE-NEW-WINDOW
MOVE LOW-VALUES TO TOPASTE-COLRS
MOVE LOW-VALUES TO TOPASTE-TYPES
PERFORM PROC-CON-TOPASTE
PERFORM PROC-CLOSE-WINDOW
.

PROC-CLOSE-WINDOW.
************************
* CLOSE CURRENT WINDOW *
************************
CALL "SP2" USING SP2-CLOSE-WINDOW SP2-NULL-PARM.

PROC-CLOSE-FILE.
**********************
* CLOSE CURRENT FILE *
**********************
CALL "SP2" USING SP2-CLOSE-FILE SP2-NULL-PARM.

PROC-END-SESSION.
*******************
* END SP2 SESSION *
*******************
CALL "SP2" USING SP2-END-SESSION SP2-NULL-PARM.
PASTE-APPEND.
PERFORM GET-SETTINGS
OPEN EXTEND DATA-FILE
IF DATA-STAT NOT = "00"
CLOSE DATA-FILE
OPEN OUTPUT DATA-FILE
END-IF
COMPUTE SP2-CB-VAR-LEN = 0 + 30000
COMPUTE SP2-CB-TEXT-LEN = 0 + 30000
CALL "SP2" USING SP2-GET-CLIPBOARD SP2-CLIPBOARD-DATA
PERFORM VARYING CNTR FROM 1 BY 1 UNTIL CNTR >
SP2-CB-TEXT-LEN
WRITE DATA-REC FROM SP2-CB-TEXT (CNTR:1)
END-PERFORM
MOVE SP2-CB-TEXT-LEN TO ED-NUM
MOVE X"0D" TO DATA-REC
WRITE DATA-REC
MOVE X"0A" TO DATA-REC
WRITE DATA-REC
PERFORM WITH TEST AFTER VARYING CNTR FROM 80 BY -1
UNTIL CNTR = 1 OR SETTINGS-SEP (CNTR:1) > SPACE
END-PERFORM
PERFORM VARYING CNTR1 FROM 1 BY 1 UNTIL CNTR1 > CNTR
WRITE DATA-REC FROM SETTINGS-SEP (CNTR1:1)
END-PERFORM
MOVE SPACES TO LAST-PASTED
MOVE SP2-CB-TEXT (1:SP2-CB-TEXT-LEN) TO LAST-PASTED
(1:SP2-CB-TEXT-LEN)
MOVE X"0D" TO DATA-REC
WRITE DATA-REC
MOVE X"0A" TO DATA-REC
WRITE DATA-REC
CLOSE DATA-FILE

MOVE LOW-VALUES TO SP2-MS-DATA
MOVE "i" TO SP2-MS-ICON
MOVE "Data Pasted!" TO SP2-MS-TITLE
STRING "Data has been pasted!"
DELIMITED BY SIZE INTO SP2-MS-TEXT
MOVE "o" TO SP2-MS-BUTTON
MOVE "n" TO SP2-MS-CANCEL
MOVE 1 TO SP2-MS-LINE-CNT
CALL "SP2" USING SP2-DISPLAY-MESSAGE SP2-MESSAGE-DATA
```

#### ↳ Re: A Word about all of the new GUI COBOL tools.

- **From:** "mike rochford" <ua-author-959623@usenetarchives.gap>
- **Date:** 1998-05-12T20:00:02+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-aa4f9ccae3-p2@usenetarchives.gap>`
- **In-Reply-To:** `<35586BC0.5F75@ibm.net>`
- **References:** `<35586BC0.5F75@ibm.net>`

```


Thane Hubbell wrote in message <355··.@i··.net>...
› This is very interesting. There are COBOL programming tools coming out
› of the woodwork. Some are very good, others are not so hot. I just
› wanted to editorialize about this for a minute.
›

Great post Thane, I found it very interesting.

Have you seen AcuCobol-GT ???

I would be interested in your comments of it regarding putting a GUI
interface on-top of existing code.

Mike.
```

##### ↳ ↳ Re: A Word about all of the new GUI COBOL tools.

- **From:** "thane hubbell" <ua-author-1728640@usenetarchives.gap>
- **Date:** 1998-05-12T20:00:03+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-aa4f9ccae3-p3@usenetarchives.gap>`
- **In-Reply-To:** `<gap-aa4f9ccae3-p2@usenetarchives.gap>`
- **References:** `<35586BC0.5F75@ibm.net> <gap-aa4f9ccae3-p2@usenetarchives.gap>`

```

Mike Rochford wrote:
› 
› Thane Hubbell wrote in message <355··.@i··.net>...
…[11 more quoted lines elided]…
› 

That's the deal. I have not seen AccuCobol GT - but I did help someone
from this group work through some of it, so I have seen the code. It's
basically Accept and display statements. Their runtime takes care of
the rest. It's an interesting method. It seemed a bit stilted, and I
have some other problems with AccuCobol that have kept me away.
However, the SP2 stuff will work with AccuCobol and it will work well.

Now, the existing code issue. *If* you used screen sections, or a 3rd
party screen I/O interface, then the conversion to a GUI with SP2 is
EASY. The conversion from that interface to Micro Focus Dialog is very
difficult.
Dialog is like a separate programming system that exists outside your
cobol code completely, and communicates with your business logic via
calls. That's over simplified, but you get the idea. This makes
existing programs, where the user interface is an integral part, hard to
convert to Dialog.

Another method is the field by field accept display method. Sp2 can be
used to dynamically paint the screens on the fly. It can do the
accept/display type logic, but it takes some work. They are working on
a method to convert those type programs easily to SP2, and I look
forward to seeing it.

One other method I have seen, that I am helping a friend struggle
through, is the "home grown" screen solution. His application was
written with version 1.0 of Realia initially, when there was no fancy
screen functions at all. He wrote a series of ASM routines that he
calls. These can't function under windows and he is under extreme
market pressure to release a windows version of his product. ANY tool
will be a difficult transition for this type of application, and begs
the question of a "rewrite". In his case, it is probably warrented.

There are some things that don't convert well to the GUI, and in my
opinion, some applications just should NOT BE GUI. Alternately, there
are some things (drop down lists for example) that make the GUI very
good for users. Learning curve is generally less also!

Any other specific questions/observations. This is one subject I enjoy
discussing!
```

###### ↳ ↳ ↳ Re: A Word about all of the new GUI COBOL tools.

- **From:** "karl wagner" <ua-author-12514286@usenetarchives.gap>
- **Date:** 1998-05-13T10:27:04+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-aa4f9ccae3-p4@usenetarchives.gap>`
- **In-Reply-To:** `<gap-aa4f9ccae3-p3@usenetarchives.gap>`
- **References:** `<35586BC0.5F75@ibm.net> <gap-aa4f9ccae3-p2@usenetarchives.gap> <gap-aa4f9ccae3-p3@usenetarchives.gap>`

```

Thane Hubbell wrote:
› 
› <>
…[7 more quoted lines elided]…
› discussing!

A bit of blasphemy:

I am as big a proponent of COBOL as anyone, and while I have written
several GUI applications in COBOL, I am not convinced it is the right
tool for the job. It is not so much an issue of capability, although
there are limitations. Rather, it is the lack of supporting
documentation and examples geared to the COBOL programmer.

The Microsoft SDK documentation is written for C or C++ programmers as
is most of the literature available at the bookstore. What isn't
targeted at C programmers is for Java or Visual Basic. I've answered a
bunch of posts in this newsgroup from people trying to sort out how to
call functions in the Win32 API. It is an exercise of translating an
example written in C to COBOL. The translation step adds an unnecessary
layer of complexity to an already difficult task. It's probably easier
to learn another programming language.

I think that the PC COBOL compiler companies and other third party
vendors which provide tools for GUI development have decent products.
Heck, my company sells a product which, among other things, enables GUI
development in COBOL. However, feature for feature, they can't keep up
with the offerings for C, VB and Java. They will always be a step or two
behind Microsoft when things change. The debugging capabilities are not
always up to the task. If you look at the pricing of some of the
products, you would be better off buying VB professional and spending
the savings (roughly $3000 US) on training.

Any company considering writing a GUI application in COBOL should take a
long, hard look at the skills of their staff and of the future staff
they will hire to maintain it. For better or worse, schools are not
producing COBOL programmers. Guaranteed they are not producing COBOL GUI
programmers.

Finally, the Win32 API and the GUI model are evolving at an ever
increasing pace. Today we've got Win32, Windows 3.x, X/Windows and all
it's flavours, browser-based forms, the java virtual machine and other
GUI engines. The trend this week is toward browser-based applications. I
would be the first person to choose COBOL for a mission critical system
with an indefinite life expectancy. In a multi-tiered architecture,
COBOL is an obvious choice for the data access and business logic
layers. But for the user interface it's just too much effort for too
little payback.

Flame on!

Karl Wagner
```

###### ↳ ↳ ↳ Re: A Word about all of the new GUI COBOL tools.

_(reply depth: 4)_

- **From:** "thane hubbell" <ua-author-1728640@usenetarchives.gap>
- **Date:** 1998-05-12T20:00:05+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-aa4f9ccae3-p5@usenetarchives.gap>`
- **In-Reply-To:** `<gap-aa4f9ccae3-p4@usenetarchives.gap>`
- **References:** `<35586BC0.5F75@ibm.net> <gap-aa4f9ccae3-p2@usenetarchives.gap> <gap-aa4f9ccae3-p3@usenetarchives.gap> <gap-aa4f9ccae3-p4@usenetarchives.gap>`

```

Karl Wagner wrote:

› layers. But for the user interface it's just too much effort for too
› little payback.
›
› Flame on!

Not a chance -- When is the movie "Fantastic Four" going to be
released. I always liked torch...

Anyway back to the subject.

I agree, for many YEARS there was "no way to get there". You could NOT
have a GUI with COBOL, and that was bad. In reality, there were some
applications that STAYED TEXT MODE, because you could not get there
without the COBOL. Some things COBOL does well, Visual Basic doesn't
even come close.

Now there are some tools to allow both. With the one I like, SP2,
debugging is a breeze. The normal COBOL debugger works fine. This tool
is keeping up - allows the use of VBX objects etc. I think this is a
chance for a revival of COBOL.

Heck, I showed a program to someone and they wanted to know what it was
written it, it was fast, clean, nice and compact. When I told them
COBOL they nearly fell over.

Today, it's not that there are no good methods to get to GUI with COBOL,
it's that no one thinks of using COBOL as the first choice for their GUI
application.
```

###### ↳ ↳ ↳ Re: A Word about all of the new GUI COBOL tools.

_(reply depth: 4)_

- **From:** "david mowat" <ua-author-4670319@usenetarchives.gap>
- **Date:** 1998-05-13T20:00:06+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-aa4f9ccae3-p6@usenetarchives.gap>`
- **In-Reply-To:** `<gap-aa4f9ccae3-p4@usenetarchives.gap>`
- **References:** `<35586BC0.5F75@ibm.net> <gap-aa4f9ccae3-p2@usenetarchives.gap> <gap-aa4f9ccae3-p3@usenetarchives.gap> <gap-aa4f9ccae3-p4@usenetarchives.gap>`

```

For business applications use COBOL. If they want the windows look (or an
intranet) put an SP2 front end on it. Quite easy really. (Unless you have
another preference.)
```

###### ↳ ↳ ↳ Re: A Word about all of the new GUI COBOL tools.

_(reply depth: 4)_

- **From:** "john m. saxton, jr." <ua-author-789954@usenetarchives.gap>
- **Date:** 1998-05-14T20:00:07+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-aa4f9ccae3-p7@usenetarchives.gap>`
- **In-Reply-To:** `<gap-aa4f9ccae3-p4@usenetarchives.gap>`
- **References:** `<35586BC0.5F75@ibm.net> <gap-aa4f9ccae3-p2@usenetarchives.gap> <gap-aa4f9ccae3-p3@usenetarchives.gap> <gap-aa4f9ccae3-p4@usenetarchives.gap>`

```

I have to disaggree about using COBOL and A GUI. We did it for a huge system
AND we converted it from a text based interface to boot. We used SP2 from
Flexus So we converted an existing code base AND we added a new user
interface.

(Like Mr Hubbell, I DO NOT WORK FOR THIS COMPANY, I DON'T GET CUT EITHER.
I am an Independent Consultant, and I can't afford to recommend a tool that
will waste my time, or the client's. The tool delivers results and supports
mission critical systems. Period)

We didn't have to change any significant amount of code. Approx 10 programs
out of approx 1500 required some changes because they were, shall I say,
written in a creative way.

Karl Wagner wrote in message <355··.@sym··o.ca>...
› Thane Hubbell wrote:
›› 
…[55 more quoted lines elided]…
› Karl Wagner
```

###### ↳ ↳ ↳ Re: A Word about all of the new GUI COBOL tools.

- **From:** "s..." <ua-author-6589262@usenetarchives.gap>
- **Date:** 1998-05-14T11:56:08+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-aa4f9ccae3-p8@usenetarchives.gap>`
- **In-Reply-To:** `<gap-aa4f9ccae3-p3@usenetarchives.gap>`
- **References:** `<35586BC0.5F75@ibm.net> <gap-aa4f9ccae3-p2@usenetarchives.gap> <gap-aa4f9ccae3-p3@usenetarchives.gap>`

```

Thane Hubbell wrote:
› 
› Mike Rochford wrote:
…[10 more quoted lines elided]…
› 
Thane-

I've looked at both SP2 and AcuCobol-GT, and I had the reverse reaction
that you did. The SP2 seemed "stilted" to me while the AcuCobol-GT
approach struck me as completely a completely natural extension of the
fundamental elegance of the screen section as a way to handle operator
I-O. As a developer who has used screen section exclusively "forever,"
I guess I was put off with the idea of replacing the intuitive screen
section with all the CALLs that SP2 seems to require. I also liked the
idea of running a single program (from a single vendor) the Acu runtime
rather than running both the basic COBOL program (the Acu runtime or MF
native code) and the SP2 DLL simulatenously.

Although what I wrote probably doesn't read this way, I am not really
interested in debating this with, so this is a genuine, not rhetorical,
question. Can you tell me more about the virtues of SP2 vs Acu-GT?

Sal
```

#### ↳ Re: A Word about all of the new GUI COBOL tools.

- **From:** "david mowat" <ua-author-4670319@usenetarchives.gap>
- **Date:** 1998-05-12T20:00:09+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-aa4f9ccae3-p9@usenetarchives.gap>`
- **In-Reply-To:** `<35586BC0.5F75@ibm.net>`
- **References:** `<35586BC0.5F75@ibm.net>`

```

I can confirm what Thane has said about Flexus SP2 tools.
Converting procedural code (with text screens) to event driven (with windows
GUI) was quite straight forward.
A keystroke capture loop with an evaluate for each datafield on a form
calling the appropriate procedures gives total event flexibility.
Regards ...
David Mowat
DSMowat Computer Consulting
D&M Computer & Technology Services Ltd
dsm··.@cle··t.nz (remove cut)
If you want to start a Debt Collection Department or Agency, or go on the
Web, I have the Software.


Thane Hubbell wrote in message <355··.@i··.net>...
› This is very interesting.  There are COBOL programming tools coming out
› of the woodwork.  Some are very good, others are not so hot.  I just
…[15 more quoted lines elided]…
› 
SNIP
```

##### ↳ ↳ Re: A Word about all of the new GUI COBOL tools.

- **From:** "material fellow" <ua-author-501273@usenetarchives.gap>
- **Date:** 1998-05-12T20:00:10+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-aa4f9ccae3-p10@usenetarchives.gap>`
- **In-Reply-To:** `<gap-aa4f9ccae3-p9@usenetarchives.gap>`
- **References:** `<35586BC0.5F75@ibm.net> <gap-aa4f9ccae3-p9@usenetarchives.gap>`

```

David Mowat wrote:
› 
› I can confirm what Thane has said about Flexus SP2 tools.
…[6 more quoted lines elided]…
› 
Two years ago, I saw a demonstration of a fellow changing legacy Pascal
procedural code into Object Oriented Delphi (GUI).

The way he demoed it, it wasn't hard at all. Cut and paste and plopping
down visual controls and it was over real quick. Perhaps it helped that
the code was well documented to begin with and that he was able to
create a few objects readily from it and recycle them in the revised
application.

It also probably helped that he was really good at programming. Skill
always counts, he said.

I use stealth Java in my sig file.
It's there, but no one can detect it.
```

###### ↳ ↳ ↳ Re: A Word about all of the new GUI COBOL tools.

- **From:** "thane hubbell" <ua-author-1728640@usenetarchives.gap>
- **Date:** 1998-05-12T20:00:11+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-aa4f9ccae3-p11@usenetarchives.gap>`
- **In-Reply-To:** `<gap-aa4f9ccae3-p10@usenetarchives.gap>`
- **References:** `<35586BC0.5F75@ibm.net> <gap-aa4f9ccae3-p9@usenetarchives.gap> <gap-aa4f9ccae3-p10@usenetarchives.gap>`

```

Material Fellow wrote:
› 
› David Mowat wrote:
…[20 more quoted lines elided]…
› 

I think that is kind of my point. That's NEW development, not
CONVERSION. If you call a rewrite conversion, then maybe, but I don't.
I want to use as much of my old code as possible, disturbing NONE of the
critical logic. I've tried a lot of different tools, only one comes
close.
```

###### ↳ ↳ ↳ Re: A Word about all of the new GUI COBOL tools.

_(reply depth: 4)_

- **From:** "material fellow" <ua-author-501273@usenetarchives.gap>
- **Date:** 1998-05-12T20:00:12+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-aa4f9ccae3-p12@usenetarchives.gap>`
- **In-Reply-To:** `<gap-aa4f9ccae3-p11@usenetarchives.gap>`
- **References:** `<35586BC0.5F75@ibm.net> <gap-aa4f9ccae3-p9@usenetarchives.gap> <gap-aa4f9ccae3-p10@usenetarchives.gap> <gap-aa4f9ccae3-p11@usenetarchives.gap>`

```

Thane Hubbell wrote:
› 
› Material Fellow wrote:
…[28 more quoted lines elided]…
› close.

I understand what you say, and what you say isn't inconsistent with what
I claim happened in the demo described above.

Mostly, the input and output was strippable and replaceable with GUI
stuff, and mostly that isn't the critical logic anyway. Not to me,
anyway, but others may differ.

The guts of the working procedure were simply cut and pasted into a kind
of blank object, and the IDE did most of the work of rearranging it to
have the right wrapper stuff on the front end. Not much had to be
redone or rewritten, unless cut and paste constitutes your definition of
rewrite.

The original 100 lines of legacy Pascal were GUI-fied in under 20
minutes, including the time it took him to explain it, compile it (more
than once as real demo's don't go 100% correct) and execute it.

The core logic wasn't touched.

You may choose to have a different word for this conversion, but I would
have great difficulty accepting the term rewrite here, much as I refuse
to accept homework assignments for research as being "Cut and Paste"
from an enclycopedia counts as a "Rewrite".

However, if you want the term convert to mean "dump the source code from
Basic into this program and out pops Cobol" then that meaning of the
word convert doesn't apply. But, I prefer not to limit the term convert
to just that intrepretation.


I use stealth Java in my sig file.
It's there, but no one can detect it.
```

###### ↳ ↳ ↳ Re: A Word about all of the new GUI COBOL tools.

- **From:** "david mowat" <ua-author-4670319@usenetarchives.gap>
- **Date:** 1998-05-14T20:00:13+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-aa4f9ccae3-p13@usenetarchives.gap>`
- **In-Reply-To:** `<gap-aa4f9ccae3-p10@usenetarchives.gap>`
- **References:** `<35586BC0.5F75@ibm.net> <gap-aa4f9ccae3-p9@usenetarchives.gap> <gap-aa4f9ccae3-p10@usenetarchives.gap>`

```


Material Fellow wrote in message <355··.@pac··l.net>...
› David Mowat wrote:
›› 
›› I can confirm what Thane has said about Flexus SP2 tools.
 
›› SNIP
›› David Mowat
…[11 more quoted lines elided]…
› always counts, he said.


I have converted Pascal for Dos to Pascal for Windows using Borlands object
oriented methods - Parceling data record variables with "methods"
(procedures). Stubs and outlines were provided, & I like borland for
"developer friendliness" but I think SP2 is closer to field by field data
handling & no "object thinking" is really required. I live in a country of
three and a half million people, so I made a little database of 3.8million
clients on my PC. Search by code was instant and paging through records was
very quick. 3GL + GUI beats 4GL. But it is true what the material fellow
said, it is a good option for the reasonably experienced COBOL programmer
working with a reasonably well written application.
David Mowat.
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
