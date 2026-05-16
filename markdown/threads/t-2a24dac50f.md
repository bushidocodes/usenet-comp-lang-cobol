[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# HELP - Preventing access to input files for two concurrent jobs.

_6 messages · 5 participants · 2005-11_

**Topics:** [`Jobs, careers, recruiting, salary`](../topics.md#jobs) · [`Help requests and how-to`](../topics.md#help)

---

### HELP - Preventing access to input files for two concurrent jobs.

- **From:** "Catch_22" <catch_20_2@yahoo.co.uk>
- **Date:** 2005-11-22T20:22:30-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1132719750.184297.129550@f14g2000cwb.googlegroups.com>`

```
Hi,

I have an issue I'm hoping to find a solution to. I work in a mainframe
environment using z/OS.

I have a program that reads in three files, it will use records from
these files and output any records that wasn't used, to three
corresponding output files. The input and output files are stored as
GDGs.

The issue I wish to safe guard against is an operator invoking the
program in two different jobs at the same time. It is important that
the input files only be used by one program at a time and that data
used by the program is unique.

I'm of the understanding that if a second job is started while the
first is still running that the second job will wait to use the file
being used in the first job - thus it will use data that may have
already been used by the first job.

Does anyone have any ideas on how it might be possible to prevent the
second job from using the old GDG ..... or possibly using the next
generation created by the first job when it has completed ?

I know it's possible to prevent this happening for scheduled jobs via
Zeke though we also have many manually executed jobs as well.

Any help that people could provide would be greatly appreciated.

Regards,
Ian.
```

#### ↳ Re: HELP - Preventing access to input files for two concurrent jobs.

- **From:** "William M. Klein" <wmklein@nospam.netcom.com>
- **Date:** 2005-11-23T07:34:37+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<hYUgf.62161$aM1.40706@fe01.news.easynews.com>`
- **References:** `<1132719750.184297.129550@f14g2000cwb.googlegroups.com>`

```
Check out the
   DISP=OLD
JCL parameter.
"Catch_22" <catch_20_2@yahoo.co.uk> wrote in message 
news:1132719750.184297.129550@f14g2000cwb.googlegroups.com...
> Hi,
>
…[29 more quoted lines elided]…
>
```

#### ↳ Re: HELP - Preventing access to input files for two concurrent jobs.

- **From:** "Alistair" <alistair@ld50macca.demon.co.uk>
- **Date:** 2005-11-23T06:09:17-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1132754957.120249.37350@z14g2000cwz.googlegroups.com>`
- **In-Reply-To:** `<1132719750.184297.129550@f14g2000cwb.googlegroups.com>`
- **References:** `<1132719750.184297.129550@f14g2000cwb.googlegroups.com>`

```
Love it! Someone else who knows ZEKE (and ZEBB).

1. Use Zeke as you thought to prevent the scheduling error.

2. Whack an indicator file in to the JCL. Check to see if it exists at
start of run and if it does then either cancel or reschedule the job
(your sysprogs should be able to provide a utility which will prompt
the ops to re-queue the job). If it does not pre-exist then create it
and run-on.

Probably of little or no interest: I had a user whose system did not
reset the 'S' for submit from the online screen after submitting the
non-rerunnable job. Unfortunately, the dumb terminal had
keyboard/screen buffering enabled and the user was able to submit the
same job several times. So it can happen (I didn't design the system
but I would have happily shot the designer and coder responsible).
```

#### ↳ Re: HELP - Preventing access to input files for two concurrent jobs.

- **From:** "Michael Mattias" <michael.mattias@gte.net>
- **Date:** 2005-11-23T14:50:00+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<sk%gf.2197$rq3.1214@newssvr19.news.prodigy.com>`
- **References:** `<1132719750.184297.129550@f14g2000cwb.googlegroups.com>`

```
"Catch_22" <catch_20_2@yahoo.co.uk> wrote in message
news:1132719750.184297.129550@f14g2000cwb.googlegroups.com...
> Hi,
>
> I have an issue I'm hoping to find a solution to. I work in a mainframe
> environment using z/OS.
...
>
> Does anyone have any ideas on how it might be possible to prevent the
…[4 more quoted lines elided]…
> Zeke though we also have many manually executed jobs as well.

Isn't this 'normally' (whatever that means) handled by using queues?

MCM
```

##### ↳ ↳ Re: HELP - Preventing access to input files for two concurrent jobs.

- **From:** "Catch_22" <catch_20_2@yahoo.co.uk>
- **Date:** 2005-11-23T12:56:56-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1132779416.541047.216550@z14g2000cwz.googlegroups.com>`
- **References:** `<1132719750.184297.129550@f14g2000cwb.googlegroups.com> <sk%gf.2197$rq3.1214@newssvr19.news.prodigy.com>`

```
Hi Again,

Thanks for all your advice ...... our sys admin says that once the
first job starts running :

It will read in the latest GDG for each of the three files, as an
example this will be GDG(0) and it will output the unused records to
GDG(+1).

If the second job is started before the first has finished it will try
to use GDG(0) and will wait till it's free.

Once the first job has completed the second will start using GDG(0) not
the latest GDG (GDG(+1)) which has been created by the first job.

When the second job is complete it will create GDG(+2).

What I believe will happen with two concurrent jobs :
GDG(0)   - Input file into Job #1 & Job #2
GDG(+1) - Output from Job #1
GDG(+2) - Output from Job #2

What I would like to have happen with two concurrent jobs :
GDG(0)   - Input file into Job #1
GDG(+1) - Output from Job #1 & Input into Job #2
GDG(+2) - Output from Job #2

While Zeke can be used to reserve a resourse unfortunately we also have
quite a few "on request" manually submitted jobs. It is these ones we
fear will cause the most trouble as the operators will not know another
job is already using these files.

Regards,
Ian.
```

###### ↳ ↳ ↳ Re: HELP - Preventing access to input files for two concurrent jobs.

- **From:** Binyamin Dissen <postingid@dissensoftware.com>
- **Date:** 2005-11-23T16:22:58-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3dn9o1pc7v2qhn77pgh5flppetn7ciqa15@4ax.com>`
- **References:** `<1132719750.184297.129550@f14g2000cwb.googlegroups.com> <sk%gf.2197$rq3.1214@newssvr19.news.prodigy.com> <1132779416.541047.216550@z14g2000cwz.googlegroups.com>`

```
On 23 Nov 2005 12:56:56 -0800 "Catch_22" <catch_20_2@yahoo.co.uk> wrote:

:>Thanks for all your advice ...... our sys admin says that once the
:>first job starts running :

:>It will read in the latest GDG for each of the three files, as an
:>example this will be GDG(0) and it will output the unused records to
:>GDG(+1).

:>If the second job is started before the first has finished it will try
:>to use GDG(0) and will wait till it's free.

:>Once the first job has completed the second will start using GDG(0) not
:>the latest GDG (GDG(+1)) which has been created by the first job.

:>When the second job is complete it will create GDG(+2).

:>What I believe will happen with two concurrent jobs :
:>GDG(0)   - Input file into Job #1 & Job #2
:>GDG(+1) - Output from Job #1
:>GDG(+2) - Output from Job #2

Wrong.

If the base name is specified it is serialized across jobs. Thus by specifying
DSN=GDG(+1),DISP=NEW in both jobs, the second job will wait until the first
completes and will then resolve the generation number. 

:>What I would like to have happen with two concurrent jobs :
:>GDG(0)   - Input file into Job #1
:>GDG(+1) - Output from Job #1 & Input into Job #2
:>GDG(+2) - Output from Job #2

That is what will happen (if JCL is used against the base name).
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
