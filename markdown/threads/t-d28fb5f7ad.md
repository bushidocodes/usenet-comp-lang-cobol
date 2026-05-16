[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# compile with Kobol was not error free

_7 messages · 4 participants · 2002-12 → 2003-01_

---

### compile with Kobol was not error free

- **From:** ronglaz6@aol.comnojunk (Ron Glazier)
- **Date:** 2002-12-29T01:26:33+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<20021228202633.01967.00000038@mb-df.aol.com>`

```
       identification division.
       program-id.     table1.
       author.         Ron Glazier.
       installation.   Los Angeles.
       date-written.   December 15, 2002.
       date-compiled.
       security.       non-classified.
      * remarks        p370.
      *********************************************************
      *
      * counting number of records in a file.
      *
      *
      *********************************************************

       environment division.
       input-output section.
       file-control.
           select catalog-file assign to "c:\catalog.dat"
           organization is line sequential.

           select out-file assign to "c:\out.dat"
           organization is line sequential.

       fd  catalog-file
           label records are standard.
       01  catalog-record.
               05 master-catalog-number            pic x(5).
               05 rest-of-record                   pic x(5).

       fd out-file
          label records are standard.
       01 out-record.
               05 catalog-num                      pic x(5).
               05 rest-of-rec                      pic x(5).


       working-storage section.
       01 more-data-remains-flag  pic x(3) value "yes".
           88 no-more-data-remains         value "no ".
           88 more-data-remains            value "yes".

       01 counter1             pic 9(6)    value zeroes.
       01 counter2             pic 9(6)    value zeroes.




       procedure division.
       a000-main.
           display " start of program table1.cbl ".
           open input catalog-file.
           open output out-file.
           move zero to counter1.
           move zero to counter2.

           read catalog-file
                   at end move "no " to more-data-remains-flag.

           move master-catalog-number to catalog-num.
           move rest-of-record to rest-of-rec.
           write out-record.

           add 1 to counter1.
           display " counter1 = " counter1.

           perform b000-process-record
               until no-more-data-remains.


           close catalog-file.
           close out-file.
           display " end of program table1 ".
           stop run.


       b000-process-record.
           read catalog-file
               at end move "no " to more-data-remains-flag.


           move master-catalog-number to catalog-num.
           move rest-of-record to rest-of-rec.
           write out-record.
           add 1 to counter1.


           if more-data-remains
               display " counter1 = " counter1.

/////////////////////////////////////
 could not get this one to compile with no errors.
 Ron
```

#### ↳ Re: compile with Kobol was not error free

- **From:** Binyamin Dissen <postingid@dissensoftware.com>
- **Date:** 2002-12-29T11:17:16+02:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<oaft0v8ssqbj58egp046bi24ekenpsepmd@4ax.com>`
- **References:** `<20021228202633.01967.00000038@mb-df.aol.com>`

```
On 29 Dec 2002 01:26:33 GMT ronglaz6@aol.comnojunk (Ron Glazier) wrote:

   [ program snipped ]

:> could not get this one to compile with no errors.

I guess I could load this into a compiler and see what happens, but why go
thru that effort?

People would more easily help if you included the compiler errors.
```

#### ↳ Re: compile with Kobol was not error free

- **From:** "Alister Munro" <alister@specsoft.freeserve.co.uk>
- **Date:** 2002-12-29T10:31:12
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<aumitg$qie$1@news5.svr.pol.co.uk>`
- **References:** `<20021228202633.01967.00000038@mb-df.aol.com>`

```
Maybe because you mist out :

    DATA DIVISION.

        FILE SECTION.

Insert these two lines just before the

            FD  catalog-file LABEL RECORDS ARE STANDARD.

"Ron Glazier" <ronglaz6@aol.comnojunk> wrote in message
news:20021228202633.01967.00000038@mb-df.aol.com...
>        identification division.
>        program-id.     table1.
…[91 more quoted lines elided]…
>
```

##### ↳ ↳ Re: compile with Kobol was not error free

- **From:** ronglaz6@aol.comnojunk (Ron Glazier)
- **Date:** 2002-12-31T04:46:47+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<20021230234647.06965.00000430@mb-cj.aol.com>`
- **References:** `<aumitg$qie$1@news5.svr.pol.co.uk>`

```
error message was
   unknown option '3'
 when using Kobol.
    RonGlaz@juno.com
```

###### ↳ ↳ ↳ Re: compile with Kobol was not error free

- **From:** ronglaz6@aol.comnojunk (Ron Glazier)
- **Date:** 2002-12-31T05:02:29+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<20021231000229.06965.00000432@mb-cj.aol.com>`
- **References:** `<20021230234647.06965.00000430@mb-cj.aol.com>`

```
it compiles ok with micro focus
```

###### ↳ ↳ ↳ Re: compile with Kobol was not error free

- **From:** riplin@Azonic.co.nz (Richard)
- **Date:** 2002-12-31T12:34:13-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<217e491a.0212311234.64dafa86@posting.google.com>`
- **References:** `<aumitg$qie$1@news5.svr.pol.co.uk> <20021230234647.06965.00000430@mb-cj.aol.com>`

```
ronglaz6@aol.comnojunk (Ron Glazier) wrote

> error message was
>    unknown option '3'
>  when using Kobol.

At last some useful indication of what the problem is.

The problem has nothing at all to do with your Cobol code. This is a
problem with Kobol where the IDE invokes the cob2c 'compiler' with an
option '-3' and the cob2c program doesn't know what this is.

There should be a version that does recognise the -3 option in the
~/kobol/bin directory:

> [riplin@Redhat bin]$ cob2c_mpe
>
…[19 more quoted lines elided]…
>   -W     (give all warnings)

The cob2c demo version has same date and time and is only a few bytes
different in size and doesn't display the -3 option in the help - it
also fails when it is passed the -3 option as you have found.

Rename the cob2c_mpe to cob2c (after removing original cob2c) and it
should work.

Somebody needs to tell TheKompany.
```

###### ↳ ↳ ↳ Re: compile with Kobol was not error free

_(reply depth: 4)_

- **From:** ronglaz6@aol.comnojunk (Ron Glazier)
- **Date:** 2003-01-03T04:26:19+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<20030102232619.22997.00000413@mb-mf.aol.com>`
- **References:** `<217e491a.0212311234.64dafa86@posting.google.com>`

```
I did e mail the Kompany about it and they will probably reply soon
          Ron
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
