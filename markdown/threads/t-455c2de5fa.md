[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Comparing Modula2 and Cobol

_2 messages · 2 participants · 1994-12_

---

### Re: Comparing Modula2 and Cobol

- **From:** ghaas@informix.com (Guy Haas)
- **Date:** 1994-12-01T17:11:42+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3bl04e$jgo@infmx.informix.com>`
- **References:** `<cfoss.85.00567357@gov.nb.ca>`

```
In article 00567357@gov.nb.ca,  cfoss@gov.nb.ca (Colin Foss) writes:

 [snip]
>
>As far as a comparison, the two language aren't very similar.
>Modula supports separate compilation, not so for COBOL.

   The COBOL standard does not require implementations to support
   separate compilation, but many vendors provide it.  In Realia (now
   CA-Realia) COBOL, I can have a routine that is separately compiled
   and not even bound in, but can be called at run time.

>Modula has local variables, again not so for COBOL

   Local to what?  COBOL85 provides scoping rules that enable you to have
   data items (variables) that are global, and others that are local to the
   program that contains them. 

>Modula is strongly typed, not COBOL.

   Depends on what you mean by "strongly typed".  COBOL does do a lot of
   implicit casting (coercion) for you.... 

>COBOL is rather fixed format and wordy, not Modula.
>etc. etc. etc.
>
>BTW, I use COBOL every day and I actually like it.


--Guy K. Haas, Sr. Tech Writer  RTFM?                  ghaas@informix.com
  Informix Software Inc         IWTFT!   [If I were speaking on behalf of
  Menlo Park, CA  94025          ^      Informix, I'd say so explicitly.]
```

#### ↳ Re: Comparing Modula2 and Cobol

- **From:** dewar@cs.nyu.edu (Robert Dewar)
- **Date:** 1994-12-02T22:12:32-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3bonn0$239@gnat.cs.nyu.edu>`
- **References:** `<cfoss.85.00567357@gov.nb.ca> <3bl04e$jgo@infmx.informix.com>`

```
THe COBOL standard aboslutely *does* require separate compilation, and
has for some considerable time (at least 20 years!)
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
