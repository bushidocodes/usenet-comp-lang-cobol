[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# C-like strings in MicroFocus COBOL ?

_34 messages · 13 participants · 1999-10 → 1999-11_

**Topics:** [`Compilers and vendors`](../topics.md#compilers)

---

### C-like strings in MicroFocus COBOL ?

- **From:** "Jacques Vidal" <syster.soft@wanadoo.fr>
- **Date:** 1999-10-28T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7v96cn$que$1@wanadoo.fr>`

```
Hi,

I've been told there's a way (compiler directive or another) to have pic
X(n)
data items to behave as C-strings (binary zeroes appended to the end of
the data item). Eg,

    move "Something" to mystring.

would behave as:

    move "Something" & x"00" to mystring.

So far, I've found no evidence of this in the MicroFocus documentation. Is
all this true or legend?

Jacques Vidal
```

#### ↳ Re: C-like strings in MicroFocus COBOL ?

- **From:** "James J. Gavan" <jjgavan@home.com>
- **Date:** 1999-10-28T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3818875A.6BFDB19B@home.com>`
- **References:** `<7v96cn$que$1@wanadoo.fr>`

```


Jacques Vidal wrote:
> 
> Hi,
…[13 more quoted lines elided]…
> all this true or legend?

Jacques,

Fact not fiction. But I had a hell of a time trying to find it from
on-line help in Visoc/NetExpress, and never did, (even with all the
cross-referencing), so I went by coded examples - and here are two
examples of usage contained in the same piece of code :-

       01 ws-Windowtitle               pic x(15) value
                                       z"Vessel Records".

	*> Note size of ws-WindowTitle - 15 not 14, it means
	*> "Vessel Records" & x"00"

	.........
        invoke MessageBox "new" using os-Parent returning ls-MsgBox
        invoke ls-MsgBox "setTitleZ" using ws-Windowtitle
        string
          ls-text                       delimited by "  "
          x"0d0a"                       delimited by size
          "do you wish to delete this line ? "
                                        delimited by size
          x"0d0a"                       delimited by size
          x"00"                         delimited by size
          into ls-MessageText
        End-string

        invoke ls-MsgBox "setTypeWarning"
        invoke ls-MsgBox "YesNo"
        move length of ls-MessageText to ls-length
        invoke CharacterArray "withlengthvalue"
          using ls-length ls-MessageText returning ls-String
        invoke ls-MsgBox "setMessage" using ls-String
         *> You can also use "setMessageZ".......
        invoke ls-MsgBox "show" returning lnk-response
        invoke ls-string "finalize" returning ls-string
        invoke ls-MsgBox "finalize" returning ls-MsgBox


.... and the x"00" at the end of the stringing.

Jimmy, Calgary AB
```

##### ↳ ↳ Re: C-like strings in MicroFocus COBOL ?

- **From:** "Simon R Hart" <hart1@technologist.com>
- **Date:** 1999-10-28T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7vaf2o$pc2$2@plutonium.btinternet.com>`
- **References:** `<7v96cn$que$1@wanadoo.fr> <3818875A.6BFDB19B@home.com>`

```

James J. Gavan wrote in message <3818875A.6BFDB19B@home.com>...
>
>
…[15 more quoted lines elided]…
>> So far, I've found no evidence of this in the MicroFocus documentation.
Is
>> all this true or legend?
>
…[40 more quoted lines elided]…
>Jimmy, Calgary AB


Good stuff Jimmy boy........



Simon R Hart
Eaton, Ottery St. Mary, UK.
```

###### ↳ ↳ ↳ Re: C-like strings in MicroFocus COBOL ?

- **From:** "James J. Gavan" <jjgavan@home.com>
- **Date:** 1999-10-28T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3818CF4F.24B1CA9A@home.com>`
- **References:** `<7v96cn$que$1@wanadoo.fr> <3818875A.6BFDB19B@home.com> <7vaf2o$pc2$2@plutonium.btinternet.com>`

```


Simon R Hart wrote:
> 
> James J. Gavan wrote in message <3818875A.6BFDB19B@home.com>...
…[25 more quoted lines elided]…
> ><snip>

> >Jimmy, Calgary AB
> 
> Good stuff Jimmy boy........

I keep on telling you stop the 'love-fest' - they'll all start thinking
we've got somethin' goin' ????? <G>

Jimmy
```

##### ↳ ↳ Re: C-like strings in MicroFocus COBOL ?

- **From:** "Ken Mullins" <KenMullins@mindspring.com>
- **Date:** 1999-10-28T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7vanmq$qli$1@nntp3.atl.mindspring.net>`
- **References:** `<7v96cn$que$1@wanadoo.fr> <3818875A.6BFDB19B@home.com>`

```

Not to change the subject here, but Jimmy, isn't that an aweful lot of
invokes (calls) to do a simple messagebox...???...I have heard about
overhead in oo, but man, I would die just typing all that in...  :-))

             Compute mbStyle = MB-OK + MB-IconHand + MB-SYSTEMMODAL.
             Call WinAPI MessageBoxA
               using by value hDeskTop
                         by value mbStyle
                         by reference z'Hello' & x'0d0a' & 'Hello again'
                         by reference ws-windowtitle
               returning MBResponse.

