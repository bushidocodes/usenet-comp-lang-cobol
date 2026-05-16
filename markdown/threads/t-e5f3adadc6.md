[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# ENTRY points

_8 messages · 6 participants · 2000-09_

---

### ENTRY points

- **From:** "Mike Sheehan" <msheehan@pks.ie>
- **Date:** 2000-09-18T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8q5e17$k21$1@kermit.esat.net>`

```
I've found a reference to multiple entry points to a sub-program that is not
part of the COBOL ISO Standard.
It does not look as it will be a part of the next standard either.

You can call an entry point in call statement e.g. CALL "entrypoint1"

Are entry points problematic in some way?

2ndly, how does the calling program know where the entry point is?
The sub-program name is not in the CALL. so does the CALL statement search a
library for a source that has that entry point name.
What if there are two sub-programs with the same entry point name?

I'm looking at how a COBOL 85 program could implement an interface in a
similar way as an Ada package (or Pascal Unit). it probably cannot be done
using COBOL85 syntax?

Mike
```

#### ↳ Re: ENTRY points

- **From:** thaneH@softwaresimple.com (Thane Hubbell)
- **Date:** 2000-09-18T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<39c645c5.54154493@207.126.101.100>`
- **References:** `<8q5e17$k21$1@kermit.esat.net>`

```
I am not positive about this - Bill K can help us I think -- but would
not nested programs solve this problem?  Each "entry point" is a
separate program and shared storage is declared as GLOBAL.

On Mon, 18 Sep 2000 17:03:25 +0100, "Mike Sheehan" <msheehan@pks.ie>
wrote:

>I've found a reference to multiple entry points to a sub-program that is not
>part of the COBOL ISO Standard.
…[19 more quoted lines elided]…
>

---
Try a better search engine:  http://www.google.com
My personal web site: http://www.geocities.com/Eureka/2006/
```

##### ↳ ↳ Re: ENTRY points

- **From:** Support@ScreenIO.com (Kevin J. Hansen)
- **Date:** 2000-09-18T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<39c6505b.8145773@news>`
- **References:** `<8q5e17$k21$1@kermit.esat.net> <39c645c5.54154493@207.126.101.100>`

```
You can define a program with multiple entry points, and it's quite
handy for some applications.  We use it to map our COBOL API calls to
Windows format API calls, like this:

PROGRAM-ID.  GSAPI.
.
.
ENTRY 'GX_CREATEWINDOWEX' USING arguments
.
GOBACK.
ENTRY 'GX'_UPDATEWINDOW' USING arguments
.
GOBACK.

and so on.

The nice thing is that all related entrypoints reside in a single
source (and object) module.  It makes maintenance easier because you
don't need to remember (or find) the one of a gazillion source files
you need, and because you can use the same WORKING-STORAGE and LINKAGE
SECTION data definitions from any/all of the entries in the module.

Another reason to use multiple entry points is that each entry has its
own argument list; because COBOL won't let you vary the number of
arguments you call a routine with, this is a way to have multiple
entries into a routine, with each one having a different number of
arguments.

As for how they're found when you CALL one of the alternate entry
points, if you call the entry point statically; e.g., CALL
'GX_CREATEWINDOWEX' the linker finds and resolves the called address.

If you call the routine dynamically, you must call the main entry
point first (the name of the .DLL), henceforth the OS or the COBOL
runtime will generally have access to other entrypoints in the DLL.

One thing you need to watch out for is that some compilers default to
converting static calls to dynamic calls.  Obviously this can cause
problems if you don't call the main entry first in your application.
Merant is one of these...

Clear as mud?

Kevin


On Mon, 18 Sep 2000 16:42:31 GMT, thaneH@softwaresimple.com (Thane
Hubbell) wrote:

>I am not positive about this - Bill K can help us I think -- but would
>not nested programs solve this problem?  Each "entry point" is a
…[20 more quoted lines elided]…
>>using COBOL85 syntax?


Norcom - COBOL Programming Tools
GUI ScreenIO - A Windows UI for COBOL
http://www.screenio.com
```

###### ↳ ↳ ↳ Re: ENTRY points

- **From:** thaneH@softwaresimple.com (Thane Hubbell)
- **Date:** 2000-09-18T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<39c66d23.64233604@207.126.101.100>`
- **References:** `<8q5e17$k21$1@kermit.esat.net> <39c645c5.54154493@207.126.101.100> <39c6505b.8145773@news>`

```
I don't think the question is can it be done, the question is can it
be done with Standard COBOL.  


On Mon, 18 Sep 2000 17:35:17 GMT, Support@ScreenIO.com (Kevin J.
Hansen) wrote:

>You can define a program with multiple entry points, and it's quite
>handy for some applications.  We use it to map our COBOL API calls to
…[74 more quoted lines elided]…
>http://www.screenio.com

---
Try a better search engine:  http://www.google.com
My personal web site: http://www.geocities.com/Eureka/2006/
```

#### ↳ Re: ENTRY points

- **From:** scomstock@aol.com (S Comstock)
- **Date:** 2000-09-18T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<20000918141637.11994.00000110@ng-fk1.aol.com>`
- **References:** `<8q5e17$k21$1@kermit.esat.net>`

```
Mike writes...

>I've found a reference to multiple entry points to a sub-program that is not
>part of the COBOL ISO Standard.
…[13 more quoted lines elided]…
>using COBOL85 syntax?

You didn't say what platform you're on, but I can answer your questions for the
OS/390 base.

Entry points are not problematic here, they are simply little known and, for
that reason, seldom used. But they are very useful.

In fact, mutliple entry points can accomplish almost everything done by DLLs in
a mainframe, and I think maybe the people bragging about DLLs being available
on the mainframe aren't even aware of alternative entry points.

Now, as far as a CALL making the connection to an alternate entry point, there
are some options:

1) Static calls
  a) if the caller calls the main entry point (program-id name) as well as an
