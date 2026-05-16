[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Flowchart generator for JCL and COBOL programs

_10 messages · 9 participants · 2004-09_

**Topics:** [`Mainframe, z/OS, JCL, CICS`](../topics.md#mainframe)

---

### Flowchart generator for JCL and COBOL programs

- **From:** "Deborah Torrekens" <deborah@phidani.be>
- **Date:** 2004-09-03T10:56:15+02:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<4138329c$0$8979$6c56d894@feed0.news.be.easynet.net>`

```
Hi,

I'm looking for a tool that generates hierarchical charts for COBOL
programs, and flowcharts for JCL members.
Does anyone know of such tools?

Regards,
Debbie
```

#### ↳ Re: Flowchart generator for JCL and COBOL programs

- **From:** "Brian Crane" <brian.crane@microfocus.com>
- **Date:** 2004-09-03T12:48:39+01:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<ch9lq8$dru$1@hyperion.microfocus.com>`
- **References:** `<4138329c$0$8979$6c56d894@feed0.news.be.easynet.net>`

```
Hi Debbie,

Recommend that you take a look at Micro Focus Revolve. It handles COBOL, JCL
and many other member types.

http://www.microfocus.com/products/revolve/datasheet.asp  (product
description)
http://www.microfocus.com/revolvedemo  (online demo)

Please let me know if you need any more information.

Best regards,

Brian Crane
Product Director
Micro Focus


"Deborah Torrekens" <deborah@phidani.be> wrote in message
news:4138329c$0$8979$6c56d894@feed0.news.be.easynet.net...
> Hi,
>
…[7 more quoted lines elided]…
>
```

#### ↳ Re: Flowchart generator for JCL and COBOL programs

- **From:** Robert Wagner <robert@wagner.net.yourmammaharvests>
- **Date:** 2004-09-03T13:21:36+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<fvrgj01lhmk5ups81a2ced0j1rf4sbak7e@4ax.com>`
- **References:** `<4138329c$0$8979$6c56d894@feed0.news.be.easynet.net>`

```
On Fri, 3 Sep 2004 10:56:15 +0200, "Deborah Torrekens"
<deborah@phidani.be> wrote:

>Hi,
>
>I'm looking for a tool that generates hierarchical charts for COBOL
>programs, and flowcharts for JCL members.
>Does anyone know of such tools?

Most JCL I've seen had one step per job. The hierarchy was up in the
job scheduler.
```

##### ↳ ↳ Re: Flowchart generator for JCL and COBOL programs

- **From:** scomstock@aol.com (S Comstock)
- **Date:** 2004-09-03T18:45:07+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<20040903144507.15331.00000154@mb-m22.aol.com>`
- **References:** `<fvrgj01lhmk5ups81a2ced0j1rf4sbak7e@4ax.com>`

```
Robert Wagner writes ...

[snip]

>Most JCL I've seen had one step per job. The hierarchy was up in the
>job scheduler. 

Huh?  Have you never seen a compile and link? Right there we have two steps per
job. I have seen jobs with tens of steps and heard of jobs with hundreds of
steps.

Kind regards,


-Steve Comstock
800-993-9716
303-393-8716
www.trainersfriend.com
email: steve@trainersfriend.com
256-B S. Monaco Parkway
Denver, CO 80224
USA
```

###### ↳ ↳ ↳ Re: Flowchart generator for JCL and COBOL programs

- **From:** Robert Wagner <robert@wagner.net.yourmammaharvests>
- **Date:** 2004-09-04T03:45:35+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<fh4ij05shsj0m0lb0ek950lt3aj5es6v3s@4ax.com>`
- **References:** `<fvrgj01lhmk5ups81a2ced0j1rf4sbak7e@4ax.com> <20040903144507.15331.00000154@mb-m22.aol.com>`

```
On 03 Sep 2004 18:45:07 GMT, scomstock@aol.com (S Comstock) wrote:

>Robert Wagner writes ...
>
…[7 more quoted lines elided]…
>steps.

At three out of three shops where I worked recently, they said that
was Old School because it made restarts too hard. The operator had to
edit JCL, which was error-prone and forbidden. The operator WAS
allowed to manipulate things in the scheduler, it was his primary
activity, so one step per job gave him the flexibility to restart at
any step.

It all stems from their prediliction to abend programs for the
slightest reason. If there weren't so many abends, job structure
wouldn't revolve around restarts.
```

###### ↳ ↳ ↳ Re: Flowchart generator for JCL and COBOL programs

_(reply depth: 4)_

- **From:** JR <nobody@dazoo.org>
- **Date:** 2004-09-04T22:07:42+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<Xns955AB869E3E72dragonslayerdazooorg@38.144.126.105>`
- **References:** `<fvrgj01lhmk5ups81a2ced0j1rf4sbak7e@4ax.com> <20040903144507.15331.00000154@mb-m22.aol.com> <fh4ij05shsj0m0lb0ek950lt3aj5es6v3s@4ax.com>`

```
Robert Wagner <robert@wagner.net.yourmammaharvests> wrote in
news:fh4ij05shsj0m0lb0ek950lt3aj5es6v3s@4ax.com: 

> On 03 Sep 2004 18:45:07 GMT, scomstock@aol.com (S Comstock) wrote:
> 
…[21 more quoted lines elided]…
> 

Yes, it's called "the dumbing down of IT" ...
```

###### ↳ ↳ ↳ Re: Flowchart generator for JCL and COBOL programs

_(reply depth: 4)_

- **From:** "Don Leahy" <leahydon@nospamplease.netscape.net>
- **Date:** 2004-09-05T00:32:54-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<OFw_c.30923$7i2.1408966@news20.bellglobal.com>`
- **References:** `<fvrgj01lhmk5ups81a2ced0j1rf4sbak7e@4ax.com> <20040903144507.15331.00000154@mb-m22.aol.com> <fh4ij05shsj0m0lb0ek950lt3aj5es6v3s@4ax.com>`

```
"Robert Wagner" <robert@wagner.net.yourmammaharvests> wrote in message 
news:fh4ij05shsj0m0lb0ek950lt3aj5es6v3s@4ax.com...
> On 03 Sep 2004 18:45:07 GMT, scomstock@aol.com (S Comstock) wrote:
>
…[22 more quoted lines elided]…
> wouldn't revolve around restarts.

FWIW, at two out of two shops where I've worked recently, the scheduling 
system would automatically restart failed job steps with no JCL editing 
involved.   Having said that, one of those shops favoured jobs with minimal 
number of steps while the other encouraged the use of complicated cataloged 
procedures consisting of dozens of steps.

I agree with your point about unnecessary abends.  Too often that is a 
symptom of poor design and/or lazy coding.
```

##### ↳ ↳ Re: Flowchart generator for JCL and COBOL programs

- **From:** Colin Campbell <cmcampb@adelphia.net>
- **Date:** 2004-09-03T13:09:22-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<hLKdnfAT9qPuUqXcRVn-pg@adelphia.com>`
- **In-Reply-To:** `<fvrgj01lhmk5ups81a2ced0j1rf4sbak7e@4ax.com>`
- **References:** `<4138329c$0$8979$6c56d894@feed0.news.be.easynet.net> <fvrgj01lhmk5ups81a2ced0j1rf4sbak7e@4ax.com>`

```
Robert Wagner wrote:

>On Fri, 3 Sep 2004 10:56:15 +0200, "Deborah Torrekens"
><deborah@phidani.be> wrote:
…[11 more quoted lines elided]…
>
In my former shop, production jobs usually consisted of many steps.  
Often, the dreaded COND= or the much clearer IF...THEN...ELSE...ENDIF 
were used to execute steps on certain days of the week, or weeks of the 
month.  This complexity makes flowcharts valuable, if somewhat hard to 
interpret.

Some of the commercially available JCL tools, such as JOB/Scan (I'm 
pretty sure about this one) and/or CA-JCLCHECK (I haven't used this one 
for some years), and/or ASG-JCLPREP (I haven't looked at its 
capabilities) include tools for graphically interpreting JCL.

Another tool which I highly recommend is SystemVision from ADPAC.  It 
will interpret both COBOL and JCL (as well as other languages).  Some 
may know this tool under an older name, PM/SS.  Pricing is pretty 
reasonable for the range of capabilities provided.

These tools have the advantage of operating on the mainframe, where the 
programs and JCL reside, instead of forcing you to move everything to 
another platform to "get the picture".
- or -
If you really want to have fun (and spend a load of money), try Vista 
from ASG (formerly Allen Systems Group).  With this tool, you get to 
download everything from your mainframe to a Unix server, license Oracle 
data base software, and do queries from a Windows client.  Expensive and 
extremely complex, but the graphics are great!
```

##### ↳ ↳ Re: Flowchart generator for JCL and COBOL programs

- **From:** yukonmama@aol.com (YukonMama)
- **Date:** 2004-09-09T01:39:35+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<20040908213935.22107.00003219@mb-m07.aol.com>`
- **References:** `<fvrgj01lhmk5ups81a2ced0j1rf4sbak7e@4ax.com>`

```
>From: Robert Wagner robert@wagner.net.yourmammaharvests 
>Date: 9/3/04 9:21 AM Eastern Daylight Time

>
>Most JCL I've seen had one step per job. The hierarchy was up in the
…[4 more quoted lines elided]…
>

Hmmm - I've been in several shops and all had multiple steps per job and
restarts were no big deal (unless someone decided to use && files).  At least 3
of the shops used CA7 which does require human intervention but no editing of
JCL unless there is a substitue dataset required.

Right now I think the longest job we have runs about every 3 minutes and has
300 steps.  I will admit it has the infamous COND all over the place so not all
execute each time the job runs - and I had to change most of them ::sigh::.
```

#### ↳ Re: Flowchart generator for JCL and COBOL programs

- **From:** neerajpeddu <member@mainframeforum.com>
- **Date:** 2004-09-14T19:16:47+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1095189407.b4/MK2TJfOI2QmJwoNM3QA@onlynews>`
- **References:** `<4138329c$0$8979$6c56d894@feed0.news.be.easynet.net>`

```
SEEK is another tool that can be used on PC to generate flow charts for
JCL and COBOL.
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
