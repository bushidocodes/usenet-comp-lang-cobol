[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# The MOVE problem

_54 messages · 18 participants · 2007-10 → 2007-11_

---

### The MOVE problem

- **From:** "Roger While" <simrw@sim-basis.de>
- **Date:** 2007-10-30T17:51:19+01:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<fg7ne4$e4q$01$1@news.t-online.com>`

```
       IDENTIFICATION DIVISION.
       PROGRAM-ID. MOVEX.
       ENVIRONMENT DIVISION.
       DATA DIVISION.
       WORKING-STORAGE SECTION.
       01  AA.
           03 A PIC 9 OCCURS 9.
       01  CC.
           03 C PIC 9 OCCURS 9.
       01  B PIC 9.
       PROCEDURE DIVISION.
           MOVE "987654321" TO AA.
           MOVE "123456789" TO CC.
           MOVE 3 TO B.
           MOVE A(B) TO B C(B).
           DISPLAY CC.
           DISPLAY B.
           GOBACK.

What shouzld be displayed in various compatible modes?

Roger
```

#### ↳ Re: The MOVE problem

- **From:** Robert <no@e.mail>
- **Date:** 2007-10-30T12:46:46-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<mruei3d4q4qf84dpofamhfbja1n8gsm176@4ax.com>`
- **References:** `<fg7ne4$e4q$01$1@news.t-online.com>`

```
On Tue, 30 Oct 2007 17:51:19 +0100, "Roger While" <simrw@sim-basis.de> wrote:

>       IDENTIFICATION DIVISION.
>       PROGRAM-ID. MOVEX.
…[17 more quoted lines elided]…
>What shouzld be displayed in various compatible modes?

123456789
7
```

##### ↳ ↳ Re: The MOVE problem

- **From:** billg999@cs.uofs.edu (Bill Gunshannon)
- **Date:** 2007-10-30T18:36:06+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<5opbsmFo1aepU1@mid.individual.net>`
- **References:** `<fg7ne4$e4q$01$1@news.t-online.com> <mruei3d4q4qf84dpofamhfbja1n8gsm176@4ax.com>`

```
In article <mruei3d4q4qf84dpofamhfbja1n8gsm176@4ax.com>,
	Robert <no@e.mail> writes:
> On Tue, 30 Oct 2007 17:51:19 +0100, "Roger While" <simrw@sim-basis.de> wrote:
> 
…[22 more quoted lines elided]…
> 7

I got:

123456389
7

which is about what I expected, but I am not sure that the correct
answer isn't compiler dependant.  Does the standard address actual
order of execution for things like this?  Or side effects?

bill
```

###### ↳ ↳ ↳ Re: The MOVE problem

- **From:** "Judson McClendon" <judmc@sunvaley0.com>
- **Date:** 2007-10-30T14:02:51-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<5dLVi.57745$c9.57091@bignews8.bellsouth.net>`
- **References:** `<fg7ne4$e4q$01$1@news.t-online.com> <mruei3d4q4qf84dpofamhfbja1n8gsm176@4ax.com> <5opbsmFo1aepU1@mid.individual.net>`

```
"Bill Gunshannon" <billg999@cs.uofs.edu> wrote:
> Robert <no@e.mail> writes:
>> "Roger While" <simrw@sim-basis.de> wrote:
…[32 more quoted lines elided]…
> order of execution for things like this?  Or side effects?

Net Express 3.1:

123456789
7

I think the subscripts should properly be calculated before the MOVE,
as Net Express apparently does here.
```

###### ↳ ↳ ↳ Re: The MOVE problem

_(reply depth: 4)_

- **From:** billg999@cs.uofs.edu (Bill Gunshannon)
- **Date:** 2007-10-30T19:43:50+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<5opfrmFo3cllU1@mid.individual.net>`
- **References:** `<fg7ne4$e4q$01$1@news.t-online.com> <mruei3d4q4qf84dpofamhfbja1n8gsm176@4ax.com> <5opbsmFo1aepU1@mid.individual.net> <5dLVi.57745$c9.57091@bignews8.bellsouth.net>`

```
In article <5dLVi.57745$c9.57091@bignews8.bellsouth.net>,
	"Judson McClendon" <judmc@sunvaley0.com> writes:
> "Bill Gunshannon" <billg999@cs.uofs.edu> wrote:
>> Robert <no@e.mail> writes:
…[41 more quoted lines elided]…
> as Net Express apparently does here.

That was what I meant by my question.  Does the standard say that all
expressions shold be evaluated before the MOVE? Or shoud expressions
be evaluated as you progress thru the statement?  Or, (and not having
read the standard this is what I would have expected based on their
handling of other items) is it un-defined and therefore left up to the 
mplementor?

bill
```

###### ↳ ↳ ↳ Re: The MOVE problem

_(reply depth: 5)_

- **From:** Robert <no@e.mail>
- **Date:** 2007-10-30T18:28:25-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<ohifi3l4tascu2g72p6iina1p1jriu4pdi@4ax.com>`
- **References:** `<fg7ne4$e4q$01$1@news.t-online.com> <mruei3d4q4qf84dpofamhfbja1n8gsm176@4ax.com> <5opbsmFo1aepU1@mid.individual.net> <5dLVi.57745$c9.57091@bignews8.bellsouth.net> <5opfrmFo3cllU1@mid.individual.net>`

```
On 30 Oct 2007 19:43:50 GMT, billg999@cs.uofs.edu (Bill Gunshannon) wrote:

>In article <5dLVi.57745$c9.57091@bignews8.bellsouth.net>,
>	"Judson McClendon" <judmc@sunvaley0.com> writes:
…[50 more quoted lines elided]…
>mplementor?

The Standard says data is copied to receiving fields "in the order specified."
In other words
MOVE A(B) TO B C(B)
is the same as
MOVE A(B) TO B
MOVE A(B) TO C(B)

The same goes for arithmetics with multiple receiving items. Fujitsu gives this example:

More Than One Arithmetic Result
An arithmetic statement can contain one or more resultant identifiers (data items to
contain results). In this case, the results of an arithmetic statement are computed as
follows:
1. In a statement, all data items to be initially evaluated are computed as required.
The result is stored in a temporary data item.
2. The temporary data item obtained in (1) is computed for each resultant
identifier, and the results are stored. This computation is done in the order in
which the identifiers are specified (from left to right).
An example of obtaining more than one result is shown below. temp indicates a
temporary storage field created by the compiler.

Example 1:
ï¿½ADD a b c TO c d(c) eï¿½ is computed as follows:
ADD a b c GIVING temp
ADD temp TO c
ADD temp TO d(c)
... The value of c was changed by the preceding addition.
ADD temp TO e

Example 2:
ï¿½MULTIPLY a(i) BY i a(i)ï¿½ is computed as follows:
MOVE a(i) TO temp
MULTIPLY temp BY i
MULTIPLY temp BY a(i)
```

###### ↳ ↳ ↳ Re: The MOVE problem

_(reply depth: 6)_

- **From:** "Sergey Kashyrin" <ska@resqnet.com>
- **Date:** 2007-10-31T22:12:43-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<xCaWi.73$gC5.92251@news.sisna.com>`
- **References:** `<fg7ne4$e4q$01$1@news.t-online.com> <mruei3d4q4qf84dpofamhfbja1n8gsm176@4ax.com> <5opbsmFo1aepU1@mid.individual.net> <5dLVi.57745$c9.57091@bignews8.bellsouth.net> <5opfrmFo3cllU1@mid.individual.net> <ohifi3l4tascu2g72p6iina1p1jriu4pdi@4ax.com>`

```
Hi Roger,

I think that was a correct answer at least for IBM compatibility. Know 
anything about standards :-)

> The Standard says data is copied to receiving fields "in the order 
> specified."

At least all 390/as400 tests show the same.



"Robert" <no@e.mail> wrote in message 
news:ohifi3l4tascu2g72p6iina1p1jriu4pdi@4ax.com...
> On 30 Oct 2007 19:43:50 GMT, billg999@cs.uofs.edu (Bill Gunshannon) wrote:
>
…[94 more quoted lines elided]…
> MULTIPLY temp BY a(i)
```

###### ↳ ↳ ↳ Re: The MOVE problem

_(reply depth: 7)_

- **From:** "Sergey Kashyrin" <ska@resqnet.com>
- **Date:** 2007-10-31T23:33:14-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1ObWi.74$0B5.24601@news.sisna.com>`
- **References:** `<fg7ne4$e4q$01$1@news.t-online.com> <mruei3d4q4qf84dpofamhfbja1n8gsm176@4ax.com> <5opbsmFo1aepU1@mid.individual.net> <5dLVi.57745$c9.57091@bignews8.bellsouth.net> <5opfrmFo3cllU1@mid.individual.net> <ohifi3l4tascu2g72p6iina1p1jriu4pdi@4ax.com> <xCaWi.73$gC5.92251@news.sisna.com>`

```
> Know anything about standards :-)

That actually mean I'm zero :-G

And the original is going to "non-defined" behavior of teh C/C++ statement:

int i;
...
i = i++ + ++i + --i;
```

###### ↳ ↳ ↳ Re: The MOVE problem

_(reply depth: 8)_

- **From:** Robert <no@e.mail>
- **Date:** 2007-10-31T23:18:03-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<t7oii3lh5eurgnrp431cb2h6i0i7bp1osk@4ax.com>`
- **References:** `<fg7ne4$e4q$01$1@news.t-online.com> <mruei3d4q4qf84dpofamhfbja1n8gsm176@4ax.com> <5opbsmFo1aepU1@mid.individual.net> <5dLVi.57745$c9.57091@bignews8.bellsouth.net> <5opfrmFo3cllU1@mid.individual.net> <ohifi3l4tascu2g72p6iina1p1jriu4pdi@4ax.com> <xCaWi.73$gC5.92251@news.sisna.com> <1ObWi.74$0B5.24601@news.sisna.com>`

```
On Wed, 31 Oct 2007 23:33:14 -0400, "Sergey Kashyrin" <ska@resqnet.com> wrote:

>> Know anything about standards :-)
>
…[6 more quoted lines elided]…
>i = i++ + ++i + --i;

       0     +    1   +   0

       1++

The answer is 2
```

###### ↳ ↳ ↳ Re: The MOVE problem

_(reply depth: 9)_

- **From:** "Sergey Kashyrin" <ska@resqnet.com>
- **Date:** 2007-11-01T00:42:41-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8PcWi.85$YD5.130176@news.sisna.com>`
- **References:** `<fg7ne4$e4q$01$1@news.t-online.com> <mruei3d4q4qf84dpofamhfbja1n8gsm176@4ax.com> <5opbsmFo1aepU1@mid.individual.net> <5dLVi.57745$c9.57091@bignews8.bellsouth.net> <5opfrmFo3cllU1@mid.individual.net> <ohifi3l4tascu2g72p6iina1p1jriu4pdi@4ax.com> <xCaWi.73$gC5.92251@news.sisna.com> <1ObWi.74$0B5.24601@news.sisna.com> <t7oii3lh5eurgnrp431cb2h6i0i7bp1osk@4ax.com>`

