[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Sorting a file w/o SORT verb

_7 messages · 7 participants · 2000-08_

**Topics:** [`VSAM, files, sorting`](../topics.md#files)

---

### Sorting a file w/o SORT verb

- **From:** Eclipse <eclipse@advalvas.be>
- **Date:** 2000-08-02T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<39884021.D1F51B5F@advalvas.be>`

```
Hi,

i would like to sort by name a sequential file without the SORT verb.

sequ file entries :

01 ident pic 9 (4)
01 Name pic a (20)




My idea was to open that file, get every entry one by one and placing
them in an indexed file.

My problem is to place them in the right order. I wanted to START the
indexed file with the key = name got from the seq file . If it doesn't
exist, write the entry. If it already exists, do nothing

Where will he write the entry after done the START ?
```

#### ↳ Re: Sorting a file w/o SORT verb

- **From:** "Jerry P" <jerryp@bisusa.com>
- **Date:** 2000-08-02T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<Ok6i5.128$l36.79859@nnrp1.sbc.net>`
- **References:** `<39884021.D1F51B5F@advalvas.be>`

```
Forget START. Neither you nor the ISAM routines care whether the
record already exists.

OPEN OUTPUT ISAM-FILE. *>Create empty ISAM file
CLOSE ISAM-FILE.
OPEN I-O ISAM-FILE.      *> Open for random writing
PERFORM WITH NO LIMIT
   READ INPUT-FILE AT END EXIT PERFORM END-READ
   WRITE ISAM-REC FROM INPUT-REC      *> If the record already exists,
no foul.
   END-PERFORM.
CLOSE INPUT-FILE.
CLOSE ISAM-FILE.
OPEN INPUT-FILE.
PERFORM WITH NO LIMIT
   READ ISAM-FILE NEXT AT END EXIT PERFORM END-READ    *> read ISAM
file sequentially
   WRITE OUTPUT-FILE FROM ISAM-REC
   END-PERFORM.
CLOSE ISAM-FILE.
CLOSE OUTPUT-FILE.


"Eclipse" <eclipse@advalvas.be> wrote in message
news:39884021.D1F51B5F@advalvas.be...
> Hi,
>
> i would like to sort by name a sequential file without the SORT
verb.
>
> sequ file entries :
…[7 more quoted lines elided]…
> My idea was to open that file, get every entry one by one and
placing
> them in an indexed file.
>
> My problem is to place them in the right order. I wanted to START
the
> indexed file with the key = name got from the seq file . If it
doesn't
> exist, write the entry. If it already exists, do nothing
>
> Where will he write the entry after done the START ?
>
>
```

#### ↳ Re: Sorting a file w/o SORT verb

- **From:** WDS@WDS.WDS.5 (WDS)
- **Date:** 2000-08-02T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<39888693.6592192@news1.frb.gov>`
- **References:** `<39884021.D1F51B5F@advalvas.be>`

```
On Wed, 02 Aug 2000 15:35:57 GMT, Eclipse wrote:

>i would like to sort by name a sequential file without the SORT verb.
[various snippages]

>My idea was to open that file, get every entry one by one and placing
>them in an indexed file.

>My problem is to place them in the right order. I wanted to START the
>indexed file with the key = name got from the seq file [...]

You can sort a file by writing its records to an indexed file, and
then re-reading the indexed file into wherever you want the records.
Define the indexed file's record key to be your desired sort key.

You don't need to worry about placing the records in order into the
indexed file.  The concept of how records are later retrieved from the
indexed file will take care of this for you.

You also don't need to worry about STARTing the file, where it is
after you finish, or any of that.  First, create a new indexed file,
write all of your records into the indexed file, and close the indexed
file.  Then, open the indexed file input in the sequential access
mode, and read the records in sequential order.

That said, there are some things to consider.

  �  On most systems, this is a *very* slow, inefficient method
     of sorting a file.  It probably will also impose a large
     burden on the system with respect to the performance of any
     other programs that are running.

  �  This method assumes that all of your records contain unique
     sort keys.  If not, then you will need to add an increasing
     sequential number to your record key, so that each record will
     have a unique key.

  �  In most implementations, you will be limited to "sorting" the
     file in increasing sequence only.
```

#### ↳ Re: Sorting a file w/o SORT verb

- **From:** Binyamin Dissen <postingid@dissensoftware.com>
- **Date:** 2000-08-03T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<rcejos8pdmadgtqvca7robu1eqq20shr6h@4ax.com>`
- **References:** `<39884021.D1F51B5F@advalvas.be>`

```
On Wed, 02 Aug 2000 15:35:57 GMT Eclipse <eclipse@advalvas.be> wrote:

:>i would like to sort by name a sequential file without the SORT verb.

:>sequ file entries :

:>01 ident pic 9 (4)
:>01 Name pic a (20)

:>My idea was to open that file, get every entry one by one and placing
:>them in an indexed file.

Why on earth would you try that approach?

I would suspect that even a bubble sort would be degrees of speed faster.

   [ snipped ]
```

#### ↳ Re: Sorting a file w/o SORT verb

- **From:** piasa_bird@my-deja.com
- **Date:** 2000-08-03T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8mcofn$ev1$1@nnrp1.deja.com>`
- **References:** `<39884021.D1F51B5F@advalvas.be>`

```
In article <39884021.D1F51B5F@advalvas.be>,
  Eclipse <eclipse@advalvas.be> wrote:

Try looking at this site.

http://www.etk.com/papers/sorting/sorting.htm#combsort

A simple bubblesort works on small files.

just compare 2 records in a table and move the lowest value up one like
bubbles floating to the surface. when you go all the way thru the table
without moving anything you are done.


> Hi,
>
…[16 more quoted lines elided]…
>


Sent via Deja.com http://www.deja.com/
Before you buy.
```

#### ↳ Re: Sorting a file w/o SORT verb

- **From:** "pwmeister" <pwm@nomail.se>
- **Date:** 2000-08-03T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8mb648$8k3$1@news1.enator.se>`
- **References:** `<39884021.D1F51B5F@advalvas.be>`

```
please, what cobol and what platform do you use.


Eclipse wrote in message <39884021.D1F51B5F@advalvas.be>...
>Hi,
>
…[18 more quoted lines elided]…
>
```

#### ↳ Re: Sorting a file w/o SORT verb

- **From:** Howard Brazee <howard@brazee.net>
- **Date:** 2000-08-03T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<39896DD4.AB86DA63@brazee.net>`
- **References:** `<39884021.D1F51B5F@advalvas.be>`

```
Eclipse wrote:
> 
> Hi,
> 
> i would like to sort by name a sequential file without the SORT verb.

I would suggest then an external sort, or copying your file to an
indexed file.

That is, unless this is homework, in which case, I would suggest that
you search the web for sort algorithms and learn how to do a comb sort.

I have occasionally coded in sorts when I create a table from data
within my program.  The next standard will make this unnecessary.  This
didn't sound like your request, so I am guessing this is homework (which
is why my answer is general).  If I am mistaken, I am curious to why you
want to do this.

 
> sequ file entries :
> 
…[10 more quoted lines elided]…
> Where will he write the entry after done the START ?
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
