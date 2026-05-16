[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Screen Print

_5 messages · 3 participants · 2000-05_

---

### Screen Print

- **From:** "brucepbarrett" <brucepbarrett@email.msn.com>
- **Date:** 2000-05-26T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<uBvl4Yxx$GA.350@cpmsnbbsa09>`

```
I need help printing GUI screens using Micro Focus 4.0 and Dialog.  What I
want to do is collect images in a file and then print the file.  I
appreciate any help anyone can provide me.
```

#### ↳ Re: Screen Print

- **From:** "Costas Giannoulis" <diavasi@otenet.gr>
- **Date:** 2000-05-26T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8gm08u$gsr$1@newssrv.otenet.gr>`
- **References:** `<uBvl4Yxx$GA.350@cpmsnbbsa09>`

```
Press ALT + PRINT SCRN while you have active the ScreenSet you want.
Paste the image into the Paint windows utility.
You can then put all of these files into a single word file and print it. :)

brucepbarrett <brucepbarrett@email.msn.com> wrote in message
news:uBvl4Yxx$GA.350@cpmsnbbsa09...
> I need help printing GUI screens using Micro Focus 4.0 and Dialog.  What I
> want to do is collect images in a file and then print the file.  I
> appreciate any help anyone can provide me.
>
>
```

##### ↳ ↳ Re: Screen Print

- **From:** "brucepbarrett" <brucepbarrett@email.msn.com>
- **Date:** 2000-05-26T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<O26ZOayx$GA.303@cpmsnbbsa09>`
- **References:** `<uBvl4Yxx$GA.350@cpmsnbbsa09> <8gm08u$gsr$1@newssrv.otenet.gr>`

```
I am new to the newsgroups and I probably didn't state the problem
correctly.
What I want to do is give users an option in a Windows 95/98/NT application
to capture a screen(the one they are looking at) puthe application would put
the image in a file and then the user would be able to select another option
to print the file of screens.   I want to automate the entire process for
thwser so all he/she has to do si select and option.  Hope this helps.

Thanks again.

"Costas Giannoulis" <diavasi@otenet.gr> wrote in message
news:8gm08u$gsr$1@newssrv.otenet.gr...
> Press ALT + PRINT SCRN while you have active the ScreenSet you want.
> Paste the image into the Paint windows utility.
> You can then put all of these files into a single word file and print it.
:)
>
> brucepbarrett <brucepbarrett@email.msn.com> wrote in message
> news:uBvl4Yxx$GA.350@cpmsnbbsa09...
> > I need help printing GUI screens using Micro Focus 4.0 and Dialog.  What
I
> > want to do is collect images in a file and then print the file.  I
> > appreciate any help anyone can provide me.
…[3 more quoted lines elided]…
>
```

#### ↳ Re: Screen Print

- **From:** "Ib Tanding" <ib@tanding.dk>
- **Date:** 2000-05-27T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8gn45d$osg$1@news.inet.tele.dk>`
- **References:** `<uBvl4Yxx$GA.350@cpmsnbbsa09>`

```
I have used PaintShop to clip the images to a file - Other tools can do the
same.
Regards
Ib
brucepbarrett skrev i meddelelsen ...
>I need help printing GUI screens using Micro Focus 4.0 and Dialog.  What I
>want to do is collect images in a file and then print the file.  I
>appreciate any help anyone can provide me.
>
>
```

#### ↳ Re: Screen Print

- **From:** "Costas Giannoulis" <diavasi@otenet.gr>
- **Date:** 2000-05-27T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8goac6$jki$1@newssrv.otenet.gr>`
- **References:** `<uBvl4Yxx$GA.350@cpmsnbbsa09>`

```
Hi again,

I think that the only way to do it from Cobol is by using ole. I am using NE
and i don't know if the Cobol you are using has this feature. Anyway the
procedure goes like this :

The user captures the window image into the system clipboard by pressing
ALT-PRNTSCR. You may override this by making a direct API call.
Then you can call a simple program to paste the image into another
application such as Word :

      $set ooctrl(+P)
      *
      * The following program is using MS Word 97
      *
       program-id. wordmgr.

       special-names.
           call-convention 2 is winapi.

       class-control.
           word is class "$OLE$word.basic"
           .

       working-storage section.

       01 theWordServer    object reference.

       procedure division.
           call "cob32api"
           call "class"
           call "apigui"

      *--- Create a new instance of word application
           invoke word "new" returning theWordServer

      *--- NOTE : Only Word 7 supports 'appShow'
           invoke theWordServer "AppShow"

      *--- Send message to word to open a new file (or open a previous one)
           invoke theWordServer "FileNew"

      *--- Copy data from clipboard into the word doc.
      *    The clipboard should contain the window image.
           invoke theWordServer "LineDown" using by value 1, 1
           invoke theWordServer "EditPaste"

      *--- Save the file if you wish
           invoke theWordServer "FileSave"

      *--- Close Word
           invoke theWordServer "appClose"

           exit program
           stop run.
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