```
>>i = i++ + ++i + --i;
>       0     +    1   +   0
>       1++
> The answer is 2

:-)))))))))))))))

ska 29> cat order.c
#include <stdio.h>

int main(int ac, char ** av) {
        int i = 0;
        i = i++ + ++i + --i;
        printf("%d\n", i);
        return 0;
}
ska 30> cc order.c
"order.c", line 5: warning #4279-D: the expression depends on order of
          evaluation
        i = i++ + ++i + --i;
            ^

ska 31> ./a.out
3

Regards
```

###### ↳ ↳ ↳ Re: The MOVE problem

_(reply depth: 10)_

- **From:** "Judson McClendon" <judmc@sunvaley0.com>
- **Date:** 2007-11-01T15:48:41-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<IYqWi.17728$u7.6839@bignews2.bellsouth.net>`
- **References:** `<fg7ne4$e4q$01$1@news.t-online.com> <mruei3d4q4qf84dpofamhfbja1n8gsm176@4ax.com> <5opbsmFo1aepU1@mid.individual.net> <5dLVi.57745$c9.57091@bignews8.bellsouth.net> <5opfrmFo3cllU1@mid.individual.net> <ohifi3l4tascu2g72p6iina1p1jriu4pdi@4ax.com> <xCaWi.73$gC5.92251@news.sisna.com> <1ObWi.74$0B5.24601@news.sisna.com> <t7oii3lh5eurgnrp431cb2h6i0i7bp1osk@4ax.com> <8PcWi.85$YD5.130176@news.sisna.com>`

```
"Sergey Kashyrin" <ska@resqnet.com> wrote:
>>>i = i++ + ++i + --i;
>>       0     +    1   +   0
…[21 more quoted lines elided]…
> 3

I don't see that there should be any ambiguity here (compiler warning).
Evaluation of arithmetic expressions should proceed left to right, within
equal precedence. That expression should always be evaluated as if it
had been written:

    step  i = ((i++ + ++i) + --i))
     1.          0                    i = 1
     2.          0  +  1              i = 2
     3.             1      +  2       i = 1
     4.   value (1+2) assigned to i   i = 3

Weird, but no ambiguity.
```

###### ↳ ↳ ↳ Re: The MOVE problem

_(reply depth: 11)_

- **From:** spambait@milmac.com (Doug Miller)
- **Date:** 2007-11-01T23:10:36+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<i9sWi.3423$%Y6.2624@nlpi061.nbdc.sbc.com>`
- **References:** `<fg7ne4$e4q$01$1@news.t-online.com> <mruei3d4q4qf84dpofamhfbja1n8gsm176@4ax.com> <5opbsmFo1aepU1@mid.individual.net> <5dLVi.57745$c9.57091@bignews8.bellsouth.net> <5opfrmFo3cllU1@mid.individual.net> <ohifi3l4tascu2g72p6iina1p1jriu4pdi@4ax.com> <xCaWi.73$gC5.92251@news.sisna.com> <1ObWi.74$0B5.24601@news.sisna.com> <t7oii3lh5eurgnrp431cb2h6i0i7bp1osk@4ax.com> <8PcWi.85$YD5.130176@news.sisna.com> <IYqWi.17728$u7.6839@bignews2.bellsouth.net>`

```
In article <IYqWi.17728$u7.6839@bignews2.bellsouth.net>, "Judson McClendon" <judmc@sunvaley0.com> wrote:
>"Sergey Kashyrin" <ska@resqnet.com> wrote:
>>>>i = i++ + ++i + --i;
…[35 more quoted lines elided]…
>Weird, but no ambiguity.

No?

Borland TurboC produces 1.
```

###### ↳ ↳ ↳ Re: The MOVE problem

_(reply depth: 12)_

- **From:** Frank Swarbrick <infocat@earthlink.net>
- **Date:** 2007-11-01T17:41:20-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<5ov6h1Foffe1U1@mid.individual.net>`
- **In-Reply-To:** `<i9sWi.3423$%Y6.2624@nlpi061.nbdc.sbc.com>`
- **References:** `<fg7ne4$e4q$01$1@news.t-online.com> <mruei3d4q4qf84dpofamhfbja1n8gsm176@4ax.com> <5opbsmFo1aepU1@mid.individual.net> <5dLVi.57745$c9.57091@bignews8.bellsouth.net> <5opfrmFo3cllU1@mid.individual.net> <ohifi3l4tascu2g72p6iina1p1jriu4pdi@4ax.com> <xCaWi.73$gC5.92251@news.sisna.com> <1ObWi.74$0B5.24601@news.sisna.com> <t7oii3lh5eurgnrp431cb2h6i0i7bp1osk@4ax.com> <8PcWi.85$YD5.130176@news.sisna.com> <IYqWi.17728$u7.6839@bignews2.bellsouth.net> <i9sWi.3423$%Y6.2624@nlpi061.nbdc.sbc.com>`

```
Doug Miller wrote:
> In article <IYqWi.17728$u7.6839@bignews2.bellsouth.net>, "Judson McClendon" <judmc@sunvaley0.com> wrote:
>> "Sergey Kashyrin" <ska@resqnet.com> wrote:
…[38 more quoted lines elided]…
> Borland TurboC produces 1.

As does MS Visual C++.

Digital Mars C++ produces 3.

Interesting...
```

###### ↳ ↳ ↳ Re: The MOVE problem

_(reply depth: 13)_

- **From:** spambait@milmac.com (Doug Miller)
- **Date:** 2007-11-02T01:09:31+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<NUtWi.9906$Pv2.8899@newssvr23.news.prodigy.net>`
- **References:** `<fg7ne4$e4q$01$1@news.t-online.com> <mruei3d4q4qf84dpofamhfbja1n8gsm176@4ax.com> <5opbsmFo1aepU1@mid.individual.net> <5dLVi.57745$c9.57091@bignews8.bellsouth.net> <5opfrmFo3cllU1@mid.individual.net> <ohifi3l4tascu2g72p6iina1p1jriu4pdi@4ax.com> <xCaWi.73$gC5.92251@news.sisna.com> <1ObWi.74$0B5.24601@news.sisna.com> <t7oii3lh5eurgnrp431cb2h6i0i7bp1osk@4ax.com> <8PcWi.85$YD5.130176@news.sisna.com> <IYqWi.17728$u7.6839@bignews2.bellsouth.net> <i9sWi.3423$%Y6.2624@nlpi061.nbdc.sbc.com> <5ov6h1Foffe1U1@mid.individual.net>`

```
In article <5ov6h1Foffe1U1@mid.individual.net>, Frank Swarbrick <infocat@earthlink.net> wrote:
>Doug Miller wrote:
>> In article <IYqWi.17728$u7.6839@bignews2.bellsouth.net>, "Judson McClendon"
…[46 more quoted lines elided]…
>Interesting...

A little bit more digging confirms what I had initially suspected: that the 
compiler's behavior is undefined, and thus permitted to be nearly anything.

http://c.ittoolbox.
com/groups/technical-functional/cpp-l/c-post-increment-operatoe-504401

Note this in particular: "any combination of ++, --, =, +=, -=, etc. in a 
single expression which causes the same object either to be modified twice or 
modified and then inspected"
```

###### ↳ ↳ ↳ Re: The MOVE problem

_(reply depth: 12)_

- **From:** Robert <no@e.mail>
- **Date:** 2007-11-01T20:28:00-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<4o2li3lt3rvt2f67nru69lqmeho20e1bl8@4ax.com>`
- **References:** `<mruei3d4q4qf84dpofamhfbja1n8gsm176@4ax.com> <5opbsmFo1aepU1@mid.individual.net> <5dLVi.57745$c9.57091@bignews8.bellsouth.net> <5opfrmFo3cllU1@mid.individual.net> <ohifi3l4tascu2g72p6iina1p1jriu4pdi@4ax.com> <xCaWi.73$gC5.92251@news.sisna.com> <1ObWi.74$0B5.24601@news.sisna.com> <t7oii3lh5eurgnrp431cb2h6i0i7bp1osk@4ax.com> <8PcWi.85$YD5.130176@news.sisna.com> <IYqWi.17728$u7.6839@bignews2.bellsouth.net> <i9sWi.3423$%Y6.2624@nlpi061.nbdc.sbc.com>`

```
On Thu, 01 Nov 2007 23:10:36 GMT, spambait@milmac.com (Doug Miller) wrote:

>In article <IYqWi.17728$u7.6839@bignews2.bellsouth.net>, "Judson McClendon" <judmc@sunvaley0.com> wrote:
>>"Sergey Kashyrin" <ska@resqnet.com> wrote:
…[40 more quoted lines elided]…
>Borland TurboC produces 1.

Ch produces -1.

http://www.softintegration.com/products/chstandard/download/
```

###### ↳ ↳ ↳ Re: The MOVE problem

_(reply depth: 13)_

- **From:** Jeff Campbell <n8wxs@arrl.net>
- **Date:** 2007-11-01T19:37:18-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1193967037_217@sp12lax.superfeed.net>`
- **In-Reply-To:** `<4o2li3lt3rvt2f67nru69lqmeho20e1bl8@4ax.com>`
- **References:** `<mruei3d4q4qf84dpofamhfbja1n8gsm176@4ax.com> <5opbsmFo1aepU1@mid.individual.net> <5dLVi.57745$c9.57091@bignews8.bellsouth.net> <5opfrmFo3cllU1@mid.individual.net> <ohifi3l4tascu2g72p6iina1p1jriu4pdi@4ax.com> <xCaWi.73$gC5.92251@news.sisna.com> <1ObWi.74$0B5.24601@news.sisna.com> <t7oii3lh5eurgnrp431cb2h6i0i7bp1osk@4ax.com> <8PcWi.85$YD5.130176@news.sisna.com> <IYqWi.17728$u7.6839@bignews2.bellsouth.net> <i9sWi.3423$%Y6.2624@nlpi061.nbdc.sbc.com> <4o2li3lt3rvt2f67nru69lqmeho20e1bl8@4ax.com>`

```
Robert wrote:
> On Thu, 01 Nov 2007 23:10:36 GMT, spambait@milmac.com (Doug Miller) wrote:
> 
…[44 more quoted lines elided]…
> 

    Welcome to OpenVMS (TM) Alpha Operating System, Version V7.3-1 on node AS600
     Last interactive login on Friday,  2-NOV-2007 01:30:29.42
     Last non-interactive login on Wednesday, 31-OCT-2007 17:25:04.82

             You have 1 new Mail message.

$ cd [.temp]
$ type a.c
#include <stdio.h>

int main(int ac, char ** av) {
     int i = 0;

     i = i++ + ++i + --i;

     printf("%d\n", i);

     return 0;
}
$ cc a

     i = i++ + ++i + --i;
....^
%CC-W-UNDEFVARMOD, In this statement, the expression "i=i+++++i+--i" modifies the variable "i" more 
than once without an intervening sequence point.  This be
havior is undefined.
at line number 6 in file SYS$SYSDEVICE:[USERS.FROG.TEMP]A.C;1

$ link a
%LINK-W-WRNERS, compilation warnings
         in module A file SYS$SYSDEVICE:[USERS.FROG.TEMP]A.OBJ;2

$ run a
2

$ logo

Jeff


----== Posted via Newsfeeds.Com - Unlimited-Unrestricted-Secure Usenet News==----
http://www.newsfeeds.com The #1 Newsgroup Service in the World! 120,000+ Newsgroups
----= East and West-Coast Server Farms - Total Privacy via Encryption =----
```