kenmullins

James J. Gavan <jjgavan@home.com> wrote in message
news:3818875A.6BFDB19B@home.com...
>
>
…[15 more quoted lines elided]…
> > So far, I've found no evidence of this in the MicroFocus documentation.
Is
> > all this true or legend?
>
…[40 more quoted lines elided]…
> Jimmy, Calgary AB
```

###### ↳ ↳ ↳ Re: C-like strings in MicroFocus COBOL ?

- **From:** "James J. Gavan" <jjgavan@home.com>
- **Date:** 1999-10-29T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3818FE55.929E5ABE@home.com>`
- **References:** `<7v96cn$que$1@wanadoo.fr> <3818875A.6BFDB19B@home.com> <7vanmq$qli$1@nntp3.atl.mindspring.net>`

```


Ken Mullins wrote:
> 
> Not to change the subject here, but Jimmy, isn't that an aweful lot of
…[10 more quoted lines elided]…
> 

Valid point Ken. But this hombre is an ex-analyst not a hot-shot
programmer. It works, and really I'm not typing it - I copy/paste big
chunks. One of the things I'd like to do when my guy goes Y2K is check
back and see where I can take short-cuts all over the place, both Base
and GUI classes. Right now given time, I could create my own class
MyMessageBox to take away the drudgery, just as I told you I have
MakeMenu.

(Just took a look at the Class Messagebox; it has a method for
DefaultFlags; could be that I could 'add them up' as you have in your
API example - but once more Newbury, until there are examples ....., or
I have the time to suck-it-and-see.....)

What I don't like, and I know it's your preference, and you have used it
to great success, is that APIs tie you into Windows as does D/S tie you
into N/E. Same applies to GUIs of course, subject to following
paragraph. And while we talk Windows - Pete Dashwood promotes ActiveX,
with which I'm not yet familiar - but doesn't that also assume Windows
is the de facto standard ?

If Standards, J4 etc., do their homework properly - we might just find
the GUI approach, (vastly simplified, I hope), is closest to becoming
non-platform specific, or at least 'markers' set to allow you to switch
platforms. They've got a lot of homework to do, Amsterdam Spring 2000 -
another year before compiler vendors do anything ? - something like
COBOL-2002/3. Meanwhile, other than the 'broad' outline for OO they
haven't done anything about standardized classes - so look hopefully
towards COBOL-2005 - could be dribbling in my bib by then <G>.

Jimmy
```

###### ↳ ↳ ↳ Re: C-like strings in MicroFocus COBOL ?

_(reply depth: 4)_

- **From:** "Ken Mullins" <KenMullins@mindspring.com>
- **Date:** 1999-10-28T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7vauu6$he0$1@nntp3.atl.mindspring.net>`
- **References:** `<7v96cn$que$1@wanadoo.fr> <3818875A.6BFDB19B@home.com> <7vanmq$qli$1@nntp3.atl.mindspring.net> <3818FE55.929E5ABE@home.com>`

```
what I do is code my own API interfaces contained as entry points in a
module I refer to as "common routines"...I have a "common routines" for OS/2
and one for windows...the call is the same in the actual application
code...For example I have a callable entry point called crMessageBox...the
code for this is different in the "common routines" module for OS/2 vs the
"common routines" for windows...But the application program calls
crMessageBox with the same parameters so it will compile and run in either
environment without change...Simply include the appropriate common routines
module in the link...

Not positive, but a lot of the OO stuff in netexpress is probably tied to
windows only also because of API calls...I do not use panels2 because it
seemed too slow...

kenmullins

James J. Gavan <jjgavan@home.com> wrote in message
news:3818FE55.929E5ABE@home.com...
>
>
…[44 more quoted lines elided]…
> Jimmy
```

###### ↳ ↳ ↳ Re: C-like strings in MicroFocus COBOL ?

_(reply depth: 5)_

- **From:** "James J. Gavan" <jjgavan@home.com>
- **Date:** 1999-10-29T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<381911EC.221E642A@home.com>`
- **References:** `<7v96cn$que$1@wanadoo.fr> <3818875A.6BFDB19B@home.com> <7vanmq$qli$1@nntp3.atl.mindspring.net> <3818FE55.929E5ABE@home.com> <7vauu6$he0$1@nntp3.atl.mindspring.net>`

```


Ken Mullins wrote:
> 
> 
> Not positive, but a lot of the OO stuff in netexpress is probably tied to
> windows only also because of API calls...I do not use panels2 because it
> seemed too slow...

You are right Ken. If you look at the source of the GUI classes, you
will see eventuially they make API calls to Windows.

Jimmy
```

