[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Seq Access using Alt Record Key

_5 messages · 4 participants · 2001-12_

---

### Seq Access using Alt Record Key

- **From:** floydj@netins.net (Floyd Johnson)
- **Date:** 2001-12-13T15:39:28+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<9vai3g$391$2@ins22.netins.net>`

```
Thane's book has an example of using sequential access using the Alternate
Record Key - it uses the start verb to set the starting point for
sequential access.  I see nothing about how to move the file pointer
associated with an Alternate Record Key to the beginning of the index.  A
couple of other texts have similar examples.

The case includes an indexed file with a primary key of
ACCOUNT-NUMBER.  The alternate key is COMPANY-NAME.  We would like to
print the file in company name order.  The work around we came up with is
to create a line sequential file and sort this new file using company name
as the sort field.  This created a temporary file that could be processed
and then deleted (see my earlier posts).  

Is there some way to use START to set the file pointer so that it is at
the beginning of the alternate record key index?

Thank you for any assistance or suggestions.

Floyd Johnson
```

#### ↳ Re: Seq Access using Alt Record Key

- **From:** "Donald Tees" <donald_tees@sympatico.ca>
- **Date:** 2001-12-13T10:57:21-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<Aa4S7.22959$DO.2912393@news20.bellglobal.com>`
- **References:** `<9vai3g$391$2@ins22.netins.net>`

```
Move low values to the key, then start as you would anywhere else. (start,
key greater than, invalid key is an empty file).  Your first read will read
the first record.

Donald

"Floyd Johnson" <floydj@netins.net> wrote in message
news:9vai3g$391$2@ins22.netins.net...
> Thane's book has an example of using sequential access using the Alternate
> Record Key - it uses the start verb to set the starting point for
…[30 more quoted lines elided]…
> +-----------------------------------------------------------+
```

#### ↳ Re: Seq Access using Alt Record Key

- **From:** "James J. Gavan" <jjgavan@shaw.ca>
- **Date:** 2001-12-13T19:29:19+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3C190203.E1DC4CEE@shaw.ca>`
- **References:** `<9vai3g$391$2@ins22.netins.net>`

```


Floyd Johnson wrote:

> Thane's book has an example of using sequential access using the Alternate
> Record Key - it uses the start verb to set the starting point for
> sequential access.  I see nothing about how to move the file pointer <snip -
> etc...>

Wouldn't hurt for one COBOL instructor to check out what another one has done
<G>. Check out  U of Limerick : -

    www.csis.ul.ie

Jimmy
```

#### ↳ Re: Seq Access using Alt Record Key

- **From:** Thane Hubbell <nospam@newsranger.com>
- **Date:** 2001-12-14T16:22:42+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<mHpS7.61594$xS6.100645@www.newsranger.com>`
- **References:** `<9vai3g$391$2@ins22.netins.net>`

```
Move Low-Values to Company-Name
Start whatever-file Key > Company-name

Unless I miss the point????


In article <9vai3g$391$2@ins22.netins.net>, Floyd Johnson says...
>
>Thane's book has an example of using sequential access using the Alternate
…[31 more quoted lines elided]…
>+-----------------------------------------------------------+
```

##### ↳ ↳ Re: Seq Access using Alt Record Key

- **From:** floydj@netins.net (Floyd Johnson)
- **Date:** 2001-12-14T18:43:20+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<9vdh88$hov$1@ins22.netins.net>`
- **References:** `<9vai3g$391$2@ins22.netins.net> <mHpS7.61594$xS6.100645@www.newsranger.com>`

```
Yep - that's right.

Let me add my thanks to Thane.  Over the last three years Thanes book has
contributed to making our File Structures course a success.  Students
comment that the book is the best CS that they have used or seen.  The
book has also contributed to getting rave reviews from the students. 

Floyd Johnson

=================================================== 

Thane Hubbell (nospam@newsranger.com) wrote:
: Move Low-Values to Company-Name
: Start whatever-file Key > Company-name

: Unless I miss the point????


: In article <9vai3g$391$2@ins22.netins.net>, Floyd Johnson says...
: >
: >Thane's book has an example of using sequential access using the Alternate
: >Record Key - it uses the start verb to set the starting point for
: >sequential access.  I see nothing about how to move the file pointer
: >associated with an Alternate Record Key to the beginning of the index.  A
: >couple of other texts have similar examples.
: >
: >The case includes an indexed file with a primary key of
: >ACCOUNT-NUMBER.  The alternate key is COMPANY-NAME.  We would like to
: >print the file in company name order.  The work around we came up with is
: >to create a line sequential file and sort this new file using company name
: >as the sort field.  This created a temporary file that could be processed
: >and then deleted (see my earlier posts).  
: >
: >Is there some way to use START to set the file pointer so that it is at
: >the beginning of the alternate record key index?
: >
: >Thank you for any assistance or suggestions.
: >
: >Floyd Johnson
: >
: >--
: >--
: >+-----------------------------------------------------------+
: >|                      Floyd H. Johnson                     |
: >+-----------------------------+-----------------------------+    
: >| Voice  : (716) 594 - 0942   | 87 Parkway Drive            |
: >| E-Mail : floydj@netins.net  | North Chili, NY  14514      |
: >+-----------------------------+-----------------------------+
: >|                 http://bounce.to/Roberts                  |
: >+-----------------------------------------------------------+
: >| If you think you understand Him,                          |
: >|               then you really do not know HIM !!          |
: >+-----------------------------------------------------------+
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