###### ↳ ↳ ↳ Re: The MOVE problem

_(reply depth: 14)_

- **From:** "billious" <billious_1954@hotmail.com>
- **Date:** 2007-11-02T14:12:44+08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<472abff1$0$12139$a82e2bb9@reader.athenanews.com>`
- **References:** `<mruei3d4q4qf84dpofamhfbja1n8gsm176@4ax.com> <5opbsmFo1aepU1@mid.individual.net> <5dLVi.57745$c9.57091@bignews8.bellsouth.net> <5opfrmFo3cllU1@mid.individual.net> <ohifi3l4tascu2g72p6iina1p1jriu4pdi@4ax.com> <xCaWi.73$gC5.92251@news.sisna.com> <1ObWi.74$0B5.24601@news.sisna.com> <t7oii3lh5eurgnrp431cb2h6i0i7bp1osk@4ax.com> <8PcWi.85$YD5.130176@news.sisna.com> <IYqWi.17728$u7.6839@bignews2.bellsouth.net> <i9sWi.3423$%Y6.2624@nlpi061.nbdc.sbc.com> <4o2li3lt3rvt2f67nru69lqmeho20e1bl8@4ax.com> <1193967037_217@sp12lax.superfeed.net>`

```

"Jeff Campbell" <n8wxs@arrl.net> wrote in message 
news:1193967037_217@sp12lax.superfeed.net...
> Robert wrote:
>> On Thu, 01 Nov 2007 23:10:36 GMT, spambait@milmac.com (Doug Miller) 
>> wrote:
>>
[snip C]

2, -1, 1, 3

no, no ambiguity anywhere in sight.

I believe that we're now awash with examples of what happens when we have a 
sloppily-written standard that leaves us all at er, C.

So what of the original point? Surely the object was to formalise MOVE 
something TO destination-list.

What happened? Powerful forces in ANSI that don't want to change their 
compilers (with the potential for altering the behaviour of existing 
processes) add the "in the order specified" clause - otherwise, it makes no 
sense.

Result? A quirk that can be exploited by those with a bent to produce 
obscure code and show how smart they are when conducting interviews.

It's disappointing that a simple standard should be manipulated for 
commercial reasons - and ANSI is the _only_ standard in my book. I don't see 
the need to bring what is to me bad logic into a standard and then insist 
that it's corect because that's what's in the rules. That is the province of 
lawyers, politicians, accountants and other minions of Evil - not 
programmers.

Worked for a mob once that insisted that DG's COBOL was THE one and only 
standard. Fifteen years after throwing away their DG machine, they're still 
writing to DG's standard - and even insisted on implementing the DG 
restrictions on their DG-emulation software. Same mob also insisted that 
MOVE SPACES to 9's-field zeroed the field - even when the destination was a 
COMP.

Titter ye not (as Frankie Howerd might say) - the "thanks, next!" argument 
is very powerful. They're still working, but I'm not....
```

###### ↳ ↳ ↳ Re: The MOVE problem

_(reply depth: 15)_

- **From:** "Judson McClendon" <judmc@sunvaley0.com>
- **Date:** 2007-11-02T06:33:24-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7WDWi.14133$a9.2577@bignews5.bellsouth.net>`
- **References:** `<mruei3d4q4qf84dpofamhfbja1n8gsm176@4ax.com> <5opbsmFo1aepU1@mid.individual.net> <5dLVi.57745$c9.57091@bignews8.bellsouth.net> <5opfrmFo3cllU1@mid.individual.net> <ohifi3l4tascu2g72p6iina1p1jriu4pdi@4ax.com> <xCaWi.73$gC5.92251@news.sisna.com> <1ObWi.74$0B5.24601@news.sisna.com> <t7oii3lh5eurgnrp431cb2h6i0i7bp1osk@4ax.com> <8PcWi.85$YD5.130176@news.sisna.com> <IYqWi.17728$u7.6839@bignews2.bellsouth.net> <i9sWi.3423$%Y6.2624@nlpi061.nbdc.sbc.com> <4o2li3lt3rvt2f67nru69lqmeho20e1bl8@4ax.com> <1193967037_217@sp12lax.superfeed.net> <472abff1$0$12139$a82e2bb9@reader.athenanews.com>`

```
"billious" <billious_1954@hotmail.com> wrote:
> "Jeff Campbell" <n8wxs@arrl.net> wrote:
>> Robert wrote:
…[6 more quoted lines elided]…
> no, no ambiguity anywhere in sight.

I didn't say there wasn't ambiguity, I said there should not be any ambiguity,
and I stand by that. Anyone implementing a C compiler that gives any other
result than 3 is a nitwit or has a bug. Compiler writers may be confused about
this, but mathematics isn't. What pre and post ++/-- do is clearly defined in
C, and all else in this example is pure mathematics, which should be THE FINAL
standard in evaluating an arithmetic expression. :-)
```

###### ↳ ↳ ↳ Re: The MOVE problem

_(reply depth: 16)_

- **From:** spambait@milmac.com (Doug Miller)
- **Date:** 2007-11-02T11:50:35+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<faEWi.2467$yV6.434@newssvr25.news.prodigy.net>`
- **References:** `<mruei3d4q4qf84dpofamhfbja1n8gsm176@4ax.com> <5opbsmFo1aepU1@mid.individual.net> <5dLVi.57745$c9.57091@bignews8.bellsouth.net> <5opfrmFo3cllU1@mid.individual.net> <ohifi3l4tascu2g72p6iina1p1jriu4pdi@4ax.com> <xCaWi.73$gC5.92251@news.sisna.com> <1ObWi.74$0B5.24601@news.sisna.com> <t7oii3lh5eurgnrp431cb2h6i0i7bp1osk@4ax.com> <8PcWi.85$YD5.130176@news.sisna.com> <IYqWi.17728$u7.6839@bignews2.bellsouth.net> <i9sWi.3423$%Y6.2624@nlpi061.nbdc.sbc.com> <4o2li3lt3rvt2f67nru69lqmeho20e1bl8@4ax.com> <1193967037_217@sp12lax.superfeed.net> <472abff1$0$12139$a82e2bb9@reader.athenanews.com> <7WDWi.14133$a9.2577@bignews5.bellsouth.net>`

```
In article <7WDWi.14133$a9.2577@bignews5.bellsouth.net>, "Judson McClendon" <judmc@sunvaley0.com> wrote:
>there wasn't ambiguity, I said there should not be any ambiguity,
>and I stand by that. Anyone implementing a C compiler that gives any other
>result than 3 is a nitwit or has a bug. 

Sorry, but that's just incorrect. C does *not* define how the compiler is 
supposed to behave in this instance.

>Compiler writers may be confused about
>this, but mathematics isn't. What pre and post ++/-- do is clearly defined in
>C, 

No, they're not -- when they're applied more than once to the same variable in 
the same statement, the resulting behavior is explicitly UNdefined.

>and all else in this example is pure mathematics, which should be THE FINAL
>standard in evaluating an arithmetic expression. :-)

OK, fine:

i = 0;
i = ... let's evaluate this expression one step at a time:
   i++    {i incremented to 1}
+ ++i   {i incremented to 2, intermediate value so far is 1 + 2 = 3}
+ --i    {i decremented to 1}
final value = 3 + 1 = 4

Pure mathematics. :-)
```

###### ↳ ↳ ↳ Re: The MOVE problem

_(reply depth: 17)_

- **From:** "Judson McClendon" <judmc@sunvaley0.com>
- **Date:** 2007-11-02T08:28:17-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<RBFWi.18108$u7.4925@bignews2.bellsouth.net>`
- **References:** `<mruei3d4q4qf84dpofamhfbja1n8gsm176@4ax.com> <5opbsmFo1aepU1@mid.individual.net> <5dLVi.57745$c9.57091@bignews8.bellsouth.net> <5opfrmFo3cllU1@mid.individual.net> <ohifi3l4tascu2g72p6iina1p1jriu4pdi@4ax.com> <xCaWi.73$gC5.92251@news.sisna.com> <1ObWi.74$0B5.24601@news.sisna.com> <t7oii3lh5eurgnrp431cb2h6i0i7bp1osk@4ax.com> <8PcWi.85$YD5.130176@news.sisna.com> <IYqWi.17728$u7.6839@bignews2.bellsouth.net> <i9sWi.3423$%Y6.2624@nlpi061.nbdc.sbc.com> <4o2li3lt3rvt2f67nru69lqmeho20e1bl8@4ax.com> <1193967037_217@sp12lax.superfeed.net> <472abff1$0$12139$a82e2bb9@reader.athenanews.com> <7WDWi.14133$a9.2577@bignews5.bellsouth.net> <faEWi.2467$yV6.434@newssvr25.news.prodigy.net>`

```
"Doug Miller" <spambait@milmac.com> wrote
> "Judson McClendon" <judmc@sunvaley0.com> wrote:
>>there wasn't ambiguity, I said there should not be any ambiguity,
…[11 more quoted lines elided]…
> the same statement, the resulting behavior is explicitly UNdefined.

What they do individually is defined, and given that, mathematics is sufficient to
define how they should act collectively. That is my point. There is simply no
reason to have ambiguity here. Use of prefix and postfix ++/-- is common in C,
specifically to address the kinds of thing that's going on here. Only the fact that
the same variable is referenced more than once in the same expression makes
this an issue, and mathematical rules of evaluation order are sufficient to make
it unambiguous. Not realizing and utilizing this is the 'nitwit' aspect.

>>and all else in this example is pure mathematics, which should be THE FINAL
>>standard in evaluating an arithmetic expression. :-)
…[10 more quoted lines elided]…
> Pure mathematics. :-)

But wrong C, because C's postfix i++ is clearly defined is presenting a value for
evaluation *before* 'i' is incremented (in fact, that's the only reason to have both
prefix and postfix ++/--). No ambiguity there. :-)
```

###### ↳ ↳ ↳ Re: The MOVE problem

_(reply depth: 18)_

