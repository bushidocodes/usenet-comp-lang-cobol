[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Flat File to XML in COBOL Program.

_8 messages · 4 participants · 2008-01_

**Topics:** [`Web, XML, modern integration`](../topics.md#web)

---

### Flat File to XML in COBOL Program.

- **From:** Paul Knudsen <pknudsen@NOSPAMyahoo.com>
- **Date:** 2008-01-19T16:52:06-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<mk65p3t0gved4r3p9jnq230kjuo6pk5pan@4ax.com>`

```

Post on Kasamba, in case you missed it:  Can sign up and respond
directly if interested.

Hi, Need the link to tutorial or the book name that helps me to
modify/code COBOL program to convert flat file into XML format. I know
COBOL but don't know XML. Thanks
```

#### ↳ Re: Flat File to XML in COBOL Program.

- **From:** Richard <riplin@azonic.co.nz>
- **Date:** 2008-01-19T20:06:44-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8283182f-82c6-4a92-b2fe-41d80bbac256@c4g2000hsg.googlegroups.com>`
- **References:** `<mk65p3t0gved4r3p9jnq230kjuo6pk5pan@4ax.com>`

```


Paul Knudsen wrote:
> Post on Kasamba, in case you missed it:  Can sign up and respond
> directly if interested.
…[3 more quoted lines elided]…
> COBOL but don't know XML. Thanks

The way that I output XML (or HTML, CSV, etc), is to use a template
and a templating routine.

The template is just a text file. It could be in sections, or it could
use counters to repeat blocks as required.  The easiest way is to have
sections (here indicated by ':'). Options are started by '*':  Tags,
where data is substituted, are <!%tagname%>.

*XML
*CRLF
:header
<?XML ...
<order>
   <oderheader>
         <ordernumber><!%orederno%></ordernumber>
        <customer id="<!%customer%>">
              <customer_name><!%custname%></customername>
              <delivery_address>
                   <street><!%cdadd1%></street>
                  ....
              </delivery_address>
       </customer>
  </orederheader>
:oderline
  <orderline>
```

##### ↳ ↳ Re: Flat File to XML in COBOL Program.

- **From:** Paul Knudsen <pknudsen@NOSPAMyahoo.com>
- **Date:** 2008-01-20T19:08:41-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<a338p3ltq7fg7msge59bt68c9hi6fkfp8q@4ax.com>`
- **References:** `<mk65p3t0gved4r3p9jnq230kjuo6pk5pan@4ax.com> <8283182f-82c6-4a92-b2fe-41d80bbac256@c4g2000hsg.googlegroups.com>`

```
On Sat, 19 Jan 2008 20:06:44 -0800 (PST), Richard
<riplin@azonic.co.nz> wrote:

>
>
…[32 more quoted lines elided]…
>  <orderline>

Chuckle...I doubt anyone who doesn't know XML will get this.   But on
the off-chance, have I your permission to forward it to the requestor?
```

###### ↳ ↳ ↳ Re: Flat File to XML in COBOL Program.

- **From:** Richard <riplin@azonic.co.nz>
- **Date:** 2008-01-20T23:26:48-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<33058073-6e21-411a-a200-ac38cc7d23fc@m34g2000hsb.googlegroups.com>`
- **References:** `<mk65p3t0gved4r3p9jnq230kjuo6pk5pan@4ax.com> <8283182f-82c6-4a92-b2fe-41d80bbac256@c4g2000hsg.googlegroups.com> <a338p3ltq7fg7msge59bt68c9hi6fkfp8q@4ax.com>`

```
On Jan 21, 4:08 pm, Paul Knudsen <pknud...@NOSPAMyahoo.com> wrote:
> On Sat, 19 Jan 2008 20:06:44 -0800 (PST), Richard
>
…[39 more quoted lines elided]…
> the off-chance,

The whole point about templating is that you need neither know nor
care what XML, or HTML, or CSV, or whatever is.

Get someone to make up an example of what is required in the output
file then divide that up into the sections that are the header,
trailer and the bits that repeat for each 'line'. Use different
sections if the layout varies in the repeating bits and change the
data items into tagnames.

Write the program to deal with the data and the result should match
the example. No need to even know that it is XML.

I liked one comment that I saw about XML:

"They have a problem and so decide to use XML. They then have two
problems."


> have I your permission to forward it to the requestor?

Yes, of course.
```

#### ↳ Re: Flat File to XML in COBOL Program.

- **From:** Richard <riplin@azonic.co.nz>
- **Date:** 2008-01-19T20:23:02-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<9f91662c-d33f-4d27-ace2-b8e89431b72c@e10g2000prf.googlegroups.com>`
- **References:** `<mk65p3t0gved4r3p9jnq230kjuo6pk5pan@4ax.com>`

```


Paul Knudsen wrote:
> Post on Kasamba, in case you missed it:  Can sign up and respond
> directly if interested.
…[3 more quoted lines elided]…
> COBOL but don't know XML. Thanks

The way that I output XML (or HTML, CSV, etc), is to use a template
and a templating routine.

The template is just a text file. It could be in sections, or it could
use counters to repeat blocks as required.  The easiest way is to have
sections (here indicated by ':'). Options are started by '*':  Tags,
where data is substituted, are <!%tagname%>.

*XML
*CRLF
:header
<?XML ...
<order>
   <oderheader>
         <ordernumber><!%orderno%></ordernumber>
        <customer id="<!%customer%>">
              <customer_name><!%custname%></customername>
              <delivery_address>
                   <street><!%cdadd1%></street>
                  ....
              </delivery_address>
       </customer>
  </orederheader>
:oderline
  <orderline>
        <product><!%prodcode%></product>
        ....

  </orderline>
:trailer
</order>

In the application set up a table of tagname: value pairs, probably
preset in W-S.

      01  XML-Header.
            03    FILLER              PIC X(12) VALUE "orderno".
            03     XML-OrderNo   PIC X(40).
            03    FILLER              PIC X(12) VALUE "customer".
            03     XML-Customer  PIC X(40).
            .....
            03    FILLER              PIC X(12) VALUE SPACES
            03     FILLER            PIC X(40).

    01  XML-OrderLine.
            03    FILLER              PIC X(12) VALUE "prodcode".
            03     XML-ProdCode  PIC X(40).
            ....

Ine the program:

          MOVE ??      TO XML-OrderNo
          MOVE ..          TO XML-Customer

          CALL "template"  USING "xmlorder" "header" XML-Header

          PERFORM
                 UNTIL all lines output

              MOVE ??      TO XML-ProdCode
              MOVE ..          TO XML-OrderQty

              CALL "template"  USING "xmlorder" "orderline" XML-
OrderLine
         END-PERFORM

          CALL "template"  USING "xmlorder" "trailer" XML-Trailer

In program template:

         LINKAGE SECTION.
         01  Template-Name             PIC X(12).
         01  Template-Section           PIC X(12).
          01  Template-Data.
               03  Template-Item          OCCURS 100.
                05  Template-Tag        PIC X(12).
                05  Tremplate-Value    PIC X(40).
        PROCEDURE DIVISION.

The program needs to identify first time in so it will open and read
the template into an array and set up a table of sections with start
end indexes into the line table.

Then for each line in the section being output replace the tagnames
with the value from the table.  (a space tagname ends the table).

Then you won't care about what the output looks like.  If it needs to
change just adjust the template. If they want it as a CSV or HTML or
some other then just use a different template.
```

#### ↳ Re: Flat File to XML in COBOL Program.

- **From:** "Michael Mattias" <mmattias@talsystems.com>
- **Date:** 2008-01-20T08:41:22-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<0uJkj.2045$Rg1.1317@nlpi068.nbdc.sbc.com>`
- **References:** `<mk65p3t0gved4r3p9jnq230kjuo6pk5pan@4ax.com>`

```
"Paul Knudsen" <pknudsen@NOSPAMyahoo.com> wrote in message 
news:mk65p3t0gved4r3p9jnq230kjuo6pk5pan@4ax.com...
>
> Hi, Need the link to tutorial or the book name that helps me to
> modify/code COBOL program to convert flat file into XML format. I know
> COBOL but don't know XML. Thanks

Tutorials on XML (and much much more):  http://www.w3schools.com/

MCM
```

##### ↳ ↳ Re: Flat File to XML in COBOL Program.

- **From:** Paul Knudsen <pknudsen@NOSPAMyahoo.com>
- **Date:** 2008-01-20T19:29:59-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1c38p3l0ht359pm2e8b59qjmo958qhe3bv@4ax.com>`
- **References:** `<mk65p3t0gved4r3p9jnq230kjuo6pk5pan@4ax.com> <0uJkj.2045$Rg1.1317@nlpi068.nbdc.sbc.com>`

```
On Sun, 20 Jan 2008 08:41:22 -0600, "Michael Mattias"
<mmattias@talsystems.com> wrote:

>Tutorials on XML (and much much more):  http://www.w3schools.com/

Thanks.  I'll give this to the requester gratis.
```

#### ↳ Re: Flat File to XML in COBOL Program.

- **From:** "William M. Klein" <wmklein@nospam.netcom.com>
- **Date:** 2008-01-21T01:12:14+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<OjSkj.40845$Yh2.5583@fe08.news.easynews.com>`
- **References:** `<mk65p3t0gved4r3p9jnq230kjuo6pk5pan@4ax.com>`

```
What is your COBOL compiler? Some (not all) COBOL compilers have specific syntax 
to do this "automatically" (more or less).  (Even with those, you can use "brute 
force" coding - and may even need to for some types of XML).
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
