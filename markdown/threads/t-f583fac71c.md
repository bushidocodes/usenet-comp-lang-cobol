[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Search all verb: Micro Focus vs Standard ?

_12 messages · 7 participants · 2008-06_

**Topics:** [`Compilers and vendors`](../topics.md#compilers) · [`COBOL standards (ANS, ISO, 74/85/2002/2014)`](../topics.md#standards)

---

### Search all verb: Micro Focus vs Standard ?

- **From:** Gary <gary.cowell@gmail.com>
- **Date:** 2008-06-19T02:59:43-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<532f71e7-91cf-4862-bb13-d1720592f293@d1g2000hsg.googlegroups.com>`

```
My program is below. Can be run via "cobrun TEMP 3" (say) to find a
value or "cobrun TEMP 0" so that the search misses.

Anyhow, the question is, in MF COBOL, what is the value of the index
when a SEARCH ALL ends without matching a row? Does the standard have
anything to say on the matter?

The MF documentation says:

"If Format 2 of the SEARCH statement is used, a non-serial type of
search operation can take place; the initial setting of the index-name
for identifier-1 is ignored and its setting is varied during the
search operation with the restriction that at no time is it set to a
value that exceeds the value which corresponds to the last element of
the table, or that is less than the value that corresponds to the
first element of the table. The length of the table is discussed in
the topic The OCCURS Clause). If any of the conditions specified in
the WHEN clause cannot be satisfied for any setting of the index
within the permitted range, control is passed to imperative-
statement-1 of the AT END phrase, when specified, or to the next
executable sentence when this phrase is not specified; in either case
the final setting of the index is not predictable. If all conditions
can be satisfied, the index indicates an occurrence that allows the
conditions to be satisfied, and control passes to imperative-
statement-2."

I interpret the phrase "at no time is it set to a value that exceeds
the value which corresponds to the last element of the table, or that
is less than the value that corresponds to the first element of the
table" to mean that the index is always valid for the table, and will
be valid when the SEARCH ALL ends. In practice, under SE 4 and 5, the
index has value 0 after the SEARCH ALL.


=========================================================
       identification division.
       program-id. TEMP.
       environment division.
       data division.
       working-storage section.
       77 MY-NUM pic 9(10).
       01 MY-LITERAL.
          02 pic X(10) value "1a2s3d4f5g".
       01 MY-ARRAY redefines MY-LITERAL
          occurs 5
          indexed by MY-INDEX
          ascending key MY-KEY.
           02 MY-KEY pic X(1).
           02 MY-VALUE pic X(1).
       linkage section.
       01  LS-PARM.
           02 LS-LEN pic S9(4) binary.
           02 LS-KEY pic X.
       procedure division using LS-PARM.
           display LS-KEY
           search all MY-ARRAY
              at end
                 continue
              when MY-KEY (MY-INDEX) = LS-KEY
                 continue
           end-search
           set MY-NUM to MY-INDEX
           display MY-NUM
           display MY-KEY(MY-INDEX)
           display MY-VALUE(MY-INDEX)
           exit program.
       end program TEMP.
=========================================================
```

#### ↳ Re: Search all verb: Micro Focus vs Standard ?

- **From:** docdwarf@panix.com ()
- **Date:** 2008-06-19T12:03:01+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<g3dhtl$5t9$1@reader2.panix.com>`
- **References:** `<532f71e7-91cf-4862-bb13-d1720592f293@d1g2000hsg.googlegroups.com>`

```
In article <532f71e7-91cf-4862-bb13-d1720592f293@d1g2000hsg.googlegroups.com>,
Gary  <gary.cowell@gmail.com> wrote:

[snip]

>The MF documentation says:
>
…[21 more quoted lines elided]…
>be valid when the SEARCH ALL ends.

Your interpretation, Mr Cowell, seems not to take into account something 
explicitly stated: 

'If any of the conditions specified in the WHEN clause cannot be satisfied 
for any setting of the index within the permitted range, control is passed 
to imperative-statement-1 of the AT END phrase, when specified, or to the 
next executable sentence when this phrase is not specified; IN EITHER CASE 
THE FINAL SETTING OF THE INDEX IS NOT PREDICTABLE.' (emphasis added)

DD
```

##### ↳ ↳ Re: Search all verb: Micro Focus vs Standard ?

- **From:** Gary <gary.cowell@gmail.com>
- **Date:** 2008-06-19T07:06:45-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<344ce66b-eaf0-4d41-8ebb-0ad4baedb74e@c58g2000hsc.googlegroups.com>`
- **References:** `<532f71e7-91cf-4862-bb13-d1720592f293@d1g2000hsg.googlegroups.com> <g3dhtl$5t9$1@reader2.panix.com>`

```
On Jun 19, 1:03 pm, docdw...@panix.com () wrote:
> In article <532f71e7-91cf-4862-bb13-d1720592f...@d1g2000hsg.googlegroups.com>,
>
…[40 more quoted lines elided]…
> DD

Yes, I did read that but we interpreted the documentation to mean that
'the final setting of the index is not predictable /(but will be a
valid index entry)/' as it's previously stated that

