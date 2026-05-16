[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# FASTSRT, COBOL II, SyncSort, VSE

_16 messages · 10 participants · 2000-04_

**Topics:** [`Compilers and vendors`](../topics.md#compilers)

---

### FASTSRT, COBOL II, SyncSort, VSE

- **From:** infocat@sprynet.com (Frank Swarbrick)
- **Date:** 2000-04-01T00:00:00
- **Newsgroups:** bit.listserv.vse-l,comp.lang.cobol
- **Message-ID:** `<38e66554.25614639@nntp.sprynet.com>`

```
Generally when we do internal sorts in our shop we use both input
procedure and output procedure.  Yesterday I had reason to use an
inpur procedure, but I used 'giving' for the output file.  The
compiler (VS COBOL II, for VSE) said it qualified for the 'fast sort'
option.  So I decided to use that.  It seemed to work the first time,
but on the second run I kept getting a bad SORT-RETURN from SyncSort
(for VSE, release 3.2).  The error seemed to be x08, which is
duplicate key on a write.

After some time wasted trying other things we came to the thought that
the file was being opened as I-O rather than as output, so all of the
original data in the file was still there.   To test this out I did an
open for output on the file followed by a close, and then the sort.
This worked fine.  I then removed that kludge and took out the FASTSRT
option.  This also worked fine!  So it looks like FASTSRT was the
problem.

Any thoughts?
Frank Swarbrick
home: infocat@sprynet.com / work: frank.swarbrick@efirstbank.com
"Ignorance and prejudice - and fear walk hand in hand" --Rush "Witch Hunt"
```

#### ↳ Re: FASTSRT, COBOL II, SyncSort, VSE

- **From:** Foodman <foodman123@aol.com>
- **Date:** 2000-04-01T00:00:00
- **Newsgroups:** bit.listserv.vse-l,comp.lang.cobol
- **Message-ID:** `<8c5t66$g3t$1@nnrp1.deja.com>`
- **References:** `<38e66554.25614639@nntp.sprynet.com>`

```
In article <38e66554.25614639@nntp.sprynet.com>,
infocat@sprynet.com (Frank Swarbrick) wrote:
> Generally when we do internal sorts in our shop we use both input
> procedure and output procedure.

Hi:

This prompts me to ask: do people still design systems using
sorts? And, if so, why? Or, is this just some old legacy stuff?

Thanks

Tony Dilworth


Sent via Deja.com http://www.deja.com/
Before you buy.
```

##### ↳ ↳ Re: FASTSRT, COBOL II, SyncSort, VSE

- **From:** "James J. Gavan" <jjgavan@home.com>
- **Date:** 2000-04-01T00:00:00
- **Newsgroups:** bit.listserv.vse-l,comp.lang.cobol
- **Message-ID:** `<38E68869.7EE47D14@home.com>`
- **References:** `<38e66554.25614639@nntp.sprynet.com> <8c5t66$g3t$1@nnrp1.deja.com>`

```


Foodman wrote:
> 
> In article <38e66554.25614639@nntp.sprynet.com>,
…[8 more quoted lines elided]…
> 
I don't know the mainframe world - but boy ! - I can see them coming
back at you on this one - example - would you want to index 68 MILLION
records as somebody mentioned recently, instead of sorting ???
Volume-wise just think of banking as a topic.

Jimmy
```

###### ↳ ↳ ↳ Re: FASTSRT, COBOL II, SyncSort, VSE

- **From:** "donald tees" <donald@willmack.com>
- **Date:** 2000-04-01T00:00:00
- **Newsgroups:** bit.listserv.vse-l,comp.lang.cobol
- **Message-ID:** `<8c68p6$j41$1@news.igs.net>`
- **References:** `<38e66554.25614639@nntp.sprynet.com> <8c5t66$g3t$1@nnrp1.deja.com> <38E68869.7EE47D14@home.com>`

```

James J. Gavan wrote in message <38E68869.7EE47D14@home.com>...
>
>Foodman wrote:
…[6 more quoted lines elided]…
>Volume-wise just think of banking as a topic.

Getting behind on your equipment again Jimmy?  I have told you over and over
again that you have to start buying a new machine every 24 hours.  My latest
wrist-watch could load that into RAM and do a bubble sort on it in under a
minute.  The channel capacity of it's cellular phone link would have trouble
loading it in less than 5 or 10 minutes, mind you, and the display leaves a
lot to be desired, but you'd be amazed at how they managed to disguise a
27.5 terabyte tape drive as the wrist band.   The only real problem is the
3.7 ton air-conditioning unit ...
```

##### ↳ ↳ Re: FASTSRT, COBOL II, SyncSort, VSE

- **From:** thaneH@softwaresimple.com (Thane Hubbell)
- **Date:** 2000-04-02T00:00:00
- **Newsgroups:** bit.listserv.vse-l,comp.lang.cobol
- **Message-ID:** `<38e6d9fd.129611310@news.cox-internet.com>`
- **References:** `<38e66554.25614639@nntp.sprynet.com> <8c5t66$g3t$1@nnrp1.deja.com>`

```
On Sat, 01 Apr 2000 22:28:37 GMT, Foodman <foodman123@aol.com> wrote:

>This prompts me to ask: do people still design systems using
>sorts? And, if so, why? Or, is this just some old legacy stuff?
>

April Fools right?

In the old days of RM COBOL before they had "SORT" we simulated it
using indexed files.  Maybe your experience is that sort is slow?
Older MicroFocus implementations were such.  Realia on the other hand
was LIGHTNING fast.  Fujitsu today has a good performing sort, and a
better one if you use their POWERBSORT.  There's LOTS of reasons to
use sort, but I won't get into it.  I'm convinced this was an April
fools joke.
```

##### ↳ ↳ Re: FASTSRT, COBOL II, SyncSort, VSE

- **From:** Ken Foskey <waratah@zip.com.au>
- **Date:** 2000-04-02T00:00:00
- **Newsgroups:** bit.listserv.vse-l,comp.lang.cobol
- **Message-ID:** `<38E6F2CE.175B24B4@zip.com.au>`
- **References:** `<38e66554.25614639@nntp.sprynet.com> <8c5t66$g3t$1@nnrp1.deja.com>`

```
Foodman wrote:
> 
> In article <38e66554.25614639@nntp.sprynet.com>,
…[7 more quoted lines elided]…
> sorts? And, if so, why? Or, is this just some old legacy stuff?

For consistently stored internal stuff, I agree.  For data from
foreign sources then sorting into account number order makes
processing more efficient.  FOr other stuff sequential is the best way
to process it.  Typically you add 15% just creating the index, so be
sure you need it first.

Thanks
Ken Foskey
http://www.zipworld.com.au/~waratah/
```

###### ↳ ↳ ↳ Re: FASTSRT, COBOL II, SyncSort, VSE - small digression

- **From:** docdwarf@clark.net ()
- **Date:** 2000-04-02T00:00:00
- **Newsgroups:** bit.listserv.vse-l,comp.lang.cobol
- **Message-ID:** `<WFIF4.16145$0o4.104259@iad-read.news.verio.net>`
- **References:** `<38e66554.25614639@nntp.sprynet.com> <8c5t66$g3t$1@nnrp1.deja.com> <38E6F2CE.175B24B4@zip.com.au>`

```
In article <38E6F2CE.175B24B4@zip.com.au>,
Ken Foskey  <waratah@zip.com.au> wrote:
>Foodman wrote:
>> 
…[14 more quoted lines elided]…
>sure you need it first.

Curious that you should mention this, Mr Foskey... please permit me a bit
of a digression.

On my present pig-of-a-contract She Who Signs My Timesheets demands that
*all* development (except for online, which is CICS) be done in
EasyTrieve... pfui!  I've taught myself the language and can manage most
tasks in it now but the other day I noticed something... curious.

The Task:  400K input recs (in three concatenated files), each 600 bytes,
each containing a 10-byte Transaction Num.  Take the Transaction Num, use
it for a primary key VSAM read, if rec exists use some data from the VSAM
file, write a report.

I trust this description is sufficient... anyhow, this thing ran for
thirty-eight minutes of wall time and swallowed 1.5 min of CPU.  I was
bored and had a few extra minutes so, just for laffs, I re-wrote the code,
*still* in EasyTrieve (pfui!), to sort the input files on Transaction Num,
sort the VSAM file to a flatfile on Transaction Num (all sorts were done
in EasyTrieve (pfui!) as well, it supports a kind of SORT INFILE TO
OUTFILE USING INREC-KEY statement) and then processing, in Easytrieve, in
a standard (oh... did I mention Easytrieve?  PFUI!) COBOL 101 'match the
update tape to the Master File and create a new Master' match/merge
fashion... *with* a loop controlled by GO TOs *but* adhering to modified
Yourdon rules in that the only GO TOs were to TOP-OF-LOOP and
BREAK-OUT-OF-LOOP.

The result ran in a bit less than half the wall time (18 vs. 38 min) and a
third of the CPU (.5 vs. 1.5 min).

DD
```

##### ↳ ↳ Re: FASTSRT, COBOL II, SyncSort, VSE

- **From:** docdwarf@clark.net ()
- **Date:** 2000-04-02T00:00:00
- **Newsgroups:** bit.listserv.vse-l,comp.lang.cobol
- **Message-ID:** `<EwyF4.16119$0o4.102969@iad-read.news.verio.net>`
- **References:** `<38e66554.25614639@nntp.sprynet.com> <8c5t66$g3t$1@nnrp1.deja.com>`

```
In article <8c5t66$g3t$1@nnrp1.deja.com>, Foodman  <foodman123@aol.com> wrote:
>In article <38e66554.25614639@nntp.sprynet.com>,
>infocat@sprynet.com (Frank Swarbrick) wrote:
…[6 more quoted lines elided]…
>sorts?

I have seen such things, aye.

>And, if so, why?

Oh, I *cannot* resist... perhaps because they learned how to do so
nimfty-scorg years ago and haven't learned anything new since.

DD
```

##### ↳ ↳ Re: FASTSRT, COBOL II, SyncSort, VSE

- **From:** infocat@sprynet.com (Frank Swarbrick)
- **Date:** 2000-04-02T00:00:00
- **Newsgroups:** bit.listserv.vse-l,comp.lang.cobol
- **Message-ID:** `<38e6c186.49155185@nntp.sprynet.com>`
- **References:** `<38e66554.25614639@nntp.sprynet.com> <8c5t66$g3t$1@nnrp1.deja.com>`

```
On Sat, 01 Apr 2000 22:28:37 GMT, Foodman <foodman123@aol.com> wrote:

>In article <38e66554.25614639@nntp.sprynet.com>,
>infocat@sprynet.com (Frank Swarbrick) wrote:
…[6 more quoted lines elided]…
>sorts? And, if so, why? Or, is this just some old legacy stuff?

It's a long story in this case, but...  Basically, I am reading input
from two DL/I databases, one for demand (checking) and one for
savings.  These are in order by bank, branch, and account number.  The
output VSAM KSDS is one file for all of the records (demand and
savings), in the same order with one exception:  I replace the actual
bank number with a generic bank number (000000001).

Now I will grant you that, since it is a KSDS, there seems to be
little reason for the sort.  But it's felt by my team leader that it
is more efficient this way, since it avoids CA/CI splits.  How much
better this is I really couldn't say...  Now that I think about it, we
do recreate the file daily, so having the sort is even less necessary.
Hmm.


Frank Swarbrick
home: infocat@sprynet.com / work: frank.swarbrick@efirstbank.com
"Ignorance and prejudice - and fear walk hand in hand" --Rush "Witch Hunt"
```

#### ↳ Re: FASTSRT, COBOL II, SyncSort, VSE

- **From:** "William M. Klein" <wmklein@nospam.ix.netcom.com>
- **Date:** 2000-04-01T00:00:00
- **Newsgroups:** bit.listserv.vse-l,comp.lang.cobol
- **Message-ID:** `<8c5rql$q4p$1@slb6.atl.mindspring.net>`
- **References:** `<38e66554.25614639@nntp.sprynet.com>`

```
Assuming that you mean VS COBOL II R3.2 (for VSE) - I will ignore how long it
has been since that was a supported product <G>.

However, is it possible that you have the same file named for both your USING
and GIVING files. (or in your case for in the INPUT procedure and the GIVING
phrase).  If so, then I think this might be your problem.
```

##### ↳ ↳ Re: FASTSRT, COBOL II, SyncSort, VSE

- **From:** infocat@sprynet.com (Frank Swarbrick)
- **Date:** 2000-04-02T00:00:00
- **Newsgroups:** bit.listserv.vse-l,comp.lang.cobol
- **Message-ID:** `<38e6c0c5.48962515@nntp.sprynet.com>`
- **References:** `<38e66554.25614639@nntp.sprynet.com> <8c5rql$q4p$1@slb6.atl.mindspring.net>`

```
On Sat, 1 Apr 2000 15:59:24 -0600, "William M. Klein"
<wmklein@nospam.ix.netcom.com> wrote:

>Assuming that you mean VS COBOL II R3.2 (for VSE) - I will ignore how long it
>has been since that was a supported product <G>.
…[3 more quoted lines elided]…
>phrase).  If so, then I think this might be your problem.

Hey, we've had COBOL for VSE for at least two years.  It just hasn't
been installed yet!  Don't look at me...

Anyway, your guess is definately not the case.  My input is two DL/I
databases.  As I said, it works fine once I eliminate the FASTSRT
option.

Thanks for the good effort, though!  :-)

Frank

>"Frank Swarbrick" <infocat@sprynet.com> wrote in message
>news:38e66554.25614639@nntp.sprynet.com...
…[23 more quoted lines elided]…
>

Frank Swarbrick
home: infocat@sprynet.com / work: frank.swarbrick@efirstbank.com
"Ignorance and prejudice - and fear walk hand in hand" --Rush "Witch Hunt"
```

#### ↳ Re: FASTSRT, COBOL II, SyncSort, VSE

- **From:** "Searcher" <mangogwr@bellsouth.net>
- **Date:** 2000-04-01T00:00:00
- **Newsgroups:** bit.listserv.vse-l,comp.lang.cobol
- **Message-ID:** `<teyF4.528$ps.368@news4.mia>`
- **References:** `<38e66554.25614639@nntp.sprynet.com>`

```
Was your 'GIVING' file a Keyed file?

(I presume so due to 'DUPE KEY'.
What was the access mode on the file?

FASTSRT ONLy changes who does the I/O.
W/O FASTSRT, even with USING/GIVING,  COBOL does the I/O
With FASTSRT, SORT does not return control to COBOl.

You see, INPUT / OUTPUT Procedure just specifies that
SORT is to use an INPUT (E15) or OUTPUT (E35) Exit Routine --
Your code.  W/O FASTSRT, the COBOL Object Program STILL
DOES THE PHYSICAL I/O for USING/GIVING!!!

Frank Swarbrick <infocat@sprynet.com> wrote in message
news:38e66554.25614639@nntp.sprynet.com...
> Generally when we do internal sorts in our shop we use both input
> procedure and output procedure.  Yesterday I had reason to use an
…[19 more quoted lines elided]…
>
```

##### ↳ ↳ Re: FASTSRT, COBOL II, SyncSort, VSE

- **From:** infocat@sprynet.com (Frank Swarbrick)
- **Date:** 2000-04-02T00:00:00
- **Newsgroups:** bit.listserv.vse-l,comp.lang.cobol
- **Message-ID:** `<38e6c405.49790400@nntp.sprynet.com>`
- **References:** `<38e66554.25614639@nntp.sprynet.com> <teyF4.528$ps.368@news4.mia>`

```
On Sat, 1 Apr 2000 21:24:45 -0800, "Searcher" <mangogwr@bellsouth.net>
wrote:

>Was your 'GIVING' file a Keyed file?
>
…[10 more quoted lines elided]…
>DOES THE PHYSICAL I/O for USING/GIVING!!!

It is a keyed file, yes.  (My reasoning for the sort given in a
previous message.)  The access is actually DYNAMIC.  I'll explain:

As I said previously, my input is two DL/I databases; savings and
demand.  Previously the program was run twice; once for each system.
There were two output VSAM KSDS files; again one for each system.  No
sort was involved because everything was in the same order.  After the
file was created it was closed, and then reopened as I-O.  Another
file (a sequential file, with the accounts not in any particular
order)  was read in.  We would then take the account number etc. and
use it as the key for a random read into the KSDS.  We would change
some information and then rewrite the record to the KSDS.

The key, BTW, is as follows:
    05  DDR-KEY.
        10  DDR-BANK    PIC s9(5) comp-3.
        10  DDR-BRANCH  PIC S9(3) comp-3.
        10  DDR-ACCOUNT  PIC S9(7) comp-3.

My goal is twofold:  1) To use a generic bank number of 00001 rather
than the one from the DL/I database, and 2) to process both the
savings followed by the demand and combine them in to one output file.

Anyway, this does seem to work when I don't use fast sort.  I'm sure
it would also work if I used no sort at all (because the output is a
KSDS).  I just would like to know, for my own edification, why it's
not working *with* fast sort.

Thanks for your input.

Frank Swarbrick
home: infocat@sprynet.com / work: frank.swarbrick@efirstbank.com
"Ignorance and prejudice - and fear walk hand in hand" --Rush "Witch Hunt"
```

#### ↳ Re: FASTSRT, COBOL II, SyncSort, VSE

- **From:** WOB Consulting <wobconsult@sprynet.com>
- **Date:** 2000-04-02T00:00:00
- **Newsgroups:** bit.listserv.vse-l,comp.lang.cobol
- **Message-ID:** `<8c63qr$n28$1@nnrp1.deja.com>`
- **References:** `<38e66554.25614639@nntp.sprynet.com>`

```
In article <38e66554.25614639@nntp.sprynet.com>,
infocat@sprynet.com (Frank Swarbrick) wrote:
> Generally when we do internal sorts in our shop we use both input
> procedure and output procedure. Yesterday I had reason to use an
…[18 more quoted lines elided]…
> "Ignorance and prejudice - and fear walk hand in hand" --Rush "Witch
Hunt"
>
>
Frank,
FWIW, there USED TO be problems in a VSE environment with the
USING/GIVING when sorting a variable length file (in the GIVING step).
It didn't matter whether in was SYNCSORT or DFSORT.
Have you checked IBMLINK for any reported problems and PTF resolutions ?
HTH....
WOB


Sent via Deja.com http://www.deja.com/
Before you buy.
```

##### ↳ ↳ Re: FASTSRT, COBOL II, SyncSort, VSE

- **From:** infocat@sprynet.com (Frank Swarbrick)
- **Date:** 2000-04-02T00:00:00
- **Newsgroups:** bit.listserv.vse-l,comp.lang.cobol
- **Message-ID:** `<38e6c348.49601000@nntp.sprynet.com>`
- **References:** `<38e66554.25614639@nntp.sprynet.com> <8c63qr$n28$1@nnrp1.deja.com>`

```
On Sun, 02 Apr 2000 00:21:57 GMT, WOB Consulting
<wobconsult@sprynet.com> wrote:

>In article <38e66554.25614639@nntp.sprynet.com>,
>infocat@sprynet.com (Frank Swarbrick) wrote:
…[28 more quoted lines elided]…
>Have you checked IBMLINK for any reported problems and PTF resolutions ?

Hmm, I was at first going to say that it wasn't a variable length
file, but actually it is.  The thing is, I don't have it defined as
one.  I have it defined as the length of the smallest record.  This is
because the variable part is a table of 0 to 20 transactions, but the
file is created daily with 0 transactions.

What is IBMLINK?  Probably my systems programmers know about it, but I
can't say for sure at the moment.  (I'm at home on a Saturday,
currently.)

Frank Swarbrick
home: infocat@sprynet.com / work: frank.swarbrick@efirstbank.com
"Ignorance and prejudice - and fear walk hand in hand" --Rush "Witch Hunt"
```

###### ↳ ↳ ↳ Re: FASTSRT, COBOL II, SyncSort, VSE

- **From:** Ken Foskey <waratah@zip.com.au>
- **Date:** 2000-04-02T00:00:00
- **Newsgroups:** bit.listserv.vse-l,comp.lang.cobol
- **Message-ID:** `<38E6F37C.1E101EB2@zip.com.au>`
- **References:** `<38e66554.25614639@nntp.sprynet.com> <8c63qr$n28$1@nnrp1.deja.com> <38e6c348.49601000@nntp.sprynet.com>`

```
Frank Swarbrick wrote:
> 
> What is IBMLINK?  Probably my systems programmers know about it, but
> I can't say for sure at the moment.  (I'm at home on a Saturday,
> currently.)
> 

IBM link is the IBM help desk system that the systems programmers use.
They typically keep it to themselves though.

Thanks
Ken Foskey
http://www.zipworld.com.au/~waratah/
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
