[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Sending date type from Cobol to SQL

_7 messages · 4 participants · 2004-09_

**Topics:** [`Databases and SQL`](../topics.md#databases) · [`Date and calendar processing`](../topics.md#dates)

---

### Sending date type from Cobol to SQL

- **From:** "Euromercante" <remove_euromercante@sapo.pt>
- **Date:** 2004-09-16T17:35:29+01:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<4149c0e2$0$4904$a729d347@news.telepac.pt>`

```
Hi,
    I need to write a field type smalldatetime in SQL Server (2000) database
using PowerCobol v7 via ODBC. In my application appears this error message
"Invalid date format !".
    I need to know how to format a field in Cobol to send the information to
a field smalldatetime type.

Regards
Euromercante
```

#### ↳ Re: Sending date type from Cobol to SQL

- **From:** Frederico Fonseca <real-email-in-msg-spam@email.com>
- **Date:** 2004-09-16T18:21:38+01:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<bfijk0lr1drjkh2lrd2vrgk9i6bh3f8q65@4ax.com>`
- **References:** `<4149c0e2$0$4904$a729d347@news.telepac.pt>`

```
On Thu, 16 Sep 2004 17:35:29 +0100, "Euromercante"
<remove_euromercante@sapo.pt> wrote:

>Hi,
>    I need to write a field type smalldatetime in SQL Server (2000) database
…[7 more quoted lines elided]…
>
How are you using the ODBC.
Data bound control, or plain SQL?

This will affect how you do things. If with SQL you can and should use
one of the convert/cast functions. 
e.g. 
update mytbl set my_small_date_time_field =
CAST('my_COBOL_variable_on_the_Correct_format' AS smalldatetime)

or
update mytbl set my_small_date_time_field = convert(smalldatetime,
my_COBOL_variable_on_the_Correct_format')

The convert has more options. Look at the SQL Server booksonline for
more info.






Frederico Fonseca
ema il: frederico_fonseca at syssoft-int.com
```

##### ↳ ↳ Re: Sending date type from Cobol to SQL

- **From:** "local" <pt40br@hotmail.com>
- **Date:** 2004-09-16T19:20:20+01:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<4149d997$0$2499$a729d347@news.telepac.pt>`
- **References:** `<4149c0e2$0$4904$a729d347@news.telepac.pt> <bfijk0lr1drjkh2lrd2vrgk9i6bh3f8q65@4ax.com>`

```
Thanks Frederico!

We use DBAccess (ocx from Fujitsu - Data bound control.

Regards



"Frederico Fonseca" <real-email-in-msg-spam@email.com> wrote in message
news:bfijk0lr1drjkh2lrd2vrgk9i6bh3f8q65@4ax.com...
> On Thu, 16 Sep 2004 17:35:29 +0100, "Euromercante"
> <remove_euromercante@sapo.pt> wrote:
>
> >Hi,
> >    I need to write a field type smalldatetime in SQL Server (2000)
database
> >using PowerCobol v7 via ODBC. In my application appears this error
message
> >"Invalid date format !".
> >    I need to know how to format a field in Cobol to send the information
to
> >a field smalldatetime type.
> >
…[25 more quoted lines elided]…
> ema il: frederico_fonseca at syssoft-int.com
```

###### ↳ ↳ ↳ Re: Sending date type from Cobol to SQL

- **From:** Frederico Fonseca <real-email-in-msg-spam@email.com>
- **Date:** 2004-09-16T20:53:58+01:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<9lrjk092gsrivvt6nu4gv0g79c7jtutdvg@4ax.com>`
- **References:** `<4149c0e2$0$4904$a729d347@news.telepac.pt> <bfijk0lr1drjkh2lrd2vrgk9i6bh3f8q65@4ax.com> <4149d997$0$2499$a729d347@news.telepac.pt>`

```
On Thu, 16 Sep 2004 19:20:20 +0100, "local" <pt40br@hotmail.com>
wrote:

Top posting corrected.
>
>"Frederico Fonseca" <real-email-in-msg-spam@email.com> wrote in message
…[39 more quoted lines elided]…
>
The following works fine
 ENVIRONMENT     DIVISION.
 DATA            DIVISION.
 WORKING-STORAGE SECTION.
 01 ReturnValue pic s9(9) comp-5.
 PROCEDURE       DIVISION.
     invoke cmdb1 "OpenDB"  returning returnvalue.
     move "Text" OF cm2 to "field1" of cmdb1.
     INVOKE CmDb1 "WriteRecord" returning returnvalue.
     invoke cmdb1 "CloseDB"  returning returnvalue.

The value of the field cm2(Text field) is "2004/01/02" or "2004/01/05
12:31".
Both work.

If I try a incorrect value on the field I get a "NULL" value on the
table.




Frederico Fonseca
ema il: frederico_fonseca at syssoft-int.com
```

###### ↳ ↳ ↳ Re: Sending date type from Cobol to SQL

_(reply depth: 4)_

- **From:** "Euromercante" <remove_euromercante@sapo.pt>
- **Date:** 2004-09-21T12:07:08+01:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<41500b5e$0$4747$a729d347@news.telepac.pt>`
- **References:** `<4149c0e2$0$4904$a729d347@news.telepac.pt> <bfijk0lr1drjkh2lrd2vrgk9i6bh3f8q65@4ax.com> <4149d997$0$2499$a729d347@news.telepac.pt> <9lrjk092gsrivvt6nu4gv0g79c7jtutdvg@4ax.com>`

```
Hi,

    We've not been successfull with the example you send us, because it
still gives the same error message "Invalid Date Format" and doesn't gives
the Null value.
    The Render Text of the text field is standard or Cobol Picture?

Thanks
Euromercante


"Frederico Fonseca" <real-email-in-msg-spam@email.com> escreveu na mensagem
news:9lrjk092gsrivvt6nu4gv0g79c7jtutdvg@4ax.com...
> On Thu, 16 Sep 2004 19:20:20 +0100, "local" <pt40br@hotmail.com>
> wrote:
…[14 more quoted lines elided]…
> >> >    I need to know how to format a field in Cobol to send the
information
> >to
> >> >a field smalldatetime type.
…[49 more quoted lines elided]…
> ema il: frederico_fonseca at syssoft-int.com
```

###### ↳ ↳ ↳ Re: Sending date type from Cobol to SQL

_(reply depth: 5)_

- **From:** Frederico Fonseca <real-email-in-msg-spam@email.com>
- **Date:** 2004-09-21T20:30:00+01:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<oru0l09klc46iusfln5f3m89oc9q6auhav@4ax.com>`
- **References:** `<4149c0e2$0$4904$a729d347@news.telepac.pt> <bfijk0lr1drjkh2lrd2vrgk9i6bh3f8q65@4ax.com> <4149d997$0$2499$a729d347@news.telepac.pt> <9lrjk092gsrivvt6nu4gv0g79c7jtutdvg@4ax.com> <41500b5e$0$4747$a729d347@news.telepac.pt>`

```
Top posting corrected.

On Tue, 21 Sep 2004 12:07:08 +0100, "Euromercante"
<remove_euromercante@sapo.pt> wrote:
>"Frederico Fonseca" <real-email-in-msg-spam@email.com> escreveu na mensagem
>news:9lrjk092gsrivvt6nu4gv0g79c7jtutdvg@4ax.com...
…[73 more quoted lines elided]…
>Euromercante

Hi,

In order for this to work the value that is sent to "field1" of cmdb1
MUST be on a datetime format, e.g. yyyy/mm/dd or yyyy/mm/dd hh:mi.

So if using a cobol picture or a date render format you will need to
convert from the value returned by the "Text" property into the format
above.

e.g. assuming a "date render format" of MM/dd/yyyy you would need to
do the following.

 ENVIRONMENT     DIVISION.
 DATA            DIVISION.
 WORKING-STORAGE SECTION.
 01 ReturnValue pic s9(9) comp-5.
 01 returnzz pic -(9)9.
 01 val1 pic 9999/99/99.
 PROCEDURE       DIVISION.
     move "Text" OF cm4 to val1.
     move val1 to "field1" of cmdb1
     INVOKE CmDb1 "WriteRecord" returning returnvalue.



Frederico Fonseca
ema il: frederico_fonseca at syssoft-int.com
```

#### ↳ Re: Sending date type from Cobol to SQL

- **From:** Robert Wagner <robert@wagner.net.yourmammaharvests>
- **Date:** 2004-09-16T20:02:17+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<r3sjk0lh23v7s4cgveqbl3fpr5jh9td4nk@4ax.com>`
- **References:** `<4149c0e2$0$4904$a729d347@news.telepac.pt>`

```
On Thu, 16 Sep 2004 17:35:29 +0100, "Euromercante"
<remove_euromercante@sapo.pt> wrote:

>Hi,
>    I need to write a field type smalldatetime in SQL Server (2000) database
…[3 more quoted lines elided]…
>a field smalldatetime type.


Say 'set dateformat ymd;'. Format dates yyyy-mm-dd (10 bytes) in
Cobol.
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