"at no time is it set to a
value that exceeds the value which corresponds to the last element of
the table, or that is less than the value that corresponds to the
first element of the table."

I could live with it being not predictable at the end, so long as it
adhered to the above.

The MF documentation seemed to be contradictory in this case. Still
wondering what the standard has to say about search all and the final
setting of the index value.
```

###### ↳ ↳ ↳ Re: Search all verb: Micro Focus vs Standard ?

- **From:** docdwarf@panix.com ()
- **Date:** 2008-06-19T14:53:23+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<g3drt3$pqo$1@reader2.panix.com>`
- **References:** `<532f71e7-91cf-4862-bb13-d1720592f293@d1g2000hsg.googlegroups.com> <g3dhtl$5t9$1@reader2.panix.com> <344ce66b-eaf0-4d41-8ebb-0ad4baedb74e@c58g2000hsc.googlegroups.com>`

```
In article <344ce66b-eaf0-4d41-8ebb-0ad4baedb74e@c58g2000hsc.googlegroups.com>,
Gary  <gary.cowell@gmail.com> wrote:
>On Jun 19, 1:03�pm, docdw...@panix.com () wrote:
>> In article <532f71e7-91cf-4862-bb13-d1720592f...@d1g2000hsg.googlegroups.com>,
…[50 more quoted lines elided]…
>first element of the table."

One might wish to consider the words 'its setting is varied during the 
'... ITS SETTING IS VARIED DURING THE SEARCH OPERATION with restriction 
indicates that no more 
searching is done, as the SEARCH is AT END... so a restriction on behavior 
during the SEARCH might not apply.

>
>I could live with it being not predictable at the end, so long as it
>adhered to the above.

I do not see what evidence there is that during the SEARCH the value 
exceeds the upper or lower element.

>
>The MF documentation seemed to be contradictory in this case.

If one expects the same behavior 'during' and 'at end', perhaps so.

DD
```

###### ↳ ↳ ↳ Re: Search all verb: Micro Focus vs Standard ?

- **From:** Robert <no@e.mail>
- **Date:** 2008-06-19T12:30:21-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<ho5l54pj3hvhpssqv04r6rmqharqogo6gs@4ax.com>`
- **References:** `<532f71e7-91cf-4862-bb13-d1720592f293@d1g2000hsg.googlegroups.com> <g3dhtl$5t9$1@reader2.panix.com> <344ce66b-eaf0-4d41-8ebb-0ad4baedb74e@c58g2000hsc.googlegroups.com>`

```
On Thu, 19 Jun 2008 07:06:45 -0700 (PDT), Gary <gary.cowell@gmail.com> wrote:

>On Jun 19, 1:03ï¿½pm, docdw...@panix.com () wrote:
>> In article <532f71e7-91cf-4862-bb13-d1720592f...@d1g2000hsg.googlegroups.com>,
…[57 more quoted lines elided]…
>setting of the index value.

The 2002 Standard says:

