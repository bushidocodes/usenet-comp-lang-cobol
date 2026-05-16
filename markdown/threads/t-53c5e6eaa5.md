[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# NT performance question clarified

_3 messages · 2 participants · 2000-10_

---

### NT performance question clarified

- **From:** lynne@nibordesigns.com (Lynne)
- **Date:** 2000-10-17T00:41:36+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<4fNG5.20979$N%1.8497782@news3.rdc1.on.home.com>`

```
There were three test case scenarios.  In all three cases, the data read, 
manipulated and written to the database was identical.  In all three cases, the 
application code was essentially the same.

The application requires a large amount of run-time memory allocated to 
many large arrays.  In all three scenarios, the *structure* of each array was 
the same.  In one case, we minimized the length of the arrays to reduce the 
amount of run-time memory required to run.

The first case was run on the NT server with Oracle.  With full-size arrays, it 
ran at a deplorable speed.

The second case was run on the Win98 laptop.  With full-size arrays it ran in 
1/10th the previous case.

Trying to isolate the problem, we ran just the reads and writes to the database 
and the speed was more than acceptable.  So in the third trial, we minimized 
the array sizes *for* the test sample and it ran almost parallel to the time 
experienced on the laptop.

In order to run at full volume data, we need to bump the array sizes back up.  
But it won't run acceptably.  I do not see that it is a database problem 
because we've isolated those processes and found them to be sound.

I believe the problem to be that we've somehow run out of run-time memory and 
the application is caching or paging out.  I believe there is enough RAM, so 
wonder what we need to do to prevent the caching.

Thanks to all who have answered thus far!
Lynne
```

#### ↳ Re: NT performance question clarified

- **From:** thaneH@softwaresimple.com (Thane Hubbell)
- **Date:** 2000-10-17T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<39ec3edd.566869493@207.126.101.100>`
- **References:** `<4fNG5.20979$N%1.8497782@news3.rdc1.on.home.com>`

```
I missed the original message.  Three Questions:

What vendor's COBOL are you using, and what version?

Second How much RAM in the NT machine, and is it Server or
WorkStation?

On Tue, 17 Oct 2000 00:41:36 GMT, lynne@nibordesigns.com (Lynne)
wrote:

>There were three test case scenarios.  In all three cases, the data read, 
>manipulated and written to the database was identical.  In all three cases, the 
…[28 more quoted lines elided]…
>

---
Try a better search engine:  http://www.google.com
My personal web site: http://www.geocities.com/Eureka/2006/
```

#### ↳ Re: NT performance question clarified

- **From:** thaneH@softwaresimple.com (Thane Hubbell)
- **Date:** 2000-10-17T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<39ec413f.567479487@207.126.101.100>`
- **References:** `<4fNG5.20979$N%1.8497782@news3.rdc1.on.home.com>`

```
I found the original message.  Can you change the database on the NT
machine to access an Access database instead of the Oracle (and stop
the Oracle service when you do it).

I'm assuming that Oracle is running locally on the NT box - you will
need to stop this service.  Actually, Oracle is going to take quite a
lot of memory overhead - it should run on a separate server from the
application.  You very well could be in a memory swapping situation on
NT and not on Windows 98 only because Oracle is running on NT, but not
on the Win98 box.  We are still pretty far from comparing apples and
apples.


On Tue, 17 Oct 2000 00:41:36 GMT, lynne@nibordesigns.com (Lynne)
wrote:

>There were three test case scenarios.  In all three cases, the data read, 
>manipulated and written to the database was identical.  In all three cases, the 
…[28 more quoted lines elided]…
>

---
Try a better search engine:  http://www.google.com
My personal web site: http://www.geocities.com/Eureka/2006/
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
