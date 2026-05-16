[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# vutil question

_6 messages · 3 participants · 2003-07_

---

### vutil question

- **From:** "nospam" <bruceradtke@REMOVEspamREMOVE.earthlink.net>
- **Date:** 2003-07-18T15:53:05+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<BJURa.9624$Mc.684883@newsread1.prod.itd.earthlink.net>`

```
Hello all -

I need help in extracting data from AcuCobol database files into a readable
format.  I'm not a Cobol programmer and could use your help.

I've tried  "vutil -unload -v -t  MYFILE > myfile.txt".    This does dump
the file except I don't recognize the numeric format.

I'm not sure what the "-extract" option does or how it works.  It asks me
the index key and number of records to dump.   If I just carriage return
past these prompts,  the program appears to be idle.

How can I use the vutil utility to dump some AcuCobol proprietary database
files to an ASCII text file?

Thanks in advance,

bruce
bruceradtke@earthlink.net.NOSPAMPLEASE
```

#### ↳ Re: vutil question

- **From:** gmspano <member9303@dbforums.com>
- **Date:** 2003-07-19T06:18:15+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3129209.1058595495@dbforums.com>`
- **References:** `<BJURa.9624$Mc.684883@newsread1.prod.itd.earthlink.net>`

```

Hi

Do you need to extract data from an indexed file or a database?

Vutil.exe can be used to extract records in line sequential format from
an indexed file..the command is:

VUTIL -E myindexed_file  > myfile.txt

If you have a line sequential file and you want to store its data on an
empty indexed file you can reverse the command like:

Vutil -load -t -r mydata.txt  myindexed.inx

Hope in this help

Gianni
```

##### ↳ ↳ Re: vutil question

- **From:** "nospam" <bruceradtke@REMOVEspamREMOVE.earthlink.net>
- **Date:** 2003-07-19T12:51:48+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<E9bSa.11535$Mc.812136@newsread1.prod.itd.earthlink.net>`
- **References:** `<BJURa.9624$Mc.684883@newsread1.prod.itd.earthlink.net> <3129209.1058595495@dbforums.com>`

```
Hello-
Thanks for the reply.

I guess I was looking for something that would dump the packed decimal
fields to a normal readable number.  I'm working now on doing this
conversion myself,  but am suprised there isn't a general utility or vutil
option to do this.

Thanks again for the help.

Regards,
bruce

"gmspano" <member9303@dbforums.com> wrote in message
news:3129209.1058595495@dbforums.com...
>
> Hi
…[18 more quoted lines elided]…
> Posted via http://dbforums.com
```

###### ↳ ↳ ↳ Re: vutil question

- **From:** "Michael Mattias" <michael.mattias@gte.net>
- **Date:** 2003-07-19T13:47:17+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<FZbSa.23137$BM.6888724@newssrv26.news.prodigy.com>`
- **References:** `<BJURa.9624$Mc.684883@newsread1.prod.itd.earthlink.net> <3129209.1058595495@dbforums.com> <E9bSa.11535$Mc.812136@newsread1.prod.itd.earthlink.net>`

```
"nospam" <bruceradtke@REMOVEspamREMOVE.earthlink.net> wrote in message
news:E9bSa.11535$Mc.812136@newsread1.prod.itd.earthlink.net...
> Hello-
> Thanks for the reply.
…[6 more quoted lines elided]…
> Thanks again for the help.

I think Ed Guy's ParseRat can dump from the "packed-decimal" flat file,
converting the packed-decimal and COMP[-whatever] fields to  DISPLAY
format..

MCM
```

###### ↳ ↳ ↳ Re: vutil question

- **From:** gmspano <member9303@dbforums.com>
- **Date:** 2003-07-19T14:57:58+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3129697.1058626678@dbforums.com>`
- **References:** `<BJURa.9624$Mc.684883@newsread1.prod.itd.earthlink.net> <3129209.1058595495@dbforums.com> <E9bSa.11535$Mc.812136@newsread1.prod.itd.earthlink.net>`

```

Hi Bruce

The "vutil.exe" utility helps you to extract all the records from a
indexed file in their original format without any number or string
convertion.
To resolve your issue, you need the original record description.

Gianni

Originally posted by Nospam 
> Hello-
> Thanks for the reply.
…[29 more quoted lines elided]…
> Posted via
    http://dbforums.com/http://dbforums.com
```

#### ↳ Re: vutil question

- **From:** gmspano <member9303@dbforums.com>
- **Date:** 2003-07-19T06:26:48+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3129210.1058596008@dbforums.com>`
- **References:** `<BJURa.9624$Mc.684883@newsread1.prod.itd.earthlink.net>`

```

Originally posted by Nospam 
> Hello all -
>
…[14 more quoted lines elided]…
> Gianni
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
