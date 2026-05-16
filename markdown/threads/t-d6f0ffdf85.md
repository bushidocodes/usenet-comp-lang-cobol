[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Search a GDD

_12 messages · 8 participants · 2005-10_

---

### Search a GDD

- **From:** "Praveen" <praveen.unnithan@gmail.com>
- **Date:** 2005-10-18T01:41:19-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1129624879.794819.54760@g43g2000cwa.googlegroups.com>`

```
Hi ,

I am newbie and I came across a scenario where I had to search for a
string in a GDG, and see if it is occuring in any of the GDG version. I
failed to find any utility for that.

Is there any way I can do this?

I am stuck. Please help me.

thanks in Advance.

Regards,
Praveen.
```

#### ↳ Re: Search a GDD

- **From:** docdwarf@panix.com ()
- **Date:** 2005-10-18T12:01:13+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<dj2o69$ikv$1@reader2.panix.com>`
- **References:** `<1129624879.794819.54760@g43g2000cwa.googlegroups.com>`

```
In article <1129624879.794819.54760@g43g2000cwa.googlegroups.com>,
Praveen <praveen.unnithan@gmail.com> wrote:
>Hi ,
>
>I am newbie and I came across a scenario where I had to search for a
>string in a GDG, and see if it is occuring in any of the GDG version. I
>failed to find any utility for that.

Which utilities did you consider for this task?

DD
```

#### ↳ Re: Search a GDD

- **From:** John Culleton <john@wexfordpress.com>
- **Date:** 2005-10-18T22:02:58+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<4audnfkjo5cR7MjeRVn-jQ@adelphia.com>`
- **References:** `<1129624879.794819.54760@g43g2000cwa.googlegroups.com>`

```
Praveen wrote:

> Hi ,
> 
…[11 more quoted lines elided]…
> Praveen.

What is a GDG?

Whst is your computer environment (OS)?
```

##### ↳ ↳ Re: Search a GDD

- **From:** Dave <MyFakeEmail@EndSpam.com>
- **Date:** 2005-10-18T22:24:57-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<HvCdnYvPEaYUIcjeRVn_vA@giganews.com>`
- **References:** `<1129624879.794819.54760@g43g2000cwa.googlegroups.com> <4audnfkjo5cR7MjeRVn-jQ@adelphia.com>`

```
> What is a GDG?

Generation Data Group.

You can keep multiple generations of files using a single file name. 
The current generation is (0). The previous (-1), the
one before that (-2). A new one is (+1). 
As in: MY.FILENAME(0) MY.FILENAME(-2) MY.FILENAME(+1) and so on. 

PC's have nothing so convenient and simple.
```

###### ↳ ↳ ↳ Re: Search a GDD

- **From:** Arnold Trembley <arnold.trembley@worldnet.att.net>
- **Date:** 2005-10-19T04:10:21+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<NGj5f.155998$qY1.54805@bgtnsc04-news.ops.worldnet.att.net>`
- **In-Reply-To:** `<HvCdnYvPEaYUIcjeRVn_vA@giganews.com>`
- **References:** `<1129624879.794819.54760@g43g2000cwa.googlegroups.com> <4audnfkjo5cR7MjeRVn-jQ@adelphia.com> <HvCdnYvPEaYUIcjeRVn_vA@giganews.com>`

```


Dave wrote:

>>What is a GDG?
> 
…[8 more quoted lines elided]…
> PC's have nothing so convenient and simple. 

You can also reference all generations of a generation data group by 
specifying the base dataset name without a generation number.

I have even seen batch jobs that created the +1 generation of a file, 
and in a subsequent step also created the +2 generation!  I have also 
seen GDG datasets alternating between tape and disk.

In MVS/OS390/zOS a dataset name can be a maximum of 44 charaters, and 
consists of 'nodes' separated by periods.  Each node is maximum of 
eight characters.  A dataset name can have more than 5 nodes, but the 
maximum length of 44 bytes cannot be exceeded.

The actual generation number is the final node of the dataset name, 
and it has the format "G0000V00", sometimes called the "Goo-Voo" number.

I used to have to access old GDG datasets that had "fallen out of the 
catalog".  I had to specify the real dataset name with explicit 
goo-voo number, something "PROD.WEEKLY.BILLING.FILE.G3127V00", instead 
of "PROD.WEEKLY.BILLING.FILE(-181)".
```

###### ↳ ↳ ↳ Re: Search a GDD

- **From:** John Culleton <john@wexfordpress.com>
- **Date:** 2005-10-19T12:43:52+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<K-mdnSiP5fKY3cveRVn-vg@adelphia.com>`
- **References:** `<1129624879.794819.54760@g43g2000cwa.googlegroups.com> <4audnfkjo5cR7MjeRVn-jQ@adelphia.com> <HvCdnYvPEaYUIcjeRVn_vA@giganews.com>`

```
Dave wrote:

>> What is a GDG?
> 
…[7 more quoted lines elided]…
> PC's have nothing so convenient and simple.

Ah yes, I remember that Univac had a similar facility in their editor
program years ago. It tracked the deltas of the file. That was for source
code of course. For data files it is easy to store backup copies. However
that eats up storage space, as compared to a system that saves and reuses
deltas.

There is no exact analog to Generational Data Sets afaik in the world of
personal computers. But for source code there are the revision control
system (rcs) and the Concurrent Versions System (cvs) on my PC, which runs
Linux of course. 

The text editor Gvim runs on most desktop computer OS'. It automatically
keeps a backup copy of the previous version. It would not take much work to
automatically rename that copy when the program exits. Again storage space
would be an issue. 

The *nix tools grep etc. will find a string in a file or group of files,
which was the original question. So if one kept the current file and delta
files, one could search all them for a given string with 
grep "search string" MY_FILENAME*

with the current file named MY_FILENAME and the delta files named
MY_FILENAME01 MY_FILENAME02 etc.

The delta files can be generated easily with diff. The only restriction to
this approach is that the files would need to be of type ASCII rather than
type binary. Alternatively a transaction log file could be used to keep a
record of the changes. 

It is an interesting system design challenge.
```

###### ↳ ↳ ↳ Re: Search a GDD

_(reply depth: 4)_

- **From:** Arnold Trembley <arnold.trembley@worldnet.att.net>
- **Date:** 2005-10-20T05:32:51+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7_F5f.465293$5N3.143457@bgtnsc05-news.ops.worldnet.att.net>`
- **In-Reply-To:** `<K-mdnSiP5fKY3cveRVn-vg@adelphia.com>`
- **References:** `<1129624879.794819.54760@g43g2000cwa.googlegroups.com> <4audnfkjo5cR7MjeRVn-jQ@adelphia.com> <HvCdnYvPEaYUIcjeRVn_vA@giganews.com> <K-mdnSiP5fKY3cveRVn-vg@adelphia.com>`

```


John Culleton wrote:
> Dave wrote:
> 
…[24 more quoted lines elided]…
> It is an interesting system design challenge.

Generation Data Groups are not delta files.  Each generation is a 
whole file.  The simplest usage to imagine is a daily job that backs 
up your customer master file (for example), which changes every day. 
If you need to restore last Wednesday's file, you just restore from 
that backup generation.  No need to work with deltas.
```

###### ↳ ↳ ↳ Re: Search a GDD

_(reply depth: 5)_

- **From:** John Culleton <john@wexfordpress.com>
- **Date:** 2005-10-20T16:59:04+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<KM2dndfv5dDEUMreRVn-tw@adelphia.com>`
- **References:** `<1129624879.794819.54760@g43g2000cwa.googlegroups.com> <4audnfkjo5cR7MjeRVn-jQ@adelphia.com> <HvCdnYvPEaYUIcjeRVn_vA@giganews.com> <K-mdnSiP5fKY3cveRVn-vg@adelphia.com> <7_F5f.465293$5N3.143457@bgtnsc05-news.ops.worldnet.att.net>`

```
Arnold Trembley wrote:

> 
> 
…[35 more quoted lines elided]…
> 
Hmm---Easier to make and more convenient to restore than deltas, but uses
perhaps 100 times the space. 
But IBM sells hardware :<)
```

###### ↳ ↳ ↳ Re: Search a GDD

_(reply depth: 6)_

- **From:** Howard Brazee <howard@brazee.net>
- **Date:** 2005-10-20T12:03:19-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<clmfl11c5n35uvuqc40rb7qslg614kd9kn@4ax.com>`
- **References:** `<1129624879.794819.54760@g43g2000cwa.googlegroups.com> <4audnfkjo5cR7MjeRVn-jQ@adelphia.com> <HvCdnYvPEaYUIcjeRVn_vA@giganews.com> <K-mdnSiP5fKY3cveRVn-vg@adelphia.com> <7_F5f.465293$5N3.143457@bgtnsc05-news.ops.worldnet.att.net> <KM2dndfv5dDEUMreRVn-tw@adelphia.com>`

```
On Thu, 20 Oct 2005 16:59:04 +0000, John Culleton
<john@wexfordpress.com> wrote:

>> Generation Data Groups are not delta files.  Each generation is a
>> whole file.  The simplest usage to imagine is a daily job that backs
…[7 more quoted lines elided]…
>But IBM sells hardware :<)

