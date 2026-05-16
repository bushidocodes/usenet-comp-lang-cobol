[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Internationalisation

_4 messages · 4 participants · 1999-08_

---

### Internationalisation

- **From:** mikefry@iafrica.nospam.com (Mike Fry)
- **Date:** 1999-08-05T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<EdHxIHxd9CDV-pn2-Qvr48sDqg7lQ@minitower>`

```
I wonder if there's anyone out there who can assist me in my efforts to 
do something that I've never done before.

I've got a COBOL program (MicroFocus, OS/2 Warp 4) that runs perfectly 
well in most english locales. I now want to change it so that it will 
work in Moscow.

My main problem is with the input of descriptive fields: some must be in
Cyrillic and some must remain in English. How can I achieve this using 
the facilities available within my COBOL runtime system?

Also, (slightly out of context) what changes would I need to make to the
CONFIG.SYS file to accommodate my Cyrillic-cum-English program? I 
presume that I'd need to alter the COUNTRY, CODEPAGE and DEVINFO(KBD) 
statements. Is there anything else to be considered?

Any help would be much appreciated.

Regards,
MIKE FRY
mailto:mikefry@iafrica.com
```

#### ↳ Re: Internationalisation

- **From:** Ken Foskey <waratah@zip.com.au>
- **Date:** 1999-08-06T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<37AAE380.9D113C53@zip.com.au>`
- **References:** `<EdHxIHxd9CDV-pn2-Qvr48sDqg7lQ@minitower>`

```
Mike Fry wrote:
> 
> I wonder if there's anyone out there who can assist me in my efforts to
…[19 more quoted lines elided]…
> mailto:mikefry@iafrica.com

The GNU trick is reasonably easy.   Have a look at how GNU do it for
there C programs (www.gnu.org).  Basically they pass all their text
through a subroutine first that (might or might not) remap it to a
different language.

This does not help when the language structure changes the order of
the values in the output (e.g. language 1 will have count 10, at
$10.00 language 2 will say $10 for 10.)

Don't do cute tricks for plurals.  If you do this.
Ken
```

#### ↳ Re: Internationalisation

- **From:** "peter dashwood" <dashwood@freewebaccess.co.uk>
- **Date:** 1999-08-09T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<37aef8ea@eeyore.callnetuk.com>`
- **References:** `<EdHxIHxd9CDV-pn2-Qvr48sDqg7lQ@minitower>`

```

Mike Fry wrote in message ...
>I wonder if there's anyone out there who can assist me in my efforts to
>do something that I've never done before.
…[13 more quoted lines elided]…
>
Mike,

As you are only using the labels on screens in Cyrillic, I wouldn't even try
to change the environment to support it. Try using the double byte character
set of COBOL (DBCS) to provide Cyrillic text for field labels on screens.

If you need to input text fields in Cyrillic you have 2 options:

1. Configure the system as you suggested above to support the Russian
Alphabet.

2. Take the input as a DBCS string and write your own routines to decode it.

I would strongly advise that you avoid option 1 like the plague. Only as a
last resort...


Pete.
```

##### ↳ ↳ Re: Internationalisation

- **From:** swiegand@neo.rr.com (SkippyPB)
- **Date:** 1999-08-10T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<134ED26635BF5828.6DCE51667BB35508.3B48A473FD9771A7@lp.airnews.net>`
- **References:** `<EdHxIHxd9CDV-pn2-Qvr48sDqg7lQ@minitower> <37aef8ea@eeyore.callnetuk.com>`

```
On Mon, 9 Aug 1999 15:45:50 +0100, "peter dashwood"
<dashwood@freewebaccess.co.uk> enlightened us:

>
>Mike Fry wrote in message ...
…[34 more quoted lines elided]…
>

Having faced the same thing in Thailand it is not that difficult to
support English characters as well as the local characters in this
case.  I don't think you need DBCS for Cryllic.  I've also done work
in Cyprus where Greek is spoken and we did not have to use DBCS for
Greek/English character input/output.  DBCS is needed for Chinese,
Japenese and possibly Korean languages.

What we found in Thailand and Cyprus was the IBM code page was
modified to handle the alpahbets.  I don't remember the specifics of
Greek, but the Thai alphabet,  which consists of 44 characters, were
assigned to normally unused EBCIDIC positions.  For example B0, B1, B2
etc.  

Now all of this was done on a mainframe, but I'd have to believe that
the same facility would exist for the PC as well.  If you're having to
do the programming here in America with hardware built to only be used
in America, then you are really up against it.  

Regards,

          ////
         (o o)
-oOO--(_)--OOo-

Some days your the dog.  Some days your the hydrant.


 Steve
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
