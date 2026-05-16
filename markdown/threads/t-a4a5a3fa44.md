[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# COMP-1 and COMP-2 resolution on unix (using microfocus)

_25 messages · 9 participants · 2007-06_

**Topics:** [`Compilers and vendors`](../topics.md#compilers) · [`Language features and syntax`](../topics.md#syntax)

---

### COMP-1 and COMP-2 resolution on unix (using microfocus)

- **From:** kimi <mraghu83@gmail.com>
- **Date:** 2007-06-21T22:26:15-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1182489975.791804.84390@d30g2000prg.googlegroups.com>`

```
HI ppl,
           i have migrated the data on mainframe to SOLARIS UNIX.
           COMP-1 and COMP-2 is read as junk when the application is
run on this data.
           But COMP and COMP-3 data are read fine.

           I have Microfocus Server Express 4.0 SP2 installed in my
UNIX system.
           I believe This issue has something to do with the way the
operaring system interprets it.
           Is there a way in which i can read this COMP-1 and COMP-2
data successfully??

Thanks and regards,
kimi
```

#### ↳ Re: COMP-1 and COMP-2 resolution on unix (using microfocus)

- **From:** Louis Krupp <lkrupp@pssw.nospam.com.invalid>
- **Date:** 2007-06-22T04:49:54-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<137naara153c81a@corp.supernews.com>`
- **In-Reply-To:** `<1182489975.791804.84390@d30g2000prg.googlegroups.com>`
- **References:** `<1182489975.791804.84390@d30g2000prg.googlegroups.com>`

```
kimi wrote:
> HI ppl,
>            i have migrated the data on mainframe to SOLARIS UNIX.
…[9 more quoted lines elided]…
> data successfully??

As far as I know, COMP-1 and COMP-2 are floating point.  Your mainframe 
(IBM?) probably uses its own floating point format, and your Sun uses 
IEEE floating point.  The bits are interpreted differently.  It's an 
architecture difference and doesn't have much to do with the operating 
system.

Depending on the range of your floating point data, you might be able to 
convert the file on the mainframe so it only uses COMP-3 (packed 
decimal), or you could try to find a program that will do the conversion 
on Solaris.  You could also write such a program (but you probably 
wouldn't want to do it in COBOL).

Louis
```

##### ↳ ↳ Re: COMP-1 and COMP-2 resolution on unix (using microfocus)

- **From:** "Michael Mattias" <mmattias@talsystems.com>
- **Date:** 2007-06-22T11:38:42+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<6xOei.3262$Rw1.896@newssvr25.news.prodigy.net>`
- **References:** `<1182489975.791804.84390@d30g2000prg.googlegroups.com> <137naara153c81a@corp.supernews.com>`

```
"Louis Krupp" <lkrupp@pssw.nospam.com.invalid> wrote in message 
news:137naara153c81a@corp.supernews.com...
> kimi wrote:
>> HI ppl,
…[22 more quoted lines elided]…
> it in COBOL).

COMP-3 doesn't help. This is an ASCII-EBCIDC character set issue, which is 
only going to be solved by putting all the data into USAGE IS DISPLAY 
format.  (Or by handling ASCII-EBCDIC conversions on a field-by-field basis 
on either end of the file transfer).

See my tutorial on the subject at 
http://www.talsystems.com/tsihome_html/downloads/C2IEEE.htm

FWIW, both COMP-1 and COMP-2 are "implementor defined" data formats. With 
IBM mainframe COBOL, it's either IBM proprietary format or IEEE single 
(COMP-1) or IEEE double (COMP-2) depending on the setting of the FLOAT 
directive at compile time===> FLOAT ([HEX |NATIVE] | IEEE)
```

###### ↳ ↳ ↳ Re: COMP-1 and COMP-2 resolution on unix (using microfocus)

- **From:** Louis Krupp <lkrupp@pssw.nospam.com.invalid>
- **Date:** 2007-06-22T06:15:24-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<137nfb497l9ol0f@corp.supernews.com>`
- **In-Reply-To:** `<6xOei.3262$Rw1.896@newssvr25.news.prodigy.net>`
- **References:** `<1182489975.791804.84390@d30g2000prg.googlegroups.com> <137naara153c81a@corp.supernews.com> <6xOei.3262$Rw1.896@newssvr25.news.prodigy.net>`

```
Michael Mattias wrote:
> "Louis Krupp" <lkrupp@pssw.nospam.com.invalid> wrote in message 
> news:137naara153c81a@corp.supernews.com...
…[37 more quoted lines elided]…
> 

The ASCII-EBCDIC issue was the first thing that occurred to me, but 
since the OP says that COMP and COMP-3 work fine, that might not be the 
problem.  (I'd be willing to guess that none of the data is DISPLAY and 
no EBCDIC->ASCII conversion is being performed.)

What I don't know -- and what you might -- is if there's  a way to mix 
both floating point formats in one executable.  If my guess about all 
this is right, that would give the OP a relatively simple solution.

Louis
```

###### ↳ ↳ ↳ Re: COMP-1 and COMP-2 resolution on unix (using microfocus)

- **From:** kimi <mraghu83@gmail.com>
- **Date:** 2007-06-22T21:07:50-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1182571670.971157.206720@m37g2000prh.googlegroups.com>`
- **In-Reply-To:** `<6xOei.3262$Rw1.896@newssvr25.news.prodigy.net>`
- **References:** `<1182489975.791804.84390@d30g2000prg.googlegroups.com> <137naara153c81a@corp.supernews.com> <6xOei.3262$Rw1.896@newssvr25.news.prodigy.net>`

```
On Jun 22, 4:38 pm, "Michael Mattias" <mmatt...@talsystems.com> wrote:
> "Louis Krupp" <lkr...@pssw.nospam.com.invalid> wrote in message
>
…[36 more quoted lines elided]…
>
OKey.. Now say I am moving COMP-1 to DISPLAY field..
The COMP-1 data is say 21.234, it will be stored as 0.21234E+02.
Now if i move it to a display field with PIC S9(8)V999, In This case i
would get the right value..But,
If i decide to move it to say PIC S9(8)V99, In this case the value in
the DISPLAY field would'nt be in SYNC with the COMP-1 field.
So, can u pls tell me how would i know what is the PICTURE clause i
have to specify in the program for the display field...???

> See my tutorial on the subject athttp://www.talsystems.com/tsihome_html/downloads/C2IEEE.htm
>
…[11 more quoted lines elided]…
> - Show quoted text -
```

###### ↳ ↳ ↳ Re: COMP-1 and COMP-2 resolution on unix (using microfocus)

_(reply depth: 4)_

- **From:** "Pete Dashwood" <dashwood@removethis.enternet.co.nz>
- **Date:** 2007-06-23T17:14:28+12:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<5e3ohlF34n4bjU1@mid.individual.net>`
- **References:** `<1182489975.791804.84390@d30g2000prg.googlegroups.com> <137naara153c81a@corp.supernews.com> <6xOei.3262$Rw1.896@newssvr25.news.prodigy.net> <1182571670.971157.206720@m37g2000prh.googlegroups.com>`

```

"kimi" <mraghu83@gmail.com> wrote in message 
news:1182571670.971157.206720@m37g2000prh.googlegroups.com...
> On Jun 22, 4:38 pm, "Michael Mattias" <mmatt...@talsystems.com> wrote:
>> "Louis Krupp" <lkr...@pssw.nospam.com.invalid> wrote in message
…[52 more quoted lines elided]…
> have to specify in the program for the display field...???

Here's one approach that might help...


WORKING-STORAGE SECTION.
...
01    integer-part      pic 9(n). *> n = the limit for your compiler, 
typically 18.
01    decimal-part    pic v9(n).

01     float-double    comp-2.

01     counts comp value zero.
        12 leading-count     pic s9(4).
        12 trailing-count      pic s9(4).
        12 length-to-move  pic s9(4).

01     display-string  pic x([2n + 1]). *> n = the limit for your compiler, 
typically 18....so pic x(37), in that case.

PROCEDURE DIVISION.
...
BUILD-DISPLAY-STRING.
        move float-double to integer-part decimal-part
        string
            integer-part
                delimited by size
            "."
                delimited by size
            decimal-part
                delimited by size
                    into display-string
        end-string
        move zero to leading-count trailing-count
        inspect display-string
            tallying leading-count leading zeroes.
        inspect REVERSED display-string
            tallying trailing-count leading zeroes.
        compute length-to-move = [2n + 1] - leading-zeros + trailing-zeros 
*> see formula above.
        move display-string (leading-count + 1: length-to-move) to 
display-string


At this point display-string  (hopefully :-))contains a left justified 
representation of your original float, without any loss of precision, 
irrespective of how many places it has, within the limits of your COBOL 
implementation.

Your example: 0.21234E+02 appears as: 21.234

0.212345678901234E+10 appears as: 21234.5678901234 etc.

DISCLAIMER: I have NOT compiled and tested this code. It is intended to show 
an approach, and may contain minor syntax or logical errors. If you use it, 
step through it with a debugger.

Pete.








>
>> See my tutorial on the subject 
…[15 more quoted lines elided]…
>
```

###### ↳ ↳ ↳ Re: COMP-1 and COMP-2 resolution on unix (using microfocus)

_(reply depth: 5)_

- **From:** kimi <mraghu83@gmail.com>
- **Date:** 2007-06-22T22:35:40-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1182576940.008574.208220@d30g2000prg.googlegroups.com>`
- **In-Reply-To:** `<5e3ohlF34n4bjU1@mid.individual.net>`
- **References:** `<1182489975.791804.84390@d30g2000prg.googlegroups.com> <137naara153c81a@corp.supernews.com> <6xOei.3262$Rw1.896@newssvr25.news.prodigy.net> <1182571670.971157.206720@m37g2000prh.googlegroups.com> <5e3ohlF34n4bjU1@mid.individual.net>`

```
On Jun 23, 10:14 am, "Pete Dashwood"
<dashw...@removethis.enternet.co.nz> wrote:
> "kimi" <mragh...@gmail.com> wrote in message
>
…[113 more quoted lines elided]…
>
Thanks for that Pete. I'l try out this and let u know.

>
>
…[20 more quoted lines elided]…
> - Show quoted text -
```

###### ↳ ↳ ↳ Re: COMP-1 and COMP-2 resolution on unix (using microfocus)

_(reply depth: 5)_

- **From:** Louis Krupp <lkrupp@pssw.nospam.com.invalid>
- **Date:** 2007-06-23T02:02:57-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<137pktr2vbnrm3c@corp.supernews.com>`
- **In-Reply-To:** `<5e3ohlF34n4bjU1@mid.individual.net>`
- **References:** `<1182489975.791804.84390@d30g2000prg.googlegroups.com> <137naara153c81a@corp.supernews.com> <6xOei.3262$Rw1.896@newssvr25.news.prodigy.net> <1182571670.971157.206720@m37g2000prh.googlegroups.com> <5e3ohlF34n4bjU1@mid.individual.net>`

```
Pete Dashwood wrote:
> "kimi" <mraghu83@gmail.com> wrote in message 
> news:1182571670.971157.206720@m37g2000prh.googlegroups.com...
…[106 more quoted lines elided]…
> step through it with a debugger.
<snip>

Something else might be required if the numbers are really big, say on 
the order of 10 to the 50th.  In that case, the following appears to 
work, at least for the value tested:

identification division.
program-id.     c1.
environment division.
data division.
working-storage section.
77      x       comp-2 value 21.234.
77      z       comp-2.
77      d       pic -(7)9.99.
01      rec.
         05      exp pic s9(3) sign leading separate.
         05      filler pic x value space.
         05      man pic s9v9(8) sign leading separate.
procedure division.
begin.
         move x to z.
         multiply 10000000000 by z.
         multiply 10000000000 by z.
         multiply 10000000000 by z.
         multiply 10000000000 by z.
         multiply 10000000000 by z.

*	Roll our own crude decimal floating point

         compute exp = function log10(z).
         perform exp times
                 divide 10 into z
         end-perform.
         move z to man.
         display rec.

*	Now decode what we just created

         move man to z.
         perform exp times
                 multiply 10 by z
         end-perform.

*	And see how it differs from what we started with

         compute d = x - z.
         display d.
         stop run.

  And the output:

+051 +212340000
        0.00

I haven't allowed for really small numbers;  you'd probably have to test 
for a negative exponent and reverse the multiplication and division.

Louis
```

###### ↳ ↳ ↳ Re: COMP-1 and COMP-2 resolution on unix (using microfocus)

_(reply depth: 6)_

- **From:** Louis Krupp <lkrupp@pssw.nospam.com.invalid>
- **Date:** 2007-06-23T02:30:06-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<137pmgo56ha2n93@corp.supernews.com>`
- **In-Reply-To:** `<137pktr2vbnrm3c@corp.supernews.com>`
- **References:** `<1182489975.791804.84390@d30g2000prg.googlegroups.com> <137naara153c81a@corp.supernews.com> <6xOei.3262$Rw1.896@newssvr25.news.prodigy.net> <1182571670.971157.206720@m37g2000prh.googlegroups.com> <5e3ohlF34n4bjU1@mid.individual.net> <137pktr2vbnrm3c@corp.supernews.com>`

```
Louis Krupp wrote:
<snip>
>         perform exp times
>                 divide 10 into z
>         end-perform.

Never mind -- I forgot that C is the language without built-in 
exponentiation, not COBOL.

         compute z = z / 10 ** exp.

works just fine.

<snip>
>         perform exp times
>                 multiply 10 by z
>         end-perform.

As does

         compute z = z * 10 ** exp.

<snip>
> I haven't allowed for really small numbers;  you'd probably have to test 
> for a negative exponent and reverse the multiplication and division.

Never mind.

Louis
```

###### ↳ ↳ ↳ Re: COMP-1 and COMP-2 resolution on unix (using microfocus)

_(reply depth: 4)_

- **From:** "Rick Smith" <ricksmith@mfi.net>
- **Date:** 2007-06-23T06:04:15-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<137ps42dmi7sd46@corp.supernews.com>`
- **References:** `<1182489975.791804.84390@d30g2000prg.googlegroups.com> <137naara153c81a@corp.supernews.com> <6xOei.3262$Rw1.896@newssvr25.news.prodigy.net> <1182571670.971157.206720@m37g2000prh.googlegroups.com>`

```

"kimi" <mraghu83@gmail.com> wrote in message
news:1182571670.971157.206720@m37g2000prh.googlegroups.com...
[snip]
> OKey.. Now say I am moving COMP-1 to DISPLAY field..
> The COMP-1 data is say 21.234, it will be stored as 0.21234E+02.
…[5 more quoted lines elided]…
> have to specify in the program for the display field...???

PIC +.9(16)E+99 was sufficient to hold every possible
value for COMP-1 and COMP-2 fields with IBM
Full ANS COBOL (COBOL 68). It might still work
today.
```

###### ↳ ↳ ↳ Re: COMP-1 and COMP-2 resolution on unix (using microfocus)

_(reply depth: 5)_

- **From:** Louis Krupp <lkrupp@pssw.nospam.com.invalid>
- **Date:** 2007-06-23T08:36:12-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<137qbv51vokat6e@corp.supernews.com>`
- **In-Reply-To:** `<137ps42dmi7sd46@corp.supernews.com>`
- **References:** `<1182489975.791804.84390@d30g2000prg.googlegroups.com> <137naara153c81a@corp.supernews.com> <6xOei.3262$Rw1.896@newssvr25.news.prodigy.net> <1182571670.971157.206720@m37g2000prh.googlegroups.com> <137ps42dmi7sd46@corp.supernews.com>`

```
Rick Smith wrote:
> "kimi" <mraghu83@gmail.com> wrote in message
> news:1182571670.971157.206720@m37g2000prh.googlegroups.com...
…[13 more quoted lines elided]…
> today.

Cool.  I didn't know you could do that.

I feel stupid.

Louis
```

###### ↳ ↳ ↳ Re: COMP-1 and COMP-2 resolution on unix (using microfocus)

_(reply depth: 4)_

- **From:** "HeyBub" <heybubNOSPAM@gmail.com>
- **Date:** 2007-06-23T17:23:13-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<137r7a3438887d3@news.supernews.com>`
- **References:** `<1182489975.791804.84390@d30g2000prg.googlegroups.com> <137naara153c81a@corp.supernews.com> <6xOei.3262$Rw1.896@newssvr25.news.prodigy.net> <1182571670.971157.206720@m37g2000prh.googlegroups.com>`

```
kimi wrote:
> OKey.. Now say I am moving COMP-1 to DISPLAY field..
> The COMP-1 data is say 21.234, it will be stored as 0.21234E+02.
…[6 more quoted lines elided]…
>

Use S9(9)V9(9) (DISPLAY) for the intermediate field, then move everything 
back to a COMP-1 fields when you read them in.

There WILL BE conversion errors, but they should be consistent.

Question: Why would anyone use floating point for a value with only five 
significant digits?
```

###### ↳ ↳ ↳ Re: COMP-1 and COMP-2 resolution on unix (using microfocus)

_(reply depth: 4)_

- **From:** Binyamin Dissen <postingid@dissensoftware.com>
- **Date:** 2007-06-24T13:02:14+03:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<35gs739m6ebkoblaudviq5ejjiujk7s5hp@4ax.com>`
- **References:** `<1182489975.791804.84390@d30g2000prg.googlegroups.com> <137naara153c81a@corp.supernews.com> <6xOei.3262$Rw1.896@newssvr25.news.prodigy.net> <1182571670.971157.206720@m37g2000prh.googlegroups.com>`

```
On Fri, 22 Jun 2007 21:07:50 -0700 kimi <mraghu83@gmail.com> wrote:

:>OKey.. Now say I am moving COMP-1 to DISPLAY field..
:>The COMP-1 data is say 21.234, it will be stored as 0.21234E+02.
:>Now if i move it to a display field with PIC S9(8)V999, In This case i
:>would get the right value..But,
:>If i decide to move it to say PIC S9(8)V99, In this case the value in
:>the DISPLAY field would'nt be in SYNC with the COMP-1 field.
:>So, can u pls tell me how would i know what is the PICTURE clause i
:>have to specify in the program for the display field...???

Do you know the scale of your data? Either way you can use an E picture.

But, be quite aware that radix 16 numbers may not convert exactly to radix 10
numbers. And vice versa.
```

##### ↳ ↳ Re: COMP-1 and COMP-2 resolution on unix (using microfocus)

- **From:** kimi <mraghu83@gmail.com>
- **Date:** 2007-06-22T04:47:27-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1182512847.839451.127030@i38g2000prf.googlegroups.com>`
- **In-Reply-To:** `<137naara153c81a@corp.supernews.com>`
- **References:** `<1182489975.791804.84390@d30g2000prg.googlegroups.com> <137naara153c81a@corp.supernews.com>`

```
On Jun 22, 3:49 pm, Louis Krupp <lkr...@pssw.nospam.com.invalid>
wrote:
> kimi wrote:
> > HI ppl,
…[24 more quoted lines elided]…
> Louis

As you suggested i am looking for a solution in which i can convert
all the COMP-1 variables to COMP-3 on mainframe itself.
But there seems to be a problem with just directly moving the COMP-1
variable to say S9(08)V99 COMP-3.  But i would be wrong in specifying
S9(08)V99 because i do not know the place of decimal point.
Therefore merely moving the COMP-1 data to COMP-3 with a move
statement would be wrong.
Can you pls suggest me methods to the conversion or if u have a COBOL
program to do that it would be great!!!!
```

###### ↳ ↳ ↳ Re: COMP-1 and COMP-2 resolution on unix (using microfocus)

- **From:** Louis Krupp <lkrupp@pssw.nospam.com.invalid>
- **Date:** 2007-06-22T06:09:53-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<137nf0qfslm3id0@corp.supernews.com>`
- **In-Reply-To:** `<1182512847.839451.127030@i38g2000prf.googlegroups.com>`
- **References:** `<1182489975.791804.84390@d30g2000prg.googlegroups.com> <137naara153c81a@corp.supernews.com> <1182512847.839451.127030@i38g2000prf.googlegroups.com>`

```
kimi wrote:
> On Jun 22, 3:49 pm, Louis Krupp <lkr...@pssw.nospam.com.invalid>
> wrote:
…[35 more quoted lines elided]…
> 

As far as I know, moving a COMP-1 to a COMP-3 would be safe as long as 
the original value was within the range of the COMP-3 picture (less than 
ten to the eighth in the case of pic s9(8)v99).  You also have to worry 
about losing too many fractional decimal places;  a value that 
approximates 0.1234 would be truncated to 0.12, and that might be a problem.

If the range is a problem, you might want to do something like this: 
add a field to store the integer part of the common logarithm of the 
COMP-1 value, normalize that value to something on the order of 1 (with 
lots of places after the decimal point), store the normalized value as 
COMP-3, and put it all back together on Solaris.  I'm sure someone here 
has done all this and can add details if you need them.

Louis
```

##### ↳ ↳ Re: COMP-1 and COMP-2 resolution on unix (using microfocus)

- **From:** kimi <mraghu83@gmail.com>
- **Date:** 2007-06-22T05:07:37-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1182514057.634311.84870@o11g2000prd.googlegroups.com>`
- **In-Reply-To:** `<137naara153c81a@corp.supernews.com>`
- **References:** `<1182489975.791804.84390@d30g2000prg.googlegroups.com> <137naara153c81a@corp.supernews.com>`

```
On Jun 22, 3:49 pm, Louis Krupp <lkr...@pssw.nospam.com.invalid>
wrote:
> kimi wrote:
> > HI ppl,
…[24 more quoted lines elided]…
> Louis

Suppose for a moment that,on mainframe the format is IBM proprietary
format  and on UNIX it is IEEE format.
In this case if i am trying to read COMP-1 or COMP-2 data [migrated
data which is converted to ASCII from EBCDIC on mainframe] then it
would read junk data because the above two formats interpret it
differently.
If i change the FLOAT directive at compile time to the format which is
same as that in mainframe , then would it work?? If so do you know any
command which would change the FLOAT format on UNIX.??
Also as i have mentioned i am using the microfocus compiler to compile
the programs on UNIX... Does microfocus provide such a command??
```

###### ↳ ↳ ↳ Re: COMP-1 and COMP-2 resolution on unix (using microfocus)

- **From:** Louis Krupp <lkrupp@pssw.nospam.com.invalid>
- **Date:** 2007-06-22T06:20:08-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<137nfk1iv31pv15@corp.supernews.com>`
- **In-Reply-To:** `<1182514057.634311.84870@o11g2000prd.googlegroups.com>`
- **References:** `<1182489975.791804.84390@d30g2000prg.googlegroups.com> <137naara153c81a@corp.supernews.com> <1182514057.634311.84870@o11g2000prd.googlegroups.com>`

```
kimi wrote:
> On Jun 22, 3:49 pm, Louis Krupp <lkr...@pssw.nospam.com.invalid>
> wrote:
…[37 more quoted lines elided]…
> 

If you're converting the records from EBCDIC to ASCII (see Michael's 
post above), then you'd get garbage even if both systems used the same 
floating point format.  In fact, I would expect that you'd get garbage 
in your COMP and COMP-3 fields as well.

