[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# COBOL Workbench for MVS, DB2, and CICS Development/Maintenance

_4 messages · 4 participants · 1996-04_

**Topics:** [`Mainframe, z/OS, JCL, CICS`](../topics.md#mainframe) · [`Databases and SQL`](../topics.md#databases)

---

### COBOL Workbench for MVS, DB2, and CICS Development/Maintenance

- **From:** "jale..." <ua-author-13875977@usenetarchives.gap>
- **Date:** 1996-04-15T20:00:01+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<4l17qj$i6m@vivaldi.telepac.pt>`

```
Could I get the net's opinion on which is the best workbench for team
based COBOL development and maintenance in a DB2+CICS MVS
environment?

Thanks,
Jose A. S. Alegria
Work: Home:
```

#### ↳ Re: COBOL Workbench for MVS, DB2, and CICS Development/Maintenance

- **From:** "a..." <ua-author-512315@usenetarchives.gap>
- **Date:** 1996-04-16T20:00:02+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-494bb6a4aa-p2@usenetarchives.gap>`
- **In-Reply-To:** `<4l17qj$i6m@vivaldi.telepac.pt>`
- **References:** `<4l17qj$i6m@vivaldi.telepac.pt>`

```
jal··.@mai··c.pt (Jose A. S. Alegria) wrote:

› Could I get the net's opinion on which is the best workbench for team
› based  COBOL development and maintenance in a DB2+CICS MVS
› environment?
 
› Thanks,
› Jose A. S. Alegria
› Work:    Home: 

I can give you a totally biased opinion if you like!
Micro Focus COBOL is the defacto standard for MVS compatible
development. We have
MVS Workbench - for a total TSO emulation
COBOL Workbench - for GUI based COBOL development
MCO - for total CICS compatibility
MF370 - for assembler compatibility
MFIMS - for IMS compatibility
HCO addon to DB2/2 - for DB2 compatibility
XDB - for DB2 compatibilty
plus a host of other tools for JCL, PLI, Source control, remote
data access, screens scraping, C/S development, visual programming etc

Andy Morris
Sales Consultant, Micro Focus
a.··.@mfl··o.uk
```

#### ↳ Re: COBOL Workbench for MVS, DB2, and CICS Development/Maintenance

- **From:** "dma..." <ua-author-11660218@usenetarchives.gap>
- **Date:** 1996-04-17T20:00:03+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-494bb6a4aa-p3@usenetarchives.gap>`
- **In-Reply-To:** `<4l17qj$i6m@vivaldi.telepac.pt>`
- **References:** `<4l17qj$i6m@vivaldi.telepac.pt>`

```
wc··.@adp··e.edu wrote:

› Another (biased) opinion...
 
› Unless you have a compelling reason to move development off of the mainframe 
› (on which the DB2+CICS MVS is running), like incredibly bad availability of 
› computer time to compile and test on the mainframe, why do so?
 
› In our case, for instance, the mainframe is sized to cover the vast group of 
› people (1500? 2000?) using CICS on-line during the day.  Whatever load the 50 
› of us developers adds to that can be managed by the priorities the operating 
› system assigns.

[snip]

I'm tempted to agree with you. If there's a weak part to your opinion, it's
this part about the load the "50 of us developers adds" to the system. Many
organizations have taken a look at the CPU time, and everything else, that
the DP department is using, and come to the conclusion that if they shell
out $1,500 or so to Microfocus, they'll get that $1,500 back pretty quick.
Even if you throw in another $5,000 for the PC, and another $10,000 for
extra money to set up the PC... the money still comes back fairly quick.

The big wonderful thing about PC's is the time on the system is free. I
cannot speak about the tools you mention (INTERTEST and EXPEDITER), but for
IMS we would use BTS to do all our testing on the mainframe. And BTS is
a real hog on resources. I know because I would see all the WARNING messages
I would get from TSO telling me that I was using a lot of CPU time et
cetera.

Are you sure that the managers of other departments in the organization you
work in aren't complaining about about the huge charge-back costs that they
are getting from your DP department?

Your users might be best served by a mainframe, with centralized data
storage and backup, and all of the other services the data center can offer
(i.e. high-speed bulk laser-jet printing, automated job scheduling, et
cetera), but your department might not need all that.

To really get the answer, you would need to start looking at the actual
numbers (CPU usage, et cetera), to figure out if you could save some big
money by moving development/maintenance/testing off the mainframe.
```

##### ↳ ↳ Re: COBOL Workbench for MVS, DB2, and CICS Development/Maintenance

- **From:** "keith farndon" <ua-author-17086118@usenetarchives.gap>
- **Date:** 1996-04-21T20:00:04+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-494bb6a4aa-p4@usenetarchives.gap>`
- **In-Reply-To:** `<gap-494bb6a4aa-p3@usenetarchives.gap>`
- **References:** `<4l17qj$i6m@vivaldi.telepac.pt> <gap-494bb6a4aa-p3@usenetarchives.gap>`

```
Unless your company outsources its computer requirements and is charged
by the CPU cycle, the average data center will make each CPU cyclce a
little more expensive to cover for the loss of revenue from PC testing.
Animator is a wonderfull tool, and even a mainframe bigot like myself
will admit that its ease of use beats the mainframe tools. The only
drawback that I can see is the inability to test large systems down on
the PC. You just dont have enough space. To create small test systems
without a store bought or inhouse developed extract tool is extremely
difficult. I will certainly code my programs using SPF/PC, compile and
try to test with MICRO FOCUS, but the final proof is uploading and
testing on the mainframe. What is really needed are more cost efficient
and dynamic data centers. I would say that the average data center is
still 10 to 15 years behind current thinking, and that is usually due to
the security issues of production data residing on the same machines.
The hardware is already present to bring us into the 1990's, we just
have to carry DCO staff with it.

David Mazeau wrote:
› 
› wc··.@adp··e.edu wrote:
…[40 more quoted lines elided]…
› money by moving development/maintenance/testing off the mainframe.
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
