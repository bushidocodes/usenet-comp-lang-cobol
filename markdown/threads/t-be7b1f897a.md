[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Wich version is it? - archivo.zip (0/1)

_6 messages · 4 participants · 1998-07_

---

### Wich version is it? - archivo.zip (0/1)

- **From:** "fs..." <ua-author-9155794@usenetarchives.gap>
- **Date:** 1998-07-20T20:00:01+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<35b4d4d2.4428349@nntp.satlink.com>`

```
Hi,
I need your help.
My brother is intenting to import data from a COBOL based
system to a new one (in delphi)
The problem is that the compiler was lost in a hard drive
crash. We don't know the version of that compiler.
We have the source, and data files, retrieved from old backup.
I try to compile with RM-COBOL 85 ver 4.10.01 but it doesn't work.
The structure of the cobol data files is not regular, records
are not of the same long, it uses .dat and .idx files, and have
special caracters to mark the beginnig of records.
That characters are the real problem, it changes from file to
file, and some times are two, other are tree, even in the same file.
Our idea is use cobol to transform files form indexed
structure to sequential. Then we can import it in a easy way.
Here is a part of code and some files, I hope it is enoght for
to know wich version is.

IDENTIFICATION DIVISION.

PROGRAM-ID. PROGRAMA .
AUTHOR. SISTEMAS.

DATE-WRITTEN . ABRIL/93.

DATE-COMPILED.

ENVIRONMENT DIVISION.

CONFIGURATION SECTION.

SOURCE-COMPUTER. IBM.

OBJECT-COMPUTER. IBM.

INPUT-OUTPUT SECTION.

FILE-CONTROL.

SELECT PEU-COM ASSIGN TO DISK
ORGANIZATION IS INDEXED
ACCESS MODE IS DYNAMIC
RECORD KEY IS CLAVE
ALTERNATE RECORD KEY IS ALTERNA
WITH DUPLICATES
ALTERNATE RECORD KEY IS RECEP
WITH DUPLICATES
FILE STATUS IS ESTADO.
DATA DIVISION.

FILE SECTION.

FD PEU-COM LABEL RECORD IS STANDARD
VALUE OF FILE-ID IS FD-PEU-COM .
01 R-PEU-COM .
02 CLAVE .
03 TIPO PIC X(01) .
03 CASA PIC 9(04) .
03 NRO PIC 9(08) .
03 CODI2 PIC 9(04) .
02 FECHA PIC 9(06) .
02 ALTERNA .
03 CODIGO PIC 9(04) .
03 RECEP PIC 9(06) .
02 NOMBRE PIC X(30) .
02 CON-IVA PIC X(02) .
02 CUIT PIC X(15) .
02 CON-VTA PIC X(01) .
02 IMPORTE PIC 9(09)V9(02) .
02 DES-1 PIC 9(03)V9(02) .
02 DES-2 PIC 9(03)V9(02) .
02 DES-3 PIC 9(03)V9(02) .
02 DES-4 PIC 9(03)V9(02) .
02 DES-5 PIC 9(03)V9(02) .
02 VTO-1 PIC 9(06) .
02 FACT-1 PIC 9(03)V9(02) .
02 VTO-2 PIC 9(06) .
02 FACT-2 PIC 9(03)V9(02) .
02 VTO-3 PIC 9(06) .
02 FACT-3 PIC 9(03)V9(02) .
02 VTO-4 PIC 9(06) .
02 FACT-4 PIC 9(03)V9(02) .
02 PROVINCIA PIC X(15) .
02 NO-GRAVADO PIC 9(09)V9(02) .
02 EXENTOS PIC 9(09)V9(02) .
02 COMPRAS-NI PIC 9(09)V9(02) .
02 RETENCIONES PIC 9(09)V9(02) .
02 NETO-TG PIC 9(09)V9(02) .
02 NETO-TD PIC 9(09)V9(02) .
02 IVA PIC 9(09)V9(02) .
02 PERCEPCION PIC 9(09)V9(02) .
02 DESCUENTO PIC 9(08)V9(02) .
02 RESERVA PIC X(20) .
WORKING-STORAGE SECTION.

77 CONT PIC 99 VALUE 88.

01 ESTADO PIC X(02) .
01 FILLER REDEFINES ESTADO.

02 KEY1 PIC 9(01) .
02 KEY2 PIC 9(01) .
02 FILLER REDEFINES KEY2.

05 KEYDOS PIC 9(02) USAGE COMP.

01 FD-PEU-COM PIC X(20) VALUE "..\AP\PEU-PDE.DAT".
LINKAGE SECTION.
77 TAREA PIC X.

01 L-PEU-COM.
02 L-CLAVE .
03 L-TIPO PIC X(01) .
03 L-CASA PIC 9(04) .
03 L-NRO PIC 9(08) .
03 L-CODI2 PIC 9(04) .
02 L-FECHA PIC 9(06) .
02 L-ALTERNA .
03 L-CODIGO PIC 9(04) .
03 L-RECEP PIC 9(06) .
02 L-NOMBRE PIC X(30) .
02 L-CON-IVA PIC X(02) .
02 L-CUIT PIC X(15) .
02 L-CON-VTA PIC X(01) .
02 L-IMPORTE PIC 9(09)V9(02) .
02 L-DES-1 PIC 9(03)V9(02) .
02 L-DES-2 PIC 9(03)V9(02) .
02 L-DES-3 PIC 9(03)V9(02) .
02 L-DES-4 PIC 9(03)V9(02) .
02 L-DES-5 PIC 9(03)V9(02) .
02 L-VTO-1 PIC 9(06) .
02 L-FACT-1 PIC 9(03)V9(02) .
02 L-VTO-2 PIC 9(06) .
02 L-FACT-2 PIC 9(03)V9(02) .
02 L-VTO-3 PIC 9(06) .
02 L-FACT-3 PIC 9(03)V9(02) .
02 L-VTO-4 PIC 9(06) .
02 L-FACT-4 PIC 9(03)V9(02) .
02 L-PROVINCIA PIC X(15) .
02 L-NO-GRAVADO PIC 9(09)V9(02) .
02 L-EXENTOS PIC 9(09)V9(02) .
02 L-COMPRAS-NI PIC 9(09)V9(02) .
02 L-RETENCIONES PIC 9(09)V9(02) .
02 L-NETO-TG PIC 9(09)V9(02) .
02 L-NETO-TD PIC 9(09)V9(02) .
02 L-IVA PIC 9(09)V9(02) .
02 L-PERCEPCION PIC 9(09)V9(02) .
02 L-DESCUENTO PIC 9(08)V9(02) .
02 L-RESERVA PIC X(20) .
SCREEN SECTION.

01 PANTA-YA.

02 LINE 24 COLUMN 1 VALUE

" [ ATENCION ] " REVERSE-VIDEO.

02 COLUMN 41 VALUE

"YA EXISTE <嚙踝蕭 " REVERSE-VIDEO.

02 COLUMN 56 PIC X TO TAREA REVERSE-VIDEO AUTO.

01 PANTA-NO.

02 LINE 24 COLUMN 1 VALUE

" [ ATENCION ] " REVERSE-VIDEO.

02 COLUMN 41 VALUE

"NO EXISTE <嚙踝蕭 " REVERSE-VIDEO.

02 COLUMN 56 PIC X TO TAREA REVERSE-VIDEO AUTO.

01 PANTA-PEU-COM .

02 LINE 23 COLUMN 1 VALUE

" [ PEU-COM ] " REVERSE-VIDEO.
02 COLUMN 41 VALUE

" " REVERSE-VIDEO.

02 COLUMN 19 PIC X(20) FROM FD-PEU-COM REVERSE-VIDEO.
01 CLS.

02 BLANK SCREEN.

PROCEDURE DIVISION USING L-PEU-COM TAREA.
INICIO.

IF TAREA = "E" OR TAREA = "e" GO TO EXISTE.
GO TO XFINAL.
EXISTE.
OPEN INPUT PEU-COM.
IF ESTADO NOT = ZEROS DISPLAY PANTA-PEU-COM
CALL "MENSAJ" USING ESTADO GO TO XFINAL.
MOVE L-CLAVE TO CLAVE.
READ PEU-COM INVALID KEY MOVE ZEROS TO L-NRO
GO TO EXISTE-FIN.
IF ESTADO NOT = ZEROS AND NOT = "02" DISPLAY PANTA-PEU-COM
CALL "MENSAJ" USING ESTADO GO TO EXISTE-FIN.
MOVE R-PEU-COM TO L-PEU-COM.
EXISTE-FIN.
CLOSE PEU-COM.
GO TO XFINAL.
XFINAL.
EXIT PROGRAM.

____________________________________________________

Francisco G. Simo'
Villa Carlos Paz - Cordoba
Argentina
____________________________________________________

ema··.@com··r.org
http://webs.satlink.com/usuarios/f/fsimo/
____________________________________________________
ICQ #: 14812559
```

#### ↳ Re: Wich version is it? - archivo.zip (0/1)

- **From:** "donald tees" <ua-author-44233@usenetarchives.gap>
- **Date:** 1998-07-20T20:00:02+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-be7b1f897a-p2@usenetarchives.gap>`
- **In-Reply-To:** `<35b4d4d2.4428349@nntp.satlink.com>`
- **References:** `<35b4d4d2.4428349@nntp.satlink.com>`

```
I would guess Micro Focus.
```

#### ↳ Re: Wich version is it? - archivo.zip (0/1)

- **From:** "greg" <ua-author-13260@usenetarchives.gap>
- **Date:** 1998-07-21T17:08:03+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-be7b1f897a-p3@usenetarchives.gap>`
- **In-Reply-To:** `<35b4d4d2.4428349@nntp.satlink.com>`
- **References:** `<35b4d4d2.4428349@nntp.satlink.com>`

```
This may be RMCOBOL ver 2.xx (prior to RMCOBOL-85, which was introduced
with ver 4.xx). Ver 2.xx did not have checks for record lengths during
reads. Also, you may be dealing with a dual-file index file, which was
supported by ver 2.xx runtimes. A dual-file system automatically stored
information in two separate files with specific suffixes. If you open a
ver 2.xx dual-file index file named FILENAME.DAT, the runtime also opens
a file named FILENAME.INX. The INX file contains the index tree, and the
DAT file is a relative file containing data records.

RMCOBOL-85 came with conversion utilities. Also, the ver. 4.xx runtime
may have flags that tell it to emulate a ver. 2.xx runtime.

Hope this helps.

-Greg


Francisco G. Simo' wrote:
› 
› Hi,
…[219 more quoted lines elided]…
› ICQ #: 14812559
```

##### ↳ ↳ Re: Wich version is it? - archivo.zip (0/1)

- **From:** "fs..." <ua-author-9155794@usenetarchives.gap>
- **Date:** 1998-07-21T20:00:04+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-be7b1f897a-p4@usenetarchives.gap>`
- **In-Reply-To:** `<gap-be7b1f897a-p3@usenetarchives.gap>`
- **References:** `<35b4d4d2.4428349@nntp.satlink.com> <gap-be7b1f897a-p3@usenetarchives.gap>`

```
On Tue, 21 Jul 1998 21:08:13 GMT, greg wrote:

› This may be RMCOBOL ver 2.xx (prior to RMCOBOL-85, which was introduced
› with ver 4.xx). Ver 2.xx did not have checks for record lengths during
…[10 more quoted lines elided]…
› Hope this helps.

No, I was thing the same, but the .idx and .dat files are complety
differents.

This files are not RM version 2.0
____________________________________________________

Francisco G. Simo'
Villa Carlos Paz - Cordoba
Argentina
____________________________________________________

ema··.@com··r.org
http://webs.satlink.com/usuarios/f/fsimo/
____________________________________________________
ICQ #: 14812559
```

###### ↳ ↳ ↳ Re: Wich version is it? - archivo.zip (0/1)

- **From:** "nop0..." <ua-author-471015@usenetarchives.gap>
- **Date:** 1998-07-21T20:00:05+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-be7b1f897a-p5@usenetarchives.gap>`
- **In-Reply-To:** `<gap-be7b1f897a-p4@usenetarchives.gap>`
- **References:** `<35b4d4d2.4428349@nntp.satlink.com> <gap-be7b1f897a-p3@usenetarchives.gap> <gap-be7b1f897a-p4@usenetarchives.gap>`

```
On Wed, 22 Jul 1998 11:18:07 GMT, fs··.@com··r.org (Francisco G.
Simo') wrote:

› 
› No, I was thing the same, but the .idx and .dat files are complety
…[5 more quoted lines elided]…
› Francisco G. Simo'

Francisco.

Has I have asked you by email if you can send me one of this pair
of files (the smaller you can get, as long it has some valid data
on it) maybe I can find out the COBOL that created them.

Best regards

Frederico Fonseca

e-mail: nop06685 at mail dot telepac dot pt
```

#### ↳ Re: Wich version is it? - archivo.zip (0/1)

- **From:** "fs..." <ua-author-9155794@usenetarchives.gap>
- **Date:** 1998-07-21T20:00:06+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-be7b1f897a-p6@usenetarchives.gap>`
- **In-Reply-To:** `<35b4d4d2.4428349@nntp.satlink.com>`
- **References:** `<35b4d4d2.4428349@nntp.satlink.com>`

```
I think you are right. Any version consideration?

On Tue, 21 Jul 1998 19:19:45 GMT, "Judson McClendon"
wrote:

› The IDX and DAT files look like Micro Focus COBOL.
› --
…[3 more quoted lines elided]…
› (please remove numbers from email id to respond)

____________________________________________________

Francisco G. Simo'
Villa Carlos Paz - Cordoba
Argentina
____________________________________________________

ema··.@com··r.org
http://webs.satlink.com/usuarios/f/fsimo/
____________________________________________________
ICQ #: 14812559
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
