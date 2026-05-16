[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Despate help needed with MF COBOL & Win98

_6 messages · 6 participants · 1999-09_

**Topics:** [`Compilers and vendors`](../topics.md#compilers)

---

### Despate help needed with MF COBOL & Win98

- **From:** "Richard Dixon" <rdixon@nildram.co.uk>
- **Date:** 1999-09-11T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<37d95c2a@glitch.nildram.co.uk>`

```
I am using Microfocus Personal COBOL Student Edition (for DOS not Windows).
I was previously running MF COBOL under Windows 95 without any problems. I
have now upgraded to Windows 98 and cannot get it to run at all. I have
tried it in MS-DOS Prompt and properly in MS-DOS without success. I get the
message :- This Program tried to execute an invalid instruction .
Fault Location FFFF:3318
Interrupts In Service None.
I do not believe that this is a memory problem and I have I checked
CONFIG.SYS and AUTOEXEC.BAT which both seem OK. I have contacted the makers
of my new computer and they seem to think that everything is OK with DOS (of
course they would!). The MS-DOS is version WINDOWS 98 (4.10.1998).
I have also downloaded the fix from the Merant web site and used this
without success.

Does anyone have any ideas on how to get this working??/

If you can help would you mind e-mailing me direct rdixon@nildam.co.uk


Thanks in advance for any help
```

#### ↳ Re: Despate help needed with MF COBOL & Win98

- **From:** "TPF Moderator" <tpf_moderator@hotmail.com>
- **Date:** 1999-09-11T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7rdsdb$mi7$1@linuxfr.org>`
- **References:** `<37d95c2a@glitch.nildram.co.uk>`

```
Howdy

You much check to see if the app is certified for Win98. Some bad code was
written to port 3.11 onto Win95 but Win98 ties the notch one more time and
maybe your version has tryied to access a deprecated API that returns NULL
thus causing the AV you described.

Regards
Andre

Richard Dixon <rdixon@nildram.co.uk> wrote in message
news:37d95c2a@glitch.nildram.co.uk...
> I am using Microfocus Personal COBOL Student Edition (for DOS not
Windows).
> I was previously running MF COBOL under Windows 95 without any problems. I
> have now upgraded to Windows 98 and cannot get it to run at all. I have
> tried it in MS-DOS Prompt and properly in MS-DOS without success. I get
the
> message :- This Program tried to execute an invalid instruction .
> Fault Location FFFF:3318
> Interrupts In Service None.
> I do not believe that this is a memory problem and I have I checked
> CONFIG.SYS and AUTOEXEC.BAT which both seem OK. I have contacted the
makers
> of my new computer and they seem to think that everything is OK with DOS
(of
> course they would!). The MS-DOS is version WINDOWS 98 (4.10.1998).
> I have also downloaded the fix from the Merant web site and used this
…[10 more quoted lines elided]…
>
```

#### ↳ Re: Despate help needed with MF COBOL & Win98

- **From:** Strider <strider@gv2.net>
- **Date:** 1999-09-24T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<xwLrN7Mb20dr2NHsdXf4DwO8XX5Y@4ax.com>`
- **References:** `<37d95c2a@glitch.nildram.co.uk>`

```
Dude can you post the files for that compiler for me? I really need
it... I don't have a good compiler argh!...

On Sat, 11 Sep 1999 20:21:23 +0100, "Richard Dixon"
<rdixon@nildram.co.uk> wrote:

>I am using Microfocus Personal COBOL Student Edition (for DOS not Windows).
>I was previously running MF COBOL under Windows 95 without any problems. I
…[19 more quoted lines elided]…
>
```

##### ↳ ↳ Re: Despate help needed with MF COBOL & Win98

- **From:** "Michael Mattias" <michael.mattias@gte.net>
- **Date:** 1999-09-24T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<%DNG3.385$MQ.9634@dfiatx1-snr1.gtei.net>`
- **References:** `<37d95c2a@glitch.nildram.co.uk> <xwLrN7Mb20dr2NHsdXf4DwO8XX5Y@4ax.com>`

```
Microfocus Personal COBOL Student Edition is copyright software, and may not
be legally distributed except by authorized agents of the copyright owner.

Licensing a copy of the compiler does not make one an agent of the copyright
owner.

MCM


Strider wrote in message ...
>Dude can you post the files for that compiler for me? I really need
>it... I don't have a good compiler argh!...
…[4 more quoted lines elided]…
>>I am using Microfocus Personal COBOL Student Edition (for DOS not
Windows).
```

###### ↳ ↳ ↳ Re: Despate help needed with MF COBOL & Win98

- **From:** "Simon R Hart" <hart1@technologist.com>
- **Date:** 1999-09-25T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<01bf0795$a7d5ee40$dd648cd4@default>`
- **References:** `<37d95c2a@glitch.nildram.co.uk> <xwLrN7Mb20dr2NHsdXf4DwO8XX5Y@4ax.com> <%DNG3.385$MQ.9634@dfiatx1-snr1.gtei.net>`

```


Michael Mattias <michael.mattias@gte.net> wrote in article
<%DNG3.385$MQ.9634@dfiatx1-snr1.gtei.net>...
> Microfocus Personal COBOL Student Edition is copyright software, and may
not
> be legally distributed except by authorized agents of the copyright
owner.
> 
> Licensing a copy of the compiler does not make one an agent of the
copyright
> owner.
> 
> MCM
> 

Else FAST will be round the corner.............

Simon R Hart
Eaton.
```

##### ↳ ↳ Re: Despate help needed with MF COBOL & Win98

- **From:** coboljit@aol.com (COBOLJIT)
- **Date:** 1999-09-27T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<19990927151950.12041.00001279@ngol03.aol.com>`
- **References:** `<xwLrN7Mb20dr2NHsdXf4DwO8XX5Y@4ax.com>`

```
Contact Microfocus support - fax 650-404-7188 or pcobsup@microfocus.com
Helen
In article <xwLrN7Mb20dr2NHsdXf4DwO8XX5Y@4ax.com>, Strider <strider@gv2.net>
writes:

>Subject:	Re: Despate help needed with MF COBOL & Win98
>From:	Strider <strider@gv2.net>
…[30 more quoted lines elided]…
>


Helen

------------------------------------------------------------------------------
King Computer Services, Inc.
COBOL Training for the Year 2000
"COBOL, Just in Time" Crash Course
"COBOL, Dates and the Year 2000" Technical Reference.
818-951-5240
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
