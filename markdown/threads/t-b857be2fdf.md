[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# SOLVED Embedded SQL and MS ACCESS dates

_2 messages · 2 participants · 2007-11_

**Topics:** [`Databases and SQL`](../topics.md#databases)

---

### SOLVED Embedded SQL and MS ACCESS dates

- **From:** "Pete Dashwood" <dashwood@removethis.enternet.co.nz>
- **Date:** 2007-11-05T15:10:01+13:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<5p7cbpFpur8tU1@mid.individual.net>`

```
OK, this one is now solved.

Many thanks to all who tried to help.

Before I post the solution, a few observations...

1. Apparently, the number of people using COBOL for RDB Access on a PC is 
"small"... This surprises me because the PC is an ideal platform for testing 
RDBs before scaling them to something else, and many people with COBOL 
backgrounds will be working daily in environments where RDBMS is the norm. 
Millions of people are using RDBs on PCs; they're just not doing it in 
COBOL... :-)

2. Because COBOL pre-dates RDBMS, and the COBOL Standards authorities have 
not considered a standard COBOL SQL interface to be necessary, support for 
RDBMS is pretty much vendor specific when using COBOL. Having said that, 
both MicroFocus and Fujitsu do provide good SQL support (I'm sure the others 
do too, but I'm limiting my comments to my own experience), and the field is 
so huge that detailed examples are thin on the ground. None of the examples 
I found in Fujitsu docs showed Date type fields being accessed. (Probably 
because different RDBMS have their own Date support and it is just too huge 
to cover...)

3. As modern PC based RDBMS have become more powerful (even MS Access is 
using the SQL Server engine now) the facilities provided by each system are 
way beyond embedded SQL. The modern approach is to connect briefly, get a 
result set, disconnect, then process the result set off-line.  Stepping 
through DB Tables with embedded cursors is just too expensive on resources.

4. Perceptions from the past tend to colour judgements. "Everyone knows" 
that MS Access performance is abysmal and facilities are limited... Except 
that for several years now it has not been like that at all. I use MySQL 
(really good free system) and sometimes I have found that Access  is better. 
I don't believe there are any "bad" RDBMS these days because the market 
place is so competitive that anything useless falls by the wayside.

OK, now to the specific problem...

1. I have a very large, complex ISAM file which has many fields (a number of 
which are dates), alternate indices and repeating groups on it, in a single 
record type, and it must load into a set of DB Tables which are all 
connected through enforced constraints and referential integrity. (The idea 
is to create the Base table first, then create the dependent tables, for 
each ISAM record encountered.)

2. The data on this file has not been cleansed so the load program does some 
basic stuff for it. For example, some of the dates are zero which is fine 
for ISAM but tends to upset a RDB...(load sets them to 01/01/1900).

3. Some of the alpha fields have embedded x'00' in them and this is also 
pretty disastrous when you try to insert them to a RDB.

Basically, if this file can be loaded, anything can be loaded :-)

I encountered the 22005 SQLSTATE and looked it up. The load program also 
does a snapshot showing what is in each ISAM field and the corresponding 
Host Variable, when an INSERT fails. From this, I was able to establish that 
some fields had nulls in them, but it was pretty tedious and error prone. 
(When you have pages of Variables it is easy to miss one...)

The load program takes the ISAM Date (string) and pushes it through a 
component that provides the date in 8 different formats, including the 
floating point one which worked previously with Access 97.

So, was it a problem with data fields or dates?

The Web was adamant that dates cause this problem, so I resolved to 
eliminate the  data fields. However, it would be much too time consuming to 
amend the target DB, amend the HVs,  amend all the moves that load the HVs, 
and there would still be no guarantee as to what was causing the dates to 
raise this exception (if it was the dates...).

So, instead, I simply initialized the ISAM record, after reading it, then 
replacedthe key information and some of the dates that were in it when it 
was read.

Same result.

This made me pretty sure it was the dates, as the data fields were all 
initialized to valid spaces or zero.

At this point I removed the component and hand coded all the various 
permutations I posted in my original.

Same result.

More time searching the Web and finding many people having or had similar 
problems, but, of course, no COBOL examples... Nevertheless, it was all good 
background and I learned much.

This morning I decided to create a small DB, based on the real one, and 
modify a copy of the real load program to access it.

It ONLY has date fields on it (and the primary key of course).

Plugged in the component that converts dates from string, ran it, it worked 
perfectly!

So my problem is NOT with dates, it is elsewhere in the humungous ISAM 
record, or in the generated definitions of the RDB Tables.

For reference, here is a way of getting dates from COBOL to MS ACCESS and I 
can guarantee it works... (There may be other ways, but this is definitely 
OK)

002700     EXEC SQL BEGIN DECLARE SECTION END-EXEC.
002710* HOST VARIABLE definitions for table: MRRESV-REC
002720* Generated on: 04-Nov-2007   at: 02:27:00.51
002730*
002740* PRIMARY Key field(s): HV-MRRESV-CD,  HV-MRRESV-RESERVATION
002750*
002760 01  HV-MRRESV-CD                                picture s9(10).
002770 01  HV-MRRESV-RESERVATION           picture s9(10).
...
002900 01  HV-MRRESV-DATE-ENTERED          comp-2.
002990 01  HV-MRRESV-BED-TAX-DATE          comp-2.
...

004350* Other useful Host Variables...
004360 01  SQLSTATE    PIC X(5).
004370 01  SQLMSG      PIC X(128).
004380     EXEC SQL END DECLARE SECTION END-EXEC.
004390* END of HOST VARIABLE definitions for MRRESV-RECrg08
004400* Number of lines generated by DECLGEN= 171

Note the date Host Variables defined as 64 bit floating point.

Now, consider we have an ISAM record that contains the above fields, among 
others...

Process the date entered.

1. Pass it to the component.
2. Take the component's floating point date property and move it to the Host 
Variable
3. Insert to the DB using the host variable.

ACCESS accepts this date/time into a column designated as "Date/Time" on the 
DB definition.


How does the component derive an acceptable float?

here's a breakdown:

1. Analyse the passed date string and derive   YYYYMMDD
2. Use the COBOL intrinsic functions to derive the number of days since 
01/01/1900, for the date in 1 above.
    (This requires arithmetic as COBOL uses a base date around 1600...)
3. Load the float with this number. (MOVE)
4. Derive the time as a fraction of ticks since midnight (noon would be .5)
5. ADD the derived "tick fraction" to the float.

Here's some actual COBOL :-)...
Data fields:
...
01  ticks   pic s9(7) comp-5.
 01  ticks-alpha.
     12 ticks-hh   pic 99.
     12 ticks-mm   pic 99.
 01  ticks-rem                    pic 9999.
01  fp-work    pic s9(9)v9(9).
 01  filler redefines fp-work.
     12 fp-integer  pic s9(9).
     12 fp-dec   pic v9(9).
 01  access2k-fp                  pic s9(14)v9(4).
 01  access2k-fp-x redefines access2k-fp.
     12 filler pic x(18).
...
Procedure code:
...
                 if lnk-vb-date < 1
024170*
024180* Calculate the "date" part of the floating point number.
024190* Should be days since 31st December, 1899. We subtract the COBOL
024200* days for that date from the COBOL days for the given date and
024210* place it in the "left" side of the decimal. There may already
024220* be a time on the "right" side of the decimal, so can't test
024230* equal zero...
024240*
024250        move lnk-vb-date to fp-work
024260        compute fp-integer = lnk-integer - ws-1900-start-int + 2
024270        move fp-work to lnk-vb-date
024280     end-if
024290     if fp-dec NOT = zero
024300*
024310* convert the time into English 24 hour. The exact opposite of
024320* b008-time...
024330           compute ticks rounded = 86400 * fp-dec
024340           divide 3600 into ticks giving ticks-hh
024350                  remainder ticks-rem
024360           divide 60 into ticks-rem
024370                  giving ticks-mm
024380           move ticks-alpha to lnk-time
024390     else
024400* There was no time passed so set current...
024410           move ws-today (9:4) to lnk-time
024420           perform b008-time
024430     end-if
024440

These routines are used get a date string from the float if the date has 
been read from the DB, using the same Host Variable...

025280*-----------------------------------------------------------------
025290 b008-time         section.
025300 b008-note.
025310*
025320*   This section is part of the MicroSoft "Date" datatype
025330*   conversion. If a time is passed it must be converted and
025340*   placed in the 64 bit floating point format for MS.
025350*
025360*   The time occupies the "right" hand side of the decimal point
025370*   and represents the seconds since midnight ("ticks") as a
025380*   decimal fraction of the total seconds in a day (86400)
025390*
025400*   Midnight is zero; Midday is .50.
025410*
025420     move lnk-vb-date to fp-work
025430     move lnk-time to ticks-alpha
025440     compute fp-dec = ((ticks-hh * 3600)
025450                     + (ticks-mm * 60)) /  86400
025460     move fp-work to lnk-vb-date
025470     if fp-integer not = zero
025480        perform b009-vb-date
025490     end-if
025500    .
025510 b008.
025520    exit.
025530*-----------------------------------------------------------------
025540 b009-vb-date         section.
025550 b009-note.
025560*
025570*   This section is part of the MicroSoft "Date" datatype
025580*   conversion.  If a date is passed it must be converted and
025590*   placed in the 64 bit floating point format for MS.
025600*
025610*   The date occupies the "left" hand side of the decimal point
025620*   and represents the number of days since 31/12/1899. (1st
025630*   January, 1900 was a Monday). As COBOL's base date is 01/01/1600
025640*   it is necessary to do some calculation... The date calculated
025650*   will be placed in ws-date-area.
025660*
025670     move lnk-vb-date to fp-work
025680     if fp-integer > 100000
025690     *> this is access 2K date with a timestamp in it...
025700        move lnk-vb-date to access2k-fp
025710        move access2k-fp-x (1:8) to ws-date-area
025720        move access2k-fp-x (9:4) to lnk-time
025730     else
025740        compute ticks = fp-integer + ws-1900-start-int - 2
025750        compute ws-date-area-num = function date-of-integer (ticks)
025760     end-if
025770*
025780*   Can't do anything about the time as zero is valid (midnight).
025790     .
025800 b008.
025810    exit.
025820

Finally,

thanks again to everyone who tried to help.

Pete.
```

#### ↳ Re: SOLVED Embedded SQL and MS ACCESS dates

- **From:** Rene_Surop <infodynamics_ph@yahoo.com>
- **Date:** 2007-11-05T22:30:00-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1194330600.104459.33390@v23g2000prn.googlegroups.com>`
- **In-Reply-To:** `<5p7cbpFpur8tU1@mid.individual.net>`
- **References:** `<5p7cbpFpur8tU1@mid.individual.net>`

```
On Nov 5, 10:10 am, "Pete Dashwood"
<dashw...@removethis.enternet.co.nz> wrote:
> OK, this one is now solved.
>
…[9 more quoted lines elided]…
> COBOL... :-)

I will count myself using RDB in Cobol, mostly on MySQL and MS/SQL
Server integration. But MS Access? Haven't use the MS Access even for
testing.

Most developers here used MS Access as a temporary dumping ground...
and there's a lot of them uses it for such purpose. But then you're
correct, they're not doing it in Cobol :-)
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