###### ↳ ↳ ↳ Re: C-like strings in MicroFocus COBOL ?

_(reply depth: 4)_

- **From:** "Cheesle" <cheesle@online.NoSpamPlease.no>
- **Date:** 1999-10-29T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7vcc9k$78v$1@news.cerf.net>`
- **References:** `<7v96cn$que$1@wanadoo.fr> <3818875A.6BFDB19B@home.com> <7vanmq$qli$1@nntp3.atl.mindspring.net> <3818FE55.929E5ABE@home.com>`

```
James J. Gavan wrote in message <3818FE55.929E5ABE@home.com>...
>Ken Mullins wrote:
>> Not to change the subject here, but Jimmy, isn't that an aweful lot of
>> invokes (calls) to do a simple messagebox...???...I have heard about

Speaking about message boxes and simplicity, here is how I do it in
Acucobol...

        DISPLAY MESSAGE BOX  "Yes it is simple!"
                TYPE IS mb-ok
                 ICON IS mb-error-icon
                 GIVING message-answer.

This will show up on character and gui.

Cheesle
```

###### ↳ ↳ ↳ Re: C-like strings in MicroFocus COBOL ?

_(reply depth: 5)_

- **From:** "James J. Gavan" <jjgavan@home.com>
- **Date:** 1999-10-29T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3819D244.12C36CDD@home.com>`
- **References:** `<7v96cn$que$1@wanadoo.fr> <3818875A.6BFDB19B@home.com> <7vanmq$qli$1@nntp3.atl.mindspring.net> <3818FE55.929E5ABE@home.com> <7vcc9k$78v$1@news.cerf.net>`

```


Cheesle wrote:
> 
> Speaking about message boxes and simplicity, here is how I do it in
…[8 more quoted lines elided]…
> 
Just clarify for me, because you've mentioned it before. Your above
example - is there a switch/flag to say you are using character or GUI
in Acu, or can you intermix char/GUI ?

Jimmy
```

###### ↳ ↳ ↳ Re: C-like strings in MicroFocus COBOL ?

_(reply depth: 6)_

- **From:** Richard Plinston <riplin@kcbbs.gen.nz>
- **Date:** 1999-10-29T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7vcvag$n4$1@aklobs.kc.net.nz>`
- **References:** `<7v96cn$que$1@wanadoo.fr> <3818875A.6BFDB19B@home.com> <7vanmq$qli$1@nntp3.atl.mindspring.net> <3818FE55.929E5ABE@home.com> <7vcc9k$78v$1@news.cerf.net> <3819D244.12C36CDD@home.com>`

```
James J. Gavan <jjgavan@home.com> wrote:

: Just clarify for me, because you've mentioned it before. Your above
: example - is there a switch/flag to say you are using character or GUI
: in Acu, or can you intermix char/GUI ?

If a GUI (eg Windows) run-time is being used then it will
display a GUI message, if a text mode run-time is being
used (eg Unix dumb terminal) then a character mode
message will display.

The program itself need not know nor care where it is being
run, nor need it be recompiled (but then it is just compiled
to 'intermediate or 'byte' code to allow it to run on any
run-time system).
```

###### ↳ ↳ ↳ Re: C-like strings in MicroFocus COBOL ?

_(reply depth: 7)_

- **From:** "James J. Gavan" <jjgavan@home.com>
- **Date:** 1999-10-29T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<381A0C71.4DB497D2@home.com>`
- **References:** `<7v96cn$que$1@wanadoo.fr> <3818875A.6BFDB19B@home.com> <7vanmq$qli$1@nntp3.atl.mindspring.net> <3818FE55.929E5ABE@home.com> <7vcc9k$78v$1@news.cerf.net> <3819D244.12C36CDD@home.com> <7vcvag$n4$1@aklobs.kc.net.nz>`

```


Richard Plinston wrote:
> 
> James J. Gavan <jjgavan@home.com> wrote:
…[14 more quoted lines elided]…
> 
Richard and Cheesle,

Taking this one step further - is Acu close to my 'dream' of platform
indepedent GUIs or is this Acu-specific ? I understand the int code, but
what about byte ? One of the criticisms I see mentioned about Java is
that it is slow because it uses byte code.

Jimmy
```

###### ↳ ↳ ↳ Re: C-like strings in MicroFocus COBOL ?

_(reply depth: 8)_

