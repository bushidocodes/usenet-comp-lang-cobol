[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# move to field "justified LEFT"

_25 messages · 19 participants · 1999-02 → 1999-03_

---

### move to field "justified LEFT"

- **From:** "don ferrario" <don@ferrario.com>
- **Date:** 1999-02-16T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7adgdp$fpo$1@news1.epix.net>`

```
I'm beating myself up - there has to be a simple way...

variable-A is described as PIC X(10).
     Records in the file contain text which is right-justified.
     There may or may not be leading spaces.
     There may or may not be spaces between the characters.


I need to move the contents to variable-B, which is PIC X(20).
    variable-B needs the data justified to the LEFT (normally default)

I need to squeeze out LEADING spaces (if any - some have none)
from variable-A during the move to variable-B.

For example:
                          variable-A  contains:      "    abc  def"
     after the move
                          variable-B contains:       "abc  def
"

I have tried INSPECTing variable-A, tallying leading spaces,
then using STRING with a POINTER to begin the after the leading
spaces.

I haven't gotten that to work consitently (probably don't have it coded
right),
but there has GOT to be a more elegant way to do this....

don ferrario
http://www.ferrario.com/don
```

#### ↳ Re: move to field "justified LEFT"

- **From:** Michael Entwistle <mikent@san.rr.com>
- **Date:** 1999-02-17T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<36CB97FE.A3AC0AA@san.rr.com>`
- **References:** `<7adgdp$fpo$1@news1.epix.net>`

```
ACUCOBOL has a routine to do this:

CALL ï¿½C$JUSTIFYï¿½ USING DATA-ITEM, JUSTIFY-TYPE

don ferrario wrote:

> I'm beating myself up - there has to be a simple way...
>
…[26 more quoted lines elided]…
> http://www.ferrario.com/don
```

#### ↳ Re: move to field "justified LEFT"

- **From:** Howard Brazee <brazee@NOSPAMhome.com>
- **Date:** 1999-02-17T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<36CAED01.5ADB5E93@NOSPAMhome.com>`
- **References:** `<7adgdp$fpo$1@news1.epix.net>`

```
> For example:
>                           variable-A  contains:      "    abc  def"
…[6 more quoted lines elided]…
> spaces.

I don't know of a "best" way of doing this.  Your suggestion should have
worked, what were your results?  

The easiest thing to do is to use your INSPECT result to do a substring
move:
MOVE VARIABLE-A (start:) TO VARIABLE-B.

I have used the UNSTRING command to parse out words when I needed them,
but I think the easiest way is to redefine your variables as arrays of
characters.  

Then loop through, moving character by character.  This has the
advantage in that you could modify it to compress multiple spaces
between words or skip punctuation, should the specs change.
```

##### ↳ ↳ Re: move to field "justified LEFT"

- **From:** "Alan Russell" <RUSSELAH@apci.com>
- **Date:** 1999-02-17T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7aeu92$t1n@netnews1.apci.com>`
- **References:** `<7adgdp$fpo$1@news1.epix.net> <36CAED01.5ADB5E93@NOSPAMhome.com>`

```
We faced this problem a long time ago in our shop, so I wrote a relatively
short assembler subroutine which will left justifiy, right justify, or
center the contents of an field.  So instead of constantly reinventing the
wheel, we just insert
                CALL 'LEFT' USING field, field-length
(or RIGHT or CENTER) as appropriate.

Alan Russell, PhD, CCP
Work - Russelah@apci.com
Home - AHRussell@computer.org
Home page - http://members.aol.com/ahrussell
-------------------------------------------------------
The views expressed are mine alone and do not necessarily reflect those of
my employer

Howard Brazee wrote in message <36CAED01.5ADB5E93@NOSPAMhome.com>...
>> For example:
>>                           variable-A  contains:      "    abc  def"
…[21 more quoted lines elided]…
>between words or skip punctuation, should the specs change.
```

###### ↳ ↳ ↳ Re: move to field "justified LEFT"

- **From:** "PAULO CRUZ" <scruz_paulo@mail.teleweb.pt>
- **Date:** 1999-02-18T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7afmod$m6c$2@fenix.maxitel.pt>`
- **References:** `<7adgdp$fpo$1@news1.epix.net> <36CAED01.5ADB5E93@NOSPAMhome.com> <7aeu92$t1n@netnews1.apci.com>`

```
Hi,