- **From:** "Michael Mattias" <mmattias@talsystems.com>
- **Date:** 2007-11-02T14:33:48+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gzGWi.52156$RX.47981@newssvr11.news.prodigy.net>`
- **References:** `<mruei3d4q4qf84dpofamhfbja1n8gsm176@4ax.com> <5opbsmFo1aepU1@mid.individual.net> <5dLVi.57745$c9.57091@bignews8.bellsouth.net> <5opfrmFo3cllU1@mid.individual.net> <ohifi3l4tascu2g72p6iina1p1jriu4pdi@4ax.com> <xCaWi.73$gC5.92251@news.sisna.com> <1ObWi.74$0B5.24601@news.sisna.com> <t7oii3lh5eurgnrp431cb2h6i0i7bp1osk@4ax.com> <8PcWi.85$YD5.130176@news.sisna.com> <IYqWi.17728$u7.6839@bignews2.bellsouth.net> <i9sWi.3423$%Y6.2624@nlpi061.nbdc.sbc.com> <4o2li3lt3rvt2f67nru69lqmeho20e1bl8@4ax.com> <1193967037_217@sp12lax.superfeed.net> <472abff1$0$12139$a82e2bb9@reader.athenanews.com> <7WDWi.14133$a9.2577@bignews5.bellsouth.net> <faEWi.2467$yV6.434@newssvr25.news.prodigy.net> <RBFWi.18108$u7.4925@bignews2.bellsouth.net>`

```
"Judson McClendon" <judmc@sunvaley0.com> wrote in message 
news:RBFWi.18108$u7.4925@bignews2.bellsouth.net...> "Doug Miller" 
<spambait@milmac.com> wrote
>> "Judson McClendon" <judmc@sunvaley0.com> wrote:
>>>there wasn't ambiguity, I said there should not be any ambiguity,
>>>and I stand by that. Anyone implementing a C compiler that gives any 
>>>other
>>>result than 3 is a nitwit or has a bug.

[ removed multiple variations of physically-abused although already-deceased 
equines]

I really think those who suggested the correct response is "Don't write like 
that!" have already hit the nail on the head.

And for those who don't think so, Mr. McClendon's selection of the word 
"nitwit" is a simply outstanding use of the available English-language 
nouns.

MCM
```

###### ↳ ↳ ↳ Re: The MOVE problem

_(reply depth: 18)_

- **From:** spambait@milmac.com (Doug Miller)
- **Date:** 2007-11-02T15:38:07+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3DGWi.3956$Nz7.1856@nlpi070.nbdc.sbc.com>`
- **References:** `<mruei3d4q4qf84dpofamhfbja1n8gsm176@4ax.com> <5opbsmFo1aepU1@mid.individual.net> <5dLVi.57745$c9.57091@bignews8.bellsouth.net> <5opfrmFo3cllU1@mid.individual.net> <ohifi3l4tascu2g72p6iina1p1jriu4pdi@4ax.com> <xCaWi.73$gC5.92251@news.sisna.com> <1ObWi.74$0B5.24601@news.sisna.com> <t7oii3lh5eurgnrp431cb2h6i0i7bp1osk@4ax.com> <8PcWi.85$YD5.130176@news.sisna.com> <IYqWi.17728$u7.6839@bignews2.bellsouth.net> <i9sWi.3423$%Y6.2624@nlpi061.nbdc.sbc.com> <4o2li3lt3rvt2f67nru69lqmeho20e1bl8@4ax.com> <1193967037_217@sp12lax.superfeed.net> <472abff1$0$12139$a82e2bb9@reader.athenanews.com> <7WDWi.14133$a9.2577@bignews5.bellsouth.net> <faEWi.2467$yV6.434@newssvr25.news.prodigy.net> <RBFWi.18108$u7.4925@bignews2.bellsouth.net>`

```
In article <RBFWi.18108$u7.4925@bignews2.bellsouth.net>, "Judson McClendon" <judmc@sunvaley0.com> wrote:
>"Doug Miller" <spambait@milmac.com> wrote
>> "Judson McClendon" <judmc@sunvaley0.com> wrote:
…[16 more quoted lines elided]…
>reason to have ambiguity here. 

Of course there is: the C language does not specify the behavior. That lack of 
specification produces the ambiguity.

>Use of prefix and postfix ++/-- is common in C,
>specifically to address the kinds of thing that's going on here. Only the fact that
>the same variable is referenced more than once in the same expression makes
>this an issue,

Exactly. Under those circumstances, the behavior is explicitly undefined.

> and mathematical rules of evaluation order are sufficient to make
>it unambiguous. Not realizing and utilizing this is the 'nitwit' aspect.

That may be. However, the behavior of any language compiler is not governed by 
mathematical rules of evaluation order, but rather by the standard for that 
language -- and in this case, (a) they don't match, and (b) the standard does 
not define the expected behavior. Perhaps it should, but it doesn't, and that 
results in ambiguity.

>>>and all else in this example is pure mathematics, which should be THE FINAL
>>>standard in evaluating an arithmetic expression. :-)
…[14 more quoted lines elided]…
>prefix and postfix ++/--). No ambiguity there. :-)

Yes, there *is* an ambiguity, because C's postfix ++ does not define at 
exactly which point the increment occurs -- and the behavior is explicitly 
undefined when applied more than once to the same variable in the same 
statement.

Example:
i = 0;
i = i++ // evaluate i = 0, temp value so far = 0
 + ++i // increment i, evaluate i = 1, temp value so far = 0 + 1 = 1
 + --i // decrement i, evaluate i = 0, temp value so far = 1 + 0 = 1
 ; // temp value assigned to i (i = 1) 
// final postfix increment: i = i + 1 = 2

Point being, the standard does not specify exactly when the postfix is to be 
applied, just that it has to be after evaluation.
```

###### ↳ ↳ ↳ Re: The MOVE problem

_(reply depth: 19)_

- **From:** "Judson McClendon" <judmc@sunvaley0.com>
- **Date:** 2007-11-02T11:01:26-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<qRHWi.25446$N7.11330@bignews7.bellsouth.net>`
- **References:** `<mruei3d4q4qf84dpofamhfbja1n8gsm176@4ax.com> <5opbsmFo1aepU1@mid.individual.net> <5dLVi.57745$c9.57091@bignews8.bellsouth.net> <5opfrmFo3cllU1@mid.individual.net> <ohifi3l4tascu2g72p6iina1p1jriu4pdi@4ax.com> <xCaWi.73$gC5.92251@news.sisna.com> <1ObWi.74$0B5.24601@news.sisna.com> <t7oii3lh5eurgnrp431cb2h6i0i7bp1osk@4ax.com> <8PcWi.85$YD5.130176@news.sisna.com> <IYqWi.17728$u7.6839@bignews2.bellsouth.net> <i9sWi.3423$%Y6.2624@nlpi061.nbdc.sbc.com> <4o2li3lt3rvt2f67nru69lqmeho20e1bl8@4ax.com> <1193967037_217@sp12lax.superfeed.net> <472abff1$0$12139$a82e2bb9@reader.athenanews.com> <7WDWi.14133$a9.2577@bignews5.bellsouth.net> <faEWi.2467$yV6.434@newssvr25.news.prodigy.net> <RBFWi.18108$u7.4925@bignews2.bellsouth.net> <3DGWi.3956$Nz7.1856@nlpi070.nbdc.sbc.com>`

```
"Doug Miller" <spambait@milmac.com> wrote:
> "Judson McClendon" <judmc@sunvaley0.com> wrote:
>> and mathematical rules of evaluation order are sufficient to make
…[5 more quoted lines elided]…
> not define the expected behavior. Perhaps it should, ...

There we go. What I've been saying all along is that it should, not that it does. :-)
```

###### ↳ ↳ ↳ Re: The MOVE problem

_(reply depth: 20)_

- **From:** spambait@milmac.com (Doug Miller)
- **Date:** 2007-11-02T16:20:59+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<L7IWi.16292$lD6.3650@newssvr27.news.prodigy.net>`
- **References:** `<mruei3d4q4qf84dpofamhfbja1n8gsm176@4ax.com> <5opbsmFo1aepU1@mid.individual.net> <5dLVi.57745$c9.57091@bignews8.bellsouth.net> <5opfrmFo3cllU1@mid.individual.net> <ohifi3l4tascu2g72p6iina1p1jriu4pdi@4ax.com> <xCaWi.73$gC5.92251@news.sisna.com> <1ObWi.74$0B5.24601@news.sisna.com> <t7oii3lh5eurgnrp431cb2h6i0i7bp1osk@4ax.com> <8PcWi.85$YD5.130176@news.sisna.com> <IYqWi.17728$u7.6839@bignews2.bellsouth.net> <i9sWi.3423$%Y6.2624@nlpi061.nbdc.sbc.com> <4o2li3lt3rvt2f67nru69lqmeho20e1bl8@4ax.com> <1193967037_217@sp12lax.superfeed.net> <472abff1$0$12139$a82e2bb9@reader.athenanews.com> <7WDWi.14133$a9.2577@bignews5.bellsouth.net> <faEWi.2467$yV6.434@newssvr25.news.prodigy.net> <RBFWi.18108$u7.4925@bignews2.bellsouth.net> <3DGWi.3956$Nz7.1856@nlpi070.nbdc.sbc.com> <qRHWi.25446$N7.11330@bignews7.bellsouth.net>`

```
In article <qRHWi.25446$N7.11330@bignews7.bellsouth.net>, "Judson McClendon" <judmc@sunvaley0.com> wrote:
>"Doug Miller" <spambait@milmac.com> wrote:
>> "Judson McClendon" <judmc@sunvaley0.com> wrote:
…[9 more quoted lines elided]…
> does. :-)

But because it doesn't, the expected behavior, and hence the result of the 
operation, is ambiguous. :-)
```

###### ↳ ↳ ↳ Re: The MOVE problem

_(reply depth: 21)_

- **From:** "Judson McClendon" <judmc@sunvaley0.com>
- **Date:** 2007-11-02T11:41:52-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<krIWi.14269$a9.1030@bignews5.bellsouth.net>`
- **References:** `<mruei3d4q4qf84dpofamhfbja1n8gsm176@4ax.com> <5opbsmFo1aepU1@mid.individual.net> <5dLVi.57745$c9.57091@bignews8.bellsouth.net> <5opfrmFo3cllU1@mid.individual.net> <ohifi3l4tascu2g72p6iina1p1jriu4pdi@4ax.com> <xCaWi.73$gC5.92251@news.sisna.com> <1ObWi.74$0B5.24601@news.sisna.com> <t7oii3lh5eurgnrp431cb2h6i0i7bp1osk@4ax.com> <8PcWi.85$YD5.130176@news.sisna.com> <IYqWi.17728$u7.6839@bignews2.bellsouth.net> <i9sWi.3423$%Y6.2624@nlpi061.nbdc.sbc.com> <4o2li3lt3rvt2f67nru69lqmeho20e1bl8@4ax.com> <1193967037_217@sp12lax.superfeed.net> <472abff1$0$12139$a82e2bb9@reader.athenanews.com> <7WDWi.14133$a9.2577@bignews5.bellsouth.net> <faEWi.2467$yV6.434@newssvr25.news.prodigy.net> <RBFWi.18108$u7.4925@bignews2.bellsouth.net> <3DGWi.3956$Nz7.1856@nlpi070.nbdc.sbc.com> <qRHWi.25446$N7.11330@bignews7.bellsouth.net> <L7IWi.16292$lD6.3650@newssvr27.news.prodigy.net>`

```
"Doug Miller" <spambait@milmac.com> wrote:
> "Judson McClendon" <judmc@sunvaley0.com> wrote:
>>"Doug Miller" <spambait@milmac.com> wrote:
…[13 more quoted lines elided]…
> operation, is ambiguous. :-)

