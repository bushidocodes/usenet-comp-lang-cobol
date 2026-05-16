[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# MicroFocus C-Isam Index Rebuild 9/037

_3 messages · 3 participants · 2004-12_

**Topics:** [`Compilers and vendors`](../topics.md#compilers) · [`VSAM, files, sorting`](../topics.md#files)

---

### MicroFocus C-Isam Index Rebuild 9/037

- **From:** salty_sohal@yahoo.com (Jonathan)
- **Date:** 2004-12-04T16:25:07-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<c95bb32e.0412041625.6b7b24b6@posting.google.com>`

```
Hi guys (and gals too),

Please excuse my ignorance I'm not a COBOLer, but I do have much
respect for what you do. (I'm lazy I write everything that I could
ever need in PERL)

So my problem is this... I'm dealing this old "Real World" accounting
system that has decided to trash one it's index files. I spent the
last day researching how to rebuild this index. I discovered I needed
to use the REBUILD.exe. According to microfocus online docs I can
restore an non corrupt idx file so that rebuild will know which keys
to build from. Great! (I thought I was homefree!) So I restore an old
idx and run:

xm rebuild PMRWRK00.dat

And I get:

***Error on input file - status 9/037 - records read = 0


After a little more digging I discover that this has something to do
with passwords/authentication. So now I am stumped, I don't know
anything about the system I am messing with except what I've read in
the past 24 hours (a lot but my brain is still indexing it) and as far
as I know there is no password associated with this app. It runs on
one persons computer and there is no security other than OS login.

Can somebody tell me what I need to do, or nudge me in the right
direction? Is there a way to subvert the password without breaking the
APP? (I'm assuming the APP knows the pasword since it writes to the
file)

Thanks alot,

Jonathan

P.S. I don't know if this will tell you anything helpful but I ran

xm rebuild Pmrwrk00.dat /f:c63d5

on the file with the restored index to see what kind of information I
could get...

XM  Micro Focus COBOL File Management Utility
Version a.b.cc Copyright (C) 1985-1996 Micro Focus Ltd.



        Index file validation. Version 1.0 (EARLY RELEASE)

        Selected  :  Check Data File
        Selected  :  Check Fsl Chain
        Selected  :  Check Fsl and Deleted Records Match
        Selected  :  Check Index Structure
        Selected  :  Check Index Entries and Data Match
        Selected  :  Check Key Values Match Data

IC008-W DATA AND IDX FILE CREATION TIMES INCONSISTENT


        File                             :   PMRWRK00.DAT

        Organization                     :   Indexed
        Open Status                      :     0/000
        Format                           :     IDX-3
        Recording Mode                   :     Fixed
        Compression                      :   Y [  1]
        Maximum Record Length            :       177
        Minimum Record Length            :       177
        Index Node Size                  :      1024
        Data  Created With Extfh Version :      8238
        Index Created With Extfh Version :      8238
        Last  Updated With Extfh Version :      8238

        Key Description:
          Key       Start     Length     Dupl     Key Comp
         0000           0         78      N          6
         0001          78         24      Y          7
         0002          12         62      Y          7

        Checking Data File :

        Checking Free Space List :
        Checking Free Space List Matches Deleted Records:
        Checking Index File :
          Key   0 :
          Key   1 :
          Key   2 :

        Checking Index Matches Data Record:
          Key   0 :
          Key   1 :
          Key   2 :


        Record Types Present In data File:.
        Type 1 =        0
        Type 2 =        0
        Type 3 =        1
        Type 4 =        0
        Type 5 =        0
        Type 6 =        0
        Type 7 =        0
        Type 8 =        0


        Total Number of User records in Data File       :          0
        Highest Duplicate Occurrence Value in Data File :          0


        Actual Data File Size                           :        316
        File Size Achievable by rebuilding              :        316

        Index Statistics  - Key Number :          0
        -------------------------------
        Highest Duplicate Occurrence Used               :          0
        (Highest Duplicate Occurrence Possible          :      65536)
        Current Index Tree Depth                        :          0
        Total Number of Nodes                           :          1
        Total Number of Leaf Nodes                      :          0
        Number of Bytes Saved By Leading Compression    :          0
        Number of Bytes Saved By Trailing Compression   :          0
        Number of Bytes Saved By Duplicate Compression  :          0
        Minimum Number of Bytes In a Node               :          2
        Maximum Number of Bytes In a Node               :          2
        Average Number of Bytes In a Node               :          2

        Index Statistics  - Key Number :          1
        -------------------------------
        Highest Duplicate Occurrence Used               :          0
        (Highest Duplicate Occurrence Possible          :      65536)
        Current Index Tree Depth                        :          0
        Total Number of Nodes                           :          1
        Total Number of Leaf Nodes                      :          0
        Number of Bytes Saved By Leading Compression    :          0
        Number of Bytes Saved By Trailing Compression   :          0
        Number of Bytes Saved By Duplicate Compression  :          0
        Minimum Number of Bytes In a Node               :          2
        Maximum Number of Bytes In a Node               :          2
        Average Number of Bytes In a Node               :          2

        Index Statistics  - Key Number :          2
        -------------------------------
        Highest Duplicate Occurrence Used               :          0
        (Highest Duplicate Occurrence Possible          :      65536)
        Current Index Tree Depth                        :          0
        Total Number of Nodes                           :          1
        Total Number of Leaf Nodes                      :          0
        Number of Bytes Saved By Leading Compression    :          0
        Number of Bytes Saved By Trailing Compression   :          0
        Number of Bytes Saved By Duplicate Compression  :          0
        Minimum Number of Bytes In a Node               :          2
        Maximum Number of Bytes In a Node               :          2
        Average Number of Bytes In a Node               :          2

        ******************************************
        *      File is OK                        *
        ******************************************
```

#### ↳ Re: MicroFocus C-Isam Index Rebuild 9/037

- **From:** "Charles W. Cribbs II" <charlescribbs@earthlink.net>
- **Date:** 2004-12-05T15:44:12+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<g1Gsd.4597$714.1183@newsread2.news.atl.earthlink.net>`
- **References:** `<c95bb32e.0412041625.6b7b24b6@posting.google.com>`

```
What microfocus is telling you is that it can't find the .idx file, which
you already new.  The rebuild utility makes the assumption that you have a
.idx file that has been corrupted and the rebuild will fix it.

If you haven't got the .idx file you are going to have to find out the
original file layout and the various keys that the file used to make up the
index.  Unless somebody has that information you are going to be out of luck
with that file.  What you might do see if they have an old back-up copy of
the data file and the .idx and that might give some clues as to what you
have to do.

If you want the big explanation of what all you have to do e-mail me back
and I can give you the long drawn out version.


"Jonathan" <salty_sohal@yahoo.com> wrote in message
news:c95bb32e.0412041625.6b7b24b6@posting.google.com...
> Hi guys (and gals too),
>
…[156 more quoted lines elided]…
>         ******************************************
```

#### ↳ Re: MicroFocus C-Isam Index Rebuild 9/037

- **From:** riplin@Azonic.co.nz (Richard)
- **Date:** 2004-12-05T10:07:36-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<217e491a.0412051007.6f311fe9@posting.google.com>`
- **References:** `<c95bb32e.0412041625.6b7b24b6@posting.google.com>`

```
salty_sohal@yahoo.com (Jonathan) wrote 

> xm rebuild PMRWRK00.dat

XM implies that it is DOS runtime.  1996 elsewhere indicates MF Cobol
version 3.4.  These things are useful to help solve the problem.
 
> And I get:
> 
> ***Error on input file - status 9/037 - records read = 0

> After a little more digging I discover that this has something to do
> with passwords/authentication. So now I am stumped, I don't know
…[3 more quoted lines elided]…
> one persons computer and there is no security other than OS login.

If the backup had been written to CD ROM then the restore may have
left the file 'read only' which could give the 9-037 error.  Check
using ATTRIB or just set it off with ATTRIB -r *.IDX

Otherwise if this in on Windows NT/XP it may be a user permissions
issue.
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
