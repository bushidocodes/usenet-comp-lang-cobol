[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# LPT Ports.

_7 messages · 4 participants · 2002-05_

---

### LPT Ports.

- **From:** "Joe Hunter" <pcs@usaor.net>
- **Date:** 2002-05-25T16:28:41-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<uevst6r4cbhgaf@corp.supernews.com>`

```
It seems to me that you can only print to LPT1, LPT2, and LPT3 in W2K and
XP.


Is any one printing to a LPT port higher then 3 using W2k or XP?

Thanks,
Joe Hunter
```

#### ↳ Re: LPT Ports.

- **From:** Rod Hewitt <rodders4@NOSPAMntlworld.com>
- **Date:** 2002-05-25T23:19:33+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<Xns921A3508AE9Erodders4ntlworldcom@80.3.128.4>`
- **References:** `<uevst6r4cbhgaf@corp.supernews.com>`

```

"Joe Hunter" <pcs@usaor.net> wrote in 

> It seems to me that you can only print to LPT1, LPT2, and LPT3 in W2K
> and XP.
> 
> Is any one printing to a LPT port higher then 3 using W2k or XP?
> 
Have you tried adding ports LPT4, etc. (or whatever you need)? I have a
host of other ports defined but nothing above LPT3 (because I don't need
them) but I am pretty sure I could add them.

Rod
```

##### ↳ ↳ Re: LPT Ports.

- **From:** "Joe Hunter" <pcs@usaor.net>
- **Date:** 2002-05-28T08:58:00-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<uf6vk02m3v0591@corp.supernews.com>`
- **References:** `<uevst6r4cbhgaf@corp.supernews.com> <Xns921A3508AE9Erodders4ntlworldcom@80.3.128.4>`

```

"Rod Hewitt" <rodders4@NOSPAMntlworld.com> wrote in message
news:Xns921A3508AE9Erodders4ntlworldcom@80.3.128.4...
>
> "Joe Hunter" <pcs@usaor.net> wrote in
…[8 more quoted lines elided]…
> them) but I am pretty sure I could add them.


I have added them using the NET USE LPT4 etc.  Then just do not work.

Joe Hunter
```

###### ↳ ↳ ↳ Re: LPT Ports.

- **From:** Frederico Fonseca <frederico_fonseca@eudoramail.com>
- **Date:** 2002-05-28T18:27:11+01:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<uef7fuc3vm1a1hgjdfrh7le2btsvg8ug0a@4ax.com>`
- **References:** `<uevst6r4cbhgaf@corp.supernews.com> <Xns921A3508AE9Erodders4ntlworldcom@80.3.128.4> <uf6vk02m3v0591@corp.supernews.com>`

```
On Tue, 28 May 2002 08:58:00 -0400, "Joe Hunter" <pcs@usaor.net>
wrote:

>
>"Rod Hewitt" <rodders4@NOSPAMntlworld.com> wrote in message
…[16 more quoted lines elided]…
>Joe Hunter
Adding additional LPT Ports

   1. Start Registry Editor (Regedt32.exe).


    * Click the following registry key. The current LPT ports are
displayed in the right pane:


   2. HKEY_LOCAL_MACHINE\Software\Microsoft\Windows
NT\CurrentVersion\Ports On the Edit menu, click Add Value .


    * Add a new value with the following attributes:


      Value Name: LPT # :
      Data Type: REG_SZ
      String: <blank> NOTE : When you create the new value name,
replace " # " in the "LPT # :" value name with the number of the LPT
port you want to add.

    * Quit Registry Editor.


    * Stop and restart the Spooler service by typing net stop spooler
and then net start spooler at a command prompt.
```

###### ↳ ↳ ↳ Re: LPT Ports.

_(reply depth: 4)_

- **From:** Rod Hewitt <rodders4@NOSPAMntlworld.com>
- **Date:** 2002-05-28T19:57:25+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<Xns921CD5304DC9Frodders4ntlworldcom@80.3.128.4>`
- **References:** `<uevst6r4cbhgaf@corp.supernews.com> <Xns921A3508AE9Erodders4ntlworldcom@80.3.128.4> <uf6vk02m3v0591@corp.supernews.com> <uef7fuc3vm1a1hgjdfrh7le2btsvg8ug0a@4ax.com>`

```

But probably easier to use Add ports.. from a printer properties dialogue 
box  :-)

Rod
```

###### ↳ ↳ ↳ Re: LPT Ports.

_(reply depth: 5)_

- **From:** Frederico Fonseca <frederico_fonseca@eudoramail.com>
- **Date:** 2002-05-29T00:21:09+01:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<2448fu07plq01bhrvhmpbgvd4oi5pqelmd@4ax.com>`
- **References:** `<uevst6r4cbhgaf@corp.supernews.com> <Xns921A3508AE9Erodders4ntlworldcom@80.3.128.4> <uf6vk02m3v0591@corp.supernews.com> <uef7fuc3vm1a1hgjdfrh7le2btsvg8ug0a@4ax.com> <Xns921CD5304DC9Frodders4ntlworldcom@80.3.128.4>`

```
On Tue, 28 May 2002 19:57:25 GMT, Rod Hewitt
<rodders4@NOSPAMntlworld.com> wrote:

>
>But probably easier to use Add ports.. from a printer properties dialogue 
>box  :-)
That would not work.
See my other post for a proper solution

FF
```

#### ↳ Re: LPT Ports.

- **From:** Liam Devlin <LiamDD@optonline.net>
- **Date:** 2002-05-26T02:01:48+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3CF04202.5090809@optonline.net>`
- **References:** `<uevst6r4cbhgaf@corp.supernews.com>`

```
Joe Hunter wrote:

> It seems to me that you can only print to LPT1, LPT2, and LPT3 in W2K and
> XP.
> 
> 
> Is any one printing to a LPT port higher then 3 using W2k or XP?


Printer ports don't have to be "LPTx". I have a printer port defined 
called "PRTmate". Perhaps you should try some alternate names?
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
