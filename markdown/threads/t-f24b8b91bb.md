[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Micro Focus file errors

_7 messages · 5 participants · 1999-08_

**Topics:** [`Compilers and vendors`](../topics.md#compilers)

---

### Micro Focus file errors

- **From:** craigdiaz@my-deja.com
- **Date:** 1999-08-18T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7peh0b$om$1@nnrp1.deja.com>`

```
I've been getting 9/018 file errors using the REBUILD utility on the
indexes for some Micro Focus COBOL v3.00A ISAM files. REBUILD
reorganization issues different counts/info/diagnostic errors for the
same file. Some of these files are 150Mb+ (dat & idx) which seems large
for a system developed 10 yrs ago - maybe it's ok? Despite REBUILD not
being able to fix the files, they are still currently used as I-O
without any apparent errors. Has anyone else found this problem? What
are the chances of being able to restore these files to a 'good'
condition? Is there a utility other than REBUILD.EXE? What are the
dangers of continuing to use the files as-is? Is there still tech
support somewhere, or is this version just too old to be supported
anymore? Thanks for any feedback.


Sent via Deja.com http://www.deja.com/
Share what you know. Learn what you don't.
```

#### ↳ Re: Micro Focus file errors

- **From:** "James J. Gavan" <jjgavan@home.com>
- **Date:** 1999-08-18T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<37BAEAB3.ECC5E333@home.com>`
- **References:** `<7peh0b$om$1@nnrp1.deja.com>`

```
craigdiaz@my-deja.com wrote:
> 
> I've been getting 9/018 file errors using the REBUILD utility on the
…[11 more quoted lines elided]…
> 
Given the volumes you are talking about, not a very attractive
suggestion - but as a LAST RESORT - output an ascii-delimited or
sequential, and re-create the file from the ascii/sequential, displaying
keys to help identify any errors.

Something is obviously amiss if you are getting 9/018 - and I wouldn't
feel safe living with it - even if the file does appear to work.

Jimmy, Calgary AB
```

#### ↳ Re: Micro Focus file errors

- **From:** melifra@satlink.com (Melifra)
- **Date:** 1999-08-18T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7pem03$nsj$1@ul3.satlink.com>`
- **References:** `<7peh0b$om$1@nnrp1.deja.com>`

```
 Usted craigdiaz@my-deja.com escribio :

>I've been getting 9/018 file errors using the REBUILD utility on the
>indexes for some Micro Focus COBOL v3.00A ISAM files. REBUILD
…[9 more quoted lines elided]…
>anymore? Thanks for any feedback.


>Sent via Deja.com http://www.deja.com/
>Share what you know. Learn what you don't.

If, lo had this error[9/018 below nets ,  to execute
the rebuild , besides the sesion of net .  you
makes disappear that error.  you is not being a
problem, the size of the archives.
Regards
Daniel Fernandez


  
E-mail: melifra@satlink.com
Comodoro Rivadavia - Chubut - Patagonia Argentina
             Capital del viento
==================================================
```

#### ↳ Re: Micro Focus file errors

- **From:** redsky@ibm.net (Thane Hubbell)
- **Date:** 1999-08-19T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<37bb7fe0.5689079@news1.ibm.net>`
- **References:** `<7peh0b$om$1@nnrp1.deja.com>`

```
I posted a very detailed message explaining this issue and what you
have done to yourself by rebuilding an index then rebuilding a file.
Search htto://www.deja.com for 9/018 and my e-mail address.   You will
find more horror than you can imagine.


On Wed, 18 Aug 1999 14:46:39 GMT, craigdiaz@my-deja.com wrote:

>I've been getting 9/018 file errors using the REBUILD utility on the
>indexes for some Micro Focus COBOL v3.00A ISAM files. REBUILD
…[13 more quoted lines elided]…
>Share what you know. Learn what you don't.
```

#### ↳ Re: Micro Focus file errors

- **From:** redsky@ibm.net (Thane Hubbell)
- **Date:** 1999-08-19T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<37bb8051.5801683@news1.ibm.net>`
- **References:** `<7peh0b$om$1@nnrp1.deja.com>`

```
If you have NOT already done a Rebuild inputfile and recieved a 9/018
- (restore a backup if you have)

Do this:

Rebuild Inputfile.dat,Outputfile.dat -D

That will correct the 9/018 errors.  Make sure the primary names of
the files are NOT the same.



On Wed, 18 Aug 1999 14:46:39 GMT, craigdiaz@my-deja.com wrote:

>I've been getting 9/018 file errors using the REBUILD utility on the
>indexes for some Micro Focus COBOL v3.00A ISAM files. REBUILD
…[13 more quoted lines elided]…
>Share what you know. Learn what you don't.
```

##### ↳ ↳ Re: Micro Focus file errors

- **From:** craigdiaz@my-deja.com
- **Date:** 1999-08-19T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7pgmbt$jpi$1@nnrp1.deja.com>`
- **References:** `<7peh0b$om$1@nnrp1.deja.com> <37bb8051.5801683@news1.ibm.net>`

```
In article <37bb8051.5801683@news1.ibm.net>,
  redsky@ibm.net (Thane Hubbell) wrote:
> If you have NOT already done a Rebuild inputfile and recieved a 9/018
> - (restore a backup if you have)
…[7 more quoted lines elided]…
>
Thanks, but the version of rebuild I have doesn't support the -D
parameter - that's probably v3.2, I'm using v3.0. Looks like I might be
SOL. On the positive side, though, it looks like they've been corrupted
for years without causing any problems. It's only when rebuild checks
the integrity that it all hits the fan, so I might have no choice but
to leave well enough alone.


Sent via Deja.com http://www.deja.com/
Share what you know. Learn what you don't.
```

###### ↳ ↳ ↳ Re: Micro Focus file errors

- **From:** "Russell Styles" <RWSTYLES@COMPUSERVE.COM>
- **Date:** 1999-08-20T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7pis0m$atg$1@ssauraab-i-1.production.compuserve.com>`
- **References:** `<7peh0b$om$1@nnrp1.deja.com> <37bb8051.5801683@news1.ibm.net> <7pgmbt$jpi$1@nnrp1.deja.com>`

```
> Thanks, but the version of rebuild I have doesn't support the -D
> parameter - that's probably v3.2, I'm using v3.0. Looks like I might be
…[3 more quoted lines elided]…
> to leave well enough alone.


    Since rebuild is a distributable file, you should be legally able to get
a newer version.

    If worse comes to worse, write a program that copies from one file to
another.  It can be programmed to skip problem areas.  If you don't do a lot
of deletes, and do not use compression, the final data file size should be
somewhat close.

    You could also try rebuild old,new  (No spaces around comma).
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
