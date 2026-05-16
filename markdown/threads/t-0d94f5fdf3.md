[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# "invalid" source code (END-IF, Next Sentence, and missing periods)

_31 messages · 11 participants · 2001-07_

**Topics:** [`Language features and syntax`](../topics.md#syntax)

---

### Re: "invalid" source code (END-IF, Next Sentence, and missing periods)

- **From:** Richard Plinston <riplin@Azonic.co.nz>
- **Date:** 2001-07-06T09:37:22+01:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3B4578C2.97E83781@Azonic.co.nz>`
- **References:** `<9fjsu2$4c0$1@slb0.atl.mindspring.net> <9fllv7$5ko$1@news.netmar.com> <3B2521F3.3FFAE797@Azonic.co.nz> <CNw07.2515$xp1.250458@newsread1.prod.itd.earthlink.net> <76I07.206$_93.29600957@newssvr15.news.prodigy.com>`

```
Terry Heinze wrote:
> 
> For those of you who haven't been bitten by EXIT PROGRAM yet,
> be aware that it functions as a GOBACK in a called program, but as a
> CONTINUE for a main program (one that was not called by another program).
> This has serious implications.  :)

GOBACK is an IBM-ism and is not standard Cobol until the next one,
whenever, or if, that occurs.

I always know whether the program I am writing is to be CALLed or
whether it is a main program (and not CALLed) and thus whether to add an
EXIT PROGRAM or STOP RUN.  This is because CALLed programs have LINKAGE
SECTION and main programs do not.

It seems to be another IBM-ism that main programs can have a LINKAGE and
thus may be executed as a main or be called.

In some systems, such as Fujitsu, there can be no mistaking which is the
main, it must be marked as such and cannot be called by another. 
Similarly if the program is not marked as main then it cannot be
executed without being called.

However I usually have in CALLed programs:

            EXIT PROGRAM
            STOP RUN
            .

even if this does conflict with some minor rules that wants to impose
additional paragraph labels and even if the STOP RUN will never be
reached because the program would fail to start if executed as if it
were a main.
```

#### ↳ Re: "invalid" source code (END-IF, Next Sentence, and missing periods)

- **From:** "Terry Heinze" <terryheinze@prodigy.net>
- **Date:** 2001-07-05T21:52:17-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<9i397i$a1js$1@newssvr06-en0.news.prodigy.com>`
- **References:** `<9fjsu2$4c0$1@slb0.atl.mindspring.net> <9fllv7$5ko$1@news.netmar.com> <3B2521F3.3FFAE797@Azonic.co.nz> <CNw07.2515$xp1.250458@newsread1.prod.itd.earthlink.net> <76I07.206$_93.29600957@newssvr15.news.prodigy.com> <3B4578C2.97E83781@Azonic.co.nz>`

```
Main programs that have PARM parameters defined DO have LINKAGE SECTIONs.
```

#### ↳ Re: "invalid" source code (END-IF, Next Sentence, and missing periods)

- **From:** Richard Plinston <riplin@Azonic.co.nz>
- **Date:** 2001-07-06T09:55:21+01:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3B457CF9.98E86EFD@Azonic.co.nz>`
- **References:** `<9fjsu2$4c0$1@slb0.atl.mindspring.net> <9fllv7$5ko$1@news.netmar.com> <3B2521F3.3FFAE797@Azonic.co.nz> <CNw07.2515$xp1.250458@newsread1.prod.itd.earthlink.net> <76I07.206$_93.29600957@newssvr15.news.prodigy.com> <3B4578C2.97E83781@Azonic.co.nz>`

```
> I use 'exit.' as my last line in every paragraph.  No other lines in my
> paragraphs are terminated by a period (full stop).  I could, of course, use just
> '.' on a blank line, but I find that hard to read.

Some seem to use CONTINUE. as the last line to highlight the full stop. 
Both of these may confuse the next programmer at 2am.  At least your
exit is true in the sense that each paragraph is performed and so,
logically, it will exit back to the perform.  If you were amending a
program in the 'perform section and goto exit' would you use 'continue.'
at the point it will drop through into the exit paragraph ?

I use a text editor that highlights full stops (except in comments) with
a red block, it works for me.
```

##### ↳ ↳ Re: "invalid" source code (END-IF, Next Sentence, and missing periods)

- **From:** Frank Swarbrick <infocat@sprynet.com>
- **Date:** 2001-07-06T18:47:41-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<9nmcktkdsf0rlmnqm1m178m75tlstto9ub@4ax.com>`
- **References:** `<9fjsu2$4c0$1@slb0.atl.mindspring.net> <9fllv7$5ko$1@news.netmar.com> <3B2521F3.3FFAE797@Azonic.co.nz> <CNw07.2515$xp1.250458@newsread1.prod.itd.earthlink.net> <76I07.206$_93.29600957@newssvr15.news.prodigy.com> <3B4578C2.97E83781@Azonic.co.nz> <3B457CF9.98E86EFD@Azonic.co.nz>`

```
On Fri, 06 Jul 2001 09:55:21 +0100, Richard Plinston <riplin@Azonic.co.nz>
wrote:

>> I use 'exit.' as my last line in every paragraph.  No other lines in my
>> paragraphs are terminated by a period (full stop).  I could, of course, use just
…[7 more quoted lines elided]…
>at the point it will drop through into the exit paragraph ?

Yes, actually.  I have written programs that use SECTIONs because I want to use
GO TO.  They look something like this:

1000-mainline section.
    if something
        go to 1000-exit
    end-if
    perform 1100-something-else
    continue.

1000-exit.
    exit.

Kind of funky, but I don't see why it wouldn't be concidered perfectly readable.

>I use a text editor that highlights full stops (except in comments) with
>a red block, it works for me.

Now wouldn't that be nice.  :-)
Frank Swarbrick
home: infocat@sprynet.com / work: frank.swarbrick@efirstbank.com
"I'm very seldom naughty." --Willow Rosenberg "Buffy the Vampire Slayer"
```

###### ↳ ↳ ↳ Re: "invalid" source code (END-IF, Next Sentence, and missing periods)

- **From:** "Robert M. Pritchett - RMP Consulting Partners LLC" <Sending-Email-To-This-Address-Constitutes-A-Promise-To-Send-One-Thousand-Dollars-To-RMPCP@rmpcp.com?Subject=I-Am-A-Spammer-So-I-Promise-To-Send-One-Thousand-Dollars-To-RMPCP-For-Each-Message>
- **Date:** 2001-07-07T04:23:09+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<N8w17.7021$G_1.698881@newsread2.prod.itd.earthlink.net>`
- **References:** `<9fjsu2$4c0$1@slb0.atl.mindspring.net> <9fllv7$5ko$1@news.netmar.com> <3B2521F3.3FFAE797@Azonic.co.nz> <CNw07.2515$xp1.250458@newsread1.prod.itd.earthlink.net> <76I07.206$_93.29600957@newssvr15.news.prodigy.com> <3B4578C2.97E83781@Azonic.co.nz> <3B457CF9.98E86EFD@Azonic.co.nz> <9nmcktkdsf0rlmnqm1m178m75tlstto9ub@4ax.com>`

```
Much easier to read by just saying what you want in the first place:

1000-mainline section.
    if not something
        perform 1100-something-else
    end-if
    .

Use of GoTo's in writing new code shows that the programmer still hasn't
learned to think structured and hasn't learned to think clearly, imho.
```

###### ↳ ↳ ↳ Re: "invalid" source code (END-IF, Next Sentence, and missing periods)

_(reply depth: 4)_

- **From:** Frank Swarbrick <infocat@sprynet.com>
- **Date:** 2001-07-07T21:35:37-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<q2lfktkbecg5puorhs8olhd12n7t3vndpq@4ax.com>`
- **References:** `<9fjsu2$4c0$1@slb0.atl.mindspring.net> <9fllv7$5ko$1@news.netmar.com> <3B2521F3.3FFAE797@Azonic.co.nz> <CNw07.2515$xp1.250458@newsread1.prod.itd.earthlink.net> <76I07.206$_93.29600957@newssvr15.news.prodigy.com> <3B4578C2.97E83781@Azonic.co.nz> <3B457CF9.98E86EFD@Azonic.co.nz> <9nmcktkdsf0rlmnqm1m178m75tlstto9ub@4ax.com> <N8w17.7021$G_1.698881@newsread2.prod.itd.earthlink.net>`

```
On Sat, 07 Jul 2001 04:23:09 GMT, "Robert M. Pritchett - RMP Consulting Partners
LLC"
<Sending-Email-To-This-Address-Constitutes-A-Promise-To-Send-One-Thousand-Dollars-To-RMPCP@rmpcp.com?Subject=I-Am-A-Spammer-So-I-Promise-To-Send-One-Thousand-Dollars-To-RMPCP-For-Each-Message>
wrote:

>Much easier to read by just saying what you want in the first place:
>
…[7 more quoted lines elided]…
>learned to think structured and hasn't learned to think clearly, imho.

Oh bollocks (however you spell it).

1000-mainline.
     if something
         exit paragraph
     end-if
***  do "something else" here
     .

Is no less structured than what you posted above.  And it saves me from having a
fairly pointless paragraph of only three lines.

Frank Swarbrick
home: infocat@sprynet.com / work: frank.swarbrick@efirstbank.com
"I'm very seldom naughty." --Willow Rosenberg "Buffy the Vampire Slayer"
```

###### ↳ ↳ ↳ Re: "invalid" source code (END-IF, Next Sentence, and missing periods)

_(reply depth: 5)_

- **From:** "Robert M. Pritchett - RMP Consulting Partners LLC" <Sending-Email-To-This-Address-Constitutes-A-Promise-To-Send-One-Thousand-Dollars-To-RMPCP@rmpcp.com?Subject=I-Am-A-Spammer-So-I-Promise-To-Send-One-Thousand-Dollars-To-RMPCP-For-Each-Message>
- **Date:** 2001-07-10T00:56:34+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<6ps27.2327$767.269976@newsread2.prod.itd.earthlink.net>`
- **References:** `<9fjsu2$4c0$1@slb0.atl.mindspring.net> <9fllv7$5ko$1@news.netmar.com> <3B2521F3.3FFAE797@Azonic.co.nz> <CNw07.2515$xp1.250458@newsread1.prod.itd.earthlink.net> <76I07.206$_93.29600957@newssvr15.news.prodigy.com> <3B4578C2.97E83781@Azonic.co.nz> <3B457CF9.98E86EFD@Azonic.co.nz> <9nmcktkdsf0rlmnqm1m178m75tlstto9ub@4ax.com> <N8w17.7021$G_1.698881@newsread2.prod.itd.earthlink.net> <q2lfktkbecg5puorhs8olhd12n7t3vndpq@4ax.com>`

```
Then the right way to handle that, and much simpler and more structured,
is

1000-mainline section.
    if not something
        *** DO YOUR SOMETHING ELSE RIGHT HERE ***
    end-if
    .

Adding unnecessary exits, else cases, etc. only clutters up the logic. The
above is much easier to read and more straightforward. Stuff like exit
paragraph is usually just a crutch, not as bad as a goto but still shows
lack of fully structured (e.g. clear) thinking. It could be a useful
transitional tool for maintenance but is generally inappropriate for new
code.
```

###### ↳ ↳ ↳ Re: "invalid" source code (END-IF, Next Sentence, and missing periods)

_(reply depth: 6)_

- **From:** Frank Swarbrick <infocat@sprynet.com>
- **Date:** 2001-07-09T23:35:39-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3B4A942B.82F13F8E@sprynet.com>`
- **References:** `<9fjsu2$4c0$1@slb0.atl.mindspring.net> <9fllv7$5ko$1@news.netmar.com> <3B2521F3.3FFAE797@Azonic.co.nz> <CNw07.2515$xp1.250458@newsread1.prod.itd.earthlink.net> <76I07.206$_93.29600957@newssvr15.news.prodigy.com> <3B4578C2.97E83781@Azonic.co.nz> <3B457CF9.98E86EFD@Azonic.co.nz> <9nmcktkdsf0rlmnqm1m178m75tlstto9ub@4ax.com> <N8w17.7021$G_1.698881@newsread2.prod.itd.earthlink.net> <q2lfktkbecg5puorhs8olhd12n7t3vndpq@4ax.com> <6ps27.2327$767.269976@newsread2.prod.itd.earthlink.net>`

```
Could do that of course, but I find it rather silly to have an entire
paragraph inside an IF statement.

Frank

"Robert M. Pritchett - RMP Consulting Partners LLC" wrote:
> 
> Then the right way to handle that, and much simpler and more structured,
…[32 more quoted lines elided]…
> fairly pointless paragraph of only three lines.
```

###### ↳ ↳ ↳ Re: "invalid" source code (END-IF, Next Sentence, and missing periods)

_(reply depth: 6)_

- **From:** Howard Brazee <howard.brazee@cusys.edu>
- **Date:** 2001-07-19T12:27:26-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3B57268E.E38CC0FC@cusys.edu>`
- **References:** `<9fjsu2$4c0$1@slb0.atl.mindspring.net> <9fllv7$5ko$1@news.netmar.com> <3B2521F3.3FFAE797@Azonic.co.nz> <CNw07.2515$xp1.250458@newsread1.prod.itd.earthlink.net> <76I07.206$_93.29600957@newssvr15.news.prodigy.com> <3B4578C2.97E83781@Azonic.co.nz> <3B457CF9.98E86EFD@Azonic.co.nz> <9nmcktkdsf0rlmnqm1m178m75tlstto9ub@4ax.com> <N8w17.7021$G_1.698881@newsread2.prod.itd.earthlink.net> <q2lfktkbecg5puorhs8olhd12n7t3vndpq@4ax.com> <6ps27.2327$767.269976@newsread2.prod.itd.earthlink.net>`

```


"Robert M. Pritchett - RMP Consulting Partners LLC" wrote:

> Then the right way to handle that, and much simpler and more structured,
> is
…[12 more quoted lines elided]…
> code.

Where EXIT-PARAGRAPH will shine is when you want to do as little touching of
existing code as possible in a maintenance request.

Of course, an even bigger advantage will be that we have a better argument
towards convincing our companies' standards boards to disallow exit paragraphs
in new programs!
```

###### ↳ ↳ ↳ Re: "invalid" source code (END-IF, Next Sentence, and missing periods)

_(reply depth: 4)_

- **From:** Frank Swarbrick <infocat@sprynet.com>
- **Date:** 2001-07-07T21:47:23-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1blfkts8mkb6m9ojpedvv1h1h1n1bq9888@4ax.com>`
- **References:** `<9fjsu2$4c0$1@slb0.atl.mindspring.net> <9fllv7$5ko$1@news.netmar.com> <3B2521F3.3FFAE797@Azonic.co.nz> <CNw07.2515$xp1.250458@newsread1.prod.itd.earthlink.net> <76I07.206$_93.29600957@newssvr15.news.prodigy.com> <3B4578C2.97E83781@Azonic.co.nz> <3B457CF9.98E86EFD@Azonic.co.nz> <9nmcktkdsf0rlmnqm1m178m75tlstto9ub@4ax.com> <N8w17.7021$G_1.698881@newsread2.prod.itd.earthlink.net>`

```
On Sat, 07 Jul 2001 04:23:09 GMT, "Robert M. Pritchett - RMP Consulting Partners
LLC"
<Sending-Email-To-This-Address-Constitutes-A-Promise-To-Send-One-Thousand-Dollars-To-RMPCP@rmpcp.com?Subject=I-Am-A-Spammer-So-I-Promise-To-Send-One-Thousand-Dollars-To-RMPCP-For-Each-Message>
wrote:

>Much easier to read by just saying what you want in the first place:
>
…[7 more quoted lines elided]…
>learned to think structured and hasn't learned to think clearly, imho.

In addition to my previous reply I also want to add this.  Take the following
code:

1000-validate-fields.
    perform validate-field-1
    if valid
        perform validate-field-2
    end-if
    if valid
        perform validate-field-3
    end-if
    if valid
        perform validate-field-4
    end-if
    if valid
        perform validate-field-5
    end-if
    if valid
        perform validate-field-6
    end-if
    .

Is this really better than:

1000-validate-fields.
    perform validate-field-1.
    if not valid
        exit paragraph
    end-if
    perform validate-field-2
    if not valid
        exit paragraph
    end-if
    perform validate-field-3
    if not valid
        exit paragraph
    end-if
    perform validate-field-4
    if not valid
        exit paragraph
    end-if
    perform validate-field-5
    if not valid
        exit paragraph
    end-if
    perform validate-field-6
    .

First, let me state that *yes*, I do *not* want to validate fields 2 - 6 if
field 1 is invalid (etc.).  With the CICS programs I write there's usually only
room for only one error message, so we simply stop validation once we find a
single invalid field.

That said, with method 1 we are checking the status of 'valid' several extra
times unnecessarily.

To be honest, this would be *most* efficient using either a SECTION or a PERFORM
THRU and having all the validation code inline with drop down paragraphs and a
GO TO 1000-EXIT once a field is found to be invalid.  But that's definitely not
something I'll be condoning as it very often does lead to spaghetti code.

Frank Swarbrick
home: infocat@sprynet.com / work: frank.swarbrick@efirstbank.com
"I'm very seldom naughty." --Willow Rosenberg "Buffy the Vampire Slayer"
```

###### ↳ ↳ ↳ Re: "invalid" source code (END-IF, Next Sentence, and missing periods)

_(reply depth: 5)_

- **From:** stephenjspiro@hotmail.com (Stephen J Spiro)
- **Date:** 2001-07-08T16:28:38-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<4145699b.0107081528.702dc31e@posting.google.com>`
- **References:** `<9fjsu2$4c0$1@slb0.atl.mindspring.net> <9fllv7$5ko$1@news.netmar.com> <3B2521F3.3FFAE797@Azonic.co.nz> <CNw07.2515$xp1.250458@newsread1.prod.itd.earthlink.net> <76I07.206$_93.29600957@newssvr15.news.prodigy.com> <3B4578C2.97E83781@Azonic.co.nz> <3B457CF9.98E86EFD@Azonic.co.nz> <9nmcktkdsf0rlmnqm1m178m75tlstto9ub@4ax.com> <N8w17.7021$G_1.698881@newsread2.prod.itd.earthlink.net> <1blfkts8mkb6m9ojpedvv1h1h1n1bq9888@4ax.com>`

```
Comments at bottom.....



Frank Swarbrick <infocat@sprynet.com> wrote in message news:<1blfkts8mkb6m9ojpedvv1h1h1n1bq9888@4ax.com>...
> On Sat, 07 Jul 2001 04:23:09 GMT, "Robert M. Pritchett - RMP Consulting Partners
> LLC"
…[77 more quoted lines elided]…
> "I'm very seldom naughty." --Willow Rosenberg "Buffy the Vampire Slayer"

*----------------

Today, you are naughty!  You set up an example that NO practitioner of
"structured, modularized" programming would code, and then say it is
no better than your own example.

Problem 1: Using the same condition name ("valid") for a whole bunch
of conditions. (If you were using "valid" as meta-code, not as a field
name, I
apologise.)

Problem 2: Even so, we would code it so your stated objections would
not exist (altho you may have OTHER criticisms of my example! <G>)
Here is how I would code it...

 1000-validate-fields.
     perform validate-field-1
     if field-1-valid
         perform validate-field-2 
         if field-2-valid
             perform validate-field-3
             if field-3-valid
                 perform validate-field-4
                 if field-4-valid
                     perform validate-field-5
                     if field-5-valid
                         perform validate-field-6                    
                     end-if
                 end-if
             end-if
         end-if
     end-if.

If any validation fails, none of the remaining tests are made.  EXIT
PERFORM, EXIT PARAGRAPH and EXIT SECTION are NEVER necessary, THEY are
GOTO's and the appropriate logic can always be coded using standard,
modular techniques.

I will confess I am unhappy about the 5 END-IF's in a row.  If the
code in the IF statements were more complex, I might think about
putting the innermost tests in a separate, performed paragraph. (That
would be safe and easy, the way I have coded it here.)  But this is
small enough to be immediately comprehensible.


Stephen J Spiro
President, Wizard Systems
```

###### ↳ ↳ ↳ Re: "invalid" source code (END-IF, Next Sentence, and missing periods)

_(reply depth: 6)_

- **From:** Frank Swarbrick <infocat@sprynet.com>
- **Date:** 2001-07-08T21:15:24-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<su7ikto7mj9be31765hhhodldvgvdpc39o@4ax.com>`
- **References:** `<9fjsu2$4c0$1@slb0.atl.mindspring.net> <9fllv7$5ko$1@news.netmar.com> <3B2521F3.3FFAE797@Azonic.co.nz> <CNw07.2515$xp1.250458@newsread1.prod.itd.earthlink.net> <76I07.206$_93.29600957@newssvr15.news.prodigy.com> <3B4578C2.97E83781@Azonic.co.nz> <3B457CF9.98E86EFD@Azonic.co.nz> <9nmcktkdsf0rlmnqm1m178m75tlstto9ub@4ax.com> <N8w17.7021$G_1.698881@newsread2.prod.itd.earthlink.net> <1blfkts8mkb6m9ojpedvv1h1h1n1bq9888@4ax.com> <4145699b.0107081528.702dc31e@posting.google.com>`

```
On 8 Jul 2001 16:28:38 -0700, stephenjspiro@hotmail.com (Stephen J Spiro) wrote:

>Comments at bottom.....
>
…[93 more quoted lines elided]…
>apologise.)

Actually, in this case I *would* use the same condition name "VALID".  But
within each validation paragraph I would set a specific error message.  In other
words:

validate-field-1.
    if field-1 numeric
    and field-1 > 0 and field-1 < 10
        set valid to true
    else
        set invalid to true
        move 'field 1 must from 1 - 9' to error-message
    end-if
    exit.


>Problem 2: Even so, we would code it so your stated objections would
>not exist (altho you may have OTHER criticisms of my example! <G>)
…[29 more quoted lines elided]…
>small enough to be immediately comprehensible.

Is that right?  I concidered your approach, and threw it out.  What if there are
30 fields to validate?  Can you honesty say you would continue your code as show
above?  Or perhaps you'd do 6 paragraphs, each containing 5 checks each?  I
think that would just add confusion.

I'm honestly curious to see how people would do this kind of thing, while
avoiding goto's, exit paragraph, etc.

Frank Swarbrick
home: infocat@sprynet.com / work: frank.swarbrick@efirstbank.com
"I'm very seldom naughty." --Willow Rosenberg "Buffy the Vampire Slayer"
```

###### ↳ ↳ ↳ Re: "invalid" source code (END-IF, Next Sentence, and missing periods)

_(reply depth: 7)_

- **From:** stephenjspiro@hotmail.com (Stephen J Spiro)
- **Date:** 2001-07-09T05:03:53-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<4145699b.0107090403.4353bf30@posting.google.com>`
- **References:** `<9fjsu2$4c0$1@slb0.atl.mindspring.net> <3B2521F3.3FFAE797@Azonic.co.nz> <CNw07.2515$xp1.250458@newsread1.prod.itd.earthlink.net> <76I07.206$_93.29600957@newssvr15.news.prodigy.com> <3B4578C2.97E83781@Azonic.co.nz> <3B457CF9.98E86EFD@Azonic.co.nz> <9nmcktkdsf0rlmnqm1m178m75tlstto9ub@4ax.com> <N8w17.7021$G_1.698881@newsread2.prod.itd.earthlink.net> <1blfkts8mkb6m9ojpedvv1h1h1n1bq9888@4ax.com> <4145699b.0107081528.702dc31e@posting.google.com> <su7ikto7mj9be31765hhhodldvgvdpc39o@4ax.com>`

```
Frank Swarbrick <infocat@sprynet.com> wrote 
<snip>
 
> >Problem 2: Even so, we would code it so your stated objections would
> >not exist (altho you may have OTHER criticisms of my example! <G>)
…[39 more quoted lines elided]…
> Frank Swarbrick

*-------------------------

Some logic just does not code "prettily"! Yeah, I'd probably code 6
paragraphs.  Confusion is very often a matter of what one is
accustomed to.  When I first was exposed to "structured, modular"
programming, I found it confusing; now I get frustrated if the code is
NOT that way.  The bottom line for why I use it is that I find that
one is less likely to get in trouble doing maintenance. (Incidentally,
the END-IFs were all superfluous in my example; it would have LOOKED
cleaner without them --- but I have them there with an eye to future
maintenance.)

Stephen J Spiro
```

###### ↳ ↳ ↳ Re: "invalid" source code (END-IF, Next Sentence, and missing periods)

_(reply depth: 8)_

- **From:** Frank Swarbrick <infocat@sprynet.com>
- **Date:** 2001-07-09T18:53:59-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3B4A5227.A7A251FE@sprynet.com>`
- **References:** `<9fjsu2$4c0$1@slb0.atl.mindspring.net> <3B2521F3.3FFAE797@Azonic.co.nz> <CNw07.2515$xp1.250458@newsread1.prod.itd.earthlink.net> <76I07.206$_93.29600957@newssvr15.news.prodigy.com> <3B4578C2.97E83781@Azonic.co.nz> <3B457CF9.98E86EFD@Azonic.co.nz> <9nmcktkdsf0rlmnqm1m178m75tlstto9ub@4ax.com> <N8w17.7021$G_1.698881@newsread2.prod.itd.earthlink.net> <1blfkts8mkb6m9ojpedvv1h1h1n1bq9888@4ax.com> <4145699b.0107081528.702dc31e@posting.google.com> <su7ikto7mj9be31765hhhodldvgvdpc39o@4ax.com> <4145699b.0107090403.4353bf30@posting.google.com>`

```
Stephen J Spiro wrote:
> 
> Frank Swarbrick <infocat@sprynet.com> wrote
…[55 more quoted lines elided]…
> maintenance.)

I guess all I'm getting at is that use of an early exist of a particular
group (function, paragraph, whatever) does not, in my opinion, make said
program 'un-structured'.  I was tought to use structured programming in
Pascal, C, and C++, all of which allow said construct.  I just find it
amazing that I'm now being told this is not structured code.  It's not
only structured, it's also, IMO, easier to read.

Anyway...
```

###### ↳ ↳ ↳ Re: "invalid" source code (END-IF, Next Sentence, and missing periods)

_(reply depth: 9)_

- **From:** "Robert M. Pritchett - RMP Consulting Partners LLC" <Sending-Email-To-This-Address-Constitutes-A-Promise-To-Send-One-Thousand-Dollars-To-RMPCP@rmpcp.com?Subject=I-Am-A-Spammer-So-I-Promise-To-Send-One-Thousand-Dollars-To-RMPCP-For-Each-Message>
- **Date:** 2001-07-10T20:41:15+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<LLJ27.1797$y%2.205330@newsread1.prod.itd.earthlink.net>`
- **References:** `<9fjsu2$4c0$1@slb0.atl.mindspring.net> <3B2521F3.3FFAE797@Azonic.co.nz> <CNw07.2515$xp1.250458@newsread1.prod.itd.earthlink.net> <76I07.206$_93.29600957@newssvr15.news.prodigy.com> <3B4578C2.97E83781@Azonic.co.nz> <3B457CF9.98E86EFD@Azonic.co.nz> <9nmcktkdsf0rlmnqm1m178m75tlstto9ub@4ax.com> <N8w17.7021$G_1.698881@newsread2.prod.itd.earthlink.net> <1blfkts8mkb6m9ojpedvv1h1h1n1bq9888@4ax.com> <4145699b.0107081528.702dc31e@posting.google.com> <su7ikto7mj9be31765hhhodldvgvdpc39o@4ax.com> <4145699b.0107090403.4353bf30@posting.google.com> <3B4A5227.A7A251FE@sprynet.com>`

```
While it's preferable to using goto's, technically, it's not structured -
true modular structured code has only one entry and one exit. If you have
several exits, then it's a real pain if you have to wrap the entire piece
of code into a deeper level e.g. under a new If or whatever. Sure, you
could do it with a Perform and just put the Perform under the If, and this
might make sense if the code you're performing is an actual meaningful
function to perform, but still having multiple exits tends to unstructure
it to some extent and makes it harder to make changes. If you use the
actual appropriate scope terminators and nesting to accomplish the same
thing, it may be nested a little more deeply than you like, but the
structure is then clear and it's easy to add both inner and outer levels
at exactly the point needed. Having exits ties it to the outer level of
the paragraph.
```

###### ↳ ↳ ↳ Re: "invalid" source code (END-IF, Next Sentence, and missing periods)

_(reply depth: 10)_

- **From:** Howard Brazee <howard.brazee@cusys.edu>
- **Date:** 2001-07-19T12:33:50-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3B57280E.D5A8FCCD@cusys.edu>`
- **References:** `<9fjsu2$4c0$1@slb0.atl.mindspring.net> <3B2521F3.3FFAE797@Azonic.co.nz> <CNw07.2515$xp1.250458@newsread1.prod.itd.earthlink.net> <76I07.206$_93.29600957@newssvr15.news.prodigy.com> <3B4578C2.97E83781@Azonic.co.nz> <3B457CF9.98E86EFD@Azonic.co.nz> <9nmcktkdsf0rlmnqm1m178m75tlstto9ub@4ax.com> <N8w17.7021$G_1.698881@newsread2.prod.itd.earthlink.net> <1blfkts8mkb6m9ojpedvv1h1h1n1bq9888@4ax.com> <4145699b.0107081528.702dc31e@posting.google.com> <su7ikto7mj9be31765hhhodldvgvdpc39o@4ax.com> <4145699b.0107090403.4353bf30@posting.google.com> <3B4A5227.A7A251FE@sprynet.com> <LLJ27.1797$y%2.205330@newsread1.prod.itd.earthlink.net>`

```


"Robert M. Pritchett - RMP Consulting Partners LLC" wrote:

> While it's preferable to using goto's, technically, it's not structured -
> true modular structured code has only one entry and one exit.

But I don't code to follow whatever someone says is "structured" - I code in a
structured way to achieve the advantages of structured programming.

What I mean, is I don't measure the goodness or badness of a GO TO by seeing
how well it fits that definition - I measure it by how it effects readability,
maintenance, correct design, etc.   Arguments that don't use these criteria
are not convincing.
```

###### ↳ ↳ ↳ Re: "invalid" source code (END-IF, Next Sentence, and missing periods)

_(reply depth: 11)_

- **From:** Giant@FingLargeSignature.com (Tony)
- **Date:** 2001-07-19T20:15:07+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3b573f79.709084830@news.swbell.net>`
- **References:** `<9fjsu2$4c0$1@slb0.atl.mindspring.net> <3B2521F3.3FFAE797@Azonic.co.nz> <CNw07.2515$xp1.250458@newsread1.prod.itd.earthlink.net> <76I07.206$_93.29600957@newssvr15.news.prodigy.com> <3B4578C2.97E83781@Azonic.co.nz> <3B457CF9.98E86EFD@Azonic.co.nz> <9nmcktkdsf0rlmnqm1m178m75tlstto9ub@4ax.com> <N8w17.7021$G_1.698881@newsread2.prod.itd.earthlink.net> <1blfkts8mkb6m9ojpedvv1h1h1n1bq9888@4ax.com> <4145699b.0107081528.702dc31e@posting.google.com> <su7ikto7mj9be31765hhhodldvgvdpc39o@4ax.com> <4145699b.0107090403.4353bf30@posting.google.com> <3B4A5227.A7A251FE@sprynet.com> <LLJ27.1797$y%2.205330@newsread1.prod.itd.earthlink.net> <3B57280E.D5A8FCCD@cusys.edu>`

```
On Thu, 19 Jul 2001 12:33:50 -0600, Howard Brazee
<howard.brazee@cusys.edu> wrote:

>
>
…[12 more quoted lines elided]…
>


This is only slightly related to the topic. Does anyone have a copy of
the original 'structured programming' document. Wasn't it written
around '71? Anyway I can't remember who wrote it or when; any help is
greatly appreciated.


Thanks,
Tony Harmon

T o n y . H a r m o n @ b n s f . c o m

===================================

"A golfer with great dreams, can 
accomplish great things."
-- Bob Rotella

"A day without hitting golf balls,
is a day longer to getting better"
-- Ben Hogan

"The average golfer's problem is 
not so much a lack of ability as 
it is a lack of knowing what he
should do." 
-- Ben Hogan

===================================
```

###### ↳ ↳ ↳ Re: "invalid" source code (END-IF, Next Sentence, and missing periods)

_(reply depth: 12)_

- **From:** "Rick Smith" <ricksmith@aiservices.com>
- **Date:** 2001-07-22T22:44:52-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<tln3tn9efhjb2f@corp.supernews.com>`
- **References:** `<9fjsu2$4c0$1@slb0.atl.mindspring.net> <3B2521F3.3FFAE797@Azonic.co.nz> <CNw07.2515$xp1.250458@newsread1.prod.itd.earthlink.net> <76I07.206$_93.29600957@newssvr15.news.prodigy.com> <3B4578C2.97E83781@Azonic.co.nz> <3B457CF9.98E86EFD@Azonic.co.nz> <9nmcktkdsf0rlmnqm1m178m75tlstto9ub@4ax.com> <N8w17.7021$G_1.698881@newsread2.prod.itd.earthlink.net> <1blfkts8mkb6m9ojpedvv1h1h1n1bq9888@4ax.com> <4145699b.0107081528.702dc31e@posting.google.com> <su7ikto7mj9be31765hhhodldvgvdpc39o@4ax.com> <4145699b.0107090403.4353bf30@posting.google.com> <3B4A5227.A7A251FE@sprynet.com> <LLJ27.1797$y%2.205330@newsread1.prod.itd.earthlink.net> <3B57280E.D5A8FCCD@cusys.edu> <3b573f79.709084830@news.swbell.net>`

```

Tony wrote in message <3b573f79.709084830@news.swbell.net>...
[...]
>This is only slightly related to the topic. Does anyone have a copy of
>the original 'structured programming' document. Wasn't it written
>around '71? Anyway I can't remember who wrote it or when; any help is
>greatly appreciated.

The original paper is part of a collection of papers by various
authors:

E. W. Dijkstra, "Structured Progamming," Software Engineering
Techniques, NATO Scientific Affairs Division, Brussels 39, Belgium
pages 84-88.

The collection is:

Software Engineering Techniques, eds. J. N. Buxton and B. Randell,
NATO Scientific Affairs Division, Brussels 39, Belgium, published
April 1970.

There is also a document:

E. W. Dijkstra, "Notes on Structured Programming," EWD 249,
Technical University, Eindhoven, Netherlands, 1969.

And a book:

O. J. Dahl, E. W. Dijkstra, and C. A. R. Hoare, Structured
Programming, Academic Press, 1972.

According to Edward Yourdon[1], an earlier paper is "sometimes
referred to as the 'structure theorem,' ... and is the basis for much of
the implementation of structured progamming ..." That paper is:

C. B�hm and G. Jacopini, "Flow Diagrams, Turing Machines, and
Languages with Only Two Formulation Rules," Communications of
the ACM, May 1966, pages 366-371.

While Dijkstra gave structured programming its name and
rationale, B�hm and Jacopini described the basic structures
and the single entry, single exit rule.

[1] E. Yourdon, Techniques of Program Structure and Design,
Prentiss-Hall, 1975.
------------------
Rick Smith
```

###### ↳ ↳ ↳ Re: "invalid" source code (END-IF, Next Sentence, and missing periods)

_(reply depth: 7)_

- **From:** "Rick Smith" <ricksmith@aiservices.com>
- **Date:** 2001-07-11T11:31:43-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<tkosalam0hane1@corp.supernews.com>`
- **References:** `<9fjsu2$4c0$1@slb0.atl.mindspring.net> <9fllv7$5ko$1@news.netmar.com> <3B2521F3.3FFAE797@Azonic.co.nz> <CNw07.2515$xp1.250458@newsread1.prod.itd.earthlink.net> <76I07.206$_93.29600957@newssvr15.news.prodigy.com> <3B4578C2.97E83781@Azonic.co.nz> <3B457CF9.98E86EFD@Azonic.co.nz> <9nmcktkdsf0rlmnqm1m178m75tlstto9ub@4ax.com> <N8w17.7021$G_1.698881@newsread2.prod.itd.earthlink.net> <1blfkts8mkb6m9ojpedvv1h1h1n1bq9888@4ax.com> <4145699b.0107081528.702dc31e@posting.google.com> <su7ikto7mj9be31765hhhodldvgvdpc39o@4ax.com>`

```

Frank Swarbrick wrote in message ...
[...]
>I'm honestly curious to see how people would do this kind of thing, while
>avoiding goto's, exit paragraph, etc.

One possibility, not discussed, is EVALUATE. EVALUATE has
a natural structure for your description; but may not, directly, fulfill
all your requirements. The basic structure for "short circuit"
validation with EVALUATE is:

validate-record.
  set record-invalid to true
  evaluate true
    when <not field-1 valid>
      move message for field-1
    when <not field-2 valid>
      move message for field-2
    ...
    when other
      set record-valid to true
  end-evaluate.

It the paragraph is too large for one's taste. The validation may
be split into two or more paragraphs.

    ...
    when other
        perform next-para-in-chain
  end-evaluate.

next-para-in-chain.
  evaluate true
    when not <field-n valid>
       move message for field-n
    ...
    when other
      set record-valid to true
  end-evaluate.

Where an additional processing step is required, such as,
a table lookup or accessing a record from a file; the validation
may be split between paragraphs.

    ...
    when <not field-n valid>
      move message for field-n empty or not numeric
    when other *> field-n has a value that may be tested
      move field-n to record-key
      read the-file key is record-key
        invalid key
          move message for field-n value not found
        not invalid key
          perform next-para-in-chain *> resume with field-n+1
      end-read
  end-evaluate.

next-para-in-chain.
  evaluate true
    when <not field-n+1 valid>
      move message for field-n+1
    ...
    when <not last-field valid>
      move message for last-field
    when other
      set record-valid to true
  end-evaluate.

It is clear that, for a record with no REDEFINES, the resulting code
will read from top to bottom. Once maintainers recognize the pattern,
they will find it easy to locate, add, remove, or modify a "when/move"
group.

Later, if I finally choose to do so, I will show how EXIT PARAGRAPH
may be used to build a "structured" solution to this problem; that is,
one that fits the guidelines for structured programming.
------------------
Rick Smith
```

###### ↳ ↳ ↳ Re: "invalid" source code (END-IF, Next Sentence, and missing periods)

_(reply depth: 8)_

- **From:** "Michael Mattias" <michael.mattias@gte.net>
- **Date:** 2001-07-12T00:40:35+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7m637.1414$FS1.422300@paloalto-snr1.gtei.net>`
- **References:** `<9fjsu2$4c0$1@slb0.atl.mindspring.net> <9fllv7$5ko$1@news.netmar.com> <3B2521F3.3FFAE797@Azonic.co.nz> <CNw07.2515$xp1.250458@newsread1.prod.itd.earthlink.net> <76I07.206$_93.29600957@newssvr15.news.prodigy.com> <3B4578C2.97E83781@Azonic.co.nz> <3B457CF9.98E86EFD@Azonic.co.nz> <9nmcktkdsf0rlmnqm1m178m75tlstto9ub@4ax.com> <N8w17.7021$G_1.698881@newsread2.prod.itd.earthlink.net> <1blfkts8mkb6m9ojpedvv1h1h1n1bq9888@4ax.com> <4145699b.0107081528.702dc31e@posting.google.com> <su7ikto7mj9be31765hhhodldvgvdpc39o@4ax.com> <tkosalam0hane1@corp.supernews.com>`

```
Rick Smith <ricksmith@aiservices.com> wrote in message
news:tkosalam0hane1@corp.supernews.com...
>
> Frank Swarbrick wrote in message ...
…[14 more quoted lines elided]…
>     when <not field-2 valid>..


Or table it
MOVE 0 to error-flag
PERFORM VARYING I from 1 by 1 until i > number-of-items or error-flag
    EVALUATE I
       WHEN field-1
           {set error-flag to true}
       WHEN field-3
       WHEN field-4
        WHEN field-5
          IF field(I) NOT NUMERIC
            set error-flag to true
           END-IF
    END-EVALUATE
END-PERFORM
IF error-flag
   move error-message (I) to Error-text
  yadda, yadda..

MCM




>       move message for field-2
>     ...
…[60 more quoted lines elided]…
>
```

###### ↳ ↳ ↳ Re: "invalid" source code (END-IF, Next Sentence, and missing periods)

_(reply depth: 8)_

- **From:** Frank Swarbrick <infocat@sprynet.com>
- **Date:** 2001-07-11T20:08:55-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3B4D06B7.BC3EC809@sprynet.com>`
- **References:** `<9fjsu2$4c0$1@slb0.atl.mindspring.net> <9fllv7$5ko$1@news.netmar.com> <3B2521F3.3FFAE797@Azonic.co.nz> <CNw07.2515$xp1.250458@newsread1.prod.itd.earthlink.net> <76I07.206$_93.29600957@newssvr15.news.prodigy.com> <3B4578C2.97E83781@Azonic.co.nz> <3B457CF9.98E86EFD@Azonic.co.nz> <9nmcktkdsf0rlmnqm1m178m75tlstto9ub@4ax.com> <N8w17.7021$G_1.698881@newsread2.prod.itd.earthlink.net> <1blfkts8mkb6m9ojpedvv1h1h1n1bq9888@4ax.com> <4145699b.0107081528.702dc31e@posting.google.com> <su7ikto7mj9be31765hhhodldvgvdpc39o@4ax.com> <tkosalam0hane1@corp.supernews.com>`

```
Rick Smith wrote:
> 
> Frank Swarbrick wrote in message ...
…[19 more quoted lines elided]…
>   end-evaluate.

I'm possibly missing something here, but where are you setting "field-1
valid"?  I don't want to make any further comment without knowing the
answer to this question.
 
> It the paragraph is too large for one's taste. The validation may
> be split into two or more paragraphs.
…[50 more quoted lines elided]…
> one that fits the guidelines for structured programming.

Looking forward to it.
```

###### ↳ ↳ ↳ Re: "invalid" source code (END-IF, Next Sentence, and missing periods)

_(reply depth: 9)_

- **From:** "Rick Smith" <ricksmith@aiservices.com>
- **Date:** 2001-07-12T00:46:20-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<tkqasi8rf0dkb0@corp.supernews.com>`
- **References:** `<9fjsu2$4c0$1@slb0.atl.mindspring.net> <9fllv7$5ko$1@news.netmar.com> <3B2521F3.3FFAE797@Azonic.co.nz> <CNw07.2515$xp1.250458@newsread1.prod.itd.earthlink.net> <76I07.206$_93.29600957@newssvr15.news.prodigy.com> <3B4578C2.97E83781@Azonic.co.nz> <3B457CF9.98E86EFD@Azonic.co.nz> <9nmcktkdsf0rlmnqm1m178m75tlstto9ub@4ax.com> <N8w17.7021$G_1.698881@newsread2.prod.itd.earthlink.net> <1blfkts8mkb6m9ojpedvv1h1h1n1bq9888@4ax.com> <4145699b.0107081528.702dc31e@posting.google.com> <su7ikto7mj9be31765hhhodldvgvdpc39o@4ax.com> <tkosalam0hane1@corp.supernews.com> <3B4D06B7.BC3EC809@sprynet.com>`

```

Frank Swarbrick wrote in message <3B4D06B7.BC3EC809@sprynet.com>...
>Rick Smith wrote:
>>
>> Frank Swarbrick wrote in message ...
>> [...]
>> >I'm honestly curious to see how people would do this kind of thing,
while
>> >avoiding goto's, exit paragraph, etc.
>>
…[19 more quoted lines elided]…
>answer to this question.

I was, quite simply, unclear. What I meant by <not field-1 valid>
is "the negation of those conditions that make field-1 valid".

Previously, you supplied the example:

validate-field-1.
    if field-1 numeric
    and field-1 > 0 and field-1 < 10
        set valid to true
    else
        set invalid to true
        move 'field 1 must from 1 - 9' to error-message
    end-if
    exit.

In the above, you expressed the conditions such that the field is 'valid'
when the conditions are true.

What I wanted to emphasize is that the conditions for the WHEN are
expressed as 'not valid' or the negation of the condition you used,
originally. For the above example, the conditions might appear as:

    evaluate true
      when not (field-1 numeric)
      when not (field-1 > 0 and field-1 < 10)
        move "field 1 must be from 1 - 9" to error-message
      when ...

or, after translation:

    evaluate true
      when field-1 not numeric
      when field-1 < 1 or field-1 > 9
        move "field 1 must be from 1 - 9" to error-message
      when ...

[...]
>> Later, if I finally choose to do so, I will show how EXIT PARAGRAPH
>> may be used to build a "structured" solution to this problem; that is,
>> one that fits the guidelines for structured programming.
>
>Looking forward to it.

I am still not looking forward to writing it. There are parts of
structured programming theory that practitioners do not use
and may not accept as practicable. This can lead to much
unproductive debate.
------------------
Rick Smith
```

###### ↳ ↳ ↳ Re: "invalid" source code (END-IF, Next Sentence, and missing periods)

_(reply depth: 10)_

- **From:** Frank Swarbrick <infocat@sprynet.com>
- **Date:** 2001-07-14T06:12:33-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3B503731.19792D4C@sprynet.com>`
- **References:** `<9fjsu2$4c0$1@slb0.atl.mindspring.net> <9fllv7$5ko$1@news.netmar.com> <3B2521F3.3FFAE797@Azonic.co.nz> <CNw07.2515$xp1.250458@newsread1.prod.itd.earthlink.net> <76I07.206$_93.29600957@newssvr15.news.prodigy.com> <3B4578C2.97E83781@Azonic.co.nz> <3B457CF9.98E86EFD@Azonic.co.nz> <9nmcktkdsf0rlmnqm1m178m75tlstto9ub@4ax.com> <N8w17.7021$G_1.698881@newsread2.prod.itd.earthlink.net> <1blfkts8mkb6m9ojpedvv1h1h1n1bq9888@4ax.com> <4145699b.0107081528.702dc31e@posting.google.com> <su7ikto7mj9be31765hhhodldvgvdpc39o@4ax.com> <tkosalam0hane1@corp.supernews.com> <3B4D06B7.BC3EC809@sprynet.com> <tkqasi8rf0dkb0@corp.supernews.com>`

```
Rick Smith wrote:
> 
> Frank Swarbrick wrote in message <3B4D06B7.BC3EC809@sprynet.com>...
…[63 more quoted lines elided]…
>       when ...


Now that is indeed interesting.  So, continuing with your example...

    evaluate true
      when field-1 not numeric
      when field-1 < 1 or field-1 > 9
        move "field 1 must be from 1 - 9" to error-message
      when (field-2 not equal to "ACTION1") and (field-2 not equal to
"ACTION2")
        move "field 2 must be 'ACTION1' or 'ACTION2'" to
error-message      

I'm not going to say I'd definately use it until I try it in a real
world example, but it's certainly something to concider.  I'm a little
wary of all of the 'not' usage, as that can get quite confusing rather
swiftly.  In any case, thanks for the idea!

Actually, I think setting an 88-level valid-field-2 as "ACTION1"
"ACTION2" and then saying
when not valid-field-2
would probably be OK.

> 
> [...]
…[11 more quoted lines elided]…
> Rick Smith
```

###### ↳ ↳ ↳ Re: "invalid" source code (END-IF, Next Sentence, and missing periods)

_(reply depth: 7)_

- **From:** Howard Brazee <howard.brazee@cusys.edu>
- **Date:** 2001-07-19T12:24:15-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3B5725CF.86887FCB@cusys.edu>`
- **References:** `<9fjsu2$4c0$1@slb0.atl.mindspring.net> <9fllv7$5ko$1@news.netmar.com> <3B2521F3.3FFAE797@Azonic.co.nz> <CNw07.2515$xp1.250458@newsread1.prod.itd.earthlink.net> <76I07.206$_93.29600957@newssvr15.news.prodigy.com> <3B4578C2.97E83781@Azonic.co.nz> <3B457CF9.98E86EFD@Azonic.co.nz> <9nmcktkdsf0rlmnqm1m178m75tlstto9ub@4ax.com> <N8w17.7021$G_1.698881@newsread2.prod.itd.earthlink.net> <1blfkts8mkb6m9ojpedvv1h1h1n1bq9888@4ax.com> <4145699b.0107081528.702dc31e@posting.google.com> <su7ikto7mj9be31765hhhodldvgvdpc39o@4ax.com>`

```
> On 8 Jul 2001 16:28:38 -0700, stephenjspiro@hotmail.com (Stephen J Spiro) wrote:
>
…[3 more quoted lines elided]…
>  single invalid field.

I tend to validate all fields, in reverse order of importance, replacing the error routine with the next one found.   It's a bit inefficient, but who cares in this instance?    It's easier to add in
a new edit this way.
```

###### ↳ ↳ ↳ Re: "invalid" source code (END-IF, Next Sentence, and missing periods)

_(reply depth: 5)_

- **From:** remove.this.scubajohn@claranet.fr
- **Date:** 2001-07-09T10:49:12+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3b49882d.425042779@news.atos-group.com>`
- **References:** `<9fjsu2$4c0$1@slb0.atl.mindspring.net> <9fllv7$5ko$1@news.netmar.com> <3B2521F3.3FFAE797@Azonic.co.nz> <CNw07.2515$xp1.250458@newsread1.prod.itd.earthlink.net> <76I07.206$_93.29600957@newssvr15.news.prodigy.com> <3B4578C2.97E83781@Azonic.co.nz> <3B457CF9.98E86EFD@Azonic.co.nz> <9nmcktkdsf0rlmnqm1m178m75tlstto9ub@4ax.com> <N8w17.7021$G_1.698881@newsread2.prod.itd.earthlink.net> <1blfkts8mkb6m9ojpedvv1h1h1n1bq9888@4ax.com>`

```
On Sat, 07 Jul 2001 21:47:23 -0600, Frank Swarbrick
<infocat@sprynet.com> wrote:

snip
>
>First, let me state that *yes*, I do *not* want to validate fields 2 - 6 if
…[3 more quoted lines elided]…
>
snip some more

Frank,
Even if you only have room for 1 error message don't you hilight, say
in red, all the invalid fields before sending back the map? 
Depending on the application the user might be able to correct other
invalid fields along with the 1st one instead of going thru IMHO an
irritating 'key in data, hit enter, correct 1st bad field, hit enter,
correct 2nd bad field, hit enter etc. cycle

Cheers
John
```

###### ↳ ↳ ↳ Re: "invalid" source code (END-IF, Next Sentence, and missing periods)

_(reply depth: 6)_

- **From:** Frank Swarbrick <infocat@sprynet.com>
- **Date:** 2001-07-09T18:49:34-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3B4A511E.7F8C4F84@sprynet.com>`
- **References:** `<9fjsu2$4c0$1@slb0.atl.mindspring.net> <9fllv7$5ko$1@news.netmar.com> <3B2521F3.3FFAE797@Azonic.co.nz> <CNw07.2515$xp1.250458@newsread1.prod.itd.earthlink.net> <76I07.206$_93.29600957@newssvr15.news.prodigy.com> <3B4578C2.97E83781@Azonic.co.nz> <3B457CF9.98E86EFD@Azonic.co.nz> <9nmcktkdsf0rlmnqm1m178m75tlstto9ub@4ax.com> <N8w17.7021$G_1.698881@newsread2.prod.itd.earthlink.net> <1blfkts8mkb6m9ojpedvv1h1h1n1bq9888@4ax.com> <3b49882d.425042779@news.atos-group.com>`

```
remove.this.scubajohn@claranet.fr wrote:
> 
> On Sat, 07 Jul 2001 21:47:23 -0600, Frank Swarbrick
…[20 more quoted lines elided]…
> John


In the particular case I was working with, the validity of field 2 is
possibly dependant on the value of field 1.  In other words, if field 1
is one thing that field 2 has certain valid values, but if field 1 is
something else then field 2 has different valid values (than the first
case).  Therefore if field 1 is not at all valid there's no way to
determine the validity of field 2.

Not something that happens often, I'll grant you, but it was true in
this particular case.
```

###### ↳ ↳ ↳ Re: "invalid" source code (END-IF, Next Sentence, and missing periods)

_(reply depth: 5)_

- **From:** "Robert M. Pritchett - RMP Consulting Partners LLC" <Sending-Email-To-This-Address-Constitutes-A-Promise-To-Send-One-Thousand-Dollars-To-RMPCP@rmpcp.com?Subject=I-Am-A-Spammer-So-I-Promise-To-Send-One-Thousand-Dollars-To-RMPCP-For-Each-Message>
- **Date:** 2001-07-10T01:06:51+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<Lys27.2321$HV1.282909@newsread1.prod.itd.earthlink.net>`
- **References:** `<9fjsu2$4c0$1@slb0.atl.mindspring.net> <9fllv7$5ko$1@news.netmar.com> <3B2521F3.3FFAE797@Azonic.co.nz> <CNw07.2515$xp1.250458@newsread1.prod.itd.earthlink.net> <76I07.206$_93.29600957@newssvr15.news.prodigy.com> <3B4578C2.97E83781@Azonic.co.nz> <3B457CF9.98E86EFD@Azonic.co.nz> <9nmcktkdsf0rlmnqm1m178m75tlstto9ub@4ax.com> <N8w17.7021$G_1.698881@newsread2.prod.itd.earthlink.net> <1blfkts8mkb6m9ojpedvv1h1h1n1bq9888@4ax.com>`

```
Re: validating multiple fields

Lots of good discussion here. Setting a flag is still much better than
using exit paragraph or goto. If fields are dependent it makes sense to
nest the if's so that e.g. field 2 isn't tested if its validity is
irrelevant or meaningless when field 1 is invalid. However, if they are
independent, it is indeed desireable to avoid giving users the same
frustration we faced with the old compilers that would only detect one bug
each time.

I can see where a flag and keeping if's at the same level can avoid lots
of nesting, but this is even better when it's desireable to detect
multiple errors anyway. My preferred approach is more like this:

#errors = 0

if field-1-bad
  #errors = #errors + 1
  highlight bad field 1
  move bad-field-1-err-msg to err-msg-line
endif

if field-2-bad
  #errors = #errors + 1
  highlight bad field 2
  move bad-field-2-err-msg to err-msg-line
endif

You can even have multiple error message lines at the bottom and subscript
them, showing the first n error messages, making sure n doesn't exceed the
number of error message lines. You can also include a line that says e.g.
"#errors errors detected" so that you get some use out of the #errors
count aside from it also being useful as a return code e.g. if it's >0 at
the end then you know the screen's bad.

If things are organized well with tables of messages you can perform
internal subroutines from each validation portion above to handle the
error messages and error counting easily, then you only need
field-specific code in each validation portion.

After all the single-field tests finally pass, you can test relationships
between them etc. using a similar approach.
```

###### ↳ ↳ ↳ Re: "invalid" source code (END-IF, Next Sentence, and missing periods)

- **From:** Howard Brazee <howard.brazee@cusys.edu>
- **Date:** 2001-07-19T12:14:35-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3B57238B.DB1D8271@cusys.edu>`
- **References:** `<9fjsu2$4c0$1@slb0.atl.mindspring.net> <9fllv7$5ko$1@news.netmar.com> <3B2521F3.3FFAE797@Azonic.co.nz> <CNw07.2515$xp1.250458@newsread1.prod.itd.earthlink.net> <76I07.206$_93.29600957@newssvr15.news.prodigy.com> <3B4578C2.97E83781@Azonic.co.nz> <3B457CF9.98E86EFD@Azonic.co.nz> <9nmcktkdsf0rlmnqm1m178m75tlstto9ub@4ax.com>`

```
Frank Swarbrick wrote:

> Yes, actually.  I have written programs that use SECTIONs because I want to use
> GO TO.  They look something like this:
…[11 more quoted lines elided]…
> Kind of funky, but I don't see why it wouldn't be concidered perfectly readable.

And I have seen people add paragraphs after code like that above.   It might be
readable, but if it isn't the standard, it might not be read.
```

#### ↳ Re: "invalid" source code (END-IF, Next Sentence, and missing periods)

- **From:** Frank Swarbrick <infocat@sprynet.com>
- **Date:** 2001-07-06T18:41:52-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<oimcktgk8ibnsmj6ba31u411ks615goto2@4ax.com>`
- **References:** `<9fjsu2$4c0$1@slb0.atl.mindspring.net> <9fllv7$5ko$1@news.netmar.com> <3B2521F3.3FFAE797@Azonic.co.nz> <CNw07.2515$xp1.250458@newsread1.prod.itd.earthlink.net> <76I07.206$_93.29600957@newssvr15.news.prodigy.com> <3B4578C2.97E83781@Azonic.co.nz>`

```
On Fri, 06 Jul 2001 09:37:22 +0100, Richard Plinston <riplin@Azonic.co.nz>
wrote:

>Terry Heinze wrote:
>> 
…[30 more quoted lines elided]…
>were a main.

I only use IBM mainframe, and I know you can pass data on the PARM= card, which
is then accessed through the linkage section.  Is this not the same when using
the PC command line.  If I were to exit program CBLPGM by typing "CBLPGM PARM1
PARM2" would I not have to use the linkage section to access the command line
parameters?

Frank Swarbrick
home: infocat@sprynet.com / work: frank.swarbrick@efirstbank.com
"I'm very seldom naughty." --Willow Rosenberg "Buffy the Vampire Slayer"
```

##### ↳ ↳ Re: "invalid" source code (END-IF, Next Sentence, and missing periods)

- **From:** Richard Plinston <riplin@Azonic.co.nz>
- **Date:** 2001-07-08T08:06:33+01:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3B480679.62C0DC78@Azonic.co.nz>`
- **References:** `<9fjsu2$4c0$1@slb0.atl.mindspring.net> <9fllv7$5ko$1@news.netmar.com> <3B2521F3.3FFAE797@Azonic.co.nz> <CNw07.2515$xp1.250458@newsread1.prod.itd.earthlink.net> <76I07.206$_93.29600957@newssvr15.news.prodigy.com> <3B4578C2.97E83781@Azonic.co.nz> <oimcktgk8ibnsmj6ba31u411ks615goto2@4ax.com>`

```
Frank Swarbrick wrote:
> 
> I only use IBM mainframe, and I know you can pass data on the PARM= card, which
> is then accessed through the linkage section.  Is this not the same when using
> the PC command line.  If I were to exit program CBLPGM by typing "CBLPGM PARM1
                                     ^^^^ execute ??
> PARM2" would I not have to use the linkage section to access the command line
> parameters?

No.  LINKAGE SECTION cannot be used in a main program executed from the
command line (in all Cobols that I have used and as specified by the '85
standard). I get the command line parameters using:

          ACCEPT Run-Parameters FROM COMMAND-LINE

or similar.
```

###### ↳ ↳ ↳ Re: "invalid" source code (END-IF, Next Sentence, and missing periods)

- **From:** "William M. Klein" <wmklein@nospam.ix.netcom.com>
- **Date:** 2001-07-07T19:07:22-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<9i88em$177$1@slb2.atl.mindspring.net>`
- **References:** `<9fjsu2$4c0$1@slb0.atl.mindspring.net> <9fllv7$5ko$1@news.netmar.com> <3B2521F3.3FFAE797@Azonic.co.nz> <CNw07.2515$xp1.250458@newsread1.prod.itd.earthlink.net> <76I07.206$_93.29600957@newssvr15.news.prodigy.com> <3B4578C2.97E83781@Azonic.co.nz> <oimcktgk8ibnsmj6ba31u411ks615goto2@4ax.com> <3B480679.62C0DC78@Azonic.co.nz>`

```
Richard,
  I think you have used Micro Focus compilers.  Check out the documentation
on the "PARMPASS" facility that allows EXACTLY this facility.
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
