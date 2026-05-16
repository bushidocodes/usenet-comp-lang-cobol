[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# How do I FTP load modules from MVS-->PC-->MVS

_10 messages · 7 participants · 2000-03_

**Topics:** [`Mainframe, z/OS, JCL, CICS`](../topics.md#mainframe) · [`Help requests and how-to`](../topics.md#help)

---

### How do I FTP load modules from MVS-->PC-->MVS

- **From:** gliptak@viewtech.com.au
- **Date:** 2000-03-05T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<38C21C29.73AC6914@viewtech.com.au>`

```
I am having great difficulty transferring cobol load modules from the
MVS to a PC and then Back to the MVS.  I am using IBM's Personnal
Communicator Emulation software.

The load modules on the MVS reside in a PDS and I FTP them to the PC
using the binary option with a record format of 'U'  (undefined).  I use
the same options when transferring back from the PC to the MVS.  The
transfers work OK but the load module is unusable on the MVS.

Anyone have any ideas.
```

#### ↳ Re: How do I FTP load modules from MVS-->PC-->MVS

- **From:** theodp@aol.com (Theo DP)
- **Date:** 2000-03-05T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<20000305135527.03672.00000544@ng-ba1.aol.com>`
- **References:** `<38C21C29.73AC6914@viewtech.com.au>`

```
>Subject: How do I FTP load modules from MVS-->PC-->MVS
>From: gliptak@viewtech.com.au
…[20 more quoted lines elided]…
>

Make sure the BINary option is set.

You'll run into problems if the TEXT option (usually the default) is set.

HTH
```

#### ↳ Re: How do I FTP load modules from MVS-->PC-->MVS

- **From:** "DennisHarley" <LegacyBlue@email.msn.com>
- **Date:** 2000-03-05T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<u8$9#9ph$GA.215@cpmsnbbsa02>`
- **References:** `<38C21C29.73AC6914@viewtech.com.au>`

```
Don't do it.

Why are you doing this with load modules?

<gliptak@viewtech.com.au> wrote in message
news:38C21C29.73AC6914@viewtech.com.au...
> I am having great difficulty transferring cobol load modules from the
> MVS to a PC and then Back to the MVS.  I am using IBM's Personnal
…[9 more quoted lines elided]…
>
```

##### ↳ ↳ Re: How do I FTP load modules from MVS-->PC-->MVS

- **From:** gliptak@viewtech.com.au
- **Date:** 2000-03-06T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<38C393C5.3FD9C45C@viewtech.com.au>`
- **References:** `<38C21C29.73AC6914@viewtech.com.au> <u8$9#9ph$GA.215@cpmsnbbsa02>`

```
I need to get load modules from one m/frame site to another and the easiest
way that I know of is to FTP the load modules to a PC, then upload to a web
site where they can be downloaded anywhere anytime.

DennisHarley wrote:

> Don't do it.
>
…[15 more quoted lines elided]…
> >
```

###### ↳ ↳ ↳ Re: How do I FTP load modules from MVS-->PC-->MVS

- **From:** "DennisHarley" <LegacyBlue@email.msn.com>
- **Date:** 2000-03-06T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<uSfoXu2h$GA.276@cpmsnbbsa03>`
- **References:** `<38C21C29.73AC6914@viewtech.com.au> <u8$9#9ph$GA.215@cpmsnbbsa02> <38C393C5.3FD9C45C@viewtech.com.au>`

```
Have you tried TSO Transmit? XMIT

If it can be done, it will eliminate possible PC Upload/download problems.

There may also be a problem if the load libraries have different block
sizes.

There are others who have apparently done this, see other messages in this
thread.

<gliptak@viewtech.com.au> wrote in message
news:38C393C5.3FD9C45C@viewtech.com.au...
> I need to get load modules from one m/frame site to another and the
easiest
> way that I know of is to FTP the load modules to a PC, then upload to a
web
> site where they can be downloaded anywhere anytime.
>
…[13 more quoted lines elided]…
> > > using the binary option with a record format of 'U'  (undefined).  I
use
> > > the same options when transferring back from the PC to the MVS.  The
> > > transfers work OK but the load module is unusable on the MVS.
…[4 more quoted lines elided]…
>
```

#### ↳ Re: How do I FTP load modules from MVS-->PC-->MVS

- **From:** docdwarf@clark.net ()
- **Date:** 2000-03-05T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<T1tw4.408$G15.11018@iad-read.news.verio.net>`
- **References:** `<38C21C29.73AC6914@viewtech.com.au>`

```
In article <38C21C29.73AC6914@viewtech.com.au>,
 <gliptak@viewtech.com.au> wrote:
>I am having great difficulty transferring cobol load modules from the
>MVS to a PC and then Back to the MVS.  I am using IBM's Personnal
…[7 more quoted lines elided]…
>Anyone have any ideas.

Leaving aside the reason for doing such a thing... sounds like
translation-table discrepancies (EBCDIC/ASCII).  Do you have a compare
utility that'll allow you to do byte-by-bytes?

DD
```

#### ↳ Re: How do I FTP load modules from MVS-->PC-->MVS

- **From:** George Young <gmyoung@attglobal.net>
- **Date:** 2000-03-05T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<38C260C2.3D1218E5@attglobal.net>`
- **References:** `<38C21C29.73AC6914@viewtech.com.au>`

```
Even if you succeeded in properly transferring the U format file, the
load module is still unusable because you have lost the PDS directory
entry, which contains critical information for a load module.

A solution is to 'unload' the load module to a transferable file format
that includes the directory information, do the transfer, and then
'reload' at the target site. The TRANSMIT and RECEIVE commands can do
that (the TSO TRANSMIT and RECEIVE commands).

Here are the steps:

On the 'sending MVS system':

 TRANSMIT no.where DATASET('loadmoduledatasetname')
MEMBERS(mem1,mem2,mem3...) OUTDA(load.bin) NONO

This uses the TRANSMIT command to 'unload' the loadmodule dataset into
'yourid.load.bin'. If you leave off the members operand it will just
unload all the members. It doesn't actually TRANSMIT the file to another
node.id, it just unloads it. You do have to give it a node.id, so I just
make up one (no.where).

'yourid.load.bin' is a sequential RECFM(FB) LRECL(80) dataset. TRANSMIT
will make it for you.

Now, transfer the data set to your PC using a binary transfer mechanism.
Carry, e-mail, etc. the file to the target PC, and upload to the target
MVS, again using a binary transfer mechanism. On the upload, you need to
ensure that the upload is done into a RECFM(FB) LRECL(80) dataset. It is
critical that the target binary file have this format.

On the 'receiving MVS system':

 RECEIVE INDA(load.bin)
 hit enter at prompt 

Either hit enter at prompt, or type in

 DSN('newloadmoduledatasetname')

You'll now have an exact copy of the load module PDS you started with
(or members of it).
 
As an aside, you mentioned both Personal Communications and FTP. If you
are using FTP directly, just do a BIN before the GET and PUT. In
addition, pre-allocate the target 'yourid.load.bin' on MVS before doing
the PUT. If you are using the Personal Communications transfer dialog
(that uses $INDFILE), I think you'll have to go into the Setup subdialog
before doing the upload and make a special format for FB 80 binary (I
seem to remember that if I didn't, that PCOMM would upload ok, but I'd
end up with a RECFM(VB) dataset and RECEIVE would choke). Again, with
PCOMM, I still recommend preallocating the 'yourid.load.bin' (as FB 80).

George

gliptak@viewtech.com.au wrote:
> 
> I am having great difficulty transferring cobol load modules from the
…[8 more quoted lines elided]…
> Anyone have any ideas.
```

##### ↳ ↳ Re: How do I FTP load modules from MVS-->PC-->MVS

- **From:** gliptak@viewtech.com.au
- **Date:** 2000-03-06T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<38C3944D.8F395CCE@viewtech.com.au>`
- **References:** `<38C21C29.73AC6914@viewtech.com.au> <38C260C2.3D1218E5@attglobal.net>`

```
This works like a dream.  Thanks for your help.

George Young wrote:

> Even if you succeeded in properly transferring the U format file, the
> load module is still unusable because you have lost the PDS directory
…[64 more quoted lines elided]…
> > Anyone have any ideas.
```

#### ↳ Re: How do I FTP load modules from MVS-->PC-->MVS

- **From:** postingid@dissensoftware.com (Binyamin Dissen)
- **Date:** 2000-03-05T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<bnj4cs0ik7jcai9v24ec38nd8h2eivra9n@4ax.com>`
- **References:** `<38C21C29.73AC6914@viewtech.com.au>`

```
On Sun, 05 Mar 2000 19:34:50 +1100 gliptak@viewtech.com.au wrote:

:>I am having great difficulty transferring cobol load modules from the
:>MVS to a PC and then Back to the MVS.  I am using IBM's Personnal
:>Communicator Emulation software.

:>The load modules on the MVS reside in a PDS and I FTP them to the PC
:>using the binary option with a record format of 'U'  (undefined).  I use
:>the same options when transferring back from the PC to the MVS.  The
:>transfers work OK but the load module is unusable on the MVS.

1. TSO XMIT A.B DA('dataset to ship') OUTDA(XMIT.UNL)

2. Download XMIT.UNL as BINARY, no CR/LF.

3. Upload XMIT.UNL as BINARY, no CR.LF, FB, LRECL=80

4. TSO RECEIVE INDA(XMIT.UNL)
   DA('new dsname') VOL(whatever)

ALl done.
```

#### ↳ Re: How do I FTP load modules from MVS-->PC-->MVS

- **From:** Greg Ferro <gferro@sprynet.com>
- **Date:** 2000-03-07T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<38C51BE3.C29A7890@sprynet.com>`
- **References:** `<38C21C29.73AC6914@viewtech.com.au>`

```
One thing that comes to mind is the translation tables that are built into
the file transfer process.  Is the EBCDIC to ASCII conversion process being
invoked?  If so, are the translation tables complimentary?  (i.e., does an
EBCDIC x'40' convert to an ASCII x'20'  on the download and does the process
reverse itself on the upload?)

Why don't you build a one block file on the mainframe consisting of the 256
possible values of x'00' through x'ff', download the file to the PC, upload
it to the mainframe under a new data set name, and compare the 'sent' and
'received' files on the mainframe.
You will either find a discrepancy in the download/upload process or
eliminate the process as a factor in your problem.

Pardon me for asking, but why are you downloading an executable program to
the PC?


gliptak@viewtech.com.au wrote:

> I am having great difficulty transferring cobol load modules from the
> MVS to a PC and then Back to the MVS.  I am using IBM's Personnal
…[7 more quoted lines elided]…
> Anyone have any ideas.
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