Alan Russell wrote<7aeu92$t1n@netnews1.apci.com>...
>We faced this problem a long time ago in our shop, so I wrote a relatively
>short assembler subroutine which will left justifiy, right justify, or
…[3 more quoted lines elided]…
>(or RIGHT or CENTER) as appropriate.


Since this is no Assembler n.g. and since reinventing the wheel has its own
value in a place so many learning people* are so often paying visit to, why
not posting some suggestions on how to...?

*) (and who is not learning anymore?)

Having a string of a given lenght and two variable subscripts, here's a way
of getting a left-justified string out of a right-justified one. The other
way round would similarly be easily achieved:

01 char-str pic x(20) value
   "           ola, la..".
01 sub-a pic 999 comp-3 value 0.
01 sub-b pic 999 comp-3 value 0.

if char-str not = spaces
   perform until char-str (1:1) not = space
      move 1 to sub-a
      perform varying sub-b from 2 by 1 until
         sub-b > 20
         move
         char-str(sub-b:1) to char-str(sub-a:1)
         add 1 to sub-a
      end-perform
      move space to char-str(sub-a:1)
   end-perform
else
   'non-valid input'
end-if

...and the 'thing' could also be made a callable object (oh, it lacks the
centering option!).

Rgds
P.Cruz

(snip)

>>> I have tried INSPECTing variable-A, tallying leading spaces,
>>> then using STRING with a POINTER to begin the after the leading
…[17 more quoted lines elided]…
>
```

###### ↳ ↳ ↳ Re: move to field "justified LEFT"

_(reply depth: 4)_

- **From:** Ken Foskey <waratah@zip.com.au>
- **Date:** 1999-02-19T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<36CC1BA0.623BBC28@zip.com.au>`
- **References:** `<7adgdp$fpo$1@news1.epix.net> <36CAED01.5ADB5E93@NOSPAMhome.com> <7aeu92$t1n@netnews1.apci.com> <7afmod$m6c$2@fenix.maxitel.pt>`

```
PAULO CRUZ wrote:
> 
> 
…[5 more quoted lines elided]…
> 

Now do it for a variable pitched font  :->  This is where the logic
really takes shape.
```

###### ↳ ↳ ↳ Re: move to field "justified LEFT"

_(reply depth: 5)_

- **From:** "PAULO CRUZ" <scruz_paulo@mail.teleweb.pt>
- **Date:** 1999-02-20T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7al3jr$35i$1@fenix.maxitel.pt>`
- **References:** `<7adgdp$fpo$1@news1.epix.net> <36CAED01.5ADB5E93@NOSPAMhome.com> <7aeu92$t1n@netnews1.apci.com> <7afmod$m6c$2@fenix.maxitel.pt> <36CC1BA0.623BBC28@zip.com.au>`

```

Ken Foskey wrote<36CC1BA0.623BBC28@zip.com.au>...
>
>Now do it for a variable pitched font  :->  This is where the logic
>really takes shape.


Literally speaking, yes!
P.Cruz
```

##### ↳ ↳ Re: move to field "justified LEFT"

- **From:** Ed.Stevens@nmm.nissan-usa.com
- **Date:** 1999-02-18T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7ah6lu$9rf$1@nnrp1.dejanews.com>`
- **References:** `<7adgdp$fpo$1@news1.epix.net> <36CAED01.5ADB5E93@NOSPAMhome.com>`

```
In article <36CAED01.5ADB5E93@NOSPAMhome.com>,
  Howard Brazee <brazee@NOSPAMhome.com> wrote:
> > For example:
> >                           variable-A  contains:      "    abc  def"
…[22 more quoted lines elided]…
>

With reference modification and in-line performs, there's no need to fool with
redefining the variable as an array of characters.

MOVE 1 TO SUB2
INSPECT SOURCE-STRING
   TALLYING SUB1 FOR LEADING SPACES
PERFORM VARYING SUB1 FROM SUB1 BY 1
        UNTIL SUB1 > LENGTH OF SOURCE-STRING
   IF SOURCE-STRING(SUB1:1).....
    .
    .    (whatever selective/bypassing logic you need)
    .
      MOVE SOURCE-STRING(SUB1:1) TO TARGET-STRING(SUB2:1)
   END-IF
END-PERFORM

Functionally no different than redefining the strings as arrays, but
eliminates the need for the redefinition itself. That, combined with the use
of the LENGTH OF function means the code self-adjusts if the length of
SOURCE-STRING ever changes.


Ed Stevens

-----------== Posted via Deja News, The Discussion Network ==----------
http://www.dejanews.com/       Search, Read, Discuss, or Start Your Own
```