As far as changing the floating point format in Microfocus COBOL, I 
wouldn't know.  See Michael's post and then check your manual...

Louis
```

###### ↳ ↳ ↳ Re: COMP-1 and COMP-2 resolution on unix (using microfocus)

- **From:** "Michael Mattias" <mmattias@talsystems.com>
- **Date:** 2007-06-22T12:55:34+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<aFPei.41364$5j1.21974@newssvr21.news.prodigy.net>`
- **References:** `<1182489975.791804.84390@d30g2000prg.googlegroups.com> <137naara153c81a@corp.supernews.com> <1182514057.634311.84870@o11g2000prd.googlegroups.com>`

```
"kimi" <mraghu83@gmail.com> wrote in message 
news:1182514057.634311.84870@o11g2000prd.googlegroups.com...
> If i change the FLOAT directive at compile time to the format which is
> same as that in mainframe , then would it work?? I

Unless your 'nix compiler supports IBM HEX (aka NATIVE) format data types, 
that's not an option.

And If you are going to recompile the mainframe program anyway, just change 
the record to ensure all your numeric fields are in a USAGE IS DISPLAY 
format.

I believe I recommended   "PICTURE whatever  SIGN [LEADING] SEPARATE"  in my 
FREE (that means you can use it at no cost) tutorial.

MCM
```

