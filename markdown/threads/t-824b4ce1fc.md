[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# vutil

_5 messages · 4 participants · 1999-07_

---

### vutil

- **From:** jrogers42@hotmail.com
- **Date:** 1999-07-28T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7nn641$d2$1@nnrp1.deja.com>`

```
I need to know how to reverse this command.

vutil -R -A +C -F variableA variableB



Sent via Deja.com http://www.deja.com/
Share what you know. Learn what you don't.
```

#### ↳ Re: vutil

- **From:** "Cheesle" <cheesle@online.NoSpamPlease.no>
- **Date:** 1999-07-28T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7nnqic$r0c$1@news.cerf.net>`
- **References:** `<7nn641$d2$1@nnrp1.deja.com>`

```
jrogers42@hotmail.com wrote in message <7nn641$d2$1@nnrp1.deja.com>...
>I need to know how to reverse this command.
>
>vutil -R -A +C -F variableA variableB

I assume this is for Acucobol vision?

-r is nothing to reverse.

-a is nothing to reverse.

+c, the opposite of compression on, is compression off, hence: -c

Compression off, does not need a factor, hence nothing to reverse of -f.
Then no variableA, I assume variableB is your filename, this is constant.

The I would do:

vutil -R -A -C variableB
```

#### ↳ Re: vutil

- **From:** "Warren Porter" <warrenp123@netdoor123.com>
- **Date:** 1999-07-28T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<ikGn3.407$_3.10479@axe.netdoor.com>`
- **References:** `<7nn641$d2$1@nnrp1.deja.com>`

```
I assume you are talking about AcuCobol 85.  If so,
1) Perhaps you don't need to do anything except give the world permission to
read the file.  You created a new file with your default permissions while
the old one was deleted;  your new file was renamed automatically (the -a
operator).  Just do a

  chmod 666 variableA variableB

Before trying the next two (if necessary), back up your existing file first.
2) You might have to rebuild the file based on something other than it's
primary key.  If that is the case, specify -k n  when you run vutil against
that file again where n is > 0.

3) The file is FUBAR.  If you can restore from a backup, try to do so.
Otherwise unload the file and recreate (generate) the indexed file, then
reload it.  The vutil program is documented in the AcuCobol-85 "User's
Guide".

Good luck.

jrogers42@hotmail.com wrote in message <7nn641$d2$1@nnrp1.deja.com>...
>I need to know how to reverse this command.
>
>vutil -R -A +C -F variableA variableB
```

#### ↳ Re: vutil

- **From:** "Robert Annandale" <zimboon @ hotmail . com>
- **Date:** 1999-07-28T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<379f4630$0$19193@fountain.mindlink.net>`
- **References:** `<7nn641$d2$1@nnrp1.deja.com>`

```
Your files are gone.
They were automatically replaced when you used the -a command.
It should always be a habit to make a copy of a file before a rebuild.

Assuming the rebuild was successful (no broken chains)
then all you would of lost is 'deleted records' that Vision
hangs on to until a rebuild clears them.

As for the reversal, you can still reverse the compression you stipulated.

May I suggest you do the following;

- backup the current file (This should be second nature, like 'rm -i
filename'!!!!)
- vutil -c filename (This will reverse compression).

Why do you want to reverse it anyways?
What is it you wish to undo?

Robert Annandale
Vancouver, BC

> I need to know how to reverse this command.
>
…[5 more quoted lines elided]…
> Share what you know. Learn what you don't.
```

#### ↳ Re: vutil

- **From:** redsky@ibm.net (Thane Hubbell)
- **Date:** 1999-07-29T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<379fcc07.54401058@news1.ibm.net>`
- **References:** `<7nn641$d2$1@nnrp1.deja.com>`

```
On Wed, 28 Jul 1999 15:03:35 GMT, jrogers42@hotmail.com wrote:

>I need to know how to reverse this command.
>
>vutil -R -A +C -F variableA variableB
>

The first thing that struck *ME* about this message was RACF - the IBM
Mainframe security utility. It Scared me and I skipped to the next
message. <G>.
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
