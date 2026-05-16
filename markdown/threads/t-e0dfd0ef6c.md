[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Problems with BMS to WEB conversion...

_2 messages · 2 participants · 2002-09_

**Topics:** [`Web, XML, modern integration`](../topics.md#web)

---

### Problems with BMS to WEB conversion...

- **From:** Simone Pagliani <member@mainframeforum.com>
- **Date:** 2002-09-19T04:03:42-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3d8992ee_6@news.onlynews.com>`

```
Hi!

I'm an italian mainframe programmer who's trying to integrate an
already existing CICS procedure with the web intranet of the company
I'm working in.

Other people developed this procedure, and I'm not allowed to modify the
COBOL CICS DB2 programs, I can just modify the BMS maps to add something
to the DFHMDX or add some DFHWBOUT to modify the graphic appearance of
the HTML pages.

We're now using the 2.2.0 version of the CICS, and we've been stuck by
a problem.

One of the maps has a group of rows listed and the operator can choose
which one modify putting a 'M' in the only field of the row who is
rewritable. There are 12 rows in a page, and if there are less then 12
records to modify the last ones are left blank.

In the BMS definition the selection field and the description field of
each row are set with an initial of all '_', and when the COBOL program
have to send for the first time the map it reads the records from the
DB2, fills the rows with what it has read, and moves spaces to all the
empty rows. But if I select a row and press the enter button, in the
selection fields of the empty rows the returning map contains LOW-VALUE
instead of spaces like it was in the sending. I've given a look to the
HTML of the page, and I've found that the selection field is valorized
as "" instead of " " like I expected, having moved SPACES to that field
in the program.

the row present itself as shown:
********
<tr> <td colspan=1 > </td> <td colspan=1 nowrap> <input type="hidden"
name="F140020001_DA3FU05" value=""> </td> <td colspan=9 nowrap> <input
type="hidden" name="F140040030_DA3CG05" value=" "> </td> <td colspan=5
nowrap> <input type="hidden" name="F140360030_DA3NM05" value=" "> </td>
<td colspan=2 nowrap> <input type="hidden" name="F140680010_DA3DT05"
value=" "> </td> </tr>
********

As you can see, the other fields of the row, DA3CG05, DA3NM05 and
DA3DT05 (surname, name and birthdate) are filled with spaces, just as it
should be. Instead, the selection field DA3FU05 is empty.

Is there a way I can obtain the same result even on the selection field
without, like I fear, modify the program? I�ve made a test creating a
personal copy of the program and adding in the input verification
section even the test for LOW-VALUE along to the test for SPACES, and in
this way it works, but it�s nothing I can do in the original version of
the program. I was looking for some modification of the BMS or, at the
very least, of the HTML template generated compiling the map.

By the way, is there some redbook in which I can find this kind of
argument? I have some, dfhtl00CICSInternetGuide and
sg245466ArchitectingWebAccessOnCICS mainly, but I haven�t found
something about this.

Tied to the previous questions, into the HTML template the map fields
are defined as F140040030_DA3CG05, where DA3CG05 is the name of the same
field inside the BMS. I supposed that the first part of the definition
was a way that descripts the field, but I haven�t found something about
this and how to translate this data. Could you help me or address me to
a specific redbook?

Thank you in advance.


Pagliani Simone
```

#### ↳ Re: Problems with BMS to WEB conversion...

- **From:** "Charles Hottel" <chottel@cpcug.org>
- **Date:** 2002-09-19T23:23:22+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<01c26033$3cf9d600$2e8bf243@chottel>`
- **References:** `<3d8992ee_6@news.onlynews.com>`

```
Each CICS map field has an attribute byte.  This may be set in the map
definintion, but regardless of that the program can still override it. When
the program moves spaces to the fieldnameO field, make sure it sets the
proper attribute in the fieldnameA field.  You want an attribute that sets
the modified data tag (MDT) so that when the user hits ENTER the spaces
will be returned to the program.  If you don't want to do this in the
program then you can do it with the map by giving the field the FSET
attribute.

Simone Pagliani <member@mainframeforum.com> wrote in article
<3d8992ee_6@news.onlynews.com>...
> Hi!
> 
…[71 more quoted lines elided]…
>
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