###### ↳ ↳ ↳ Re: COMP-1 and COMP-2 resolution on unix (using microfocus)

_(reply depth: 4)_

- **From:** "Michael Mattias" <mmattias@talsystems.com>
- **Date:** 2007-06-22T13:01:53+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<5LPei.41365$5j1.20090@newssvr21.news.prodigy.net>`
- **References:** `<1182489975.791804.84390@d30g2000prg.googlegroups.com> <137naara153c81a@corp.supernews.com> <1182514057.634311.84870@o11g2000prd.googlegroups.com> <aFPei.41364$5j1.21974@newssvr21.news.prodigy.net>`

```
"Michael Mattias" <mmattias@talsystems.com> wrote in message 
news:aFPei.41364$5j1.21974@newssvr21.news.prodigy.net...
> I believe I recommended   "PICTURE whatever  SIGN [LEADING] SEPARATE"  in 
> my FREE (that means you can use it at no cost) tutorial.

I was just thinking, "why did I bother putting up that document on my web 
site all those years ago?"

But before I did anything dramatic, I thought I'd had better check to see if 
ANYONE was looking at it.....

May 2007: 292 reads (Well, opens. Can't say if all 292 actually READ the 
damn thing).

(Sheesh, that was more hits than my home page last month.)
```

#### ↳ Re: COMP-1 and COMP-2 resolution on unix (using microfocus)

- **From:** "William M. Klein" <wmklein@nospam.netcom.com>
- **Date:** 2007-06-25T03:46:05+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1UGfi.7159$ia2.4910@fe01.news.easynews.com>`
- **References:** `<1182489975.791804.84390@d30g2000prg.googlegroups.com>`

