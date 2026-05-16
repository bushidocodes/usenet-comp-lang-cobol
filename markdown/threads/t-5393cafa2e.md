[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Fujitsu Query

_15 messages · 6 participants · 1999-10_

**Topics:** [`Compilers and vendors`](../topics.md#compilers)

---

### Fujitsu Query

- **From:** "Jerry P" <bismail@bisusa.com>
- **Date:** 1999-10-02T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<WyAJ3.2251$mN5.102464@typhoon01.swbell.net>`

```
Suppose:
1. User enters data in field "A" and attempts to exit via
Tab, Return, or mouse click, destination: field "B."
2. Program gets control and attempts to
validate user-supplied data in "A". Data are found
to be wrong and (after suitable message)
control is forced to the beginning of field "A"
(via a SetFocus) so user can make corrections.
3. However, this SetFocus to "A" causes loss of
focus from "B"  (where control has apparently moved).
The SetFocus to "A"  triggers a LostFocus for "B,"
which may have validation tests for "B" and a SetFocus
of its own. The whole thing spirals out of control.
Endless loops, dogs marrying cats. It's just awful.

Fujitsu support has mulled, is mulling, will mull.

Any suggestions?


--------------------------------------------------------------------
"I opened my Windows 95 manual and fell into a magical place."
```

#### ↳ Re: Fujitsu Query

- **From:** "Judson McClendon" <judmc123@bellsouth.net>
- **Date:** 1999-10-03T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<LdIJ3.8373$Iv5.69013@news2.mia>`
- **References:** `<WyAJ3.2251$mN5.102464@typhoon01.swbell.net>`

```
Yes.  Validate on a screen, not field, basis, then SetFocus to the
first error you find.
```

##### ↳ ↳ Re: Fujitsu Query

- **From:** "Jerry P" <bismail@bisusa.com>
- **Date:** 1999-10-03T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<QtOJ3.2694$mN5.147328@typhoon01.swbell.net>`
- **References:** `<WyAJ3.2251$mN5.102464@typhoon01.swbell.net> <LdIJ3.8373$Iv5.69013@news2.mia>`

```

Judson McClendon <judmc123@bellsouth.net> wrote in message
news:LdIJ3.8373$Iv5.69013@news2.mia...
> Yes.  Validate on a screen, not field, basis, then SetFocus to the
> first error you find.

That isn't reasonable:
1. One screen has 108 editable fields on it. Others are similarly
packed.
2. The length of time the record would have to be locked while
the user --- well, you get the idea.
3. VB has a control (I'm told) called VALIDATE that gives you
an opportunity to stay in the field.
4. One circumvention we've considered is starting each
LostFocus event with:

    IF ALLOW-FOCUS = 'N'
            EXIT PROGRAM.
    MOVE 'Y' TO ALLOW-FOCUS.

just in case the program got there when it shouldn't.


Then, just before a SetFocus command in field "A," the
statement:

     MOVE 'N' TO ALLOW-FOCUS.

So, then, in the error checking for field "A" we have:

     (error condition detected)
     MOVE 'N' TO ALLOW-FOCUS
     INVOKE FIELD-A 'SetFocus'

And in every other LostFocus possibility;

     IF ALLOW-FOCUS = 'N'
          EXIT PROGRAM.

I'm not looking forward to adding this (in my mind)
klutzy circumvention.
```

###### ↳ ↳ ↳ Re: Fujitsu Query

- **From:** "Michael Mattias" <michael.mattias@gte.net>
- **Date:** 1999-10-03T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<q5PJ3.2178$Iw5.61475@dfiatx1-snr1.gtei.net>`
- **References:** `<WyAJ3.2251$mN5.102464@typhoon01.swbell.net> <LdIJ3.8373$Iv5.69013@news2.mia> <QtOJ3.2694$mN5.147328@typhoon01.swbell.net>`

```
Jerry P wrote in message ...
>
>Judson McClendon <judmc123@bellsouth.net> wrote in message
…[6 more quoted lines elided]…
>packed.

So what's unreasonable? You take in 108 fields, you edit 108 fields. Seems
fair to me.

>2. The length of time the record would have to be locked while
>the user --- well, you get the idea.

No, I don't get the idea. There is no reason to lock the record while you
edit. You should not procure a lock until the data have been validated and
you are ready to rewrite.

>3. VB has a control (I'm told) called VALIDATE that gives you
>an opportunity to stay in the field.

So use Visual BASIC instead of COBOL for your dialog. Return to your COBOL
program when done. (It's a thought).

>4. One circumvention we've considered is starting each
>LostFocus event with:..klutzy..

Not needed if you follow Judson's sound advice. Besides, I find it extremely
difficult to believe that with 108 fields on a single screen, there is not
at least one 'dependent' edit; that is, the data in field '57' must be
non-blank if and only if the data in field '56' is equal to "Y" or something
like that. Full screen editing makes a lot of sense when you have dependent
edits.

Michael Mattias
Tal Systems
Racine WI USA
The views and opinions expressed herein are my own.
As I am self-employed, they also express the views of my employer.
```

###### ↳ ↳ ↳ Record Locking while doing data validation (was Fujitsu Query

_(reply depth: 4)_

- **From:** "William M. Klein" <wmklein@nospam.netcom.com>
- **Date:** 1999-10-03T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7t8h11$9pi@dfw-ixnews4.ix.netcom.com>`
- **References:** `<WyAJ3.2251$mN5.102464@typhoon01.swbell.net> <LdIJ3.8373$Iv5.69013@news2.mia> <QtOJ3.2694$mN5.147328@typhoon01.swbell.net> <q5PJ3.2178$Iw5.61475@dfiatx1-snr1.gtei.net>`

```
Michael Mattias <michael.mattias@gte.net> wrote in message
news:q5PJ3.2178$Iw5.61475@dfiatx1-snr1.gtei.net...
  <snip>
> >2. The length of time the record would have to be locked while
> >the user --- well, you get the idea.
…[4 more quoted lines elided]…
>

Well, maybe this shows my "mainframe background" - but I agree with the
concept of "locking a record" while you do the editing.  Otherwise, any edits
that you do against "existing" field data may or may not be "valid" when you
have finished your editing.

NOTE: if your application ONLY "edits" input fields - that don't depend at
all upon existing data (in the "record in storage") then this does become
irrelevant.

The alternative method (that I know of) is to "save" the record - but don't
lock it, then do your editing, then (if everything passes), RE-get the record
(this time with a LOCK), then compare the "new" record with the saved
record - and FINALLY if everything is OK (original edits and no changes to
the record), do the update.

IMHO, if you don't do one of these, then you had better do the other
(unless - of course - you are in a "single user" environment - or use some
other type of "enquing").

Maybe it is simplistic, but I guess that I would recommend the first method -
if your validation - is "relatively" quick and would recommend the second
method if your editing is slow (compared to the multi-user "demand" for
records).  (With the first method, do make certain that you "handle" the case
where the "user" walks away from a terminal for a break, lunch, overnight -
or a 2-week vacation - in the middle of doing some data entry.)

NOTE WELL:  All of the previous assumes that you have a method of doing
"individual record locking".  With some environments, you can only "lock" a
block of records - or worse a full file.  This too can "impact" your
decisions on what/how to lock.
```

###### ↳ ↳ ↳ Re: Record Locking while doing data validation (was Fujitsu Query

_(reply depth: 5)_

- **From:** "Jerry P" <bismail@bisusa.com>
- **Date:** 1999-10-03T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<6USJ3.2949$mN5.161919@typhoon01.swbell.net>`
- **References:** `<WyAJ3.2251$mN5.102464@typhoon01.swbell.net> <LdIJ3.8373$Iv5.69013@news2.mia> <QtOJ3.2694$mN5.147328@typhoon01.swbell.net> <q5PJ3.2178$Iw5.61475@dfiatx1-snr1.gtei.net> <7t8h11$9pi@dfw-ixnews4.ix.netcom.com>`

```

William M. Klein <wmklein@nospam.netcom.com> wrote in message
news:7t8h11$9pi@dfw-ixnews4.ix.netcom.com...
>
>
> The alternative method (that I know of) is to "save" the record -
but don't
> lock it, then do your editing, then (if everything passes), RE-get
the record
> (this time with a LOCK), then compare the "new" record with the
saved
> record - and FINALLY if everything is OK (original edits and no
changes to
> the record), do the update.

Our plan was:
1. Get the record and release the locks.
2. If the user changes a field, test the new value.
3. If valid, get the record with lock, replace the field, rewrite the
record.
4. If an invalid entry, issue warning, and reset the input screen
to the field being worked on.

It is, of course, this last item that's at issue because the program
does
not get control - or at least we can't find a way to get control -
until after
the field pointer has moved to the start of another field. Our pointer
reset causes an automatic loss of focus from whereever the pointer
has moved. This LostFocus event causes the program to meander
through code in a field the user may not yet have visited.

For example: Suppose Field A: "Is tornado coming (Y/N)?" and
Field B is "Type of warning:" The LostFocus event for Field B is
(after passing evaluation tests)
IF FIELD-A NOT = "N"
     IF FIELD-B = 'A' PERFORM CALL-BOSS END-IF
     IF FIELD-B = 'B' PERFORM (something else) END-IF
    PERFORM SOUND-EVACUATION-WARNING.

And the user enters a "B" in Field-A.

> Maybe it is simplistic, but I guess that I would recommend the first
method -

One disadvantage I can see in editting the whole screen occurs when
each field on the screen consumes significant resources, such as a
file lookup on a part number. Locking a record while (maybe several
hundred) file look-ups take place seems unacceptable compared to
a field-by-field edit.
```

###### ↳ ↳ ↳ Re: Record Locking while doing data validation (was Fujitsu Query

_(reply depth: 6)_

- **From:** "James J. Gavan" <jjgavan@home.com>
- **Date:** 1999-10-04T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<37F83A70.2D8239F1@home.com>`
- **References:** `<WyAJ3.2251$mN5.102464@typhoon01.swbell.net> <LdIJ3.8373$Iv5.69013@news2.mia> <QtOJ3.2694$mN5.147328@typhoon01.swbell.net> <q5PJ3.2178$Iw5.61475@dfiatx1-snr1.gtei.net> <7t8h11$9pi@dfw-ixnews4.ix.netcom.com> <6USJ3.2949$mN5.161919@typhoon01.swbell.net>`

```


Jerry P wrote:
> 
> William M. Klein <wmklein@nospam.netcom.com> wrote in message
…[47 more quoted lines elided]…
> a field-by-field edit.

Intersting topic. Strange how the 'real-world' contradicts the simple
Windows-type examples where you see an empty screen, fill the record,
validate, then file it.

Probably a play on words, but taking Jerry's example, (caveat I'm not
into multi-user record-locking, but same concepts really apply). 

Having a system which has worked in DOS for almost 20 years, my user is
not about to switch to that bloody tab-key so I'm testing if ENTER-key
is used to end-a-fieldentry or is it truly the default <OK> button. So
rather than tabs, I'm using Business-Logic to control "set-nextfocs"

Right or wrong I validate each field by returning the value from Dialog
to Business-Logic when entered, and where necessary do file/collection
'look-ups'.

- If incorrect
     error-messasge
     set CurrentObject = this-field, invoke Dialog            		
	"setfocus-CurrentObject" "clearing" or "emptying"
- if correct, increment this-field 
     set CurrentObject = this-field, invoke Dialog            		
     	"setfocus-CurrentObject"
- if correct and this-field > MaxField
     invoke Dialog "setfocus-DefaultOK"

I take Jerry's point. Read the record to get it into your program and
then unlock. You should not be concerned with the file until the user
clicks on the OK-button, then as necesary you go through your
lock/unllock to write/rewrite the record, and of course don't even
access the file if the user hasn't changed the record.

Coupled with the above I use Level 88s :-

01			pic 9.
  88 RecordFound   	value 1.
  88 RecordNotFound 	value 0.

01 			pic 9.
  88 RecordChanged	value 1.
  88 RecordNotChanged	value 0.

On the question of using tab-key - I find it extremely irritating. I
have one program, (actually it represents 80% of the activity in the
system), which is a 10 x 24 table. Assuming user is entering
'past-history' - given there are only 5 points to be inspected for 3
inspection dates gives me a 'true' data-entry table of 3 x 5  - I
disable all remaining entry-fields. But, I still have to 'guide' the
user down column 1, back up to column 2, then column 3, and at that
stage after (3, 5) has been entered, "setfocs-OKdefault" 

Changes - he randomly selects fields, follows same routine, back to
Business-Logic, which checks, and if correct "setfocus-OKdefault".

Multi-User 

What I've described so far works fine as an outline for both single and
multi-user. But take the situation where user(Bill) accesses Record 123;
while you are playing with it user(Jerry) also accesses Record 123 -
rather than tie-up the file with locks, when you press <OK> you should
do a second read of Record 123, locking the record - do a field-by-field
comparison and display back at you, if necessary, with a message saying
fields have since been changed - you are looking at latest state before
updating. (Rather than the field-by-field comparision, if records had a
time-stamp - this would give an easier approach; another possibility  -
a flag(88s) in the record - RecordBeingUsed = 1, RecordNotUsed = 0).

Two situations can occur - user(Jerry) clicks on <OK>

- if currently unlocked he updates - and if you didn't beat him to the
  punch you're going to get back that "fields-changed" message
- if he attempts to update while you have temporarily got it locked
he's   the one who will get back the "fields-changed" message when you
unlock

What we are talking about, is what in the old days we would have called
'Masterfiles' - it isn't relevant to individual transactions such as
entering invoices into an A/P system is it - or is it ?

Arguably, one could contend that the likelihood of two users changing
the same 'existing' master record are highly unlikely, and it isn't
unreasonable to have that record locked while user(Bill) is editing it.
(You've got this file in i-o mode, and those look-up files Jerry
mentioned are opened as input only with no locks required).
Unless I have a phone in each hand and make two phone calls to Amex
simultaneously, to tell them they've misspelled my last name - not much
likelihood two Amex operators are going to change my name, is there ?

Problem arises if user(Jimmy), three floors down, is entering A/P
transactions and needs to access Record 123 to confirm it exists before
the system will accept an invoice. Such a situation suggests having the
record locked/unlocked ONLY for the duration of your rewrite, triggered
by your <OK>. This situation can only occur with EXISTING records.

Sorry to plug it guys - but a COBOL site with examples of how to do
things in the 'real-world' would have helped here. We are discussing a
topic for which literally thousands of COBOLers have already found a
solution.

Jimmy, Calgary AB
```

###### ↳ ↳ ↳ Re: Record Locking while doing data validation (was Fujitsu Query

_(reply depth: 6)_

- **From:** "James J. Gavan" <jjgavan@home.com>
- **Date:** 1999-10-04T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<37F83DFF.46D1671D@home.com>`
- **References:** `<WyAJ3.2251$mN5.102464@typhoon01.swbell.net> <LdIJ3.8373$Iv5.69013@news2.mia> <QtOJ3.2694$mN5.147328@typhoon01.swbell.net> <q5PJ3.2178$Iw5.61475@dfiatx1-snr1.gtei.net> <7t8h11$9pi@dfw-ixnews4.ix.netcom.com> <6USJ3.2949$mN5.161919@typhoon01.swbell.net>`

```


Jerry P wrote:
> 
> William M. Klein <wmklein@nospam.netcom.com> wrote in message
…[47 more quoted lines elided]…
> a field-by-field edit.

Intersting topic. Strange how the 'real-world' contradicts the simple
Windows-type examples where you see an empty screen, fill the record,
validate, then file it.

Probably a play on words, but taking Jerry's example, (caveat I'm not
into multi-user record-locking, but same concepts really apply). 

Having a system which has worked in DOS for almost 20 years, my user is
not about to switch to that bloody tab-key so I'm testing if ENTER-key
is used to end-a-fieldentry or is it truly the default <OK> button. So
rather than tabs, I'm using Business-Logic to control "set-nextfocs"

Right or wrong I validate each field by returning the value from Dialog
to Business-Logic when entered, and where necessary do file/collection
'look-ups'.

- If incorrect
     error-messasge
     set CurrentObject = this-field, invoke Dialog            		
	"setfocus-CurrentObject" "clearing" or "emptying"
- if correct, increment this-field 
     set CurrentObject = this-field, invoke Dialog            		
     	"setfocus-CurrentObject"
- if correct and this-field > MaxField
     invoke Dialog "setfocus-DefaultOK"

I take Jerry's point. Read the record to get it into your program and
then unlock. You should not be concerned with the file until the user
clicks on the OK-button, then as necesary you go through your
lock/unllock to write/rewrite the record, and of course don't even
access the file if the user hasn't changed the record.

Coupled with the above I use Level 88s :-

01			pic 9.
  88 RecordFound   	value 1.
  88 RecordNotFound 	value 0.

01 			pic 9.
  88 RecordChanged	value 1.
  88 RecordNotChanged	value 0.

On the question of using tab-key - I find it extremely irritating. I
have one program, (actually it represents 80% of the activity in the
system), which is a 10 x 24 table. Assuming user is entering
'past-history' - given there are only 5 points to be inspected for 3
inspection dates gives me a 'true' data-entry table of 3 x 5  - I
disable all remaining entry-fields. But, I still have to 'guide' the
user down column 1, back up to column 2, then column 3, and at that
stage after (3, 5) has been entered, "setfocs-OKdefault" 

Changes - he randomly selects fields, follows same routine, back to
Business-Logic, which checks, and if correct "setfocus-OKdefault".

Multi-User 

What I've described so far works fine as an outline for both single and
multi-user. But take the situation where user(Bill) accesses Record 123;
while you are playing with it user(Jerry) also accesses Record 123 -
rather than tie-up the file with locks, when you press <OK> you should
do a second read of Record 123, locking the record - do a field-by-field
comparison and display back at you, if necessary, with a message saying
fields have since been changed - you are looking at latest state before
updating. (Rather than the field-by-field comparision, if records had a
time-stamp - this would give an easier approach; another possibility  -
a flag(88s) in the record - RecordBeingUsed = 1, RecordNotUsed = 0).

Two situations can occur - user(Jerry) clicks on <OK>

- if currently unlocked he updates - and if you didn't beat him to the
  punch you're going to get back that "fields-changed" message
- if he attempts to update while you have temporarily got it locked
he's   the one who will get back the "fields-changed" message when you
unlock

What we are talking about, is what in the old days we would have called
'Masterfiles' - it isn't relevant to individual transactions such as
entering invoices into an A/P system is it - or is it ?

Arguably, one could contend that the likelihood of two users changing
the same 'existing' master record are highly unlikely, and it isn't
unreasonable to have that record locked while user(Bill) is editing it.
(You've got this file in i-o mode, and those look-up files Jerry
mentioned are opened as input only with no locks required).
Unless I have a phone in each hand and make two phone calls to Amex
simultaneously, to tell them they've misspelled my last name - not much
likelihood two Amex operators are going to change my name, is there ?

Problem arises if user(Jimmy), three floors down, is entering A/P
transactions and needs to access Record 123 to confirm it exists before
the system will accept an invoice. Such a situation suggests having the
record locked/unlocked ONLY for the duration of your rewrite, triggered
by your <OK>. This situation can only occur with EXISTING records.

Sorry to plug it guys - but a COBOL site with examples of how to do
things in the 'real-world' would have helped here. We are discussing a
topic for which literally thousands of COBOLers have already found a
solution.

Jimmy, Calgary AB
```

###### ↳ ↳ ↳ Re: Record Locking while doing data validation (was Fujitsu Query

_(reply depth: 5)_

- **From:** "Judson McClendon" <judmc123@bellsouth.net>
- **Date:** 1999-10-04T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<yJ1K3.280$01.2947@news3.mia>`
- **References:** `<WyAJ3.2251$mN5.102464@typhoon01.swbell.net> <LdIJ3.8373$Iv5.69013@news2.mia> <QtOJ3.2694$mN5.147328@typhoon01.swbell.net> <q5PJ3.2178$Iw5.61475@dfiatx1-snr1.gtei.net> <7t8h11$9pi@dfw-ixnews4.ix.netcom.com>`

```
William M. Klein wrote:
>Michael Mattias wrote:
>  <snip>
…[11 more quoted lines elided]…
>have finished your editing.

This is a circular argument. :-)  If the above is true, then how are you
better by editing the fields one at a time as they are entered?  Would
you not need to keep accessing the record for each field validated? ;-)

