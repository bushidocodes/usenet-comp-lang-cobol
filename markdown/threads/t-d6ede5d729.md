[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Fiscal Year

_13 messages · 4 participants · 2005-04_

---

### Fiscal Year

- **From:** "Jeff" <jmoore207@hotmail.com>
- **Date:** 2005-04-22T05:27:10-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1114172830.129788.228170@l41g2000cwc.googlegroups.com>`

```
I have a report that currently gives totals depending on the MOYR you
enter (0405) and it works back to 0005, then it starts with 0405 and
subtracts 1 from yr (0404) and works back to 00 month. They want to
give an option to use fiscal year instead June-May. I am having a time
coming up with logic if you enter 0405 it needs to go back June I
guess. Any help would be appreciated.
```

#### ↳ Re: Fiscal Year

- **From:** docdwarf@panix.com
- **Date:** 2005-04-22T08:40:02-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<d4arb2$mqq$1@panix5.panix.com>`
- **References:** `<1114172830.129788.228170@l41g2000cwc.googlegroups.com>`

```
In article <1114172830.129788.228170@l41g2000cwc.googlegroups.com>,
Jeff <jmoore207@hotmail.com> wrote:
>I have a report that currently gives totals depending on the MOYR you
>enter (0405) and it works back to 0005, then it starts with 0405 and
…[3 more quoted lines elided]…
>guess. Any help would be appreciated.

I am uncertain what it is that you need.  What you have at present appears 
to be a routine which, given a month and a year, produces a report based 
on the data from the calendar year preceding.

Your fiscal year runs from June - May.  Are you saying that if you run the 
report using the fiscal year on 01 Aug 2005 you wish to see data only for 
01 Jun 2005 - 31 Jul 2005?

DD
```

##### ↳ ↳ Re: Fiscal Year

- **From:** "Jeff" <jmoore207@hotmail.com>
- **Date:** 2005-04-22T05:41:49-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1114173709.237919.122700@z14g2000cwz.googlegroups.com>`
- **In-Reply-To:** `<d4arb2$mqq$1@panix5.panix.com>`
- **References:** `<1114172830.129788.228170@l41g2000cwc.googlegroups.com> <d4arb2$mqq$1@panix5.panix.com>`

```
Yes. and the same for 01 Jun 2004- 31 July 2004
```

###### ↳ ↳ ↳ Re: Fiscal Year

- **From:** docdwarf@panix.com
- **Date:** 2005-04-22T09:08:55-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<d4at17$1h5$1@panix5.panix.com>`
- **References:** `<1114172830.129788.228170@l41g2000cwc.googlegroups.com> <d4arb2$mqq$1@panix5.panix.com> <1114173709.237919.122700@z14g2000cwz.googlegroups.com>`

```
In article <1114173709.237919.122700@z14g2000cwz.googlegroups.com>,
Jeff <jmoore207@hotmail.com> wrote:
>Yes. and the same for 01 Jun 2004- 31 July 2004

I see... so it would appear that you need something like

If Fiscal-Year-Option
    Move 06 To From-MM
    Move 01 To From-DD   
    If To-MM < 06
        Compute From-YY = (To-YY - 1)
    Else
        Move To-YY To From-YY
    End-If
End-If

... or am I missing something here?

DD
```

###### ↳ ↳ ↳ Re: Fiscal Year

_(reply depth: 4)_

- **From:** "Jeff" <jmoore207@hotmail.com>
- **Date:** 2005-04-22T06:18:59-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1114175939.618257.232970@g14g2000cwa.googlegroups.com>`
- **In-Reply-To:** `<d4at17$1h5$1@panix5.panix.com>`
- **References:** `<1114172830.129788.228170@l41g2000cwc.googlegroups.com> <d4arb2$mqq$1@panix5.panix.com> <1114173709.237919.122700@z14g2000cwz.googlegroups.com> <d4at17$1h5$1@panix5.panix.com>`

```
I think something like that. I am not worrying about day,

 13234 SBD-0240.
         97219049
 13235      SUBTRACT 1 FROM WK-MOYR.                           97219049
 13236      IF WK-MO = 0 GO TO SBD-0260.
97219049
 13238      MOVE WK-MOYR TO DB-ARG-BLMY.

 13282 SBD-0260.
93277147
 13283      MOVE WW-BILLMOYR TO WK-MOYR.
93277147
 13284      CALL "MOYR2Y2K" USING WK-MOYR, Y2K-WK-MOYR.      98147059
 13285      SUBTRACT 1 FROM Y2K-YYYY OF Y2KR-WK-MOYR.         98147059
 13286      CALL "Y2K2MOYR" USING Y2K-WK-MOYR, WK-MOYR.      98147059
 13287      MOVE WK-MOYR TO DB-ARG-BLMY.
93277147
 13288      PERFORM FIND-BILLSTAT.
          93277147


  2036 01  WK-MOYR                  PIC 9(4).
89250117
  2037 01  WK-MOYR-R REDEFINES WK-MOYR.
  2038     03  WK-YR                PIC 99.
89250117
  2039     03  WK-MO                PIC 99.
89250117
  2040 01  Y2K-WK-MOYR              PIC 9(6).
98147059
  2041 01  Y2KR-WK-MOYR REDEFINES Y2K-WK-MOYR.
98147059
  2042     03  Y2K-YYYY             PIC 9(4).
98147059
  2043     03  Y2K-MM               PIC 99.

It accepts a BILLMOYR (0405) and if fiscal I need to go back to 0604.
I also would need last-year  (0404) back to 0603.
```

###### ↳ ↳ ↳ Re: Fiscal Year

_(reply depth: 5)_

- **From:** docdwarf@panix.com
- **Date:** 2005-04-22T09:28:48-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<d4au6g$3pq$1@panix5.panix.com>`
- **References:** `<1114172830.129788.228170@l41g2000cwc.googlegroups.com> <1114173709.237919.122700@z14g2000cwz.googlegroups.com> <d4at17$1h5$1@panix5.panix.com> <1114175939.618257.232970@g14g2000cwa.googlegroups.com>`

```
In article <1114175939.618257.232970@g14g2000cwa.googlegroups.com>,
Jeff <jmoore207@hotmail.com> wrote:
>I think something like that.

I see... where does the solution proposed fall short of what you need?

DD
```

###### ↳ ↳ ↳ Re: Fiscal Year

_(reply depth: 6)_

- **From:** "Jeff" <jmoore207@hotmail.com>
- **Date:** 2005-04-22T06:35:10-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1114176910.053899.276720@z14g2000cwz.googlegroups.com>`
- **In-Reply-To:** `<d4au6g$3pq$1@panix5.panix.com>`
- **References:** `<1114172830.129788.228170@l41g2000cwc.googlegroups.com> <1114173709.237919.122700@z14g2000cwz.googlegroups.com> <d4at17$1h5$1@panix5.panix.com> <1114175939.618257.232970@g14g2000cwa.googlegroups.com> <d4au6g$3pq$1@panix5.panix.com>`

```
Sorry just got more info. The fiscal year can be any period, different
Companies use different. My example happened to be June-May, but it can
be March - Feb or any other. It's nice to get all the specs up front
huh?
```

###### ↳ ↳ ↳ Re: Fiscal Year

_(reply depth: 7)_

- **From:** docdwarf@panix.com
- **Date:** 2005-04-22T09:55:14-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<d4avo2$rcs$1@panix5.panix.com>`
- **References:** `<1114172830.129788.228170@l41g2000cwc.googlegroups.com> <1114175939.618257.232970@g14g2000cwa.googlegroups.com> <d4au6g$3pq$1@panix5.panix.com> <1114176910.053899.276720@z14g2000cwz.googlegroups.com>`

```
In article <1114176910.053899.276720@z14g2000cwz.googlegroups.com>,
Jeff <jmoore207@hotmail.com> wrote:
>Sorry just got more info. The fiscal year can be any period, different
>Companies use different. My example happened to be June-May, but it can
>be March - Feb or any other. It's nice to get all the specs up front
>huh?

It certainly is... so there are multiple fiscal years which are determined 
by the company for which the program is being run?  That might seem to be 
taken care of by:

If Fiscal-Year-Option
    Evaluate True
        When First-Company
            Move 06 To From-MM
            If To-MM < 06
                Compute From-YY = (To-YY - 1)
            Else
                Move To-YY To From-YY
            End-If
        When Second-Company
            Move 02 To From-MM
            If To-MM < 02
                Compute From-YY = (To-YY - 1)
            Else
                Move To-YY To From-YY
            End-If
    End-Evaluate
End-If

... or is there something I am not understanding here?

DD
```

###### ↳ ↳ ↳ Re: Fiscal Year

_(reply depth: 8)_

- **From:** "Jeff" <jmoore207@hotmail.com>
- **Date:** 2005-04-22T08:03:59-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1114182239.613306.4270@l41g2000cwc.googlegroups.com>`
- **In-Reply-To:** `<d4avo2$rcs$1@panix5.panix.com>`
- **References:** `<1114172830.129788.228170@l41g2000cwc.googlegroups.com> <1114175939.618257.232970@g14g2000cwa.googlegroups.com> <d4au6g$3pq$1@panix5.panix.com> <1114176910.053899.276720@z14g2000cwz.googlegroups.com> <d4avo2$rcs$1@panix5.panix.com>`

```
No, Sorry again, I guess I explained that wrong this is a standard
report, we have 180 companies that use this program the fiscal year
will be determined by a 2 digit code (beginning month) read from the
control-file. So It is parameter driven depending on parameter(98) = 06
or 02 or 12 or whatever.
```

###### ↳ ↳ ↳ Re: Fiscal Year

_(reply depth: 9)_

- **From:** Donald Tees <donald_tees@sympatico.ca>
- **Date:** 2005-04-22T11:15:38-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<uy8ae.9335$9G.710848@news20.bellglobal.com>`
- **In-Reply-To:** `<1114182239.613306.4270@l41g2000cwc.googlegroups.com>`
- **References:** `<1114172830.129788.228170@l41g2000cwc.googlegroups.com> <1114175939.618257.232970@g14g2000cwa.googlegroups.com> <d4au6g$3pq$1@panix5.panix.com> <1114176910.053899.276720@z14g2000cwz.googlegroups.com> <d4avo2$rcs$1@panix5.panix.com> <1114182239.613306.4270@l41g2000cwc.googlegroups.com>`

```
Jeff wrote:
> No, Sorry again, I guess I explained that wrong this is a standard
> report, we have 180 companies that use this program the fiscal year
…[3 more quoted lines elided]…
> 

Why not just keep a from-date/to-date in the control file? You only set 
it once per year. We have companies that use a complete list of fiscal 
periods, as they run on 13 4 week "months".  It is not like someone 
enters it every day, and there is probably a professional handling year 
ends.

Donald
```

###### ↳ ↳ ↳ Re: Fiscal Year

_(reply depth: 9)_

- **From:** docdwarf@panix.com
- **Date:** 2005-04-22T11:45:34-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<d4b66u$svu$1@panix5.panix.com>`
- **References:** `<1114172830.129788.228170@l41g2000cwc.googlegroups.com> <1114176910.053899.276720@z14g2000cwz.googlegroups.com> <d4avo2$rcs$1@panix5.panix.com> <1114182239.613306.4270@l41g2000cwc.googlegroups.com>`

```
In article <1114182239.613306.4270@l41g2000cwc.googlegroups.com>,
Jeff <jmoore207@hotmail.com> wrote:
>No, Sorry again, I guess I explained that wrong this is a standard
>report, we have 180 companies that use this program the fiscal year
…[3 more quoted lines elided]…
>

I see... where does the solution proposed fall short of what you need?

DD
```

###### ↳ ↳ ↳ Re: Fiscal Year

_(reply depth: 8)_

- **From:** "Jeff" <jmoore207@hotmail.com>
- **Date:** 2005-04-22T08:04:01-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1114182241.955579.64870@o13g2000cwo.googlegroups.com>`
- **In-Reply-To:** `<d4avo2$rcs$1@panix5.panix.com>`
- **References:** `<1114172830.129788.228170@l41g2000cwc.googlegroups.com> <1114175939.618257.232970@g14g2000cwa.googlegroups.com> <d4au6g$3pq$1@panix5.panix.com> <1114176910.053899.276720@z14g2000cwz.googlegroups.com> <d4avo2$rcs$1@panix5.panix.com>`

```
No, Sorry again, I guess I explained that wrong this is a standard
report, we have 180 companies that use this program the fiscal year
will be determined by a 2 digit code (beginning month) read from the
control-file. So It is parameter driven depending on parameter(98) = 06
or 02 or 12 or whatever.
```

###### ↳ ↳ ↳ Re: Fiscal Year

_(reply depth: 9)_

- **From:** l.willms@jpberlin.de (Lueko Willms)
- **Date:** 2005-04-23T13:58:00+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<9VRNdbTPflB@jpberlin-l.willms.jpberlin.de>`
- **References:** `<1114172830.129788.228170@l41g2000cwc.googlegroups.com> <d4avo2$rcs$1@panix5.panix.com> <1114182241.955579.64870@o13g2000cwo.googlegroups.com>`

```
.    On  22.04.05
  wrote  jmoore207@hotmail.com (Jeff)
     on  /COMP/LANG/COBOL
     in  1114182241.955579.64870@o13g2000cwo.googlegroups.com
  about  Re: Fiscal Year


j> No, Sorry again, I guess I explained that wrong this is a standard
j> report, we have 180 companies that use this program the fiscal year
j> will be determined by a 2 digit code (beginning month) read from the
j> control-file. So It is parameter driven depending on parameter(98) =
j> 06 or 02 or 12 or whatever.

   Frankly, I do not understand at all what is so complicated about  
that?

   The file which is to be reported or summariesed is sequentially  
accessible via the date, isn't it? With an index on it, where you can  
start with the appropriate month, right?

   So, where is the problem?



Yours,
Lï¿½ko Willms                                     http://www.willms-edv.de
/--------- L.WILLMS@jpberlin.de -- Alle Rechte vorbehalten --

Wir wohnen in Gï¿½ttingen in Scheiterhaufen, die mit Tï¿½ren und Fenstern versehen sind. -G.C.Lichtenberg
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