```
There have been lots of answers that seem to ignore the fact that the OP asked 
specifically about Server Express V4 SP2.

If you check the documentation at:
http://supportline.microfocus.com/Documentation/books/sx40sp2/sx40indx.htm
, you will find information on:
   NATIVE-FLOATING-POINT
compiler directive.  According to the documentation,

"Specifying NATIVE-FLOATING-POINT causes all floating point data items to use 
IEEE. Specifying NONATIVE-FLOATING-POINT causes the format used to be determined 
by the MAINFRAME_FLOATING_POINT environment variable."

The V4 dox aren't good on the environment variable, but the V5 dox explain it, 
i.e.

"TRUE Specifies that IBM hexadecimal format floating point data items are to be 
used."

  ***

In other words, if you download a mainframe file in "binary" (keeping character 
data in EBCDIC and COMP fields with mainframe sign nibbles) you will ALSO be 
able to use S/390 (hex format) COMP-1 and COMP-2 values.

If you want to have a "combination" of ASCII data and S/390 hex floating point 
fields - or EBCDIC character data and IEEE floating point, then you will need to 
do some more work.

   ***

In general,
   >>> IF USING ANY MICRO FOCUS product (not true for many others workstation 
COBOL compilers
if you are "moving" data from the (IBM) mainframe to Windows, Linux, or Unix, 
then you PROBABLY want to convert (before downloading) all (non-Unicode) data to 
"USAGE DISPLAY".

 For Comp, COMP-3, COMP-4, Packed-Decimal, and BINARY usages, this means
  - move them to USAGE DISPLAY SIGN IS SEPARATE fields

For COMP-1 and COMP-2, then move them to
  "external floating point" fields, i.e
     Pic is +9(9).9(9)E+99
fields

Then download the data with EBCDIC to ASCII conversion.  Then convert the fields 
back to "native" fields.  This will give you the "best performing" native data 
types on the "Workstation".

If, on the other hand, you are moving files back and forth from the (IBM) 
mainframe to the Workstation and run-time performance on the workstation isn't 
the highest priority,

Then use all the MF directives to get "mainframe emulation" on the workstation. 
This would include (but not be limited to)
 CHARSET(EBCIC), IBM-COMP, NO-NATIVE-FLOATIN-POINT

In the Server Express V5 manuals at:
   http://supportline.microfocus.com/Documentation/books/sx50/sx50indx.htm

you can find a book called
  "Mainframe Emulation"

Even if you (like the OP) are using Server Express 4.0 (or one of the other MF 
products), this book should give you good guidance on how to "emulate" the (IBM) 
mainframe on the workstation (Unix, PC, or Linux).

Hopefully, this answers the original question without getting into what you can 
and cannot do with other workstation COBOL compilers.
```

