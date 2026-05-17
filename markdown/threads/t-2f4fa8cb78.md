[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Pointers Help in Vax Cobol

_8 messages · 7 participants · 1997-06_

---

### Pointers Help in Vax Cobol

- **From:** "esn..." <ua-author-17073673@usenetarchives.gap>
- **Date:** 1997-06-25T09:38:01+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<867245887.18115@dejanews.com>`

```

I am in need of a solution: How to use pointers in an older version of
COBOL.

The particulars are: DEC VAX 6440 running VMS 5.5.2, using VAX COBOL
4.4-65, compiled by a Ver3 VAX COBOL 85 Compiler.

The compiler does not support set "address of" needed for the use of
pointers. I need to be able to pass pointers to and from a C program.

All of this is on a client machine to which I need to provide a solution.
What are my options:
A newer compiler? Will Vax Cobol 4.4 support pointers with a newer
compiler?
A third party solution? ie. API to IP Socket
Other?

Please advise.

-------------------==== Posted via Deja News ====-----------------------
http://www.dejanews.com/ Search, Read, Post to Usenet
```

#### ↳ Re: Pointers Help in Vax Cobol

- **From:** "gtru..." <ua-author-1163276@usenetarchives.gap>
- **Date:** 1997-06-25T20:00:02+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-2f4fa8cb78-p2@usenetarchives.gap>`
- **In-Reply-To:** `<867245887.18115@dejanews.com>`
- **References:** `<867245887.18115@dejanews.com>`

```

On Wed, 25 Jun 1997 08:53:21 -0600, esn··.@tou··t.com wrote:

› I am in need of a solution: How to use pointers in an older version of
› COBOL.
…[14 more quoted lines elided]…
› Please advise.

4.4 is over 5 years old. My 5.0 book is dated 1992. However:

VAX COBOL's handling of pointers is limited and apparently different
from other COBOLs.

It has a pointer data type, it's value can be set to refer to other
data items in a program either in working-storage with the VALUE IS
REFERENCE data-item, or in the procedure division with SET
pointer-name TO REFERENCE data-item.

Generally you 'dereference' a pointer in a called program by merely
defining the structure that it references in the LINKAGE SECTION.

This pair of programs show how that works, and also how to dereference
a pointer using a library call.

identification division.
program-id. callingprogram.
data division.
working-storage section.
1 ptr pointer.
1 datastruct.
3 pic x(20) value "this is the data".
procedure division.
begin.
set ptr to reference of datastruct
call "calledprogram" using by value ptr by reference datastruct
by reference ptr
* on return show the modified datastruct
display datastruct.
end program callingprogram.

identification division.
program-id. calledprogram.
data division.
working-storage section.
1 gottendata pic x(20).
1 twenty pic 9999 comp value 20.
1 one pic 9999 comp value 1.
1 star pic x value "*".
1 newpointer pointer.
linkage section.
1 pointedto pic x(20).
1 referenced pic x(20).
1 thepointer pointer.
procedure division using pointedto referenced thepointer.
begin.
* copy data pointed to by thepointer to working-storage
call "lib$movc3" using
twenty
by value thepointer
by reference gottendata
* show the result of the 3 references to the same data
* ought to be the same
display pointedto
display referenced
display gottendata
* modify the pointer then modify the data pointed to
add thepointer 4 giving newpointer
call "lib$movc3" using
one
star
by value newpointer.
end program calledprogram.

George Trudeau, Town of Falmouth
```

##### ↳ ↳ Re: Pointers Help in Vax Cobol

- **From:** "arnold trembley" <ua-author-6588869@usenetarchives.gap>
- **Date:** 1997-06-26T20:00:03+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-2f4fa8cb78-p3@usenetarchives.gap>`
- **In-Reply-To:** `<gap-2f4fa8cb78-p2@usenetarchives.gap>`
- **References:** `<867245887.18115@dejanews.com> <gap-2f4fa8cb78-p2@usenetarchives.gap>`

```

George Trudeau wrote:
› 
› Generally you 'dereference' a pointer in a called program by merely
…[3 more quoted lines elided]…
› a pointer using a library call.

This language has confused me for some time. The first time I read
"dereferencing a pointer" in an article about C or C++ programming a few
years back, I immediately assumed it meant "to drop addressability". When
I use SET ADDRESS OF linkage-section-record TO pointer-name, I think of
that as establishing addressability to that record.

But increasingly it seems to me "dereferencing a pointer" means to establish
addressability to a storage area. Is this the common meaning for this idiom?
Would it mean something different to say you were "referencing a pointer"?

I am not trying to be picky about the English language. I'm just trying to
understand a technical term I'm not used to.

Arnold Trembley
Software Engineer I (just a job title, still a programmer)
MasterCard International
St. Louis, Missouri
```

###### ↳ ↳ ↳ Re: Pointers Help in Vax Cobol

- **From:** "kevin digweed" <ua-author-6588872@usenetarchives.gap>
- **Date:** 1997-06-26T20:00:04+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-2f4fa8cb78-p4@usenetarchives.gap>`
- **In-Reply-To:** `<gap-2f4fa8cb78-p3@usenetarchives.gap>`
- **References:** `<867245887.18115@dejanews.com> <gap-2f4fa8cb78-p2@usenetarchives.gap> <gap-2f4fa8cb78-p3@usenetarchives.gap>`

```

Arnold Trembley wrote:
› This language has confused me for some time.  The first time I read
› "dereferencing a pointer" in an article about C or C++ programming a few
…[5 more quoted lines elided]…
› addressability to a storage area.  Is this the common meaning for this idiom?

I (from a C/C++ background) will use the term "dereferencing" to mean
accessing the data to which a pointer points. I've no idea where I
originally picked this meaning up from, of course :)

I guess you can think of it this way: a pointer is effectively a
reference to some other data (in general, implementations store the
machine address of that data, but that doesn't have to be the case
to call something "a pointer"). If you "DEreference" the pointer, you
are "removing the reference" (ie, getting at the data). If you
take the "reference" away from "reference to data" you end up with
"data". This is as opposed to "producing a bad reference", which is
what you take to mean dereferencing as.

I'm not sure what I've added to this discussion, other than a theory of
how the difference in meaning may have originated. I'd never thought of
the meaning you apply before, I can see arguments for both being
correct now! :)

› Would it mean something different to say you were "referencing a pointer"?

I guess "referencing a pointer" could mean taking a reference to a
pointer (ie, a pointer to a pointer) ?

Cheers,
Kev.
```

#### ↳ Re: Pointers Help in Vax Cobol

- **From:** "phase-q" <ua-author-13467915@usenetarchives.gap>
- **Date:** 1997-06-25T20:00:05+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-2f4fa8cb78-p5@usenetarchives.gap>`
- **In-Reply-To:** `<867245887.18115@dejanews.com>`
- **References:** `<867245887.18115@dejanews.com>`

```


› The compiler does not support set "address of" needed for the use of
› pointers. I need to be able to pass pointers to and from a C program.
›

have you tried

Call "C_Program" using by reference WS-PASSING-VARIABLE
giving ss-return.
```

#### ↳ Re: Pointers Help in Vax Cobol

- **From:** "cwes..." <ua-author-13502721@usenetarchives.gap>
- **Date:** 1997-06-25T20:00:06+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-2f4fa8cb78-p6@usenetarchives.gap>`
- **In-Reply-To:** `<867245887.18115@dejanews.com>`
- **References:** `<867245887.18115@dejanews.com>`

```

In article <867··.@dej··s.com>,
esn··.@tou··t.com wrote:
› 
› I am in need of a solution: How to use pointers in an older version of
› COBOL.
 
› How to use pointers depends more on the vendor than on the age.
 
 
› The particulars are: DEC VAX 6440 running VMS 5.5.2, using VAX COBOL
› 4.4-65, compiled by a Ver3 VAX COBOL 85 Compiler.
› 
› The compiler does not support set "address of" needed for the use of
› pointers.  I need to be able to pass pointers to and from a C program.

Passing pointers from VAX CoBOL to C is trivial.

Passing pointers from C to VAX CoBOL is not usually a problem because C
passes arguments by value, not by reference:

$ copy sys$input demo.c
int main(int argc, char* argv[])
{
char* pc="Hello, world!";
extern void COBOLSUB(char*);
COBOLSUB(pc);
return;
}
^Z
$ cc demo
$ copy sys$input cobolsub.cob
IDENTIFICATION DIVISION.
PROGRAM-ID. COBOLSUB.
DATA DIVISION.
LINKAGE SECTION.
01 IN-REC.
05 FILLER PIC X(13).
PROCEDURE DIVISION USING IN-REC.
0000-MAIN.
DISPLAY IN-REC.
EXIT PROGRAM.
^Z
$ cobol cobolsub
$ link demo,cobolsub
$ run demo
Hello, world!
$


There are cases that pose more difficulty, but they can be solved.
Please post an example of a call with which you are having trouble.


Christopher Westbury, Midtown Associates, 15 Fallon Place, Cambridge, MA 02138
```

##### ↳ ↳ Re: Pointers Help in Vax Cobol

- **From:** "andrew werden" <ua-author-14739961@usenetarchives.gap>
- **Date:** 1997-06-26T20:00:07+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-2f4fa8cb78-p7@usenetarchives.gap>`
- **In-Reply-To:** `<gap-2f4fa8cb78-p6@usenetarchives.gap>`
- **References:** `<867245887.18115@dejanews.com> <gap-2f4fa8cb78-p6@usenetarchives.gap>`

```

› Please post an example of a call with which you are having trouble.

My particular problem is that I've got a PL/1 program that is trying to
call a Cobol program passing a pointer BY REFERENCE.

Not a structure by reference. Not a pointer by value.

In the Vax manual, this looks like 'calling by descriptor', which
unfortunately, they claim NOT to support.

Time to hit the books and see what "lib$movc3" does....

/Andrew

*------------------------------------------------------------------*
*Andrew J Werden                        Princeton Junction Software*
*tel : 609.936.9248     awe··.@prn··t.com     fax : 609.275.7419*
*------------------------------------------------------------------*
```

###### ↳ ↳ ↳ Re: Pointers Help in Vax Cobol

- **From:** "cwes..." <ua-author-13502721@usenetarchives.gap>
- **Date:** 1997-06-27T20:00:08+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-2f4fa8cb78-p8@usenetarchives.gap>`
- **In-Reply-To:** `<gap-2f4fa8cb78-p7@usenetarchives.gap>`
- **References:** `<867245887.18115@dejanews.com> <gap-2f4fa8cb78-p6@usenetarchives.gap> <gap-2f4fa8cb78-p7@usenetarchives.gap>`

```

In article <33B··.@prn··t.com>,
Andrew Werden wrote:
› 
› In article <1997Jun26.095949.17789@giant>,
…[5 more quoted lines elided]…
› call a Cobol program passing a pointer BY REFERENCE.

This thread, entitled "Pointers Help in Vax Cobol", was started by a
fellow who wanted to pass pointers to and from C programs, and the
article you quote was addressed to that problem.

The nearby thread that you started, entitled "Pointers in VAX Cobol:
Help!" is of course about passing pointers by reference from a PL/I
program, and I posted an answer in that thread. If it hasn't reached
your cesspool, er, newsspool yet, email me for a copy.


› Not a structure by reference. Not a pointer by value.
›
› In the Vax manual, this looks like 'calling by descriptor', which
› unfortunately, they claim NOT to support.

Um, no, a descriptor is a VMS control block. When you call by
descriptor, the compiler creates a descriptor block in local storage and
then passes the descriptor by reference.

It's true that VAX CoBOL can not receive parameters by descriptor within
the language itself, but, like your problem, there is a workaround for it
if the situation ever arises.


Christopher Westbury, Midtown Associates, 15 Fallon Place, Cambridge, MA 02138
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
