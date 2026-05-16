[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Total # of Records Problem.

_9 messages · 8 participants · 2000-06_

---

### Total # of Records Problem.

- **From:** "Awais Baig" <awais22@khi.comsats.net.pk>
- **Date:** 2000-06-04T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8hdnh9$119a$2@news.interpacket.net>`

```
is there any command in microfocus cobol to calculate
total no. of records in the file.
actually i have program which process the complete
file, but the user should know how much time it will
ake or how much percentage is completed.
if i know the total no of records before
start process then it will be
very much easier to calculate the percentage
completed. If i use "read next at end of file" and
add 1 in a counter then i know the total no of records
but it will take too much time. if anyone knows any procedure
to solve this problem please let know.
```

#### ↳ Re: Total # of Records Problem.

- **From:** thaneH@softwaresimple.com (Thane Hubbell)
- **Date:** 2000-06-04T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<393a6ebf.310319611@news.cox-internet.com>`
- **References:** `<8hdnh9$119a$2@news.interpacket.net>`

```
Where I last worked the solution was to have a header record in each
file, with a low-value key.  In this record was kept the file record
count.  When a record was added, the count was incremented.  When one
was deleted, the count was decremented.


On Sun, 4 Jun 2000 16:45:47 +0500, "Awais Baig"
<awais22@khi.comsats.net.pk> wrote:

>is there any command in microfocus cobol to calculate
>total no. of records in the file.
…[11 more quoted lines elided]…
>

---
Try a better search engine:  http://www.google.com
My personal web site: http://www.geocities.com/Eureka/2006/
```

##### ↳ ↳ Re: Total # of Records Problem.

- **From:** Charles Haatvedt Jr. <clastname@nospam.com>
- **Date:** 2000-06-04T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<MPG.13a46bc510a77a2f9896cd@news>`
- **References:** `<8hdnh9$119a$2@news.interpacket.net> <393a6ebf.310319611@news.cox-internet.com>`

```
If the file being processed is a sequential file, one possible solution 
is to add another output file to the process which creates it. The 
additional file would have control counts, We have this as a standard in 
just about all of our programs. This is accomplished via a small 
subroutine which creates the control report from a passed table of 
control counters and descriptions...

Then in any process which reads the file in question, you could also read 
the control report file from the job which created the file in 
question...    this should give you the information you need

				hope this helps.....

                              chuck haatvedt


In article <393a6ebf.310319611@news.cox-internet.com>, 
thaneH@softwaresimple.com says...
> Where I last worked the solution was to have a header record in each
> file, with a low-value key.  In this record was kept the file record
…[25 more quoted lines elided]…
> 
```

#### ↳ Re: Total # of Records Problem.

- **From:** Ken Foskey <waratah@zip.com.au>
- **Date:** 2000-06-05T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<393ADC48.B38A4621@zip.com.au>`
- **References:** `<8hdnh9$119a$2@news.interpacket.net>`

```
Awais Baig wrote:
> 
> is there any command in microfocus cobol to calculate
…[10 more quoted lines elided]…
> to solve this problem please let know.

Take a directory listing and find out how many bytes there are. 
Divide this by the record length (plus 2 on DOS, plus 1 on Unix). 
This will give you the answer fairly quickly.

Now your challenge is to find the directory size, this is compiler
dependant.

Thanks
Ken Foskey
http://www.zipworld.com.au/~waratah/
```

##### ↳ ↳ Re: Total # of Records Problem.

- **From:** "Paddy Coleman" <paddy.coleman@merant.com>
- **Date:** 2000-06-05T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8hfn7j$28u$1@hyperion.mfltd.co.uk>`
- **References:** `<8hdnh9$119a$2@news.interpacket.net> <393ADC48.B38A4621@zip.com.au>`

```
Awais,

If you are using Net Express 3.0 or later then you can use the following
method for indexed files:

...
select testfile assign ...
   organization indexed
   access mode dynamic
   record key is ...
...
fd  testfile.

01  tf-record                        pic x(20).
...
working-storage section.

01  ws-rec-count                  pic x(2) comp-x.

linkage section.

01  ls-fcd.
copy "xfhfcd.cpy".

procedure division.
     ...
     open i-o testfile.
     set address ls-fcd to address of fh--fcd of testfile.
     move fcd-relative-key to ws-rec-count.
     ...

Hope this helps.

Paddy Coleman
Manager, E-Business Support, EMEA
MERANT International.

Ken Foskey <waratah@zip.com.au> wrote in message
news:393ADC48.B38A4621@zip.com.au...
> Awais Baig wrote:
> >
…[22 more quoted lines elided]…
> http://www.zipworld.com.au/~waratah/
```

###### ↳ ↳ ↳ Re: Total # of Records Problem.

- **From:** "Joshua Seltzer" <jseltzer@larich.com>
- **Date:** 2000-06-05T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8hg4jn$a6e$1@tracy.nacs.net>`
- **References:** `<8hdnh9$119a$2@news.interpacket.net> <393ADC48.B38A4621@zip.com.au> <8hfn7j$28u$1@hyperion.mfltd.co.uk>`

```
Does this method work with Merant Micro Focus IDX format 3 or 4 or 8?
Is this supported under OCDS on UNIX v4.1.30 or Server Express?

Paddy Coleman wrote in message <8hfn7j$28u$1@hyperion.mfltd.co.uk>...
>Awais,
>
…[63 more quoted lines elided]…
>
```

###### ↳ ↳ ↳ Re: Total # of Records Problem.

_(reply depth: 4)_

- **From:** "Paddy Coleman" <paddy.coleman@merant.com>
- **Date:** 2000-06-05T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8hgf8m$4p3$1@hyperion.mfltd.co.uk>`
- **References:** `<8hdnh9$119a$2@news.interpacket.net> <393ADC48.B38A4621@zip.com.au> <8hfn7j$28u$1@hyperion.mfltd.co.uk> <8hg4jn$a6e$1@tracy.nacs.net>`

```
Joshua,

This method should work on file formats 3, 4 and 8 on NE30+.  It will not
work on OCDS but should be fine on Server Express.  Another point, this
method will only work on files created with NE30+ and SE.

Hope this helps.

Paddy Coleman
Manager, E-Business Support, EMEA
MERANT International.


Joshua Seltzer <jseltzer@larich.com> wrote in message
news:8hg4jn$a6e$1@tracy.nacs.net...
> Does this method work with Merant Micro Focus IDX format 3 or 4 or 8?
> Is this supported under OCDS on UNIX v4.1.30 or Server Express?
…[69 more quoted lines elided]…
>
```

###### ↳ ↳ ↳ Re: Total # of Records Problem.

- **From:** Howard Brazee <howard.brazee@cusys.edu>
- **Date:** 2000-06-05T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<393BA755.432D8797@cusys.edu>`
- **References:** `<8hdnh9$119a$2@news.interpacket.net> <393ADC48.B38A4621@zip.com.au> <8hfn7j$28u$1@hyperion.mfltd.co.uk>`

```
I would explore to see if you can ask your operating system how many
records you have.  Maybe you can run an API to see the current file size
and then divide by your record length.  What OS are you using?
```

###### ↳ ↳ ↳ Re: Total # of Records Problem.

_(reply depth: 4)_

- **From:** Richard Plinston <riplin@Azonic.co.nz>
- **Date:** 2000-06-06T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<393C9BFC.7E1C@Azonic.co.nz>`
- **References:** `<8hdnh9$119a$2@news.interpacket.net> <393ADC48.B38A4621@zip.com.au> <8hfn7j$28u$1@hyperion.mfltd.co.uk> <393BA755.432D8797@cusys.edu>`

```
Howard Brazee wrote:
> 
> I would explore to see if you can ask your operating system how many
> records you have.  Maybe you can run an API to see the current file size
> and then divide by your record length.  What OS are you using?

That would only work if the file was sequential and fixed length.  You
would also need to know of any record headers and/or trailers and of
file headers and of slack space at end of file.

With any file that allowed logical deletion of records this would fail.

I do know that MF Level II indexed files hold a 'last record' in the
.IDX file.  I have a C program which I wrote (decades ago it seems) that
will display key details, record size etc. But it must scan the data
file to count the undeleted records.
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