Anyway, since you are updating an existing record, you must read it first
to display its current contents, or the user is entering the data blind.
Save off that record.  When the changes have been entered, validate them
against the saved data.  If the data is valid, then lock the record for
update.  If the data in the record has changed from the saved data, then
release the record and notify the user.

If you allow a user to modify data in a record, without locking it during
the process, you must allow for the possibility that the data has been
changed during that time.  This is irrelevant of whether the data is
validated by field or by screen.
```

###### ↳ ↳ ↳ Re: Record Locking while doing data validation (was Fujitsu Query

_(reply depth: 6)_

- **From:** "James J. Gavan" <jjgavan@home.com>
- **Date:** 1999-10-04T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<37F8CB69.D7B3E037@home.com>`
- **References:** `<WyAJ3.2251$mN5.102464@typhoon01.swbell.net> <LdIJ3.8373$Iv5.69013@news2.mia> <QtOJ3.2694$mN5.147328@typhoon01.swbell.net> <q5PJ3.2178$Iw5.61475@dfiatx1-snr1.gtei.net> <7t8h11$9pi@dfw-ixnews4.ix.netcom.com> <yJ1K3.280$01.2947@news3.mia>`

```


> William M. Klein wrote: <snip>.......

Have to go out this morning but thought I should add this as a
supplement to what I've already written. Ignore my 'business' about
RecordUse/NotUsed flag - it's a no-brainer and necessitates two
re-writes. It's just as dangerous as the following. 

Editing with Locked Record -

Betsy works for a large corporation; her main job setting-up new vendors
and changing records for same. Diligent worker - on flexi-time comes in
at 7:30 and keeps busy at her keyboard. She brings up the existing
record for Abercromby Corporation, checks her watch - it's 10 am -
coffee time. With Abercromby Corp still staring at you on the screen she
takes off for coffee. Normally she's back at her desk by 10:15 but
to-day she gets into a gab-fest with her co-workers at the coffee
counter. On the way back to her desk she bumps into the deputy
controller. "Oh Betsy come with me, there's something I'd like you to
do....". She gets back to her desk at 11:05 - then actions that
Abercromby record.

Somewhere else in the building at 10:15 somebody was trying to enter a
bunch of invoices for Abercromby.....

-never happened/wont happen - you gotta be kidding.

Record locking for duration of an edit has to be a No-No. The situation
of course, varies depending upon the application - but possibly some
time-out mechanism if somebody has a record displayed for too long.
Again, we need various examples.

Jimmy, Calgary AB
```

