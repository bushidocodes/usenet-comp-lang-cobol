[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Deleteing a file inside a Cobol program

_9 messages · 7 participants · 2006-10_

---

### Deleteing a file inside a Cobol program

- **From:** jeff@sum-it.com
- **Date:** 2006-10-11T09:35:11-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1160584511.385814.13500@k70g2000cwa.googlegroups.com>`

```
Is there a system call or something I can use to delete a file from a
unix directory? I have a program that calls another program that
deletes a list of  files, I need to be able to delete the from the
directory as well. They are in a subdir called reports. Any help would
be appreciated
```

#### ↳ Re: Deleteing a file inside a Cobol program

- **From:** Alain Reymond <arwebmail@skynet.be>
- **Date:** 2006-10-11T19:02:04+02:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<452d2331$0$21498$ba620e4c@news.skynet.be>`
- **In-Reply-To:** `<1160584511.385814.13500@k70g2000cwa.googlegroups.com>`
- **References:** `<1160584511.385814.13500@k70g2000cwa.googlegroups.com>`

```
jeff@sum-it.com a ï¿½crit :
> Is there a system call or something I can use to delete a file from a
> unix directory? I have a program that calls another program that
…[3 more quoted lines elided]…
> 
You can use :
call "CBL_DELETE_FILE" using     filename
                       returning status-code

And

call "CBL_DELETE_DIR" using	     path-name
                      returning status-code

for a directory.

Regards.

Alain
```

##### ↳ ↳ Re: Deleteing a file inside a Cobol program

- **From:** jeff@sum-it.com
- **Date:** 2006-10-11T10:37:54-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1160588274.182465.14620@e3g2000cwe.googlegroups.com>`
- **In-Reply-To:** `<452d2331$0$21498$ba620e4c@news.skynet.be>`
- **References:** `<1160584511.385814.13500@k70g2000cwa.googlegroups.com> <452d2331$0$21498$ba620e4c@news.skynet.be>`

```
Thank you!!




Alain Reymond wrote:
> jeff@sum-it.com a écrit :
> > Is there a system call or something I can use to delete a file from a
…[18 more quoted lines elided]…
> Alain
```

###### ↳ ↳ ↳ Re: Deleteing a file inside a Cobol program

- **From:** "HeyBub" <heybubNOSPAM@gmail.com>
- **Date:** 2006-10-12T09:34:33-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<12iskjefnai4532@news.supernews.com>`
- **References:** `<1160584511.385814.13500@k70g2000cwa.googlegroups.com> <452d2331$0$21498$ba620e4c@news.skynet.be> <1160588274.182465.14620@e3g2000cwe.googlegroups.com>`

```
jeff@sum-it.com wrote:
> Thank you!!
>
…[21 more quoted lines elided]…
>>

Beware of filenames/paths containing imbedded spaces. Fujitsu has an 
enhanced CBL routine for such:

CBL_DELETE_FILE2 USING...
```

##### ↳ ↳ Re: Deleteing a file inside a Cobol program

- **From:** "William M. Klein" <wmklein@nospam.netcom.com>
- **Date:** 2006-10-11T17:56:04+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<UeaXg.30016$aE2.16016@fe04.news.easynews.com>`
- **References:** `<1160584511.385814.13500@k70g2000cwa.googlegroups.com> <452d2331$0$21498$ba620e4c@news.skynet.be>`

```
For this solution to work, you need to be using a compiler that supports "CBL_" 
routines.  Micro Focus originated these and Fujitsu has "emulation" routines.  I 
don't think any other COBOL Unix compiler would have them.
```

##### ↳ ↳ Re: Deleteing a file inside a Cobol program

- **From:** "Richard" <riplin@Azonic.co.nz>
- **Date:** 2006-10-11T11:11:28-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1160590288.543650.295190@c28g2000cwb.googlegroups.com>`
- **In-Reply-To:** `<452d2331$0$21498$ba620e4c@news.skynet.be>`
- **References:** `<1160584511.385814.13500@k70g2000cwa.googlegroups.com> <452d2331$0$21498$ba620e4c@news.skynet.be>`

```

Alain Reymond wrote:

> You can use :
> call "CBL_DELETE_FILE" using     filename
…[7 more quoted lines elided]…
> for a directory.

Only if they have an appropriate version of MicroFocus COBOL or a
derivitive.
```

#### ↳ Re: Deleteing a file inside a Cobol program

- **From:** Frederico Fonseca <real-email-in-msg-spam@email.com>
- **Date:** 2006-10-11T19:39:03+01:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<cnbqi2lfiuim9qvp2vc8ovh7cbds0ead5d@4ax.com>`
- **References:** `<1160584511.385814.13500@k70g2000cwa.googlegroups.com>`

```
On 11 Oct 2006 09:35:11 -0700, jeff@sum-it.com wrote:

>Is there a system call or something I can use to delete a file from a
>unix directory? I have a program that calls another program that
>deletes a list of  files, I need to be able to delete the from the
>directory as well. They are in a subdir called reports. Any help would
>be appreciated
Which OS, COBOL Vendor and version?


Frederico Fonseca
ema il: frederico_fonseca at syssoft-int.com
```

##### ↳ ↳ Re: Deleteing a file inside a Cobol program

- **From:** jeff@sum-it.com
- **Date:** 2006-10-11T12:32:11-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1160595131.121467.199510@i3g2000cwc.googlegroups.com>`
- **In-Reply-To:** `<cnbqi2lfiuim9qvp2vc8ovh7cbds0ead5d@4ax.com>`
- **References:** `<1160584511.385814.13500@k70g2000cwa.googlegroups.com> <cnbqi2lfiuim9qvp2vc8ovh7cbds0ead5d@4ax.com>`

```
Thank everybody for there help. Alain's solution worked fine. I am
running AcuCobol 7.2 on a Solaris box. Thanks again for everyone's
help!!!!

Frederico Fonseca wrote:
> On 11 Oct 2006 09:35:11 -0700, jeff@sum-it.com wrote:
>
…[9 more quoted lines elided]…
> ema il: frederico_fonseca at syssoft-int.com
```

#### ↳ Re: Deleteing a file inside a Cobol program

- **From:** "Alistair" <alistair@ld50macca.demon.co.uk>
- **Date:** 2006-10-11T13:21:09-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1160598069.181043.47640@m73g2000cwd.googlegroups.com>`
- **In-Reply-To:** `<1160584511.385814.13500@k70g2000cwa.googlegroups.com>`
- **References:** `<1160584511.385814.13500@k70g2000cwa.googlegroups.com>`

```

jeff@sum-it.com wrote:
> Is there a system call or something I can use to delete a file from a
> unix directory? I have a program that calls another program that
> deletes a list of  files, I need to be able to delete the from the
> directory as well. They are in a subdir called reports. Any help would
> be appreciated

If you have a list of files then you should be able to feed the list
into a Unix script call which would delete each listed file.
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
