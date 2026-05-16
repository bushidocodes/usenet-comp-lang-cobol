[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Renumbering - how do I

_6 messages · 6 participants · 1999-10_

**Topics:** [`Help requests and how-to`](../topics.md#help)

---

### Renumbering - how do I

- **From:** Star Straf <star@prairienet.org>
- **Date:** 1999-10-20T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<380DC5E9.BAE73114@prairienet.org>`

```
Is there a simple command or utility to renumber the
line numbers for a cobol program in either UNIX or
windows 95.  I have a program that I inherited that
needs massive changes and I would like to 
renumber/resequence the line numbers.  I haven't
done any COBOL in a long time and I thought I remeber
there begin a simple resequence command but our 
sysop here dosen't know of such a thing

Thanks
  Star Straf   KU    star@prairienet.org
```

#### ↳ Re: Renumbering - how do I

- **From:** "Judson McClendon" <judmc123@bellsouth.net>
- **Date:** 1999-10-20T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<ZIjP3.14446$Fj2.126667@news1.mia>`
- **References:** `<380DC5E9.BAE73114@prairienet.org>`

```
Star Straf wrote:
>Is there a simple command or utility to renumber the
>line numbers for a cobol program in either UNIX or
…[5 more quoted lines elided]…
>sysop here dosen't know of such a thing

I have one in C.  E-mail me and I'll be happy to send you the source
and DOS EXE file.
```

#### ↳ Re: Renumbering - how do I

- **From:** Steven Lalewicz <strl@mfltd.co.uk>
- **Date:** 1999-10-21T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<380F1584.CF9CDEB6@mfltd.co.uk>`
- **References:** `<380DC5E9.BAE73114@prairienet.org>`

```
Star Straf wrote:

> Is there a simple command or utility to renumber the
> line numbers for a cobol program in either UNIX or
…[8 more quoted lines elided]…
> � Star Straf�� KU��� star@prairienet.org

Hi,

If you are using any Mico Focus compiler you can use the RESEQ
directive. This causes the compiler to produce line numbers in the
listing file (.lst) which you can then copy back to .cbl.

UNIX:
cob demo.cbl -C reseq -C rawlist -P� # rawlist� remove page headers
PC:
cobol demo.cbl reseq rawlist list();

The COPYLIST directive controls inclusion of the copy book in the
listing. The sequence numbers produced counts the contents of the copy
book too. If you wish to retain individual copy books (and don't want to
create them by cutting them out the listing), not sure what to suggest.
Maybe my answer is getting too complex.

Hope I've helped somewhere......

Regards,
Steve.
�
```

#### ↳ Re: Renumbering - how do I

- **From:** "Gunnar Opheim" <gunnar.opheim@eunet.no>
- **Date:** 1999-10-21T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<01bf1b5f$8cf85030$0100007f@vaagshaugen>`
- **References:** `<380DC5E9.BAE73114@prairienet.org>`

```
Star Straf <star@prairienet.org> wrote in article
<380DC5E9.BAE73114@prairienet.org>...
> Is there a simple command or utility to renumber the
> line numbers for a cobol program in either UNIX or
> windows 95.  I have a program that I inherited that
> needs massive changes and I would like to 
> renumber/resequence the line numbers.

For us mainframers this is a simple command in the editor.  Why do you need
line numbers?

Gunnar.
```

##### ↳ ↳ Re: Renumbering - how do I

- **From:** Howard Brazee <brazee@NOSPAMhome.com>
- **Date:** 1999-10-21T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<380F181B.75471C63@NOSPAMhome.com>`
- **References:** `<380DC5E9.BAE73114@prairienet.org> <01bf1b5f$8cf85030$0100007f@vaagshaugen>`

```
Gunnar Opheim wrote:
> 
> Star Straf <star@prairienet.org> wrote in article
…[10 more quoted lines elided]…
> Gunnar.

I was wondering the same thing (being a mainframe guy).  But most
programmer's editors have macro facilities which can be programmed to
renumber COBOL numbers.  Trouble is, each editor is different.
```

#### ↳ Re: Renumbering - how do I

- **From:** "Michael Mattias" <michael.mattias@gte.net>
- **Date:** 1999-10-21T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<mUtP3.1020$zO.30928@dfiatx1-snr1.gtei.net>`
- **References:** `<380DC5E9.BAE73114@prairienet.org>`

```
Some editors have 'sequence numbers" as a "built-in" function.

You might look at alternate editors if this is a recurring need.
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
