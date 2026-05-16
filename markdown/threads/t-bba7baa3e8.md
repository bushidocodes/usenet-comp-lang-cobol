[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# COBOL and C

_4 messages · 4 participants · 1998-10_

---

### COBOL and C

- **From:** "Mike Kozelka" <mkozelka@execpc.com>
- **Date:** 1998-10-05T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<6vb2fi$lr7@newsops.execpc.com>`

```
        I'm trying to link to a C library of routines on a PC.  I don't know
anything about C.  Below is the C structure I'm supposed to use.  I
think I know what some of these items are; see the Linkage Section
following.
        My question is: What are the COBOL definitions of the items in the
Linkage Section that have the '?' ?.  Any help would be appreciated.

              C Structure:
typedef struct z_stream_s {
    Bytef    *next_in;  /* next input byte */
    uInt     avail_in;  /* number of bytes available at next_in */
    uLong    total_in;  /* total nb of input bytes read so far */

    Bytef    *next_out; /* next output byte should be put there */
    uInt     avail_out; /* remaining free space at next_out */
    uLong    total_out; /* total nb of bytes output so far */

    char     *msg;      /* last error message, NULL if no error */
    struct internal_state FAR *state; /* not visible by applications */

    alloc_func zalloc;  /* used to allocate the internal state */
    free_func  zfree;   /* used to free the internal state */
    voidpf     opaque;  /* private data object passed to other routines */

    int     data_type;  /* best guess about the data type: ascii or binary
*/
    uLong   adler;      /* adler32 value of the data */
    uLong   reserved;   /* reserved for future use */
} z_stream;

typedef z_stream FAR *z_streamp;

                        COBOL Linkage Section

       LINKAGE SECTION.
       01  Z-STREAM-STRUCTURE.
           05  NEXT-IN              POINTER.
           05  AVAIL-IN             PIC 9(04) COMP-5 VALUE 0.
           05  TOTAL-IN             PIC 9(08) COMP-5 VALUE 0.
           05  NEXT-OUT             POINTER.
           05  AVAIL-OUT            PIC 9(04) COMP-5 VALUE 0.
           05  TOTAL-OUT            PIC 9(08) COMP-5 VALUE 0.
           05  ERR-MSG              POINTER.
           05  INTERNAL-STATE       POINTER.
           05  ALLOC-FUNC           ?
           05  FREE-FUNC            ?
           05  OPAQUE               ?
           05  DATA-TYPE            PIC 9(04) COMP-5 VALUE 1.
           05  ADLER32              PIC 9(08) COMP-5 VALUE 0.
           05  RESERVE-IT           PIC 9(08) COMP-5 VALUE 0.

       PROCEDURE DIVISION USING Z-STREAM-STRUCTURE.
```

#### ↳ Re: COBOL and C

- **From:** cadams@cadams-ntw.acucorp.com (Chris Adams)
- **Date:** 1998-10-05T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<slrn71i8c4.h0q.cadams@cadams-ntw.acucorp.com>`
- **References:** `<6vb2fi$lr7@newsops.execpc.com>`

```
On Mon, 5 Oct 1998 09:05:26 -0500, Mike Kozelka <mkozelka@execpc.com> wrote:
>        I'm trying to link to a C library of routines on a PC.  I don't know
>anything about C.  Below is the C structure I'm supposed to use.  I
>think I know what some of these items are; see the Linkage Section
>following.

What compiler are you using? 

>        My question is: What are the COBOL definitions of the items in the
>Linkage Section that have the '?' ?.  Any help would be appreciated.

>    alloc_func zalloc;  /* used to allocate the internal state */
>    free_func  zfree;   /* used to free the internal state */
>    voidpf     opaque;  /* private data object passed to other routines */

These are all custom types that have been declared somewhere in your C program,
probably in the header files. You can use a tool like grep to search through
the source to find out just what these are declared to be.  

>           05  INTERNAL-STATE       POINTER.

As a side comment, the C code referred to this as *state. It might be a good
idea to keep the names the same to avoid confusion. 
```

#### ↳ Re: COBOL and C

- **From:** Scott McKellar <mck9@swbell.net>
- **Date:** 1998-10-05T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<361961D9.2699@swbell.net>`
- **References:** `<6vb2fi$lr7@newsops.execpc.com>`

```
(posted and mailed)

Mike Kozelka wrote:
> 
>         I'm trying to link to a C library of routines on a PC.  I don't know
…[50 more quoted lines elided]…
>        PROCEDURE DIVISION USING Z-STREAM-STRUCTURE.

As Chris Adams has already pointed out, the C datatypes in question
(alloc_func, free_func, and voidpf) are not defined by the C language.
They are presumably defined somewhere in a header file that came
with your library.

However, the following are reasonable guesses:

alloc_func and free_func are probably function pointers.  The
equivalent in COBOL, in dialects which support it, is called a
procedure pointer.  If your dialect doesn't support it then you
can't use them from COBOL anyway; just declare FILLER of the
appropriate sizes -- either two bytes or four, depending on the 
compiler and memory model.

A voidpf is probably a void pointer, i.e. a generic pointer to an 
unspecified datatype.  COBOL pointers are untyped (in the few 
dialects I'm familiar with, anyway), so just call it POINTER.

Keep in mind that C does not guarantee that the members of a struct
are contiguous in memory.  The compiler is at liberty to insert padding
bytes wherever it pleases in order to maintain byte alignment. 
Intel-based compilers typically give the user a compile-time option to 
suppress padding bytes.  You'll need to find out how this option was 
set for whatever C code you're interfacing to.  In the presence of
padding bytes it may take some experimentation -- preferably with the
help of a C programmer -- to determine the appropriate offset for 
each member.

Michael C. Kasten	mck9@swbell.net
http://home.swbell.net/mck9/cobol/cobol.html
```

#### ↳ parameter passing intro was Re: COBOL and C

- **From:** gvwmoore@ix.netcom.com (G Moore)
- **Date:** 1998-10-06T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<36248e70.10521378@nntp.ix.netcom.com>`
- **References:** `<6vb2fi$lr7@newsops.execpc.com>`

```
On Mon, 5 Oct 1998 09:05:26 -0500, "Mike Kozelka"
<mkozelka@execpc.com> wrote:

>        My question is: What are the COBOL definitions of the items in the
>Linkage Section that have the '?' ?.  Any help would be appreciated.

A SECOND GLANCE (i wrote this after thinking long about it)

look up CBL_Byte stream functions.
quite frankly, i think the C programmer is giving you the runaround.
COBOL has byte stream functions. the only real parameters that your
C program might have that the CBL doesn't would be the opaque
function pointer and best-guess data. for that, you would have to
define opaque as external, and verify it exists upon running your
COBOL program.


A FIRST GLANCE (an answer to your initial question)

probably all are procedure pointer.

voidpf is probably a void pointer to function. however, the other two
are not vpfs, so my best guess is that they take parameters.

however, i would make certain the parameters you pass are matched
exactly by reference or value, the correct USAGE, and exactly as the C
and COBOL parameter standards given by both compilers. make sure to
write comments in your source code for parameter passing, and how
parameter passing works from the COBOL and C compiler in
your COBOL code. parameter orders for C are pascal or C based, and you
should include docs on both, as well as the default method.

alittle more about usage. data and code might in the COBOL compiler be
defined with less or more space than that in the C compiler. matching
this data 1:1 is an absolute necessity. you can write error checking
code for verifying your first time run of the data, but if the
function pointers are passed wrong, your machine will crash anyways.

one thing to make certain is the two outside data variables are
verified the first run through. thus:

    struct internal_state FAR *state; /* not visible by applications
*/

should be verified as should
    int     data_type;  /* best guess about the data type: ascii or
binary
*/

this will make certain your function pointers at *least* take up the
right amount of space (as they are sandwiched between those two
variables), which is 1 method of verifying they are passed correctly.

this assumes the sub-structures are not aligned on boundaries.

now, pretend you want to assign a value to be passed to your alloc.
you first must make certain you are passing the correct *size*
variable. (for instance, the FAR variable tells me you r using a
segmented architecture)

get your C programmer to tell you the size of the function pointers.

printf ( "%d bytes",	sizeof(	functionpointertype)	);

where functionpointertype = alloc free or opaque should give you an
idea of what size of function pointer you are dealing with.

another note, make certain that you include info on returned
variables, and verify at least 1 returned variable.

on some stack based machines, variables may be changed, but returned
variables may not be removed from the stack, and cause the machine to
crash. make a comment in your source code that this is a possibility,
under the environment, object computer section.

and finally , after you get your cobol program running, assert the
program you connect to's date has not changed.
a changed date may mean changes in the structure types.

if it is changed, halt the computer, send a message to the operator
with info to the C source code file name (if possible) or company name
and phone number (if not), and offer to continue the program, or halt
the machine, with a variable that doesn't ask until the next time the
cobol prog is run.

now your cobol program is bullet proofed and commented.

So lets look at the steps involved:

a>verify correct USAGE clauses

b>verify data is passed
	1>on boundaries or not
	2>by reference or value
	3>tests same value in called and calling programs
c>verify code pointers are sandwiched between two data statements
d>verify code pointers are correct size
	1>document all far and near types in COBOL source
e>verify and document returned variables
f>verify stacks position before and after called function

thats a 1 way parameter pass. 2 way parameter passing requires
you to verify which data/code is memory managed.



gvwmoore@ix.spam.netcom.com to reply remove the spam
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
