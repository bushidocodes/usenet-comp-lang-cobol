[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Standard dialogs in NetExpress

_3 messages · 2 participants · 1999-08_

**Topics:** [`COBOL standards (ANS, ISO, 74/85/2002/2014)`](../topics.md#standards)

---

### Standard dialogs in NetExpress

- **From:** "Martin" <hnetkong@post.cz>
- **Date:** 1999-08-03T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7o63oq$27td$1@ns.felk.cvut.cz>`

```

Hi everybody,
 can anybody help me with calling standard dialogs (save and print dialogs),
please? I'm beginner in Cobol, so I need very detailed description (with
example).
                                                                Martin
```

#### ↳ Re: Standard dialogs in NetExpress

- **From:** "Simon R Hart" <hart1@technologist.com>
- **Date:** 1999-08-03T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<933705454.20720.0.nnrp-10.c1edc1b5@news.demon.co.uk>`
- **References:** `<7o63oq$27td$1@ns.felk.cvut.cz>`

```

Martin <hnetkong@post.cz> wrote in message
news:7o63oq$27td$1@ns.felk.cvut.cz...
>
> Hi everybody,
>  can anybody help me with calling standard dialogs (save and print
dialogs),
> please? I'm beginner in Cobol, so I need very detailed description (with
> example).
>                                                                 Martin
>
>

Of course:
OpenDialog is class opendlg

           invoke OpenDialog "new" using self
                                                   returning lsOpenDialog

           *> set the file filter so only *.DEF files are shown.
           invoke self "setFileFilter" using lsOpenDialog
           invoke lsOpenDialog "show"


To receive the text entered in the open dialog use

           invoke lsOpenDialog "getFile" returning oPath

oPath is an object, convert it to text if not equal to null.

To print is a little different:

           move length of PrintFileN to FileNameLgth
           move FileName to DocumentTitle
           call 'PC_PRINT_FILE'
               using by reference FileNameGP,
                     by reference DocumentTitleGP,
                     by value     1 size 1,  <-------- play with this value
to execute diff dialogs, ie: font etc.
                     by value     0 size 4,
               returning          statusCode;
           move statusCode to lnk-PrintErrCode

Simon R Hart
Eaton.
```

##### ↳ ↳ Re: Standard dialogs in NetExpress

- **From:** "Martin" <hnetkong@post.cz>
- **Date:** 1999-08-05T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<37a928d3.0@news.cvut.cz>`
- **References:** `<7o63oq$27td$1@ns.felk.cvut.cz> <933705454.20720.0.nnrp-10.c1edc1b5@news.demon.co.uk>`

```
Thank you, it works fine.
                                    Martin
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