- **From:** "Cheesle" <cheesle@online.NoSpamPlease.no>
- **Date:** 1999-10-29T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7vd83v$84c$1@news.cerf.net>`
- **References:** `<7v96cn$que$1@wanadoo.fr> <3818875A.6BFDB19B@home.com> <7vanmq$qli$1@nntp3.atl.mindspring.net> <3818FE55.929E5ABE@home.com> <7vcc9k$78v$1@news.cerf.net> <3819D244.12C36CDD@home.com> <7vcvag$n4$1@aklobs.kc.net.nz> <381A0C71.4DB497D2@home.com>`

```
James J. Gavan wrote in message <381A0C71.4DB497D2@home.com>...
>Taking this one step further - is Acu close to my 'dream' of platform
>indepedent GUIs or is this Acu-specific ? I understand the int code, but
>what about byte ? One of the criticisms I see mentioned about Java is
>that it is slow because it uses byte code.

Well, I am not sure about details here. What I do know, is that the compiled
intermediate code is portable, there is no need for recompile. About speed?

Well, if you are analyzing a 128 Mb string for occurences of capital A, I am
most certain that Any C application will outperform Acucobol by 1 : 100 if
not more.

If you keep in mind that most Cobol application does database access, which
Acucobol in my opinion does pretty good, you won't see much difference, if
any at all.

When it comes to portable gui, I don't know for sure, but my guess is that
they currently only support windows, all other hosts are character (please
correct me anyone if I am wrong). On the other side, as mentioned in another
mail, most of their controls are supported in both worlds, like one of the
newest ones, the Treeview control, which is available in both worlds.
Without syntax differences of course.

Ok, ok, I see the wave; how about positioning. Yes that is an issue, as one
definitely can't just "down scale" a gui to character. There is a solution
as well. In the Screen Section they support two labels;
    GRAPHICAL
    CHARACTER

Which is checked real time.

Which means that I would for instance:
CODE START
    Screen Section.
            01 My-Screen.
        GRAPHICAL
              03  label "Mylabel",
                       line 1.5, column 21, size 25,
                       font large-font, center.

               03  bitmap, graphical, bitmap-handle = gt-bitmap,
                       size 39, bitmap-start = 1, bitmap-end = 15,
                       bitmap-timer = 10,
                       line 1.5, column 57.

               03  frame, rimmed, font small-font
                       line 4, column 4, size 32, lines 9.

               03  entry-field, using entry-data-1
                       column + 2, 3-d.

        CHARACTER
              03  label "Mylabel",
                       line 1, column 21, size 25.

               03  frame, rimmed, font small-font
                       line 4, column 4, size 32, lines 9.

               03  entry-field, using entry-data-1
                       column + 2.

    Procedure Division.
    Main Section.
    Main-001.
        Display    MyScreen.
        Accept MyScreen Allowing Messages From Any Thread.
CODE END

and so on, Threads? Of course there are threads, portable too!

I am for sure positive that Acucobol is way faster than Java.

I don't know if this was an appropriate answer though.

Cheesle
```

###### ↳ ↳ ↳ Re: C-like strings in MicroFocus COBOL ?

_(reply depth: 8)_

- **From:** thaneH@softwaresimple.com (Thane Hubbell)
- **Date:** 1999-10-30T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<381a6d18.209681089@news1.attglobal.net>`
- **References:** `<7v96cn$que$1@wanadoo.fr> <3818875A.6BFDB19B@home.com> <7vanmq$qli$1@nntp3.atl.mindspring.net> <3818FE55.929E5ABE@home.com> <7vcc9k$78v$1@news.cerf.net> <3819D244.12C36CDD@home.com> <7vcvag$n4$1@aklobs.kc.net.nz> <381A0C71.4DB497D2@home.com>`

```
On Fri, 29 Oct 1999 20:58:24 GMT, "James J. Gavan" <jjgavan@home.com>
wrote:

>Taking this one step further - is Acu close to my 'dream' of platform
>indepedent GUIs or is this Acu-specific ? I understand the int code, but
>what about byte ? One of the criticisms I see mentioned about Java is
>that it is slow because it uses byte code.

The one thing that wasn't answered in Cheesle's reply - Yes this is an
AcuCorp specific extension to the Screen Section.  It is not portable
between compilers.

As far as file access goes, I don't know about Vision  files.  Before
Vision, their file system was the slowest of all PC COBOLS.  It was
one reason I chose Realia in 1991, but all that may have changed -
Vision files may have superior performance to the current Ca-Realia
file system, I do not know.


---
Try a better search engine:  http://www.google.com
My personal web site: http://www.geocities.com/Eureka/2006/
```

###### ↳ ↳ ↳ Re: C-like strings in MicroFocus COBOL ?

_(reply depth: 9)_

- **From:** "James J. Gavan" <jjgavan@home.com>
- **Date:** 1999-10-30T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<381B4ECD.54E3C01A@home.com>`
- **References:** `<7v96cn$que$1@wanadoo.fr> <3818875A.6BFDB19B@home.com> <7vanmq$qli$1@nntp3.atl.mindspring.net> <3818FE55.929E5ABE@home.com> <7vcc9k$78v$1@news.cerf.net> <3819D244.12C36CDD@home.com> <7vcvag$n4$1@aklobs.kc.net.nz> <381A0C71.4DB497D2@home.com> <381a6d18.209681089@news1.attglobal.net>`

```


