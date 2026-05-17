[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Do you need to read COBOL data files in the R Project for Statistical Computing?

_6 messages · 2 participants · 2020-04 → 2020-06_

---

### Do you need to read COBOL data files in the R Project for Statistical Computing?

- **From:** "thomas.fuller" <ua-author-14501893@usenetarchives.gap>
- **Date:** 2020-04-27T10:29:01+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<03a4b564-6475-41e0-b081-915386519f7c@googlegroups.com>`

```
Hi Folks,

I'd like to bring your attention to the open-source R COBOL Data Integration (RCOBOLDI) package for importing COBOL data files directly into the R Project for Statistical Computing as properly structured data frames.

Please find the project on GitHub here:

https://github.com/thospfuller/rcoboldi

Releases are available in a Drat repository and this is described in detail in the instructions.

and I also have an image available on DockerHub so you can work with the package in minutes if you have Docker available -- see here:

https://hub.docker.com/r/thospfuller/rcoboldi-rocker-rstudio

I welcome your feedback.

Tom
```

#### ↳ Re: Do you need to read COBOL data files in the R Project for Statistical Computing?

- **From:** "kilgasto" <ua-author-14501876@usenetarchives.gap>
- **Date:** 2020-05-20T03:49:02+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-aeaa65de1f-p2@usenetarchives.gap>`
- **In-Reply-To:** `<03a4b564-6475-41e0-b081-915386519f7c@googlegroups.com>`
- **References:** `<03a4b564-6475-41e0-b081-915386519f7c@googlegroups.com>`

```
I clearly laud the effort. But in my experience there is not a special "cobol" data file format. File formats are given in file systems, subsystems of operating systems.
So on a Z/OS - the typical cobol program will write either key-sequenced datasets or entry-sequenced datasets - and can exchange them with pl/1 or or language programs without a hassle. (or they write db2 databases).
Same for Cobol on HP nonstop, another of the cobol giants. The files are defined in the operating systems.

R systems might benefit greatly, OTOH, if they can integrate with the Data Dictionary product on the host machine. On HP nonstops this would be the DDL product under the enscribe system, and i cant remember anymore what, on the zos. Because that would deliver the formatting of the data into the R programs. and this would be worthwhile.
IS it actually this you have to offer?






mandag den 27. april 2020 kl. 16.29.29 UTC+2 skrev Thomas Fuller:
› Hi Folks,
› 
…[14 more quoted lines elided]…
› Tom
```

##### ↳ ↳ Re: Do you need to read COBOL data files in the R Project for Statistical Computing?

- **From:** "thomas.fuller" <ua-author-14501893@usenetarchives.gap>
- **Date:** 2020-05-20T09:11:03+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-aeaa65de1f-p3@usenetarchives.gap>`
- **In-Reply-To:** `<gap-aeaa65de1f-p2@usenetarchives.gap>`
- **References:** `<03a4b564-6475-41e0-b081-915386519f7c@googlegroups.com> <gap-aeaa65de1f-p2@usenetarchives.gap>`

```
Thanks for your response.

Re: "IS it actually this you have to offer?"

The RCOBOLDI package relies (internally) on a Java API called JRecord (which I did not develop), which actually does most of the transformation and supports several COBOL data formats, for example in R:

result <- RCOBOLDI::ReadCopyBookAsDataFrame("DTAR020.cbl", "DTAR020.bin", "Fixed Length Binary", "cp037")

File Structures supported include (this is taken from the JRecord Cobol2Csv application and is supported by RCOBOLDI since it relies on that API):

Default : Determine by Copybook
Text : Use Standard Text IO
Fixed_Length : Fixed record Length binary
Mainframe_VB : Mainframe VB File
Mainframe_VB_As_RECFMU : Mainframe VB File including BDW (block descriptor word)
FUJITSU_VB : Fujitsu Cobol VB File
Open_Cobol_VB: Gnu Cobol VB File

Cobol dialects supported:

0 or Intel : Intel little endian
1 or Mainframe : Mainframe big endian (Default)
4 or Open_Cobol_Little_Endian_(Intel) : Gnu:Cobol
2 or Fujitsu : Fujitsu Cobol

If you want to see what JRecord can do, please see here:

https://github.com/bmTas/JRecord

and

https://sourceforge.net/projects/jrecord/

Tom

On Wednesday, May 20, 2020 at 3:50:03 AM UTC-4, kil··.@gm··l.com wrote:
› I clearly laud the effort. But in my experience there is not a special "cobol" data file format. File formats are given in file systems, subsystems of operating systems. 
› So on a Z/OS - the typical cobol program will write either key-sequenced datasets or entry-sequenced datasets - and can exchange them with pl/1 or or language programs without a hassle. (or they write db2 databases).
…[27 more quoted lines elided]…
›› Tom
```

###### ↳ ↳ ↳ Re: Do you need to read COBOL data files in the R Project for Statistical Computing?

- **From:** "kilgasto" <ua-author-14501876@usenetarchives.gap>
- **Date:** 2020-05-20T12:11:04+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-aeaa65de1f-p4@usenetarchives.gap>`
- **In-Reply-To:** `<gap-aeaa65de1f-p3@usenetarchives.gap>`
- **References:** `<03a4b564-6475-41e0-b081-915386519f7c@googlegroups.com> <gap-aeaa65de1f-p2@usenetarchives.gap> <gap-aeaa65de1f-p3@usenetarchives.gap>`

```
Ah, cobol copy books. yes, COPY libraries that define records for files and otherwise. OK i see what you have got there.
They are more or less the ".H files of Cobol". it still really isnt a "cobol" file but i can see what you are driving at.

I am certain this is a worthwhile tool.

onsdag den 20. maj 2020 kl. 15.11.49 UTC+2 skrev Thomas Fuller:
› Thanks for your response.
› 
…[63 more quoted lines elided]…
››› Tom
```

###### ↳ ↳ ↳ Re: Do you need to read COBOL data files in the R Project for Statistical Computing?

_(reply depth: 4)_

- **From:** "thomas.fuller" <ua-author-14501893@usenetarchives.gap>
- **Date:** 2020-05-21T11:23:05+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-aeaa65de1f-p5@usenetarchives.gap>`
- **In-Reply-To:** `<gap-aeaa65de1f-p4@usenetarchives.gap>`
- **References:** `<03a4b564-6475-41e0-b081-915386519f7c@googlegroups.com> <gap-aeaa65de1f-p2@usenetarchives.gap> <gap-aeaa65de1f-p3@usenetarchives.gap> <gap-aeaa65de1f-p4@usenetarchives.gap>`

```
On Wednesday, May 20, 2020 at 12:11:35 PM UTC-4, kil··.@gm··l.com wrote:
› Ah, cobol copy books. yes, COPY libraries that define records for files and otherwise. OK i see what you have got there.
› They are more or less the ".H files of Cobol". it still really isnt a "cobol" file but i can see what you are driving at.
…[69 more quoted lines elided]…
›››› Tom

I hope it's useful and that people use it. There's another open-source API which offers similar functionality called cobrix, however cobrix targets the Apache Spark cluster computing platform. The reason I mention Cobrix is that it has 61 stars and 38 forks as of today so I'm assuming someone finds it useful and if people need this functionality in Spark, they might also need it in R.

https://github.com/AbsaOSS/cobrix

Tom
```

###### ↳ ↳ ↳ Re: Do you need to read COBOL data files in the R Project for Statistical Computing?

_(reply depth: 5)_

- **From:** "thomas.fuller" <ua-author-14501893@usenetarchives.gap>
- **Date:** 2020-06-15T12:58:06+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-aeaa65de1f-p6@usenetarchives.gap>`
- **In-Reply-To:** `<gap-aeaa65de1f-p5@usenetarchives.gap>`
- **References:** `<03a4b564-6475-41e0-b081-915386519f7c@googlegroups.com> <gap-aeaa65de1f-p2@usenetarchives.gap> <gap-aeaa65de1f-p3@usenetarchives.gap> <gap-aeaa65de1f-p4@usenetarchives.gap> <gap-aeaa65de1f-p5@usenetarchives.gap>`

```
On Thursday, May 21, 2020 at 11:23:30 AM UTC-4, Thomas Fuller wrote:
› On Wednesday, May 20, 2020 at 12:11:35 PM UTC-4, kil··.@gm··l.com wrote:
›› Ah, cobol copy books. yes, COPY libraries that define records for files and otherwise. OK i see what you have got there.
…[76 more quoted lines elided]…
› Tom

Join us this Friday, June 19th, at noon (EST) over Zoom when I will discuss the open-source R COBOL DI (Data Integration) Package (RCOBOLDI).

RCOBOLDI allows data scientists to import COBOL CopyBook data files directly into R as properly structured data frames.

The RCOBOLDI project is written in R script and Java and utilizes the JRecord API which actually does most of the transformation and supports several COBOL data formats and has been released under the #opensourcesoftware LGPL license.

The package is available on DockerHub as well so one can get up and running in a few minutes simply by pulling a Docker image and creating a container.

File Structures supported include:
- Default : Determine by Copybook
- Text : Use Standard Text IO
- Fixed_Length : Fixed record Length binary
- Mainframe_VB : Mainframe VB File
- Mainframe_VB_As_RECFMU : Mainframe VB File including BDW (block descriptor word)
- FUJITSU_VB : Fujitsu Cobol VB File
- Open_Cobol_VB: Gnu Cobol VB File

Dialects supported include:
- 0 or Intel : Intel little endian
- 1 or Mainframe : Mainframe big endian (Default)
- 4 or Open_Cobol_Little_Endian_(Intel) : Gnu:Cobol
- 2 or Fujitsu : Fujitsu Cobol

Questions and comments are welcomed.

https://www.meetup.com/Washington-DC-CTO-Meetup-Group/events/270883610/
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