##### ↳ ↳ Re: COMP-1 and COMP-2 resolution on unix (using microfocus)

- **From:** "Rick Smith" <ricksmith@mfi.net>
- **Date:** 2007-06-25T00:31:28-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<137uhdf5167ogb2@corp.supernews.com>`
- **References:** `<1182489975.791804.84390@d30g2000prg.googlegroups.com> <1UGfi.7159$ia2.4910@fe01.news.easynews.com>`

```

"William M. Klein" <wmklein@nospam.netcom.com> wrote in message
news:1UGfi.7159$ia2.4910@fe01.news.easynews.com...
[snip]
> For COMP-1 and COMP-2, then move them to
>   "external floating point" fields, i.e
>      Pic is +9(9).9(9)E+99
> fields

Hmm! "9(9).9(9)" is 18 digits.

<
http://publib.boulder.ibm.com/infocenter/pdthelp/v1r1/index.jsp?topic=/com.i
bm.entcobol3.doc/cpari09.htm >
-----
The mantissa can contain from 1 to 16 numeric characters.
-----
< http://supportline.microfocus.com/Documentation/books/sx40sp2/sx40indx.htm
>
-----
The significand can contain from 1 to 16 numeric characters.
-----
```

##### ↳ ↳ Re: COMP-1 and COMP-2 resolution on unix (using microfocus)

- **From:** kimi <mraghu83@gmail.com>
- **Date:** 2007-06-24T23:53:51-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1182754431.099620.291300@g37g2000prf.googlegroups.com>`
- **In-Reply-To:** `<1UGfi.7159$ia2.4910@fe01.news.easynews.com>`
- **References:** `<1182489975.791804.84390@d30g2000prg.googlegroups.com> <1UGfi.7159$ia2.4910@fe01.news.easynews.com>`

