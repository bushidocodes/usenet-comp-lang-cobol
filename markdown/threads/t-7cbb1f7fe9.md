[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Sort Procedure!!

_4 messages · 4 participants · 2000-07_

**Topics:** [`VSAM, files, sorting`](../topics.md#files)

---

### Sort Procedure!!

- **From:** "Andrew Lee" <alee@netactive.co.za>
- **Date:** 2000-07-19T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8l56vc$17dm$1@nnrp01.ops.uunet.co.za>`

```
I have a project for cobol.  I have to write a program that will get the
number of students and then ask for their student numbers.

The program must then sort the student numbers (selection sort), then it
must ask you to enter a number to search for.  The program must then do a
binary search for the number which the user entered.

here's the basic:

    accept total
    sort
    search until search number is "end"

my problem is that it doesnt work and I'm still at the beginning of my
course and don't know all that much.  It gets the total, maybe sorts, asks
for search number, but doesn't search properly.

If anyone has a program like this or would like to send me something like
it.  It is a short program.  I need something to work from.  My teacher is
totally useless.

Ryan
alee@netactive.co.za
```

#### ↳ Re: Sort Procedure!!

- **From:** docdwarf@clark.net ( NA)
- **Date:** 2000-07-19T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<5vqd5.7559$IZ1.57319@iad-read.news.verio.net>`
- **References:** `<8l56vc$17dm$1@nnrp01.ops.uunet.co.za>`

```
In article <8l56vc$17dm$1@nnrp01.ops.uunet.co.za>,
Andrew Lee <alee@netactive.co.za> wrote:
>I have a project for cobol.  I have to write a program that will get the
>number of students and then ask for their student numbers.

Please do your own homework.  If you want help with your homework then
please show what you've done.

DD
```

#### ↳ Re: Sort Procedure!!

- **From:** sff5ky@aol.comxxx123 (Sff5ky)
- **Date:** 2000-07-20T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<20000719212406.02132.00001904@nso-cr.aol.com>`
- **References:** `<8l56vc$17dm$1@nnrp01.ops.uunet.co.za>`

```
In article <8l56vc$17dm$1@nnrp01.ops.uunet.co.za>, "Andrew Lee"
<alee@netactive.co.za> writes:

>
>If anyone has a program like this or would like to send me something like
>it.  It is a short program.  I need something to work from.  My teacher is
>totally useless.
>

It might be helpful to show more of what you have tried.
Does your sort deal with an external file or an internal table?
If you are working with an internal table , as I would assume from
your mention of needing to do a binary search, you need to 
write your own sort routine to sort the table.  There has been 
mention of some vendors that have an extension to the language
that permits sorting of internal tables.
```

#### ↳ Re: Sort Procedure!!

- **From:** Charles Hammond <ceh1@cec.wustl.edu>
- **Date:** 2000-07-21T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<Pine.SOL.3.96.1000721125640.27532A-100000@hilton.cec.wustl.edu>`
- **References:** `<8l56vc$17dm$1@nnrp01.ops.uunet.co.za>`

```
Try reading the Book, what an idea, duh.

If all else fails write some code and then ask for help.  What a
remarkable Idea.

Put a display in the program so you know where it crashes.

Put the input in a table or a file?

Still pondering what a selection sort is? Never was too particular with
terms.  You just compare two items  and move the biggest one to the bottom
using a temporary field to hold the bottom one in while you move the top
one to the bottom, and then move the temp to the top.  You sort in a
loop.  Use a test field and turn it to true if you have to
move any fields, if it is false you exit the loop and everything is in
order, if it is try you keep doing the loop!

Perform table-sort-routine until sort-sw = 'f'.

Know what a bubble sort is?

I wrote a program in pascal that orders a table of 50 entries,
randomizes and then sorts them.  We used a bubble sort algorithm.
 There are faster sorting algorithms but they are more complex.

Charles Hammond 

On Wed, 19 Jul 2000, Andrew Lee wrote:

> I have a project for cobol.  I have to write a program that will get the
> number of students and then ask for their student numbers.
…[25 more quoted lines elided]…
>
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
