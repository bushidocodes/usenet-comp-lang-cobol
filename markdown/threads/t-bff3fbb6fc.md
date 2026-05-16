[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Is Global Copy Possible?

_5 messages · 5 participants · 2005-08 → 2005-09_

**Topics:** [`Language features and syntax`](../topics.md#syntax)

---

### Is Global Copy Possible?

- **From:** "Chris" <ctaliercio@yahoo.com>
- **Date:** 2005-08-29T13:45:26-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1125348326.679722.231110@g49g2000cwa.googlegroups.com>`

```
I know this is probably reaching, but I'm always looking for a way to
do things more simplistically.

Does anyone know of a way to include a specific copy file in every
program belonging to an application without explicitly using a COPY
statement inside of the programs? For example, can I add it as a
compile time option?

More specifically I am looking to include the same list of EXTERNAL
variables in each program that is a member of my application without
having to add a line like:

COPY "EXTERNALS.WS"

These values are static values and each program within the application
will need to know the value of them. But rather than have each program
look them up in the database, and make each program more efficient, the
initial program looks up and populates these values. Then since they
are declared as external in all of the other applications the values
carry automatically.

I'm using MF Server Express 4.0 SP2 on HP-UX11i.

Thanks in advance!
Chris
```

#### ↳ Re: Is Global Copy Possible?

- **From:** "Richard" <riplin@Azonic.co.nz>
- **Date:** 2005-08-29T13:48:32-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1125348512.260112.126680@g44g2000cwa.googlegroups.com>`
- **In-Reply-To:** `<1125348326.679722.231110@g49g2000cwa.googlegroups.com>`
- **References:** `<1125348326.679722.231110@g49g2000cwa.googlegroups.com>`

```

Chris wrote:
> Does anyone know of a way to include a specific copy file in every
> program belonging to an application without explicitly using a COPY
> statement inside of the programs? For example, can I add it as a
> compile time option?

No.
```

#### ↳ Re: Is Global Copy Possible?

- **From:** "William M. Klein" <wmklein@nospam.netcom.com>
- **Date:** 2005-08-29T21:03:49+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<VKKQe.227061$uo4.198269@fe01.news.easynews.com>`
- **References:** `<1125348326.679722.231110@g49g2000cwa.googlegroups.com>`

```
You certainly COULD create your own "preprocessor" to do this.

For information on how to create and access such a thing in Server Express 4.0, 
see

 "Chapter 16: Integrated Preprocessor Interface"

in the "Program Development" manual.

Having said that, I am not really certain that it would be worth it, but it is 
POSSIBLE.
```

#### ↳ Re: Is Global Copy Possible?

- **From:** Paul Knudsen <bigkahuna@jupada.com>
- **Date:** 2005-09-09T00:10:53-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<6ad2i11spnjl5nc4tejjte1k36lchahohv@4ax.com>`
- **References:** `<1125348326.679722.231110@g49g2000cwa.googlegroups.com>`

```
Change your compile jobs to copy the source, inserting the new code.

On 29 Aug 2005 13:45:26 -0700, "Chris" <ctaliercio@yahoo.com> wrote:

>I know this is probably reaching, but I'm always looking for a way to
>do things more simplistically.
…[22 more quoted lines elided]…
>Chris
```

##### ↳ ↳ Re: Is Global Copy Possible?

- **From:** Russell <rws0203nospam@comcast.net>
- **Date:** 2005-09-09T10:02:58-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<Xns96CC70693D591rws0203comcastnet@216.196.97.131>`
- **References:** `<1125348326.679722.231110@g49g2000cwa.googlegroups.com> <6ad2i11spnjl5nc4tejjte1k36lchahohv@4ax.com>`

```
Paul Knudsen <bigkahuna@jupada.com> wrote in 
news:6ad2i11spnjl5nc4tejjte1k36lchahohv@4ax.com:

> Change your compile jobs to copy the source, inserting the new code.
> 
…[27 more quoted lines elided]…
> 

    	Do you already have one or more copy files that are used in every 
program, or almost every program?  If so, you can use the conditional 
compile feature to conditionally copy this copy file, either as a nested 
copy, or by physically adding the data to the other copy(s).

    	Use the "if defined" along with a 78 level.  If you are clever, you 
can acomplish a lot.  This would leave manually handling the residue.
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
