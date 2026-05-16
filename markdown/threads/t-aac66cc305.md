[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# RMCobol Error invoking unauthorized copy of the runtime

_4 messages · 4 participants · 2003-05_

**Topics:** [`Compilers and vendors`](../topics.md#compilers) · [`Language features and syntax`](../topics.md#syntax)

---

### RMCobol Error invoking unauthorized copy of the runtime

- **From:** pazzoshoe2@aol.com (Glenn Estes)
- **Date:** 2003-05-15T07:54:20-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<c2f0b01a.0305150654.4bfceee2@posting.google.com>`

```
We are running RMCobol 7.50.00 on an RS6000 under AIX 4.3. This
morning when I came in to work, I found all the overnight batch
programs had aborted with this error code. There were no users on the
system. As of five o'clock yeaterday afternoon, everything seemed
fine.

No COBOL program would run. We re-booted the RS6000 and everything
seems to work OK now.

Has anyone else seen this behavior, and if so, is there a fix?

I hate when AIX starts acting like Window$ - "We don't know what's
wrong - try a reboot" :)
```

#### ↳ Re: RMCobol Error invoking unauthorized copy of the runtime

- **From:** Frederico Fonseca <real-email-in-msg-spam@email.com>
- **Date:** 2003-05-15T21:55:33+01:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<0fv7cv4mbsvhg7cl2uq9gmb2tnsjgfoub0@4ax.com>`
- **References:** `<c2f0b01a.0305150654.4bfceee2@posting.google.com>`

```
On 15 May 2003 07:54:20 -0700, pazzoshoe2@aol.com (Glenn Estes) wrote:

>We are running RMCobol 7.50.00 on an RS6000 under AIX 4.3. This
>morning when I came in to work, I found all the overnight batch
…[10 more quoted lines elided]…
>wrong - try a reboot" :)
Well, I have seen it but not with this version, and this was long ago.

A possible solution for this, and only possible of you only have one
process running at the same time, is to "kill" the shared memory
process that holds the license, whenever you find that particular
error.

Look at the shared memory commands and change your shell scripts so
they invoke the runtime in a loop while checking for this particular
error.

You should still contact Liant to see if this is a know problem in
this OS/Runtime setting.

Regards

FF
Frederico Fonseca
ema il: frederico_fonseca at syssoft-int.com
```

#### ↳ Re: RMCobol Error invoking unauthorized copy of the runtime

- **From:** greg@ncs.co.nz (Greg M Lee)
- **Date:** 2003-05-15T23:47:23+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<BqWwa.895$3t6.14170@news.xtra.co.nz>`
- **References:** `<c2f0b01a.0305150654.4bfceee2@posting.google.com>`

```
In article <c2f0b01a.0305150654.4bfceee2@posting.google.com>, pazzoshoe2@aol.com (Glenn Estes) wrote:
>We are running RMCobol 7.50.00 on an RS6000 under AIX 4.3. This
>morning when I came in to work, I found all the overnight batch
…[10 more quoted lines elided]…
>wrong - try a reboot" :)

One of our clients has had this problem with the same version running on 
RedHat 8.0.  We solved at the time by rebooting also and they haven't had it 
reappear. Experimentation in-house suggests that the rmdaemon process is very 
sensitive to network problems.  We also have a note that if the problem 
re-occurs to first get all users (if any) out of cobol and to then try and 
kill the rmdaemon process.

Good Luck
-Greg
```

#### ↳ Re: RMCobol Error invoking unauthorized copy of the runtime

- **From:** "ShadowFox" <me@email.com>
- **Date:** 2003-05-16T12:00:02+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<6p4xa.860705$L1.248897@sccrnsc02>`
- **References:** `<c2f0b01a.0305150654.4bfceee2@posting.google.com>`

```
Sometimes  you can get that error if you are trying to run multiple jobs and
you only have a one user liscence. In that case just run the jobs one at a
time.
Bob

"Glenn Estes" <pazzoshoe2@aol.com> wrote in message
news:c2f0b01a.0305150654.4bfceee2@posting.google.com...
> We are running RMCobol 7.50.00 on an RS6000 under AIX 4.3. This
> morning when I came in to work, I found all the overnight batch
…[10 more quoted lines elided]…
> wrong - try a reboot" :)
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
