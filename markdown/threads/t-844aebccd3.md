[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Fujitsu PowerCobol

_3 messages · 2 participants · 2004-03_

**Topics:** [`Compilers and vendors`](../topics.md#compilers)

---

### Fujitsu PowerCobol

- **From:** "Euromercante" <euro@dsdd.com>
- **Date:** 2004-03-01T13:56:22
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<4043673d$0$28136$a729d347@news.telepac.pt>`

```
Hi,
    I've made an exe file (PCExample.exe) in PowerCobol with 3 forms
(PCform1, PCform2, PCform3) and the starting form is PCform2.
    What I would like to ask if it's possible in the command line to call
the exe file referecing the form to open, this is :
        - c:\PowerCobol\PCExample.exe -> this will open the PCform2,
and what I would like to do this:
        - INVOKE POW-SELF "CALLForm" USING "PCform3" "PCExample.exe"
in the command line. It's possible??

Thanks
```

#### ↳ Re: Fujitsu PowerCobol

- **From:** "JerryMouse" <nospam@bisusa.com>
- **Date:** 2004-03-01T18:40:15-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<M5ydnR1VbfB5St7dRVn-uA@giganews.com>`
- **References:** `<4043673d$0$28136$a729d347@news.telepac.pt>`

```
Euromercante wrote:
> Hi,
>     I've made an exe file (PCExample.exe) in PowerCobol with 3 forms
…[8 more quoted lines elided]…
> Thanks

No.

One solution is another form, PCform0, as the starting form that
interrogates the command line. PDform0 has the statement:

   MOVE COMMAND-LINE OF POW-SELF TO MyCommandLine

Then you check MyCommandLine for whatever command line params you passed at
execution time.

For example:

PCEXAMPLE.EXE Form1

then in PCform0

MOVE COMMAND-LINE (as above)
EVALUATE COMMAND-LINE(1:5)
   WHEN "Form1"
        INVOKE POW-SELF 'CALLFORM' USING 'PCForm1'

PCform0 can be an invisible form and the above code would most likely be in
a timer event.
```

##### ↳ ↳ Re: Fujitsu PowerCobol

- **From:** "Euromercante" <euro@dsdd.com>
- **Date:** 2004-03-02T14:00:59
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<40449271$0$28120$a729d347@news.telepac.pt>`
- **References:** `<4043673d$0$28136$a729d347@news.telepac.pt> <M5ydnR1VbfB5St7dRVn-uA@giganews.com>`

```
Thank you very much for you help.
Euro



"JerryMouse" <nospam@bisusa.com> escreveu na mensagem
news:M5ydnR1VbfB5St7dRVn-uA@giganews.com...
> Euromercante wrote:
> > Hi,
…[18 more quoted lines elided]…
> Then you check MyCommandLine for whatever command line params you passed
at
> execution time.
>
…[11 more quoted lines elided]…
> PCform0 can be an invisible form and the above code would most likely be
in
> a timer event.
>
>
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