```
On Jun 25, 8:46 am, "William M. Klein" <wmkl...@nospam.netcom.com>
wrote:
> There have been lots of answers that seem to ignore the fact that the OP asked
> specifically about Server Express V4 SP2.
…[92 more quoted lines elided]…
> - Show quoted text -

Yes William you are right, the compiler directive CHARSET=EBCDIC works
but the NONATIVE-FLOATING-POINT directive doesnt seem to work.
The result is that the COMP and COMP-3 data are read successfully but
still the COMP-1 and COMP-2 data remain a mystery even after the use
of NONATIVE-FLOATING-POINT.
```

###### ↳ ↳ ↳ Re: COMP-1 and COMP-2 resolution on unix (using microfocus)

- **From:** Louis Krupp <lkrupp@pssw.nospam.com.invalid>
- **Date:** 2007-06-25T01:10:31-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<137uqj8fvr2fu5f@corp.supernews.com>`
- **In-Reply-To:** `<1182754431.099620.291300@g37g2000prf.googlegroups.com>`
- **References:** `<1182489975.791804.84390@d30g2000prg.googlegroups.com> <1UGfi.7159$ia2.4910@fe01.news.easynews.com> <1182754431.099620.291300@g37g2000prf.googlegroups.com>`

```
kimi wrote:
> On Jun 25, 8:46 am, "William M. Klein" <wmkl...@nospam.netcom.com>
> wrote:
…[98 more quoted lines elided]…
> 

