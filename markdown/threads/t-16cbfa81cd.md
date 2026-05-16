[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# use of inspect statement

_18 messages · 10 participants · 2006-09_

**Topics:** [`Language features and syntax`](../topics.md#syntax)

---

### use of inspect statement

- **From:** Jerome <j.aubert1@free.fr>
- **Date:** 2006-09-05T17:02:30+02:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<edk3i1$u7c$1@s1.news.oleane.net>`

```
hello,

I want to compare the first two figures of a number with another number, 
for exemple : first number = "845263", so i want to compare "84" to 
another number.

I think i must use inspect statement but i don't understand how.

Someone could explain me with one or more exemples, please ?

Best regards

Jerome
```

#### ↳ Re: use of inspect statement

- **From:** docdwarf@panix.com ()
- **Date:** 2006-09-05T15:30:22+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<edk56e$dmn$1@reader2.panix.com>`
- **References:** `<edk3i1$u7c$1@s1.news.oleane.net>`

```
In article <edk3i1$u7c$1@s1.news.oleane.net>,
Jerome  <j.aubert1@free.fr> wrote:
>hello,
>
…[4 more quoted lines elided]…
>I think i must use inspect statement but i don't understand how.

I think that posting examples of what you have tried might help.

DD
```

##### ↳ ↳ Re: use of inspect statement

- **From:** Jerome <j.aubert1@free.fr>
- **Date:** 2006-09-05T17:51:52+02:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<edk6ei$vte$1@s1.news.oleane.net>`
- **In-Reply-To:** `<edk56e$dmn$1@reader2.panix.com>`
- **References:** `<edk3i1$u7c$1@s1.news.oleane.net> <edk56e$dmn$1@reader2.panix.com>`

```
docdwarf@panix.com a ï¿½crit :

> I think that posting examples of what you have tried might help.
> 
> DD

OK,

01 VAR1 PIC 9(6) VALUE "265453"

IF ... = "26" THEN
     process ...
END-IF

My problem is to know if VAR1 begins with then number "26" or not.
I thought INSPECT statement could help me but the more I read the doc, 
the more I think it's an error. But I must admit I don't english very 
well and the doc is in english :-(

Best regards

Jerome
```

###### ↳ ↳ ↳ Re: use of inspect statement

- **From:** "Oliver Wong" <owong@castortech.com>
- **Date:** 2006-09-05T16:05:04+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<QehLg.5773$0k7.3229@clgrps13>`
- **References:** `<edk3i1$u7c$1@s1.news.oleane.net> <edk56e$dmn$1@reader2.panix.com> <edk6ei$vte$1@s1.news.oleane.net>`

```

"Jerome" <j.aubert1@free.fr> wrote in message 
news:edk6ei$vte$1@s1.news.oleane.net...
> docdwarf@panix.com a ï¿½crit :
>
…[15 more quoted lines elided]…
> the doc is in english :-(

    You can take advantage of the hierarchical nature of data items. 
Something like this (may contain some syntax errors):

01 VAR1
  03 FIRST-TWO-DIGITS PIC 9(2) VALUE "26"
  03 FILLER           PIC 9(4) VALUE "5453"

...

IF FIRST-TWO-DIGITS OF VAR1 = "26" THEN
  process ...
END-IF

    - Oliver
```

###### ↳ ↳ ↳ Re: use of inspect statement

- **From:** "CICS_lover" <aparicio.esteves@gmail.com>
- **Date:** 2006-09-05T09:08:36-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1157472516.915193.162300@i3g2000cwc.googlegroups.com>`
- **References:** `<edk3i1$u7c$1@s1.news.oleane.net> <edk56e$dmn$1@reader2.panix.com> <edk6ei$vte$1@s1.news.oleane.net>`

```

Jerome wrote:
> docdwarf@panix.com a écrit :
>
…[19 more quoted lines elided]…
> Jerome

You could use:

IF FAR1(1:2) = '26'
....


or
 01 VAR1 PIC 9(6) VALUE "265453"
 01 RVAR1 REDEFINES VAR1.
      05  FIRST-TW0-DIGITIS PIC X(02).
      05 FILLER                     PIC X(04).

IF FIRST-TW0-DIGITS = '26'
...

Best regards
Esteves
```

###### ↳ ↳ ↳ Re: use of inspect statement

_(reply depth: 4)_

- **From:** "William M. Klein" <wmklein@nospam.netcom.com>
- **Date:** 2006-09-05T19:29:31+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<uekLg.871920$tQ4.146311@fe01.news.easynews.com>`
- **References:** `<edk3i1$u7c$1@s1.news.oleane.net> <edk56e$dmn$1@reader2.panix.com> <edk6ei$vte$1@s1.news.oleane.net> <1157472516.915193.162300@i3g2000cwc.googlegroups.com>`

```
Using reference modification (e.g. Var1 (1:2)) is certainly what I would do BUT 
as the original poster doesn't seem too knowledgeable about COBOL, I would warn 
that changing the USAGE to anything (but the default) DISPLAY or adding an "S" 
to the PICTURE clause would change what I would recommend.
```

###### ↳ ↳ ↳ Re: use of inspect statement

- **From:** docdwarf@panix.com ()
- **Date:** 2006-09-05T17:19:43+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<edkbje$at4$1@reader2.panix.com>`
- **References:** `<edk3i1$u7c$1@s1.news.oleane.net> <edk56e$dmn$1@reader2.panix.com> <edk6ei$vte$1@s1.news.oleane.net>`

```
In article <edk6ei$vte$1@s1.news.oleane.net>,
Jerome  <j.aubert1@free.fr> wrote:
>docdwarf@panix.com a �crit :
>
…[14 more quoted lines elided]…
>the more I think it's an error.

Hmmmmm... this sure smells like homework... but try this:

INITIALIZE SORT-RETURN.                                
PERFORM VARYING TALLY FROM 1 BY 1                      
 UNTIL (TALLY > 2) OR (TALLY > (LENGTH OF VAR1))       
    EVALUATE TRUE                                      
        WHEN TALLY > (LENGTH OF VAR1)                  
            DISPLAY ' ERR IN VARLEN - CONTACT SYSTEMS '
            STOP RUN                                   
        WHEN TALLY = 1                                 
            INSPECT VAR1(TALLY:1) TALLYING SORT-RETURN 
                                  FOR ALL '2'          
        WHEN TALLY = 2                                 
            INSPECT VAR1(TALLY:1) TALLYING SORT-RETURN 
                                  FOR ALL '6'          
    END-EVALUATE                                       
END-PERFORM.                                           
IF SORT-RETURN = 2                                     
    DISPLAY ' YES, THERE WAS A 26 FOUND'.              
GOBACK.

... or maybe something like that, almost.

DD
```

###### ↳ ↳ ↳ Re: use of inspect statement

_(reply depth: 4)_

- **From:** "Pete Dashwood" <dashwood@enternet.co.nz>
- **Date:** 2006-09-06T12:51:05+12:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<4m6kbtF4qpejU1@individual.net>`
- **References:** `<edk3i1$u7c$1@s1.news.oleane.net> <edk56e$dmn$1@reader2.panix.com> <edk6ei$vte$1@s1.news.oleane.net> <edkbje$at4$1@reader2.panix.com>`

```
Doc, shame on you...:-)

(When did you take to the easy targets...?)

Pete.

<docdwarf@panix.com> wrote in message news:edkbje$at4$1@reader2.panix.com...
> In article <edk6ei$vte$1@s1.news.oleane.net>,
> Jerome  <j.aubert1@free.fr> wrote:
…[42 more quoted lines elided]…
>
```

###### ↳ ↳ ↳ Re: use of inspect statement

_(reply depth: 5)_

- **From:** docdwarf@panix.com ()
- **Date:** 2006-09-06T09:31:39+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<edm4hr$so4$1@reader2.panix.com>`
- **References:** `<edk3i1$u7c$1@s1.news.oleane.net> <edk6ei$vte$1@s1.news.oleane.net> <edkbje$at4$1@reader2.panix.com> <4m6kbtF4qpejU1@individual.net>`

```
In article <4m6kbtF4qpejU1@individual.net>,
Pete Dashwood <dashwood@enternet.co.nz> wrote:
>Doc, shame on you...:-)

For what reason(s), Mr Dashwood... is it so obvious that I have so little?

>
>(When did you take to the easy targets...?)

Gotta love this Web-thingie... just to be on the safe side I checked and 
discovered that I've been misquoting for decades.  My memory is, 
admittedly, porous and I recalled it as 'A foolish consistency is the 
petty hobgoblin of small minds'; according to 
http://www.gutenberg.org/dirs/etext01/1srwe10.txt Emerson wrote 'A foolish 
consistency is the hobgoblin of little minds, adored by little statesmen 
and philosophers and divines.'

Now I am neither statesman nor philosopher... perhaps, decades on back, 
one of my professors in my Basic Elements of Drama and Dance course (part 
of a Liberal Education and all that) referred to me as 'absolutely 
*divine*!' but I have no recollection of that, either... but perhaps you 
are right and I should have prefaced this with the signpost of 'Oh, I 
*cannot* resist...' ... ah well, shoulda, coulda, woulda, as others have 
said.

[top post, nothing new below]

><docdwarf@panix.com> wrote in message news:edkbje$at4$1@reader2.panix.com...
>> In article <edk6ei$vte$1@s1.news.oleane.net>,
…[45 more quoted lines elided]…
>
```

###### ↳ ↳ ↳ Re: use of inspect statement

_(reply depth: 6)_

- **From:** Howard Brazee <howard@brazee.net>
- **Date:** 2006-09-06T09:16:22-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gsitf21kef7252lun62kb2cb68k3n8sula@4ax.com>`
- **References:** `<edk3i1$u7c$1@s1.news.oleane.net> <edk6ei$vte$1@s1.news.oleane.net> <edkbje$at4$1@reader2.panix.com> <4m6kbtF4qpejU1@individual.net> <edm4hr$so4$1@reader2.panix.com>`

```
On Wed, 6 Sep 2006 09:31:39 +0000 (UTC), docdwarf@panix.com () wrote:

>Gotta love this Web-thingie... just to be on the safe side I checked and 
>discovered that I've been misquoting for decades.  My memory is, 
…[4 more quoted lines elided]…
>and philosophers and divines.'

It is interesting to read this when politicians are campaigning
against their opponents for "flip-flopping" instead of pre-judging
everything.
```

###### ↳ ↳ ↳ Re: use of inspect statement

_(reply depth: 7)_

- **From:** docdwarf@panix.com ()
- **Date:** 2006-09-06T15:58:38+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<edmr7e$n9c$1@reader2.panix.com>`
- **References:** `<edk3i1$u7c$1@s1.news.oleane.net> <4m6kbtF4qpejU1@individual.net> <edm4hr$so4$1@reader2.panix.com> <gsitf21kef7252lun62kb2cb68k3n8sula@4ax.com>`

```
In article <gsitf21kef7252lun62kb2cb68k3n8sula@4ax.com>,
Howard Brazee  <howard@brazee.net> wrote:
>On Wed, 6 Sep 2006 09:31:39 +0000 (UTC), docdwarf@panix.com () wrote:
>
…[10 more quoted lines elided]…
>everything.

I try not to pay too much attention to the antics of politicians and those 
who watch them and those who watch those who watch them and the like... 
but I try to keep a couple of things in mind.

'Falsus in unum, falsus in omnibus' is a legalist's formulation, not a way 
to judge a human being.

Someone of age n(x) says, proudly, 'Why, I've thought this way about this 
matter ever since I was a child of (x)!'  On the one hand this shows how a 
child of (x) might come to conclusions far beyond its years, and that can 
be a Good Thing... and on the other hand it shows how a person of n(x) is 
still thinking about a matter in the same style and with the same 
conclusions as a child of (x)... and that can be a Sad Thing.

'I could have chosen a Negro... I was about to choose a Negro but instead 
I chose a tall, blond man with one black shoe.'

'Wait until you retire to philosophise.'

... or something like that, from 'The Tall Blond Man with One Black Shoe.'

DD
```

#### ↳ Re: use of inspect statement

- **From:** Jerome <j.aubert1@free.fr>
- **Date:** 2006-09-06T09:25:03+02:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<edlt4a$tga$1@s1.news.oleane.net>`
- **In-Reply-To:** `<edk3i1$u7c$1@s1.news.oleane.net>`
- **References:** `<edk3i1$u7c$1@s1.news.oleane.net>`

```
Thank you very much all of you for your useful answers.

Best regards

Jerome
```

##### ↳ ↳ Re: use of inspect statement

- **From:** docdwarf@panix.com ()
- **Date:** 2006-09-06T09:32:30+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<edm4je$8n1$1@reader2.panix.com>`
- **References:** `<edk3i1$u7c$1@s1.news.oleane.net> <edlt4a$tga$1@s1.news.oleane.net>`

```
In article <edlt4a$tga$1@s1.news.oleane.net>,
Jerome  <j.aubert1@free.fr> wrote:
>Thank you very much all of you for your useful answers.

You're quite welcome... are you going to tell us what grade you get when 
you hand in the assignment?

DD
```

###### ↳ ↳ ↳ Re: use of inspect statement

- **From:** "Michael Mattias" <michael.mattias@gte.net>
- **Date:** 2006-09-06T11:11:19+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<r1yLg.8327$yO7.6791@newssvr14.news.prodigy.com>`
- **References:** `<edk3i1$u7c$1@s1.news.oleane.net> <edlt4a$tga$1@s1.news.oleane.net> <edm4je$8n1$1@reader2.panix.com>`

```
<docdwarf@panix.com> wrote in message news:edm4je$8n1$1@reader2.panix.com...
> In article <edlt4a$tga$1@s1.news.oleane.net>,
> Jerome  <j.aubert1@free.fr> wrote:
…[3 more quoted lines elided]…
> you hand in the assignment?

What grade *who* got?
```

###### ↳ ↳ ↳ Re: use of inspect statement

_(reply depth: 4)_

- **From:** docdwarf@panix.com ()
- **Date:** 2006-09-06T12:28:08+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<edmesn$rdt$1@reader2.panix.com>`
- **References:** `<edk3i1$u7c$1@s1.news.oleane.net> <edlt4a$tga$1@s1.news.oleane.net> <edm4je$8n1$1@reader2.panix.com> <r1yLg.8327$yO7.6791@newssvr14.news.prodigy.com>`

```
In article <r1yLg.8327$yO7.6791@newssvr14.news.prodigy.com>,
Michael Mattias <michael.mattias@gte.net> wrote:
><docdwarf@panix.com> wrote in message news:edm4je$8n1$1@reader2.panix.com...
>> In article <edlt4a$tga$1@s1.news.oleane.net>,
…[6 more quoted lines elided]…
>What grade *who* got?

Answering a question with a question, Mr Mattias, is no answer at all.  
Even though the actual work for an assignment might be copied by someone 
else the grade an instructor awards is, quite often, given to the student 
who hands in the work; this may be why an otherwise perfectly-acceptable 
bit of homework could be returned with a red 'F' and the triply-underlined 
comment of 'PLAGIARISED!!!'.

DD
```

###### ↳ ↳ ↳ Re: use of inspect statement

_(reply depth: 5)_

- **From:** "HeyBub" <heybubNOSPAM@gmail.com>
- **Date:** 2006-09-06T13:35:30-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<12fu56sqrji8498@news.supernews.com>`
- **References:** `<edk3i1$u7c$1@s1.news.oleane.net> <edlt4a$tga$1@s1.news.oleane.net> <edm4je$8n1$1@reader2.panix.com> <r1yLg.8327$yO7.6791@newssvr14.news.prodigy.com> <edmesn$rdt$1@reader2.panix.com>`

```
docdwarf@panix.com wrote:
>>>
>>> You're quite welcome... are you going to tell us what grade you get
…[4 more quoted lines elided]…
> Answering a question with a question, Mr Mattias, is no answer at all.

Really?
```

###### ↳ ↳ ↳ Re: use of inspect statement

_(reply depth: 6)_

- **From:** docdwarf@panix.com ()
- **Date:** 2006-09-06T19:00:53+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<edn5t5$qkm$1@reader2.panix.com>`
- **References:** `<edk3i1$u7c$1@s1.news.oleane.net> <r1yLg.8327$yO7.6791@newssvr14.news.prodigy.com> <edmesn$rdt$1@reader2.panix.com> <12fu56sqrji8498@news.supernews.com>`

```
In article <12fu56sqrji8498@news.supernews.com>,
HeyBub <heybubNOSPAM@gmail.com> wrote:
>docdwarf@panix.com wrote:
>>>>
…[7 more quoted lines elided]…
>Really?

For certain values of 'real', perhaps so.

DD
```

#### ↳ Re: use of inspect statement

- **From:** Donald Tees <donald_tees@donald-tees.ca>
- **Date:** 2006-09-06T08:29:12-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<edmeuq$t3e$1@emma.aioe.org>`
- **References:** `<edk3i1$u7c$1@s1.news.oleane.net>`

```
Jerome wrote:
> hello,
> 
…[10 more quoted lines elided]…
> Jerome

It depends on how you define the "first two digits".  Do you mean the
first two characters in a fixed length field, or do you mean the first
two *meaningfull* digits in a numeric value? If the number "845263" is
defined as 9(8), for example, then the first two digits are actually
"00". Regardless, what you probably want is to redefine the number,
rather than using "inspect".

Donald
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