alternate entry point, the alternate entry point can be found at link (bind)
time, since the subroutine load module is brought into memory for linking

  b) if the caller only class an alternate entry point then either:
      i) at link time of the calling program you need to explicitly INCLUDE the
         load module using a linkage editor control statement like
            INCLUDE DDNAME(PGMNAME)
         where PGMNAME is the name in the directory for the load module and
DDNAME
         is a name you make up; (you must supply this DD statement in the link
edit step,
         then; it points to the library (PDS or PDSE) containing the
subroutine's load module)
      or
      ii) at link time of the subroutine, build an ALIAS for the alternate
entry point by 
         including a link edit control statement like this:
            ALIAS DIRNAME(ENTPTNAME)
         where DIRNAME is the name you are specifying in your CALL and 
         ENTPTNAME is the name identified by an ENTRY statement in the COBOL
         program (they are normally the same); this puts an entry in the
directory
         of the load module library that points to the same load module as the
main,
         but indicates where the alternat entry point begins

2) Dynamic calls
    the only way a dynamic call of an alternate entry point can be resolved is
if
    you use option b.ii) above, set up an ALIAS when you link the subroutine

Note that you can have multiple alternate entry points, and multiple aliases.
Also, you can call alternate entry points across language boundaries.

Note also that people coding programs with alternate entry points need to make
sure any logic conflicts are allowed for and that details of what is going on
are clearly documented for subsequent maintenance programmers.

We cover this (and a whole lot more) in our class "Inter-Language Communication
in OS/390". Check http:www//trainersfriend.com for details (follow link to
complete course list to that course (course code M220 in our scheme)).

Regards,


Steve Comstock
Telephone: 303-393-8716
www.trainersfriend.com
email: steve@trainersfriend.com
256-B S. Monaco Parkway
Denver, CO 80224
USA
```

#### ↳ Re: ENTRY points

- **From:** "William M. Klein" <wmklein@nospam.ix.netcom.com>
- **Date:** 2000-09-18T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8q5r1q$1g9$1@slb7.atl.mindspring.net>`
- **References:** `<8q5e17$k21$1@kermit.esat.net>`

```
1) The ENTRY statement (and alternate entry points) are NOT a part of any
past or proposed ANSI/ISO COBOL Standard.

2) IBM COBOL has (and continues) to support them.  ENTRY point resolution is
USUALLY handled by implicit or explicit linkage editor/binder statements.
(Many compilers that provide IBM "emulation" also support them)

3) IBM does document some "gotchas" when you use them.  For example, you may
NOT call dynamically and statically the same entry point in the same
run-unit - without causing "potential" problems.

4) J4 and WG4 have consistently REJECTED adding them to Standard COBOL

5) If you are interested in writing "truly portable" COBOL, then you should
avoid their use.

6) If you use an "EVALUATE" (or comparable) statement at the beginning of
your Procedure Division and then use nested programs (or even
paragraphs/sections), then you can provide "comparable" functionality.

  ***
does this answer all the questions?
```

#### ↳ Re: ENTRY points

- **From:** Daniel Jacot <djacot@my-deja.com>
- **Date:** 2000-09-19T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8q74g3$o3o$1@nnrp1.deja.com>`
- **References:** `<8q5e17$k21$1@kermit.esat.net>`

```
I will not answer to your first questions since Steve described very
clearly what you have to do.
And I don't know of 'Ada package' and 'Pascal Unit', but if these are
about the same as a DLLs in Windows, then you could think about using
DLLs in OS/390 too. There is a restriction that you cannot mix dynamic
calls and DLL calls in the same program, but at least it is 'standard'
since no 'ENTRY' statement is needed.

So, IF you do not need to mix old and new programs AND you have the most
current compiler available (COBOL for OS/390 & VM Version 2.1) THEN you
can use DLL linkage (and mix COBOL, C, C++ and VA PL/I DLLs).

