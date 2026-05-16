[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# OLE, Word & NetExpress: changing fonts, bold etc

_6 messages · 4 participants · 2002-05 → 2002-06_

---

### OLE, Word & NetExpress: changing fonts, bold etc

- **From:** philhickling@compuserve.com (Phil Hickling)
- **Date:** 2002-05-29T06:05:04-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<6a371be2.0205290505.6cefa309@posting.google.com>`

```
Can anyone please advise on how to change fonts using OLE calling
Word2000 from MicroFocus NetExpress.

I am able to do many things, such as open a file, add text, mailmerge,
print, paste clipboard, save file, but I cannot find the correct
syntax for changing fonts, size, bold, italics etc.

I am enclosing some code I have got working, in the hope it may be of
help to others.  If anyone wants the full source they are welcome to
email me.

      **** Create an instance of Word AND MAKE IT VISIBLE
           invoke wordapp "new" returning wordServer
           invoke wordServer "SetVisible" using by value 1
      **** Get the Word documents collection object
           invoke wordServer "getDocuments" returning theDocuments
      **** EITHER open existing file OR create new document
      *    invoke theDocuments "Open" using "C:\XX.DOC ".
           invoke theDocuments "add".
      **** INSERT SOME TEXT (EQUIVALENT TO Selection.InsertAfter)
           invoke wordServer "getSelection" returning theSelection
           invoke theSelection "InsertAfter" using Z"BEFORE macros ".
      **** SELECT THE WHOLE DOCUMENT (Selection.WholeStory)
      *    invoke theSelection "WholeStory".
      *    invoke theSelection "InsertAfter" using Z"AT END? ".
      **** GO TO END OF DOCUMENT (Selection.EndKey Unit:=wdStory)
           invoke theSelection "WholeStory".
           invoke theSelection "EndKey".
      **** PASTE A SCREEN PRINT (Selection.Paste)
      *    invoke theSelection "Paste".
      **** PRINT THE CURRENT DOCUMENT (Application.PrintOut)
      *    invoke wordServer "PrintOut".
      **** RUN A MACRO Application.Run
MacroName:="Normal.NewMacros.x4")
           invoke wordServer "Run" using "Macro1". *> it works
      **** INSERT SOME TEXT (EQUIVALENT TO Selection.InsertAfter
           invoke wordServer "getSelection" returning theSelection
           invoke theSelection "InsertAfter" using Z"between macros ".
```

#### ↳ Printing in Net Express

- **From:** "James J. Gavan" <jjgavan@shaw.ca>
- **Date:** 2002-05-29T18:09:00+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3CF5195E.D0F2AAFB@shaw.ca>`
- **References:** `<6a371be2.0205290505.6cefa309@posting.google.com>`

```


Phil Hickling wrote:

> Can anyone please advise on how to change fonts using OLE calling
> Word2000 from MicroFocus NetExpress.
>

graham wrote:

> We have a MF COBOL package that can produce printed output...currently
> plain and simple text but we have plans to improve this in the not too
> distant future.

This is in response to your separate messages. One other *possibilty* that
may help you both, go take a look at :-

     http://www.microfocus.com/files/whitepapers/wpautomation.pdf

Wayne Rippin's examples spell it out pretty neatly using MS Word as the
OLE. Read through and you will see you need to access from the IDE -->
Tools -->  the Type Library Assistant which shows you what you can invoke
per OLE

In Graham's case he wants to print continuous, so there *might* be a
restriction in the Word software on maximum file size. As a suggestion,
perhaps you can create a fixed page (continuous page) template in Word and
'merge' entries from COBOL ?

Jimmy, Calgary AB
```

##### ↳ ↳ Re: Printing in Net Express

- **From:** philhickling@compuserve.com (Phil Hickling)
- **Date:** 2002-06-06T02:06:18-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<6a371be2.0206060106.4be30033@posting.google.com>`
- **References:** `<6a371be2.0205290505.6cefa309@posting.google.com> <3CF5195E.D0F2AAFB@shaw.ca>`

```
Thanks, Jimmy.  That is an excelant document - I have now worked out
how to do it, and even more amazing, I now understand it!
```

#### ↳ Re: OLE, Word & NetExpress: changing fonts, bold etc

- **From:** "Grinder" <grinder@no.spam.maam.com>
- **Date:** 2002-05-29T15:01:02-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<ad3c1v01rkj@enews1.newsguy.com>`
- **References:** `<6a371be2.0205290505.6cefa309@posting.google.com>`

```

"Phil Hickling" <philhickling@compuserve.com> wrote in message
news:6a371be2.0205290505.6cefa309@posting.google.com...
> Can anyone please advise on how to change fonts using OLE calling
> Word2000 from MicroFocus NetExpress.
…[3 more quoted lines elided]…
> syntax for changing fonts, size, bold, italics etc.

I'm not sure of the exact syntax, but here's a speck of VB code that will
open a document and change all of it's text to use "Tahoma"  I've included
the analagous COBOL commands from your code -- hope that helps.

  Dim wordServer As Word.Application

  'invoke wordapp "new" returning wordServer
  Set wordServer = New Word.Application

  'invoke wordServer "SetVisible" using by value 1
  wordServer.Visible = True

  'invoke wordServer "getDocuments" returning theDocuments
  'invoke theDocuments "Open" using "C:\XX.DOC ".
  wordServer.Documents.Open "c:\xx.doc"

  'invoke theSelection "WholeStory".
  wordServer.Selection.WholeStory


  'I'm not sure what this will look like in COBOL, though...
  wordServer.Selection.Font.Name = "Tahoma"

__________________

One suggestion worth making, concerns the Documents.Open and Documents.Add
methods.  These routines return a document reference.  It's worth hanging
onto that reference and applying your command to it, instead of the word
application itself.  This removes the requirement that your document be the
active one in that application.

Translated, the code looks like:

  Dim wordServer As Word.Application
  Dim wordDoc As Word.Document

  'invoke wordapp "new" returning wordServer
  Set wordServer = New Word.Application

  'invoke wordServer "SetVisible" using by value 1
  wordServer.Visible = True

  'invoke wordServer "getDocuments" returning theDocuments
  'invoke theDocuments "Open" using "C:\XX.DOC " returning wordDoc
  Set wordDoc = wordServer.Documents.Open("c:\xx.doc")

  'invoke wordDoc "getRange" returning theRange
  'invoke theRange "WholeStory".
  wordDoc.Range.WholeStory

  'I'm not sure what this will look like in COBOL, though...
  wordDoc.Range.Font.Name = "Tahoma"
```

#### ↳ Re: OLE, Word & NetExpress: changing fonts, bold etc

- **From:** jean.villemaire@microfocus.com (Jean Villemaire)
- **Date:** 2002-05-30T05:35:30-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3b9b30ab.0205300435.2cfd6aa0@posting.google.com>`
- **References:** `<6a371be2.0205290505.6cefa309@posting.google.com>`

```
Phil,

An example demonstrating this can be found at
http://supportline.microfocus.com, then click on Self-Service on the
left and choose Net Express Samples & Utilities and on the page click
Samples.

A demo called wordsetup.zip contains the code that you are looking
for.

Hope this helps.
```

##### ↳ ↳ Re: OLE, Word & NetExpress: changing fonts, bold etc

- **From:** philhickling@compuserve.com (Phil Hickling)
- **Date:** 2002-06-06T02:01:27-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<6a371be2.0206060101.73bc862f@posting.google.com>`
- **References:** `<6a371be2.0205290505.6cefa309@posting.google.com> <3b9b30ab.0205300435.2cfd6aa0@posting.google.com>`

```
Thank you, everyone.  The above helped:  I have found out how to do it!
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
