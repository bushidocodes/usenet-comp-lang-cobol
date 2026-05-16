[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# fxd to html

_6 messages · 5 participants · 2009-04 → 2009-05_

**Topics:** [`Web, XML, modern integration`](../topics.md#web)

---

### fxd to html

- **From:** mario <mmc_vw1200@hotmail.com>
- **Date:** 2009-04-30T06:35:55-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<9e1c91b4-876b-4668-b963-eed06f4251f1@n7g2000prc.googlegroups.com>`

```
hi everyone,

i´m looking for a tool that gives me a html or something useful to
write a documentation of my included files.
freeware would be the best ;)
any idears, how do u document your projects ??


kind regards
mario
```

#### ↳ Re: fxd to html

- **From:** docdwarf@panix.com ()
- **Date:** 2009-04-30T13:54:57+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gtcajh$365$7@reader1.panix.com>`
- **References:** `<9e1c91b4-876b-4668-b963-eed06f4251f1@n7g2000prc.googlegroups.com>`

```
In article <9e1c91b4-876b-4668-b963-eed06f4251f1@n7g2000prc.googlegroups.com>,
mario  <mmc_vw1200@hotmail.com> wrote:

[snip]

>any idears, how do u document your projects ??

I document my projects in the way that the person who signs my timesheets 
requests it; I document my code with comment-lines.

DD
```

#### ↳ Re: fxd to html

- **From:** Alain Reymond <arwebmail@skynet.be>
- **Date:** 2009-04-30T17:58:42+02:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<49f9cac7$0$2868$ba620e4c@news.skynet.be>`
- **In-Reply-To:** `<9e1c91b4-876b-4668-b963-eed06f4251f1@n7g2000prc.googlegroups.com>`
- **References:** `<9e1c91b4-876b-4668-b963-eed06f4251f1@n7g2000prc.googlegroups.com>`

```
mario a ï¿½crit :
> hi everyone,
>
…[8 more quoted lines elided]…
>   
Robodoc is what you need!

It is a simple yet powerful documentation system.
http://www.xs4all.nl/~rfsber/Robo/robodoc.html

You include your documentation in the source code. Then, you generate an
html file with the complete doc.
It is easy, freeware and useful.

Here is an example of the comments placed at the beginning og a source
file :

       *>***h* Application/myprogram
       *> NAME
       *>  myprogram
       *> FUNCTION
       *>  Description of what the programm does
       *>  and so on ...
       *> USAGE
       *>  Is called by
       *> INPUTS
       *>  lnk-i1-duplicata : 1 if true
       *>                     0 if false
       *> OUTPUT
       *>  A PostScript file or pdf file
       *> USES
       *>  prog1
       *>  prog2
       *>  prog3
       *> USED BY
       *>  prog4
       *>  prog5
       *> HISTORY
       *>  23/07/2008 : modification 2
       *>  09/10/2007 : modification 1
       *>  08/06/2006 : creation
       *>**


If you do the same with prog1, prog2, etc..., Robodoc will generate the
links.

Robodoc does not come with a definition for Cobol. You can easily use it
by creating a cobol.rc file that contains the definitions for cobol.
Here is what I use :
#
# Cobol.rc
#
accept files:
    *.cbl
headertypes:
    p  Paragraph
header markers:
    *>***
remark markers:
    *>
end markers:
    *>**
options:
    --src ./.
    --doc api
    --singledoc
    --html
    --tell
    --nodesc
    --index
    --sections
    --toc

Then, call robodoc so :
    robodoc --rc  cobol.rc

Hope this helps.

Regards,

Alain
```

##### ↳ ↳ Re: fxd to html

- **From:** Alain Reymond <arwebmail@skynet.be>
- **Date:** 2009-05-08T14:41:28+02:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<4a0428af$0$2861$ba620e4c@news.skynet.be>`
- **In-Reply-To:** `<49f9cac7$0$2868$ba620e4c@news.skynet.be>`
- **References:** `<9e1c91b4-876b-4668-b963-eed06f4251f1@n7g2000prc.googlegroups.com> <49f9cac7$0$2868$ba620e4c@news.skynet.be>`

```


Alain Reymond a ï¿½crit :
> mario a ï¿½crit :
>   
…[89 more quoted lines elided]…
>   

To complete that, you will find an article on the OpenCobol Forum with a
nice configuration for Robodoc.
http://www.opencobol.org/modules/newbb/viewtopic.php?topic_id=580&forum=1

Regards

Alain
```

#### ↳ Re: fxd to html

- **From:** "Pete Dashwood" <dashwood@removethis.enternet.co.nz>
- **Date:** 2009-05-01T15:30:55+12:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<75v8neF19o1vhU1@mid.individual.net>`
- **References:** `<9e1c91b4-876b-4668-b963-eed06f4251f1@n7g2000prc.googlegroups.com>`

```
mario wrote:
> hi everyone,
>
…[4 more quoted lines elided]…
>

I have Dobby the house elf do it while I'm asleep.

Then, the next day I change everything and he can do it all again.

He's a miserable little toad and never smiles. Can't imagine why...

Pete.
```

##### ↳ ↳ Re: fxd to html

- **From:** "Michael Mattias" <mmattias@talsystems.com>
- **Date:** 2009-05-01T08:58:58-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<YeDKl.25763$c45.3867@nlpi065.nbdc.sbc.com>`
- **References:** `<9e1c91b4-876b-4668-b963-eed06f4251f1@n7g2000prc.googlegroups.com> <75v8neF19o1vhU1@mid.individual.net>`

```
> i�m looking for a tool that gives me a html or something useful to
> write a documentation of my included files.
> freeware would be the best ;)
> any idears, how do u document your projects ??

I believe that tool is called, "better work habits with regard to 
documentation"

MCM
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
