[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Sending Mail From Cobol

_9 messages · 7 participants · 2003-09 → 2004-03_

---

### Sending Mail From Cobol

- **From:** dipu <member37866@dbforums.com>
- **Date:** 2003-09-03T04:27:48-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3323031.1062577668@dbforums.com>`

```

Is there some standard IBM supplied API that can be used to send email
from a MAINFRAME COBOL PROGRAM ?
```

#### ↳ Re: Sending Mail From Cobol

- **From:** "Harley" <dennis.harleyNoSpam@worldnet.att.net>
- **Date:** 2003-09-03T12:02:55+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<PLk5b.124085$0v4.9016260@bgtnsc04-news.ops.worldnet.att.net>`
- **References:** `<3323031.1062577668@dbforums.com>`

```

"dipu" <member37866@dbforums.com> wrote in message
news:3323031.1062577668@dbforums.com...
|
| Is there some standard IBM supplied API that can be used to send email
| from a MAINFRAME COBOL PROGRAM ?
|

If you're on an IBM OS/390 or z/OS, scan your JCL, PROC, and control
libraries for SMTP.

You might also scan the control library for @, to look for e-mail addresses.

Also check SDSF for anything starting with SMTP.

If it's already being used, you should be able to figure out how to use it.
```

#### ↳ Re: Sending Mail From Cobol

- **From:** Joe Zitzelberger <joe_zitzelberger@nospam.com>
- **Date:** 2003-09-03T08:03:39-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<joe_zitzelberger-A32C03.08033903092003@corp.supernews.com>`
- **References:** `<3323031.1062577668@dbforums.com>`

```
In article <3323031.1062577668@dbforums.com>,
 dipu <member37866@dbforums.com> wrote:

> Is there some standard IBM supplied API that can be used to send email
> from a MAINFRAME COBOL PROGRAM ?
> 

Depends on the way your shop has SMTP configured.  You can usually spool 
mail message to the SMTP started task and everything else is automagick.

You will need:

   - the name of the started task for the SMTP you wish to use.  By 
default this is SMTP.

   - the output class that your sysprogs have defined.  By default this 
is class B.

   - permission to use SMTP if RACF or allow/deny have been configured 
for SMTP.

Your output DD statement will look like:

   //YOURMAIL  DD  SYSOUT=(x,yyyyyyyy)  

where x = output class and yyyyyyyy = started task name for SMTP.

Just write your email to the YOURMAIL dd in the standard email style and 
you are done, e.g.:

   HELO jes-node-name
   RCPT TO  you@yoursite.com
   DATA
   Test
   .

You can do the same from CICS using the SPOOL OPEN/WRITE/CLOSE.  Use an 
output descriptor on the SPOOL OPEN command of (B,SMTP) and your mails 
will be sent.
```

#### ↳ Re: Sending Mail From Cobol

- **From:** thaneh@softwaresimple.com (Thane Hubbell)
- **Date:** 2003-09-03T09:57:09-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<bfdfc3e8.0309030857.14a6f7e8@posting.google.com>`
- **References:** `<3323031.1062577668@dbforums.com>`

```
Mainframe OS version?

dipu <member37866@dbforums.com> wrote in message news:<3323031.1062577668@dbforums.com>...
> Is there some standard IBM supplied API that can be used to send email
> from a MAINFRAME COBOL PROGRAM ?
```

#### ↳ Re: Sending Mail From Cobol

- **From:** dipu <member37866@dbforums.com>
- **Date:** 2003-09-04T00:49:33-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3328249.1062650973@dbforums.com>`
- **References:** `<3323031.1062577668@dbforums.com>`

```

OS Version is OS/390.I also want to add attachement.
```

##### ↳ ↳ Re: Sending Mail From Cobol

- **From:** thaneh@softwaresimple.com (Thane Hubbell)
- **Date:** 2003-09-04T06:00:55-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<bfdfc3e8.0309040500.3a34b97e@posting.google.com>`
- **References:** `<3323031.1062577668@dbforums.com> <3328249.1062650973@dbforums.com>`

```
dipu <member37866@dbforums.com> wrote in message news:<3328249.1062650973@dbforums.com>...
> OS Version is OS/390.I also want to add attachement.

Which VERSION of OS/390?  This determines the level of default unix
serives installed as either "Open Edition", "USS" or maybe even LINUX
- and will help determine what is available to you.  Hopefully the
other messages on your thread have given you the answer you seek.

Curious though - what are you going to attach?  What could possibly
exist on the mainframe that you can attach that would be of use on the
PC?  There's a whole EBCDIC/ASCII issue to consider especially if you
get into MIME binary attachments.
```

#### ↳ Re: Sending Mail From Cobol

- **From:** weberm@polaris.net (Ubiquitous)
- **Date:** 2003-09-04T18:11:53+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<bj7v99$d3k$3@news.utelfla.com>`
- **References:** `<3323031.1062577668@dbforums.com>`

```
dipu <member37866@dbforums.com> wrote:

: Is there some standard IBM supplied API that can be used to send email
: from a MAINFRAME COBOL PROGRAM ?

I would think there is, since I have JCL which does just that.
```

#### ↳ Re: Sending Mail From Cobol

- **From:** superk <member@mainframeforum.com>
- **Date:** 2004-03-04T19:26:31+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<d0c2386cd6c6253887d94ede04eef4a8@news.onlynews.com>`
- **References:** `<3323031.1062577668@dbforums.com>`

```
Thane Hubbell  wrote:
  > Curious though - what are you going to attach? What could possibly exist
  > on the mainframe that you can attach that would be of use on the PC?
  > There's a whole EBCDIC/ASCII issue to consider especially if you get
  > into MIME binary attachments.
We regularly e-mail RTF and PDF documents that we have generated on
the mainframe to groups of recipients for viewing on the desktop with
Word or Adobe.
```

##### ↳ ↳ Re: Sending Mail From Cobol

- **From:** Frederico Fonseca <real-email-in-msg-spam@email.com>
- **Date:** 2004-03-04T21:02:50+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<i86f40dcg46bpdhs8h0knbav51h9uedsuk@4ax.com>`
- **References:** `<3323031.1062577668@dbforums.com> <d0c2386cd6c6253887d94ede04eef4a8@news.onlynews.com>`

```
On Thu, 04 Mar 2004 19:26:31 GMT, superk <member@mainframeforum.com>
wrote:

>Thane Hubbell  wrote:
>  > Curious though - what are you going to attach? What could possibly exist
…[5 more quoted lines elided]…
>Word or Adobe.

And to add to this you can create ZIP files that are fully compatible
with normal "PC" zip (e.g. winzip and others), and that does all the
conversion from EBCDIC to ASCII.





Frederico Fonseca
ema il: frederico_fonseca at syssoft-int.com
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
