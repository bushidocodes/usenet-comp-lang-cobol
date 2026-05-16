[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Old-and-New - Debugging Lines

_6 messages · 4 participants · 2003-06_

---

### Old-and-New - Debugging Lines

- **From:** "William M. Klein" <wmklein@ix.netcom.com>
- **Date:** 2003-06-03T22:58:03-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<bbjqoe$p7l$1@slb4.atl.mindspring.net>`

```
For those who don't have a <good> interactive debugger, the use of
"debugging lines" has always been useful.  This feature is marked as
OBSOLETE in the 2002 Standard - so they will be gone in the next Standard.
The following shows what feature can be used (besides an interactive
debugger) to accomplish the old task.

Old Code:

       Identification Division.
        Program-Id. DebugConditional.
       Environment Division.
        Configuration Section.
         Source-Computer. AnyWhere
               with Debugging Mode
                .
       Procedure Division.
        Mainline.
      D    Perform While-Testing
           Perform Always-Do
           Display "   Shown"
           Stop Run
            .
        While-Testing.
           Display "This is only shown"
            .
        Always-Do.
      D    Display "   When Debugging Mode is specified"
           Display "While this is always"
            .

New Code (Minimal changes):

       Identification Division.
        Program-Id. DebugConditional.
       Environment Division.
        Configuration Section.
         Source-Computer. AnyWhere
        >>Define Debug-Mode  as "YES"
                .
       Procedure Division.
        Mainline.
         >>IF Debug-Mode = "YES"
           Perform While-Testing
         >>End
           Perform Always-Do
           Display "   Shown"
           Stop Run
            .
        While-Testing.
           Display "This is only shown"
            .
        Always-Do.
            >>IF Debug-Mode = "YES"
          Display "   When Debugging Mode is specified"
            >>End-IF
           Display "While this is always"
            .

New Code (A couple more valid changes):

  Program-Id. DebugConditional.
 >>Define Debug-Mode  as "YES"
   Procedure Division.
    Mainline.
  >>IF Debug-Mode = "YES"
           Perform While-Testing
  >>End
  Perform Always-Do
  Display "   Shown"
  Stop Run
            .
  While-Testing.      Display "This is only shown"
            .
  Always-Do.
  >>IF Debug-Mode = "YES"
          Display "   When Debugging Mode is specified"
    >>End-IF
           Display "While this is always"
            .
```

#### ↳ Re: Old-and-New - Debugging Lines

- **From:** "William M. Klein" <wmklein@ix.netcom.com>
- **Date:** 2003-06-03T23:21:56-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<bbjs57$17j$1@slb2.atl.mindspring.net>`
- **References:** `<bbjqoe$p7l$1@slb4.atl.mindspring.net>`

```
I should have put in my original note that there are LOTS of other reasons
for using "conditional compilation" - and many other things that it can do.
Among other "purposes" that it can serve is

 - the ability to "single source" slight-variations of the same program -
such as the weekly, monthly, quarterly, and annual versions of a "report"
program

 - keeping multiple "maintenance levels" of a program all stored in a
"single source"

 - keeping variations of the same program for different customers
single-sourced

and many other purposes.
```

#### ↳ Re: Old-and-New - Debugging Lines

- **From:** Karl Kiesel <Karl.Kiesel@fujitsu-siemens.com>
- **Date:** 2003-06-04T14:23:30+02:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3EDDE4C2.88778885@fujitsu-siemens.com>`
- **References:** `<bbjqoe$p7l$1@slb4.atl.mindspring.net>`

```
"William M. Klein" schrieb:
> 
> New Code (A couple more valid changes):
…[7 more quoted lines elided]…
>   >>End

The '-If' got lost on the >>End-If; but let me highlight an other
feature: 
in the example, switching the Debug-Mode requires change of source and a
recompilation; COBOL 2002 enhances flexibility here: it is possible to
obtain values from the operating environment; if Debug-Mode were defined
as 
   >>Define Debug-Mode as PARAMETER
thus no more source changes, but simply recompilation with appropriate
values provided via operating environment!
In case no value was provided, error handling should be done too, which
results in something like:
   >>Define Debug-Mode as Parameter
   >>If Debug-Mode is NOT DEFINED
     >>Define Debug-Mode as "some-default-value"
   >>End-If

regards
K. Kiesel
```

##### ↳ ↳ Re: Old-and-New - Debugging Lines

- **From:** riplin@Azonic.co.nz (Richard)
- **Date:** 2003-06-04T12:32:08-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<217e491a.0306041132.20ca4487@posting.google.com>`
- **References:** `<bbjqoe$p7l$1@slb4.atl.mindspring.net> <3EDDE4C2.88778885@fujitsu-siemens.com>`

```
Karl Kiesel <Karl.Kiesel@fujitsu-siemens.com> wrote

> in the example, switching the Debug-Mode requires change of source and a
> recompilation; COBOL 2002 enhances flexibility here: it is possible to
…[4 more quoted lines elided]…
> values provided via operating environment!

That does have a slight disadvantage that inspecting the current
source code doesn't necessarily tell you whether the latest compile
has it on or off, a compiler listing should tell you, but I don't
usually keep them.

My own preference for 'debugging' lines is to use a run-time
parameter.  This can be set on or off in a configuration or control
file, or for interactive systems may be set by a flag on the login
name.  Usually my debug data goes out to a log file or otherwise to a
line sequential file or puts additinal information on screens or
popups.

This allows the live system to run without clutter, if the user finds
a problem then running the same version with the flag on may give more
details of what is happening.
```

#### ↳ Re: Old-and-New - Debugging Lines

- **From:** LX-i <DanielJSNOSPAM@Knology.net>
- **Date:** 2003-06-04T17:56:11-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3EDE790B.4000108@Knology.net>`
- **References:** `<bbjqoe$p7l$1@slb4.atl.mindspring.net>`

```
Do you actually preface the lines with >>?  And I noticed you just have 
 >>End as opposed to >>End-If.  Is that an "oops", or is that really how 
it's done?

<example below>
William M. Klein wrote:
>   Program-Id. DebugConditional.
>  >>Define Debug-Mode  as "YES"
…[16 more quoted lines elided]…
>             .
```

##### ↳ ↳ Re: Old-and-New - Debugging Lines

- **From:** "William M. Klein" <wmklein@ix.netcom.com>
- **Date:** 2003-06-04T18:39:51-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<bbm00a$78e$1@slb4.atl.mindspring.net>`
- **References:** `<bbjqoe$p7l$1@slb4.atl.mindspring.net> <3EDE790B.4000108@Knology.net>`

```
Yes, ">>" is the beginning of ALL the new "compiler directives".

Yes,  ">>END" was an "oops"  and should be ">>END-IF"
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
