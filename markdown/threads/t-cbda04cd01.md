[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# PDS2PDS V3.02

_4 messages · 4 participants · 1999-08_

---

### PDS2PDS V3.02

- **From:** wb4huc@texas.net (Michael A. Newell)
- **Date:** 1999-08-16T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<37b77310.19775483@news.texas.net>`

```
Hello:

Version 3.02 of PDS2PDS, the Partitioned Dataset Comparison/Maintenance Utility,
is now available.

Details at http://wb4huc.home.texas.net/pds2pds

Thank you,
```

#### ↳ Re: PDS2PDS V3.02

- **From:** "Robert M. Pritchett - RMP Consulting Partners LLC" <MSN.Bus.News@rmpcp.com>
- **Date:** 1999-08-21T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<uGw9CYC7#GA.285@cpmsnbbsa05>`
- **References:** `<37b77310.19775483@news.texas.net>`

```
Sounds interesting. Does anyone have an FTP program that can automatically
load/unload a PDS (all or selected members) from/to a group of files on a
PC by setting up corresponding naming conventions? Most FTP programs and
terminal programs I've seen can easily transfer an entire directory between
PC's and/or Unix systems but I haven't seen any that will map these into
PDS member names.


Robert M. Pritchett, President - RMP Consulting Partners LLC
http://rmpcp.com - rmp@rmpcp.com - Dallas, TX - Member ICCA
"Quality means doing it right the first time!"
See http://www.headhunter.net/jobstv/0j/j04651mjxt8trch80j.htm?ShowJob
Contractors: tired of hearing "W-2 only"? Join us and let us help you get
that same contract on a 1099 as a self-employed independent contractor!


Michael A. Newell wrote in message <37b77310.19775483@news.texas.net>...
>Hello:
>
>Version 3.02 of PDS2PDS, the Partitioned Dataset Comparison/Maintenance
Utility,
>is now available.
>
…[8 more quoted lines elided]…
>http://wb4huc.home.texas.net
```

##### ↳ ↳ Re: PDS2PDS V3.02

- **From:** "William M. Klein" <wmklein@nospam.netcom.com>
- **Date:** 1999-08-21T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7pnfi1$o0l@dfw-ixnews3.ix.netcom.com>`
- **References:** `<37b77310.19775483@news.texas.net> <uGw9CYC7#GA.285@cpmsnbbsa05>`

```
I think that there is such a program on the SHARE "CBT" tape.  Try posting
your question in the
      bit.listserv.ibm-main
newsgroup.
```

##### ↳ ↳ Re: PDS2PDS V3.02

- **From:** Ken Foskey <waratah@zip.com.au>
- **Date:** 1999-08-22T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<37BFEC1F.A7F85737@zip.com.au>`
- **References:** `<37b77310.19775483@news.texas.net> <uGw9CYC7#GA.285@cpmsnbbsa05>`

```
"Robert M. Pritchett - RMP Consulting Partners LLC" wrote:
> 
> Sounds interesting. Does anyone have an FTP program that can
…[5 more quoted lines elided]…
> 

I have not got the manual pages handy right now but this is possible
with standard FTP.

Here is the description I lifted from the man files.  I have seen this
work transferring xxx.cob to xxx on MVS.  I have not have the
opportunity (need) to really make this stuff work, most of mine are
simple one off transfers or totally program controlled (I write a
script that is input to FTP as a command file, has work reliably for
about 4 years through 4 changes of FTP client).

Ken

nmap [inpattern outpattern]

Set or unset the filename mapping mechanism.  If no arguments are
specified, the filename mapping mechanism is unset.  If arguments are
specified, remote filenames are mapped during mput commands and put
commands issued without a specified remote target filename.  If
arguments are specified, local filenames are mapped during mget
commands and get commands issued without a specified local target
filename.  This command is useful when connecting to a non-UNIX remote
computer with different file naming conventions or practices.  The
mapping follows the pattern set by inpattern and outpattern.
[Inpattern] is a template for incoming filenames (which may have
already been processed according to the ntrans and case settings). 
Variable templating is accomplished by including the sequences `$1',
`$2', ..., `$9' in inpattern. Use `\' to prevent this special
treatment of the `$' character.  All other characters are treated
literally, and are used to determine the nmap [inpattern] variable
values.  For example,  given inpattern $1.$2 and the remote file name
"mydata.data", $1 would have the value "mydata", and $2 would have the
value "data".  The outpattern determines the resulting mapped
file-name.  The sequences `$1', `$2', ...., `$9' are replaced by any
value resulting from the inpattern template.  The sequence `$0' is
replace by the original filename.  Additionally, the sequence `[seq1,
seq2]' is replaced by [seq1] if seq1 is not a null string; otherwise
it is replaced by seq2. For example, the command

    nmap $1.$2.$3 [$1,$2].[$2,file]

would yield the output filename "myfile.data" for input filenames
"myfile.data" and "myfile.data.old", "myfile.file" for the input
filename "myfile", and "myfile.myfile" for the input filename
".myfile".  Spaces may be included in outpattern, as in the example:
`nmap $1 sed "s/  *$//" > $1'.  Use the `\' character to prevent
special treatment of the `$','[','[', and `,' characters.
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