###### ↳ ↳ ↳ Re: move to field "justified LEFT"

- **From:** Howard Brazee <brazee@NOSPAMhome.com>
- **Date:** 1999-02-18T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<36CC2890.B21C4B2F@NOSPAMhome.com>`
- **References:** `<7adgdp$fpo$1@news1.epix.net> <36CAED01.5ADB5E93@NOSPAMhome.com> <7ah6lu$9rf$1@nnrp1.dejanews.com>`

```
I wonder which is more efficient.  With a good compiler, either one.

Ed.Stevens@nmm.nissan-usa.com wrote:
> 
> In article <36CAED01.5ADB5E93@NOSPAMhome.com>,
…[51 more quoted lines elided]…
> http://www.dejanews.com/       Search, Read, Discuss, or Start Your Own
```

###### ↳ ↳ ↳ Re: move to field "justified LEFT"

- **From:** psychedelic-harry_SPAM_THIS_@mindless.com (Psychedelic Harry)
- **Date:** 1999-02-19T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<psychedelic-harry_SPAM_THIS_-1902990117320001@192.168.0.2>`
- **References:** `<7adgdp$fpo$1@news1.epix.net> <36CAED01.5ADB5E93@NOSPAMhome.com> <7ah6lu$9rf$1@nnrp1.dejanews.com>`

```
In article <7ah6lu$9rf$1@nnrp1.dejanews.com>,
Ed.Stevens@nmm.nissan-usa.com wrote:

> In article <36CAED01.5ADB5E93@NOSPAMhome.com>,
>   Howard Brazee <brazee@NOSPAMhome.com> wrote:
…[15 more quoted lines elided]…
> END-PERFORM

In this case, why not the simple approach:

   01 field-a pic x(10) just right.
   01 field-b pic x(20) just left.
   01 sub1    pic s9(8) comp binary.
   ...
   inspect field-a tallying sub1 for leading ' '
   move field-a (sub1:length of field-a - sub1) to field-b
   ...
*** or even easier (but I cant remember if it is an extension)
   string 
     field-a delimited leading ' '
     into field-b
   end-string
```

###### ↳ ↳ ↳ Re: move to field "justified LEFT"

_(reply depth: 4)_

- **From:** e=mc^3@netcom.com (Richard Anderson)
- **Date:** 1999-02-19T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7akie7$3u4@dfw-ixnews8.ix.netcom.com>`
- **References:** `<7adgdp$fpo$1@news1.epix.net> <36CAED01.5ADB5E93@NOSPAMhome.com> <7ah6lu$9rf$1@nnrp1.dejanews.com> <psychedelic-harry_SPAM_THIS_-1902990117320001@192.168.0.2>`

```
On Fri, 19 Feb 1999 01:17:32 -0500,
psychedelic-harry_SPAM_THIS_@mindless.com (Psychedelic Harry)
wrote:

>In this case, why not the simple approach:
>
…[11 more quoted lines elided]…
>   end-string

This is just peachy-keen if what you have in mind is to read
compiler error messages.  Sadly, "just left" and "delimited
leading" don't exist -- at least they don't in the IBM COBOL for
this and that Language Reference manual.

Rick Anderson
Seattle
anderson  ï¿½atï¿½  pobox  ï¿½fullstopï¿½  com
```

###### ↳ ↳ ↳ Re: move to field "justified LEFT"

_(reply depth: 5)_

- **From:** Howard Brazee <brazee@NOSPAMhome.com>
- **Date:** 1999-02-19T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<36CDD3CD.6C4F0EE5@NOSPAMhome.com>`
- **References:** `<7adgdp$fpo$1@news1.epix.net> <36CAED01.5ADB5E93@NOSPAMhome.com> <7ah6lu$9rf$1@nnrp1.dejanews.com> <psychedelic-harry_SPAM_THIS_-1902990117320001@192.168.0.2> <7akie7$3u4@dfw-ixnews8.ix.netcom.com>`

```
> This is just peachy-keen if what you have in mind is to read
> compiler error messages.  Sadly, "just left" and "delimited
> leading" don't exist -- at least they don't in the IBM COBOL for
> this and that Language Reference manual.

I thought I saw it, maybe it just left.
```

###### ↳ ↳ ↳ Re: move to field "justified LEFT"

_(reply depth: 6)_

