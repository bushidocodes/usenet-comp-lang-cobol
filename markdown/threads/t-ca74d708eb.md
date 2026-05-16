[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# AIX IBM Cobol Set and VSAM Files

_2 messages · 2 participants · 2003-03_

**Topics:** [`Compilers and vendors`](../topics.md#compilers) · [`VSAM, files, sorting`](../topics.md#files)

---

### AIX IBM Cobol Set and VSAM Files

- **From:** michael.bierenfeld@web.de (michael)
- **Date:** 2003-03-26T04:01:54-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<f11c8440.0303260401.75748f27@posting.google.com>`

```
Hi there,

I am using IBM Cobol for AIX and I am stuck while accessing VSAM
Files.

The following Code

       FILE-CONTROL. 
           SELECT RK-EIN       ASSIGN USING RK-EIN-NAME 
                               FILE STATUS IS F-STATUS.

...

       FD  RK-EIN 
           DATA RECORD IS BLESAVE-DATEN. 
           COPY 'BLESAVE.cpy'. 

..

       01  RK-EIN-NAME0            PIC X(12) VALUE 'RK.dat'. 

RK-EIN-NAME is concatenated with the path to eg.

'/home/lvmbi/rk/quellen/RK.dat'

When I try to open the file with OPEN INPUT RK-EIN the system issues
F-STATUS 35 which means 'File not found'. The File is there for sure.
The Dokumentation speaks something about using some strange ("as for a
C/Java/C++ Programmer") namingconventions like 'VSAM-RK.dat' or
'STL-RK.dat'. Strangly enough using
'STL-/home/lvmbi/rk/quellen/RK.dat' results in finding the file but as
it is a VSAM File copied from another station I receive some data
mismatch errors like corrupted File Header etc. Using
'VSAM-/home/lvmbi/quellen/rk/RK.dat' results in Filenot found.

I have no clue and if somebody knows the secret pls let me know.

Regards

Michael
```

#### ↳ Re: AIX IBM Cobol Set and VSAM Files

- **From:** "Peter E.C. Dashwood" <dashwood@enternet.co.nz>
- **Date:** 2003-03-27T01:47:07
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3e825823_2@127.0.0.1>`
- **References:** `<f11c8440.0303260401.75748f27@posting.google.com>`

```
 Try replacing USING with TO ...

Pete

"michael" <michael.bierenfeld@web.de> wrote in message
news:f11c8440.0303260401.75748f27@posting.google.com...
> Hi there,
>
…[37 more quoted lines elided]…
> Michael




----== Posted via Newsfeed.Com - Unlimited-Uncensored-Secure Usenet News==----
http://www.newsfeed.com The #1 Newsgroup Service in the World! >100,000 Newsgroups
---= 19 East/West-Coast Specialized Servers - Total Privacy via Encryption =---
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
