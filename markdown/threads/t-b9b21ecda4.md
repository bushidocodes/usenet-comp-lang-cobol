[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# DB2 authentication

_3 messages · 2 participants · 2006-09_

**Topics:** [`Databases and SQL`](../topics.md#databases)

---

### DB2 authentication

- **From:** "Frank Swarbrick" <Frank.Swarbrick@efirstbank.com>
- **Date:** 2006-09-21T17:31:05-06:00
- **Newsgroups:** comp.databases.ibm-db2,comp.lang.cobol
- **Message-ID:** `<4ngllpFa2tviU2@individual.net>`

```
Here's a question I posted to the VSE list.  I know there are few if any VSE
users around here, but I thought a z/OS person (or even another OS) might be
able to answer...


Still pondering VSE and DB2.  Don't have DB2 Server for VSE up yet to
actually test anything, but I feel the burning need to have this question
answered sooner rather than later...

According to the SQL Reference (for VSE) both an authorization name (userID)
and a password are always required for a batch job using the CONNECT
statement.  What does this mean in terms of operators submitting batch jobs
that access DB2 databases?  I can't imagine that you would have the operator
type in their user ID and password each time they need to submit a
production batch job.  Do you use your ESM to determine who the user is? 
How do you get the password?

Can operators have database rights only through applications?  In other
words, we wouldn't want to have an operator be able to connect to a database
via the CLP or Control Center and update tables, but they certainly need to
have update capability when submitting batch jobs.  [Actually, I believe I
have found the answer to this, and the answer is yes, by only authorizing
the operators to have rights via bound packages.]

If connecting to a remote DB2/LUW database, how does the DB2/LUW "client"
authentication come in to play.  Is there any type of ID mapping available? 
For instance, right now I have a VSE user ID of 'FJS', but my ID on our
DB2/LUW server is 'fjswarbr'.  Do these names need to be the same, or is
there some way to 'map' them?

Thanks!
Frank


--- 
Frank Swarbrick
Senior Developer/Analyst - Mainframe Applications
FirstBank Data Corporation - Lakewood, CO  USA
```

#### ↳ Re: DB2 authentication

- **From:** "Artur" <artur.wronski@gmail.com>
- **Date:** 2006-09-24T12:30:12-07:00
- **Newsgroups:** comp.databases.ibm-db2,comp.lang.cobol
- **Message-ID:** `<1159126212.598748.143030@m73g2000cwd.googlegroups.com>`
- **References:** `<4ngllpFa2tviU2@individual.net>`

```
Frank,

I know nothing about VSE, but anyway I would like to comment on DB2/LUW
authentication.

When you are connecting to DB2/LUW database you have to specify user
and password, eg. CONNECT TO dbonluw USER dbuser USING password.
Sometimes the user is different from the user that runs application, so
in your case the dbuser/password should be stored within a batch
script. On z/OS you can configure Communications Database to store
users and passwords when connecting z/OS client to DB2/LUW database (as
described in: "Understanding DB2(R): Learning Visually with
Examples", Appendix E),but I don't know how it differs from DB2 for
VSE.

How DB2/LUW authenticates depends on DB2 instance configuration. With
default configuration it is based on operating system users and
passwords on DB2 server. But also you can write your authentication
plugin (GSS-API), which for example positively authenticate only users
who are connecting from certain application. The same users might not
be authenticated, when connecting from CLP. There is set of articles on
ibm.com/developerworks describing DB2/LUW authentication.
Authentications plugins are used in special cases, so probably not in
your case.

-- Artur Wronski
```

##### ↳ ↳ Re: DB2 authentication

- **From:** "Frank Swarbrick" <Frank.Swarbrick@efirstbank.com>
- **Date:** 2006-09-28T10:57:03-06:00
- **Newsgroups:** comp.databases.ibm-db2,comp.lang.cobol
- **Message-ID:** `<4o2d74Fcjr51U1@individual.net>`
- **References:** `<4ngllpFa2tviU2@individual.net> <1159126212.598748.143030@m73g2000cwd.googlegroups.com>`

```
Hi Artur,

I don't see that VSE has anything similar to the z/OS CDB, but I think I can
at least make some use of how it works.

Thanks for the information,
Frank

--- 
Frank Swarbrick
Senior Developer/Analyst - Mainframe Applications
FirstBank Data Corporation - Lakewood, CO  USA

>>> Artur<artur.wronski@gmail.com> 09/24/06 1:30 PM >>>
Frank,

I know nothing about VSE, but anyway I would like to comment on DB2/LUW
authentication.

When you are connecting to DB2/LUW database you have to specify user
and password, eg. CONNECT TO dbonluw USER dbuser USING password.
Sometimes the user is different from the user that runs application, so
in your case the dbuser/password should be stored within a batch
script. On z/OS you can configure Communications Database to store
users and passwords when connecting z/OS client to DB2/LUW database (as
described in: "Understanding DB2(R): Learning Visually with
Examples", Appendix E),but I don't know how it differs from DB2 for
VSE.

How DB2/LUW authenticates depends on DB2 instance configuration. With
default configuration it is based on operating system users and
passwords on DB2 server. But also you can write your authentication
plugin (GSS-API), which for example positively authenticate only users
who are connecting from certain application. The same users might not
be authenticated, when connecting from CLP. There is set of articles on
ibm.com/developerworks describing DB2/LUW authentication.
Authentications plugins are used in special cases, so probably not in
your case.

-- Artur Wronski
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
