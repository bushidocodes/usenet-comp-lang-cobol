[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Open Associated file

_4 messages · 2 participants · 2008-03_

---

### Open Associated file

- **From:** "Euro" <euo@euromercante.pt>
- **Date:** 2008-03-19T11:54:51
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<newscache$zt7zxj$zxo$1@newsfront4.netvisao.pt>`

```
Fujitsu Power Cobol V7.0

I try with this code:

      call "ShellExecuteA" with stdcall linkage
          using
              by value 0      *> window handle
              by reference
                  open-command *> operation to perform
                  file-to-open *> document to open
              by value 0       *> parameters (none here)
              by reference
                  default-directory, *> directory (could also be null)
              by value 0       *> SW-SHOWNORMAL show the file when open
          returning
              se-hInstance     *> not 'really' a handle,
                               *> more an error return
      end-call



I open all files less the MS office.
Some reason?

Thanks
Joe
```

#### ↳ Re: Open Associated file

- **From:** Kellie Fitton <KELLIEFITTON@yahoo.com>
- **Date:** 2008-03-19T13:09:59-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<dc783353-fcd8-4834-860c-4716e1b2845a@i7g2000prf.googlegroups.com>`
- **References:** `<newscache$zt7zxj$zxo$1@newsfront4.netvisao.pt>`

```
On Mar 19, 4:54 am, "Euro" <e...@euromercante.pt> wrote:
> Fujitsu Power Cobol V7.0
>
…[21 more quoted lines elided]…
> Joe


Hi,

You can use the following APIs to retrieve the name and handle of the
executable file associated with a specified filename (doc, xls, pps):

	FindExecutable()

	CreateProcess()

	WaitForSingleObject()

	CloseHandle()

http://msdn2.microsoft.com/en-us/library/ms647374.aspx

http://msdn2.microsoft.com/en-us/library/ms682425.aspx

http://msdn2.microsoft.com/en-us/library/ms687032.aspx

http://msdn2.microsoft.com/en-us/library/ms724211.aspx

Kellie.
```

##### ↳ ↳ Re: Open Associated file

- **From:** "Euro" <euo@euromercante.pt>
- **Date:** 2008-03-20T11:01:17
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<newscache$t001yj$f0g$1@newsfront4.netvisao.pt>`
- **References:** `<newscache$zt7zxj$zxo$1@newsfront4.netvisao.pt> <dc783353-fcd8-4834-860c-4716e1b2845a@i7g2000prf.googlegroups.com>`

```
Thanks Kellie,

I open all, less the XLS.
Gives a message already within Excel:
"There was an error of DDE and it is not possible to show a description 
because it is too long..."

Joe



"Kellie Fitton" <KELLIEFITTON@yahoo.com> escreveu na mensagem 
news:dc783353-fcd8-4834-860c-4716e1b2845a@i7g2000prf.googlegroups.com...
> On Mar 19, 4:54 am, "Euro" <e...@euromercante.pt> wrote:
>> Fujitsu Power Cobol V7.0
…[47 more quoted lines elided]…
>
```

###### ↳ ↳ ↳ Re: Open Associated file

- **From:** Kellie Fitton <KELLIEFITTON@yahoo.com>
- **Date:** 2008-03-20T10:22:55-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<24c4cedd-2b14-4838-954a-5cb59c2e118f@s8g2000prg.googlegroups.com>`
- **References:** `<newscache$zt7zxj$zxo$1@newsfront4.netvisao.pt> <dc783353-fcd8-4834-860c-4716e1b2845a@i7g2000prf.googlegroups.com> <newscache$t001yj$f0g$1@newsfront4.netvisao.pt>`

```
On Mar 20, 4:01 am, "Euro" <e...@euromercante.pt> wrote:
> Thanks Kellie,
>
…[6 more quoted lines elided]…
>


Hi,

The following weblinks should give you some pointers:

http://en.wikipedia.org/wiki/Dynamic_Data_Exchange

http://whitepapers.techrepublic.com.com/whitepaper.aspx?docid=297657

http://msdn2.microsoft.com/en-us/library/ms648774(VS.85).aspx

Kellie.
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