Possibly stupid question:  Have you set the MAINFRAME_FLOATING_POINT 
environment variable?

Louis
```

##### ↳ ↳ Re: COMP-1 and COMP-2 resolution on unix (using microfocus)

- **From:** "Roger While" <simrw@sim-basis.de>
- **Date:** 2007-06-26T18:39:47+02:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<f5rfgt$sp9$01$1@news.t-online.com>`
- **References:** `<1182489975.791804.84390@d30g2000prg.googlegroups.com> <1UGfi.7159$ia2.4910@fe01.news.easynews.com>`

```
Note that OC (0.33 current) supports S9(18)V9(18)
:-)
However, anything over the 16'th decimal is
subject to the machine implementation as shown by
the OC tests -
eg. the FUNCTION ACOS -

       IDENTIFICATION   DIVISION.
       PROGRAM-ID.      prog.
       DATA             DIVISION.
       WORKING-STORAGE  SECTION.
       01  X   PIC   S9(4)V9(4) VALUE -0.2345.
       01  Z   PIC   S9V9(17)   COMP.
       PROCEDURE        DIVISION.
           MOVE FUNCTION ACOS ( X ) TO Z.
           IF Z >= 1.80750052110824325 AND
               Z <= 1.80750052110824345
                   DISPLAY "OK"
           ELSE
                   DISPLAY Z
           END-IF.
           STOP RUN.

This applies to all POSIX systems including Win.

On the other side, an eighteen digit integer is pretty big :-)

Roger
```

