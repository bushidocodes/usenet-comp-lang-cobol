[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Table logic

_2 messages · 2 participants · 1998-05_

---

### Table logic

- **From:** "mark celli" <ua-author-17084328@usenetarchives.gap>
- **Date:** 1998-05-05T20:00:01+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<354FE8AF.7C689043@earthlink.net>`

```
Hello to all!
I'm a programing student here in New Jersey at The Chubb Institute.
I have consulted with the group before in regards to some questions I've
had in the earlier units of my studies and have come across another one
that I hope y'all could answer.
The purpose of the project that we are writing is to use a table of
print lines to format a bank statement. Now the concept of tables(1 or 2
level, literal values, etc.) I understand but for this project, we need
to define the table of print lines using a separate page for each new
customer read from an activity file.Again no problem to format a page
for 1 customer but the trick comes in when the detail lines needed to be
formatted (18 double spaced) on the page contain different
information(i.e. deposits, checks,atm,etc).
Our instructor has tipped us off saying that the detail lines are
actually a table within a table and not a two level table as I
believed.My question is when defining the table of print lines does it
look something like this?


01 PRINT-LINES.
05.
10 PIC X(100).
10 PIC X(50).
05 DET-LINE OCCURS 18 TIMES INDEXED BY DET-IND.
10 DESC-MSG PIC X(25).
10 PIC X(10).
10 ETC...
01 PRINT-TAB REDEFINES PRINT-LINES.
O5 PRINT-TAB OCCURS 26 TIMES INDEXED BY PRINT-IND.
10 PIC X(150).


Would this allow all 18 of the customers activities(providing there were
a full 18) to be printed along with the other 8 lines of print lines?

Again thanx in advance
for any help.
Mark Celli

nic··.@ear··k.net
```

#### ↳ Re: Table logic

- **From:** "in..." <ua-author-17074430@usenetarchives.gap>
- **Date:** 1998-05-06T09:29:02+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-6aad7d1a37-p2@usenetarchives.gap>`
- **In-Reply-To:** `<354FE8AF.7C689043@earthlink.net>`
- **References:** `<354FE8AF.7C689043@earthlink.net>`

```

›    The purpose of the project that we are writing is to use a table of
› print lines to format a bank statement. Now the concept of tables(1 or 2
…[9 more quoted lines elided]…
› look something like this?
 
› 01 PRINT-LINES.
›     05.
…[9 more quoted lines elided]…
› 

Your basic table definition here is faulty, if I see it correctly...
You say here PRINT-LINES consists of one field (first 05) of 150 bytes
and then 18 fields (DET-LINE), presumably also each 150bytes. A total
of 19 X 150.
Then you redefine that as a field - PRINT-TAB (please give the 01 and
05 different names) and this consists of 26 times 150bytes.

In order to really understand tables you must be able to draw them in
a diagram - which will prove impossible with the above.

So before you start coding - let's look at the DRAWING of the table:
(Pse use a non-proportional font to view this)


--------------------------------
1 | |
--------------------------------
2 | |
--------------------------------
3 | |
--------------------------------
4 | |
--------------------------------
5 | |
--------------------------------
6 | |
--------------------------------
7 | |
--------------------------------
8 | |
--------------------------------
1 | |
--------------------------------
2 | |
--------------------------------
3 | |
.
.
16| |
--------------------------------
17| |
--------------------------------
18| |
--------------------------------

Now first do the plain language translation of what you see and then
you convert THAT into coding:
The table consist of eight printlines:
01 W07-PRINT-LINE-TABLE.
03 W07-PRINT-LINES occurs 8.
05 W07-FIRST-LINES PIC X(150).

Then the table consist of a second part (could have been a seperate
table) which consist of 18 detail lines:
01 W07-PRINT-LINE-TABLE.
03 W07-PRINT-LINES OCCURS 8.
05 W07-FIRST-LINES PIC X(150).
03 W07-DETAILLINES OCCURS 18.
05 W07-DL-FIELD-ONE PIC X(16).
05 W07 and whatever ....

So you can see that you have two tables coded under one 01 level.
Maybe I understood you wrong, but from my interpretation, that is my
2c worth.....


Johan Potgieter
www.choicetraining.com
in··.@cho··g.com
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
