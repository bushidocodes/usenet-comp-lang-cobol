[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Need help with File Status "9-" in MicroFocus COBOL

_4 messages · 1 participant · 1998-01 → 1998-02_

**Topics:** [`Compilers and vendors`](../topics.md#compilers) · [`VSAM, files, sorting`](../topics.md#files) · [`Help requests and how-to`](../topics.md#help)

---

### Need help with File Status "9-" in MicroFocus COBOL

- **From:** "emmanouil g. petridis" <ua-author-17074956@usenetarchives.gap>
- **Date:** 1998-01-29T19:00:01+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<34D212F7.AF99A9C0@mail.otenet.gr>`

```
I wonder if anyone else has encountered the following problem:

After a couple of hours of normal work (say 16 to 22 simultaneous users)
the system gives a file status of "9-" to an arbitrary file operation,
and then on fails on almost any file access, for every user and RTS
instance.

The only solution so far is to power down the machine and then re-boot
and perform a bcheck on the application files. One might correctly guess
that this does tend to strain our relations with the user community :-).

File status description is the following: "Attempt to open an NLS file
using an incompatible program (Fatal)".
Not much help, is it? Our S/W supplier is more or less at a loss, and
frankly so am I. I would very much appreciate any help, info or hint you
might feel applicable.

Environment details:
--------------------

Compiler: Micro Focus COBOL/2 v1.1 revision 000 (according to listing
header at least)
O.S.: INTERACTIVE UNIX System V/386 Release 3.2, Version 4.1

Platform is a DIGITAL Prioris 166XL with 48 MB of RAM and two SCSI HDs
of 2.2GB each.
Key Packages installed are:
-INTERACTIVE TCP/IP ver 1.5
-INTERACTIVE NFS ver 2.2.2

Total number of different files per application is roughly 94, all of
them indexed (so one would have to count 94 .idx files as well), but
maximum number of files open per program would be about 12.

Kernel tunables have as follows:
--------------------------------

Report on unix.8
Description: Mon Jan 27 23:40:59 1997

Driver Configuration for unix.8
Driver State Description
fd Y Floppy Disk Driver
lp Y Line Printer Driver
ramd N Dynamic RAM Disk Driver
sxt Y Shell Layers Driver
wt N Wangtek Tape Controller Driver - AT bus only
asy Y Serial I/O Driver
itimer Y interval timer pseudo device driver
pwrmon N UPS shutdown support
llc Y Link level protocol pseudo driver
e3E0 Y 3Com EtherLink III Driver
sl0 Y SLIP (Serial Line IP) driver
sl1 Y SLIP (Serial Line IP) driver - unit 1
sl2 N SLIP (Serial Line IP) driver - unit 2
sl3 N SLIP (Serial Line IP) driver - unit 3
socksys Y network application compatibility driver

Facility Configuration for unix.8
Facility State Description
dos Y MS-DOS File System Service
osm Y Operating System Messages
prf Y Unix Kernel Profiler
s52k Y 2 Kilobyte File System
s5l Y Long Filename File System
xsd Y XENIX Shared Memory
hs N High Sierra (ISO 9660) CD-ROM File System
xx Y XENIX File System
vf Y Very Fast File System
nfs Y Network File System
dbg Y Kernel Debugger
wtk N Weitek 1167 Support
xsm Y XENIX Semaphores
net Y STREAMS Facilities
hbtcp Y INTERACTIVE TCP/IP

High Performance Device Driver configuration for unix.8

Adaptec 294x/394x PCI SCSI Adapter
Interrupt 11
Installed devices:
DISK target 0 TAPE target 4

unix.8 Tunable parameter settings for KERNEL
Parameter Current Default Minimum Maximum
NBUF 2048 0 0 10240
NCALL 250 50 30 250
NINODE 800 400 100 800
NS5INODE 800 400 100 800
NFILE 800 400 100 800
NMOUNT 25 25 10 200
NPROC 1000 100 50 1000
NGROUPS 16 16 16 16
NREGION 600 350 210 600
NCLIST 400 200 120 400
MAXUP 512 30 15 1000
NOFILES 100 60 20 100
NHBUF 512 512 32 10240
NPBUF 20 20 20 20
NAUTOUP 3 15 0 30
BDFLUSHR 1 10 1 30
MAXPMEM 0 0 0 4096
ARG_MAX 16384 5120 4096 128000
SHLBMAX 8 8 2 12
FLCKREC 100 100 100 100
PUTBUFSZ 2000 2000 1000 10000
MAXSLICE 25 50 25 100
ULIMIT 4194303 4194303 2048 4194303
SPTMAP 50 50 50 200
PIOMAP 50 50 50 50
PIOMAXSZ 64 64 4 64
DO387CR3 0 0 0 1
UAREAUS 0 1 0 1
UAREARW 0 1 0 1

unix.8 Tunable parameter settings for MSG
Parameter Current Default Minimum Maximum
MSGMAP 100 100 10 32767
MSGMAX 2048 2048 512 32767
MSGMNB 4096 4096 4096 65535
MSGMNI 50 50 50 1024
MSGSSZ 8 8 8 32
MSGTQL 40 40 40 1024
MSGSEG 1024 1024 1024 32767

unix.8 Tunable parameter settings for DEVICE
Parameter Current Default Minimum Maximum
NUMXT 3 3 1 3
NUMSXT 6 6 1 6
NCPYRIGHT 10 10 10 10
NKDVTTY 8 8 1 8
PRFMAX 2048 2048 2048 40960
TTHOG 256 256 256 6144
RAMDSIZE 256 256 256 32768
NLDD 10 10 0 128

unix.8 Tunable parameter settings for PAGE
Parameter Current Default Minimum Maximum
VHNDFRAC 16 16 8 32
AGEINTERVAL 9 9 2 100
GPGSLO 25 25 0 25
GPGSHI 40 40 1 40
GPGSMSK 1056 1056 1056 1056
MAXSC 1 1 1 1
MAXFC 1 1 1 1
MAXUMEM 4096 4096 2560 131072
MINARMEM 25 25 25 40
MINASMEM 25 25 25 40
MINHIDUSTK 4 4 4 32
MINUSTKGAP 2 2 2 32

unix.8 Tunable parameter settings for SEM
Parameter Current Default Minimum Maximum
SEMMAP 10 10 10 10
SEMMNI 10 10 10 20
SEMMNS 60 60 60 60
SEMMNU 30 30 30 30
SEMMSL 25 25 25 25
SEMOPM 10 10 10 10
SEMUME 10 10 10 10
SEMVMX 32767 32767 32767 32767
SEMAEM 16384 16384 16384 16384

unix.8 Tunable parameter settings for SHM
Parameter Current Default Minimum Maximum
SHMMAX 1048576 1048576 131072 2097152
SHMMIN 1 1 1 1
SHMMNI 100 100 100 100
SHMSEG 6 6 6 15
SHMALL 512 512 256 512

unix.8 Tunable parameter settings for STREAMS
Parameter Current Default Minimum Maximum
NQUEUE 2048 128 0 4096
NSTREAM 512 32 0 512
NSTRPUSH 9 9 9 9
NSTREVENT 256 256 256 512
MAXSEPGCNT 1 1 0 32
NMUXLINK 64 87 1 87
STRMSGSZ 4096 4096 4096 32767
STRCTLSZ 1024 1024 1024 1024
NBLK4096 56 1 0 2048
NBLK2048 80 20 0 2048
NBLK1024 64 20 0 2048
NBLK512 128 8 0 2048
NBLK256 128 8 0 2048
NBLK128 512 8 0 2048
NBLK64 256 40 0 2048
NBLK16 256 40 0 2048
NBLK4 256 40 0 2048
STRLOFRAC 80 80 0 80
STRMEDFRAC 90 90 80 100
NLOG 3 3 3 3
NUMSP 32 32 5 256
NUMTIM 96 16 1 512
NUMTRW 96 16 1 512

unix.8 Tunable parameter settings for DMA
Parameter Current Default Minimum Maximum
DMAEXCL 1 1 0 1
DMA24BIT 0 0 0 1
DMAKSTACK 0 0 0 1

unix.8 Tunable parameter settings for S52K
Parameter Current Default Minimum Maximum
S52KNBUF 100 100 100 400
S52KNHBUF 32 32 32 256

unix.8 Tunable parameter settings for RFS
Parameter Current Default Minimum Maximum
NRCVD 150 150 40 500
NSNDD 100 100 100 350
NSRMOUNT 10 10 1 50
NADVERTISE 25 25 0 25
MAXGDP 24 24 10 32
MINSERVE 3 3 3 3
MAXSERVE 6 6 3 6
NRDUSER 250 250 0 700
RFHEAP 3072 3072 1024 3072
NLOCAL 0 0 0 10
NREMOTE 0 0 0 10
RCACHETIME 10 10 -1 10
RFS_VHIGH 1 1 1 1
RFS_VLOW 1 1 1 1

unix.8 Tunable parameter settings for XENIX
Parameter Current Default Minimum Maximum
DSTFLAG 1 1 0 1
NSCRN 0 0 0 10
NEMAP 10 10 10 10
TIMEZONE 480 480 0 1440
XSEMMAX 60 60 20 60
XSDSEGS 25 25 1 25
XSDSLOTS 3 3 1 3

unix.8 Tunable parameter settings for UA
Parameter Current Default Minimum Maximum
UAREAUS 0 1 0 1
UAREARW 0 1 0 1



Thanks in advance for your time and consideration.

Emmanouil G. Petridis
Information Systems Manager, KONTI Steel Hellas S.A.
120 Vassilisis Sofias Avenue, GR-115 26 Athens, Greece
Opinions expressed do not necessarily reflect those of my employer.


I wonder if anyone else has encountered the following problem:

After a couple of hours of normal work (say 16 to 22 simultaneous users)
the system gives a file status of "9-" to an arbitrary file operation,
and then on fails on almost any file access, for every user and RTS instance.

The only solution so far is to power down the machine and then re-boot
and perform a bcheck on the application files. One might correctly guess
that this does tend to strain our relations with the user community :-).
File status description is the following: "Attempt to open an NLS file
using an incompatible program (Fatal)".
Not much help, is it? Our S/W supplier is more or less at a loss, and
frankly so am I. I would very much appreciate any help, info or hint you
might feel applicable.

