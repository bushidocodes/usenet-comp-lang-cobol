[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# OLE or API

_2 messages · 2 participants · 1999-10_

---

### OLE or API

- **From:** "Tom Wright" <twright@larimore.net>
- **Date:** 1999-10-11T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<HVpM3.11$kV2.419037@news1.i1.net>`

```
I'm trying to write several programs that will automatically print a word
2000 document.  Can someone point me to how to use ole fuctions..like a
sample or something...or list the api's I need to call.  Like StartDoc..or
PrintDlg to get the printer first.

Any help would be appreciated.  I am using MF cobol workbench 4.32

Tom Wright
twright@larimore./net
```

#### ↳ Re: OLE or API

- **From:** "Simon R Hart" <hart1@technologist.com>
- **Date:** 1999-10-12T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7u03m2$q9g$1@plutonium.btinternet.com>`
- **References:** `<HVpM3.11$kV2.419037@news1.i1.net>`

```
Tom,

You can do many things with OLE I use it quite often.
If you just simply want to print a file this is easy.

You need to define word as an OLE class in the class section
like:

 wordServ "$OLE$word.application"


Then create an instance of it:

 invoke word "new" returning wordServer

Open the document:
 invoke wordServ "FileOpen" using Path

Then print..
 invoke wordServ "FilePrint" using by value 0

This example the word program will be running in the background but will not
be shown on the screen. If you want it to be shown on the screen then you
can code:

invoke wordServ "AppShow"

This is very primitive Automation if you would like more code then mail me.

Simon R Hart
Eaton, Ottery St. Mary UK.


Tom Wright wrote in message ...
>I'm trying to write several programs that will automatically print a word
>2000 document.  Can someone point me to how to use ole fuctions..like a
…[8 more quoted lines elided]…
>
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