When GDGs were invented, most datasets were on tape.  GDGs are still
more common on tapes (in my experience).   

The tape management system knows that MY.MONTHLY.FILE(-3) is currently
tape number 12345.   It knows that the GDG was set up to keep 13
generations of MY.MONTHLY.FILE cataloged and current, freeing up the
14th generation to be re-written.

Often generations are kept off-site and don't need to be pieced
together after a disaster, as they are complete datasets.
```

###### ↳ ↳ ↳ Re: Search a GDD

_(reply depth: 6)_

- **From:** Christopher Pomasl <pomasl-NOSpam@starband.net>
- **Date:** 2005-10-20T13:58:23-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<pan.2005.10.20.19.57.49.602694@starband.net>`
- **References:** `<1129624879.794819.54760@g43g2000cwa.googlegroups.com> <4audnfkjo5cR7MjeRVn-jQ@adelphia.com> <HvCdnYvPEaYUIcjeRVn_vA@giganews.com> <K-mdnSiP5fKY3cveRVn-vg@adelphia.com> <7_F5f.465293$5N3.143457@bgtnsc05-news.ops.worldnet.att.net> <KM2dndfv5dDEUMreRVn-tw@adelphia.com>`

```
On Thu, 20 Oct 2005 16:59:04 +0000, John Culleton wrote:

> Arnold Trembley wrote:
>> 
…[9 more quoted lines elided]…
> But IBM sells hardware :<)
Actually, it is more useful for getting and retaining transaction
information from day to day for a batching process.  Each generation of
the data set is independent from the others but ideally contain similar
data (but doesn't have, I think).

Each day the system may extract a batch of records into gdg.dataset(+1)
and the system would retain on disk the last 10 generations of that set of
data.  So the (0) data would be yesterdays batch, the (-1) from the day
before etc.  This prevents the current extraction from overwriting the
current set of data if there is a problem in the batch run.  So while you
are working on the problem for G0021V00, the system can generate the batch
input for today into G0022V00.

Now instead of needing to update the GooVoo numbers manually on a
daily/hourly/whatever basis, the GDG system (a part of VSAM) takes care of
incrementing the name for each iteration of the data. 

GDGs can be used in any number of ways but in my experience it is used
mostly for recurring sets of data that are different time period to time
period.

Chris
```