Thane Hubbell wrote:
> 
> On Fri, 29 Oct 1999 20:58:24 GMT, "James J. Gavan" <jjgavan@home.com>
…[15 more quoted lines elided]…
> file system, I do not know.

Thane,

I was intrigued by Cheesle's examples. Wouldn't it be really nice if we
could take chunks of the various compilers and select the bits that
appealed to us, based on flexibility, speed, file-handling etc.

I sympathize with Judson - at some stage has to make a decision, which
way to jump, Fujitsu or NetExpress - would be nice if he could merge the
bits from each that he likes. Having made that decision, he's locked
into a particular compiler for specific applications.

I'm sure AcuCorp will have improved on file access. The only outfit in
downtown Calgary that I ever talked to was a bunch of head-hunters,
(head-quartered, I believe, in the States) Towers Perrin. They used M/F
from the early days - didn't like file-handling, so wrote their own.
Pretty ambitious for such a specialized area. And no doubt, having
written it, insist their people continue to use it, even though M/F is
now conceivably faster and has 'goodies' like split alternate keys. (Add
to the above that they were running applictions in THREE versions of M/F
COBOL - Ugggh!)

Jimmy, Calgary AB
```

###### ↳ ↳ ↳ Re: C-like strings in MicroFocus COBOL ?

_(reply depth: 10)_

- **From:** "Cheesle" <cheesle@online.NoSpamPlease.no>
- **Date:** 1999-10-31T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7vjauq$mam$1@news.cerf.net>`
- **References:** `<7v96cn$que$1@wanadoo.fr> <3818875A.6BFDB19B@home.com> <7vanmq$qli$1@nntp3.atl.mindspring.net> <3818FE55.929E5ABE@home.com> <7vcc9k$78v$1@news.cerf.net> <3819D244.12C36CDD@home.com> <7vcvag$n4$1@aklobs.kc.net.nz> <381A0C71.4DB497D2@home.com> <381a6d18.209681089@news1.attglobal.net> <381B4ECD.54E3C01A@home.com>`

```
James J. Gavan wrote in message <381B4ECD.54E3C01A@home.com>...
>I was intrigued by Cheesle's examples. Wouldn't it be really nice if we
>could take chunks of the various compilers and select the bits that
>appealed to us, based on flexibility, speed, file-handling etc.

Great idea!

I have always wanted to know more about other Cobol's. I guess the message
box is my contribution so far. Anyone else?

Cheesle
```

###### ↳ ↳ ↳ Re: C-like strings in MicroFocus COBOL ?

_(reply depth: 6)_

- **From:** "Cheesle" <cheesle@online.NoSpamPlease.no>
- **Date:** 1999-10-29T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7vd776$lfb$1@news.cerf.net>`
- **References:** `<7v96cn$que$1@wanadoo.fr> <3818875A.6BFDB19B@home.com> <7vanmq$qli$1@nntp3.atl.mindspring.net> <3818FE55.929E5ABE@home.com> <7vcc9k$78v$1@news.cerf.net> <3819D244.12C36CDD@home.com>`

```
James J. Gavan wrote in message <3819D244.12C36CDD@home.com>...
>
>
…[14 more quoted lines elided]…
>in Acu, or can you intermix char/GUI ?

That is the cool thing about it all. This is it, I don't have to think about
where this is to be displayed. I just want a message box, and I am getting
it, no matter where the application is ran. Be it Windows, MSDOS, OS/2,
Linux, VMS...

No switch, no flag.

I don't even need to recompile.

The same applies for almost all controls of Acucobol.

Cheesle
```

###### ↳ ↳ ↳ Cobol calls to APIs vs pre compiler translations

- **From:** Howard Brazee <brazee@NOSPAMhome.com>
- **Date:** 1999-10-29T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<38199F77.62FFA9B7@NOSPAMhome.com>`
- **References:** `<7v96cn$que$1@wanadoo.fr> <3818875A.6BFDB19B@home.com> <7vanmq$qli$1@nntp3.atl.mindspring.net>`

```
Ken Mullins wrote:
> 
> Not to change the subject here, but Jimmy, isn't that an aweful lot of
> invokes (calls) to do a simple messagebox...???...I have heard about
> overhead in oo, but man, I would die just typing all that in...  :-))

I prefer pre-compilers when COBOL starts calling DLLs & C routines. 
There is a huge advantage of COBOL over most Windows languages and REXX
(REXX has native REXX commands, but does a lot of calls to its
environment which are NOT in REXX) in that the commands are in English. 
As soon as it switches to calls in another language's syntax, it is no
longer speaking COBOL/English, but is speaking APIs, TCP/IP, behind the
scene Windows, etc.

A pre-compiler should be able to take syntax which looks like
COBOL/English and then convert it to the calls necessary to make it work
in the proper environment.

Don't throw away the strengths of COBOL to fit it into the Windows
environment - but adapt its strengths instead.
```

