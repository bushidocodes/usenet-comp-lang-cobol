[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Initializing a char using ASCII value in COBOL

_3 messages · 3 participants · 2004-08_

---

### Initializing a char using ASCII value in COBOL

- **From:** b18cspecr@yahoo.ca (Type-D)
- **Date:** 2004-08-26T13:40:19-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<ebdca0cf.0408261240.1f740a03@posting.google.com>`

```
Hi people!

What I'm trying to do is very simple, but I just can't figure it out
since I'm not too good with COBOL. I have a set of characters that
must not be found in a particular string. I know how to search a
string and all, but my problem is that I receive the ASCII values of
these characters and I can't seem to find a way to convert them back
to chars (pic x) efficiently!? What I'm looking to do exactly is
something like this piece of "C" code does:

int iSomeChar = 64;
char cThisChar = iSomeChar;

Since ASCII for 0064 is "@", cThisChar now has the value "@". It's so
simple that I even feel dumb asking. Thanks a lot for your help,

Type-D
```

#### ↳ Re: Initializing a char using ASCII value in COBOL

- **From:** "Chuck Stevens" <charles.stevens@unisys.com>
- **Date:** 2004-08-26T13:44:41-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<cgli3q$ed9$1@si05.rsvl.unisys.com>`
- **References:** `<ebdca0cf.0408261240.1f740a03@posting.google.com>`

```
Would the intrinsic function "CHAR" meet your needs?

    -Chuck Stevens

"Type-D" <b18cspecr@yahoo.ca> wrote in message
news:ebdca0cf.0408261240.1f740a03@posting.google.com...
> Hi people!
>
…[14 more quoted lines elided]…
> Type-D
```

#### ↳ Re: Initializing a char using ASCII value in COBOL

- **From:** jlcaverlyca@yahoo.ca (Joe Caverly)
- **Date:** 2004-08-27T03:49:48-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<974d391e.0408270249.1ba17ba1@posting.google.com>`
- **References:** `<ebdca0cf.0408261240.1f740a03@posting.google.com>`

```
b18cspecr@yahoo.ca (Type-D) wrote in message news:<ebdca0cf.0408261240.1f740a03@posting.google.com>...
> Hi people!
> 
…[14 more quoted lines elided]…
> Type-D

Hi,
  Hopefully this will help.

Joe

Knowledge Base

Title: REDEFINES in COBOL 3.0/3.0a Can Mimic BASIC's ASC and CHR$ 
Document Number: Q58566           Publ Date: 20-APR-1993 
Product Name: Microsoft COBOL Compiler 
Product Version:  3.00 3.00a | 3.00 3.00a 
Operating System: MS-DOS     | OS/2 

 ---------------------------------------------------------------------- 
 The information in this article applies to:

  - Microsoft COBOL for MS-DOS and OS/2, versions 3.0 and 3.0a 
 ----------------------------------------------------------------------

 Summary:

 Microsoft COBOL Compiler Versions 3.0 and 3.0a do not have a 
 statement that directly converts between characters (PIC X) and their 
 numeric ASCII representations. However, you can write a program using 
 COBOL's REDEFINES clause to do this conversion. (This conversion is 
 equivalent to that done by the CHR$ and ASC functions found in 
 Microsoft BASIC.)

 More Information:

 By using the REDEFINES clause, the same variable (memory location) can 
 be referenced using different formats. By using a PIC X for a 
 character and a PIC 99 COMP-X, BASIC's CHR$ and ASC functions are 
 simulated in COBOL by moving information into one data-name and 
 checking the other.

 Note that BASIC's CHR$(num) function returns a one-character string 
 whose ASCII code is num. BASIC's ASC(stringargument) function returns 
 a numeric value that is the ASCII code for the first character in the 
 stringargument.

 The following code example illustrates how to use COBOL's REDEFINES 
 clause to simulate BASIC's ASC() and CHR$() functions:

        WORKING-STORAGE SECTION. 
        01  CHR PIC X. 
        01  ASC PIC 99 COMP-X REDEFINES CHR.

        PROCEDURE DIVISION. 
        000-MAIN.

       **** equivalent to ASC("X") in BASIC 
            MOVE "X" TO CHR. 
            DISPLAY "ASCII VALUE OF X:". 
            DISPLAY ASC.

       **** equivalent to CHR$(89) 
            MOVE 89 TO ASC. 
            DISPLAY "CHAR FOR ASCII 89:". 
            DISPLAY CHR.

            STOP RUN.

 The output of the above program is as follows:

    ASCII VALUE OF X: 
    088 
    CHAR FOR ASCII 89: 
    Y

 Additional reference words: 3.00 3.00a 

COPYRIGHT Microsoft Corporation, 1993.
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