- **From:** redsky@ibm.net (Thane Hubbell)
- **Date:** 1999-02-20T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<36ce46da.210706955@news1.ibm.net>`
- **References:** `<7adgdp$fpo$1@news1.epix.net> <36CAED01.5ADB5E93@NOSPAMhome.com> <7ah6lu$9rf$1@nnrp1.dejanews.com> <psychedelic-harry_SPAM_THIS_-1902990117320001@192.168.0.2> <7akie7$3u4@dfw-ixnews8.ix.netcom.com> <36CDD3CD.6C4F0EE5@NOSPAMhome.com>`

```
On Fri, 19 Feb 1999 14:12:45 -0700, Howard Brazee
<brazee@NOSPAMhome.com> wrote:

>> This is just peachy-keen if what you have in mind is to read
>> compiler error messages.  Sadly, "just left" and "delimited
…[3 more quoted lines elided]…
>I thought I saw it, maybe it just left.

The only Just is Right.

(Pun intended)
```

###### ↳ ↳ ↳ Re: move to field "justified LEFT"

_(reply depth: 4)_

- **From:** "JHartnett" <JHartnett@jjsnack.com>
- **Date:** 1999-03-04T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<9ZDD2.7$5M1.1029354@news.cwi.net>`
- **References:** `<7adgdp$fpo$1@news1.epix.net> <36CAED01.5ADB5E93@NOSPAMhome.com> <7ah6lu$9rf$1@nnrp1.dejanews.com> <psychedelic-harry_SPAM_THIS_-1902990117320001@192.168.0.2>`

```
Try this....

01 FIELD-1.
   03 CHAR-1        Pic x(1).
   03 REST-OF-FIELD        Pic x(19).

Move FIELD-TO-JUSTIFY to FIELD-1.
If FIELD-1 not = spaces
        perform until CHAR-1 not = space
                move REST-OF-FIELD to FIELD-1
        end-perform
End-if.



This works....,
```

###### ↳ ↳ ↳ Re: move to field "justified LEFT"

_(reply depth: 5)_

- **From:** twymer@aol.com (Twymer)
- **Date:** 1999-03-05T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<19990305084604.20123.00000791@ng-cg1.aol.com>`
- **References:** `<9ZDD2.7$5M1.1029354@news.cwi.net>`

```
sorry I came in on this late...but are you trying to get rid of spaces to the
left?
Why not set up 2 fields of equal length as the first field and unstring the
first putting all spaces in the first field and the rest in the second field. 
This would eliminate the need for a performs and moves and is a little more
elegant.

Tom Wymer
```

###### ↳ ↳ ↳ Re: move to field "justified LEFT"

_(reply depth: 6)_

- **From:** "Jerry Peacock" <bismail@bisusa.com>
- **Date:** 1999-03-05T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7bq8pc$itc$1@fir.prod.itd.earthlink.net>`
- **References:** `<9ZDD2.7$5M1.1029354@news.cwi.net> <19990305084604.20123.00000791@ng-cg1.aol.com>`

```

Twymer wrote in message <19990305084604.20123.00000791@ng-cg1.aol.com>...
>sorry I came in on this late...but are you trying to get rid of spaces to
the
>left?
>Why not set up 2 fields of equal length as the first field and unstring the
>first putting all spaces in the first field and the rest in the second
field.
>This would eliminate the need for a performs and moves and is a little more
>elegant.
>
I think he worries about:

bbbNOWbbbISbbbTHEbbbTIMEbFORbALLbbGOODbMEN

And I'm not sure how you would configure an UNSTRING command
to do it.
```

###### ↳ ↳ ↳ Re: move to field "justified LEFT"

_(reply depth: 7)_

- **From:** twymer@aol.com (Twymer)
- **Date:** 1999-03-07T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<19990306190158.14110.00004445@ng-ca1.aol.com>`
- **References:** `<7bq8pc$itc$1@fir.prod.itd.earthlink.net>`

```
could be..Ithought he was just trying to get rid of the leading spaces....

Tom Wymer
```

###### ↳ ↳ ↳ Re: move to field "justified LEFT"

_(reply depth: 7)_

- **From:** "Gunnar Opheim" <gunnar.opheim@eunet.no>
- **Date:** 1999-03-08T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<01be69a3$09791af0$0100007f@vaagshaugen>`
- **References:** `<9ZDD2.7$5M1.1029354@news.cwi.net> <19990305084604.20123.00000791@ng-cg1.aol.com> <7bq8pc$itc$1@fir.prod.itd.earthlink.net>`

