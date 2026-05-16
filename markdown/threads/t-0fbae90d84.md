[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# BARCODE - Code39, Using with Cobol and HP laserjet printer

_3 messages · 3 participants · 1999-06_

---

### BARCODE - Code39, Using with Cobol and HP laserjet printer

- **From:** Rich Johnson <rjohn61389@yahoo.com>
- **Date:** 1999-06-14T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<929405489.20577@www.remarq.com>`

```
I have to print Code39 barcodes using Microfocus Cobol
running on a Unix box, I have a Laserjet 4si printer with
barcode and more cartridge. Question is

How do I invoke the barcode to print. I have the Escape
sequence needed. I have a print program "shop traveler" that
I would like to barcode certain fields, ie Part Number,
order number etc.



**** Posted from RemarQ - http://www.remarq.com - Discussions Start Here (tm) ****
```

#### ↳ Re: BARCODE - Code39, Using with Cobol and HP laserjet printer

- **From:** "James King" <mangogwr@bellsouth.net>
- **Date:** 1999-06-14T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<iii93.13220$hh1.2939@news1.mia>`
- **References:** `<929405489.20577@www.remarq.com>`

```
As long as you can write to the Printer, then if you can 'embed' the
seqeunces within
the data, the printer will recognize them and do its thing.  The 'Esc'
sequence is called
the escape sequence because ASCII 27 / Hex 1b is the 'Escape' character
which means
to 'break out of what you are doing and go into a special mode',  as LONG AS
the characters
that follow the 'Esc' are coded correctly (and there are two parts) it will
work.
Hdr 'Esc'
Part 1: command code - one to several bytes that indicate what TYPE of
function to perform
Part 2: the values to be used

repeat as needed

e.g.  'ESC'+Elite_Font_Code+Font_Size+Font_Special (Bold/Italic,etc)


Rich Johnson wrote in message <929405489.20577@www.remarq.com>...
>I have to print Code39 barcodes using Microfocus Cobol
>running on a Unix box, I have a Laserjet 4si printer with
…[9 more quoted lines elided]…
>**** Posted from RemarQ - http://www.remarq.com - Discussions Start Here
(tm) ****
```

#### ↳ Re: BARCODE - Code39, Using with Cobol and HP laserjet printer

- **From:** Alex Romaniuk <ales.romaniuk@zag.si>
- **Date:** 1999-06-15T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3766640E.79E8@zag.si>`
- **References:** `<929405489.20577@www.remarq.com>`

```
Rich Johnson wrote:
> 
> I have to print Code39 barcodes using Microfocus Cobol
…[8 more quoted lines elided]…
> **** Posted from RemarQ - http://www.remarq.com - Discussions Start Here (tm) ****
Check LJ4si documentation for PCL (Printer Control Language) for
Barcode printing. I know some old Fujitsu Matrix printer have barcode
printing programmed yet.
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
