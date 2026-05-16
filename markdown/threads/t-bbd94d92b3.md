[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# help please - MF netexpress 3.1, ODBC, dbase,Win2K

_5 messages · 5 participants · 2001-12_

**Topics:** [`Databases and SQL`](../topics.md#databases) · [`Help requests and how-to`](../topics.md#help)

---

### help please - MF netexpress 3.1, ODBC, dbase,Win2K

- **From:** "Charlie" <foxgrove@home.com>
- **Date:** 2001-12-24T09:31:59+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<jCCV7.44660$ip4.1143657@news2.calgary.shaw.ca>`

```
I'm trying to use NetExpress 3.1 to read data from DBase III file using
ODBC.  Operating environment is Windows 2000.

The CONNECT seems to work, but I can't seem to get SELECT to work.

Can you help aim me in the right direction?

Charlie Goodman
```

#### ↳ Re: help please - MF netexpress 3.1, ODBC, dbase,Win2K

- **From:** "Peter E. C. Dashwood" <dashwood@nospam.enternet.co.nz>
- **Date:** 2001-12-25T00:35:05+13:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3c2713d9_1@Usenet.com>`
- **References:** `<jCCV7.44660$ip4.1143657@news2.calgary.shaw.ca>`

```
We need more details.

Have you set up the ODBC data source using ODBC32, and pointed it at the
DBase file?

Please post the embedded SQL with the SELECT in it.

Pete.

Charlie <foxgrove@home.com> wrote in message
news:jCCV7.44660$ip4.1143657@news2.calgary.shaw.ca...
> I'm trying to use NetExpress 3.1 to read data from DBase III file using
> ODBC.  Operating environment is Windows 2000.
…[7 more quoted lines elided]…
>



 Posted Via Usenet.com Premium Usenet Newsgroup Services
----------------------------------------------------------
    ** SPEED ** RETENTION ** COMPLETION ** ANONYMITY **
----------------------------------------------------------        
                http://www.usenet.com
```

##### ↳ ↳ Re: help please - MF netexpress 3.1, ODBC, dbase,Win2K

- **From:** "Charlie Goodman" <cgoodman@imi.mb.ca>
- **Date:** 2001-12-24T16:47:55+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<%_IV7.280$8i2.9101@news2.mts.net>`
- **References:** `<jCCV7.44660$ip4.1143657@news2.calgary.shaw.ca> <3c2713d9_1@Usenet.com>`

```
>
> Please post the embedded SQL with the SELECT in it.
>
> Pete.
>

>
> Please post the embedded SQL with the SELECT in it.
>
> Pete.

Peter,

Thanks for your reply to my usenet request.



I am experimenting with a bastardized version of the MF demo program
"base\emo\odbcesql\SELECT.CBL".

           EXEC SQL CONNECT TO "imi" END-EXEC.
seems to work as the field sqlcode is zero


I added a few data items
           EXEC SQL BEGIN DECLARE SECTION END-EXEC.
       01  pcustid             pic x(5).
       01  pcompany            pic x(40).
       01  pcity               pic x(20).
       01  pstate              pic x(20).
       01  ws-ident    pic x(40).
       01  ws-original pic x(40).
       01  ws-title    pic x(40).
       01  ws-find     pic x(40).
       EXEC SQL END DECLARE SECTION END-EXEC.

now my attempt at a select
           move "MUXX105" to ws-find
           EXEC SQL
             SELECT ident, original, title
               INTO :ws-ident, :ws-original, :ws-title
               WHERE ident = :ws-find
           END-EXEC

The DBase III structure:
   Structure for database: C:IMI.dbf
   Number of data records:  211691
   Date of last update   : 10/01/01
   Field  Field Name  Type       Width    Dec
       1  IDENT       Character      7
       2  ORIGINAL    Character     14
       3  ORDERTYPE   Character     20
       4  CLIENT      Numeric        5
       5  ITEM        Numeric        5
       6  DID         Numeric       10
       7  TITLE       Character      5
       8  FIRST       Character     15
       9  INITIALS    Character      5
      10  LAST        Character     30

After the SELECT sqlcode has a value of -0000003010


Best Regards for the season,

Charlie Goodman
Winnipeg Canada
```

###### ↳ ↳ ↳ Re: help please - MF netexpress 3.1, ODBC, dbase,Win2K

- **From:** "James J. Gavan" <jjgavan@shaw.ca>
- **Date:** 2001-12-24T17:44:50+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3C2769E8.8734A0D9@shaw.ca>`
- **References:** `<jCCV7.44660$ip4.1143657@news2.calgary.shaw.ca> <3c2713d9_1@Usenet.com> <%_IV7.280$8i2.9101@news2.mts.net>`

```
Charlie,

No doubt Pete will give you a satisfactory reply. If you are a bit
'vague' about the syntax, take a look at the OpenESQL  Assistant. Looks
a bit daunting at first, but fairly straight forward when you study it.
Most importantly it does your syntax for you depending upon your
selection criteria.

Joyeux Noel to you in Winterpeg <G>

Jimmy, Calgary AB

Charlie Goodman wrote:

> >
> > Please post the embedded SQL with the SELECT in it.
…[60 more quoted lines elided]…
> Winnipeg Canada
```

###### ↳ ↳ ↳ Re: help please - MF netexpress 3.1, ODBC, dbase,Win2K

- **From:** lsunley@mb.sympatico.ca
- **Date:** 2001-12-24T18:58:46+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<ZpzG4UNLyRNq-pn2-fbJKMpFTxGuo@thishost>`
- **References:** `<jCCV7.44660$ip4.1143657@news2.calgary.shaw.ca> <3c2713d9_1@Usenet.com> <%_IV7.280$8i2.9101@news2.mts.net>`

```
On Mon, 24 Dec 2001 16:47:55 UTC, "Charlie Goodman" 
<cgoodman@imi.mb.ca> wrote:

> >
> > Please post the embedded SQL with the SELECT in it.
…[65 more quoted lines elided]…
> 

Hi Charlie, long time no see

The SELECT INTO can only select a single row from the table. Are you 
sure that there is only one that matches the select criteria?

Lorne Sunley (from the old Compushare/Cybershare days)

Contact me via e-mail if you need help with this, I've done a bunch of
Netexpress ESQL stuff lately.
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
