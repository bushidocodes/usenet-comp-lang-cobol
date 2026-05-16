[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Corrupt Index Files with FileShare

_8 messages · 5 participants · 2000-01_

---

### Corrupt Index Files with FileShare

- **From:** Stefan.Meyer@Triumph-international.de
- **Date:** 2000-01-06T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<851qom$hus$1@nnrp1.deja.com>`

```
Hi all,

I'm sitting at the moment in Ljubljana (Slowenia) and I'm wondering why I get
corrupt index files??

Our application accesses all files thru FileShare, which is really good
running and gets restarted every night to improve performance....

After some minutes one of our main files is getting corrupt. After rebuilding
the file using fhrebuild, everything is working again.

I don't know if other files are getting corrupt, too... but I have to find
out.

We're using MF Cobol V 4.1 running on Siemens RM 400 with Unix 5.43 C40.

We don't use FS in other countries and everything is working having no 
corrupt indexes....

Is this a known problem?

Does fhrebuild use FileShare as well?

If not, which filehandler is used by fhredir?

How can I avoid corrupt index files, when all programs are using the same
file declarations (copy books)?

Thanks for any hints ....

Stefan Meyer




Sent via Deja.com http://www.deja.com/
Before you buy.
```

#### ↳ Re: Corrupt Index Files with FileShare

- **From:** "Rick Price" <rick@hpd.co.uk>
- **Date:** 2000-01-06T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<85270h$s63$1@starburst.uk.insnet.net>`
- **References:** `<851qom$hus$1@nnrp1.deja.com>`

```
How often do you reorganise your data? How often do the other sites?

One thing that we came across which corrupted an index was too many deleted
records.  This was on hp-ux using MF COBOL 4.0 so it may not apply to you.
Also it wasn't under FileShare.

I can't remember the exact details but I believe that we found that if a
file contained more than 64k deleted records,  MF processing could corrupt
the index.   I assume that MF keeps track of deleted records for reuse using
a 2 byte binary field but it doesn't check whether this field is full.

We tested this by writing a simple index file containing 70k records where
the key (and data) was just the record number.   We then started deleting
records until the index was corrupted.  Then we looked at what records were
left.

Hope this helps.

Rick

<Stefan.Meyer@Triumph-international.de> wrote in message
news:851qom$hus$1@nnrp1.deja.com...
> Hi all,
>
> I'm sitting at the moment in Ljubljana (Slowenia) and I'm wondering why I
get
> corrupt index files??
>
…[3 more quoted lines elided]…
> After some minutes one of our main files is getting corrupt. After
rebuilding
> the file using fhrebuild, everything is working again.
>
…[25 more quoted lines elided]…
> Before you buy.
```

##### ↳ ↳ Re: Corrupt Index Files with FileShare

- **From:** "James J. Gavan" <jjgavan@home.com>
- **Date:** 2000-01-08T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3876E2B8.16F72CC3@home.com>`
- **References:** `<851qom$hus$1@nnrp1.deja.com> <85270h$s63$1@starburst.uk.insnet.net>`

```


Rick Price wrote:
> 
> How often do you reorganise your data? How often do the other sites?
> 
> One thing that we came across which corrupted an index was too many deleted
> records.  This was on hp-ux using MF COBOL 4.0 so it may not apply to you.

Rick,

You found the problem - but more to the point did M/F provide a solution
?

Jimmy
```

##### ↳ ↳ Re: Corrupt Index Files with FileShare

- **From:** Stefan.Meyer@Triumph-international.de
- **Date:** 2000-01-10T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<85c5b2$n31$1@nnrp1.deja.com>`
- **References:** `<851qom$hus$1@nnrp1.deja.com> <85270h$s63$1@starburst.uk.insnet.net>`

```
In article <85270h$s63$1@starburst.uk.insnet.net>,
  "Rick Price" <rick@hpd.co.uk> wrote:
> How often do you reorganise your data? How often do the other sites?

These datas are reorganized once a week as all other countries do. And
all other countries have much more data.

>
> One thing that we came across which corrupted an index was too many
deleted
> records.  This was on hp-ux using MF COBOL 4.0 so it may not apply to
you.

Oops. Nice information. I will check if this is the reason.


> Also it wasn't under FileShare.
>

> I can't remember the exact details but I believe that we found that
if a
> file contained more than 64k deleted records,  MF processing could
corrupt
> the index.   I assume that MF keeps track of deleted records for
reuse using
> a 2 byte binary field but it doesn't check whether this field is full.
>
> We tested this by writing a simple index file containing 70k records
where
> the key (and data) was just the record number.   We then started
deleting
> records until the index was corrupted.  Then we looked at what
records were
> left.

What does it mean: 64K deleted records? Is this the amount of deleted
records or the size of all deleted records? I assume amount...

Thanks for the details. I will check it out (also reading the books)
and give some feedback.

Bye - Stefan Meyer


Sent via Deja.com http://www.deja.com/
Before you buy.
```

###### ↳ ↳ ↳ Re: Corrupt Index Files with FileShare

- **From:** "Russell Styles" <RWSTYLES@COMPUSERVE.COM>
- **Date:** 2000-01-11T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<85ejnv$86r$1@ssauraab-i-1.production.compuserve.com>`
- **References:** `<851qom$hus$1@nnrp1.deja.com> <85270h$s63$1@starburst.uk.insnet.net> <85c5b2$n31$1@nnrp1.deja.com>`

```
    Some comments:

1.  Try looking at the rebuild utility to see if it has a non invasive
option
to detect file type (Ie /I).

2.  Deleted records are reused when adding records to the file, if
deleted records are present.  Files with variable length records or
compressed data are more complex, but the principle is the same.

    However, an ordinary "rebuild", in which the data portion is not changed
will "lose" deleted records, ie the disk space will never be reused.
However
this should avoid overflowing the deleted record index.

    I am not responsible if MF or C-tree upgrades this function.


3.  Another problem that can cause corruption (error 9-047 if lucky) is too
many
records with same alternate key, when duplicates are allowed.  If you truely
have
70,000 records with the same exact key, you might consider having the
program
replace that key with all zeroes or all spaces.  Than use the sparse key
function to cause those records to be skipped in that key.

    Or upgrade file type.




<Stefan.Meyer@Triumph-international.de> wrote in message
news:85c5b2$n31$1@nnrp1.deja.com...
> In article <85270h$s63$1@starburst.uk.insnet.net>,
>   "Rick Price" <rick@hpd.co.uk> wrote:
…[43 more quoted lines elided]…
> Before you buy.
```

#### ↳ Re: Corrupt Index Files with FileShare

- **From:** kennzo@aol.com (Kennzo)
- **Date:** 2000-01-06T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<20000106103005.03567.00000035@ng-fx1.aol.com>`
- **References:** `<851qom$hus$1@nnrp1.deja.com>`

```
Would make sure you use the directive
Set writethrough      when using index files
```

##### ↳ ↳ Re: Corrupt Index Files with FileShare

- **From:** Stefan.Meyer@Triumph-international.de
- **Date:** 2000-01-10T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<85c5fp$nar$1@nnrp1.deja.com>`
- **References:** `<851qom$hus$1@nnrp1.deja.com> <20000106103005.03567.00000035@ng-fx1.aol.com>`

```
In article <20000106103005.03567.00000035@ng-fx1.aol.com>,
  kennzo@aol.com (Kennzo) wrote:
> Would make sure you use the directive
> Set writethrough      when using index files
>

I'll give it a try...(after reading the books, what it means,
sideeffects and so one)

bye - Stefan Meyer


Sent via Deja.com http://www.deja.com/
Before you buy.
```

#### ↳ Re: Corrupt Index Files with FileShare

- **From:** Stefan.Meyer@Triumph-international.de
- **Date:** 2000-01-10T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<85d400$cuv$1@nnrp1.deja.com>`
- **References:** `<851qom$hus$1@nnrp1.deja.com>`

```
In article <851qom$hus$1@nnrp1.deja.com>,
  Stefan.Meyer@Triumph-international.de wrote:
> Hi all,
>
> I'm sitting at the moment in Ljubljana (Slowenia) and I'm wondering
why I get
> corrupt index files??

I hopefully found the error: The filetype of the accessed file was
different to other countries. The filetype was MF and we always use C-
ISAM (the original file has been created with WorkBench for Windows and
than copied to the Unix filesystem :-( ). So I used fhconvert to
convert the filetype to C-ISAM and everything should be working....I
hope.

Question: Has anyone a small program to detect filetypes?

bye - Stefan Meyer


Sent via Deja.com http://www.deja.com/
Before you buy.
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
