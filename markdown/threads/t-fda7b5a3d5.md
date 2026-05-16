[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# MS Cobol4.5 help

_3 messages · 3 participants · 1999-12_

---

### MS Cobol4.5 help

- **From:** "Roy Shao" <Roy.Shao@amd.com>
- **Date:** 1999-12-29T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<84cbi1$cn8$1@amdint2.amd.com>`

```
Hi, I get a MS Cobol 4.5 which under DOS.
when i use "Cobol" to compile the file,
"Cobol run time library not installed" error message appeared.

can you tell me how can i use the cobol normally ?
thanks.
```

#### ↳ Re: MS Cobol4.5 help

- **From:** "James J. Gavan" <jjgavan@home.com>
- **Date:** 1999-12-29T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<386A78F4.E9EB5A6A@home.com>`
- **References:** `<84cbi1$cn8$1@amdint2.amd.com>`

```


Roy Shao wrote:
> 
> Hi, I get a MS Cobol 4.5 which under DOS.
…[4 more quoted lines elided]…
> thanks.

Boy, are you SOL - Microsoft no longer supports it. Do you know for sure
you have the complete package installed. If you have manuals and
diskettes check that you have necessary entries in your autoexec.bat
'pointing' to necessary path names. Given you have all the materials it
might be worth the effort of doing a re-install on the software which
will prompt to add entries to your autoexec.bat.

For assistance, check deja.com for old messages for this News Group -
from memory there were two people using M/S COBOL, one in Czechoslovakia
and the other in Italy - they may give you guidance.

I still use the Editor from their Version 5 - so the following
autoexec.bat entries might give you some guidance :-

SET COBDIR=C:\MSCOB50\BIN;
SET LIB=C:\MSCOB50\LIB;
SET INCLUDE=C:\MSCOB50\SOURCE;
SET HELPFILES=C:\MSCOB50\HELP;
SET INIT=C:\MSCOB50\INIT;
C:\WINDOWS;C:\WINDOWS\COMMAND;C:\PROGRA~1\NORTON~1;C:\MSCOB50\BIN;c:\batch


Jimmy, Calgary AB
```

#### ↳ Re: MS Cobol4.5 help

- **From:** "donald tees" <donald@willmack.com>
- **Date:** 1999-12-29T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<84e0l0$bv$1@news.igs.net>`
- **References:** `<84cbi1$cn8$1@amdint2.amd.com>`

```
You need the file COBLIB.DLE in your path.

Roy Shao wrote in message <84cbi1$cn8$1@amdint2.amd.com>...
>Hi, I get a MS Cobol 4.5 which under DOS.
>when i use "Cobol" to compile the file,
…[6 more quoted lines elided]…
>
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
