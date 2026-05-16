[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# On Size Error

_4 messages · 3 participants · 1999-08_

---

### Re: On Size Error

- **From:** "James J. Gavan" <jjgavan@home.com>
- **Date:** 1999-08-14T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<37B4F84E.BDF76E6A@home.com>`
- **References:** `<7ouvo8$p41$1@mail.dstsystems.com> <37b5aee8.540433@news.indigo.ie>`

```
> On Thu, 12 Aug 1999 12:13:53 -0500, "Charles Dusheke"
> <cwdusheke@dstsystems.com> wrote:
…[16 more quoted lines elided]…
> >

Dare I say it ? (Yes) - the above is HORRIBLE code. Why confuse the
file reading technique with a compute, wrapping READ and END-READ around
the COMPUTE - they are separate actions and the COMPUTE only comes into
play if you have a record that satisfies your processing conditions.
From your example 'read file1' you don't quote a key, so I assume you
are reading sequentially :-

	set FileNotFinished to true
	read infile next record at end set FileFinished to true
	End-read 				*> if you want 

	perform until FileFinished

	  If RecordKey = MyCondition		*> optiional
	     compute x = a + b
       	        on size error
	        set FileFinished to true
                perform error-routine
	      end-compute
	   End-if				*> optional

	   if FileNotFinished
	      read infile next record at end set FileFinished to true
	      End-read  			*> if you want
           end-if
	End-perform

Sure you can intermingle stuff - but KISS.

Jimmy, Calgary AB
```

#### ↳ Re: On Size Error

- **From:** "Rick Smith" <ricksmith@aiservices.com>
- **Date:** 1999-08-14T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7p3b19$dtl$1@news.hitter.net>`
- **References:** `<7ouvo8$p41$1@mail.dstsystems.com> <37b5aee8.540433@news.indigo.ie> <37B4F84E.BDF76E6A@home.com>`

```

James J. Gavan wrote in message <37B4F84E.BDF76E6A@home.com>...
[...]
> set FileNotFinished to true
> read infile next record at end set FileFinished to true
> End-read *> if you want

Probably just a "thinko" but  the 'End-read' is not *really*
optional. The choice is either 'End-read' or a period. Failure
to have one of these will cause the following perform to be
executed only "at end".

> perform until FileFinished
[...]
> End-perform

And yes, I, too, have posted such "thinkos" ;-)
------------------
Rick Smith
```

##### ↳ ↳ Re: On Size Error

- **From:** "James J. Gavan" <jjgavan@home.com>
- **Date:** 1999-08-14T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<37B5CF76.99CE0423@home.com>`
- **References:** `<7ouvo8$p41$1@mail.dstsystems.com> <37b5aee8.540433@news.indigo.ie> <37B4F84E.BDF76E6A@home.com> <7p3b19$dtl$1@news.hitter.net>`

```
Rick Smith wrote:
> 
> James J. Gavan wrote in message <37B4F84E.BDF76E6A@home.com>...
…[16 more quoted lines elided]…
> Rick Smith

You're right - I did a test after your comment and on first read - Boom
! - went straight to STOP RUN. Tricky, tricky this END and PERIOD thing.
This is where we need a on-line library of examples to overcome this
type of goof.

I don't program in this style, using OO to keep my file-handling as
separate classes, but if I'd checked my own STANDARD code first.......

          Evaluate TRUE

            When read-PrimeKey

             move lnk-PrimeKey to Data-PrimeKey
             Read Data-File
               Invalid key
                 Set record-not-found to True
               Not invalid key
                 Move Data-record to os-record
             End-Read

            When read-next

             Read Data-File next record
               At End
                 Set file-finis to True
               Not at End
                 Move Data-record to os-record
             End-Read

            When start-PrimeKey
		....................
	End-evaluate

Jimmy, Calgary AB
```

#### ↳ Re: On Size Error

- **From:** "Jim" <jpprice@surfsouth.com>
- **Date:** 1999-08-20T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<OQjv3.15759$gO1.527974@news2.giganews.com>`
- **References:** `<7ouvo8$p41$1@mail.dstsystems.com> <37b5aee8.540433@news.indigo.ie> <37B4F84E.BDF76E6A@home.com>`

```
> Dare I say it ? (Yes) - the above is HORRIBLE code.

COMPUTE X = A * B
            ON SIZE ERROR
                     MOVE ZERO TO X
END-COMPUTE

By the way, the code after >perform abend-routine<, if a true abend routine,
would never be executed, why not just go to abend-routine.
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
