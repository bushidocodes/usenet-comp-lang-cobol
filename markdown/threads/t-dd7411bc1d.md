[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# COBOL, JCL and OS/390

_4 messages · 4 participants · 2003-02_

**Topics:** [`Mainframe, z/OS, JCL, CICS`](../topics.md#mainframe)

---

### COBOL, JCL and OS/390

- **From:** "Max Boettner" <max.boettner@t-online.de>
- **Date:** 2003-02-03T01:41:07+01:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<b1kdvh$56d$02$1@news.t-online.com>`

```
Anybody that can explain with an example the use of  DYNAMIC FILE ALLOCATION
?

Thank for alls

MAXimo
```

#### ↳ Re: COBOL, JCL and OS/390

- **From:** "William M. Klein" <wmklein@ix.netcom.com>
- **Date:** 2003-02-02T19:18:11-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<b1kg0n$tp1$1@slb6.atl.mindspring.net>`
- **References:** `<b1kdvh$56d$02$1@news.t-online.com>`

```
I thought that there was an "easy" example online, but I don't find it at
the moment.  Assuming you are using the "latest" IBM compiler (Enterprise
COBOL - either V3R1 or V3R1), you can find an example of using "putenv" at:


http://publibz.boulder.ibm.com/cgi-bin/bookmgr_OS390/BOOKS/igy3pg10/3.4.2.4

and the information on WHAT to put in the evnironment variable at:


http://publibz.boulder.ibm.com/cgi-bin/bookmgr_OS390/BOOKS/igy3lr10/4.2.3.1

If you are *not* using the latest compiler, there are some other solutions -
that you should be able to find by searching this newsgroup via google for
"dynamic allocation"
```

#### ↳ Re: COBOL, JCL and OS/390

- **From:** "Ron" <NoSoy@swbell.net>
- **Date:** 2003-02-02T22:15:53-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<b1kqdq$h6c$1@ngspool-d02.news.aol.com>`
- **References:** `<b1kdvh$56d$02$1@news.t-online.com>`

```
This is a sample allocating a GDG. Modify as needed
according to the manual specs.

 CBL NODYNAM
       identification division.
       program-id. jpcobtst.
       environment division.
       input-output section.
       file-control.
           select test-file
             assign to DYNAMDD
             file status is test-status.
       data division.
       file section.
       fd  test-file
           label records are standard
           recording mode is F
           block contains 0 records.
       01  test-record pic x(80).
       working-storage section.
       01  test-status        pic xx.
       01  rc                 pic 9(9) comp.
       01  rc-display         pic 9(9).
       01  addr-pointer       usage is pointer.
       01  dynalloc.
           05 filler          pic x(12)  value
           'DYNAMDD=DSN('.
           05 dyn-dsn         pic x(46).
           05 filler          pic x(90)  value
           'NEW TRACKS SPACE(1,1) CATALOG STORCLAS(STANDARD) MGMTCLAS(WO
      -    'RK)  '.
       procedure division.
       mission-control.
           set addr-pointer to address of dynalloc.
      *
      ***  test1
      *
           move 'D5.P.NOR.GDGTEST(+1))' to dyn-dsn.
           call 'putenv'
             using by value addr-pointer
             returning rc.
           if rc not = zero
               move rc to rc-display
               display 'putenv failed, rc = ' rc-display
               goback.
           open output test-file.
           if test-status not = '00'
               display 'open error test 1, status ' test-status
               goback.
           move 'This is a test record' to test-record.
           write test-record.
           close test-file
      *
      ***  test2 (Reuse the DD)
      *
           move 'D5.P.NOR.GDGTEST2(+1))' to dyn-dsn.
           call 'putenv'
             using by value addr-pointer
             returning rc.
           if rc not = zero
               move rc to rc-display
               display 'putenv failed, rc = ' rc-display
               goback.
           open output test-file.
           if test-status not = '00'
               display 'open error test 2, status ' test-status
               goback.
           move 'This is a test record' to test-record.
           write test-record.
           close test-file
           goback.
```

##### ↳ ↳ Re: COBOL, JCL and OS/390

- **From:** "Roland Schiradin" <schiradi@tap.de>
- **Date:** 2003-02-12T22:42:56+01:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<b2ef5v$9c$1@innferno.news.tiscali.de>`
- **References:** `<b1kdvh$56d$02$1@news.t-online.com> <b1kqdq$h6c$1@ngspool-d02.news.aol.com>`

```
Ron,

dynalloc should be null-terminated.

>        01  dynalloc.
>            05 filler          pic x(12)  value
>            'DYNAMDD=DSN('.
>            05 dyn-dsn         pic x(46).
>            05 filler          pic x(90)  value
Z"NEW TRACKS SPACE(1,1) CATALOG STORCLAS(STANDARD) MGMTCLAS(WO
-    'RK)  ".

Roland


"Ron" <NoSoy@swbell.net> schrieb im Newsbeitrag
news:b1kqdq$h6c$1@ngspool-d02.news.aol.com...
> This is a sample allocating a GDG. Modify as needed
> according to the manual specs.
…[70 more quoted lines elided]…
>
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