```
Jerry Peacock <bismail@bisusa.com> wrote in article
<7bq8pc$itc$1@fir.prod.itd.earthlink.net>...
> I think he worries about:
> 
…[3 more quoted lines elided]…
> to do it.

Assuming he wants to get rid of all spaces (leading and intermediate),
could't this be done with an UNSTRING + a STRING statement?

INITIALIZE TEMP1 TEMP2 ... TARGET
UNSTRING SOURCE DELIMITED BY ALL SPACE INTO TEMP1 TEMP2 ...
STRING TEMP1 TEMP2 ... DELIMITED BY SPACE INTO TARGET

You must have enough TEMPn identifiers for the maximum number of words, and
each of them must be long enough to accomodate it's word.
```

###### ↳ ↳ ↳ Re: move to field "justified LEFT"

- **From:** "James King" <mangogwr@bellsouth.net>
- **Date:** 1999-02-23T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<HtqA2.15031$OS5.14987522@news3.mia>`
- **References:** `<7adgdp$fpo$1@news1.epix.net> <36CAED01.5ADB5E93@NOSPAMhome.com> <7ah6lu$9rf$1@nnrp1.dejanews.com>`

```
Yes but REMember the Length of is a COMPILE-TIME measurement.

Ed.Stevens@nmm.nissan-usa.com wrote in message
<7ah6lu$9rf$1@nnrp1.dejanews.com>...
>In article <36CAED01.5ADB5E93@NOSPAMhome.com>,
>  Howard Brazee <brazee@NOSPAMhome.com> wrote:
…[26 more quoted lines elided]…
>With reference modification and in-line performs, there's no need to fool
with
>redefining the variable as an array of characters.
>
…[14 more quoted lines elided]…
>eliminates the need for the redefinition itself. That, combined with the
use
>of the LENGTH OF function means the code self-adjusts if the length of
>SOURCE-STRING ever changes.
…[5 more quoted lines elided]…
>http://www.dejanews.com/       Search, Read, Discuss, or Start Your Own
```

###### ↳ ↳ ↳ Re: move to field "justified LEFT"

_(reply depth: 4)_

- **From:** Ed.Stevens@nmm.nissan-usa.com
- **Date:** 1999-02-23T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7aud4i$b8k$1@nnrp1.dejanews.com>`
- **References:** `<7adgdp$fpo$1@news1.epix.net> <36CAED01.5ADB5E93@NOSPAMhome.com> <7ah6lu$9rf$1@nnrp1.dejanews.com> <HtqA2.15031$OS5.14987522@news3.mia>`

```
In article <HtqA2.15031$OS5.14987522@news3.mia>,
  "James King" <mangogwr@bellsouth.net> wrote:

> Yes but REMember the Length of is a COMPILE-TIME measurement.
>
<snip>

And your point is??  Yes, "LENGTH OF" is a compile time measurement, but the
length of the object to which it is applied is also fixed at compile time.

 01 my-string pic x(30).
 01 str-len   pic 9(4) comp.

      MOVE LENGTH OF MY-STRING TO STR-LEN.

*comment: the length of MY-STRING cannot be changed at run-time,
*         so it doesn't matter that "LENGTH OF" my string is fixed at
*         compile-* time.

Ed Stevens

-----------== Posted via Deja News, The Discussion Network ==----------
http://www.dejanews.com/       Search, Read, Discuss, or Start Your Own
```

###### ↳ ↳ ↳ Re: move to field "justified LEFT"

- **From:** "Rick Smith" <ricksmith@aiservices.com>
- **Date:** 1999-02-23T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1rxA2.4$sr6.41@news19.ispnews.com>`
- **References:** `<7adgdp$fpo$1@news1.epix.net> <36CAED01.5ADB5E93@NOSPAMhome.com> <7ah6lu$9rf$1@nnrp1.dejanews.com>`

```

Ed.Stevens@nmm.nissan-usa.com wrote in message
<7ah6lu$9rf$1@nnrp1.dejanews.com>...
[...]
>PERFORM VARYING SUB1 FROM SUB1 BY 1
>        UNTIL SUB1 > LENGTH OF SOURCE-STRING

LENGTH OF is an IBM extension. The original poster did not
specify the implementation.

FUNCTION LENGTH (SOURCE-STRING) would provide
ANSI 85 compatibility.
-------------------------------
Rick Smith
e-mail: < ricksmith@aiservices.com >
```

###### ↳ ↳ ↳ Re: move to field "justified LEFT"

_(reply depth: 4)_

- **From:** Ed.Stevens@nmm.nissan-usa.com
- **Date:** 1999-02-24T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7b0v1o$ied$1@nnrp1.dejanews.com>`
- **References:** `<7adgdp$fpo$1@news1.epix.net> <36CAED01.5ADB5E93@NOSPAMhome.com> <7ah6lu$9rf$1@nnrp1.dejanews.com> <1rxA2.4$sr6.41@news19.ispnews.com>`