"A nonserial type of search operation may take place. The initial setting of the search
index is ignored. Its setting is varied during the search operation in a manner specified
by the implementor. At no time is it set to a value that exceeds the value that
corresponds to the last element of the table or is less than the value that
corresponds to the first element of the table. The length of the table is discussed in the
OCCURS clause. If any of the conditions specified in the WHEN phrase is not satisfied for
any setting of the search index within the permitted range, the final setting of the
search index is undefined."
```

###### ↳ ↳ ↳ Re: Search all verb: Micro Focus vs Standard ?

_(reply depth: 4)_

- **From:** Howard Brazee <howard@brazee.net>
- **Date:** 2008-06-19T12:02:59-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<um7l54l5tksfo7jnous8b5ek06u21nvh1a@4ax.com>`
- **References:** `<532f71e7-91cf-4862-bb13-d1720592f293@d1g2000hsg.googlegroups.com> <g3dhtl$5t9$1@reader2.panix.com> <344ce66b-eaf0-4d41-8ebb-0ad4baedb74e@c58g2000hsc.googlegroups.com> <ho5l54pj3hvhpssqv04r6rmqharqogo6gs@4ax.com>`

```
I just came across a table boundary error when I recompiled the
following:

SEARCH SUBC-ENTRY                                  
    WHEN SE-KEY (SE-INDEX) = WS01-HOLD-TABLE-KEY   
        NEXT SENTENCE.                             
                
                          
IF SE-KEY (SE-INDEX) NOT = WS01-HOLD-TABLE-KEY     
    GO TO 2000-PDT-000.        

SE-INDEX was 151 in a table of OCCURS 150.
```

###### ↳ ↳ ↳ Re: Search all verb: Micro Focus vs Standard ?

_(reply depth: 5)_

- **From:** Robert <no@e.mail>
- **Date:** 2008-06-19T21:49:33-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<jj5m549kgfm232eu18kdtu6ma5d0hq7pp2@4ax.com>`
- **References:** `<532f71e7-91cf-4862-bb13-d1720592f293@d1g2000hsg.googlegroups.com> <g3dhtl$5t9$1@reader2.panix.com> <344ce66b-eaf0-4d41-8ebb-0ad4baedb74e@c58g2000hsc.googlegroups.com> <ho5l54pj3hvhpssqv04r6rmqharqogo6gs@4ax.com> <um7l54l5tksfo7jnous8b5ek06u21nvh1a@4ax.com>`

```
On Thu, 19 Jun 2008 12:02:59 -0600, Howard Brazee <howard@brazee.net> wrote:

>I just came across a table boundary error when I recompiled the
>following:
…[9 more quoted lines elided]…
>SE-INDEX was 151 in a table of OCCURS 150.                    

Little known Standard feature: you're not allowed to use NEXT SENTENCE in a SEARCH unless
you say END-SEARCH. CONTINUE is allowed. 

Turn off bounds checking and you should be ok.

If all else fails, you might be forced to do it the way you're supposed to, with AT END.
I realize that destroys the symmetry of testing the same condition twice. How about this:

IF SE-INDEX < 1 OR > (LENGTH OF SE-TABLE / LENGTH OF SE-ENTRY) OR 
    SE-KEY (SE-INDEX) NOT = WS01-HOLD-TABLE-KEY     
    GO TO 2000-PDT-000.       

or this

SEARCH SUBC-ENTRY                                  
     WHEN SE-KEY (SE-INDEX) = WS01-HOLD-TABLE-KEY   
       NEXT SENTENCE
END-SEARCH
GO TO 2000-PDT-000.
```

###### ↳ ↳ ↳ Re: Search all verb: Micro Focus vs Standard ?

_(reply depth: 6)_

- **From:** "Karl Kiesel" <Karl.Kiesel@fujitsu-siemens.com>
- **Date:** 2008-06-20T08:39:28+02:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<g3fjb0$t1h$1@nntp.fujitsu-siemens.com>`
- **References:** `<532f71e7-91cf-4862-bb13-d1720592f293@d1g2000hsg.googlegroups.com> <g3dhtl$5t9$1@reader2.panix.com> <344ce66b-eaf0-4d41-8ebb-0ad4baedb74e@c58g2000hsc.googlegroups.com> <ho5l54pj3hvhpssqv04r6rmqharqogo6gs@4ax.com> <um7l54l5tksfo7jnous8b5ek06u21nvh1a@4ax.com> <jj5m549kgfm232eu18kdtu6ma5d0hq7pp2@4ax.com>`

