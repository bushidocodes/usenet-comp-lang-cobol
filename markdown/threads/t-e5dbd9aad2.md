[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Fujitsu COBOL Ver. 3.0

_4 messages · 4 participants · 1999-01_

**Topics:** [`Compilers and vendors`](../topics.md#compilers)

---

### Fujitsu COBOL Ver. 3.0

- **From:** "Ian Stoddart" <Ian@stoddart60.freeserve.co.uk>
- **Date:** 1999-01-04T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<01be381d$953d9280$b311883e@stodfamily.u-net.com>`

```
Hi,

anybody with experience of Fujitsu Ver. 3.0 ?  I have a problem with the
first program I have used this compiler with.  I defined a data field as
PIC X(10).  In the procedure division when using the Accept statement I
cannot use the enter key until I have entered 10 characters !!  I have used
a VALUE clause and also used PIC A.  Initially I forgot to use a VALUE
clause and when added I thought it had worked but it now doesn't though I
think I might have used another compiler at that stage.
Is anybody aware of this with Fujitsu, is there some way round it ?  

Regards,

Ian.
```

#### ↳ Re: Fujitsu COBOL Ver. 3.0

- **From:** "Donald Tees" <donald@willmack.com>
- **Date:** 1999-01-04T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<76rcpe$30p$1@news.igs.net>`
- **References:** `<01be381d$953d9280$b311883e@stodfamily.u-net.com>`

```
About the only way around it is to use the screen section. The
accept/display dataname is as crude as hell.

Ian Stoddart wrote in message
<01be381d$953d9280$b311883e@stodfamily.u-net.com>...
>Hi,
>
…[11 more quoted lines elided]…
>Ian.
```

#### ↳ Re: Fujitsu COBOL Ver. 3.0

- **From:** "Hajo Schepker" <schepker@geocities.com>
- **Date:** 1999-01-08T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<775f6e$idb$2@hermes.btu.de>`
- **References:** `<01be381d$953d9280$b311883e@stodfamily.u-net.com>`

```
Do you work under windows?
Then you can mark a checkbox, hat the return key terminates the accept.

Ian Stoddart schrieb in Nachricht
<01be381d$953d9280$b311883e@stodfamily.u-net.com>...
>Hi,
>
…[11 more quoted lines elided]…
>Ian.
```

##### ↳ ↳ Re: Fujitsu COBOL Ver. 3.0

- **From:** "Dana Brasie" <dbrasie@mindspring.com>
- **Date:** 1999-01-08T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<776ebk$o7m$1@camel21.mindspring.com>`
- **References:** `<01be381d$953d9280$b311883e@stodfamily.u-net.com> <775f6e$idb$2@hermes.btu.de>`

```
You can use 'accept <variable> from console' to enter fewer characters than
defined in the PIC clause.  The example below will demonstrate this.


       IDENTIFICATION DIVISION.
       PROGRAM-ID. CONSOLE-TEST.
       DATA DIVISION.
       WORKING-STORAGE SECTION.

       01  TEST-VAR            PIC X(10) VALUE SPACES.
       01  CHOICE              PIC X(01) VALUE SPACE.

       PROCEDURE DIVISION.
             DISPLAY 'TEST USING "FROM CONSOLE" (Y/N):  '
               WITH NO ADVANCING.
             ACCEPT CHOICE FROM CONSOLE.

             DISPLAY 'ENTER CONSOLE TEST VARIABLE:  ' WITH NO ADVANCING.
             IF FUNCTION UPPER-CASE(CHOICE) = 'Y'
                ACCEPT TEST-VAR  FROM CONSOLE
             ELSE
                MOVE SPACES TO TEST-VAR
                ACCEPT TEST-VAR
             END-IF.

             DISPLAY 'YOUR INPUT = <' TEST-VAR '>'.

             STOP RUN.


Dana


Hajo Schepker wrote in message <775f6e$idb$2@hermes.btu.de>...
>Do you work under windows?
>Then you can mark a checkbox, hat the return key terminates the accept.
…[8 more quoted lines elided]…
>>cannot use the enter key until I have entered 10 characters !!  I have
used
>>a VALUE clause and also used PIC A.  Initially I forgot to use a VALUE
>>clause and when added I thought it had worked but it now doesn't though I
…[7 more quoted lines elided]…
>
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
