[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# GVIM COBOL syntax hiliting columnar?

_2 messages · 2 participants · 1998-10_

---

### GVIM COBOL syntax hiliting columnar?

- **From:** borgnaes@freenet.columbus.oh.us (Chris Borgnaes)
- **Date:** 1998-10-20T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<70itf4$qq1@login.freenet.columbus.oh.us>`

```

Is there a way to make GVIM not look at columns 1-6 and 73-80 when COBOL
syntax hiliting is turned on?  It reds-out the entire line if there are
any comments in those areas.
```

#### ↳ Re: GVIM COBOL syntax hiliting columnar?

- **From:** cadams@cadams-ntw.acucorp.com (Chris Adams)
- **Date:** 1998-10-23T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<slrn731br0.1hc.cadams@cadams-ntw.acucorp.com>`
- **References:** `<70itf4$qq1@login.freenet.columbus.oh.us>`

```
On 20 Oct 1998 16:57:08 -0400, Chris Borgnaes <borgnaes@freenet.columbus.oh.us>
wrote:
>Is there a way to make GVIM not look at columns 1-6 and 73-80 when COBOL
>syntax hiliting is turned on?  It reds-out the entire line if there are any
>comments in those areas.

Disclaimer: I'm assuming that your gvim is at least somewhat similar to the vim
5.1 (1998 Apr 7) I'm using...

Somewhere you should have syntax directory with a number of .vim files,
including cobol.vim.  On my RedHat 5.1 linux box, this is
/usr/share/vim/syntax/ but YMMV.

Load cobol.vim in vim. There should be a block such as: 
-------------------------------------------------
if ! exists("cobol_legacy_code")
    " catch junk in columns 1-6 for modern code
    syn match cobolBAD      "^ \{0,5\}[^ ].*"
endif

" many legacy sources have junk in columns 1-6: must be before others
" Stuff after column 72 is in error - must be after all other "match" entries
if exists("cobol_legacy_code")
    syn match   cobolBadLine      "^.\{6}[^*/].\{66,\}"
else
    syn match   cobolBadLine      "^.\{6}.\{67,\}"
endif
-------------------------------------------------

That last syn match is the key: it's looking for 6 characters at the start of
the line followed by 67 characters, which is considered invalid since that ends
in column 73.

Here's the modified block I used to allow up to 120 character lines:
-------------------------------------------------
if ! exists("cobol_legacy_code")
    " catch junk in columns 1-6 for modern code
    syn match cobolBAD      "^ \{0,5\}[^ ].*"
endif

" many legacy sources have junk in columns 1-6: must be before others
" Stuff after column 72 is in error - must be after all other "match" entries
if exists("cobol_legacy_code")
    syn match   cobolBadLine      "^.\{6}[^*/].\{66,\}"
else
" CTA: Modified to allow anything out to column 120 for Acucobol terminal 
" format...
" Original:
"    syn match   cobolBadLine      "^.\{6}.\{67,\}"
    syn match   cobolBadLine      "^.\{6}.\{115,\}"

endif
-------------------------------------------------



If you need some help figuring out just what to do, check out the online help
":h syntax".
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