Environment details:
--------------------

Compiler: Micro Focus COBOL/2 v1.1 revision 000 (according to listing
header at least)
O.S.: INTERACTIVE UNIX System V/386 Release 3.2, Version 4.1

Platform is a DIGITAL Prioris 166XL with 48 MB of RAM and two SCSI HDs
of 2.2GB each.
Key Packages installed are:
-INTERACTIVE TCP/IP ver 1.5
-INTERACTIVE NFS ver 2.2.2

Total number of different files per application is roughly 94, all of
them indexed (so one would have to count 94 .idx files as well), but maximum
number of files open per program would be about 12.

Kernel tunables have as follows:
--------------------------------

Report on unix.8
Description: Mon Jan 27 23:40:59 1997
Driver Configuration for unix.8
Driver  State   Description
fd      Y      
Floppy Disk Driver
lp      Y      
Line Printer Driver
ramd    N       Dynamic
RAM Disk Driver
sxt     Y      
Shell Layers Driver
wt      N      
Wangtek Tape Controller Driver - AT bus only
asy     Y      
Serial I/O Driver
itimer  Y       interval timer
pseudo device driver
pwrmon  N       UPS shutdown
support
llc     Y      
Link level protocol pseudo driver
e3E0    Y       3Com
EtherLink III Driver
sl0     Y      
SLIP (Serial Line IP) driver
sl1     Y      
SLIP (Serial Line IP) driver - unit 1
sl2     N      
SLIP (Serial Line IP) driver - unit 2
sl3     N      
SLIP (Serial Line IP) driver - unit 3
socksys Y       network application
compatibility driver
Facility Configuration for unix.8
Facility State  Description
dos     Y      
MS-DOS File System Service
osm     Y      
Operating System Messages
prf     Y      
Unix Kernel Profiler
s52k    Y       2
Kilobyte File System
s5l     Y      
Long Filename File System
xsd     Y      
XENIX Shared Memory
hs      N      
High Sierra (ISO 9660) CD-ROM File System
xx      Y      
XENIX File System
vf      Y      
Very Fast File System
nfs     Y      
Network File System
dbg     Y      
Kernel Debugger
wtk     N      
Weitek 1167 Support
xsm     Y      
XENIX Semaphores
net     Y      
STREAMS Facilities
hbtcp   Y       INTERACTIVE
TCP/IP
High Performance Device Driver configuration for unix.8
Adaptec 294x/394x PCI SCSI Adapter
Interrupt 11
Installed devices:
DISK target 0          
TAPE target 4
unix.8 Tunable parameter settings for KERNEL
Parameter    Current   Default  
Minimum   Maximum
NBUF          
2048      0        
0         10240
NCALL          250      
50        30       
250
NINODE         800      
400       100      
800
NS5INODE       800      
400       100      
800
NFILE          800      
400       100      
800
NMOUNT         25       
25        10       
200
NPROC          1000     
100       50       
1000
NGROUPS        16       
16        16       
16
NREGION        600      
350       210      
600
NCLIST         400      
200       120      
400
MAXUP          512      
30        15       
1000
NOFILES        100      
60        20       
100
NHBUF          512      
512       32       
10240
NPBUF          20       
20        20       
20
NAUTOUP        3        
15        0        
30
BDFLUSHR       1        
10        1        
30
MAXPMEM        0        
0         0        
4096
ARG_MAX        16384    
5120      4096      128000
SHLBMAX        8        
8         2        
12
FLCKREC        100      
100       100      
100
PUTBUFSZ       2000     
2000      1000      10000
MAXSLICE       25       
50        25       
100
ULIMIT         4194303  
4194303   2048      4194303
SPTMAP         50       
50        50       
200
PIOMAP         50       
50        50       
50
PIOMAXSZ       64       
64        4        
64
DO387CR3       0        
0         0        
1
UAREAUS        0        
1         0        
1
UAREARW        0        
1         0        
1
unix.8 Tunable parameter settings for MSG
Parameter    Current   Default  
Minimum   Maximum
MSGMAP         100      
100       10       
32767
MSGMAX         2048     
2048      512      
32767
MSGMNB         4096     
4096      4096      65535
MSGMNI         50       
50        50       
1024
MSGSSZ         8        
8         8        
32
MSGTQL         40       
40        40       
1024
MSGSEG         1024     
1024      1024      32767
unix.8 Tunable parameter settings for DEVICE
Parameter    Current   Default  
Minimum   Maximum
NUMXT          3        
3         1        
3
NUMSXT         6        
6         1        
6
NCPYRIGHT      10       
10        10       
10
NKDVTTY        8        
8         1        
8
PRFMAX         2048     
2048      2048      40960
TTHOG          256      
256       256      
6144
RAMDSIZE       256      
256       256      
32768
NLDD          
10        10       
0         128
unix.8 Tunable parameter settings for PAGE
Parameter    Current   Default  
Minimum   Maximum
VHNDFRAC       16       
16        8        
32
AGEINTERVAL    9        
9         2        
100
GPGSLO         25       
25        0        
25
GPGSHI         40       
40        1        
40
GPGSMSK        1056     
1056      1056      1056
MAXSC          1        
1         1        
1
MAXFC          1        
1         1        
1
MAXUMEM        4096     
4096      2560      131072
MINARMEM       25       
25        25       
40
MINASMEM       25       
25        25       
40
MINHIDUSTK     4        
4         4        
32
MINUSTKGAP     2        
2         2        
32
unix.8 Tunable parameter settings for SEM
Parameter    Current   Default  
Minimum   Maximum
SEMMAP         10       
10        10       
10
SEMMNI         10       
10        10       
20
SEMMNS         60       
60        60       
60
SEMMNU         30       
30        30       
30
SEMMSL         25       
25        25       
25
SEMOPM         10       
10        10       
10
SEMUME         10       
10        10       
10
SEMVMX         32767    
32767     32767     32767
SEMAEM         16384    
16384     16384     16384
unix.8 Tunable parameter settings for SHM
Parameter    Current   Default  
Minimum   Maximum
SHMMAX         1048576  
1048576   131072    2097152
SHMMIN         1        
1         1        
1
SHMMNI         100      
100       100      
100
SHMSEG         6        
6         6        
15
SHMALL         512      
512       256      
512
unix.8 Tunable parameter settings for STREAMS
Parameter    Current   Default  
Minimum   Maximum
NQUEUE         2048     
128       0        
4096
NSTREAM        512      
32        0        
512
NSTRPUSH       9        
9         9        
9
NSTREVENT      256      
256       256      
512
MAXSEPGCNT     1        
1         0        
32
NMUXLINK       64       
87        1        
87
STRMSGSZ       4096     
4096      4096      32767
STRCTLSZ       1024     
1024      1024      1024
NBLK4096       56       
1         0        
2048
NBLK2048       80       
20        0        
2048
NBLK1024       64       
20        0        
2048
NBLK512        128      
8         0        
2048
NBLK256        128      
8         0        
2048
NBLK128        512      
8         0        
2048
NBLK64         256      
40        0        
2048
NBLK16         256      
40        0        
2048
NBLK4          256      
40        0        
2048
STRLOFRAC      80       
80        0        
80
STRMEDFRAC     90       
90        80       
100
NLOG          
3         3        
3         3
NUMSP          32       
32        5        
256
NUMTIM         96       
16        1        
512
NUMTRW         96       
16        1        
512
unix.8 Tunable parameter settings for DMA
Parameter    Current   Default  
Minimum   Maximum
DMAEXCL        1        
1         0        
1
DMA24BIT       0        
0         0        
1
DMAKSTACK      0        
0         0        
1
unix.8 Tunable parameter settings for S52K
Parameter    Current   Default  
Minimum   Maximum
S52KNBUF       100      
100       100      
400
S52KNHBUF      32       
32        32       
256
unix.8 Tunable parameter settings for RFS
Parameter    Current   Default  
Minimum   Maximum
NRCVD          150      
150       40       
500
NSNDD          100      
100       100      
350
NSRMOUNT       10       
10        1        
50
NADVERTISE     25       
25        0        
25
MAXGDP         24       
24        10       
32
MINSERVE       3        
3         3        
3
MAXSERVE       6        
6         3        
6
NRDUSER        250      
250       0        
700
RFHEAP         3072     
3072      1024      3072
NLOCAL         0        
0         0        
10
NREMOTE        0        
0         0        
10
RCACHETIME     10       
10        -1       
10
RFS_VHIGH      1        
1         1        
1
RFS_VLOW       1        
1         1        
1
unix.8 Tunable parameter settings for XENIX
Parameter    Current   Default  
Minimum   Maximum
DSTFLAG        1        
1         0        
1
NSCRN          0        
0         0        
10
NEMAP          10       
10        10       
10
TIMEZONE       480      
480       0        
1440
XSEMMAX        60       
60        20       
60
XSDSEGS        25       
25        1        
25
XSDSLOTS       3        
3         1        
3
unix.8 Tunable parameter settings for UA
Parameter    Current   Default  
Minimum   Maximum
UAREAUS        0        
1         0        
1
UAREARW        0        
1         0        
1
 
 

