[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Email from m/f Batch

_3 messages · 2 participants · 2004-09_

---

### Email from m/f Batch

- **From:** Old Mainframer <member@mainframeforum.com>
- **Date:** 2004-09-14T08:36:43+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1095151003.oRbv2jKJ10W16W4wC5AycA@onlynews>`

```
Does anyone know of how to send an email (to multiple recipients) from
within a mainframe program ? Does it have to be written to a file for
JCL to send or can it be done directly ? Either way, examples of code
welcomed !
```

#### ↳ Re: Email from m/f Batch

- **From:** Hans Kok <member@mainframeforum.com>
- **Date:** 2004-09-14T12:37:03+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1095165423.Cdg4WrVkhIc4xW+yrqP6NA@onlynews>`
- **References:** `<1095151003.oRbv2jKJ10W16W4wC5AycA@onlynews>`

```
We used this jcl:

//GENMAIL EXEC PGM=IEBGENER //SYSUT1 DD *


  TEST THIS IS LINE 1 TEST THIS IS LINE 2 TEST THIS IS LINE 3


//SYSUT2 DD DSN=HLQ.DISTNEW.MAIL,DISP=(,CATLG), // SPACE=(TRK,5)
//SYSPRINT DD SYSOUT=* //SYSIN DD DUMMY
//*-----------------------------------------------------------
//SENDMAIL EXEC PGM=IKJEFT01,DYNAMNBR=20 //SYSTSPRT DD SYSOUT=*
//SYSPRINT DD SYSOUT=* //SYSEXEC DD DISP=SHR,DSN=SYS1.ISPCLIB //SYSTSIN
DD * SMTPNOTE SUBJECT(TESTMAIL) BATCH - TO(RECEIVER@MAIL.BLABLA.COM) -
DATASET('HLQ.DISTNEW.MAIL')
//*----------------------------------------------------------- //DELMAIL
EXEC PGM=IEFBR14 //DD1 DD DISP=(OLD,DELETE,DELETE),DSN=HLQ.DISTNEW.MAIL


You must have a SMTP server installed of course.
```

#### ↳ Re: Email from m/f Batch

- **From:** Joe Zitzelberger <joe_zitzelberger@nospam.com>
- **Date:** 2004-09-14T18:45:56-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<joe_zitzelberger-22F9F5.18455614092004@knology.usenetserver.com>`
- **References:** `<1095151003.oRbv2jKJ10W16W4wC5AycA@onlynews>`

```
In article <1095151003.oRbv2jKJ10W16W4wC5AycA@onlynews>,
 Old Mainframer <member@mainframeforum.com> wrote:

> Does anyone know of how to send an email (to multiple recipients) from
> within a mainframe program ? Does it have to be written to a file for
…[6 more quoted lines elided]…
> posted via MFF :  http://www.MainFrameForum.com - USENET Gateway

Depends.  From a batch job, the simplest way is to write to the started 
SMTP task.  If your SMTP task is named SMTPXYZ, they you would code in 
your JCL:

   //MAILMSG  DD  SYSOUT=(B,SMTPXYZ)

The sysout class must be the one configured for your SMTP task, and the 
writer name must me the started task name.  Other than that, just format 
it like any mail message.  E.g.

   HELO SMTPXYZ
   RCPT TO soandso@wherever.com
   FROM you@yourplace.com
   SUBJECT Test
   Test
   .

From CICS, you can use the SPOOLOPEN, SPOOLWRITE, SPOOLCLOSE commands to 
route to the SMTP task the same way.
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
