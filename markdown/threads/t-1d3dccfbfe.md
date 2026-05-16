[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Sequential File Update w/ Multiple Input Records

_5 messages · 5 participants · 1999-03_

**Topics:** [`VSAM, files, sorting`](../topics.md#files)

---

### Sequential File Update w/ Multiple Input Records

- **From:** y2kbyten@aol.com (Y2KByten)
- **Date:** 1999-03-28T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<19990328122544.02899.00000566@ng-fc1.aol.com>`

```
Hi,

In class we are updating a sequential file (fields were previously error
checked).
It appears the input (transaction) record(s) consist of 2 - 80 char recs.  The
common fields are type, and employee number.  My main question for the
experienced is when I load the files for compairison, do I load tran-rec-1 AND
trans-rec-2 into WS (ws-trans-1, ws-trans-2) then compare when loading
old-master-1, and old-master-2 into WS ?  Or is this done trans-rec-1 first,
with
old-master-1 following.  I also  believe my key-choice  here would be the
employee number. Type would determine where to load it into WS.  ?????  We were
told
each employee that has a transaction will have the two recs. (no suprises, so
they tell me)

Thanks for any advice in advance.
Jake
```

#### ↳ Re: Sequential File Update w/ Multiple Input Records

- **From:** twymer@aol.com (Twymer)
- **Date:** 1999-03-29T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<19990329081812.24505.00002430@ng-cg1.aol.com>`
- **References:** `<19990328122544.02899.00000566@ng-fc1.aol.com>`

```
Personally I would create two separate processes...merge the two trans files
into one and then compare the merged trans file against the masters one at a
time.  In CPU time this may not be the most efficient solution but maintenance
wise this would make things a whole lot easier...plus you can always mirro the
merged trans file and run the two processes concurrently
```

##### ↳ ↳ Re: Sequential File Update w/ Multiple Input Records

- **From:** postingid@dissensoftware.com (Binyamin Dissen)
- **Date:** 1999-03-29T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3707b190.39850794@news.netvision.net.il>`
- **References:** `<19990328122544.02899.00000566@ng-fc1.aol.com> <19990329081812.24505.00002430@ng-cg1.aol.com>`

```
On 29 Mar 1999 13:18:12 GMT twymer@aol.com (Twymer) wrote:

:>Personally I would create two separate processes...merge the two trans files
:>into one and then compare the merged trans file against the masters one at a
:>time.  In CPU time this may not be the most efficient solution but maintenance
:>wise this would make things a whole lot easier...plus you can always mirro the
:>merged trans file and run the two processes concurrently

Not speaking about the validity of the solution, but I would expect that
Y2KByten's instructor would not prefer that solution.
```

#### ↳ Re: Sequential File Update w/ Multiple Input Records

- **From:** "gee" <grant_englebrecht@nospam.compuware.com>
- **Date:** 1999-03-30T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<37002dbe@199.186.16.51>`
- **References:** `<19990328122544.02899.00000566@ng-fc1.aol.com>`

```
what it sounds like IMO is a sequential file update process using the
'balance line algorithm'.
with this it assumes that the input transaction file and the master file are
in ordered sequence.
the algorithm goes like this (from memory so be wary, tho this is covered in
text books)

read master at end move high values to master.key
read transaction at end move high values to transaction.key

perform until master.key = high values AND transaction.key = high values
    if master.key  < transaction.key
        key = master.key
        write output from master record
        read master at end move high values to master.key
    else if  master.key  > transaction.key
               key = transaction.key
               write output from transaction record
               read transaction at end move high values to transaction.key
           else if  master.key = transaction.key
               apply transaction to master file  NB this is either an
add/change/delete...
           endif
     endif
end-perform


Y2KByten wrote in message <19990328122544.02899.00000566@ng-fc1.aol.com>...
>Hi,
>
>In class we are updating a sequential file (fields were previously error
>checked).
>It appears the input (transaction) record(s) consist of 2 - 80 char recs.
The
>common fields are type, and employee number.  My main question for the
>experienced is when I load the files for compairison, do I load tran-rec-1
AND
>trans-rec-2 into WS (ws-trans-1, ws-trans-2) then compare when loading
>old-master-1, and old-master-2 into WS ?  Or is this done trans-rec-1
first,
>with
>old-master-1 following.  I also  believe my key-choice  here would be the
>employee number. Type would determine where to load it into WS.  ?????  We
were
>told
>each employee that has a transaction will have the two recs. (no suprises,
so
>they tell me)
>
>Thanks for any advice in advance.
>Jake
>
```

##### ↳ ↳ Re: Sequential File Update w/ Multiple Input Records

- **From:** "Alan Russell" <RUSSELAH@apci.com>
- **Date:** 1999-03-30T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7dqjme$9qj@netnews1.apci.com>`
- **References:** `<19990328122544.02899.00000566@ng-fc1.aol.com> <37002dbe@199.186.16.51>`

```
What was listed below was NOT the balanced line algorithm.  Here is my
skeltal solution.  See my doctoral dissertation which covered this topic
(among others) at http://members.aol.com/ahrussell

 (let's assume that trans-file-1 contains add/change/delete transactions and
trans-file-2 contains update transaction.  all 3 files are in order by the
same key.  I'm ignoring such details as open/close and error reports, etc.
Note that the ONLY comparison between keys is in the routine
choose-next-key.  This can obviously be extended for multiple files in this
key sequence.  I have personally coded a 7-file match program which ran
correctly the first time.)

mainline.
    perform read-master.
    perform read-trans-1.
    perform read-trans-2.
    perform choose-next-key.
    perform process-one-key until next-key = high-values.
    stop run.

read-master.
    read master-file into master-rec
        at end move high-values to master-rec.
read-trans-1.
    read trans-file-1 into trans-rec-1
        at end move high-values to trans-rec-1.
read-trans-2.
    read trans-file-2 into trans-rec-2
        at end move high-values to trans-rec-2.

choose-next-key.
    move master-key to next-key.
    if trans-key-1 < next-key move trans-key-1 to next-key.
    if trans-key-2 < next-key move trans-key-2 to next-key.

process-one-key.
    move 'N' to master-is-valid.
    perform process-master until master-key not = next-key.
    perform process-trans-1 until trans-key-1 not = next-key.
    perform process-trans-2 until trans-key-2 not = next-key.
    if master-is-valid = 'Y'
        perform write-new-master
    end-if.
    perform choose-next-key.

process-master.
    move master-rec to new-master-rec.
    move 'Y' to master-is-valid.
    perform read-master.

process-trans-1.
    if trans-1-type = 'A'
        if master-is-valid = 'Y'
            perform error-duplicate-add
        else
            perform good-add-routine
            move 'Y' to master-is-valid
        end-if
    else if trans-1-type = 'C'
        if master-is-valid = 'Y'
            perform good-change-routine
        else
            perform error-no-master-for-change
        end-if
    else if trans-1-type = 'D'
        if master-is-valid = 'Y'
            move 'N' to master-is-valid
        else
            perform error-no-master-for-change
        end-if
    else
        perform bad-trans-1
    end-if.
    perform read-trans-1.

process-trans-2.
    if  master-is-valid = 'Y'
        perform good-trans-2
    else
        perform error-no-master-for-trans-2
    end-if.
    perform read-trans-2.

Alan Russell, PhD, CCP
Work - Russelah@apci.com
Home - AHRussell@computer.org
Home page - http://members.aol.com/ahrussell
-------------------------------------------------------
The views expressed are mine alone and do not necessarily reflect those of
my employer


gee wrote in message <37002dbe@199.186.16.51>...
>what it sounds like IMO is a sequential file update process using the
>'balance line algorithm'.
>with this it assumes that the input transaction file and the master file
are
>in ordered sequence.
>the algorithm goes like this (from memory so be wary, tho this is covered
in
>text books)
>
…[46 more quoted lines elided]…
>
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