```
In article <1rxA2.4$sr6.41@news19.ispnews.com>,
  "Rick Smith" <ricksmith@aiservices.com> wrote:
>
> Ed.Stevens@nmm.nissan-usa.com wrote in message
…[14 more quoted lines elided]…
>

By golly, you're right! Since I learned on an IBM mainframe, I do tend to have
that tunnel vision.  LENGTH OF just got tossed from my toolbox in favor of the
LENGTH intrinsic function.  Thanks!

Ed Stevens

-----------== Posted via Deja News, The Discussion Network ==----------
http://www.dejanews.com/       Search, Read, Discuss, or Start Your Own
```

#### ↳ Re: move to field "justified LEFT"

- **From:** pduboisREMOVETHIS@enteract.com (PAL3000)
- **Date:** 1999-02-17T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<36ca4f39.10583811@news.enteract.com>`
- **References:** `<7adgdp$fpo$1@news1.epix.net>`

```
Find the first non space character in the source field, then do a

	MOVE SOURCE-FLD (FIRST-NON-BLANK:) TO DEST-FLD.

When you use a subscript without a size as in (3:) it will move all
the characters starting with and after the subscript.

Paul

On Tue, 16 Feb 1999 23:27:48 -0500, "don ferrario" <don@ferrario.com>
wrote:

>I'm beating myself up - there has to be a simple way...
>
…[29 more quoted lines elided]…
>

--------------------------------------
To reply by email, please take out the
words REMOVETHIS from my email address
```

#### ↳ Re: move to field "justified LEFT"

- **From:** paulr@bix.com (paulr)
- **Date:** 1999-02-17T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7admso$mb8@lotho.delphi.com>`
- **References:** `<7adgdp$fpo$1@news1.epix.net>`

```

I dont have a manual sitting here so you will probably 
have to go check the syntax but here is the easy way...:) 

Inspect the-thing tallying space-counter for leading spaces
computer move-size = 10 - space-counter
move the-thing(space-counter:move-size)
  the-20-char-thing(0:move-size)       


Funny how often we run into the exact same problems isn't it?  
Someone isn't going to like the reference modification, but 
hey... so C me. :) 
-Paul


don ferrario (don@ferrario.com) wrote:
: I'm beating myself up - there has to be a simple way...

: variable-A is described as PIC X(10).
:      Records in the file contain text which is right-justified.
:      There may or may not be leading spaces.
:      There may or may not be spaces between the characters.


: I need to move the contents to variable-B, which is PIC X(20).
:     variable-B needs the data justified to the LEFT (normally default)

: I need to squeeze out LEADING spaces (if any - some have none)
: from variable-A during the move to variable-B.

: For example:
:                           variable-A  contains:      "    abc  def"
:      after the move
:                           variable-B contains:       "abc  def
: "

: I have tried INSPECTing variable-A, tallying leading spaces,
: then using STRING with a POINTER to begin the after the leading
: spaces.

: I haven't gotten that to work consitently (probably don't have it coded
: right),
: but there has GOT to be a more elegant way to do this....

: don ferrario
: http://www.ferrario.com/don
```

#### ↳ Re: move to field "justified LEFT"

- **From:** "Donald Tees" <donald@willmack.com>
- **Date:** 1999-02-17T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7aek21$qet$1@news.igs.net>`
- **References:** `<7adgdp$fpo$1@news1.epix.net>`

```
Unstring delimited by ALL " " will get rid of the spaces,
then re-string the same way.
IE:

01 data-in                picture x(25) value "THIS is TEXT with SPACE".
01 temp1                picture x(15).
01 temp2                picture x(15).
etc.
MOVE SPACE TO TEMP1 TEMP2 ....
UNSTRING DATA-IN DELIMITED BY ALL " "
INTO TEMP1 TEMP2 TEMP3 TEMP4 TEMP5 TEMP6.
MOVE SPACE TO DATA-IN.
STRING TEMP1 DELIMITED BY SPACE
                TEMP2 DELIMITED BY SPACE
                 ETC
                 INTO DATA-IN.

don ferrario wrote in message <7adgdp$fpo$1@news1.epix.net>...
>I'm beating myself up - there has to be a simple way...
>
…[30 more quoted lines elided]…
>
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