Is this a Pete & Repeat scenario? :-)
```

###### ↳ ↳ ↳ Re: The MOVE problem

_(reply depth: 15)_

- **From:** Howard Brazee <howard@brazee.net>
- **Date:** 2007-11-02T09:11:20-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<defmi35g65lcvhp0n6ihf7sf61usg52vf4@4ax.com>`
- **References:** `<5opfrmFo3cllU1@mid.individual.net> <ohifi3l4tascu2g72p6iina1p1jriu4pdi@4ax.com> <xCaWi.73$gC5.92251@news.sisna.com> <1ObWi.74$0B5.24601@news.sisna.com> <t7oii3lh5eurgnrp431cb2h6i0i7bp1osk@4ax.com> <8PcWi.85$YD5.130176@news.sisna.com> <IYqWi.17728$u7.6839@bignews2.bellsouth.net> <i9sWi.3423$%Y6.2624@nlpi061.nbdc.sbc.com> <4o2li3lt3rvt2f67nru69lqmeho20e1bl8@4ax.com> <1193967037_217@sp12lax.superfeed.net> <472abff1$0$12139$a82e2bb9@reader.athenanews.com>`

```
On Fri, 2 Nov 2007 14:12:44 +0800, "billious"
<billious_1954@hotmail.com> wrote:

>2, -1, 1, 3
>
…[3 more quoted lines elided]…
>sloppily-written standard that leaves us all at er, C.

The evidence supports your statement.   But in the absence of a
defined C standard, shouldn't the common standard used everywhere else
apply?
```

###### ↳ ↳ ↳ Re: The MOVE problem

_(reply depth: 12)_

- **From:** "Judson McClendon" <judmc@sunvaley0.com>
- **Date:** 2007-11-02T06:20:37-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<9KDWi.14128$a9.8721@bignews5.bellsouth.net>`
- **References:** `<fg7ne4$e4q$01$1@news.t-online.com> <mruei3d4q4qf84dpofamhfbja1n8gsm176@4ax.com> <5opbsmFo1aepU1@mid.individual.net> <5dLVi.57745$c9.57091@bignews8.bellsouth.net> <5opfrmFo3cllU1@mid.individual.net> <ohifi3l4tascu2g72p6iina1p1jriu4pdi@4ax.com> <xCaWi.73$gC5.92251@news.sisna.com> <1ObWi.74$0B5.24601@news.sisna.com> <t7oii3lh5eurgnrp431cb2h6i0i7bp1osk@4ax.com> <8PcWi.85$YD5.130176@news.sisna.com> <IYqWi.17728$u7.6839@bignews2.bellsouth.net> <i9sWi.3423$%Y6.2624@nlpi061.nbdc.sbc.com>`

```
"Doug Miller" <spambait@milmac.com> wrote:
> "Judson McClendon" <judmc@sunvaley0.com> wrote:
>>"Sergey Kashyrin" <ska@resqnet.com> wrote:
…[40 more quoted lines elided]…
> Borland TurboC produces 1.

So? There still *shouldn't* (active word) be any ambiguity. :-)
```

###### ↳ ↳ ↳ Re: The MOVE problem

_(reply depth: 11)_

- **From:** "Charles Hottel" <chottel@earthlink.net>
- **Date:** 2007-11-02T21:53:06-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<13inl3v5i4sqf11@corp.supernews.com>`
- **References:** `<fg7ne4$e4q$01$1@news.t-online.com> <mruei3d4q4qf84dpofamhfbja1n8gsm176@4ax.com> <5opbsmFo1aepU1@mid.individual.net> <5dLVi.57745$c9.57091@bignews8.bellsouth.net> <5opfrmFo3cllU1@mid.individual.net> <ohifi3l4tascu2g72p6iina1p1jriu4pdi@4ax.com> <xCaWi.73$gC5.92251@news.sisna.com> <1ObWi.74$0B5.24601@news.sisna.com> <t7oii3lh5eurgnrp431cb2h6i0i7bp1osk@4ax.com> <8PcWi.85$YD5.130176@news.sisna.com> <IYqWi.17728$u7.6839@bignews2.bellsouth.net>`

```

"Judson McClendon" <judmc@sunvaley0.com> wrote in message 
news:IYqWi.17728$u7.6839@bignews2.bellsouth.net...
> "Sergey Kashyrin" <ska@resqnet.com> wrote:
>>>>i = i++ + ++i + --i;
…[28 more quoted lines elided]…
>
I don't think that is true for C, without explicit parentheses the compiler 
can do them in any order it chooses.
```

###### ↳ ↳ ↳ Re: The MOVE problem

_(reply depth: 12)_

- **From:** "Sergey Kashyrin" <ska@resqnet.com>
- **Date:** 2007-11-03T00:15:03-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<eBSWi.71$tV1.41001@news.sisna.com>`
- **References:** `<fg7ne4$e4q$01$1@news.t-online.com> <mruei3d4q4qf84dpofamhfbja1n8gsm176@4ax.com> <5opbsmFo1aepU1@mid.individual.net> <5dLVi.57745$c9.57091@bignews8.bellsouth.net> <5opfrmFo3cllU1@mid.individual.net> <ohifi3l4tascu2g72p6iina1p1jriu4pdi@4ax.com> <xCaWi.73$gC5.92251@news.sisna.com> <1ObWi.74$0B5.24601@news.sisna.com> <t7oii3lh5eurgnrp431cb2h6i0i7bp1osk@4ax.com> <8PcWi.85$YD5.130176@news.sisna.com> <IYqWi.17728$u7.6839@bignews2.bellsouth.net> <13inl3v5i4sqf11@corp.supernews.com>`

```

"Charles Hottel" <chottel@earthlink.net> wrote in message 
news:13inl3v5i4sqf11@corp.supernews.com...
>
> "Judson McClendon" <judmc@sunvaley0.com> wrote in message 
…[12 more quoted lines elided]…
> compiler can do them in any order it chooses.

It's already been correctly said that it's a time of postfix "++" operation 
which is undefined and parentheses will not help.
The same as undefined
int i = 1;
i = f(++i, ++i);

because the order of parametes calculation is undefined.
```

###### ↳ ↳ ↳ Re: The MOVE problem

_(reply depth: 13)_

- **From:** "Judson McClendon" <judmc@sunvaley0.com>
- **Date:** 2007-11-03T04:28:45-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<hbXWi.60804$c9.50981@bignews8.bellsouth.net>`
- **References:** `<fg7ne4$e4q$01$1@news.t-online.com> <mruei3d4q4qf84dpofamhfbja1n8gsm176@4ax.com> <5opbsmFo1aepU1@mid.individual.net> <5dLVi.57745$c9.57091@bignews8.bellsouth.net> <5opfrmFo3cllU1@mid.individual.net> <ohifi3l4tascu2g72p6iina1p1jriu4pdi@4ax.com> <xCaWi.73$gC5.92251@news.sisna.com> <1ObWi.74$0B5.24601@news.sisna.com> <t7oii3lh5eurgnrp431cb2h6i0i7bp1osk@4ax.com> <8PcWi.85$YD5.130176@news.sisna.com> <IYqWi.17728$u7.6839@bignews2.bellsouth.net> <13inl3v5i4sqf11@corp.supernews.com> <eBSWi.71$tV1.41001@news.sisna.com>`

```
"Sergey Kashyrin" <ska@resqnet.com> wrote:
> "Charles Hottel" <chottel@earthlink.net> wrote:
>> "Judson McClendon" <judmc@sunvaley0.com> wrote:
…[16 more quoted lines elided]…
> because the order of parametes calculation is undefined.

Which was unnecessary and mind-bogglingly stupid. It *should* have been
defined; that is my point. It is an incredibly sloppy design flaw, one of many
in C (e.g. =/== seems almost purposely designed to be visually confused).

And parenthesis *should* help, because they define the order of evaluation
in every mathematical expression written for thousands of years. For what
conceivable reason would the creators of C ignore such a thing? As I said,
it was unnecessary and mind-bogglingly stupid.
```

###### ↳ ↳ ↳ Re: The MOVE problem

_(reply depth: 14)_

- **From:** Robert <no@e.mail>
- **Date:** 2007-11-03T11:02:34-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<588pi3128qfd7jtq07jt0cbpnlfgmsfaag@4ax.com>`
- **References:** `<5opbsmFo1aepU1@mid.individual.net> <5dLVi.57745$c9.57091@bignews8.bellsouth.net> <5opfrmFo3cllU1@mid.individual.net> <ohifi3l4tascu2g72p6iina1p1jriu4pdi@4ax.com> <xCaWi.73$gC5.92251@news.sisna.com> <1ObWi.74$0B5.24601@news.sisna.com> <t7oii3lh5eurgnrp431cb2h6i0i7bp1osk@4ax.com> <8PcWi.85$YD5.130176@news.sisna.com> <IYqWi.17728$u7.6839@bignews2.bellsouth.net> <13inl3v5i4sqf11@corp.supernews.com> <eBSWi.71$tV1.41001@news.sisna.com> <hbXWi.60804$c9.50981@bignews8.bellsouth.net>`

```
On Sat, 3 Nov 2007 04:28:45 -0500, "Judson McClendon" <judmc@sunvaley0.com> wrote:

>"Sergey Kashyrin" <ska@resqnet.com> wrote:
>> "Charles Hottel" <chottel@earthlink.net> wrote:
…[26 more quoted lines elided]…
>it was unnecessary and mind-bogglingly stupid.

Programming Standards are written by programmers, not mathematicians.

This reminds me of a conversation I had with the manager of testing at a federal
government department.

rw: How do you determine the number of test cases required?
mt: That's determined by the budget.
rw: Did you ever take Statistics 101?
mt: Yeah. It was irrelevant crap I've never used in the real world.
rw: Do you remember probability of false positive and false negative.
mt: Sure, alpha and beta. How's that related to software testing?
rw: When you run a regression test, you're looking for a negative finding. 
      Most other tests are positive.
mt: Ah, negative .. positive. It's all the same. You sound like a professor.
rw: It's not all the same. Regression testing requires thousands of test cases; positive 
      rests require a small number of cases.