###### ↳ ↳ ↳ Re: Fujitsu Query

_(reply depth: 4)_

- **From:** "Jerry P" <bismail@bisusa.com>
- **Date:** 1999-10-03T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<M2TJ3.2987$mN5.162060@typhoon01.swbell.net>`
- **References:** `<WyAJ3.2251$mN5.102464@typhoon01.swbell.net> <LdIJ3.8373$Iv5.69013@news2.mia> <QtOJ3.2694$mN5.147328@typhoon01.swbell.net> <q5PJ3.2178$Iw5.61475@dfiatx1-snr1.gtei.net>`

```

Michael Mattias <michael.mattias@gte.net> wrote in message
news:q5PJ3.2178$Iw5.61475@dfiatx1-snr1.gtei.net...
>
> >3. VB has a control (I'm told) called VALIDATE that gives you
> >an opportunity to stay in the field.
>
> So use Visual BASIC instead of COBOL for your dialog. Return to your
COBOL
> program when done. (It's a thought).

It's not a thought. I mentioned it to illustrate the construct is
available in other languages, not as a thinking-out-loud list
of possibilities. VB is almost totally useless for our purposes.
>
>
> Not needed if you follow Judson's sound advice. Besides, I find it
extremely
> difficult to believe that with 108 fields on a single screen, there
is not
> at least one 'dependent' edit; that is, the data in field '57' must
be
> non-blank if and only if the data in field '56' is equal to "Y" or
something
> like that. Full screen editing makes a lot of sense when you have
dependent
> edits.

To do full screen editing, the record must be locked during the entire
editing process (exception below). It may take a user an unacceptable
amount of time (maybe several hours) to fill the screen, so locking
the record for that duration is out.

One could get a copy of the record,
wait for the user to complete the screen, then get a fresh copy of the
record with lock and compare the recently-edited data with the fresh
copy. Where differences exist, the newly-edited data could be
inserted into the record and the record rewritten.

I'd just rather do it field-by-field and am looking for an easier way
than trapping for do-not-execute-this-event code in each LostFocus
procedure.
```

###### ↳ ↳ ↳ Re: Fujitsu Query

_(reply depth: 5)_

- **From:** "James J. Gavan" <jjgavan@home.com>
- **Date:** 1999-10-04T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<37F83FC1.EA371E6@home.com>`
- **References:** `<WyAJ3.2251$mN5.102464@typhoon01.swbell.net> <LdIJ3.8373$Iv5.69013@news2.mia> <QtOJ3.2694$mN5.147328@typhoon01.swbell.net> <q5PJ3.2178$Iw5.61475@dfiatx1-snr1.gtei.net> <M2TJ3.2987$mN5.162060@typhoon01.swbell.net>`

```


Jerry P wrote:
> 
> Michael Mattias <michael.mattias@gte.net> wrote in message
> news:q5PJ3.2178$Iw5.61475@dfiatx1-snr1.gtei.net...
> > <snip>....

Jerry, Don't want to repeat it here - see if my other message to Bill
and you gives any help.

Jimmy, Calgary AB
```

##### ↳ ↳ Re: Fujitsu Query

- **From:** "Michael Mattias" <michael.mattias@gte.net>
- **Date:** 1999-10-03T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<mROJ3.1961$Iw5.60123@dfiatx1-snr1.gtei.net>`
- **References:** `<WyAJ3.2251$mN5.102464@typhoon01.swbell.net> <LdIJ3.8373$Iv5.69013@news2.mia>`

```
Judson McClendon wrote in message ...
>Yes.  Validate on a screen, not field, basis, then SetFocus to the
>first error you find.
>--


Gee, I wonder if you've done any mainframe type MCS(1) programming.....


MCM
(1) CICS, COMS, etc. message control systems (hell, you must go back at
least to GEMCOS!)
```

###### ↳ ↳ ↳ Re: Fujitsu Query

- **From:** "Judson McClendon" <judmc123@bellsouth.net>
- **Date:** 1999-10-04T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<XS1K3.297$01.3197@news3.mia>`
- **References:** `<WyAJ3.2251$mN5.102464@typhoon01.swbell.net> <LdIJ3.8373$Iv5.69013@news2.mia> <mROJ3.1961$Iw5.60123@dfiatx1-snr1.gtei.net>`

```
Michael Mattias wrote in message ...
>Judson McClendon wrote in message ...
>>Yes.  Validate on a screen, not field, basis, then SetFocus to the
>>first error you find.
>
>Gee, I wonder if you've done any mainframe type MCS(1) programming.....

Almost 30 years, and multi-user systems on PC's almost 20 years. ;-)
```

#### ↳ Re: Fujitsu Query

- **From:** redsky@ibm.net (Thane Hubbell)
- **Date:** 1999-10-04T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<37f80058.266679877@news1.attglobal.net>`
- **References:** `<WyAJ3.2251$mN5.102464@typhoon01.swbell.net>`

```
On Sat, 2 Oct 1999 22:58:57 -0500, "Jerry P" <bismail@bisusa.com>
wrote:

>Suppose:
>1. User enters data in field "A" and attempts to exit via
…[15 more quoted lines elided]…
>Any suggestions?

The same issue exists with Dialog System form MicroFocus or in direct
API event driven programming.  When I was programming with DS I
avoided "lost focus"events, but when they were necessary I had save
fields that I compared the field contents with to see  if there was a
change.  I am not conversant in PowerCOBOL so I can't help with the
coding, but could something similar work?
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
