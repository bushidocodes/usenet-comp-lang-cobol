[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# unique program-names and contained programs

_7 messages · 3 participants · 2005-12_

---

### unique program-names and contained programs

- **From:** "Karl Kiesel" <Karl.Kiesel@fujitsu-siemens.com>
- **Date:** 2005-12-19T14:11:30+01:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<do6bi2$mvq$1@nntp.fujitsu-siemens.com>`

```
consider the following 'program'

  IDENFIFICATION DIVISION.
  PROGRAM-ID.        sud001 RECURSIVE.
 ...
   IDENTIFICATION DIVISION.
   PROGRAM-ID.        sud002.
 ...
      CALL sud001.
 ...
    IDENTIFICATION DIVISION.
    PROGRAM-ID.       sud001.
 ...
    END PROGRAM       sud001.
   END PROGRAM       sud002.
  END PROGRAM       sud001.

according to STD85 (4.2.2.1.1, IV-6...) the program-names 'sud001', 'sud002' 
and 'sud001' are one of the sets of user-defined words and must be unique 
within that set; exceptions to this requirement as sepcified in V-17 and 
then X-4 do not relax this requirement; therefore this program is erroneous.

considering STD2002, the requirement for uniqueness of names within a set 
has been replaced by '8.4.1 uniqueness of reference', which again refers to 
'8.4.5 scope of names'; there we find (8.4.5.2) '...the names assigned to 
programs that are contained directly or indirectly within the same outermost 
program shall be unique within that outermost program'
Unless I misunderstand the semantic of 'within' completely, it seems that 
the reqirement for uniqueness excludes the outermost program - thus program 
now is correct!
Any opinions, which programm is called in the example above, if this change 
really has been intended or did I miss some rules?

regards  Karl Kiesel
```

#### ↳ Re: unique program-names and contained programs

- **From:** "Rick Smith" <ricksmith@mfi.net>
- **Date:** 2005-12-19T12:04:21-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<11qdq2vepb67b3c@corp.supernews.com>`
- **References:** `<do6bi2$mvq$1@nntp.fujitsu-siemens.com>`

```

"Karl Kiesel" <Karl.Kiesel@fujitsu-siemens.com> wrote in message
news:do6bi2$mvq$1@nntp.fujitsu-siemens.com...
> consider the following 'program'
>
…[15 more quoted lines elided]…
> according to STD85 (4.2.2.1.1, IV-6...) the program-names 'sud001',
'sud002'
> and 'sud001' are one of the sets of user-defined words and must be unique
> within that set; exceptions to this requirement as sepcified in V-17 and
> then X-4 do not relax this requirement; therefore this program is
erroneous.
>
> considering STD2002, the requirement for uniqueness of names within a set
> has been replaced by '8.4.1 uniqueness of reference', which again refers
to
> '8.4.5 scope of names'; there we find (8.4.5.2) '...the names assigned to
> programs that are contained directly or indirectly within the same
outermost
> program shall be unique within that outermost program'
> Unless I misunderstand the semantic of 'within' completely, it seems that
> the reqirement for uniqueness excludes the outermost program - thus
program
> now is correct!
> Any opinions, which programm is called in the example above, if this
change
> really has been intended or did I miss some rules?

I don't accept that the program was erroneous in COBOL 85.
-----
      $set ans85 flag"ans85" flagas"s" nestcall
       identification division.
       program-id. sud001.
       procedure division.
       begin.
           display "in outermost 'sud001'"
           call "sud002"
           display "in outermost 'sud001'"
           stop run
           .
       identification division.
       program-id. sud002.
       procedure division.
       begin.
           display "in 'sud002'"
           call "sud001"
           display "in 'sud002'"
           exit program
           .
       identification division.
       program-id. sud001.
       procedure division.
       begin.
           display "in inner 'sud001'"
           exit program
           .
       end program sud001.
       end program sud002.
       end program sud001.
-----

Which gave the result:
-----
in outermost 'sud001'
in 'sud002'
in inner 'sud001'
in 'sud002'
in outermost 'sud001'
-----

The contained 'sud001' will be called in COBOL 2002
since it is local to 'sud002' while the outermost 'sud001'
is global. See "8.4.5.1 Local and global names".

"3) If more than one item is identified, no more than one
of them may have a name local to source element B. If
zero or one of the items has a name local to source
element B, the following rules apply:
a) If the name is declared in source element B, the item
in source element B is the referenced item."

Though I could be mistaken.
```

##### ↳ ↳ Re: unique program-names and contained programs

- **From:** "Chuck Stevens" <charles.stevens@unisys.com>
- **Date:** 2005-12-19T12:56:55-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<do76qo$1mr8$1@si05.rsvl.unisys.com>`
- **References:** `<do6bi2$mvq$1@nntp.fujitsu-siemens.com> <11qdq2vepb67b3c@corp.supernews.com>`

```
If for no other reason, the program is syntactically invalid in standard 
ANSI-85 COBOL because of the presence of RECURSIVE in the PROGRAM-ID 
paragraph.

    -Chuck Stevens

"Rick Smith" <ricksmith@mfi.net> wrote in message 
news:11qdq2vepb67b3c@corp.supernews.com...
>
> "Karl Kiesel" <Karl.Kiesel@fujitsu-siemens.com> wrote in message
…[96 more quoted lines elided]…
>
```

###### ↳ ↳ ↳ Re: unique program-names and contained programs

- **From:** "Rick Smith" <ricksmith@mfi.net>
- **Date:** 2005-12-19T17:06:28-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<11qebp8l298c9f7@corp.supernews.com>`
- **References:** `<do6bi2$mvq$1@nntp.fujitsu-siemens.com> <11qdq2vepb67b3c@corp.supernews.com> <do76qo$1mr8$1@si05.rsvl.unisys.com>`

```

"Chuck Stevens" <charles.stevens@unisys.com> wrote in message
news:do76qo$1mr8$1@si05.rsvl.unisys.com...
> "Rick Smith" <ricksmith@mfi.net> wrote in message
> news:11qdq2vepb67b3c@corp.supernews.com...
[snip]
> > The contained 'sud001' will be called in COBOL 2002
> > since it is local to 'sud002' while the outermost 'sud001'
…[13 more quoted lines elided]…
> paragraph.

As it turns out, I missed some of the nuances of the
FDIS (2002).

"8.4.5 Scope of names" states, in part, "Specific conventions
for declarations and references to the following types of
user-defined words are specified in 8.4.5.1, Local and
global names, through 8.4.5.10, Scope of property-names:",
where the list of names that follows includes "program-name".
Thus I thought 8.5.4.1 applied to "program-name".

What I failed to see was that the subsections of 8.4.5.1
provided direction for determining what is a local name
and what is a global name. Thus the requirements given
in 8.4.5.1 precede the definitions and that one must
understand the content of the subsections before
determining whether the section applies.

Had there been a statement at the beginning of 8.4.5.1
to the effect that 8.4.5.1 applies only to its subsections,
it is unlikely that I would have considered 8.4.5.1 to be
relevant to the discussion of "program-name".

I know what happened; but I am in no position to
judge whether the problem was mine alone, or whether
the standard is misleading because the meaning of the terms
'local name' and 'global name' comes after their use.
```

#### ↳ Re: unique program-names and contained programs

- **From:** "Chuck Stevens" <charles.stevens@unisys.com>
- **Date:** 2005-12-19T09:12:41-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<do6pma$1f1u$1@si05.rsvl.unisys.com>`
- **References:** `<do6bi2$mvq$1@nntp.fujitsu-siemens.com>`

```
No, I don't think that's quite correct, and I think your misunderstanding 
stems from missing the importance of "contained" in the phrase "contained 
within".  The program "sud002" is "contained within" the outermost program 
"sud001", but the outermost program does not qualify as "contained within" 
itself.  That "sud001" is a separately compiled program that is not 
contained within anything, and the distinction between "separately compiled 
program" and "nested program" that is of importance here.

First, some notes on this program relative to the '85 standard.

The most immediate reason that the program wouldn't compile with a 
1985-compliant compiler is that the RECURSIVE phrase of the PROGRAM-ID 
paragraph is not part of 1985 COBOL; it was introduced with the '02 
standard.

Second, ANSI X3.23-1985 page X-5, 1.3.8.1, Conventions for Program-Names, 
states in part "... when two programs in a run unit are identically named, 
at least one of those two programs must be directly or indirectly contained 
within another separately compiled program which does not contain the other 
of these two programs."  Thus, in this circumstance, if "sud001" were 
renamed "sud003", the CALL sud001 would have to reference something in 
*another* object code file, not this one.   The "outer" sud001 is invisible 
to sud002.

Third, Rule 3 in the same section states "If the program-name is that of a 
program which is separately compiled, that program may be referenced by 
statements included in any other program in the run unit, except programs it 
directly or indirectly contains."  I think the "if" is satisfied by the 
outermost "sud001", and the rule precludes any reference to the outer 
"sud001" from "sud002".

Fourth, ibid. page X-28, 5.2.4, CALL statement, general rule 4 describes how 
name resolution works for CALL, and the only things that can be called are 
(1) the outermost program of a (different) separate code file; (2) a sibling 
of the caller within a containing outer program; (3) a program nested within 
the caller.  From that rule, the outer "sud001" is invisible as a candidate 
for CALL from within "sud002".

Fifth, assuming unique names throughout, ibid. page X-30, general rule 15 
prohibits recursive CALLs, so even if no syntax error is generated, "sud002" 
cannot successfully call the outermost "sud001".

Now to ISO/IEC 1989:2002, page 104, 8.4.5.2, Scope of program-names:  "The 
names assigned to *programs that are contained directly or indirectly 
within* the same outermost program shall be unique within that outermost 
program."    [emphasis added]

The way I see it, that set of names does not include the program-id of the 
outermost program.  The outermost program does not contain itself, it stands 
alone.    If compiled with a 2002-compliant compiler, I would expect the 
innermost "sud001" to be called by those rules; if this innermost program 
were titled instead "sud003", then the outermost -- and 
recursivity-allowed -- program would be CALLed from within "sud002".   But 
because a nested program "sud001" exists within the calling scope of 
"sud002", that is the one that is chosen.

Thus, I don't think the behavior as to which program is chosen first from 
among a list of candidates has changed between the '85 and '02 standards; 
the program that gets called is the nested one, in both cases.

What has changed is the ability to do recursive calls, and thus at least in 
theory (pending discovery of a rule I missed preventing it!) the possibility 
does exist of calling a "parent" outermost program from inside a program 
nested within it.  But if indeed it is allowed, it would be *because* it's a 
separately-compiled program with that ID *and because* there was no "nested" 
program with that name in the scope of the caller.   In this example, again, 
if the innermost "sud001" were changed to "sud003", then I think the CALL 
would still work in '02-compliant COBOL, and the result would be a recursive 
CALL on the separartely-compiled program as a whole.

Thus, new capabilities exist in '02 COBOL, but I don't think the behavior of 
a '85-compliant program has changed as to which instantiation of "sud001" 
would get called according to the '02 standard.

    -Chuck Stevens
```

##### ↳ ↳ Re: unique program-names and contained programs

- **From:** "Karl Kiesel" <Karl.Kiesel@fujitsu-siemens.com>
- **Date:** 2005-12-21T14:03:35+01:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<dobjr7$tnq$1@nntp.fujitsu-siemens.com>`
- **References:** `<do6bi2$mvq$1@nntp.fujitsu-siemens.com> <do6pma$1f1u$1@si05.rsvl.unisys.com>`

```
"Chuck Stevens" <charles.stevens@unisys.com> schrieb im Newsbeitrag 
news:do6pma$1f1u$1@si05.rsvl.unisys.com...
>... The most immediate reason that the program wouldn't compile with a 
>1985-compliant compiler is that the RECURSIVE phrase of the PROGRAM-ID 
>paragraph is not part of 1985 COBOL; it was introduced with the '02 
>standard.
ok, my error, trying to use RECURSIVE in context of Standard 1985

> ... Fifth, assuming unique names throughout, ibid. page X-30, general rule 
> 15 prohibits recursive CALLs, so even if no syntax error is generated, 
> "sud002" cannot successfully call the outermost "sud001".
well, assuming the same example program, but without the RECURSIVE clause, I 
think that the innermost 'sud001' must be called; but there still remains 
the the requirement (4.2.2.1.1, IV-7) '...Further, all user-defined words 
within a given disjoint set must be unique...'. Thus, even if the outermost 
'sud001' may never be called according to the rules in chapter X, alone 
naming it the same as one of the icontained programs violates this 
uniqueness and therfore the program does not conform to Standard 1985

> Now to ISO/IEC 1989:2002, page 104, 8.4.5.2, Scope of program-names:  "The 
> names assigned to *programs that are contained directly or indirectly 
…[6 more quoted lines elided]…
> expect the innermost "sud001" to be called by those rules;
this was also my first thought, but according do 8.4.5.2 (page 104,105) both 
'sud001' are in the scope of the CALL satement: the innermost 'sud001' 
according to rule 1) and the outermost 'sud001' according to rule 3). What I 
thought was missing here, is some 'priority rule', which of the several 
candidates to choose. Meanwhile I think, as Rick Smith already remarked, 
that 8.4.5.1 'local and global names' can be used as 'priority' rule, that 
will select the innermost 'sud001' (even if the wording used there does not 
match exactly the situation of program names - is the contained 'sud001' a 
*local* name, which is *declared* in 'sud002' ?!)

Thanks for Your consideration
Karl Kiesel
```

###### ↳ ↳ ↳ Re: unique program-names and contained programs

- **From:** "Chuck Stevens" <charles.stevens@unisys.com>
- **Date:** 2005-12-21T10:17:41-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<doc686$1kov$1@si05.rsvl.unisys.com>`
- **References:** `<do6bi2$mvq$1@nntp.fujitsu-siemens.com> <do6pma$1f1u$1@si05.rsvl.unisys.com> <dobjr7$tnq$1@nntp.fujitsu-siemens.com>`

```

"Karl Kiesel" <Karl.Kiesel@fujitsu-siemens.com> wrote in message
news:dobjr7$tnq$1@nntp.fujitsu-siemens.com...
> "Chuck Stevens" <charles.stevens@unisys.com> schrieb im Newsbeitrag
> news:do6pma$1f1u$1@si05.rsvl.unisys.com...
…[8 more quoted lines elided]…
>> generated, "sud002" cannot successfully call the outermost "sud001".

> well, assuming the same example program, but without the RECURSIVE clause,
> I think that the innermost 'sud001' must be called;

We agree; it matches page X-28 , 5.2.3, CALL statement, General Rule 4. as
well as Page X-5, 1.3.8.1, Conventions for Program-Names.

> but there still remains the the requirement (4.2.2.1.1, IV-7) '...Further,
> all user-defined words within a given disjoint set must be unique...'.
…[3 more quoted lines elided]…
> conform to Standard 1985

I do not believe that to be the case, given that reference to the
"outermost" sud001 can only occur from outside the compiled program.  Note
also the exclusion on page IV-6:  "Within a given source program, *but
excluding any contained program*, the user-defined words are grouped into
the following disjoint sets: " [emphasis added].   The "outermost" sud001
and the "innermost" sud001 are *not in* the same "given disjoint set".

>> Now to ISO/IEC 1989:2002, page 104, 8.4.5.2, Scope of program-names:
>> "The names assigned to *programs that are contained directly or
…[6 more quoted lines elided]…
>> expect the innermost "sud001" to be called by those rules;

> this was also my first thought, but according do 8.4.5.2 (page 104,105)
> both 'sud001' are in the scope of the CALL satement: the innermost
> 'sud001' according to rule 1) and the outermost 'sud001' according to rule
> 3).

Since rule 1) applies, rule 3) is irrelevant to the point.  It only tries an
"outside" call if the PROGRAM-ID can't be located among the nested programs.


> What I thought was missing here, is some 'priority rule', which of the
> several candidates to choose.

I don't.  The system is always supposed to pick an eligible nested program
first, and only if there isn't one, *then* it looks for an outside program.

> Meanwhile I think, as Rick Smith already remarked, that 8.4.5.1 'local and
> global names' can be used as 'priority' rule, that will select the
> innermost 'sud001' (even if the wording used there does not match exactly
> the situation of program names - is the contained 'sud001' a *local* name,
> which is *declared* in 'sud002' ?!)

Yes.


    -Chuck Stevens
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