##### ↳ ↳ Re: C-like strings in MicroFocus COBOL ?

- **From:** "William M. Klein" <wmklein@nospam.netcom.com>
- **Date:** 1999-11-03T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7vqqeg$7cf$1@nntp2.atl.mindspring.net>`
- **References:** `<7v96cn$que$1@wanadoo.fr> <3818875A.6BFDB19B@home.com>`

```
Z-literals were introduced by IBM (on the mainframe) and seem to be making
their way thru various vendors (as extensions).  It was REJECTED (and don't
ask me why) for inclusion in the next COBOL Standard.
```

###### ↳ ↳ ↳ Re: C-like strings in MicroFocus COBOL ?

- **From:** "Russell Styles" <RWSTYLES@COMPUSERVE.COM>
- **Date:** 1999-11-04T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7vs6n9$r5j$1@ssauraaa-i-1.production.compuserve.com>`
- **References:** `<7v96cn$que$1@wanadoo.fr> <3818875A.6BFDB19B@home.com> <7vqqeg$7cf$1@nntp2.atl.mindspring.net>`

```
    Judging from things like this, and other aspects of the upcoming new
standard, the J4 committee sounds like they are collectively a bunch of
indecisive pinheads.  Since I suspect that they are individually very bright
people, what gives.  Some of the decisions, not to mention nondecisions
sound very odd.  Why bother expanding data name length from 30 to 31.  Why
reject z-literals. Why doesn't initialize respect occurs depending on.

    You could probably come up with 100's of even better questions with your
background.




William M. Klein <wmklein@nospam.netcom.com> wrote in message
news:7vqqeg$7cf$1@nntp2.atl.mindspring.net...
> Z-literals were introduced by IBM (on the mainframe) and seem to be making
> their way thru various vendors (as extensions).  It was REJECTED (and
don't
> ask me why) for inclusion in the next COBOL Standard.
>
> --
> Bill Klein
>     wmklein <at> ix dot netcom dot com
```

###### ↳ ↳ ↳ Re: C-like strings in MicroFocus COBOL ?

_(reply depth: 4)_

- **From:** "James J. Gavan" <jjgavan@home.com>
- **Date:** 1999-11-04T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3821DFF6.D082C509@home.com>`
- **References:** `<7v96cn$que$1@wanadoo.fr> <3818875A.6BFDB19B@home.com> <7vqqeg$7cf$1@nntp2.atl.mindspring.net> <7vs6n9$r5j$1@ssauraaa-i-1.production.compuserve.com>`

```


Russell Styles wrote:
> 
>     Judging from things like this, and other aspects of the upcoming new
…[18 more quoted lines elided]…
> >     wmklein <at> ix dot netcom dot com

Ditto Russell. Bill, Don(J4) can expect a further message from me! And
suggest you do the same Russell.

Jimmy, Calgary AB
```

###### ↳ ↳ ↳ Re: C-like strings in MicroFocus COBOL ?

_(reply depth: 4)_

- **From:** "William M. Klein" <wmklein@nospam.netcom.com>
- **Date:** 1999-11-04T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7vsiqo$dfo$1@nntp6.atl.mindspring.net>`
- **References:** `<7v96cn$que$1@wanadoo.fr> <3818875A.6BFDB19B@home.com> <7vqqeg$7cf$1@nntp2.atl.mindspring.net> <7vs6n9$r5j$1@ssauraaa-i-1.production.compuserve.com>`

```
INITIALIZE with OCCURS items *is* in the draft of the next Standard.

The next Standard does also include "concatenation" expressions, (along with
hex-literals) so you can say

  MOVE 'ABC' & X'00' to C-string-place.

You can also say

  Move 'ABC' to Some-field
  Move X'00' to Some-field (4:1)

I am not saying that having z-literals wouldn't have been useful, but they
are needed LESS with other enhancements that have already been included in
the draft Standard.  (and obviously, I am *NOT* the person who should be
defending their general decision-making abilities - but I did want to clarify
those specific examples.)
```

#### ↳ Re: C-like strings in MicroFocus COBOL ?

- **From:** "Judson McClendon" <judmc123@bellsouth.net>
- **Date:** 1999-10-28T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<zR%R3.7558$l22.58062@news1.mia>`
- **References:** `<7v96cn$que$1@wanadoo.fr>`

```
Jacques Vidal wrote:
>
>I've been told there's a way (compiler directive or another) to have
…[10 more quoted lines elided]…
>Is all this true or legend?

