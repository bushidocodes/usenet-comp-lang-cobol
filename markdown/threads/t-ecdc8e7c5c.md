[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# PLUG: txt2pdf 7.5

_1 message · 1 participant · 2004-09_

---

### PLUG: txt2pdf 7.5

- **From:** mail@sanface.com (SANFACE Software)
- **Date:** 2004-09-13T05:48:33-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8c682947.0409130448.555a3314@posting.google.com>`

```
We would like to announce txt2pdf 7.5 version. 
http://www.sanface.com/txt2pdf.html
txt2pdf is shareware; it is a very flexible and powerful Perl5 script
that converts text files to PDF format files, so you can use it in
every operating systems supported by Perl5, including MPE/iX, OpenVMS
and EPOC.
It's simple to design background like invoices, orders etc.
Here nice examples made using txt2pdf PRO
http://www.sanface.com/pdf/Purchase_Order.pdf
http://www.sanface.com/pdf/oldinvoice.pdf
http://www.sanface.com/pdf/hfmus.pdf
http://www.sanface.com/pdf/heraldbill.pdf
If you prefer we also distribute executables for Windows, Linux,
Solaris, AIX, HP-UX, and Mac OS X. Inside the Windows version is
Visual txt2pdf, a VB GUI.
Remember to read the Hachette Filipacchi Media U.S. project at
http://www.aboutlegacycoding.com/archives/v4/v40603.asp

What's new in this version

To put one or more lines before the beginning of the PDF now you can
use inside txt2pdf.cfg prepdf.
This feature can be very useful. On Xerox printers + DocuSP controller
you can use Xerox Job ticket commands. The "options" must be placed at
the beginning of the pdf file, before the %PDF. To print duplex you
can use
prepdf: %XRXbegin: 001.0300\n%XRXPDLformat: PDF\n%XRXrequirements:
duplex\n%XRXend
(\n means go to a new line)
If you need more information about Xerox Job ticket or how to
configure it don't hesitate to contact us.
Pay attention: accordingly with PDF Specification 1.5 (specifically -
Implementation Notes 13 and 14) PDF Header in form "%PDF-M.m" or
"%!PS-Adobe-N.n PDF-M.m" should appear somewhere within the first 1024
bytes of the file. We suggest you to use this feature only to print
the pdf!

If you use email txt2pdf feature with priority now you can set the
email priority. The default 3 means X-Priority: 3 (Normal) and
X-MSMail-Priority: Normal. You can use also 1 X-Priority: 1 (Highest)
and X-MSMail-Priority: High or 5 X-Priority: 5 (Lowest) and
X-MSMail-Priority: Low

Test txt2pdf 7.5!
You can find it at http://www.sanface.com/txt2pdf.html
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
