[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Table Quicksort (Was: COBOL SORT within an online program)

_7 messages · 5 participants · 2003-02_

**Topics:** [`VSAM, files, sorting`](../topics.md#files)

---

### Table Quicksort (Was: COBOL SORT within an online program)

- **From:** psychedelic-harry@mindless.com (Joe Zitzelberger)
- **Date:** 2003-02-27T16:14:34-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<16e2f010.0302271614.1d8f6078@posting.google.com>`

```
All this talk of sorting tables made me just want to write some code. 
Here is quicksort, alter and used freely at your own risk...


       Identification Division.
       Program-ID. JAZQSORT is recursive.
      *---------------------------------------------------------------*
      *
      * Qsort
      *   if size(a) equals 1, then return
      *   select pivot record at a[random]
      *   make array a1 with elements less than pivot
      *   make array a2 with elements greater than pivot
      *   QSort a1
      *   QSort a2
      *
      * This is a Cobol implementation of C.A.R Hoare's quicksort.
      *
      * Please note that I have just banged this out -- it has been
      * desk-checked, that is all.  If I get any comments about
      * silly syntax errors I'll killfile the sender.
      *
      * If, OTOH, someone has a modern Cobol compiler running under
      * Hercules I'd love some information on it.
      *
      * It is written with the IBM mainframe in mind (since that is
      * what started the thread) and I've used a few extensions.
      *
      * This is also  just an example implementation, so I did the
      * lazy thing and used an actual table for the table instead
      * of computing the offsets in a buffer.  But that also
      * is left as an exercise for the interested reader.
      *
      * Happy sorting! Use at your own risk.
      *---------------------------------------------------------------*
       Environment Division.
       Data Division.
       Working-Storage Section.
       01 JAZQSORT-Working-Storage.
         05 Swap-Space           Pic X(80) Value spaces.

       Local-Storage Section.
       01 JAZQSORT-Local-Storage.
         05 Lo            Binary Pic S9(8) Value 0.
         05 Hi            Binary Pic S9(8) Value 0.
         05 Pivot                 Pic 9(08) Value 0.

       Linkage Section.

       01 The-Table-Area.
         05 The-Table     occurs 0 to 32767 depending on High-Element.
           10 The-Key            Pic 9(08).
           10 The-Data           Pic X(72).

       01 Low-Element     Binary Pic S9(8).
       01 High-Element    Binary Pic S9(8).

       Procedure Division using The-Table-Area
                                Low-Element
                                High-Element.

           Compute Lo  = Low-Element
           Compute Hi  = High-Element

           If ( High-Element > Low-Element )

              Perform Select-Pivot


      * ----- Loop through table until indices cross
              Perform until Hi < Lo


      * -------- Locate an item that should not be in less partition
                 Perform varying Lo from Lo by 1
                   until (( Lo >= High-Element )
                      or  ( The-Key of The-Table ( Lo ) >= Pivot ))
                    Continue
                 End-Perform


      * -------- Locate an item that should not be in greater
partition
                 Perform varying Hi from Hi by -1
                   until (( Hi <= Low-Element )
                      or  ( The-Key of The-Table ( Hi ) <= Pivot ))
                 End-Perform


      * -------- Exchange the two and keep looking
                 If ( Lo <= Hi )
                    Perform Swap-Elements
                    Compute Lo = Lo + 1
                    Compute Hi = Hi - 1
                 End-If


              End-Perform

              Perform Qsort-Less-Partition

              Perform Qsort-Greater-Partition

           End-If


      *--------------------------------------------------------------*
      * Return in a manner that does not wreck our environment
      *--------------------------------------------------------------*
           Goback.

      *--------------------------------------------------------------*
      * Select the pivot using median of three rule.
      *--------------------------------------------------------------*
       Select-Pivot.
           Compute Pivot = Lo + Hi / 2
           Compute Pivot = Function Median (
              The-Key of The-Table ( Lo )
              The-Key of The-Table ( Pivot )
              The-Key of The-Table ( Hi ) )
           End-Compute
           Exit.


      *--------------------------------------------------------------*
      * Exchange elements in the wrong partition
      *--------------------------------------------------------------*
       Swap-Elements.
           Move The-Table ( Lo ) to Swap-Space
           Move The-Table ( Hi ) to The-Table ( Lo )
           Move Swap-Space       to The-Table ( Hi )
           Exit.


      *--------------------------------------------------------------*
      * Sort the less sub-partition
      *  -- Optimization opportunity for the user: if the partition
      *    size is sufficiently small you might want to apply a simple
      *    sort like insertion or bubble, or perhaps a bose-nelson
      *    network to order the last few and save the overhead of
      *    another recursive call.
      *--------------------------------------------------------------*
       Qsort-Less-Partition.
           If ( Low-Element < Hi )
              Call 'JAZQSORT' Using
                 The-Table-Area
                 Low-Element
                 Hi
              End-Call
           End-If
           Exit.


      *--------------------------------------------------------------*
      * Sort the greater sub-partition
      *  -- Optimization opportunity for the user: same as left part.
      *--------------------------------------------------------------*
       Qsort-Greater-Partition.
           If ( Lo < High-Element )
              Call 'JAZQSORT' Using
                 The-Table-Area
                 Lo
                 High-Element
              End-Call
           End-If
           Exit.


       End Program JAZQSORT.





psychedelic-harry@mindless.com

Old programmers never die, they just terminate and stay resident.
```

#### ↳ Re: Table Quicksort (Was: COBOL SORT within an online program)

- **From:** "James J. Gavan" <jjgavan@shaw.ca>
- **Date:** 2003-02-28T03:04:11+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3E5ED0E8.E6116324@shaw.ca>`
- **References:** `<16e2f010.0302271614.1d8f6078@posting.google.com>`

```


Joe Zitzelberger wrote:

> All this talk of sorting tables made me just want to write some code.
> Here is quicksort, alter and used freely at your own risk...
>

Joe,

Rather than blather on about what can and can't happen - I really wish more
people  would be courageous enough to post source. The downside is, that
rather than look at what is being offered and in a positive sense, offer
constructive suggestions for enhancements - the bloody nit pickers get
involved !

Jimmy, Calgary AB
```

##### ↳ ↳ Re: Table Quicksort (Was: COBOL SORT within an online program)

- **From:** psychedelic-harry@mindless.com (Joe Zitzelberger)
- **Date:** 2003-02-28T05:26:29-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<16e2f010.0302280526.1adf0b6e@posting.google.com>`
- **References:** `<16e2f010.0302271614.1d8f6078@posting.google.com> <3E5ED0E8.E6116324@shaw.ca>`

```
"James J. Gavan" <jjgavan@shaw.ca> wrote in message news:<3E5ED0E8.E6116324@shaw.ca>...
> Joe Zitzelberger wrote:
> 
…[12 more quoted lines elided]…
> Jimmy, Calgary AB

Let 'em pick!  What complaints could they have, that I didn't use
enough periods?

It is fast and functional, and if I find myself with another hour I'll
get rid of the fixed table size and key size/offset and make it a
useful utility.
```

###### ↳ ↳ ↳ Re: Table Quicksort (Was: COBOL SORT within an online program)

- **From:** "Charles Hottel" <chottel@cpcug.org>
- **Date:** 2003-02-28T21:25:06+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<01c2df6f$ca3db200$328bf243@chottel>`
- **References:** `<16e2f010.0302271614.1d8f6078@posting.google.com> <3E5ED0E8.E6116324@shaw.ca> <16e2f010.0302280526.1adf0b6e@posting.google.com>`

```
More power to you! Code on goodfellow!

Joe Zitzelberger <psychedelic-harry@mindless.com> wrote in article
<16e2f010.0302280526.1adf0b6e@posting.google.com>...
> "James J. Gavan" <jjgavan@shaw.ca> wrote in message
news:<3E5ED0E8.E6116324@shaw.ca>...
> > Joe Zitzelberger wrote:
> > 
…[6 more quoted lines elided]…
> > Rather than blather on about what can and can't happen - I really wish
more
> > people  would be courageous enough to post source. The downside is,
that
> > rather than look at what is being offered and in a positive sense,
offer
> > constructive suggestions for enhancements - the bloody nit pickers get
> > involved !
…[9 more quoted lines elided]…
>
```

#### ↳ Re: Table Quicksort (Was: COBOL SORT within an online program)

- **From:** robert@wagner.net (Robert Wagner)
- **Date:** 2003-02-28T12:20:31+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3e5f5228.139263430@news.optonline.net>`
- **References:** `<16e2f010.0302271614.1d8f6078@posting.google.com>`

```
psychedelic-harry@mindless.com (Joe Zitzelberger) wrote:

>All this talk of sorting tables made me just want to write some code. 
>Here is quicksort, alter and used freely at your own risk...

Mainframe COBOL does not allow recursion. At least it didn't in the Good Old
Days. The reason is, it stores the return address and parameters in
working-storage-like memory rather than on a stack. 

You can get around this by using PERFORM rather than CALL, maintaining your own
parameter stack containing Hi and Lo in an array.

Robert
```

##### ↳ ↳ Re: Table Quicksort (Was: COBOL SORT within an online program)

- **From:** jzitzelb@tsys.com (Joe Zitzelberger)
- **Date:** 2003-02-28T11:04:59-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<dcedb8d0.0302281104.2eba9b05@posting.google.com>`
- **References:** `<16e2f010.0302271614.1d8f6078@posting.google.com> <3e5f5228.139263430@news.optonline.net>`

```
robert@wagner.net (Robert Wagner) wrote in message news:<3e5f5228.139263430@news.optonline.net>...
> psychedelic-harry@mindless.com (Joe Zitzelberger) wrote:
> 
…[10 more quoted lines elided]…
> Robert

IBM unscrewed that oversight sometime in the mid-90's.  I'm not sure
exactly when, but I think it was when they started the Compiler of the
Week subscription club.
```

##### ↳ ↳ Re: Table Quicksort (Was: COBOL SORT within an online program)

- **From:** "Charles Hottel" <chottel@cpcug.org>
- **Date:** 2003-02-28T21:23:22+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<01c2df6f$8b741640$328bf243@chottel>`
- **References:** `<16e2f010.0302271614.1d8f6078@posting.google.com> <3e5f5228.139263430@news.optonline.net>`

```
It does allow it now and IBM OO programs must be RECURSIVE.

Robert Wagner <robert@wagner.net> wrote in article
<3e5f5228.139263430@news.optonline.net>...
> psychedelic-harry@mindless.com (Joe Zitzelberger) wrote:
> 
…[3 more quoted lines elided]…
> Mainframe COBOL does not allow recursion. At least it didn't in the Good
Old
> Days. The reason is, it stores the return address and parameters in
> working-storage-like memory rather than on a stack. 
> 
> You can get around this by using PERFORM rather than CALL, maintaining
your own
> parameter stack containing Hi and Lo in an array.
> 
…[3 more quoted lines elided]…
>
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
