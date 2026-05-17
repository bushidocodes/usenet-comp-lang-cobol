[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# PowerCOBOL

_5 messages · 2 participants · 2013-09 → 2013-11_

---

### PowerCOBOL

- **From:** "dashwood" <ua-author-2154790@usenetarchives.gap>
- **Date:** 2013-09-26T19:49:01+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<bajvg0FktlsU1@mid.individual.net>`

```
I have a client who is converting a PowerCOBOL package to .NET using the
PRIMA Toolset.

This is proving to be quite an effort and before I dive in and re-invent
some wheels I thought I'd just ask the following:

1. Has anyone ever managed to update scriptlets in a PowerCOBOL project
under program control? (NOT by manually editing them).

We can obviously produce a schedule of the changes and where they are
required, for manually cutting and pasting back into the project, but that's
a pretty tedious solution when there are hundreds of projects. We already
have tools that analyze the .PRC code, derive the scriptlets for the project
and transform them. Reading them is no problem; writing them is something
else.

2. It seems to be impossible to pass an object reference easily between
forms in PowerCOBOL. The normal (and documented) way to share data between
forms is by marking it GLOBAL and EXTERNAL. However, it won't let you apply
these clauses to an Object Reference.

Consider the following: (Calling MAIN Form is Form1, Called Form is Form2)

Form1 instantiates an instance of a COM object and uses some of its methods.
(we have the object reference and I'll call it "objRef")

Form1 invokes Form2 (with CALLForm or OPENForm, it doesn't matter...)

We want Form2 to have access to the methods and properties of objRef.
Obviously, if we invoke it, from within Form2 we will get a new instance, so
we really need for objRef to be passed to Form2.

There is no facility I can see in the parameters to OPENForm or CALLForm
that let you pass anything to the new form. Given that Form1 and Form2 are
both in the same project (generated module) you might thnk it should be easy
(at compile time?) for Form1 to get an object reference for Form2 then set a
property in it before opening it. Again, I can find no way in PowerCOBOL to
get a reference to a Form, whether it is opened or not.

I know I can fudge the factory in the objRef component so it will always
return the same instance (it is a "singleton" object), but that involves
overriding the CREATE-OBJECT method of Fujitsu's *COM Class (or changing it
from being a COM component to a standard component and overriding "NEW") and
is a pretty horrendous solution when simply passing the objRef would do the
job.

I can't believe that no-one has encountered this problem, but I know
PowerCOBOL is a dying product and there probably aren't too many people
still using it.

If anyone has any thoughts on either of these problems and is prepared to
share them, I'd be grateful.

Cheers,

Pete.

"I used to write COBOL...now I can do anything."
```

#### ↳ Re: PowerCOBOL

- **From:** "real-email-in-msg-spam" <ua-author-5864872@usenetarchives.gap>
- **Date:** 2013-11-17T13:03:02+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-e2e84fdfa8-p2@usenetarchives.gap>`
- **In-Reply-To:** `<bajvg0FktlsU1@mid.individual.net>`
- **References:** `<bajvg0FktlsU1@mid.individual.net>`

```
On Fri, 27 Sep 2013 11:49:18 +1200, "Pete Dashwood"
wrote:

› I have a client who is converting a PowerCOBOL package to .NET using the 
› PRIMA Toolset.
…[53 more quoted lines elided]…
› Pete.
Hi Peter,

the following works with V8

01 global-variables global.
05 WK PIC X(80).
05 CReportName PIC X(1024).
05 CApplication OBJECT REFERENCE COM.
05 CReport OBJECT REFERENCE COM.
* 05 cob2 redefines Creport pic s9(9) comp-5.
05 sections-obj OBJECT REFERENCE COM.
05 section-obj OBJECT REFERENCE COM.
05 sections-obj-count pic S9(9) COMP-5 value 0.
05 reports-obj OBJECT REFERENCE COM.
05 report-obj OBJECT REFERENCE COM.
05 reports-obj-count pic S9(9) COMP-5 value 0.
05 new-report-obj OBJECT REFERENCE COM.
05 CobReport OBJECT REFERENCE POW-COBJECT.
05 cob1 redefines cobreport pic s9(9) comp-5.
05 null1 pic s9(9) comp-5 value 0.
05 dsp pic z9(9).
05 W-TEXT PIC X(100).
05 W-INDEX PIC 99.
05 W-INDEX1 PIC 99.
05 W-NODE OBJECT REFERENCE POW-CNODE.
01 cobreport1 pic s9(9) comp-5 global external.

- this is something I did for a client to work with Cristal Reports
(another annoying thing as PowerCobol will not work with events
correctly - had to do a VB wrapper)


Frederico Fonseca
ema il: frederico_fonseca at syssoft-int.com
```

##### ↳ ↳ Re: PowerCOBOL

- **From:** "dashwood" <ua-author-2154790@usenetarchives.gap>
- **Date:** 2013-11-17T18:04:03+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-e2e84fdfa8-p3@usenetarchives.gap>`
- **In-Reply-To:** `<gap-e2e84fdfa8-p2@usenetarchives.gap>`
- **References:** `<bajvg0FktlsU1@mid.individual.net> <gap-e2e84fdfa8-p2@usenetarchives.gap>`

```
Frederico Fonseca wrote:
› On Fri, 27 Sep 2013 11:49:18 +1200, "Pete Dashwood"
›  wrote:
…[88 more quoted lines elided]…
› correctly - had to do a VB wrapper)

Hi Frederico, nice to see you back... :-)
I'm not sure what I'm supposed to be looking at here...