Thanks in advance for your time and consideration.

Emmanouil G. Petridis
Information Systems Manager, KONTI Steel Hellas S.A.
120 Vassilisis Sofias Avenue, GR-115 26 Athens, Greece
Opinions expressed do not necessarily reflect those of my employer.
```

#### ↳ Re: Need help with File Status "9-" in MicroFocus COBOL

- **From:** "emmanouil g. petridis" <ua-author-17074956@usenetarchives.gap>
- **Date:** 1998-01-29T19:00:02+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-e6ad95c02e-p2@usenetarchives.gap>`
- **In-Reply-To:** `<34D212F7.AF99A9C0@mail.otenet.gr>`
- **References:** `<34D212F7.AF99A9C0@mail.otenet.gr>`

```

› After a couple of hours of normal work (say 16 to 22 simultaneous users) the system gives a file status of "9-" to an arbitrary file operation, and then on fails on almost any file access, for every user and RTS instance.
› 
…[3 more quoted lines elided]…
› ............................

I must admit failing to mention the following:

The application used keeps separate file areas for each accounting year. As it is still January, both 1997 and 1998 areas are in use, with the 1997 one having a lighter usage, but on full files. The largest one takes 26 MB
for the data part, and 31 MB for the index. This situation has occurred before -during the first months of 1997- but the actual number of files used by the application has risen slightly in the meantime.

Hope it helps to come up with a solution.
Thanks again for your time and consideration.

Emmanouil G. Petridis
Information Systems Manager, KONTI Steel Hellas S.A.
120 Vassilisis Sofias Avenue, GR-115 26 Athens, Greece
Opinions expressed do not necessarily reflect those of my employer.
```