You produce DLLs like that:

        CBL DLL,PGMNAME(LONGMIXED),EXPORTALL
        Program-Id "First_Entry_of_my_DLL".
        ....
        ....
        End Program "First_Entry_of_my_DLL".

        Program-Id "Second_Entry_of_my_DLL".
        ....
        ....
        End Program "Second_Entry_of_my_DLL".

All the DLLs are in the same source file and they are NOT nested and
they cannot share global variables.

The Prelink-utility or, if you use PDSE, the Binder produces an 'IMPORT'
statement for each Program-Id you used (on a file with DDNAME
'SYSDEFSD').

You compile the calling program with the same compiler-options as you
used in the DLL (except EXPORTALL if the calling program is a main
program). And you add the generated 'IMPORT' commands to the SYSLIN of
the Prelinker- or the Binder-Input. That's all. And yes, you call the
entries like:
CALL "First_Entry_of_my_DLL" USING ....
No more restriction on 8 characters. That's fine, isn't it?


In article <8q5e17$k21$1@kermit.esat.net>,
  "Mike Sheehan" <msheehan@pks.ie> wrote:
> I've found a reference to multiple entry points to a sub-program that
is not
> part of the COBOL ISO Standard.
> It does not look as it will be a part of the next standard either.
…[6 more quoted lines elided]…
> The sub-program name is not in the CALL. so does the CALL statement
search a
> library for a source that has that entry point name.
> What if there are two sub-programs with the same entry point name?
>
> I'm looking at how a COBOL 85 program could implement an interface in
a
> similar way as an Ada package (or Pascal Unit). it probably cannot be
done
> using COBOL85 syntax?
>
> Mike
>
>
```

##### ↳ ↳ Re: ENTRY points

- **From:** "Mike Sheehan" <msheehan@pks.ie>
- **Date:** 2000-09-19T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8q787t$ca5$1@kermit.esat.net>`
- **References:** `<8q5e17$k21$1@kermit.esat.net> <8q74g3$o3o$1@nnrp1.deja.com>`

```
fyi,
Ada packages are used to create Abstract Data Types...

An Ada package allows you to define a public interface that is separately
compilable from the implementation body...

The advantage is that you can have an public interface - stub in your
programs that declares the functions/procedures and the parameters
involved - and you can change the implementation without affecting the
calling program.
The package body is private, hidden, and so gives you encapsulation...

This is a very powerful facility as it allows for information hiding and
modularisation.
It would fall short of a class/object as inheritance is not directly
available, but, where, inheritance is not required, ideal...

My interest is in how COBOL85 could enable (if not support) such a package
concept, however, it should be far easier to implement in the next version
of the standard using OO facilities. The DLL approach seems a suitable
alternative...

Mike

package LeapYearPackage is

subtype year_type is integer range 1600..9999;
subtype day_number_type is integer range 0..366;

type day_of_week_type is (friday, saturday, sunday, monday,
                            tuesday, wednesday, thursday);

function isleap(year : year_type) return boolean;
function days_since_1600(year : year_type; day_this_year : day_number_type)
                     return integer;

function DayOfWeek(year : year_type; day_this_year : day_number_type)
                                          return day_of_week_type;
end LeapYearPackage;


With Ada.Text_IO, Ada.Integer_Text_IO;
use Ada.Text_IO, Ada.Integer_Text_IO;


package body LeapYearPackage is


function isleap(year : year_type) return boolean is
begin
-- Checks if year is a leap year
   if (year mod 4 = 0 and year mod 100 /= 0)
        or year mod 400 =0 then
       return TRUE;
   else
       return FALSE;
   end if;
end isleap;

function days_since_1600(year : year_type; day_this_year : day_number_type)
                                          return integer is
   diff_year, days_to_last_year, total_days : integer;
 begin
   diff_year := year - year_type'first;
   days_to_last_year := (diff_year * 365) + (diff_year / 4) -
                 (diff_year / 100) + (diff_year / 400) + 1;
                          -- 1 for the leap year 1600!!!!!!!!
   total_days := days_to_last_year + day_this_year;
   return total_days;
end days_since_1600;

function DayOfWeek(year : year_type; day_this_year : day_number_type)
                                          return day_of_week_type is

    day_of_week : day_of_week_type; -- 0 is friday
   total_days : integer;
begin
  total_days := days_since_1600(year,day_this_year);
  day_of_week :=  day_of_week_type'val(total_days mod 7);
  return day_of_week;
--  return day_of_week_type'val(total_days mod 7);

end  DayOfWeek ;

end LeapYearPackage;

Daniel Jacot <djacot@my-deja.com> wrote in message
news:8q74g3$o3o$1@nnrp1.deja.com...
> I will not answer to your first questions since Steve described very
> clearly what you have to do.
…[48 more quoted lines elided]…
> > Are entry points problematic in some way?
[snip]
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