###### ↳ ↳ ↳ Re: COMP-1 and COMP-2 resolution on unix (using microfocus)

- **From:** "Michael Mattias" <mmattias@talsystems.com>
- **Date:** 2007-06-26T17:39:17+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<9bcgi.6923$Rw1.6500@newssvr25.news.prodigy.net>`
- **References:** `<1182489975.791804.84390@d30g2000prg.googlegroups.com> <1UGfi.7159$ia2.4910@fe01.news.easynews.com> <f5rfgt$sp9$01$1@news.t-online.com>`

```
"Roger While" <simrw@sim-basis.de> wrote in message 
news:f5rfgt$sp9$01$1@news.t-online.com...
> Note that OC (0.33 current) supports S9(18)V9(18)
> :-)
> However, anything over the 16'th decimal is
> subject to the machine implementation as shown by
> the OC tests -

Well, if COMP-1 and COMP-2 are designed to use IEEE single and double format 
by this compiler (COMP-1 and COMP-2 being implementor-defined), of course 
that's true because there is a finite number of binary digits in the matissa 
and therefore the number of significant digits (binary or decimal) is also 
finite.

For IEEE single the number of significant decimal digits is six (6); for 
IEEE double it is sixteen (16) .

In both cases there is a LIMITED range of numbers over which the 7th 
(single) or 17th (double) decimal digit is significant.

MCM
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
