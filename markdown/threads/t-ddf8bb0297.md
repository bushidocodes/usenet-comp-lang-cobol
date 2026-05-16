[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Find number of characters read with accept.

_9 messages · 4 participants · 2005-07_

**Topics:** [`Language features and syntax`](../topics.md#syntax)

---

### Find number of characters read with accept.

- **From:** brian.joh@comcast.net
- **Date:** 2005-07-01T16:06:58-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1120259218.841793.237550@o13g2000cwo.googlegroups.com>`

```
I'm a COBOL newbie (just learned it today), but
I'm a pretty experienced programmer.

I wrote a very small COBOL program using
Microfocus Server Express 4 on Suse Linux.  The
program reads an ID and password from a user,
and then calls a C library (Kerberos) to
authenticate them to Active Directory
(authenticate them to a Windows environment).

I've got it working with one major hitch.
ACCEPT always pads strings with spaces, and
(AFAIK) there is basically no way to tell if
the user typed trailing spaces or ACCEPT put
them there.  That is, if the user enters
"ab12  ", I need to know that the user typed
those 2 spaces.  I cannot just strip off the
trailing spaces, because Active Directory
does not strip trailing spaces off passwords.
That is, "ab12  " is a valid SIX character
password in Active Directory.

I can read in the password from C, and I
will if I can't find a way to do this in
COBOL.  But it's much cleaner for us to do
this on the COBOL side. 

Any ideas?  Thanks!!!!
```

#### ↳ Re: Find number of characters read with accept.

- **From:** Russell <rws0203nospam@comcast.net>
- **Date:** 2005-07-01T22:54:23-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<Xns9686F3307C16rws0203comcastnet@216.196.97.131>`
- **References:** `<1120259218.841793.237550@o13g2000cwo.googlegroups.com>`

```
Try the "cursor is" syntax for the accept statement.
Note that the data name referenced in the "cursor is" 
syntax will need to be initialized to the start of the accept.

Your program will need to know where the accept is
supposed to be.







brian.joh@comcast.net wrote in news:1120259218.841793.237550
@o13g2000cwo.googlegroups.com:

> I'm a COBOL newbie (just learned it today), but
> I'm a pretty experienced programmer.
…[27 more quoted lines elided]…
>
```

##### ↳ ↳ Re: Find number of characters read with accept.

- **From:** brian.joh@comcast.net
- **Date:** 2005-07-02T00:48:13-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1120290493.763288.211120@g44g2000cwa.googlegroups.com>`
- **In-Reply-To:** `<Xns9686F3307C16rws0203comcastnet@216.196.97.131>`
- **References:** `<1120259218.841793.237550@o13g2000cwo.googlegroups.com> <Xns9686F3307C16rws0203comcastnet@216.196.97.131>`

```
Unfortunately, I don't have access to Microfocus from home, so I
can't try the "cursor is" right now.  I'm wondering if that will work
with a NO ECHO specified.
```

#### ↳ Re: Find number of characters read with accept.

- **From:** "Ron" <NoSpam@SpamSucks.Org>
- **Date:** 2005-07-01T23:32:40-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<nZudnQLxz5Z3hVvfRVn_vg@giganews.com>`
- **References:** `<1120259218.841793.237550@o13g2000cwo.googlegroups.com>`

```
How are you writing the ACCEPT?
I tried this with MicroFocus workbench and got
acceptable results but I don't if it is what you want.

01  input-area pic x(80) value low-values.
accept input-area at line 1.

When I typed 'ab12  ' I had
'ab12  ' with trailing low-values in input-area.
Exactly what the user typed including trailing spaces
followed by low-values (nulls) in the remainder of the field.

However, when I tried "accept from command-line" that
did indeed convert the trailing low-values to spaces. But
that form is used to pass line command parameters to
a program so that's probably not what you're doing.

Anyway, I'd be interested to hear how you resolve this.
```

##### ↳ ↳ Re: Find number of characters read with accept.

- **From:** brian.joh@comcast.net
- **Date:** 2005-07-02T00:23:15-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1120288994.882416.85200@o13g2000cwo.googlegroups.com>`
- **In-Reply-To:** `<nZudnQLxz5Z3hVvfRVn_vg@giganews.com>`
- **References:** `<1120259218.841793.237550@o13g2000cwo.googlegroups.com> <nZudnQLxz5Z3hVvfRVn_vg@giganews.com>`

```
I tried something similar to that without success.  I initialized the
whole string, before ACCEPTing the input.  I didn't use
LOW-VALUES though.  I'll pop into work tomorrow and try it
with LOW-VALUES (no VPN access) and I'll give the cursor
idea a shot too.

Thanks.
```

##### ↳ ↳ Re: Find number of characters read with accept.

- **From:** brian.joh@comcast.net
- **Date:** 2005-07-02T00:54:08-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1120290848.319650.324770@g14g2000cwa.googlegroups.com>`
- **References:** `<1120259218.841793.237550@o13g2000cwo.googlegroups.com> <nZudnQLxz5Z3hVvfRVn_vg@giganews.com>`

```
This would be kinda painful, but I stumbled across another idea.
Read the data character by character, and keep reading until the
user types the return key.  Apparently, this can be done in
Compaq Cobol by putting the keyboard in auxilary mode and
using an "ACCEPT CONTROL KEY IN":

http://www.helsinki.fi/atk/unix/dec_manuals/cobv27ua/cobum_035.htm

Obviously, I need to do this in Microfocus, but I'm guessing
Microfocus can do something similar.
```

###### ↳ ↳ ↳ Re: Find number of characters read with accept.

- **From:** "Richard" <riplin@Azonic.co.nz>
- **Date:** 2005-07-02T11:59:32-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1120330772.248475.267720@g43g2000cwa.googlegroups.com>`
- **In-Reply-To:** `<1120290848.319650.324770@g14g2000cwa.googlegroups.com>`
- **References:** `<1120259218.841793.237550@o13g2000cwo.googlegroups.com> <nZudnQLxz5Z3hVvfRVn_vg@giganews.com> <1120290848.319650.324770@g14g2000cwa.googlegroups.com>`

```
>  Read the data character by character, and keep reading until the
> user types the return key.

You would also need to cater for the user hitting the backspace key, or
the insert, delete, and arrow keys.

Why not just use the supplied password with all spaces attached and if
it fails the lop off one space at a time and retry until all the spaces
have gone.  Or preferably do the reverse and add a space and retry as
it is unlikely that spaces will be used anyway.
```

###### ↳ ↳ ↳ Re: Find number of characters read with accept.

_(reply depth: 4)_

- **From:** brian.joh@comcast.net
- **Date:** 2005-07-02T15:43:01-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1120344181.049314.211790@g49g2000cwa.googlegroups.com>`
- **In-Reply-To:** `<1120330772.248475.267720@g43g2000cwa.googlegroups.com>`
- **References:** `<1120259218.841793.237550@o13g2000cwo.googlegroups.com> <nZudnQLxz5Z3hVvfRVn_vg@giganews.com> <1120290848.319650.324770@g14g2000cwa.googlegroups.com> <1120330772.248475.267720@g43g2000cwa.googlegroups.com>`

```
At our company, we have an account lockout policy that temporarily
disables
the account after 5 bad login attempts, so we can't just keep retrying.
```

##### ↳ ↳ Re: Find number of characters read with accept.

- **From:** brian.joh@comcast.net
- **Date:** 2005-07-02T16:23:53-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1120346633.597464.232880@o13g2000cwo.googlegroups.com>`
- **In-Reply-To:** `<nZudnQLxz5Z3hVvfRVn_vg@giganews.com>`
- **References:** `<1120259218.841793.237550@o13g2000cwo.googlegroups.com> <nZudnQLxz5Z3hVvfRVn_vg@giganews.com>`

```
Yeah, that worked.  Thanks.  It seems the "AT LINE" disables the
padding.
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
