[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# KEYBOARD, Accept and standard input

_2 messages · 2 participants · 1996-07_

**Topics:** [`Language features and syntax`](../topics.md#syntax) · [`COBOL standards (ANS, ISO, 74/85/2002/2014)`](../topics.md#standards)

---

### KEYBOARD, Accept and standard input

- **From:** "sven akkermans" <ua-author-16917105@usenetarchives.gap>
- **Date:** 1996-07-01T20:00:01+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<31D91676.1DC9@denkart.be>`

```

Hello,

I've got a COBOL program that reads from standard
input. The problem is that the READ (from stdin) and
the ACCEPT statement don't seem to be reading from
"the same standard input".

system : HP-UX 9000
OS : HP-UX 10.01
Microfocus cobol

IDENTIFICATION DIVISION.
Program-id. IO-tester.

ENVIRONMENT DIVISION.
CONFIGURATION SECTION.
INPUT-OUTPUT SECTION.
File-control.
select stdin assign to keyboard
organization is line sequential.
select stdin2 assign to keyboard
organization is line sequential.
select stdout assign to display.

DATA DIVISION.
FILE SECTION.
FD stdin.
01 input-record.
03 I-field1 PIC X(11).

FD stdin2.
01 input-record2.
03 I2-field1 PIC X(11).

FD stdout.
01 output-record.
03 O-field1 PIC X(11).

WORKING-STORAGE SECTION.
01 std-record PIC X(11).

PROCEDURE DIVISION.
open input stdin stdin2.

read-loop.
read stdin.
move input-record to std-record.
display "read : " std-record.
accept std-record.
* read stdin2 into std-record.
display "accepted : " std-record.
read stdin.
move input-record to std-record.
display "read : " std-record.
accept std-record.
* read stdin2 into std-record.
display "accepted : " std-record.

end-program.
display "end".
stop run.


The input file looks like
aaaaaaaaaaa
bbbbbbbbbbb
ccccccccccc
ddddddddddd

and the command I used to test it:

cat input-file | IO-TESTER

The result is that the accept statement seems to have no
effect.
In my opinion it should read the first line with the READ
stmt,
the next one with the ACCEPT, the next one with the READ and
the last one with the ACCEPT.
When I comment the 2 ACCEPT statements and uncomment the
READ statements, everything works fine.

Any suggestions are welcome,

Thanks in advance,
Sven Akkermans
s.··.@den··t.be
```

#### ↳ Re: KEYBOARD, Accept and standard input

- **From:** "joan colley" <ua-author-15559010@usenetarchives.gap>
- **Date:** 1996-07-03T20:00:02+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-d892bb0ca7-p2@usenetarchives.gap>`
- **In-Reply-To:** `<31D91676.1DC9@denkart.be>`
- **References:** `<31D91676.1DC9@denkart.be>`

```

Sven,

Is this your first attempt at a Cobol interactive program?

Normally in an interactive program you would use ACCEPT and DISPLAY not file i-o.

MF Cobol supports full ACCEPT and DISPLAY features, including cursor control.

I have never tried your method which I think rather cumbersome as I have a background in
interactive programming in Cobol - always using ACCEPT and DISPLAY.

It is possible to cat a file to an interactive program and the accept statement will
read the data from STDIN. You can also pipe the output from the displays.


Good Luck,
Joan Colley
Sydney
Australia

Sven Akkermans wrote:
› 
› Hello,
…[84 more quoted lines elided]…
› s.··.@den··t.be
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