mt: All our tests are positive. If they're not, we write 'em up as failures.
rw: What's your confidence interval?
mt: We try for 100%.
rw: Your test design is really sophisticated. 
mt: Thank you.
```

###### ↳ ↳ ↳ Re: The MOVE problem

_(reply depth: 15)_

- **From:** Howard Brazee <howard@brazee.net>
- **Date:** 2007-11-05T11:45:22-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<0foui39fhjgrk6jvcl96ppkmvf44m5khr3@4ax.com>`
- **References:** `<5opfrmFo3cllU1@mid.individual.net> <ohifi3l4tascu2g72p6iina1p1jriu4pdi@4ax.com> <xCaWi.73$gC5.92251@news.sisna.com> <1ObWi.74$0B5.24601@news.sisna.com> <t7oii3lh5eurgnrp431cb2h6i0i7bp1osk@4ax.com> <8PcWi.85$YD5.130176@news.sisna.com> <IYqWi.17728$u7.6839@bignews2.bellsouth.net> <13inl3v5i4sqf11@corp.supernews.com> <eBSWi.71$tV1.41001@news.sisna.com> <hbXWi.60804$c9.50981@bignews8.bellsouth.net> <588pi3128qfd7jtq07jt0cbpnlfgmsfaag@4ax.com>`

```
On Sat, 03 Nov 2007 11:02:34 -0600, Robert <no@e.mail> wrote:

>rw: How do you determine the number of test cases required?
>mt: That's determined by the budget.
…[13 more quoted lines elided]…
>mt: Thank you.

LOL!

Workers have a bit of the fault that we see so often with politicians.
We do what rewards us and avoid what hurts us.    It is real hard to
run a company, a country, or a project so that we see what we need to
see instead of what we want to see.    Those running them need well
defined criteria - but how many managers even understand statistical
analysis?
```

###### ↳ ↳ ↳ Re: The MOVE problem

_(reply depth: 16)_

- **From:** John Reagan <john.reagan@hp.com>
- **Date:** 2007-11-05T16:41:19-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<fgo2r8$fft$1@usenet01.boi.hp.com>`
- **In-Reply-To:** `<0foui39fhjgrk6jvcl96ppkmvf44m5khr3@4ax.com>`
- **References:** `<5opfrmFo3cllU1@mid.individual.net> <ohifi3l4tascu2g72p6iina1p1jriu4pdi@4ax.com> <xCaWi.73$gC5.92251@news.sisna.com> <1ObWi.74$0B5.24601@news.sisna.com> <t7oii3lh5eurgnrp431cb2h6i0i7bp1osk@4ax.com> <8PcWi.85$YD5.130176@news.sisna.com> <IYqWi.17728$u7.6839@bignews2.bellsouth.net> <13inl3v5i4sqf11@corp.supernews.com> <eBSWi.71$tV1.41001@news.sisna.com> <hbXWi.60804$c9.50981@bignews8.bellsouth.net> <588pi3128qfd7jtq07jt0cbpnlfgmsfaag@4ax.com> <0foui39fhjgrk6jvcl96ppkmvf44m5khr3@4ax.com>`

```
As a compiler writer and standards member (X3J9 - Pascal), I want to 
point out the difference between order of evaluation and operand precedence.

There has been lots of discussion on whether parens would help or not.

For statements like:

i = (a + b) + (c + d);

the parens tell the compiler how to associate the operands of the 
various binary addition operators.  It doesn't tell the compiler in what 
order to do many of the operations.  It could add "c" to "d" before 
adding "a" to "b".  It could do them all in parallel if the hardware 
supported such a concept.  I've had customers confused by this subtly 
over the years.

When "a", "b", "c", and "d" are large complex operands, the compiler can 
  often generate better code evaluating the operands in different orders 
than "a" then "b" then "add" then "c" then "d" then "add" then "add". 
Might want to do the most complicated first or perhaps there might be 
some common sub-expression shared between each operand.
```

###### ↳ ↳ ↳ Re: The MOVE problem

_(reply depth: 16)_

- **From:** Robert <no@e.mail>
- **Date:** 2007-11-05T22:14:09-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<s6qvi3dqbv1kccij0unkm40dnni8cdi3fd@4ax.com>`
- **References:** `<ohifi3l4tascu2g72p6iina1p1jriu4pdi@4ax.com> <xCaWi.73$gC5.92251@news.sisna.com> <1ObWi.74$0B5.24601@news.sisna.com> <t7oii3lh5eurgnrp431cb2h6i0i7bp1osk@4ax.com> <8PcWi.85$YD5.130176@news.sisna.com> <IYqWi.17728$u7.6839@bignews2.bellsouth.net> <13inl3v5i4sqf11@corp.supernews.com> <eBSWi.71$tV1.41001@news.sisna.com> <hbXWi.60804$c9.50981@bignews8.bellsouth.net> <588pi3128qfd7jtq07jt0cbpnlfgmsfaag@4ax.com> <0foui39fhjgrk6jvcl96ppkmvf44m5khr3@4ax.com>`

```
On Mon, 05 Nov 2007 11:45:22 -0700, Howard Brazee <howard@brazee.net> wrote:

>On Sat, 03 Nov 2007 11:02:34 -0600, Robert <no@e.mail> wrote:
>
…[24 more quoted lines elided]…
>analysis?

Those who program well think the key to success is code inspection.

Those who program poorly think the key to success is testing.

Managers who don't program think the key to success is process. 

Analysts think the key to success is design. 

In short, everyone thinks the key to success is what (s)he is good at or likes doing.

Therefore, your priorities reveal how you see yourself.
```

###### ↳ ↳ ↳ Re: The MOVE problem

_(reply depth: 14)_

- **From:** "Charles Hottel" <chottel@earthlink.net>
- **Date:** 2007-11-03T16:17:08-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<13iplpvatnlda19@corp.supernews.com>`
- **References:** `<fg7ne4$e4q$01$1@news.t-online.com> <mruei3d4q4qf84dpofamhfbja1n8gsm176@4ax.com> <5opbsmFo1aepU1@mid.individual.net> <5dLVi.57745$c9.57091@bignews8.bellsouth.net> <5opfrmFo3cllU1@mid.individual.net> <ohifi3l4tascu2g72p6iina1p1jriu4pdi@4ax.com> <xCaWi.73$gC5.92251@news.sisna.com> <1ObWi.74$0B5.24601@news.sisna.com> <t7oii3lh5eurgnrp431cb2h6i0i7bp1osk@4ax.com> <8PcWi.85$YD5.130176@news.sisna.com> <IYqWi.17728$u7.6839@bignews2.bellsouth.net> <13inl3v5i4sqf11@corp.supernews.com> <eBSWi.71$tV1.41001@news.sisna.com> <hbXWi.60804$c9.50981@bignews8.bellsouth.net>`

```

"Judson McClendon" <judmc@sunvaley0.com> wrote in message 
news:hbXWi.60804$c9.50981@bignews8.bellsouth.net...
> "Sergey Kashyrin" <ska@resqnet.com> wrote:
>> "Charles Hottel" <chottel@earthlink.net> wrote:
…[37 more quoted lines elided]…
>

I think this was one of those  things done in the name of efficiency.
```

###### ↳ ↳ ↳ Re: The MOVE problem

_(reply depth: 15)_

- **From:** "Rick Smith" <ricksmith@mfi.net>
- **Date:** 2007-11-05T10:46:24-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<13iuesbhfi65h82@corp.supernews.com>`
- **References:** `<fg7ne4$e4q$01$1@news.t-online.com> <mruei3d4q4qf84dpofamhfbja1n8gsm176@4ax.com> <5opbsmFo1aepU1@mid.individual.net> <5dLVi.57745$c9.57091@bignews8.bellsouth.net> <5opfrmFo3cllU1@mid.individual.net> <ohifi3l4tascu2g72p6iina1p1jriu4pdi@4ax.com> <xCaWi.73$gC5.92251@news.sisna.com> <1ObWi.74$0B5.24601@news.sisna.com> <t7oii3lh5eurgnrp431cb2h6i0i7bp1osk@4ax.com> <8PcWi.85$YD5.130176@news.sisna.com> <IYqWi.17728$u7.6839@bignews2.bellsouth.net> <13inl3v5i4sqf11@corp.supernews.com> <eBSWi.71$tV1.41001@news.sisna.com> <hbXWi.60804$c9.50981@bignews8.bellsouth.net> <13iplpvatnlda19@corp.supernews.com>`

```

"Charles Hottel" <chottel@earthlink.net> wrote in message
news:13iplpvatnlda19@corp.supernews.com...
>
> "Judson McClendon" <judmc@sunvaley0.com> wrote in message
…[5 more quoted lines elided]…
> >>>>> "order.c", line 5: warning #4279-D: the expression depends on order
of
> >>>>> evaluation
> >>>>>        i = i++ + ++i + --i;
> >>>>>            ^
> >>>> I don't see that there should be any ambiguity here (compiler
warning).
> >>>> Evaluation of arithmetic expressions should proceed left to right,
> >>>> within
…[15 more quoted lines elided]…
> > defined; that is my point. It is an incredibly sloppy design flaw, one
of
> > many
> > in C (e.g. =/== seems almost purposely designed to be visually
confused).
> >
> > And parenthesis *should* help, because they define the order of
evaluation
> > in every mathematical expression written for thousands of years. For
what
> > conceivable reason would the creators of C ignore such a thing? As I
said,
> > it was unnecessary and mind-bogglingly stupid.
>
> I think this was one of those  things done in the name of efficiency.


Whether for efficiency or to eliminate ambiguity, this is the rule.

ISO/IEC 9899:TC2 - Programming languages -- C
6.5 Expressions
-----
2. Between the previous and next sequence point an object
shall have its stored value modified at most once by the
evaluation of an expression. Furthermore, the prior value
shall be read only to determine the value to be stored.[71]
---
71) This paragraph renders undefined statement expressions
such as

    i = ++i + 1;
    a[i++] = i;

while allowing

    i = i + 1;
    a[i] = i;
-----
```

###### ↳ ↳ ↳ Re: The MOVE problem

_(reply depth: 14)_

- **From:** Howard Brazee <howard@brazee.net>
- **Date:** 2007-11-05T11:32:04-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<h9oui3pmf7063m3egcp4gsogs5tcrqpcmh@4ax.com>`
- **References:** `<5opbsmFo1aepU1@mid.individual.net> <5dLVi.57745$c9.57091@bignews8.bellsouth.net> <5opfrmFo3cllU1@mid.individual.net> <ohifi3l4tascu2g72p6iina1p1jriu4pdi@4ax.com> <xCaWi.73$gC5.92251@news.sisna.com> <1ObWi.74$0B5.24601@news.sisna.com> <t7oii3lh5eurgnrp431cb2h6i0i7bp1osk@4ax.com> <8PcWi.85$YD5.130176@news.sisna.com> <IYqWi.17728$u7.6839@bignews2.bellsouth.net> <13inl3v5i4sqf11@corp.supernews.com> <eBSWi.71$tV1.41001@news.sisna.com> <hbXWi.60804$c9.50981@bignews8.bellsouth.net>`

```
On Sat, 3 Nov 2007 04:28:45 -0500, "Judson McClendon"
<judmc@sunvaley0.com> wrote:

>And parenthesis *should* help, because they define the order of evaluation
>in every mathematical expression written for thousands of years. For what
>conceivable reason would the creators of C ignore such a thing? As I said,
>it was unnecessary and mind-bogglingly stupid.