Are you saying that because the 01 level is global, these objects are
visible in another form? I don't think so... they would need to be external
and the compiler won't allow it.

I'm interested to see that you successfully redefined CobReport; I have been
unable to redefine an object reference as anything...

Do you move cob1 to cobreport1 somewhere, then reference cobreport1 in
another form?

Maybe it works with object refecrences of type POW-COBJECT; I need it to do
so with type COM.

Thanks for the response; am I missing something?

Pete.
"I used to write COBOL...now I can do anything."
```

###### ↳ ↳ ↳ Re: PowerCOBOL

- **From:** "real-email-in-msg-spam" <ua-author-5864872@usenetarchives.gap>
- **Date:** 2013-11-18T13:40:04+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-e2e84fdfa8-p4@usenetarchives.gap>`
- **In-Reply-To:** `<gap-e2e84fdfa8-p3@usenetarchives.gap>`
- **References:** `<bajvg0FktlsU1@mid.individual.net> <gap-e2e84fdfa8-p2@usenetarchives.gap> <gap-e2e84fdfa8-p3@usenetarchives.gap>`

```
On Mon, 18 Nov 2013 12:04:08 +1300, "Pete Dashwood"
wrote:

› Frederico Fonseca wrote:
›› On Fri, 27 Sep 2013 11:49:18 +1200, "Pete Dashwood"
…[22 more quoted lines elided]…
› Pete.


Sent you an email with sample.

Regarding redefining from COM -- this for others that may look for it.

05 CobReport OBJECT REFERENCE POW-COBJECT.
05 cob1 redefines cobreport pic s9(9) comp-5.
05 CReport OBJECT REFERENCE COM.
CALL "POWERCONVFROMCOM" USING CReport RETURNING CobReport.





Frederico Fonseca
ema il: frederico_fonseca at syssoft-int.com
```

###### ↳ ↳ ↳ Re: PowerCOBOL

_(reply depth: 4)_

- **From:** "dashwood" <ua-author-2154790@usenetarchives.gap>
- **Date:** 2013-11-18T16:49:05+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-e2e84fdfa8-p5@usenetarchives.gap>`
- **In-Reply-To:** `<gap-e2e84fdfa8-p4@usenetarchives.gap>`
- **References:** `<bajvg0FktlsU1@mid.individual.net> <gap-e2e84fdfa8-p2@usenetarchives.gap> <gap-e2e84fdfa8-p3@usenetarchives.gap> <gap-e2e84fdfa8-p4@usenetarchives.gap>`

```
Frederico Fonseca wrote:
› On Mon, 18 Nov 2013 12:04:08 +1300, "Pete Dashwood"
›  wrote:
…[42 more quoted lines elided]…
› ema il: frederico_fonseca at syssoft-int.com

Thanks Frederico, that was very helpful.

Pete.

"I used to write COBOL...now I can do anything."
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