###### ↳ ↳ ↳ Re: Search a GDD

_(reply depth: 6)_

- **From:** Lawrence Greenwald <lgreenwa@cts.com>
- **Date:** 2005-10-20T23:57:58+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<lgreenwa-65CF7F.16573520102005@chiapp18.algx.net>`
- **References:** `<1129624879.794819.54760@g43g2000cwa.googlegroups.com> <4audnfkjo5cR7MjeRVn-jQ@adelphia.com> <HvCdnYvPEaYUIcjeRVn_vA@giganews.com> <K-mdnSiP5fKY3cveRVn-vg@adelphia.com> <7_F5f.465293$5N3.143457@bgtnsc05-news.ops.worldnet.att.net> <KM2dndfv5dDEUMreRVn-tw@adelphia.com>`

```
In article <KM2dndfv5dDEUMreRVn-tw@adelphia.com>,
 John Culleton <john@wexfordpress.com> wrote:

> Arnold Trembley wrote:
> 
…[40 more quoted lines elided]…
> But IBM sells hardware :<)

Just one thing to point out. If you do not include the generation number 
or relative generation (i.e., instead of MY.FILENAME(0), you simply have 
MY.FILENAME) in the dataset name, the system will attempt to read ALL 
the existing generations of the file - in reverse order of creation - 
that is it will first read the (0) generation, then the (-1) generation 
if it exists, then the (-2) if it exists, etc.

If you're trying to put things into chronological order, it will be up 
to you to sort them into correct sequence, for whatever purpose you need.

By the way, the max absolute generation is 9999 (ie, last level will be 
.G9999V00). Creating a (+1) generation at that point should create an 
absolute 1 generation (.G0001V00); it will never create a file as an 
absolute zero generation (.G0000V00).  I've never actually hit that 
situation, can anyone else confirm my hypothesis?

--LG
```

#### ↳ Re: Search a GDD

- **From:** Dave <MyFakeEmail@EndSpam.com>
- **Date:** 2005-10-18T22:08:43-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<F8CdnXBotNYmJcjeRVn_vA@giganews.com>`
- **References:** `<1129624879.794819.54760@g43g2000cwa.googlegroups.com>`

```
> Hi ,
> 
…[4 more quoted lines elided]…
> Is there any way I can do this?

I would use ISRSUPC. You can submit a batch search from 3.13 or 3.14.
I suggest you go to IBM.COM and download the ISPF User's Guides. They
have everything you need to know. In batch just put the dataset 
name without a relative GDG to read whole index. I'm pointing you
in the right direction. Finding out the details on your own will
be good education for you.
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