From the NetExpress 3.0 *online* documentation:

  A null-terminated string can be created by specifying Z"string" and
  can be used anywhere a nonnumeric literal is permitted. The resultant
  literal is equivalent to concatenating X"00" (a null byte) to the end
  of the specified string. In other words, the two following lines are
  equivalent:

  MOVE Z"my-literal" TO an-item
  MOVE "my-literal" & X"00" TO an-item

  In the following example, the PICTURE declaration has an extra byte
  for the zero-byte:

  01 my-name PIC X(5) VALUE Z"Jane".

I could find no trace of this in the printed documentation.
```

##### ↳ ↳ Re: C-like strings in MicroFocus COBOL ?

- **From:** "James J. Gavan" <jjgavan@home.com>
- **Date:** 1999-10-28T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<38189146.380FFFAD@home.com>`
- **References:** `<7v96cn$que$1@wanadoo.fr> <zR%R3.7558$l22.58062@news1.mia>`

```


Judson McClendon wrote:
> 
> Jacques Vidal wrote:
…[29 more quoted lines elided]…
> 

Well I'll be damned ! Judson, point me to the proper part of the on-line
index <G>

Jimmy
```

###### ↳ ↳ ↳ Re: C-like strings in MicroFocus COBOL ?

- **From:** "Judson McClendon" <judmc123@bellsouth.net>
- **Date:** 1999-10-28T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<mX1S3.7782$qy6.96677@news2.mia>`
- **References:** `<7v96cn$que$1@wanadoo.fr> <zR%R3.7558$l22.58062@news1.mia> <38189146.380FFFAD@home.com>`

```
James J. Gavan wrote:
>
>Judson, point me to the proper part of the on-line index <G>

It is under 'Literals'.  I found it by clicking Help, Help Topics,
Find tab, and keying 'null'.  In the list was 'null-terminated',
and when that was selected, one of the topics was 'Literals'.
```

###### ↳ ↳ ↳ Re: C-like strings in MicroFocus COBOL ?

_(reply depth: 4)_

- **From:** "James J. Gavan" <jjgavan@home.com>
- **Date:** 1999-10-28T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3818B468.5E82E037@home.com>`
- **References:** `<7v96cn$que$1@wanadoo.fr> <zR%R3.7558$l22.58062@news1.mia> <38189146.380FFFAD@home.com> <mX1S3.7782$qy6.96677@news2.mia>`

```


Judson McClendon wrote:
> 
> James J. Gavan wrote:
…[5 more quoted lines elided]…
> and when that was selected, one of the topics was 'Literals'.

Many thanks for the info - now I feel much happier. I was looking
originally in Visoc for z"....  AND.... just in case you are a
teensy-weensy bit interested in OO <G> from the Windows runtime-box
enter the following to get at the OO Classes syntax :-

	\NetExpress\Base\Bin\mfnxcl30.chm

Jimmy
```

##### ↳ ↳ Re: C-like strings in MicroFocus COBOL ?

- **From:** "Rick Smith" <ricksmith@aiservices.com>
- **Date:** 1999-10-28T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7v9ou5$20os$1@news.hitter.net>`
- **References:** `<7v96cn$que$1@wanadoo.fr> <zR%R3.7558$l22.58062@news1.mia>`

```

Judson McClendon wrote in message ...
[...]
>From the NetExpress 3.0 *online* documentation:
[...]
This is the first time you mentioned having NetExpress.

Upgrade from MF WB 3.2?

Decided to replace character screens with GUI?
If so, which interface?

Decided to get into OO?

Inquiring minds want to know?
------------------
Rick Smith
```

###### ↳ ↳ ↳ Re: C-like strings in MicroFocus COBOL ?

- **From:** "James J. Gavan" <jjgavan@home.com>
- **Date:** 1999-10-28T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3818A340.6F7883FD@home.com>`
- **References:** `<7v96cn$que$1@wanadoo.fr> <zR%R3.7558$l22.58062@news1.mia> <7v9ou5$20os$1@news.hitter.net>`

```


Rick Smith wrote:
> 
> Judson McClendon wrote in message ...
…[12 more quoted lines elided]…
> Inquiring minds want to know?

Strangely I had the same thought. I thought he had DT branded on his
forehead like you <G>

Jimmy
```

###### ↳ ↳ ↳ Re: C-like strings in MicroFocus COBOL ?

_(reply depth: 4)_

- **From:** "Judson McClendon" <judmc123@bellsouth.net>
- **Date:** 1999-10-28T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<U32S3.7793$qy6.97131@news2.mia>`
- **References:** `<7v96cn$que$1@wanadoo.fr> <zR%R3.7558$l22.58062@news1.mia> <7v9ou5$20os$1@news.hitter.net> <3818A340.6F7883FD@home.com>`

```
James J. Gavan wrote:
>
>Strangely I had the same thought. I thought he had DT branded on his
>forehead like you <G>