```
"Robert" <no@e.mail> schrieb im Newsbeitrag
> Little known Standard feature: you're not allowed to use NEXT SENTENCE in 
> a SEARCH unless
> you say END-SEARCH. CONTINUE is allowed.
>
...
> How about this:
>
…[11 more quoted lines elided]…
>

Really ??? with my little knowledge of English as a non-native speaker, I 
read STD2002 just the the other way: syntax rule 2 (all formats) says:
'if the END-SEARCH phrase is specified, the NEXT SENTENCE phrase shall not 
be specified.'

Karl Kiesel
Fujitsu Siemens Computers, M�nchen
```

###### ↳ ↳ ↳ Re: Search all verb: Micro Focus vs Standard ?

_(reply depth: 7)_

- **From:** "William M. Klein" <wmklein@nospam.netcom.com>
- **Date:** 2008-06-24T19:25:50+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<2Tb8k.103412$tY4.33945@fe06.news.easynews.com>`
- **References:** `<532f71e7-91cf-4862-bb13-d1720592f293@d1g2000hsg.googlegroups.com> <g3dhtl$5t9$1@reader2.panix.com> <344ce66b-eaf0-4d41-8ebb-0ad4baedb74e@c58g2000hsc.googlegroups.com> <ho5l54pj3hvhpssqv04r6rmqharqogo6gs@4ax.com> <um7l54l5tksfo7jnous8b5ek06u21nvh1a@4ax.com> <jj5m549kgfm232eu18kdtu6ma5d0hq7pp2@4ax.com> <g3fjb0$t1h$1@nntp.fujitsu-siemens.com>`

```
Karl is correct and Robert is wrong.

"NEXT SENTENCE" is prohibited with END-SEARCH (like END-IF) according to the 
Standard.  However, as this thread is about a Micro Focus issue, it should be 
noted that they (like several other implementers - and the original CODASYL JOD) 
*do* allow this.
```

###### ↳ ↳ ↳ Re: Search all verb: Micro Focus vs Standard ?

_(reply depth: 6)_

- **From:** "Michael Mattias" <mmattias@talsystems.com>
- **Date:** 2008-06-20T07:28:49-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<MoN6k.8957$jI5.911@flpi148.ffdc.sbc.com>`
- **References:** `<532f71e7-91cf-4862-bb13-d1720592f293@d1g2000hsg.googlegroups.com> <g3dhtl$5t9$1@reader2.panix.com> <344ce66b-eaf0-4d41-8ebb-0ad4baedb74e@c58g2000hsc.googlegroups.com> <ho5l54pj3hvhpssqv04r6rmqharqogo6gs@4ax.com> <um7l54l5tksfo7jnous8b5ek06u21nvh1a@4ax.com> <jj5m549kgfm232eu18kdtu6ma5d0hq7pp2@4ax.com>`

```

```

###### ↳ ↳ ↳ Re: Search all verb: Micro Focus vs Standard ?

_(reply depth: 4)_

- **From:** Gary <gary.cowell@gmail.com>
- **Date:** 2008-06-20T00:57:52-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<d565d4f6-b527-45a6-a1aa-47622fe5ce61@l42g2000hsc.googlegroups.com>`
- **References:** `<532f71e7-91cf-4862-bb13-d1720592f293@d1g2000hsg.googlegroups.com> <g3dhtl$5t9$1@reader2.panix.com> <344ce66b-eaf0-4d41-8ebb-0ad4baedb74e@c58g2000hsc.googlegroups.com> <ho5l54pj3hvhpssqv04r6rmqharqogo6gs@4ax.com>`

```
On Jun 19, 6:30 pm, Robert <n...@e.mail> wrote:


> The 2002 Standard says:
>
…[7 more quoted lines elided]…
> search index is undefined."

Ah thanks for that. That's much clearer.
```

#### ↳ Re: Search all verb: Micro Focus vs Standard ?

- **From:** "William M. Klein" <wmklein@nospam.netcom.com>
- **Date:** 2008-06-24T19:24:01+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<kRb8k.83189$tn2.44642@fe07.news.easynews.com>`
- **References:** `<532f71e7-91cf-4862-bb13-d1720592f293@d1g2000hsg.googlegroups.com>`

```
Lots of replies and I think you already have the answer, but "unpredictable" (or 
"undefined") means exactly what it says.  It means that ALL rules are "out the 
window" and there is nothing "defined by the Standard" or predictable about the 
"results".
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
