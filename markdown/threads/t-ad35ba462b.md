[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Creating Excel files in Mainframes

_29 messages · 18 participants · 2001-10_

**Topics:** [`Mainframe, z/OS, JCL, CICS`](../topics.md#mainframe)

---

### Creating Excel files in Mainframes

- **From:** bvasanth123@rediffmail.com (Vasanth)
- **Date:** 2001-10-10T11:31:58-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<4aca0d77.0110101031.1eabfb1b@posting.google.com>`

```
Hi
Are there tools/applications available to generate MS-Excel files in
Mainframes so that excel files cane be downloaded from mainframes and
viewed in MS-Excel?

Ay help is appreciated..

Thanks
```

#### ↳ Re: Creating Excel files in Mainframes

- **From:** "Tim Scrivens" <tim.scrivens@nz.eds.com>
- **Date:** 2001-10-11T08:11:42+13:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<9q26hg$h5b$1@hermes.nz.eds.com>`
- **References:** `<4aca0d77.0110101031.1eabfb1b@posting.google.com>`

```

"Vasanth" <bvasanth123@rediffmail.com> wrote in message
news:4aca0d77.0110101031.1eabfb1b@posting.google.com...
> Hi
> Are there tools/applications available to generate MS-Excel files in
…[3 more quoted lines elided]…
> Ay help is appreciated..

Presumably automatically?

If it is a one-off, you are best off to just create a flat file, FTP it
across, and then open the flat file in Excel and play with it - far easier
than mucking around with scripts.
```

#### ↳ Re: Creating Excel files in Mainframes

- **From:** docdwarf@clark.net ( NA)
- **Date:** 2001-10-10T19:16:21+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<981x7.8861$ym4.380290@iad-read.news.verio.net>`
- **References:** `<4aca0d77.0110101031.1eabfb1b@posting.google.com>`

```
In article <4aca0d77.0110101031.1eabfb1b@posting.google.com>,
Vasanth <bvasanth123@rediffmail.com> wrote:
>Hi
>Are there tools/applications available to generate MS-Excel files in
>Mainframes so that excel files cane be downloaded from mainframes and
>viewed in MS-Excel?

Yes.  These tools are called 'programmers' and most can create a CSV file
for download.

DD
```

#### ↳ Re: Creating Excel files in Mainframes

- **From:** JAndersen@screenio.com (John Andersen)
- **Date:** 2001-10-10T19:27:30+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3bc5a094.76012186@192.168.2.2>`
- **References:** `<4aca0d77.0110101031.1eabfb1b@posting.google.com>`

```
On 10 Oct 2001 11:31:58 -0700, bvasanth123@rediffmail.com (Vasanth) wrote:

 >Hi
 >Are there tools/applications available to generate MS-Excel files in
…[5 more quoted lines elided]…
 >Thanks

Just create CSV (Comma Separated Value) files.  Excel
and most any other spread sheep package read them just
fine, and you can create it as a simple
flat file, building each line with a string command.

John Andersen
NORCOM
http://www.SCREENIO.com/
Juneau, Alaska
```

#### ↳ Re: Creating Excel files in Mainframes

- **From:** "Grinder" <grinder@no.spam.maam.com>
- **Date:** 2001-10-10T18:01:03-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<9q2k4s082b@enews3.newsguy.com>`
- **References:** `<4aca0d77.0110101031.1eabfb1b@posting.google.com>`

```
I you're in a COM-enabled environment, Excel itself is a COM
server, and can be driven by through that interface.

"Vasanth" <bvasanth123@rediffmail.com> wrote in message
news:4aca0d77.0110101031.1eabfb1b@posting.google.com...
> Hi
> Are there tools/applications available to generate MS-Excel
files in
> Mainframes so that excel files cane be downloaded from
mainframes and
> viewed in MS-Excel?
>
> Ay help is appreciated..
>
> Thanks
```

#### ↳ Re: Creating Excel files in Mainframes

- **From:** dashwood@enternet.co.nz (Peter E. C. Dashwood)
- **Date:** 2001-10-10T19:39:02-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<b3638c46.0110101839.5de4257@posting.google.com>`
- **References:** `<4aca0d77.0110101031.1eabfb1b@posting.google.com>`

```
bvasanth123@rediffmail.com (Vasanth) wrote in message news:<4aca0d77.0110101031.1eabfb1b@posting.google.com>...
> Hi
> Are there tools/applications available to generate MS-Excel files in
…[5 more quoted lines elided]…
> Thanks

I don't know of any tools to do this (that doesn't mean there aren't
any...<G>) but if I had to do it, I would simply produce a CSV file on
the mainframe, FTP it to a server (or use whatever the installation
standard tool is for downloading and uploading between the Network and
the mainframe - this should give you the EBCDIC to ASCII conversion
you require), and import it to Excel.

CSV files are "Comma Separated Variable" files. Each field is
separated from the others by a comma (except the last one);
alphanumeric fields should be in quotes, and Numeric fields in
external decimal, with a point if required. Like this:
"pete",123.45,"hello you sexy thing",123

This can be easily written to a standard sequential file on the
mainframe and will be "converted" to a Line Sequential PC file when it
is downloaded to the Network. (Remember to keep the mainframe "record
size" to less than 256 characters; it helps when you convert to PC
file format.)

You can easily write a module to create CSV files in COBOL (hint: use
STRING...) on the mainframe.

Hope this helps,

Pete.
```

##### ↳ ↳ Re: Creating Excel files in Mainframes

- **From:** bvasanth123@rediffmail.com (Vasanth)
- **Date:** 2001-10-11T08:33:22-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<4aca0d77.0110110733.24d9fcab@posting.google.com>`
- **References:** `<4aca0d77.0110101031.1eabfb1b@posting.google.com> <b3638c46.0110101839.5de4257@posting.google.com>`

```
Our current process uses CSV files to generate excel in NT box..This
process is time consuming as we produce thousands of report...

We want to reduce the turnover time by creating excel in Mainframes
instead of downloading CSV/DATA files..


thanks..
```

##### ↳ ↳ Re: Creating Excel files in Mainframes

- **From:** bvasanth123@rediffmail.com (Vasanth)
- **Date:** 2001-10-11T08:36:44-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<4aca0d77.0110110736.24e9b0ed@posting.google.com>`
- **References:** `<4aca0d77.0110101031.1eabfb1b@posting.google.com> <b3638c46.0110101839.5de4257@posting.google.com>`

```
We are already doing this CSV process..As we are producing thousands
of reports, it takes lot of time..
To reduce this this turnover time, We want to create excel files in
mainframes and download excel files instead of csv files

Thanks..

dashwood@enternet.co.nz (Peter E. C. Dashwood) wrote in message news:<b3638c46.0110101839.5de4257@posting.google.com>...
> bvasanth123@rediffmail.com (Vasanth) wrote in message news:<4aca0d77.0110101031.1eabfb1b@posting.google.com>...
> > Hi
…[32 more quoted lines elided]…
> Pete.
```

###### ↳ ↳ ↳ Re: Creating Excel files in Mainframes

- **From:** "Michael Mattias" <michael.mattias@gte.net>
- **Date:** 2001-10-11T18:07:32+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<Cdlx7.394$Pr5.262967@paloalto-snr2.gtei.net>`
- **References:** `<4aca0d77.0110101031.1eabfb1b@posting.google.com> <b3638c46.0110101839.5de4257@posting.google.com> <4aca0d77.0110110736.24e9b0ed@posting.google.com>`

```
Vasanth <bvasanth123@rediffmail.com> wrote in message
news:4aca0d77.0110110736.24e9b0ed@posting.google.com...
> We are already doing this CSV process..As we are producing thousands
> of reports, it takes lot of time..
> To reduce this this turnover time, We want to create excel files in
> mainframes and download excel files instead of csv files
>

A. Have you looked at your application IN GENERAL to see where your time is
going?  That is, is the bottleneck on the mainframe producing the QSAM
files, or in the communications (file transfer), or in the Excel "import"
phase?

B. Instead of all those STRING operations used to create CSV with COBOL/390,
have you tried creating the files in fixed-record-size format and letting
Excel import that?

C. Have you looked at the C-Cubed products? I have not used them, but from
their web page it certainly appears that you should take a look.
www.c-cubed.net


MCM
```

###### ↳ ↳ ↳ Re: Creating Excel files in Mainframes

- **From:** Richard Plinston <riplin@Azonic.co.nz>
- **Date:** 2001-10-12T07:52:52+01:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3BC69343.1B5069B@Azonic.co.nz>`
- **References:** `<4aca0d77.0110101031.1eabfb1b@posting.google.com> <b3638c46.0110101839.5de4257@posting.google.com> <4aca0d77.0110110736.24e9b0ed@posting.google.com>`

```
Vasanth wrote:
> 
> We are already doing this CSV process..As we are producing thousands
> of reports, it takes lot of time..
> To reduce this this turnover time, We want to create excel files in
> mainframes and download excel files instead of csv files

Where does the saving in time come ?

The only point of having an Excel file is so that it can be loaded into
Excel.  A CSV can be loaded into Excel.  Given that at the point of
usage either could be loaded what saves the time ?
```

###### ↳ ↳ ↳ Re: Creating Excel files in Mainframes

_(reply depth: 4)_

- **From:** JAndersen@screenio.com (John Andersen)
- **Date:** 2001-10-11T21:28:17+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3bc80e87.169709282@192.168.2.2>`
- **References:** `<4aca0d77.0110101031.1eabfb1b@posting.google.com> <b3638c46.0110101839.5de4257@posting.google.com> <4aca0d77.0110110736.24e9b0ed@posting.google.com> <3BC69343.1B5069B@Azonic.co.nz>`

```
On Fri, 12 Oct 2001 07:52:52 +0100, Richard Plinston <riplin@Azonic.co.nz> wrote:

 >Vasanth wrote:
 >> 
…[9 more quoted lines elided]…
 >usage either could be loaded what saves the time ?

Yes, I agree, Excel loads a csv just as fast as an Excel
file, if not faster (because its a much simpler file).

I see no possibility of saving time.
John Andersen
NORCOM
http://www.SCREENIO.com/
Juneau, Alaska
```

###### ↳ ↳ ↳ Re: Creating Excel files in Mainframes

_(reply depth: 4)_

- **From:** SkippyPB <swiegand@nospam.neo.rr.com>
- **Date:** 2001-10-12T12:17:26-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<D2C4B0504C765DA5.1CA10E6B4BAA953D.EC118B50FBBCF717@lp.airnews.net>`
- **References:** `<4aca0d77.0110101031.1eabfb1b@posting.google.com> <b3638c46.0110101839.5de4257@posting.google.com> <4aca0d77.0110110736.24e9b0ed@posting.google.com> <3BC69343.1B5069B@Azonic.co.nz>`

```
On Fri, 12 Oct 2001 07:52:52 +0100, Richard Plinston
<riplin@Azonic.co.nz> enlightened us:

>Vasanth wrote:
>> 
…[9 more quoted lines elided]…
>usage either could be loaded what saves the time ?

This looks to be a case of treating the symptoms of a problem rather
than the problem itself.  A more thorough analysis may be warranted
looking at why things are taking too long.

Regards,

          ////
         (o o)
-oOO--(_)--OOo-

When I was born, I was so surprised I couldn't 
talk for a year and a half.

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Remove nospam to email me.

Steve
```

###### ↳ ↳ ↳ Re: Creating Excel files in Mainframes

_(reply depth: 5)_

- **From:** "Dan Bartoli" <dbartoli@adelphia.net>
- **Date:** 2001-10-15T02:16:57+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<tGry7.2812$uO2.501360@news2.news.adelphia.net>`
- **References:** `<4aca0d77.0110101031.1eabfb1b@posting.google.com> <b3638c46.0110101839.5de4257@posting.google.com> <4aca0d77.0110110736.24e9b0ed@posting.google.com> <3BC69343.1B5069B@Azonic.co.nz> <D2C4B0504C765DA5.1CA10E6B4BAA953D.EC118B50FBBCF717@lp.airnews.net>`

```
I have a similar problem.  The time involved with using csv files comes when
the user has to adjust column widths, formatting, etc.

If anyone can come up with the formatting for an xls file format, it would
be most helpful.

DB
```

###### ↳ ↳ ↳ Re: Creating Excel files in Mainframes

_(reply depth: 6)_

- **From:** "Grinder" <grinder@no.spam.maam.com>
- **Date:** 2001-10-14T23:03:49-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<9qdne801rkk@enews3.newsguy.com>`
- **References:** `<4aca0d77.0110101031.1eabfb1b@posting.google.com> <b3638c46.0110101839.5de4257@posting.google.com> <4aca0d77.0110110736.24e9b0ed@posting.google.com> <3BC69343.1B5069B@Azonic.co.nz> <D2C4B0504C765DA5.1CA10E6B4BAA953D.EC118B50FBBCF717@lp.airnews.net> <tGry7.2812$uO2.501360@news2.news.adelphia.net>`

```
"Dan Bartoli" <dbartoli@adelphia.net> wrote:

> I have a similar problem.  The time involved with using csv
files comes when
> the user has to adjust column widths, formatting, etc.

Data type coercion can also trash incoming data--it's a luxury
to be able to send typing information with your dataset.
Unfortunately, CSV doesn't really have this, except though
implication, and CSV parsers have grown interpretive because of
it.

> If anyone can come up with the formatting for an xls file
format, it would
> be most helpful.

A reasonable approach would be to go after WKS output.  It's
less complicated and better documented than XLS files.  (I'm not
sure if it's proprietary as well?)  At any rate, it looks as if
it has enough in its spec to do data formats and basic
formatting--formulas as well.

Here's a link to XLS and WKS specifications:
http://www.wotsit.org/search.asp?page=2&s=database
```

###### ↳ ↳ ↳ Re: Creating Excel files in Mainframes

_(reply depth: 6)_

- **From:** "Peter E. C. Dashwood" <dashwood@nospam.enternet.co.nz>
- **Date:** 2001-10-15T17:13:58+13:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3bca6303_6@news.newsgroups.com>`
- **References:** `<4aca0d77.0110101031.1eabfb1b@posting.google.com> <b3638c46.0110101839.5de4257@posting.google.com> <4aca0d77.0110110736.24e9b0ed@posting.google.com> <3BC69343.1B5069B@Azonic.co.nz> <D2C4B0504C765DA5.1CA10E6B4BAA953D.EC118B50FBBCF717@lp.airnews.net> <tGry7.2812$uO2.501360@news2.news.adelphia.net>`

```
Be careful what you wish for, Dan, you might get it <G>

Even if you had the XLS internal format, you would then be locked in to
using Excel in the current Version, for ever.

It is extremely likely that MS will change the format with new releases...

They certainly won't publish the internal formats in a timely way. Think
about it...

Pete.
"Dan Bartoli" <dbartoli@adelphia.net> wrote in message
news:tGry7.2812$uO2.501360@news2.news.adelphia.net...
> I have a similar problem.  The time involved with using csv files comes
when
> the user has to adjust column widths, formatting, etc.
>
…[5 more quoted lines elided]…
>



-----=  Posted via Newsfeeds.Com, Uncensored Usenet News  =-----
http://www.newsfeeds.com - The #1 Newsgroup Service in the World!
 Check out our new Unlimited Server. No Download or Time Limits!
-----==  Over 80,000 Newsgroups - 19 Different Servers!  ==-----
```

###### ↳ ↳ ↳ Re: Creating Excel files in Mainframes

_(reply depth: 7)_

- **From:** PhilOnline@pgrahams.com
- **Date:** 2001-10-15T16:36:23+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3bcb1028.70372650@news.cadiz1.ky.home.com>`
- **References:** `<4aca0d77.0110101031.1eabfb1b@posting.google.com> <b3638c46.0110101839.5de4257@posting.google.com> <4aca0d77.0110110736.24e9b0ed@posting.google.com> <3BC69343.1B5069B@Azonic.co.nz> <D2C4B0504C765DA5.1CA10E6B4BAA953D.EC118B50FBBCF717@lp.airnews.net> <tGry7.2812$uO2.501360@news2.news.adelphia.net> <3bca6303_6@news.newsgroups.com>`

```
"Peter E. C. Dashwood" <dashwood@nospam.enternet.co.nz> wrote:

|Even if you had the XLS internal format, you would then be locked in to
|using Excel in the current Version, for ever.

At least for the moment, Excel will read prior version files without
complaint, but, of course, will ask about reformating if you try to
save a changed file.

Phil
```

###### ↳ ↳ ↳ Re: Creating Excel files in Mainframes

_(reply depth: 7)_

- **From:** "Grinder" <grinder@no.spam.maam.com>
- **Date:** 2001-10-15T13:57:15-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<9qfbpg0s9e@enews3.newsguy.com>`
- **References:** `<4aca0d77.0110101031.1eabfb1b@posting.google.com> <b3638c46.0110101839.5de4257@posting.google.com> <4aca0d77.0110110736.24e9b0ed@posting.google.com> <3BC69343.1B5069B@Azonic.co.nz> <D2C4B0504C765DA5.1CA10E6B4BAA953D.EC118B50FBBCF717@lp.airnews.net> <tGry7.2812$uO2.501360@news2.news.adelphia.net> <3bca6303_6@news.newsgroups.com>`

```
The Binary File Format (BIFF,) which is the standard for XLS
files, has been stable since Win 3.11.  But BIFF is really a
meta-format, so the details of what information needs to be
stored in that format, in order to be an Excel spreadsheet, has
perhaps changed.

"Peter E. C. Dashwood" <dashwood@nospam.enternet.co.nz> wrote in
message news:3bca6303_6@news.newsgroups.com...
> Be careful what you wish for, Dan, you might get it <G>
>
> Even if you had the XLS internal format, you would then be
locked in to
> using Excel in the current Version, for ever.
>
> It is extremely likely that MS will change the format with new
releases...
>
> They certainly won't publish the internal formats in a timely
way. Think
> about it...
>
…[3 more quoted lines elided]…
> > I have a similar problem.  The time involved with using csv
files comes
> when
> > the user has to adjust column widths, formatting, etc.
> >
> > If anyone can come up with the formatting for an xls file
format, it would
> > be most helpful.
> >
…[6 more quoted lines elided]…
> -----=  Posted via Newsfeeds.Com, Uncensored Usenet News
=-----
> http://www.newsfeeds.com - The #1 Newsgroup Service in the
World!
>  Check out our new Unlimited Server. No Download or Time
Limits!
> -----==  Over 80,000 Newsgroups - 19 Different Servers!
==-----
```

###### ↳ ↳ ↳ Re: Creating Excel files in Mainframes

_(reply depth: 6)_

- **From:** Ed Guy <ed_guy@paralynx.com>
- **Date:** 2001-10-21T18:50:50-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3BD37B7A.FBC@paralynx.com>`
- **References:** `<4aca0d77.0110101031.1eabfb1b@posting.google.com> <b3638c46.0110101839.5de4257@posting.google.com> <4aca0d77.0110110736.24e9b0ed@posting.google.com> <3BC69343.1B5069B@Azonic.co.nz> <D2C4B0504C765DA5.1CA10E6B4BAA953D.EC118B50FBBCF717@lp.airnews.net> <tGry7.2812$uO2.501360@news2.news.adelphia.net>`

```
Dan Bartoli wrote:
> 
> I have a similar problem.  The time involved with using csv files comes when
…[3 more quoted lines elided]…
> be most helpful.

If that's the problem, write a DBF III file instead.  Its format is well documented and 
just about anything reads it too, including Excel.
```

#### ↳ Re: Creating Excel files in Mainframes

- **From:** "Lucas, Todd" <Todd.Lucas@C-Cubed.net>
- **Date:** 2001-10-11T08:45:34+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<O_cx7.52182$kf1.17003165@news1.rdc1.ne.home.com>`
- **References:** `<4aca0d77.0110101031.1eabfb1b@posting.google.com>`

```
You also might want to take a look at a product from C-Cubed, called MVS
Direct API.  It allows you to transfer and populate the spreadsheet from
within an Excel VBA macro - ie no external process to retrieve the Mainframe
file (FTP, IND$File, NDM, etc.).  It can transfer QSAM flat files, PDS
members, or even VSAM records directly into the spreadsheet.  Check out
www.c-cubed.net if you're interested ...

HTH - TL

"Vasanth" <bvasanth123@rediffmail.com> wrote in message
news:4aca0d77.0110101031.1eabfb1b@posting.google.com...
> Hi
> Are there tools/applications available to generate MS-Excel files in
…[5 more quoted lines elided]…
> Thanks
```

#### ↳ Re: Creating Excel files in Mainframes

- **From:** "Jeff Farkas" <JeffFarkas@noland.com>
- **Date:** 2001-10-11T07:15:24-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<9q3v15$lkpq9$1@ID-101435.news.dfncis.de>`
- **References:** `<4aca0d77.0110101031.1eabfb1b@posting.google.com>`

```
A CSV file would be the best bet but you can create an excel file
directly. Not easy but it can be done.
http://www.myfileformats.com/
Jeff

--------------
"Vasanth" <bvasanth123@rediffmail.com> wrote in message
news:4aca0d77.0110101031.1eabfb1b@posting.google.com...
> Hi
> Are there tools/applications available to generate MS-Excel files in
> Mainframes so that excel files cane be downloaded from mainframes
and
> viewed in MS-Excel?
>
> Ay help is appreciated..
>
> Thanks
```

##### ↳ ↳ Re: Creating Excel files in Mainframes

- **From:** PhilOnline@pgrahams.com
- **Date:** 2001-10-11T17:53:39+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3bc5dbd3.15713179@news.cadiz1.ky.home.com>`
- **References:** `<4aca0d77.0110101031.1eabfb1b@posting.google.com> <9q3v15$lkpq9$1@ID-101435.news.dfncis.de>`

```
"Jeff Farkas" <JeffFarkas@noland.com> wrote:

|A CSV file would be the best bet but you can create an excel file
|directly. Not easy but it can be done.
|http://www.myfileformats.com/

The file would have to be output in ASCII with proper-endian numerics
and downloaded without any conversion.  Conversion of an unformatted
binary file such as .XLS would be (almost) impossible.

I still don't understand the problem with CVS.  I get the impression
the writer thinks that .XLS might be smaller file!  Doubtfull.

Phil
```

###### ↳ ↳ ↳ Re: Creating Excel files in Mainframes

- **From:** "Jeff Farkas" <JeffFarkas@noland.com>
- **Date:** 2001-10-11T14:45:01-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<9q4pc6$lqa5a$1@ID-101435.news.dfncis.de>`
- **References:** `<4aca0d77.0110101031.1eabfb1b@posting.google.com> <9q3v15$lkpq9$1@ID-101435.news.dfncis.de> <3bc5dbd3.15713179@news.cadiz1.ky.home.com>`

```

<PhilOnline@pgrahams.com> wrote in message
news:3bc5dbd3.15713179@news.cadiz1.ky.home.com...
> "Jeff Farkas" <JeffFarkas@noland.com> wrote:
>
…[4 more quoted lines elided]…
> The file would have to be output in ASCII with proper-endian
numerics
> and downloaded without any conversion.  Conversion of an unformatted
> binary file such as .XLS would be (almost) impossible.
…[4 more quoted lines elided]…
> Phil

 Yea, that would be at best very hard. I would think it might..just
might
be a far easier task if you wrote the code to generate the XLS on
the PC side. And I have no idea what the goal is?? Saving time
converting the file from CVS to XLS ?? The size of the XLS would
be larger that the CSV.. *sigh*

Jeff...
```

#### ↳ Re: Creating Excel files in Mainframes

- **From:** Charles <nospam@newsranger.com>
- **Date:** 2001-10-11T19:58:58+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<6Smx7.25032$ev2.34027@www.newsranger.com>`
- **References:** `<4aca0d77.0110101031.1eabfb1b@posting.google.com>`

```
On 10 Oct 2001 11:31:58 -0700, in article
<4aca0d77.0110101031.1eabfb1b@posting.google.com>, Vasanth stated 
>
>Hi
…[6 more quoted lines elided]…
>Thanks

We use an application called Decision Analyzer that makes ,downloadable to the
PC, fully functional Excel OR ".WK3" spreadsheets.  It can also make ".dbf"
database files that can be imported into Access.  It requires some set up and
administration on the Mainframe end, but it is very accessable from the PC with
interactive Screens and Mouse Clicks.  It works with databases on the mainframe
also.  Sometimes we use it to make Comma Delimited Address Files to merge with
Microsoft Word.  Decision Analyzer is made by Decision Technology Inc. (DTI).
In Princeton, NJ, off of route 1.  That is a traffic jam waiting to happen!
They are located in pretty area to visit if you need a business trip; HEE HEE.
They have a website at www.Decision-Technology.com.  I think they can do a Web-X
presentation or send you a demonstration CD.  They actually help us solve
problems when we call them for help; won't get that from Microsoft.

If you can write a program to insert commas inbetween elements in a file,
surrounds text with quotes, and converts packed numbers to decimal, then  you
can make files that can be imported into Excel.  A smart person could probably
write an application to do that, but a windows style application that lets you
highlight fields and files and sort options would be a lot easier.  This
application uses Assembly, Fortran, and I think VB, and EHLLAPI in the Windows
client.

I think EZTREIVE can make files from Databases like Peoplesoft.
```

#### ↳ Re: Creating Excel files in Mainframes

- **From:** Steve Thompson <sthompson_2@neo.rr.com>
- **Date:** 2001-10-12T15:52:00+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3BC710E9.784B2586@neo.rr.com>`
- **References:** `<4aca0d77.0110101031.1eabfb1b@posting.google.com>`

```
Vasanth wrote:
> 
> Hi
…[6 more quoted lines elided]…
> Thanks

Yes you can. Let us look at a few methods.

Get a copy of Linux for S/390 and install it. Now run WINE.
From your PC you can attach to the mainframe and run Excel.
All of this, except for the display on your PC, can be
driven on the mainframe. You can then send files (data)
between the other mainframe operating systems and the Linux
system on the mainframe, and let your code process that
before finally downloading to your PC.

You can write code that runs under OS/390 USS (Unix System
Services). Possibly WINE will run here (not sure of this).
This will allow you to do things w/o having to install
Linux.

You can write code (COBOL, PL/1, etc.) that will do the job
on the mainframe and then download it to your PC. If you
know the Micros**t format for the XL files, you can write
this type of file out. However, you will probably want to
output CSV format, which COBOL is quite capable of doing (I
think this is the type of thing most of the other posters
have been talking about).
```

##### ↳ ↳ Re: Creating Excel files in Mainframes

- **From:** Richard Plinston <riplin@Azonic.co.nz>
- **Date:** 2001-10-13T09:24:09+01:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3BC7FA29.54A8353@Azonic.co.nz>`
- **References:** `<4aca0d77.0110101031.1eabfb1b@posting.google.com> <3BC710E9.784B2586@neo.rr.com>`

```
Steve Thompson wrote:
>
> Yes you can. Let us look at a few methods.
> 
> Get a copy of Linux for S/390 and install it. Now run WINE.

Linux on S/390 is running native IBM instructions set.  WINE is not an
an emulator (hint: W.I.N.an E.) and only runs on Intel 80x86 instruction
set, as does any Windows application.

> From your PC you can attach to the mainframe and run Excel.
> All of this, except for the display on your PC, can be
…[3 more quoted lines elided]…
> before finally downloading to your PC.

Even if this could be done, it doesn't necessarily help in saving time. 
You are expecting someone to sit at the terminal and laod and save and
transfer files using mouse clicks and keyboard.  This is probably all
that is wrong with the original problem.

It seems to me that what 'is taking too long' is having to have someone
sit at a keyboard and do the task.  What (IMHO) is required is to
_eliminate_entirely_ any and all manual intervention.

As the actual task has not been defined adequately nor has the 'too
long' been identified then I doubt that much could be done to provide
useful advice.  It is quite probable that spreadsheets are being
distributed within the company and that someone is sitting down and
loading, changing and saving new versions using data from the mainframe.

It would seem to be having the mainframe write the .XLS might be a
solution, except that it would need to work on an existing framework
.XLS as a template into which the data has to be merged.
```

###### ↳ ↳ ↳ Re: Creating Excel files in Mainframes

- **From:** Steve Thompson <sthompson_2@neo.rr.com>
- **Date:** 2001-10-14T03:39:29+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3BC90838.832346FC@neo.rr.com>`
- **References:** `<4aca0d77.0110101031.1eabfb1b@posting.google.com> <3BC710E9.784B2586@neo.rr.com> <3BC7FA29.54A8353@Azonic.co.nz>`

```
Richard Plinston wrote:
<snip>
> Linux on S/390 is running native IBM instructions set.  WINE is not an
> an emulator (hint: W.I.N.an E.) and only runs on Intel 80x86 instruction
> set, as does any Windows application.
> 
<snip>
If I understand correctly, the port to Linux was done using
a "standard" Linux compiler. This then allows one to use the
G5 or later chipset of the S/390 or z/Architecture by Linux
(IEEE Floating Point wherein 16 Registers are available, not
emulated). I have come to this understanding from some
things learned at IBM classes and www.winehq.com. At this
point, I do not have a mainframe available to me so that I
can attempt to "compile" and execute WINE on an z/series
machine (of any kind). However, the testing that I have done
with Linux on a mainframe suggested that it would be very
fast (compared to my AMD K6-2 350MHz based server).

Also, with the current changes made to the S/390 and
especially to the z/Architecture, UNICODE, ASCII and EBCDIC
are all "natively" supported, along with instructions for
handling the little-endian and big-endian situations.
```

###### ↳ ↳ ↳ Re: Creating Excel files in Mainframes

_(reply depth: 4)_

- **From:** Richard Plinston <riplin@Azonic.co.nz>
- **Date:** 2001-10-15T07:57:45+01:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3BCA88E9.CD6AC2E3@Azonic.co.nz>`
- **References:** `<4aca0d77.0110101031.1eabfb1b@posting.google.com> <3BC710E9.784B2586@neo.rr.com> <3BC7FA29.54A8353@Azonic.co.nz> <3BC90838.832346FC@neo.rr.com>`

```
Steve Thompson wrote:
> 
> Richard Plinston wrote:
…[7 more quoted lines elided]…
> a "standard" Linux compiler. 

The standard Linux compiler, gcc, can emit a wide range of different
machine code sets.  This does not mean that programs can run on
different machines.

> This then allows one to use the
> G5 or later chipset of the S/390 or z/Architecture by Linux
> (IEEE Floating Point wherein 16 Registers are available, not
> emulated). I have come to this understanding from some
> things learned at IBM classes and www.winehq.com. 

Did you learn at winehq that it only claimed compatability with '16 and
32 bit x86' ?

> At this
> point, I do not have a mainframe available to me so that I
> can attempt to "compile" and execute WINE on an z/series
> machine (of any kind). 

It may well be that WINE itself would recompile to other machine codes,
though it probably hasn't been written with this in mind and there may
be issues that require code changes.  But WINE itself is just a series
of DLLs that provide an environment to run Windows programs.  Windows
programs are 80x86 machine code (a handful are also MIPS and Alpha when
these processors were supported).

> However, the testing that I have done
> with Linux on a mainframe suggested that it would be very
> fast (compared to my AMD K6-2 350MHz based server).

You should be able to get a reasonable performance out of a 80x86
machine code interpreter that you would need to write.
```

###### ↳ ↳ ↳ Re: Creating Excel files in Mainframes

_(reply depth: 5)_

- **From:** Steve Thompson <sthompson_2@neo.rr.com>
- **Date:** 2001-10-15T22:40:24+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3BCB6520.32709F15@neo.rr.com>`
- **References:** `<4aca0d77.0110101031.1eabfb1b@posting.google.com> <3BC710E9.784B2586@neo.rr.com> <3BC7FA29.54A8353@Azonic.co.nz> <3BC90838.832346FC@neo.rr.com> <3BCA88E9.CD6AC2E3@Azonic.co.nz>`

```
Richard Plinston wrote:
<snip>
> 
> You should be able to get a reasonable performance out of a 80x86
> machine code interpreter that you would need to write.

I stand corrected. For some reason (fuzzy logic induced by
too much ...) I was thinking back to yet another project
where a certain company was attempting to port "NT" to
S/370-XA level code. Your point about the 80x86 kept failing
to dawn on me until sometime this AM when I suddenly
realized a "small" set of problems. WINE can only emulate
the API, but the other code taken from the Intel arena would
have to be cross-compiled to the S/3x0 instruction set in
order for it to work... No small task. 

Steve Thompson
OSP Consulting
330/335-9907 office
```

#### ↳ Re: Creating Excel files in Mainframes

- **From:** jraben@cascinc.com (Jeff Raben)
- **Date:** 2001-10-15T19:49:03+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3bcb3bd8.13326898@news.bullseyetelecom.net>`
- **References:** `<4aca0d77.0110101031.1eabfb1b@posting.google.com>`

```
if your many spreadsheets are fixed(?) in length you can do what I
did.
1) Build a prototype on the PC with formulae to pick up data.
2) build a CSV file.
3) execute - a little copy and "special" paste and BAM.

If you need more, between excel macros (I'm not very experienced in
that) and Visual Basic you can "merge" the csv and the predefined
sheets into valid output a number of ways.  
I have been very successful in building the equivalent of 1 page
sheets of over 300 variations exported in csv.

Beat a sharp stick but not by much.

Jeff

and stir with a Runcible spoon...
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
