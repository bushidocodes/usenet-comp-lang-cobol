[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Status 39

_6 messages · 4 participants · 2004-12 → 2005-01_

---

### Status 39

- **From:** "Euro" <euromercante@sapo.pt>
- **Date:** 2004-12-21T11:40:32
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<41c80bb3$0$1848$a729d347@news.telepac.pt>`

```
Hi,

    We have our software installed in a company, and we are having problems 
when we open the file "Fmatri01" an error message appears indicating  that 
this files has status = 39 and this is happening several times a day. This 
problem never happen before until few days ago. I don�t know if this problem 
is related or not, but it start at the same time when started to use the SP2 
update from Fujitsu Cobol on my computer.
Can anyone help me with this problem???

Thanks
JM
```

#### ↳ Re: Status 39

- **From:** "JerryMouse" <nospam@bisusa.com>
- **Date:** 2004-12-21T08:33:11-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<10sgd0vhou9shb7@news.supernews.com>`
- **References:** `<41c80bb3$0$1848$a729d347@news.telepac.pt>`

```
Euro wrote:
> Hi,
>
…[9 more quoted lines elided]…
> JM

Hmmm. "39" means an existing file does not conform internally to what is 
expected. The most common cause being the file's record definition in the 
executing program does not match the layout of the file as it was created. 
For example:

Creating program:
FD ISAM-FILE.
01  ISAM-REC.
   02  ISAM-KEY  PIC X(10).

Reading program:
FD ISAM-FILE.
01  ISAM-REC.
  02  ISAM-KEY  PIC X(12).

So, then, your first step is to verify that the program that creates the 
file and the program that accesses the file have the same record 
definitions.
```

##### ↳ ↳ Re: Status 39

- **From:** "Thane" <thaneh@softwaresimple.com>
- **Date:** 2004-12-21T07:38:23-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1103643503.755420.298030@c13g2000cwb.googlegroups.com>`
- **In-Reply-To:** `<10sgd0vhou9shb7@news.supernews.com>`
- **References:** `<41c80bb3$0$1848$a729d347@news.telepac.pt> <10sgd0vhou9shb7@news.supernews.com>`

```
This largely depends on the compiler.  Fujitsu, for example, returns a
39 for a corrupt data file.
```

##### ↳ ↳ Re: Status 39

- **From:** "Euro" <euromercante@sapo.pt>
- **Date:** 2004-12-22T12:13:34
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<41c964f2$0$1828$a729d347@news.telepac.pt>`
- **References:** `<41c80bb3$0$1848$a729d347@news.telepac.pt> <10sgd0vhou9shb7@news.supernews.com>`

```
Hi,

    We use an external copybook (*.fd, *.fc), and they have the same record 
definitions.
    When the error message appears I make the recover of the file and the 
application works fine until the next error message appears. I think that 
data file somehow becomes corrupt, the problem is to know what is causing it 
to be corrupt so many times a day.
    I'm thinking it could be because of the SP2 from Fujitsu. I installed it 
in my computer and in the customer computers. I've already compile the 
program in a computer that doesn't have the SP2 installed but the problem 
continues.

Thanks
JM



"JerryMouse" <nospam@bisusa.com> escreveu na mensagem 
news:10sgd0vhou9shb7@news.supernews.com...
> Euro wrote:
>> Hi,
…[32 more quoted lines elided]…
>
```

###### ↳ ↳ ↳ Re: Status 39

- **From:** "Richard" <riplin@Azonic.co.nz>
- **Date:** 2004-12-22T10:28:39-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1103740119.216377.256930@f14g2000cwb.googlegroups.com>`
- **In-Reply-To:** `<41c964f2$0$1828$a729d347@news.telepac.pt>`
- **References:** `<41c80bb3$0$1848$a729d347@news.telepac.pt> <10sgd0vhou9shb7@news.supernews.com> <41c964f2$0$1828$a729d347@news.telepac.pt>`

```
> I'm thinking it could be because of the SP2 from Fujitsu. I installed
it
> in my computer and in the customer computers. I've already compile
the
> program in a computer that doesn't have the SP2 installed but the
problem
> continues.

When you say 'SP2 from Fujitsu', I assume that you mean 'UP2' as in:

""" --------------------------------
Fujitsu NetCOBOL for Windows Version 7 Update Pack 2 - Development
last updated on 11/16/04,8044KB

This is Update Pack 2 for the development version of NetCOBOL for
Windows Version 7. This update includes:

* Support for Windows XP SP2
* All of the fixes in NetCOBOL Update Pack 1
* Misc. other fixes

Installation instructions and a list of Development fixes can be found
<a
href="http://www.netcobol.com/coboldlp/FC-NET/Software/Readme_NetCOBOLV7_UP2.htm">here</a>,
and are provided in readme files included in the download .zip file.
For more information about how Windows XP SP2 affects NetCOBOL please
see this <a
href="http://www.netcobol.com/coboldlp/FC-NET/Software/Readme_Windows_XP_SP2.htm">readme
file</a>, also found in the download .zip file.
---------------------------------------""""

The problem is most likely yet another effect of Windows XP SP2 that
Fujitsu hasn't discovered yet, so you should report this to Fujitsu
support and in the meantime revert to whatever works, which is probably
XP less SP2 and less Fujitsu UP2.
```

###### ↳ ↳ ↳ Re: Status 39

- **From:** "Richard" <riplin@Azonic.co.nz>
- **Date:** 2005-01-02T19:07:26-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1103739897.649954.243030@f14g2000cwb.googlegroups.com>`
- **In-Reply-To:** `<41c964f2$0$1828$a729d347@news.telepac.pt>`
- **References:** `<41c80bb3$0$1848$a729d347@news.telepac.pt> <10sgd0vhou9shb7@news.supernews.com> <41c964f2$0$1828$a729d347@news.telepac.pt>`

```
> I'm thinking it could be because of the SP2 from Fujitsu. I installed
it
> in my computer and in the customer computers. I've already compile
the
> program in a computer that doesn't have the SP2 installed but the
problem
> continues.

When you say 'SP2 from Fujitsu', I assume that you mean 'UP2' as in:

""" --------------------------------
Fujitsu NetCOBOL for Windows Version 7 Update Pack 2 - Development
last updated on 11/16/04,8044KB

This is Update Pack 2 for the development version of NetCOBOL for
Windows Version 7. This update includes:

* Support for Windows XP SP2
* All of the fixes in NetCOBOL Update Pack 1
* Misc. other fixes

Installation instructions and a list of Development fixes can be found
<a
href="http://www.netcobol.com/coboldlp/FC-NET/Software/Readme_NetCOBOLV7_UP2.htm">here</a>,
and are provided in readme files included in the download .zip file.
For more information about how Windows XP SP2 affects NetCOBOL please
see this <a
href="http://www.netcobol.com/coboldlp/FC-NET/Software/Readme_Windows_XP_SP2.htm">readme
file</a>, also found in the download .zip file.
---------------------------------------""""

The problem is most likely yet another effect of Windows XP SP2 that
Fujitsu hasn't discovered yet, so you should report this to Fujitsu
support and in the meantime revert to whatever works, which is probably
XP less SP2 and less Fujitsu UP2.
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
