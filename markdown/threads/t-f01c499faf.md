[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Program works fine in JCL but not when imbedded in a PROC

_6 messages · 5 participants · 2006-02_

**Topics:** [`Mainframe, z/OS, JCL, CICS`](../topics.md#mainframe)

---

### Program works fine in JCL but not when imbedded in a PROC

- **From:** "CHSB" <CBehrends@maccnet.com>
- **Date:** 2006-02-20T09:01:12-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1140454872.930360.232760@g14g2000cwa.googlegroups.com>`

```
I am having a problem where my COBOL programs do not work when located
inside a PROC but execute fine when submitted as normal JCL.  I looks
like the problem is with overlaid storage because I get errors like
USER-ABEND CODE 4083 and SEGMENT TRANSLATION EXCEPTION depending on
which program I run.  I even commented out all of the code on one
program except one display statement and still get the error.  My
thought is that when the JCL is inside a PROC that the system doesn't
allocate the proper storage for the program and it ends up writing over
storage.  I tried modifying the SIZE parameter on the EXEC PGM=....
statement to add an extra meg of storage but still get the same error.
Is there anyway to specify a size when executing the PROC itself or
does anyone have any ideas as to how I might fix this error?

Thanks

Chris
```

#### ↳ Re: Program works fine in JCL but not when imbedded in a PROC

- **From:** Arnold Trembley <arnold.trembley@worldnet.att.net>
- **Date:** 2006-02-20T20:31:20+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<sGpKf.433872$qk4.308199@bgtnsc05-news.ops.worldnet.att.net>`
- **In-Reply-To:** `<1140454872.930360.232760@g14g2000cwa.googlegroups.com>`
- **References:** `<1140454872.930360.232760@g14g2000cwa.googlegroups.com>`

```


CHSB wrote:
> I am having a problem where my COBOL programs do not work when located
> inside a PROC but execute fine when submitted as normal JCL.  I looks
…[14 more quoted lines elided]…
> 

Please post examples of both the JCL version and the PROC version. 
The PROC version should include the JCL that invokes the PROC.  One 
possibility is that your JCL includes JOBLIB DD statements that are 
missing from the PROC version.
```

##### ↳ ↳ Re: Program works fine in JCL but not when imbedded in a PROC

- **From:** Howard Brazee <howard@brazee.net>
- **Date:** 2006-02-20T13:50:58-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<grakv1pi6h4vlmg4hshand6d95f3js5nn2@4ax.com>`
- **References:** `<1140454872.930360.232760@g14g2000cwa.googlegroups.com> <sGpKf.433872$qk4.308199@bgtnsc05-news.ops.worldnet.att.net>`

```
On Mon, 20 Feb 2006 20:31:20 GMT, Arnold Trembley
<arnold.trembley@worldnet.att.net> wrote:

>Please post examples of both the JCL version and the PROC version. 
>The PROC version should include the JCL that invokes the PROC.  One 
>possibility is that your JCL includes JOBLIB DD statements that are 
>missing from the PROC version.

That makes sense.   Try replacing the JOBLIB statements with STEPLIB
statements.
```

###### ↳ ↳ ↳ Re: Program works fine in JCL but not when imbedded in a PROC

- **From:** CG <carl.gehr.RemoveThis@ThisToo.attglobal.net>
- **Date:** 2006-02-20T19:39:29-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<32c3f$43fa6142$453db2dd$3639@FUSE.NET>`
- **In-Reply-To:** `<grakv1pi6h4vlmg4hshand6d95f3js5nn2@4ax.com>`
- **References:** `<1140454872.930360.232760@g14g2000cwa.googlegroups.com> <sGpKf.433872$qk4.308199@bgtnsc05-news.ops.worldnet.att.net> <grakv1pi6h4vlmg4hshand6d95f3js5nn2@4ax.com>`

```
Howard Brazee wrote:
> On Mon, 20 Feb 2006 20:31:20 GMT, Arnold Trembley
> <arnold.trembley@worldnet.att.net> wrote:
…[7 more quoted lines elided]…
> statements.
JOBLIB and STEPLIB are identical in function.  The only difference is 
the scope of the statement.  Arnold's comment, I believe, is more a case 
of there either is a xxxLIB statement or there is not one applicable 
when the program runs or does not run.

JCL is JCL:  There is no combination of valid JCL that cannot be created 
via a PROC.  You just need to be sure, for example, when you are doing 
an override that you are overriding the specific statement in the 
specific step that you intend.

So, the specific JESn messages will be very key in diagnosing your 
problem.  BTW, tell us which JESn are you running along with the other 
environmental info Arnold mentioned such as compiler, MVS-OS/390-z/OS 
release, etc.
```

#### ↳ Re: Program works fine in JCL but not when imbedded in a PROC

- **From:** "Robert Jones" <rjones0@hotmail.com>
- **Date:** 2006-02-20T12:35:42-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1140467742.438060.81850@g47g2000cwa.googlegroups.com>`
- **In-Reply-To:** `<1140454872.930360.232760@g14g2000cwa.googlegroups.com>`
- **References:** `<1140454872.930360.232760@g14g2000cwa.googlegroups.com>`

```

CHSB wrote:
> I am having a problem where my COBOL programs do not work when located
> inside a PROC but execute fine when submitted as normal JCL.  I looks
…[13 more quoted lines elided]…
> Chris

Hello Chris

Conceptually there is no reason why they shouldn't run in a PROC.
Though you don't specify it, I presume you are running under some
flavour of IBM MVS.  It usually helps to specify the hardware,
operating system and compiler version in use.  In this case, you should
review the PROC JCL expansion, which can be obtained with MSGLEVEL(1,1)
on the JOB card.  This should tell you what options are being set from
within the PROC and you can hopefully resolve the problem yourself from
there, if not come back to us with the details of the parameters set
within the PROC that differ from those you have set yourself in the
plain JCL version that works.

Robert
```

##### ↳ ↳ Re: Program works fine in JCL but not when imbedded in a PROC

- **From:** "Robert Jones" <rjones0@hotmail.com>
- **Date:** 2006-02-21T12:59:24-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1140555564.836414.311320@f14g2000cwb.googlegroups.com>`
- **In-Reply-To:** `<1140467742.438060.81850@g47g2000cwa.googlegroups.com>`
- **References:** `<1140454872.930360.232760@g14g2000cwa.googlegroups.com> <1140467742.438060.81850@g47g2000cwa.googlegroups.com>`

```
Bottom posting only

Robert Jones wrote:
> CHSB wrote:
> > I am having a problem where my COBOL programs do not work when located
…[29 more quoted lines elided]…
> Robert

I should have also suggested that you add ',TYPRUN=SCAN' to the end of
your JOB statement  when first using MSGLEVEL=(1,1), this allows the
JCL interpreter to expand the JCL in the PROC to show the parameter
substitutions without executing it.  Alternatively, just list the
contents of the PROC from wherever it is stored.  This wouldn't show
how the substitutions were actually applied, but you could work out
what they would be manually.

Robert

Robert
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