It's easy to skip the obvious.   After all, anybody with half a brain
will realize that the standards that we have been using for such a
long time are the defaults.

Unfortunately, it appears that some compiler writers don't have half a
brain.
```

###### ↳ ↳ ↳ Re: The MOVE problem

_(reply depth: 15)_

- **From:** "billious" <billious_1954@hotmail.com>
- **Date:** 2007-11-06T12:04:20+08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<472fe852$0$12165$a82e2bb9@reader.athenanews.com>`
- **References:** `<5opbsmFo1aepU1@mid.individual.net> <5dLVi.57745$c9.57091@bignews8.bellsouth.net> <5opfrmFo3cllU1@mid.individual.net> <ohifi3l4tascu2g72p6iina1p1jriu4pdi@4ax.com> <xCaWi.73$gC5.92251@news.sisna.com> <1ObWi.74$0B5.24601@news.sisna.com> <t7oii3lh5eurgnrp431cb2h6i0i7bp1osk@4ax.com> <8PcWi.85$YD5.130176@news.sisna.com> <IYqWi.17728$u7.6839@bignews2.bellsouth.net> <13inl3v5i4sqf11@corp.supernews.com> <eBSWi.71$tV1.41001@news.sisna.com> <hbXWi.60804$c9.50981@bignews8.bellsouth.net> <h9oui3pmf7063m3egcp4gsogs5tcrqpcmh@4ax.com>`

```

"Howard Brazee" <howard@brazee.net> wrote in message 
news:h9oui3pmf7063m3egcp4gsogs5tcrqpcmh@4ax.com...
> On Sat, 3 Nov 2007 04:28:45 -0500, "Judson McClendon"
> <judmc@sunvaley0.com> wrote:
…[11 more quoted lines elided]…
> brain.

Hmmm... so your first recommendation for a case of tuberculosis would be a 
good leeching, no doubt?

Maintaining a standard that was badly implemented in the first instance 
simply to maintain the legitimacy of that original implementation would seem 
to be the province of said half-brained legions.

My experience is that those that are most incompetent are those that reach 
first for the standards documentation.
```

###### ↳ ↳ ↳ Re: The MOVE problem

_(reply depth: 16)_

- **From:** Howard Brazee <howard@brazee.net>
- **Date:** 2007-11-06T09:48:26-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<4g61j39dlljnhpna0ijjupuvmlop5ebhtc@4ax.com>`
- **References:** `<ohifi3l4tascu2g72p6iina1p1jriu4pdi@4ax.com> <xCaWi.73$gC5.92251@news.sisna.com> <1ObWi.74$0B5.24601@news.sisna.com> <t7oii3lh5eurgnrp431cb2h6i0i7bp1osk@4ax.com> <8PcWi.85$YD5.130176@news.sisna.com> <IYqWi.17728$u7.6839@bignews2.bellsouth.net> <13inl3v5i4sqf11@corp.supernews.com> <eBSWi.71$tV1.41001@news.sisna.com> <hbXWi.60804$c9.50981@bignews8.bellsouth.net> <h9oui3pmf7063m3egcp4gsogs5tcrqpcmh@4ax.com> <472fe852$0$12165$a82e2bb9@reader.athenanews.com>`

```
On Tue, 6 Nov 2007 12:04:20 +0800, "billious"
<billious_1954@hotmail.com> wrote:

>> It's easy to skip the obvious.   After all, anybody with half a brain
>> will realize that the standards that we have been using for such a
…[6 more quoted lines elided]…
>good leeching, no doubt?

Talk about leaping to conclusions. 

A compiler has to have predictable results.   Undefined doesn't cut
it.   

>Maintaining a standard that was badly implemented in the first instance 
>simply to maintain the legitimacy of that original implementation would seem 
>to be the province of said half-brained legions.

So you don't like the default standard that has been used in math and
science.   That's fine - as long as there is a new standard to replace
it.  

>My experience is that those that are most incompetent are those that reach 
>first for the standards documentation.

I haven't had experience writing compilers.   On this forum, I have
seen quite a bit of evidence that the most competent are those who
know the standards the best.
```

###### ↳ ↳ ↳ Re: The MOVE problem

_(reply depth: 13)_

- **From:** "Charles Hottel" <chottel@earthlink.net>
- **Date:** 2007-11-03T16:16:09-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<13iplo4md92cs06@corp.supernews.com>`
- **References:** `<fg7ne4$e4q$01$1@news.t-online.com> <mruei3d4q4qf84dpofamhfbja1n8gsm176@4ax.com> <5opbsmFo1aepU1@mid.individual.net> <5dLVi.57745$c9.57091@bignews8.bellsouth.net> <5opfrmFo3cllU1@mid.individual.net> <ohifi3l4tascu2g72p6iina1p1jriu4pdi@4ax.com> <xCaWi.73$gC5.92251@news.sisna.com> <1ObWi.74$0B5.24601@news.sisna.com> <t7oii3lh5eurgnrp431cb2h6i0i7bp1osk@4ax.com> <8PcWi.85$YD5.130176@news.sisna.com> <IYqWi.17728$u7.6839@bignews2.bellsouth.net> <13inl3v5i4sqf11@corp.supernews.com> <eBSWi.71$tV1.41001@news.sisna.com>`

```

"Sergey Kashyrin" <ska@resqnet.com> wrote in message 
news:eBSWi.71$tV1.41001@news.sisna.com...
>
> "Charles Hottel" <chottel@earthlink.net> wrote in message 
…[28 more quoted lines elided]…
>

Ok. Yes I did not mean that adding parenthesis would help in this case.
```

###### ↳ ↳ ↳ Re: The MOVE problem

_(reply depth: 12)_

- **From:** Howard Brazee <howard@brazee.net>
- **Date:** 2007-11-05T11:29:22-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<g0oui35cm3lg0b14erkh8jnfhpgc81flkp@4ax.com>`
- **References:** `<fg7ne4$e4q$01$1@news.t-online.com> <mruei3d4q4qf84dpofamhfbja1n8gsm176@4ax.com> <5opbsmFo1aepU1@mid.individual.net> <5dLVi.57745$c9.57091@bignews8.bellsouth.net> <5opfrmFo3cllU1@mid.individual.net> <ohifi3l4tascu2g72p6iina1p1jriu4pdi@4ax.com> <xCaWi.73$gC5.92251@news.sisna.com> <1ObWi.74$0B5.24601@news.sisna.com> <t7oii3lh5eurgnrp431cb2h6i0i7bp1osk@4ax.com> <8PcWi.85$YD5.130176@news.sisna.com> <IYqWi.17728$u7.6839@bignews2.bellsouth.net> <13inl3v5i4sqf11@corp.supernews.com>`

```
On Fri, 2 Nov 2007 21:53:06 -0400, "Charles Hottel"
<chottel@earthlink.net> wrote:

>> I don't see that there should be any ambiguity here (compiler warning).
>> Evaluation of arithmetic expressions should proceed left to right, within
…[4 more quoted lines elided]…
>can do them in any order it chooses. 

I think that *is* true for C - That is the way it *should* work. (Note
the above quote specifically said "should" - twice).

Unfortunately we have to live in the world the way it is instead of
the way it should be.

No computer language should give a compiler to choose what results an
arithmetic expression should resolve to.
```

#### ↳ Re: The MOVE problem

- **From:** "William M. Klein" <wmklein@nospam.netcom.com>
- **Date:** 2007-10-30T22:30:38+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<cgOVi.218417$m81.218277@fe01.news.easynews.com>`
- **References:** `<fg7ne4$e4q$01$1@news.t-online.com>`

```
The standard requires subscripts of the sending item o be evaluated once at the 
beginning of execution of the statement and of the receiving item immediately 
before it gets its data.  Pages 478-479 of the '02 Standard has:

   ***

Item identification for identifier-2 is performed immediately before the data is 
moved to the respective data tem. If identifier-2 is a zero-length item, the 
MOVE statement leaves identifier-2 unchanged.

If identifier-1 is reference modified, subscripted, or is a function-identifier, 
the reference modifier, subscript, or function-identifier is evaluated only 
once, immediately before data is moved to the first of the receiving operands.
    ...

The result of the statement

MOVE a (b) TO b, c (b)

is equivalent to:

MOVE a (b) TO temp
MOVE temp TO b
MOVE temp to c (b)

where 'temp' is an intermediate result item provided by the implementor


    ***

Now having said that,  the concept of "item identification" was new in the '02 
Standard (as I recall) and although this EXACT same "smple" appears in the '85 
Standard (with the "temp" data item), my memory is that many (most?) compilers 
use "temp" as the subscript for the receiving item.

Page VI-103 of the '85 Standard had the rule

 "Any length evaluation or subscripting associated with identifier-2 is 
evaluated immediately before the data is moved to the respective data item."

and then has exaclty the example given above.
```

##### ↳ ↳ Re: The MOVE problem

- **From:** "Judson McClendon" <judmc@sunvaley0.com>
- **Date:** 2007-10-31T06:14:58-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<ssZVi.44717$b9.24845@bignews1.bellsouth.net>`
- **References:** `<fg7ne4$e4q$01$1@news.t-online.com> <cgOVi.218417$m81.218277@fe01.news.easynews.com>`

```
Thanks Bill, I thought you would come back with a definitive response. :-)

>           MOVE A(B) TO B C(B).

I would never consider writing such code as in this example. Code should
be written to be as simple and easy to understand as possible, and this
example violates that principle. Using two statements would make the intent
obvious.
```

###### ↳ ↳ ↳ Re: The MOVE problem

- **From:** spambait@milmac.com (Doug Miller)
- **Date:** 2007-10-31T11:58:57+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<56_Vi.15993$lD6.14460@newssvr27.news.prodigy.net>`
- **References:** `<fg7ne4$e4q$01$1@news.t-online.com> <cgOVi.218417$m81.218277@fe01.news.easynews.com> <ssZVi.44717$b9.24845@bignews1.bellsouth.net>`

```
In article <ssZVi.44717$b9.24845@bignews1.bellsouth.net>, "Judson McClendon" <judmc@sunvaley0.com> wrote:
>Thanks Bill, I thought you would come back with a definitive response. :-)
>
…[5 more quoted lines elided]…
>obvious.

DING DING DING! We have a winner, ladies and gentlemen! *That* is the correct 
answer.
```

###### ↳ ↳ ↳ Re: The MOVE problem

_(reply depth: 4)_

- **From:** billg999@cs.uofs.edu (Bill Gunshannon)
- **Date:** 2007-10-31T12:26:49+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<5orak9Fo6n6dU2@mid.individual.net>`
- **References:** `<fg7ne4$e4q$01$1@news.t-online.com> <cgOVi.218417$m81.218277@fe01.news.easynews.com> <ssZVi.44717$b9.24845@bignews1.bellsouth.net> <56_Vi.15993$lD6.14460@newssvr27.news.prodigy.net>`

```
In article <56_Vi.15993$lD6.14460@newssvr27.news.prodigy.net>,
	spambait@milmac.com (Doug Miller) writes:
> In article <ssZVi.44717$b9.24845@bignews1.bellsouth.net>, "Judson McClendon" <judmc@sunvaley0.com> wrote:
>>Thanks Bill, I thought you would come back with a definitive response. :-)
…[9 more quoted lines elided]…
> answer.

Undoubtedly!!  I have spent many an hour trying to get that point
across to some of the faculty here regarding code they let students
write, in many languages!!  You would be amazed (well, for most of
us here, probably not) some of the wierd stuff I see just like that
which leaves a student (and frequently the professor) totally baffled
about how the program generated the answer it did.

bill
```

###### ↳ ↳ ↳ Re: The MOVE problem

_(reply depth: 4)_

- **From:** docdwarf@panix.com ()
- **Date:** 2007-10-31T22:37:45+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<fgb03p$kmc$1@reader1.panix.com>`
- **References:** `<fg7ne4$e4q$01$1@news.t-online.com> <cgOVi.218417$m81.218277@fe01.news.easynews.com> <ssZVi.44717$b9.24845@bignews1.bellsouth.net> <56_Vi.15993$lD6.14460@newssvr27.news.prodigy.net>`

```
In article <56_Vi.15993$lD6.14460@newssvr27.news.prodigy.net>,
Doug Miller <spambait@milmac.com> wrote:
>In article <ssZVi.44717$b9.24845@bignews1.bellsouth.net>, "Judson
>McClendon" <judmc@sunvaley0.com> wrote:
…[10 more quoted lines elided]…
>answer.

Never mind that the Original Poster's question was 'What shouzld (sic) be 
displayed in various compatible modes?', of course.  I'm sure that would 
go over quite well in a tech interview:

'Here's one of our Production programs... what should be displayed in 
various compatible modes?'

'I would never consider writing such code.'

'Thanks much... next, please.'

DD
```

###### ↳ ↳ ↳ Re: The MOVE problem

_(reply depth: 5)_

- **From:** "Judson McClendon" <judmc@sunvaley0.com>
- **Date:** 2007-10-31T18:03:08-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<nQ7Wi.14423$u7.1682@bignews2.bellsouth.net>`
- **References:** `<fg7ne4$e4q$01$1@news.t-online.com> <cgOVi.218417$m81.218277@fe01.news.easynews.com> <ssZVi.44717$b9.24845@bignews1.bellsouth.net> <56_Vi.15993$lD6.14460@newssvr27.news.prodigy.net> <fgb03p$kmc$1@reader1.panix.com>`

```
<docdwarf@panix.com> wrote:
> Doug Miller <spambait@milmac.com> wrote:
>>"Judson McClendon" <judmc@sunvaley0.com> wrote:
…[21 more quoted lines elided]…
> 'Thanks much... next, please.'

Then I guess it's a Good Thing I wasn't answering the original question,
but merely commenting on the code in general, eh? :-)
```

###### ↳ ↳ ↳ Re: The MOVE problem

_(reply depth: 6)_

- **From:** docdwarf@panix.com ()
- **Date:** 2007-10-31T23:06:33+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<fgb1pp$f2e$1@reader1.panix.com>`
- **References:** `<fg7ne4$e4q$01$1@news.t-online.com> <56_Vi.15993$lD6.14460@newssvr27.news.prodigy.net> <fgb03p$kmc$1@reader1.panix.com> <nQ7Wi.14423$u7.1682@bignews2.bellsouth.net>`

```
In article <nQ7Wi.14423$u7.1682@bignews2.bellsouth.net>,
Judson McClendon <judmc@sunvaley0.com> wrote:
><docdwarf@panix.com> wrote:
>> Doug Miller <spambait@milmac.com> wrote:
…[25 more quoted lines elided]…
>but merely commenting on the code in general, eh? :-)

Almost as Good a Thing as responding to the interviewer with 'I hope you 
are very happy with whoever you hire for this position; at these rates and 
this code it certainly isn't going to be me.'

DD
```

###### ↳ ↳ ↳ Re: The MOVE problem

_(reply depth: 5)_

- **From:** "Pete Dashwood" <dashwood@removethis.enternet.co.nz>
- **Date:** 2007-11-01T16:42:29+13:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<5ot099FnttonU1@mid.individual.net>`
- **References:** `<fg7ne4$e4q$01$1@news.t-online.com> <cgOVi.218417$m81.218277@fe01.news.easynews.com> <ssZVi.44717$b9.24845@bignews1.bellsouth.net> <56_Vi.15993$lD6.14460@newssvr27.news.prodigy.net> <fgb03p$kmc$1@reader1.panix.com>`

```


<docdwarf@panix.com> wrote in message news:fgb03p$kmc$1@reader1.panix.com...
> In article <56_Vi.15993$lD6.14460@newssvr27.news.prodigy.net>,
> Doug Miller <spambait@milmac.com> wrote:
…[28 more quoted lines elided]…
> DD

LOL! Very true... :-)

Pete.
```

###### ↳ ↳ ↳ Re: The MOVE problem

_(reply depth: 5)_

- **From:** "Roger While" <simrw@sim-basis.de>
- **Date:** 2007-11-01T13:48:50+01:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<fgchvf$tuq$03$1@news.t-online.com>`
- **References:** `<fg7ne4$e4q$01$1@news.t-online.com> <cgOVi.218417$m81.218277@fe01.news.easynews.com> <ssZVi.44717$b9.24845@bignews1.bellsouth.net> <56_Vi.15993$lD6.14460@newssvr27.news.prodigy.net> <fgb03p$kmc$1@reader1.panix.com>`

```

<docdwarf@panix.com> schrieb im Newsbeitrag
news:fgb03p$kmc$1@reader1.panix.com...
> In article <56_Vi.15993$lD6.14460@newssvr27.news.prodigy.net>,
> Doug Miller <spambait@milmac.com> wrote:
> >In article <ssZVi.44717$b9.24845@bignews1.bellsouth.net>, "Judson
> >McClendon" <judmc@sunvaley0.com> wrote:
> >>Thanks Bill, I thought you would come back with a definitive response.
:-)
> >>
> >>>           MOVE A(B) TO B C(B).
…[3 more quoted lines elided]…
> >>example violates that principle. Using two statements would make the
intent
> >>obvious.
> >
> >DING DING DING! We have a winner, ladies and gentlemen! *That* is the
correct
> >answer.
>
> Never mind that the Original Poster's question was 'What shouzld (sic) be

Per dictionary -
so; thus: usually written parenthetically to denote that a word, phrase,
passage, etc., that may appear strange or incorrect has been written
intentionally or has been quoted verbatim: He signed his name as e. e.
cummings (sic).

Not intentinial and not quoted.

Roger


> displayed in various compatible modes?', of course.  I'm sure that would
> go over quite well in a tech interview:
…[9 more quoted lines elided]…
>
```

###### ↳ ↳ ↳ Re: The MOVE problem

_(reply depth: 6)_

- **From:** "Roger While" <simrw@sim-basis.de>
- **Date:** 2007-11-01T13:55:36+01:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<fgcic5$hgd$00$1@news.t-online.com>`
- **References:** `<fg7ne4$e4q$01$1@news.t-online.com> <cgOVi.218417$m81.218277@fe01.news.easynews.com> <ssZVi.44717$b9.24845@bignews1.bellsouth.net> <56_Vi.15993$lD6.14460@newssvr27.news.prodigy.net> <fgb03p$kmc$1@reader1.panix.com> <fgchvf$tuq$03$1@news.t-online.com>`

```

"Roger While" <simrw@sim-basis.de> schrieb im Newsbeitrag
news:fgchvf$tuq$03$1@news.t-online.com...
>
> <docdwarf@panix.com> schrieb im Newsbeitrag
…[10 more quoted lines elided]…
> > >>I would never consider writing such code as in this example. Code
should
> > >>be written to be as simple and easy to understand as possible, and
this
> > >>example violates that principle. Using two statements would make the
> intent
…[6 more quoted lines elided]…
> > Never mind that the Original Poster's question was 'What shouzld (sic)
be
>
> Per dictionary -
…[6 more quoted lines elided]…
>

Or intentnial (sic) ?

> Roger
>
…[14 more quoted lines elided]…
>
```

###### ↳ ↳ ↳ Re: The MOVE problem

_(reply depth: 6)_

- **From:** docdwarf@panix.com ()
- **Date:** 2007-11-01T13:24:13+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<fgck1t$6l1$1@reader1.panix.com>`
- **References:** `<fg7ne4$e4q$01$1@news.t-online.com> <56_Vi.15993$lD6.14460@newssvr27.news.prodigy.net> <fgb03p$kmc$1@reader1.panix.com> <fgchvf$tuq$03$1@news.t-online.com>`

```
In article <fgchvf$tuq$03$1@news.t-online.com>,
Roger While <simrw@sim-basis.de> wrote:
>
><docdwarf@panix.com> schrieb im Newsbeitrag
…[26 more quoted lines elided]…
>Not intentinial and not quoted.

'... has been written intentionally OR (emphasis added) has been quoted 
verbatim'.

As author you are welcome to have the definitive word on what was 
intended; as 
<http://groups.google.com/group/comp.lang.cobol/msg/3e9bf8fb100bbe4c?dmode=source> 
shows the mis-spelling is accurately quoted.

DD
```

###### ↳ ↳ ↳ Re: The MOVE problem

- **From:** "William M. Klein" <wmklein@nospam.netcom.com>
- **Date:** 2007-10-31T16:31:41+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<M52Wi.45174$g82.13198@fe07.news.easynews.com>`
- **References:** `<fg7ne4$e4q$01$1@news.t-online.com> <cgOVi.218417$m81.218277@fe01.news.easynews.com> <ssZVi.44717$b9.24845@bignews1.bellsouth.net>`

```
The original question came from a "compiler writer" not from a programmer.  The 
issue is not whether this SHOULD ever be written - but what should a compiler do 
when it finds it.  Of course, a compiler could reject the code - but then it 
wouldn't conform to any Standard (at least from the '74 Standard on).
```

###### ↳ ↳ ↳ Re: The MOVE problem

_(reply depth: 4)_

- **From:** "HeyBub" <heybubNOSPAM@gmail.com>
- **Date:** 2007-10-31T14:04:36-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<13ihkdv6ko4rab2@news.supernews.com>`
- **References:** `<fg7ne4$e4q$01$1@news.t-online.com> <cgOVi.218417$m81.218277@fe01.news.easynews.com> <ssZVi.44717$b9.24845@bignews1.bellsouth.net> <M52Wi.45174$g82.13198@fe07.news.easynews.com>`

```
William M. Klein wrote:
> The original question came from a "compiler writer" not from a
> programmer.  The issue is not whether this SHOULD ever be written -
> but what should a compiler do when it finds it.  Of course, a
> compiler could reject the code - but then it wouldn't conform to any
> Standard (at least from the '74 Standard on).

The compiler, in not rejecting the code, is relying on the good sense of the 
Senior Programmer to, ah, reject the code of the beginner.
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