#### ↳ Re: Need help with File Status "9-" in MicroFocus COBOL

- **From:** "emmanouil g. petridis" <ua-author-17074956@usenetarchives.gap>
- **Date:** 1998-01-30T19:00:03+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-e6ad95c02e-p3@usenetarchives.gap>`
- **In-Reply-To:** `<34D212F7.AF99A9C0@mail.otenet.gr>`
- **References:** `<34D212F7.AF99A9C0@mail.otenet.gr>`

```

I've just received a reply by e-mail, and since it has made me to note a few more clues (me hopes), I decided on posting my reply here as well. I only feel that I have to respect the originator's wish for privacy by omitting
his/her name from the following:

Dear ...,

first, thank you for your prompt and kind reply.
I do have though a couple of questions on your remarks.

› OK, I don't have a 100% positive answer, but I've seen this kind of
› thing happen before.
…[7 more quoted lines elided]…
›› NOFILES        100       60        20        100

It is to my understanding that NOFILES describes something like
"the maximum number of open / referenced files per user-id / job / process".
As I am writing this from home and I don't have the manuals handy I'm
not sure, but unless memory fails me, it should read "open files per
process". Obviously no such number of files is open per process. It
could be that each print output counts as one more file - printer
output is more or less a sequential file, re-directed to the lp
service - but if such were the case, the problem should have appeared
before.

