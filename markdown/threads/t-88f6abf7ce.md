[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Writing CGI in Cobol Ans85

_3 messages · 3 participants · 1999-06_

**Topics:** [`Web, XML, modern integration`](../topics.md#web)

---

### Writing CGI in Cobol Ans85

- **From:** semiel@my-deja.com
- **Date:** 1999-06-18T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7kdp2d$kce$1@nnrp1.deja.com>`

```
Hi,
i need to get some info about how to write a cgi
program in Cobol Ans85, i.e. without using any
proprietary functions, libraries...
The "standard" Accept/Display dont read the
stdin/send to stdout, dont they?

Thanks for your help,
Sem.


Sent via Deja.com http://www.deja.com/
Share what you know. Learn what you don't.
```

#### ↳ Re: Writing CGI in Cobol Ans85

- **From:** "Simon Hart" <hart1@technologist.com>
- **Date:** 1999-06-18T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<Ezya3.1198$BS6.640@wards>`
- **References:** `<7kdp2d$kce$1@nnrp1.deja.com>`

```

<semiel@my-deja.com> wrote in message news:7kdp2d$kce$1@nnrp1.deja.com...
> Hi,
> i need to get some info about how to write a cgi
…[10 more quoted lines elided]…
> Share what you know. Learn what you don't.

Check out Cobol Unleashed by sams, book, It contains
a resonable amount of info.

Simon Hart
```

#### ↳ Re: Writing CGI in Cobol Ans85

- **From:** "Gazaloo" <gaz@home.com>
- **Date:** 1999-06-19T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<PjFa3.11163$NY6.4115@news.rdc1.sfba.home.com>`
- **References:** `<7kdp2d$kce$1@nnrp1.deja.com>`

```
here's a simple example i have for an older MERANT compiler (Visual Object
COBOL). the example should work just fine with the current product (Net
Express).

a nice/slick alternative to using external-forms to output a page is to
simply embed the HTML into your program. in this case the 01 output-page
item is not needed and instead of the 'display output-page', you have:

exec html
    copy "output.htm"
end exec

well, something like that anyway. it's been a while. you can of course just
enter HTML directly; you don't have to use copybooks. anyway, pretty simple,
COBOL/SQL-like implementation.

==>start of cobolcgi source
identification division.

working-storage section.
01 input-page is external-form.
   03  name-field pic x(30) identified by "Name".
   03  phone-no   pic x(30) identified by "Phone".
   03  email      pic x(30) identified by "Email".

01 output-page is external-form identified by "output".
   03  name-field pic x(30) identified by "Name".
   03  phone-no   pic x(30) identified by "Phone".
   03  email      pic x(30) identified by "Email".

procedure division.

    accept input-page
    move corresponding input-page to output-page
    display output-page
    .
==>end of cobolcgi source

==>start of input.htm
<HTML>
<HEAD>
<TITLE>Sample Form for VISOC</TITLE>
</HEAD>
<BODY>

<P>Visual Object COBOL Input Form

<FORM METHOD="POST" ACTION="/cgi-bin/cobolcgi.exe"></P>
<PRE>
Name     <INPUT TYPE="TEXT" NAME="Name" VALUE="" MAXLENGTH="30" >
Email id <INPUT TYPE="TEXT "NAME="Email" VALUE="" MAXLENGTH="30" >
Phone    <INPUT NAME="Phone" VALUE="" MAXLENGTH="12">
<INPUT TYPE="SUBMIT" VALUE="Send Form"><INPUT TYPE="RESET">
</PRE>
</FORM>

</BODY>
</HTML>
==>end of input.htm

==>start of output.htm
<HTML>

<P>*** SAMPLE OUTPUT FORM ***</P>
<P>Dear :name-field</P>
<P>blah blah blah</P>

</HTML>
==>end of output.htm
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
