[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Recalling source code.

_8 messages · 6 participants · 2002-06_

---

### Recalling source code.

- **From:** nivas_shyam@indiatimes.com (shyam nivas)
- **Date:** 2002-06-01T00:03:32-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<c02fd744.0205312303.5abd205f@posting.google.com>`

```
Hi,
          Once by mistake I put the load in the same PDS where my
source is and
finally my source code get screwed. Is there any method of recalling
the source code?

Regards,
Shyam
```

#### ↳ Re: Recalling source code.

- **From:** docdwarf@panix.com
- **Date:** 2002-06-01T09:20:54-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<adahnm$s4j$1@panix1.panix.com>`
- **References:** `<c02fd744.0205312303.5abd205f@posting.google.com>`

```
In article <c02fd744.0205312303.5abd205f@posting.google.com>,
shyam nivas <nivas_shyam@indiatimes.com> wrote:
>Hi,
>          Once by mistake I put the load in the same PDS where my
>source is and
>finally my source code get screwed. Is there any method of recalling
>the source code?

That depends on what your site's backup standards are... be prepared, you 
have made a common mistake and you are not going to be able to keep it 
secret; people will make fun of you, point at you and laugh.

DD
```

##### ↳ ↳ Re: Recalling source code.

- **From:** jnjsle@aol.com (Jnjsle)
- **Date:** 2002-06-01T18:28:19+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<20020601142819.28330.00001764@mb-mh.aol.com>`
- **References:** `<adahnm$s4j$1@panix1.panix.com>`

```
Hi Shy,

I've come across this a few times, but I'll be damned if I can recall the
solution. It's very simple, too!

Have you tried recompiling and linking another pgm using the approprate
libraries?
Give it a shot; I think that's all that's required.

When you made the error the DSCB (or the Catalog entry) of the source lib was
changed to contain the DS attributes of the Link library (RECFM U and a large,
27K+ LRECL).

I'm not sure why a recompile/relink returns them to their original state, but
give it a try.
Sorry I couldn't be more definite.
  
 Jack.
```

###### ↳ ↳ ↳ Re: Recalling source code.

- **From:** Liam Devlin <LiamDD@optonline.net>
- **Date:** 2002-06-02T05:45:36+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3CF9B0EE.20105@optonline.net>`
- **References:** `<adahnm$s4j$1@panix1.panix.com> <20020601142819.28330.00001764@mb-mh.aol.com>`

```
Jnjsle wrote:

> Hi Shy,
> 
…[13 more quoted lines elided]…
> Sorry I couldn't be more definite.


You may have an Undelete function in MVS / OS/390 / z/OS. It was on the 
Utility panel, option 3, the last place I worked. If you have it, it'll 
give you a list of every backup, i.e., every Save, of every member 
altered since the last compress, so you'll have to browse thru the list 
to find the most recent copy of your pgm. Good luck.
```

###### ↳ ↳ ↳ Re: Recalling source code.

_(reply depth: 4)_

- **From:** jnjsle@aol.com (Jnjsle)
- **Date:** 2002-06-02T15:42:36+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<20020602114236.06614.00001771@mb-ca.aol.com>`
- **References:** `<3CF9B0EE.20105@optonline.net>`

```
OK Shy,

Here's another approach. Since the data content of your source lib has remained
unchanged in spite of your misstep, try copying the library using IEBGENER, or
SYNCSORT or DFSORT or whatever.

Be sure to explicitly define the DCBs for the sending and receiving DDs as:

DCB=(DSORG=PO,RECFM=FB,LRECL=80,BLKSIZE=n) 
where, n = the blocksize of your source lib before the "accident" occured.

I'm sure you'll find the library "restored".

Jack
```

#### ↳ Re: Recalling source code.

- **From:** "Rick Hood" <RickHood@insightbb.com>
- **Date:** 2002-06-01T19:01:56+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<ES8K8.79490$ux5.100538@rwcrnsc51.ops.asp.att.net>`
- **References:** `<c02fd744.0205312303.5abd205f@posting.google.com>`

```
Shyam:

You didn't mention what environment you're using, so I will assume that it
is MVS/TSO.  Actually, you're dealing with two separate issues here.  First,
you need to assess the extent of the damage to your source PDS.  Second, you
need to restore your original source.

Source libraries are usually RECFM=FB and LRECL=80 whereas load libraries
are usually RECFM=U and LRECL=0.  If the linkage editor changed the DCB
information on your source PDS or messed it up in any other way, then you
will probably have to restore the entire PDS.  However, if the DCB
information is intact and you can access other members of the PDS you may
only have to restore the individual member.

Assuming that your site uses SMS to manage disk space and that you didn't
create the source member today, you could check to see if there is a backup
copy of the dataset available.  From a TSO ready prompt or ISPF option 6,
enter the following command replacing the sample dataset name with yours of
course:

        HLIST 'userid.source.cobol' BCDS

This command checks the Backup Control Data Set (BCDS) to see if there are
any backup copies of the specified dataset available.  I haven't done this
for a while, so I'm not sure the syntax is exactly right, but you can enter
"HELP HLIST" to verify the syntax.  If the HLIST command shows that there is
a backup available, enter the following command to restore it to a temporary
dataset name:

        HRECOVER DATASET('userid.source.cobol')
                              NEWNAME('userid.source.cobol.temp')
                              GEN(??)

Again, I'm not sure the syntax is exactly right, so you might want to check
it via "HELP HRECOVER".  Check the output of the HLIST command to get the
value for the generation (GEN) number.  After the dataset is restored
successfully, you can either copy the individual member from the temporary
dataset to your original dataset and delete the temporary dataset, or delete
your original dataset and rename the temporary dataset.  Now you should be
back in business!

If you are unable to resolve the situation yourself, you can always ask for
assistance from your technical support team.  That's what they are there
for.

Good luck,
Rick


"shyam nivas" <nivas_shyam@indiatimes.com> wrote in message
news:c02fd744.0205312303.5abd205f@posting.google.com...
> Hi,
>           Once by mistake I put the load in the same PDS where my
…[5 more quoted lines elided]…
> Shyam
```

#### ↳ Re: Recalling source code.

- **From:** "Kjeld Hansen" <paabol@12mail.dk>
- **Date:** 2002-06-01T23:15:57+02:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3cf9398d$0$9117$edfadb0f@dspool01.news.tele.dk>`
- **References:** `<c02fd744.0205312303.5abd205f@posting.google.com>`

```
You can use a utility like PDSFAST or a SAS procedure (can't remember the
name of the proc) to recover overwritten PDS-members, as long as the dataset
hasn't been compressed, and assuming the linkage editor didn't alter the
dataset organisation..

Good luck..

Kjeld Paab�l Hansen


"shyam nivas" <nivas_shyam@indiatimes.com> skrev i en meddelelse
news:c02fd744.0205312303.5abd205f@posting.google.com...
> Hi,
>           Once by mistake I put the load in the same PDS where my
…[5 more quoted lines elided]…
> Shyam
```

##### ↳ ↳ Re: Recalling source code.

- **From:** jnjsle@aol.com (Jnjsle)
- **Date:** 2002-06-02T04:08:56+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<20020602000856.14149.00001972@mb-cj.aol.com>`
- **References:** `<3cf9398d$0$9117$edfadb0f@dspool01.news.tele.dk>`

```
Hi Shy,

As I stated before, I've seen this happen on more than one occasion. There is
nothing permanently wrong with the contents of the PDS. The contents are NOT
permanently compromised. The dataset has just been "reblocked".

When you look at a member via ISPF Edit, you'll probably only see the first
card of the program. Maybe some other code, if the pgm is big. This results
from the data being "reblocked" as ~27k Undefined records. If you PF11 across
the record you'll see the rest of the pgm code in the record.

Try what I've suggested. If it doesn't correct the problem, talk to your
sysprog. He's probably encountered it before.

Jack
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