› If the OS can't open files for itself...strange things start to
› happen, you pretty much have to shut down.
…[5 more quoted lines elided]…
› that will let you massage the number of open files...)

If I read the manuals correctly, the maximum number of
open / referenced (?) files in the system is set to 800.
NFILE 800 400 100 800
It is set as high as it can go, but it should suffice.

We have tried forcing users to return to the shell prompt on every 8
program calls, but this seems not to alleviate the problem. It could
be that we should force users to come out to the shell
simultaneously, but I don't think it would be very productive, and it
seems not to solve the problem anyhow, once the problem appears that
is.

By the way, the file system on which the application resides is of
the SystemV style, 2K block, long file name supporting variety, and
the application consists of ".int" files evoked through a "cobrun menuporg",
rather than ".gnt" ones.

› "NLS" sounds like "National Language Services"...a set of tables the
› OS uses to give system messages in your native format.  IF the OS
› encounters an error...wishes to print a message, can't open the NLS
› database...I'd expect an error like this.

The funny thing is that in both the development and the production
machine no International Supplements have been installed, and that
has been the case for a year and a half now. So it may not relate
directly with the problem at hand, as the COBOL RTS should think
that it runs on a - somewhat modified - US machine.

› Please don't post in HTML. It's not good form in USENET.
As I had to use a different environment from my usual, old trusted
PegasusMail / FreeAgent combi, I must have missed the relevant
setting. My fault. Sorry.

