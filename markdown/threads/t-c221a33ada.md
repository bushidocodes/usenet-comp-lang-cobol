[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# MF Cobol and Longfilenames

_5 messages · 3 participants · 1998-10 → 1998-11_

**Topics:** [`Compilers and vendors`](../topics.md#compilers)

---

### MF Cobol and Longfilenames

- **From:** dblaze@merchants-fla.com
- **Date:** 1998-10-30T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3639d008.69617294@news.mci2000.com>`

```
I've got an application written in MF Cobol 4.0.32 that is using
InstallShield 5.1 Professional for the installation package.  I've
come across a problem when the user specifies a path that contains an
embedded space, such as "Program Files".  I'm saving the directory
name the user selects into an .ini file that I then use to dynamically
assign file names at BOJ.  If the path name is greater than 8
characters and does not contain a space, the file opens OK.  If the
path contains a spaces, the file isn't found.  I checked the MF
Programmer's Guide to File Handling and see that MF Cobol does not
accept embedded spaces in file/path names.  I believe I can force the
long filename to a short one in the InstallShield script by using
"LongPathToShortPath" function but is there a better/easier way within
the Cobol for doing this?  I'm fairly new to MF Cobol (I'm a mainframe
punk as my colleagues say!) so please be explicit if you have a work
around so I can understand what you're referring to.

Thanks,
Doug
```

#### ↳ Re: MF Cobol and Longfilenames

- **From:** "Leif Svalgaard" <leif@ibm.net>
- **Date:** 1998-10-30T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3639d216.0@news1.ibm.net>`
- **References:** `<3639d008.69617294@news.mci2000.com>`

```
You might want to go to http://www.etk.com and look at
our download area (filelong.exe). You find a set of routines
to access long filenames from MF Cobol.

dblaze@merchants-fla.com wrote in message
<3639d008.69617294@news.mci2000.com>...
>I've got an application written in MF Cobol 4.0.32 that is using
>InstallShield 5.1 Professional for the installation package.  I've
…[15 more quoted lines elided]…
>Doug
```

#### ↳ Re: MF Cobol and Longfilenames

- **From:** "Bill Wood" <beavis27@email.msn.com>
- **Date:** 1998-11-13T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<eiI2ug0D#GA.78@upnetnews05>`
- **References:** `<3639d008.69617294@news.mci2000.com>`

```
Doug,
     We had a similar problem in that we have our users enter a "temporary"
directory for working files.  If there are no spaces (or as MF likes to say
"the path is not spacey"), it works fine but when we get a space in there it
doesn't like it.  What we did was take the path they enter, put a quote (")
on the front and back and we were able to use the directory without any
problems.  Try that and see if it works.

bill


dblaze@merchants-fla.com wrote in message
<3639d008.69617294@news.mci2000.com>...
>I've got an application written in MF Cobol 4.0.32 that is using
>InstallShield 5.1 Professional for the installation package.  I've
…[15 more quoted lines elided]…
>Doug
```

#### ↳ Re: MF Cobol and Longfilenames

- **From:** "Bill Wood" <beavis27@email.msn.com>
- **Date:** 1998-11-13T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<Odf34h0D#GA.142@upnetnews05>`
- **References:** `<3639d008.69617294@news.mci2000.com>`

```
Doug,
      We had a similar problem in our application and we found that by
putting a double-quote (") on the front and back of the path, we were able
to use it without any problems.  Try that and see if it works.

bill


dblaze@merchants-fla.com wrote in message
<3639d008.69617294@news.mci2000.com>...
>I've got an application written in MF Cobol 4.0.32 that is using
>InstallShield 5.1 Professional for the installation package.  I've
…[4 more quoted lines elided]…
>Doug
```

#### ↳ Re: MF Cobol and Longfilenames

- **From:** "Bill Wood" <beavis27@email.msn.com>
- **Date:** 1998-11-13T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<#hGF1n0D#GA.262@upnetnews05>`
- **References:** `<3639d008.69617294@news.mci2000.com>`

```
Doug,
      We had a similar problem in our application and we found that by
putting a double-quote (") on the front and back of the path, we were able
to use it without any problems.  Try that and see if it works.

bill


dblaze@merchants-fla.com wrote in message
<3639d008.69617294@news.mci2000.com>...
>I've got an application written in MF Cobol 4.0.32 that is using
>InstallShield 5.1 Professional for the installation package.  I've
…[4 more quoted lines elided]…
>Doug
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
