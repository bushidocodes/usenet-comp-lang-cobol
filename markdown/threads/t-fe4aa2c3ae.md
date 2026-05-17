[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Repost of help needed please

_11 messages · 8 participants · 1998-03_

---

### Repost of help needed please

- **From:** "sha..." <ua-author-17075329@usenetarchives.gap>
- **Date:** 1998-03-10T19:00:01+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<6e6u99$pnn@curly.cc.emory.edu>`

```

I'm not certain whether the first posting did in fact post if so forgive me if not
here it is.
I'm a student at Dekalb Tech and no this is not a please do my homework for me
post. Also I have asked the faculty for help and they either don't know or are
stumped. I'd just like to get the groups thoughts on something. As I said I'm a
student at Dekalb Tech with a programming major in my final quarter of cobol we
have a group project as the final assignment before CICS and we decided to do it
on a golf handicapping program. Two questions: first my part of it is the login
and encryption part. On the encryption part the username and password can each be
20 characters long, and I need to know is COBOL has a command that will return a
characters ascii value, to be later used in an encryption algorithm. Secondly,
and this is the part that stumped the faculty as well as everybody I've asked, my
login subprogram is saying basically that all of my variables are not declared,
but I disagree. I've checked spelling, periods, etc. and can not find what is
wrong. Below is the compiler listing for the program. Any and all help would be
appreciated. Thanks Benjamin Hazelwood.
Start of listing:
* Micro Focus COBOL for UNIX V3.2 revision 037 11-Mar-98 16:03 Page 1
* login.cbl
* Options: int(login.int) verbose nolist trace endp list(login.lst)
1 IDENTIFICATION DIVISION.
2
3****************************************************************
4* THIS PROGRAM IS THE SUBPROGRAM LOGIN.CBL IT ALLOWS THE USER *
5* TO LOGIN AND THEN RETURNS CONTROL TO THE MAIN PROGRAM IF THE *
6* USER FAILS TO CORRECTLY IDENTIFY AFTER THREE TRIES THEY ARE *
7* KICKED OUT AND IT ALSO STORES THE NUMBER OF INCORRECT TRIES *
8****************************************************************
9
10 PROGRAM-ID. LOGIN-SUBPROGRAM.
11 AUTHOR. GROUP-A.
12 DATE-WRITTEN. 02-08-98.
13 DATE-COMPILED.
14
15 ENVIRONMENT DIVISION.
16
17 CONFIGURATION SECTION.
18
19
20 SOURCE-COMPUTER. IBM-RISC-6000.
21 OBJECT-COMPUTER. IBM-RISC-6000.
22
23 SPECIAL-NAMES.
24 CURSOR IS CURSOR-POS.
25
26 INPUT-OUTPUT SECTION.
27
28 FILE-CONTROL.
29
30 SELECT PASS-DAT
31 ASSIGN TO 'pass.dat'
32 ORGANIZATION IS INDEXED
33 ACCESS MODE IS RANDOM
34 RECORD KEY IS PR-USERNAME.
35
36 DATA DIVISION.
37
38 FILE SECTION.
39 FD PASS-DAT.
40 01 PASS-RECORD.
41 05 PR-USERNAME PIC X(20).
42 05 FILLER PIC X(25).
43
44 WORKING-STORAGE SECTION.
45 COPY 'pass-rec.cbl'.
46
47 01 CONSTANTS.
48 05 CON-USER PIC X(9) VALUE
49 'INEEDHELP'.
50 05 CON-PASS PIC X(15) VALUE
51 'IREALLYNEEDHELP'.
52 05 MAX-TRIES PIC 9 VALUE 2.
53 05 LOGIN-LINE1 PIC X(23) VALUE
54 'GOLF HANDICAPING SYSTEM'.
55 05 LOGIN-LINE2 PIC X(12) VALUE
56 'LOGIN SCREEN'.
57 05 LOGIN-LINE3 PIC X(9) VALUE

* Micro Focus COBOL for UNIX V3.2 revision 037 11-Mar-98 16:03 Page 2
* login.cbl
58 'USERNAME:'.
59 05 LOGIN-LINE4 PIC X(9) VALUE
60 'PASSWORD:'.
61 05 INV-USER PIC X(31) VALUE
62 'YOU DO NOT EXIST ON THIS SYSTEM'.
63 05 INV-PASS PIC X(19) VALUE
64 'INVALID PASSWORD!!!'.
65 05 LOGIN-ERROR-MSG2 PIC X(8) VALUE
66 'YOU HAVE'.
67 05 LOGIN-ERROR-MSG2-2 PIC X(10) VALUE
68 'MORE TRIES'.
69
70 01 MISC.
71 05 QUIT PIC X.
72 88 USER-EXIT VALUE 'Y'.
73 05 NUM-TRIES PIC 9.
74 05 PASS-TRUE PIC X VALUE 'N'.
75 05 LOGIN-ERROR-LINE1 PIC X(31) VALUE SPACES.
76 05 LOGIN-ERROR-LINE2 PIC X(8) VALUE SPACES.
77 05 LOGIN-ERROR-LINE-TRIES PIC X VALUE SPACES.
78 05 LOGIN-ERROR-LINE2-2 PIC X(10) VALUE SPACES.
79 05 ERROR-TRIES PIC 9 VALUE ZERO.
80
81 01 LOGIN-PASSED-DATA.
82 05 LPD-USERNAME PIC X(20).
83 05 LPD-PASSWORD PIC X(20).
84 05 RETURNED-PASSWORD PIC X(20).
85 05 RETURNED-USERNAME PIC X(20).
86
87 LINKAGE SECTION.
88 01 PASSED-DATA.
89 05 PD-USER-NUM PIC 9(4).
90 05 PD-LEV-PRIV PIC 9.
91 05 PD-EXIT-TRUE PIC X.
92 05 PD-NUM-TRIES PIC 99.
93
94 SCREEN SECTION.
95 01 LOGIN-SCREEN.
96 05 BLANK SCREEN.
97 05 LINE 2 COLUMN 28 PIC X(23) FROM LOGIN-LINE1.
98 05 LINE 4 COLUMN 34 PIC X(12) FROM LOGIN-LINE2.
99 05 LINE 10 COLUMN 25 PIC X(9) FROM LOGIN-LINE3.
100 05 LINE 10 COLUMN 35 PIC X(20) TO LPD-USERNAME.
* 12-S******************************************************** ( 0)**
** Operand LPD-USERNAME is not declared
101 05 LINE 12 COLUMN 25 PIC X(9) FROM LOGIN-LINE4.
102 05 LINE 12 COLUMN 35 PIC X(20) TO LPD-PASSWORD
* 12-S******************************************************** ( 2)**
** Operand LPD-PASSWORD is not declared
103 SECURE.
104 05 LINE 16 COLUMN 10 PIC X(31) FROM
105 LOGIN-ERROR-LINE1.
106 05 LINE 17 COLUMN 10 PIC X(8) FROM
107 LOGIN-ERROR-LINE2.
108 05 LINE 17 COLUMN 19 PIC X FROM
109 LOGIN-ERROR-LINE-TRIES.
110 05 LINE 17 COLUMN 21 PIC X(10) FROM
111 LOGIN-ERROR-LINE2-2.

* Micro Focus COBOL for UNIX V3.2 revision 037 11-Mar-98 16:03 Page 3
* login.cbl
112
* LOGIN-LINE1
* 12-S*********** ( 2)**
** Operand LOGIN-LINE1 is not declared
113 PROCEDURE DIVISION USING PASSED-DATA.
114
115 MAIN.
116************************************************************
117* CONTROLS THE PROGRAM AND KICKS THE USER OUT IF THEY HAVE *
118* NOT LOGGED IN CORRECTLY AFTER 3 TRIES. *
119************************************************************
120 PERFORM INIT.
121 PERFORM PROC
122 UNTIL NUM-TRIES > MAX-TRIES OR
* 12-S*************************** ( 3)**
** Operand NUM-TRIES is not declared
123 PASS-TRUE = 'Y'.
124 PERFORM TERM.
125 EXIT PROGRAM.
126
127 INIT.
128 OPEN INPUT PASS-DAT.
* 12-S*************************** ( 3)**
** Operand PASS-DAT is not declared
129
130 PROC.
131 ADD 1 TO NUM-TRIES.
* 12-S************************** ( 3)**
** Operand NUM-TRIES is not declared
132 DISPLAY LOGIN-SCREEN.
133 ACCEPT LOGIN-SCREEN.
134 PERFORM READ-FILE.
135 INITIALIZE LOGIN-ERROR-LINE1.
* 12-S************************************ ( 3)**
** Operand LOGIN-ERROR-LINE1 is not declared
136 INITIALIZE LOGIN-ERROR-LINE2.
* 12-S************************************ ( 3)**
** Operand LOGIN-ERROR-LINE2 is not declared
137 INITIALIZE LOGIN-ERROR-LINE-TRIES.
* 12-S***************************************** ( 3)**
** Operand LOGIN-ERROR-LINE-TRIES is not declared
138 INITIALIZE LOGIN-ERROR-LINE2-2.
* 12-S************************************** ( 3)**
** Operand LOGIN-ERROR-LINE2-2 is not declared
139
140 TERM.
141 CLOSE PASS-DAT.
* 12-S********************** ( 3)**
** Operand PASS-DAT is not declared
142 IF PASS-TRUE = 'N'
* 12-S********************* ( 3)**
** Operand PASS-TRUE is not declared
143 MOVE 'Y' TO PD-EXIT-TRUE.
144
145 READ-FILE.
146 READ PASS-DAT INTO PASS-REC
* 12-S********************* ( 3)**
** Operand PASS-DAT is not declared

* Micro Focus COBOL for UNIX V3.2 revision 037 11-Mar-98 16:03 Page 4
* login.cbl
147 KEY IS LPD-USERNAME
148 INVALID KEY
149 MOVE INV-USER TO LOGIN-ERROR-MSG AND
* 12-S***************************** ( 3)**
** Operand INV-USER is not declared
150 PERFORM ERROR-ROUT
151 NOT INVALID KEY
* 561-S*************************** ( 4)**
** A "NOT" phrase did not have a matching verb and was discarded.
152 PERFORM PASS-CHECK
153 END-READ.
* 564-S**************** ( 4)**
** A scope-delimiter did not have a matching verb and was discarded.
154
155 PASS-CHECK.
156 CALL 'encrypt.int' USING LOGIN-PASSED-DATA.
* 12-S************************************************** ( 4)**
** Operand LOGIN-PASSED-DATA is not declared
157 CANCEL 'encrypt.int'.
158 IF LPD-PASSWORD = PR-USER-PASS
* 12-S************************ ( 4)**
** Operand LPD-PASSWORD is not declared
159 MOVE 'Y' TO PASS-TRUE
* 12-S********************************** ( 4)**
** Operand PASS-TRUE is not declared
160 ELSE
* 562-S************ ( 4)**
** An "ELSE" phrase did not have a matching IF and was discarded.
161 MOVE INV-PASS TO LOGIN-ERROR-MSG
* 12-S************************* ( 4)**
** Operand INV-PASS is not declared
162 PERFORM ERROR-ROUT.
163
164 ERROR-ROUT.
165 COMPUTE ERROR-TRIES = 3 - NUM-TRIES.
* 12-S*************************** ( 4)**
** Operand ERROR-TRIES is not declared
166 MOVE ERROR-TRIES TO LOGIN-ERROR-LINE-TRIES.
* 12-S************************ ( 4)**
** Operand ERROR-TRIES is not declared
167 MOVE LOGIN-ERROR-MSG2 TO LOGIN-ERROR-LINE2.
* 12-S***************************** ( 4)**
** Operand LOGIN-ERROR-MSG2 is not declared
168 MOVE LOGIN-ERROR-MSG2-2 TO LOGIN ERROR-LINE2-2.
* 12-S******************************* ( 4)**
** Operand LOGIN-ERROR-MSG2-2 is not declared
* Micro Focus COBOL for UNIX V3.2 revision 037 Compiler
* Copyright (C) 1984-1994 Micro Focus Ltd. URN 2XCLY/ZZ0/00000C
* REF GNB-049054000AA
*
* Last message on page: 4
*
* Total Messages: 25
* Unrecoverable : 0 Severe : 25
* Errors : 0 Warnings: 0
* Informational : 0 Flags : 0
* Data: 636 Code: 392
```

#### ↳ Re: Repost of help needed please

- **From:** "william m. klein" <ua-author-3041905@usenetarchives.gap>
- **Date:** 1998-03-10T19:00:02+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-fe4aa2c3ae-p2@usenetarchives.gap>`
- **In-Reply-To:** `<6e6u99$pnn@curly.cc.emory.edu>`
- **References:** `<6e6u99$pnn@curly.cc.emory.edu>`

```

Sylvia,
The message that you are getting about variables not declared certainly
looks like a BUG. You have a medium-old version of Micro Focus COBOL. Have
you or your faculty checked with MF about this? What I *did* notice was
that I couldn't find any declaration for CURSOR-POS. The messages that you
are getting certainly shouldn't be caused by that - but you might try fixing
that and see what happens.

Yes, there is a MF routine that will let you get the ASCII value of each key
that is entered. Check your manual for "call-by-name" routines (I can't
remember the name off the top of my head and don't have the manual handy).
```

##### ↳ ↳ Re: Repost of help needed please

- **From:** "david mowat" <ua-author-4670319@usenetarchives.gap>
- **Date:** 1998-03-12T19:00:03+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-fe4aa2c3ae-p3@usenetarchives.gap>`
- **In-Reply-To:** `<gap-fe4aa2c3ae-p2@usenetarchives.gap>`
- **References:** `<6e6u99$pnn@curly.cc.emory.edu> <gap-fe4aa2c3ae-p2@usenetarchives.gap>`

```


Sylvia,
My guess is that your names go past column 72?
David M.
```

#### ↳ Re: Repost of help needed please

- **From:** "william m. klein" <ua-author-3041905@usenetarchives.gap>
- **Date:** 1998-03-11T19:00:04+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-fe4aa2c3ae-p4@usenetarchives.gap>`
- **In-Reply-To:** `<6e6u99$pnn@curly.cc.emory.edu>`
- **References:** `<6e6u99$pnn@curly.cc.emory.edu>`

```

Sylvia,
I got a "definitive" answer to what is causing your problem. According to
my sources,

"This is an obscure one!
Â¥
The problem is all due to having the AUTHOR phrase followed by a comment
entry. The comment entry should be terminated by some text in area A.
The only recognized keyword that appears in area is PROCEDURE DIVISION.
To fix the program, just move ENVIRONMENT DIVISION to start in Column 8."

I hope this helps.

P.S. I couldn't tell from looking at your code that your stuff wasn't in
column 8 - but my source seemed certain that this was the problem.
```

##### ↳ ↳ Re: Repost of help needed please

- **From:** "don nelson" <ua-author-20234@usenetarchives.gap>
- **Date:** 1998-03-12T13:48:05+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-fe4aa2c3ae-p5@usenetarchives.gap>`
- **In-Reply-To:** `<gap-fe4aa2c3ae-p4@usenetarchives.gap>`
- **References:** `<6e6u99$pnn@curly.cc.emory.edu> <gap-fe4aa2c3ae-p4@usenetarchives.gap>`

```

William M. Klein wrote:
› 
› Sylvia,
…[9 more quoted lines elided]…
› 
Bill is exactly right. I get problem reports with this same thing all
the time. For those of us who maintain COBOL compilers it is a "ho hum"
problem. The compiler thought everything from AUTHOR to PROCEDURE
DIVISION was part of the AUTHOR comment entry. This is not a bug and
the compler is acting properly. This is one of the reasons why the
comment entries were made obsolete. You should never use them and
instead use a comment line.

Don Nelson
COBOL Development, Tandem Computers, Inc.
Member, NCITS J4 and ISO/IEC JTC1/SC22 WG4 COBOL Committees
don··.@tan··m.com
No clever quotes here
```

###### ↳ ↳ ↳ Re: Repost of help needed please

- **From:** "cobol frog (huib klink)" <ua-author-4414632@usenetarchives.gap>
- **Date:** 1998-03-12T19:00:06+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-fe4aa2c3ae-p6@usenetarchives.gap>`
- **In-Reply-To:** `<gap-fe4aa2c3ae-p5@usenetarchives.gap>`
- **References:** `<6e6u99$pnn@curly.cc.emory.edu> <gap-fe4aa2c3ae-p4@usenetarchives.gap> <gap-fe4aa2c3ae-p5@usenetarchives.gap>`

```

And of course:

All three types of headers should start in margin A (columns 8, 9, 10 or 11). The
program is still not syntactically correct when the environment division header is
placed in col. 8. Free format is in the next standard.

How subtle an error is this anyway. Those who solved it (Bill, others) earn a
compliment.

Impressed Frog
```

###### ↳ ↳ ↳ Re: Repost of help needed please

- **From:** "cobol frog (huib klink)" <ua-author-4414632@usenetarchives.gap>
- **Date:** 1998-03-12T19:00:07+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-fe4aa2c3ae-p7@usenetarchives.gap>`
- **In-Reply-To:** `<gap-fe4aa2c3ae-p5@usenetarchives.gap>`
- **References:** `<6e6u99$pnn@curly.cc.emory.edu> <gap-fe4aa2c3ae-p4@usenetarchives.gap> <gap-fe4aa2c3ae-p5@usenetarchives.gap>`

```

And of couse:

All three types of headers should start in margin A (columns 8, 9, 10 or 11). The
program is still not syntactically correct when the environment division header is
placed in col. 8. Free format is in the next standard.

How subtle an error is this anyway. Those who solved it (Bill, others) earn a
compliment.

Impressed Frog
```

###### ↳ ↳ ↳ Re: Repost of help needed please

- **From:** "cobol frog (huib klink)" <ua-author-4414632@usenetarchives.gap>
- **Date:** 1998-03-12T19:00:08+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-fe4aa2c3ae-p8@usenetarchives.gap>`
- **In-Reply-To:** `<gap-fe4aa2c3ae-p5@usenetarchives.gap>`
- **References:** `<6e6u99$pnn@curly.cc.emory.edu> <gap-fe4aa2c3ae-p4@usenetarchives.gap> <gap-fe4aa2c3ae-p5@usenetarchives.gap>`

```

Even my newsreader was imply depressed, eh, impres depleed, eh deeply imressed.

Cobol Frog (Huib Klink) wrote 3 times:

a lot 8<

› Impressed Frog
```

#### ↳ Re: Repost of help needed please

- **From:** "a..." <ua-author-17074323@usenetarchives.gap>
- **Date:** 1998-03-11T19:00:09+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-fe4aa2c3ae-p9@usenetarchives.gap>`
- **In-Reply-To:** `<6e6u99$pnn@curly.cc.emory.edu>`
- **References:** `<6e6u99$pnn@curly.cc.emory.edu>`

```

In article <6e6u99$p.··.@cur··y.edu>, sha··.@cur··y.edu
(Sylvia L. Hazelwood) wrote:

› I'm not certain whether the first posting did in fact post if so forgive me if not 
› here it is.
 
› --- snip ---
 
› Start of listing:
› * Micro Focus COBOL for UNIX         V3.2 revision 037 11-Mar-98 16:03 Page   1
› *                      login.cbl
› * Options: int(login.int) verbose nolist trace endp list(login.lst)
›     1 IDENTIFICATION DIVISION.
 
› ----- snip -----
 
›   110          05  LINE 17 COLUMN 21 PIC X(10) FROM
›   111              LOGIN-ERROR-LINE2-2.
…[6 more quoted lines elided]…
› **    Operand LOGIN-LINE1 is not declared

What do you have on line #112? It looks like it doesn't belong. Sometimes a
syntax error in a program will so totally confuse a compiler, that it
starts spitting out error messages for lines that aren't really errors.
That could be the case here. You need to carefully review the source code
and all error messages. Fixing one seemingly unrelated error could cause
the other error messages to dissappear
```

#### ↳ Re: Repost of help needed please

- **From:** "menno holscher" <ua-author-7393296@usenetarchives.gap>
- **Date:** 1998-03-13T19:00:10+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-fe4aa2c3ae-p10@usenetarchives.gap>`
- **In-Reply-To:** `<6e6u99$pnn@curly.cc.emory.edu>`
- **References:** `<6e6u99$pnn@curly.cc.emory.edu>`

```

Sylvia L. Hazelwood wrote:
› 44 WORKING-STORAGE SECTION.
› 45 COPY 'pass-rec.cbl'.
› 46

Just a guess (I do not know the compiler): try shifting the COPY
statement to area B (from column 12).

HTH
```

#### ↳ Re: Repost of help needed please

- **From:** "judson mcclendon" <ua-author-18805@usenetarchives.gap>
- **Date:** 1998-03-14T19:00:11+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-fe4aa2c3ae-p11@usenetarchives.gap>`
- **In-Reply-To:** `<6e6u99$pnn@curly.cc.emory.edu>`
- **References:** `<6e6u99$pnn@curly.cc.emory.edu>`

```

Sylvia, there mostly two things wrong with this program. Primarily, COBOL 85 does
not support free-form source. Division, section and paragraph headers should start
in column 8. Comments are placed inside the listing.

Sylvia L. Hazelwood wrote:
› I'm not certain whether the first posting did in fact post if so forgive me if not 
› here it is.
…[62 more quoted lines elided]…
›     45      COPY 'pass-rec.cbl'.
 
› Can't see what's in 'pass-rec.cbl'.
 
›     46
›     47      01  CONSTANTS.
…[57 more quoted lines elided]…
› **    Operand LPD-USERNAME is not declared

I believe this error may be caused by your source formatting problems.
I copied your source file to disk, corrected the allignment problems,
and DOS MF COBOL 3.2 did not give me this error.

›    101          05  LINE 12 COLUMN 25 PIC X(9) FROM LOGIN-LINE4.
›    102          05  LINE 12 COLUMN 35 PIC X(20) TO LPD-PASSWORD
› *  12-S********************************************************        (   2)**
› **    Operand LPD-PASSWORD is not declared
 
› Same here.
 
›    103              SECURE.
›    104          05  LINE 16 COLUMN 10 PIC X(31) FROM
…[13 more quoted lines elided]…
› **    Operand LOGIN-LINE1 is not declared
 
› Same here.  I did not get this error.
 
›    113  PROCEDURE DIVISION USING PASSED-DATA.
›    114
…[9 more quoted lines elided]…
› **    Operand NUM-TRIES is not declared
 
› Same here.
 
›    123                   PASS-TRUE = 'Y'.
›    124         PERFORM TERM.
…[5 more quoted lines elided]…
› **    Operand PASS-DAT is not declared
 
› Same here.
 
›    129
›    130     PROC.
›    131         ADD 1 TO NUM-TRIES.
› *  12-S**************************                                      (   3)**
› **    Operand NUM-TRIES is not declared
 
› Same here.
 
›    132         DISPLAY LOGIN-SCREEN.
›    133         ACCEPT LOGIN-SCREEN.
…[3 more quoted lines elided]…
› **    Operand LOGIN-ERROR-LINE1 is not declared
 
› Same here.
 
›    136         INITIALIZE LOGIN-ERROR-LINE2.
› *  12-S************************************                            (   3)**
› **    Operand LOGIN-ERROR-LINE2 is not declared
 
› Same here.
 
›    137         INITIALIZE LOGIN-ERROR-LINE-TRIES.
› *  12-S*****************************************                       (   3)**
› **    Operand LOGIN-ERROR-LINE-TRIES is not declared
 
› Same here.
 
›    138         INITIALIZE LOGIN-ERROR-LINE2-2.
› *  12-S**************************************                          (   3)**
› **    Operand LOGIN-ERROR-LINE2-2 is not declared
 
› Same here.
 
›    139
›    140     TERM.
›    141         CLOSE PASS-DAT.
› *  12-S**********************                                          (   3)**
› **    Operand PASS-DAT is not declared
 
› Same here.
 
›    142         IF  PASS-TRUE = 'N'
› *  12-S*********************                                           (   3)**
› **    Operand PASS-TRUE is not declared
 
› Same here.
 
›    143             MOVE 'Y' TO PD-EXIT-TRUE.
›    144
…[3 more quoted lines elided]…
› **    Operand PASS-DAT is not declared
 
› Same here.
 
› 
› * Micro Focus COBOL for UNIX         V3.2 revision 037 11-Mar-98 16:03 Page   4
…[5 more quoted lines elided]…
› **    Operand INV-USER is not declared
 
› Same here.  Also, the 'AND' at the end of the line should be removed.
 
›    150                 PERFORM ERROR-ROUT
›    151             NOT INVALID KEY
› * 561-S***************************                                     (   4)**
› **    A "NOT" phrase did not have a matching verb and was discarded.
 
› This was probably a cascade error caused by the syntax error above.
 
›    152                 PERFORM PASS-CHECK
›    153         END-READ.
› * 564-S****************                                                (   4)**
› **    A scope-delimiter did not have a matching verb and was discarded.
 
› Same cascade error.
 
›    154
›    155     PASS-CHECK.
›    156         CALL 'encrypt.int' USING LOGIN-PASSED-DATA.
› *  12-S**************************************************              (   4)**
› **    Operand LOGIN-PASSED-DATA is not declared
 
› Same column 8 problem in Data Division.
 
›    157         CANCEL 'encrypt.int'.
›    158         IF  LPD-PASSWORD = PR-USER-PASS
› *  12-S************************                                        (   4)**
› **    Operand LPD-PASSWORD is not declared

Column 8 problem for LPD-PASSWORD, but PR-USER-PASS is undefined,
unless it is in the COPY file.

›    159             MOVE 'Y'  TO PASS-TRUE
› *  12-S**********************************                              (   4)**
› **    Operand PASS-TRUE is not declared
 
› Column 8 in Data Division.
 
›    160         ELSE
› * 562-S************                                                    (   4)**
› **    An "ELSE" phrase did not have a matching IF and was discarded.
 
› Cascade error from above.
 
›    161             MOVE INV-PASS TO LOGIN-ERROR-MSG
› *  12-S*************************                                       (   4)**
› **    Operand INV-PASS is not declared
 
› Column 8 in Data Division.
 
›    162             PERFORM ERROR-ROUT.
›    163
…[3 more quoted lines elided]…
› **    Operand ERROR-TRIES is not declared
 
› Column 8 in Data Division.
 
›    166         MOVE ERROR-TRIES TO LOGIN-ERROR-LINE-TRIES.
› *  12-S************************                                        (   4)**
› **    Operand ERROR-TRIES is not declared
 
› Column 8 in Data Division.
 
›    167         MOVE LOGIN-ERROR-MSG2 TO LOGIN-ERROR-LINE2.
› *  12-S*****************************                                   (   4)**
› **    Operand LOGIN-ERROR-MSG2 is not declared
 
› Column 8 in Data Division.
 
›    168         MOVE LOGIN-ERROR-MSG2-2 TO LOGIN ERROR-LINE2-2.
› *  12-S*******************************                                 (   4)**
› **    Operand LOGIN-ERROR-MSG2-2 is not declared
 
› Column 8 in Data Division.
 
› * Micro Focus COBOL for UNIX         V3.2 revision 037 Compiler
› * Copyright (C) 1984-1994 Micro Focus Ltd.     URN 2XCLY/ZZ0/00000C
…[8 more quoted lines elided]…
› * Data:         636     Code:         392

Try this reformatted program with the 'AND' removed from line 149.
If you post or e-mail file 'pass-rec.cbl', I will try another compile.

1 IDENTIFICATION DIVISION.
2
3****************************************************************
4* THIS PROGRAM IS THE SUBPROGRAM LOGIN.CBL IT ALLOWS THE USER *
5* TO LOGIN AND THEN RETURNS CONTROL TO THE MAIN PROGRAM IF THE *
6* USER FAILS TO CORRECTLY IDENTIFY AFTER THREE TRIES THEY ARE *
7* KICKED OUT AND IT ALSO STORES THE NUMBER OF INCORRECT TRIES *
8****************************************************************
9
10 PROGRAM-ID. LOGIN-SUBPROGRAM.
11 AUTHOR. GROUP-A.
12 DATE-WRITTEN. 02-08-98.
13 DATE-COMPILED.
14
15 ENVIRONMENT DIVISION.
16
17 CONFIGURATION SECTION.
18
19
20 SOURCE-COMPUTER. IBM-RISC-6000.
21 OBJECT-COMPUTER. IBM-RISC-6000.
22
23 SPECIAL-NAMES.
24 CURSOR IS CURSOR-POS.
25
26 INPUT-OUTPUT SECTION.
27
28 FILE-CONTROL.
29
30 SELECT PASS-DAT
31 ASSIGN TO 'pass.dat'
32 ORGANIZATION IS INDEXED
33 ACCESS MODE IS RANDOM
34 RECORD KEY IS PR-USERNAME.
35
36 DATA DIVISION.
37
38 FILE SECTION.
39 FD PASS-DAT.
40 01 PASS-RECORD.
41 05 PR-USERNAME PIC X(20).
42 05 FILLER PIC X(25).
43
44 WORKING-STORAGE SECTION.
45 COPY 'pass-rec.cbl'.
46
47 01 CONSTANTS.
48 05 CON-USER PIC X(9) VALUE
49 'INEEDHELP'.
50 05 CON-PASS PIC X(15) VALUE
51 'IREALLYNEEDHELP'.
52 05 MAX-TRIES PIC 9 VALUE 2.
53 05 LOGIN-LINE1 PIC X(23) VALUE
54 'GOLF HANDICAPING SYSTEM'.
55 05 LOGIN-LINE2 PIC X(12) VALUE
56 'LOGIN SCREEN'.
57 05 LOGIN-LINE3 PIC X(9) VALUE
58 'USERNAME:'.
59 05 LOGIN-LINE4 PIC X(9) VALUE
60 'PASSWORD:'.
61 05 INV-USER PIC X(31) VALUE
62 'YOU DO NOT EXIST ON THIS SYSTEM'.
63 05 INV-PASS PIC X(19) VALUE
64 'INVALID PASSWORD!!!'.
65 05 LOGIN-ERROR-MSG2 PIC X(8) VALUE
66 'YOU HAVE'.
67 05 LOGIN-ERROR-MSG2-2 PIC X(10) VALUE
68 'MORE TRIES'.
69
70 01 MISC.
71 05 QUIT PIC X.
72 88 USER-EXIT VALUE 'Y'.
73 05 NUM-TRIES PIC 9.
74 05 PASS-TRUE PIC X VALUE 'N'.
75 05 LOGIN-ERROR-LINE1 PIC X(31) VALUE SPACES.
76 05 LOGIN-ERROR-LINE2 PIC X(8) VALUE SPACES.
77 05 LOGIN-ERROR-LINE-TRIES PIC X VALUE SPACES.
78 05 LOGIN-ERROR-LINE2-2 PIC X(10) VALUE SPACES.
79 05 ERROR-TRIES PIC 9 VALUE ZERO.
80
81 01 LOGIN-PASSED-DATA.
82 05 LPD-USERNAME PIC X(20).
83 05 LPD-PASSWORD PIC X(20).
84 05 RETURNED-PASSWORD PIC X(20).
85 05 RETURNED-USERNAME PIC X(20).
86
87 LINKAGE SECTION.
88 01 PASSED-DATA.
89 05 PD-USER-NUM PIC 9(4).
90 05 PD-LEV-PRIV PIC 9.
91 05 PD-EXIT-TRUE PIC X.
92 05 PD-NUM-TRIES PIC 99.
93
94 SCREEN SECTION.
95 01 LOGIN-SCREEN.
96 05 BLANK SCREEN.
97 05 LINE 2 COLUMN 28 PIC X(23) FROM LOGIN-LINE1.
98 05 LINE 4 COLUMN 34 PIC X(12) FROM LOGIN-LINE2.
99 05 LINE 10 COLUMN 25 PIC X(9) FROM LOGIN-LINE3.
100 05 LINE 10 COLUMN 35 PIC X(20) TO LPD-USERNAME.
101 05 LINE 12 COLUMN 25 PIC X(9) FROM LOGIN-LINE4.
102 05 LINE 12 COLUMN 35 PIC X(20) TO LPD-PASSWORD
103 SECURE.
104 05 LINE 16 COLUMN 10 PIC X(31) FROM
105 LOGIN-ERROR-LINE1.
106 05 LINE 17 COLUMN 10 PIC X(8) FROM
107 LOGIN-ERROR-LINE2.
108 05 LINE 17 COLUMN 19 PIC X FROM
109 LOGIN-ERROR-LINE-TRIES.
110 05 LINE 17 COLUMN 21 PIC X(10) FROM
111 LOGIN-ERROR-LINE2-2.
112
113 PROCEDURE DIVISION USING PASSED-DATA.
114
115 MAIN.
116************************************************************
117* CONTROLS THE PROGRAM AND KICKS THE USER OUT IF THEY HAVE *
118* NOT LOGGED IN CORRECTLY AFTER 3 TRIES. *
119************************************************************
120 PERFORM INIT.
121 PERFORM PROC
122 UNTIL NUM-TRIES > MAX-TRIES OR
123 PASS-TRUE = 'Y'.
124 PERFORM TERM.
125 EXIT PROGRAM.
126
127 INIT.
128 OPEN INPUT PASS-DAT.
129
130 PROC.
131 ADD 1 TO NUM-TRIES.
132 DISPLAY LOGIN-SCREEN.
133 ACCEPT LOGIN-SCREEN.
134 PERFORM READ-FILE.
135 INITIALIZE LOGIN-ERROR-LINE1.
136 INITIALIZE LOGIN-ERROR-LINE2.
137 INITIALIZE LOGIN-ERROR-LINE-TRIES.
138 INITIALIZE LOGIN-ERROR-LINE2-2.
139
140 TERM.
141 CLOSE PASS-DAT.
142 IF PASS-TRUE = 'N'
143 MOVE 'Y' TO PD-EXIT-TRUE.
144
145 READ-FILE.
146 READ PASS-DAT INTO PASS-REC
147 KEY IS LPD-USERNAME
148 INVALID KEY
149 MOVE INV-USER TO LOGIN-ERROR-MSG
150 PERFORM ERROR-ROUT
151 NOT INVALID KEY
152 PERFORM PASS-CHECK
153 END-READ.
154
155 PASS-CHECK.
156 CALL 'encrypt.int' USING LOGIN-PASSED-DATA.
157 CANCEL 'encrypt.int'.
158 IF LPD-PASSWORD = PR-USER-PASS
159 MOVE 'Y' TO PASS-TRUE
160 ELSE
161 MOVE INV-PASS TO LOGIN-ERROR-MSG
162 PERFORM ERROR-ROUT.
163
164 ERROR-ROUT.
165 COMPUTE ERROR-TRIES = 3 - NUM-TRIES.
166 MOVE ERROR-TRIES TO LOGIN-ERROR-LINE-TRIES.
167 MOVE LOGIN-ERROR-MSG2 TO LOGIN-ERROR-LINE2.
168 MOVE LOGIN-ERROR-MSG2-2 TO LOGIN ERROR-LINE2-2.
Judson McClendon          This is a faithful saying and worthy of all
Sun Valley Systems        acceptance, that Christ Jesus came into the
jud··.@min··g.com   world to save sinners  (1 Timothy 1:15)
(please remove zzz from email id to respond)
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