Thanks once more for your comments. Food for thought.

Emmanouil G. Petridis
Information Systems Manages, KONTI Steel Hellas S.A.
120 Vasilissis Sofias Avenue, GR-115 26 Athens, Greece
Opinions expressed do not necessarily reflect those of my employer.
```

#### ↳ Re: Need help with File Status "9-" in MicroFocus COBOL

- **From:** "emmanouil g. petridis" <ua-author-17074956@usenetarchives.gap>
- **Date:** 1998-02-09T19:00:04+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-e6ad95c02e-p4@usenetarchives.gap>`
- **In-Reply-To:** `<34D212F7.AF99A9C0@mail.otenet.gr>`
- **References:** `<34D212F7.AF99A9C0@mail.otenet.gr>`

```

I had written in mild despair the other day:

› ... the system gives a file status of "9-" to an arbitrary file
› operation, and then on fails on almost any file access, for every
› user and RTS instance.

It seems that this behaviour can be attributed to an insufficient
FLCKREC
setting. It defaulted to 100 (with 100 as both the minimum and maximum
values permitted), and as the sar -v reports showed, it was simply not
enough.
After some tweaking it is now set to 800 with today's reports showing
the max.
usage climbing to 119.
I believe -need to add hope?- to have put this one behind.

Thanks for your time and consideration.

Emmanouil G. Petridis
Information Systems Manager, KONTI Steel Hellas S.A.
120 Vassilisis Sofias Avenue, GR-115 26 Athens, Greece
Opinions expressed do not necessarily reflect those of my employer.
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