What's 'DT'?
```

###### ↳ ↳ ↳ Re: C-like strings in MicroFocus COBOL ?

_(reply depth: 5)_

- **From:** "James J. Gavan" <jjgavan@home.com>
- **Date:** 1999-10-28T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3818B571.E919CAE9@home.com>`
- **References:** `<7v96cn$que$1@wanadoo.fr> <zR%R3.7558$l22.58062@news1.mia> <7v9ou5$20os$1@news.hitter.net> <3818A340.6F7883FD@home.com> <U32S3.7793$qy6.97131@news2.mia>`

```


Judson McClendon wrote:
> 
> James J. Gavan wrote:
…[4 more quoted lines elided]…
> What's 'DT'?

Let's turn it into a quiz. One of the twelve - I think you use the
phrase down there, "Show me. I'm from Missouri".<G>

Jimmy
```

###### ↳ ↳ ↳ Re: C-like strings in MicroFocus COBOL ?

_(reply depth: 6)_

- **From:** thaneH@softwaresimple.com (Thane Hubbell)
- **Date:** 1999-10-29T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3819190d.122616785@news1.attglobal.net>`
- **References:** `<7v96cn$que$1@wanadoo.fr> <zR%R3.7558$l22.58062@news1.mia> <7v9ou5$20os$1@news.hitter.net> <3818A340.6F7883FD@home.com> <U32S3.7793$qy6.97131@news2.mia> <3818B571.E919CAE9@home.com>`

```
On Thu, 28 Oct 1999 20:34:58 GMT, "James J. Gavan" <jjgavan@home.com>
wrote:

>
>
…[10 more quoted lines elided]…
>phrase down there, "Show me. I'm from Missouri".<G>

Dumb Terminal (text mode interface)?

---
Try a better search engine:  http://www.google.com
My personal web site: http://www.geocities.com/Eureka/2006/
```

###### ↳ ↳ ↳ Re: C-like strings in MicroFocus COBOL ?

- **From:** "Judson McClendon" <judmc123@bellsouth.net>
- **Date:** 1999-10-28T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<R22S3.7790$qy6.97069@news2.mia>`
- **References:** `<7v96cn$que$1@wanadoo.fr> <zR%R3.7558$l22.58062@news1.mia> <7v9ou5$20os$1@news.hitter.net>`

```
Rick Smith wrote:
>
>This is the first time you mentioned having NetExpress.

I just received it last week and installed it on Saturday. :-)
>
>Upgrade from MF WB 3.2?

Actually, COBOL 3.2, I didn't have WorkBench.

>Decided to replace character screens with GUI?

Actually, more replace 16 bit by 32 bit, and have GUI available.

>If so, which interface?

I'm still pondering that.  How about some input? :-)  One
question I have right now is: How do I change the size of the
'screen' on a character based app from 80x25, when using Panels
and when not using Panels?  I understand that if I use Panels,
I can create character and/or GUI interfaces for the same app.

>Decided to get into OO?

Eventually.  I also upgraded to Fujitsu 4.2 (from 4.0) at the same
time (so I will get 5.0 free when it comes out).  I have some new
development pending, and I wanted to evaluate both compilers to see
which would be better.
```

###### ↳ ↳ ↳ Re: C-like strings in MicroFocus COBOL ?

_(reply depth: 4)_

- **From:** "James J. Gavan" <jjgavan@home.com>
- **Date:** 1999-10-28T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3818BA12.1890AF18@home.com>`
- **References:** `<7v96cn$que$1@wanadoo.fr> <zR%R3.7558$l22.58062@news1.mia> <7v9ou5$20os$1@news.hitter.net> <R22S3.7790$qy6.97069@news2.mia>`

```


Judson McClendon wrote:
> 
> Rick Smith wrote:
…[15 more quoted lines elided]…
> I'm still pondering that.  How about some input? :-) 

> >Decided to get into OO?
> 
…[3 more quoted lines elided]…
> which would be better.

On behalf of Pete Dashwood I've been taking a look at the Fujitsu manual
regarding OO; so I'm near to writing to him and Donald Tees, and I did
want to make minor comments to Rick's message about OO under thread
"Screens". I'm looking at Fujitsu and NetExpress, comparing the two
current approaches, not vying for one or the other. If useful, I could
post it here ? (If so, I'll post under OO Methodology).

Sorry can't help you on Panels - I only had the bare-bones V 3.?, only
used Screen Section and then jumped straight into Visoc/NetExpress.

Jimmy
```

#### ↳ Re: C-like strings in MicroFocus COBOL ?

- **From:** "Gael Wilson" <gael.wilson@merant.com>
- **Date:** 1999-10-28T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7v9j3g$5h6$1@hyperion.mfltd.co.uk>`
- **References:** `<7v96cn$que$1@wanadoo.fr>`

```
Jacques,

It is definitely true and, who knows, in years to come it may develop into a
legend ! The way to do it is to MOVE z"string" TO pic x(n).

Jacques Vidal wrote in message <7v96cn$que$1@wanadoo.fr>...
>Hi,
>
…[17 more quoted lines elided]…
>
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
