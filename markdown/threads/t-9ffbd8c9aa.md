[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# RM-COBOL Index Structure

_5 messages · 5 participants · 2003-06_

**Topics:** [`Compilers and vendors`](../topics.md#compilers)

---

### RM-COBOL Index Structure

- **From:** "Davide Bortolini" <davide@comune.mogliano-veneto.tv.it>
- **Date:** 2003-06-03T12:25:11+02:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<pan.2003.06.03.10.25.11.485504@comune.mogliano-veneto.tv.it>`

```
Hi,
can anyone help me?
I would extract the entire database from a RM-COBOL Index Database but i
must know the RMFK format to extract data.
I've searched with google but I haven't fount too much infos.

Thanks
```

#### ↳ Re: RM-COBOL Index Structure

- **From:** "Johan den Boer" <me@knoware.nl>
- **Date:** 2003-06-03T17:05:35+02:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<vdpe9s1ft0usea@corp.supernews.com>`
- **References:** `<pan.2003.06.03.10.25.11.485504@comune.mogliano-veneto.tv.it>`

```
Hi,

In RM cobol you have a tool to display info about your index files. The tool
is

RMMAPINX  :  this produces a report describing the structure of an index
file created by RM/COBOL-85.
The tool display info about the keys, the position, length etc

It can be found on the utility disk of RM cobol.

Hope this helps

regards

Johan den Boer

email : johan@jdb.demon.nl

"Davide Bortolini" <davide@comune.mogliano-veneto.tv.it> schreef in bericht
news:pan.2003.06.03.10.25.11.485504@comune.mogliano-veneto.tv.it...
> Hi,
> can anyone help me?
…[5 more quoted lines elided]…
>
```

#### ↳ Re: RM-COBOL Index Structure

- **From:** "Danny Maijer" <info@liveartists.com>
- **Date:** 2003-06-03T17:34:32+02:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<bbif5k$evi$1@reader08.wxs.nl>`
- **References:** `<pan.2003.06.03.10.25.11.485504@comune.mogliano-veneto.tv.it>`

```
Hi Davide,

We have a long time experience in migration of data from RM/Cobol
applications to database environments. There is not a standard tool that
will provide you with a solution for your project. However, if you can get
hold of the file descriptors of the RM/Cobol applications we can provide you
with a toolset that generates conversion programs for your data files.

We can also deliver complete data migration. In other words, you deliver the
data files (.IDX files) and we return flat ASCII files to you for import in
a database.

If you are interested in our products and services, please feel free to
contact us at :

Maijer ICT Services
Attn. D. Maijer
Alkemaderschans 13
3432 CH  Nieuwegein
The Netherlands

Tel. +31 306579755
GSM +31 621242789
E-mail d.maijer@maijerict.net

"Davide Bortolini" <davide@comune.mogliano-veneto.tv.it> schreef in bericht
news:pan.2003.06.03.10.25.11.485504@comune.mogliano-veneto.tv.it...
> Hi,
> can anyone help me?
…[5 more quoted lines elided]…
>
```

#### ↳ Re: RM-COBOL Index Structure

- **From:** Scott Williamson <syw@cdvdc.demon.co.uk>
- **Date:** 2003-06-03T16:39:00+01:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<hvl6lBAUEM3+Ew$8@cdvdc.demon.co.uk>`
- **References:** `<pan.2003.06.03.10.25.11.485504@comune.mogliano-veneto.tv.it>`

```
In article <pan.2003.06.03.10.25.11.485504@comune.mogliano-
veneto.tv.it>, Davide Bortolini <davide@comune.mogliano-veneto.tv.it>
writes
>Hi,
>can anyone help me?
…[5 more quoted lines elided]…
>
Some years ago, I did some work on analysing the RM index file structure
and compression algorithms.  I was able to recover the original data
from any file (but NOT the internal record structure).
I wrote a brief paper on my findings and posted it to Wotsit's File
Formats (www.wotsit.org), and it should still be there.  
I've also written a number of programs to assist with recovering record
structures, and convert data to readable format.
```

#### ↳ Re: RM-COBOL Index Structure

- **From:** Frederico Fonseca <real-email-in-msg-spam@email.com>
- **Date:** 2003-06-03T17:48:22+01:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<tpjpdvk8n0jekih3qdeaciagj64hsdtgno@4ax.com>`
- **References:** `<pan.2003.06.03.10.25.11.485504@comune.mogliano-veneto.tv.it>`

```
On Tue, 03 Jun 2003 12:25:11 +0200, "Davide Bortolini"
<davide@comune.mogliano-veneto.tv.it> wrote:

>Hi,
>can anyone help me?
…[4 more quoted lines elided]…
>Thanks

Davide,

The internal RM file structure is not available to the public, but
this does not mean that it is not possible to do what you require.

If you have access to the FD (File Description) of the files then my
company can easly do the required programs to extract the data and
create normal text files with whatever field separator you need for
importing to other programs (e.g ".csv").

If you do not have access to the FD's it is still possible but will
imply a lot of trial and error to try and figure out the record
layout. This last one requires direct access to each file.

If you require more information please contact us through either of
the following emails.

info at syssoft-int.com
frederico_fonseca at syssoft-int.com


Best regards


Frederico Fonseca
ema il: frederico_fonseca at syssoft-int.com
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
