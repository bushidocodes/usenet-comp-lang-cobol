[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# input indicator variables

_15 messages · 5 participants · 2006-10_

---

### input indicator variables

- **From:** "Frank Swarbrick" <Frank.Swarbrick@efirstbank.com>
- **Date:** 2006-10-18T12:34:17-06:00
- **Newsgroups:** comp.databases.ibm-db2,comp.lang.cobol
- **Message-ID:** `<4pnadbFjlr01U1@individual.net>`

```
A few weeks ago I had posed a question about how one my create a cursor for
a query where the predicate condition is dynamic.  Meaning that the query
might want to have one of several possible predicates.  Take the following
queries, for instance:

-- check for branch/account and amount
SELECT BRCH_NBR, ACCT_NBR, POST_DATE, AMOUNT, SERIAL_NBR, SEQUENCE_NBR,
POST_FLAG
  FROM FILM.FILM_TRANSACTIONS
  WHERE BRCH_NBR = 001 AND ACCT_NBR = 1234567 AND AMOUNT = 25.00;

-- check for branch/account and serial number
SELECT BRCH_NBR, ACCT_NBR, POST_DATE, AMOUNT, SERIAL_NBR, SEQUENCE_NBR,
POST_FLAG
  FROM FILM.FILM_TRANSACTIONS
  WHERE BRCH_NBR = 001 AND ACCT_NBR = 1234567 AND SERIAL_NBR = 0;

-- check for branch/account and both amount and serial number
SELECT BRCH_NBR, ACCT_NBR, POST_DATE, AMOUNT, SERIAL_NBR, SEQUENCE_NBR,
POST_FLAG
  FROM FILM.FILM_TRANSACTIONS
  WHERE BRCH_NBR = 001 AND ACCT_NBR = 1234567 AND AMOUNT = 25.00 AND
SERIAL_NBR = 1670;

Using dynamic SQL and building the predicate programatically depending on
the input is one option, but I was really looking at a way to do it using
static SQL.  Why?  Well, because that's what I wanted!  :-)

Anyway, I was reading the DB2 Server for VSE & VM Application Programming
manual (of all things!) and just happened to stumble on the possibility of
using input indicator variables in the predicate.  Here's what the manual
says:
----------------------
...there are cases where setting up a negative input indicator
variable in the predicate can prove useful and efficient. For example, if
an
application prompts the user to interactively supply information that will
identify an employee (by either number or name), you can design the program
to use only one select-statement to extract the indicated employee data from
the
database.
Here is the pseudocode:
    get either empno or lastname from user
    if empno is entered then empnoind = 0, else empnoind = -1
    if lastname is entered then nameind = 0, else nameind = -1
    SELECT * FROM EMPLOYEE
    WHERE EMPNO = :EMPNO:EMPNOIND
    OR LASTNAME = :NAME:NAMEIND
----------------------

This appears to be exactly what I'm looking for.  So I wrote a little
program to test it, and lo and behold it appears to work!  I am posting this
for a few reasons:
1) To see if I appear to be using it correctly (it appears to work, but
perhaps for some other reason?).
2) To see if there are comments on perhaps why I should not use this kind of
coding.  (Too be honest, if I had not read this and I had seen a SELECT like
I have below in my example I would never have figured out what it is
doing.)
3) To let others who don't know about it that this seemingly quite useful
feature is available.
4) To see if anyone has any other comments on my use of imbedded SQL. 
(Ideas to make it better, etc.)
5) To see if this is documented anywhere in the DB2 LUW manuals.  My test
program is actually using DB2 LUW, but DB2 Server for VSE, but I can't find
this feature documented anywhere in the LUW manuals.

Anyway, here is my (COBOL) program:


       program-id. filmqry.

       environment division.
       configuration section.
       special-names.
           console is console.

       data division.
       working-storage section.
       copy "sqlenv.cbl".
       copy "sql.cbl".
       copy "sqlca.cbl".

       exec sql begin declare section end-exec.
       01  film-transactions.
           05  ft-brch-nbr             pic S9(3) comp-3.
           05  ft-acct-nbr             pic S9(7) comp-3.
           05  ft-post-date            pic x(10).
           05  ft-amount               pic S9(9)v99 comp-3.
           05  ft-serial-nbr           pic S9(9) comp-3.
           05  ft-sequence-nbr         pic S9(9) comp-3.
           05  ft-post-flag            pic x.
       01  indicators.
           05  ind                     pic s9(4) comp occurs 10.
       exec sql end declare section end-exec.

       77  errloc          	       pic x(80).
       01  account-in.
           05  brch-in                 pic 9(3).
           05  acct-in                 pic 9(7).
       77  amount-in                   pic x(12).
       77  serial-in                   pic x(9).
       77  record-status               pic x.
           88  record-found                value 'Y'.
           88  record-not-found            value 'N'.
       01  search-flags.
           05  search-amount-flag          pic 9.
               88  search-amount               value 'Y'.
           05  search-serial-flag          pic 9.
               88  search-serial               value 'Y'.

       exec sql declare ft_select cursor for
           select BRCH_NBR, ACCT_NBR, POST_DATE, AMOUNT,
               SERIAL_NBR, SEQUENCE_NBR, POST_FLAG
           from FILM.FILM_TRANSACTIONS
           where BRCH_NBR = :ft-brch-nbr
                 and
                 ACCT_NBR = :ft-acct-nbr
                 and
                 (
                     AMOUNT = :ft-amount:ind(1)
                     or
                     SERIAL_NBR = :ft-serial-nbr:ind(2)
                     or
                     (
                         AMOUNT = :ft-amount:ind(3) 
                         and
                         SERIAL_NBR = :ft-serial-nbr:ind(4)
                     )
                 )
       end-exec.

       procedure division.
           perform connect
           perform get-account
           perform get-input
           perform until amount-in = spaces
                     and serial-in = spaces
               perform mainline
               perform get-input
           end-perform
           perform disconnect
           exit program.

       get-account.
           accept account-in from command-line
           move brch-in to ft-brch-nbr
           move acct-in to ft-acct-nbr
           .

       get-input.
           display 'amount to search' upon console
           accept amount-in from console
           display 'serial to search' upon console
           accept serial-in from console
           .

       mainline.
           perform set-search-fields
           perform start-query
           perform next-record
           if record-found
               display '**results found**'
           else
               display '**no results found**'
           end-if
           perform until record-not-found
               if record-found
                   perform display-record
               end-if
               perform next-record
           end-perform
           perform end-query
           display ' '
           .

       set-search-fields.
           initialize search-flags
           move -1 to ind(1), ind(2), ind(3), ind(4)
          
           if amount-in > spaces
               set search-amount to true
               move function numval(amount-in) to ft-amount
           end-if
           if serial-in > spaces
               set search-serial to true
               move function numval(serial-in) to ft-serial-nbr
           end-if

           move -1 to ind(1), ind(2), ind(3), ind(4)
           evaluate true
           when search-amount and search-serial
               display 'amount and serial'
               move 0 to ind(3), ind(4)
           when search-amount
               display 'amount only'
               move 0 to ind(1)
           when search-serial 
               display 'serial only'
               move 0 to ind(2)
           when other
               display '**unexpected search**'
           end-evaluate
           .

       display-record.
           display ft-brch-nbr ' ' ft-acct-nbr ' '
                   ft-post-date ' ' ft-amount ' '
                   ft-serial-nbr ' ' ft-sequence-nbr ' '
                   ft-post-flag
           .

       connect.
           exec sql connect
               to testdb
               user xyz
               using ********
           end-exec
           call "checkerr" using SQLCA errloc
           .

       start-query.
           display ft-amount ' ' ft-serial-nbr
           display ind(1) ' ' ind(2) ' ' ind(3) ' ' ind(4)
           exec sql open ft_select
           end-exec
           call "checkerr" using SQLCA errloc
           .

       next-record.
           exec sql fetch ft_select
               into :film-transactions
           end-exec
           evaluate sqlcode
           when zero
               set record-found to true
           when 100
               set record-not-found to true
           when other
               call "checkerr" using SQLCA errloc                           

           end-evaluate
           .

       end-query.
           exec sql close ft_select
           end-exec
           call "checkerr" using SQLCA errloc
           .

       disconnect.
           exec sql connect reset
           end-exec
           call "checkerr" using SQLCA errloc                               
   
           .

       end program filmqry.


Frank


--- 
Frank Swarbrick
Senior Developer/Analyst - Mainframe Applications
FirstBank Data Corporation - Lakewood, CO  USA
```

#### ↳ Re: input indicator variables

- **From:** "Richard" <riplin@Azonic.co.nz>
- **Date:** 2006-10-18T12:11:25-07:00
- **Newsgroups:** comp.databases.ibm-db2,comp.lang.cobol
- **Message-ID:** `<1161198685.438672.257260@h48g2000cwc.googlegroups.com>`
- **In-Reply-To:** `<4pnadbFjlr01U1@individual.net>`
- **References:** `<4pnadbFjlr01U1@individual.net>`

```

Frank Swarbrick wrote:

> Here is the pseudocode:
>     get either empno or lastname from user
…[4 more quoted lines elided]…
>     OR LASTNAME = :NAME:NAMEIND

I am not sure that it is doing anything special because those are 'null
indicators', so in effect the setting may be turning the value into
NULL.

     SELECT * FROM EMPLOYEE
      WHERE EMPENO = 'somevalue'
            OR LASTNAME = NULL

Which should work correctly as long as the columns are not allowed to
be NULL.
```

##### ↳ ↳ Re: input indicator variables

- **From:** "Frank Swarbrick" <Frank.Swarbrick@efirstbank.com>
- **Date:** 2006-10-18T14:28:55-06:00
- **Newsgroups:** comp.databases.ibm-db2,comp.lang.cobol
- **Message-ID:** `<4pninoFih028U1@individual.net>`
- **References:** `<4pnadbFjlr01U1@individual.net> <1161198685.438672.257260@h48g2000cwc.googlegroups.com>`

```
Richard<riplin@Azonic.co.nz> 10/18/06 1:11 PM >>>
>
>Frank Swarbrick wrote:
…[18 more quoted lines elided]…
>be NULL.

It appears that a "null indicator" in a predicate is not the same as
checking for NULL.  Instead, that part of the predicate is not checked. 
Here's more from the manual I was reading:
--------------------
Do not use input indicator variables in search conditions (WHERE or HAVING
clauses) to test for null values. The correct way to test for nulls is with
the
NULL predicate (described earlier):
WHERE MGRNO IS NULL  ** correct **
This will return every row where MGRNO is NULL.
WHERE MGRNO = :MGR:MGRIND
If MGRIND has been set negative to make MGR null, the truth value is
�UNKNOWN�, and nothing will be returned.
--------------------

How the first example above appears to work is if EMPNOIND is -1 then the
predicate is interpreted as "WHERE LASTNAME = :NAME".  If NAMEIND is -1 then
it is interpreted as "WHERE EMPNO = :EMPNO".  If neither is -1 then it's
simply "WHERE EMPNO = :EMPNO OR LASTNAME = :NAME".  In no case is either
EMPNO or LASTNAME actually being checked for a NULL value.  If one wishes to
do that (which was not what I was wanting) then you would have to check for
"= NULL".

As a further example, I believe the following is *not* redundant; it does
not have the same meaning as either of the above examples:
SELECT * FROM EMPLOYEE
WHERE EMPNO = :EMPNO:EMPNOIND
      OR EMPNO = NULL
      OR LASTNAME = :NAME:NAMEIND
      OR LASTNAME = NULL

Frank


--- 
Frank Swarbrick
Senior Developer/Analyst - Mainframe Applications
FirstBank Data Corporation - Lakewood, CO  USA
```

###### ↳ ↳ ↳ Re: input indicator variables

- **From:** "Richard" <riplin@Azonic.co.nz>
- **Date:** 2006-10-18T15:39:58-07:00
- **Newsgroups:** comp.databases.ibm-db2,comp.lang.cobol
- **Message-ID:** `<1161211198.384162.318500@b28g2000cwb.googlegroups.com>`
- **In-Reply-To:** `<4pninoFih028U1@individual.net>`
- **References:** `<4pnadbFjlr01U1@individual.net> <1161198685.438672.257260@h48g2000cwc.googlegroups.com> <4pninoFih028U1@individual.net>`

```

Frank Swarbrick wrote:

> How the first example above appears to work is if EMPNOIND is -1 then the
> predicate is interpreted as "WHERE LASTNAME = :NAME".  If NAMEIND is -1 then
…[4 more quoted lines elided]…
> "= NULL".

Perhaps then the meaning of a -1 indicator is 'NOT A VALUE'. Then the
two tests can be done and the one -1ed with never be true because no
value can ever have that.
```

###### ↳ ↳ ↳ Re: input indicator variables

_(reply depth: 4)_

- **From:** "Mark A" <nobody@nowhere.com>
- **Date:** 2006-10-19T00:08:28-06:00
- **Newsgroups:** comp.databases.ibm-db2,comp.lang.cobol
- **Message-ID:** `<ZNadnUwFF5LFi6rYnZ2dnUVZ_uqdnZ2d@comcast.com>`
- **References:** `<4pnadbFjlr01U1@individual.net> <1161198685.438672.257260@h48g2000cwc.googlegroups.com> <4pninoFih028U1@individual.net> <1161211198.384162.318500@b28g2000cwb.googlegroups.com>`

```
"Richard" <riplin@Azonic.co.nz> wrote in message 
news:1161211198.384162.318500@b28g2000cwb.googlegroups.com...
> Perhaps then the meaning of a -1 indicator is 'NOT A VALUE'. Then the
> two tests can be done and the one -1ed with never be true because no
> value can ever have that.
>

Indicator variables have the following meanings:

- A negative number indicates that the column has been set to null.

- The value -2 indicates that the column has been set to null as a result of 
a data conversion error.

- A positive or zero value indicates that the column is not null.

- If a column defined as a CHARACTER data type is truncated on retrieval 
because the host variable is not large enough, the indicator variable 
contains the original length of the truncated column.
```

###### ↳ ↳ ↳ Re: input indicator variables

_(reply depth: 5)_

- **From:** "Richard" <riplin@Azonic.co.nz>
- **Date:** 2006-10-19T10:59:37-07:00
- **Newsgroups:** comp.databases.ibm-db2,comp.lang.cobol
- **Message-ID:** `<1161280777.453803.80000@e3g2000cwe.googlegroups.com>`
- **In-Reply-To:** `<ZNadnUwFF5LFi6rYnZ2dnUVZ_uqdnZ2d@comcast.com>`
- **References:** `<4pnadbFjlr01U1@individual.net> <1161198685.438672.257260@h48g2000cwc.googlegroups.com> <4pninoFih028U1@individual.net> <1161211198.384162.318500@b28g2000cwb.googlegroups.com> <ZNadnUwFF5LFi6rYnZ2dnUVZ_uqdnZ2d@comcast.com>`

```

Mark A wrote:
> "Richard" <riplin@Azonic.co.nz> wrote in message
> news:1161211198.384162.318500@b28g2000cwb.googlegroups.com...
…[6 more quoted lines elided]…
> - A negative number indicates that the column has been set to null.

Yes, the issue was specifically on its use with the equals predicate.
In fact it does not work as an 'is null' because it is defined:

"""The EQUAL predicate will always be evaluated as false when it
compares a null value. The result of this example will select no
rows."""

This means that ' = <nullvalue>' acts as if it were ' =
<impossiblevalue>'.
```

#### ↳ Re: input indicator variables

- **From:** Knut Stolze <stolze@de.ibm.com>
- **Date:** 2006-10-19T08:53:24+02:00
- **Newsgroups:** comp.databases.ibm-db2,comp.lang.cobol
- **Message-ID:** `<eh77d4$f1a$1@lc03.rz.uni-jena.de>`
- **References:** `<4pnadbFjlr01U1@individual.net>`

```
Frank Swarbrick wrote:

> A few weeks ago I had posed a question about how one my create a cursor
> for
…[47 more quoted lines elided]…
> ----------------------

Using the NULL-indicator variables this way will _only_ work if you have an
OR-operator between the predicates.  If it is an AND, then this will
happen, assuming that var1_ind is set to -1, indicating that "var1" itself
shall be treated as being NULL:

WHERE col1 = :var1 :var1_ind AND col2 = :var2 :var2_ind

=> col1 = NULL AND col2 = whatever
=> UNKNOWN AND whatever
=> UNKNOWN
=> FALSE

Summarized: no row will be returned by the query.  Applied to your above
queries, you will not get any results.

What you can do to remedy the situation is to rephrase the query a bit and
not rely on the NULL-indicators.  The idea is simply to provide some more
host-variables as part of the SQL statements, and those host variables
conditionally activate/deactivate a certain predicate.

WHERE ( col1 = :var1 OR :var1_skipped = 1 ) AND
      ( col2 = :var2 OR :var2_skipped = 1 )

var1_skipped and var2_skipped are two regular host variables.  When they are
set to 1, the value of var1 and var2, respectively, don't matter.  For all
other values of the varX_skipped variables, the row will only be returned
if the colX = :varX condition is satisfied.


The nice part is that you have an OR and you can use NULL indicators like
this:

WHERE BRCH_NBR = 001 AND ACCT_NBR = 1234567 AND
      ( AMOUNT = 25.00 OR
        SERIAL_NBR = 0 OR
        ( AMOUNT = 25.00 AND SERIAL_NBR = 1670 ) )

Note however, how the third OR-ed predicate is handled (see above).
```

##### ↳ ↳ Re: input indicator variables

- **From:** "Frank Swarbrick" <Frank.Swarbrick@efirstbank.com>
- **Date:** 2006-10-19T11:01:40-06:00
- **Newsgroups:** comp.databases.ibm-db2,comp.lang.cobol
- **Message-ID:** `<4pppbnFjqtkgU1@individual.net>`
- **References:** `<4pnadbFjlr01U1@individual.net> <eh77d4$f1a$1@lc03.rz.uni-jena.de>`

```
>
>
…[5 more quoted lines elided]…
>> a query where the predicate condition is dynamic.  Meaning that the
query
>> might want to have one of several possible predicates.  Take the
following
>> queries, for instance:
>> 
…[19 more quoted lines elided]…
>> Using dynamic SQL and building the predicate programatically depending
on
>> the input is one option, but I was really looking at a way to do it
using
>> static SQL.  Why?  Well, because that's what I wanted!  :-)
>> 
>> Anyway, I was reading the DB2 Server for VSE & VM Application
Programming
>> manual (of all things!) and just happened to stumble on the possibility
of
>> using input indicator variables in the predicate.  Here's what the
manual
>> says:
>> ----------------------
>> ...there are cases where setting up a negative input indicator
>> variable in the predicate can prove useful and efficient. For example,
if
>> an
>> application prompts the user to interactively supply information that
will
>> identify an employee (by either number or name), you can design the
>> program to use only one select-statement to extract the indicated
employee
>> data from the
>> database.
…[9 more quoted lines elided]…
>Using the NULL-indicator variables this way will _only_ work if you have
an
>OR-operator between the predicates.  If it is an AND, then this will
>happen, assuming that var1_ind is set to -1, indicating that "var1" itself
…[20 more quoted lines elided]…
>var1_skipped and var2_skipped are two regular host variables.  When they
are
>set to 1, the value of var1 and var2, respectively, don't matter.  For all
>other values of the varX_skipped variables, the row will only be returned
>if the colX = :varX condition is satisfied.

This is indeed the way to go.  Thank you very much!  I now have

       exec sql begin declare section end-exec.
       01  search-flags.
           05  amount-flag             pic s9(4) comp.
               88  search-amount               value +1.
               88  skip-amount                 value zero.
           05  serial-flag             pic s9(4) comp.
               88  search-serial               value +1.
               88  skip-serial                 value 0.
       exec sql end declare section end-exec.

       exec sql declare ft_select cursor for
           select BRCH_NBR, ACCT_NBR, POST_DATE, AMOUNT,
               SERIAL_NBR, SEQUENCE_NBR, POST_FLAG
           from FILM.FILM_TRANSACTIONS
           where BRCH_NBR = :ft-brch-nbr
                 and
                 ACCT_NBR = :ft-acct-nbr
                 and
                 (
                    AMOUNT = :ft-amount
                    or
                    :amount-flag = 0
                 )
                 and
                 (
                     SERIAL_NBR = :ft-serial-nbr
                     or
                     :serial-flag = 0
                 )
       end-exec.

And I eliminated the indicator variables.  I get the same results as my
first try, but this is much easier to understand.
(I reversed your 'skip' logic to be, essentially, not-skipped, but it's
still the same idea.)

Question: Does DB2 optimize the query so that if, say, amount-flag is 0 then
it does not even check the AMOUNT column, since that part of the predicate
will always be true no matter what the value of AMOUNT is?  (Same for
SERIAL_NBR, of course).  Would it make any difference if I did the
":amount-flag = 0" comparison first?

Thanks again!

Frank


--- 
Frank Swarbrick
Senior Developer/Analyst - Mainframe Applications
FirstBank Data Corporation - Lakewood, CO  USA
```

###### ↳ ↳ ↳ Re: input indicator variables

- **From:** Knut Stolze <stolze@de.ibm.com>
- **Date:** 2006-10-19T20:41:08+02:00
- **Newsgroups:** comp.databases.ibm-db2,comp.lang.cobol
- **Message-ID:** `<eh8gs4$2og$1@lc03.rz.uni-jena.de>`
- **References:** `<4pnadbFjlr01U1@individual.net> <eh77d4$f1a$1@lc03.rz.uni-jena.de> <4pppbnFjqtkgU1@individual.net>`

```
Frank Swarbrick wrote:

> Question: Does DB2 optimize the query so that if, say, amount-flag is 0
> then it does not even check the AMOUNT column, since that part of the
> predicate
> will always be true no matter what the value of AMOUNT is? (Same for 
> SERIAL_NBR, of course).

Yes, DB2 will do that.  However, you have embedded SQL and that is compiled
and optimized during the "db2 precompile" step and not during runtime.
Thus, the values for the host variables are not known and DB2 has no chance
to eliminate any branches.

> Would it make any difference if I did the 
> ":amount-flag = 0" comparison first?

No, changing the order of predicates doesn't make any semantic difference
(as it does in C/C++, for instance).
```

###### ↳ ↳ ↳ Re: input indicator variables

- **From:** Frederico Fonseca <real-email-in-msg-spam@email.com>
- **Date:** 2006-10-20T08:17:04+01:00
- **Newsgroups:** comp.databases.ibm-db2,comp.lang.cobol
- **Message-ID:** `<d8tgj2teuj6ol4qvtjct3j4ds4aqtj5ens@4ax.com>`
- **References:** `<4pnadbFjlr01U1@individual.net> <eh77d4$f1a$1@lc03.rz.uni-jena.de> <4pppbnFjqtkgU1@individual.net>`

```
On Thu, 19 Oct 2006 11:01:40 -0600, "Frank Swarbrick"
<Frank.Swarbrick@efirstbank.com> wrote:

>>
>>
…[138 more quoted lines elided]…
>Thanks again!
The order of the columns does not really matter. Constants are
evaluated first.

I have been following this interesting thread without any input so
far, but I do need to mention something now that you may not have
looked at so far.

Have you looked at the explain plans for the above SQL's? Use of "OR"
with fields that are part of a index will normally prevent the use of
that index, and that will take away any benefit of using static vs
Dynamic SQL. Obviously this will not be a problem if all the fields
you are using the "or" with are not from an index.

Just in case you dont know, assuming a table where BRCH_NBR is the
first column of a index the following coding will basically tell DB2
NOT to use the index
       (BRCH_NBR = :ft-brch-nbr or 0=1)

Depending on the number of fields you need to do the above construct
with, it may be better to use a CASE construct for each individual
field. More work, but better performance, and still Static.



Frederico Fonseca
ema il: frederico_fonseca at syssoft-int.com
```

###### ↳ ↳ ↳ Re: input indicator variables

_(reply depth: 4)_

- **From:** "Frank Swarbrick" <Frank.Swarbrick@efirstbank.com>
- **Date:** 2006-10-20T18:36:02-06:00
- **Newsgroups:** comp.databases.ibm-db2,comp.lang.cobol
- **Message-ID:** `<4pt8bkFkhgmlU1@individual.net>`
- **References:** `<4pnadbFjlr01U1@individual.net> <eh77d4$f1a$1@lc03.rz.uni-jena.de> <4pppbnFjqtkgU1@individual.net> <d8tgj2teuj6ol4qvtjct3j4ds4aqtj5ens@4ax.com>`

```
>
>
…[5 more quoted lines elided]…
>>Question: Does DB2 optimize the query so that if, say, amount-flag is 0
then
>>it does not even check the AMOUNT column, since that part of the
predicate
>>will always be true no matter what the value of AMOUNT is?  (Same for
>>SERIAL_NBR, of course).  Would it make any difference if I did the
…[18 more quoted lines elided]…
>       (BRCH_NBR = :ft-brch-nbr or 0=1)

I had not done an explain plan, but below is the query followed by the
db2expln output:

       exec sql declare ft_select cursor for
           select BRCH_NBR, ACCT_NBR, POST_DATE, AMOUNT,
               SERIAL_NBR, SEQUENCE_NBR, POST_FLAG
           from FILM.FILM_TRANSACTIONS
           where BRCH_NBR = :ft-brch-nbr
                 and
                 ACCT_NBR = :ft-acct-nbr
                 and
                 (
                     :amount-flag = ' '
                     or
                     AMOUNT = :ft-amount
                 )
                 and
                 (
                     :serial-flag = ' '
                     or
                     SERIAL_NBR = :ft-serial-nbr
                 )
       end-exec.

SQL Statement:
  declare FT_SELECT CURSOR
  FOR
     SElect BRCH_NBR, ACCT_NBR, POST_DATE, AMOUNT, SERIAL_NBR,
             SEQUENCE_NBR, POST_FLAG
     from FILM.FILM_TRANSACTIONS
     where BRCH_NBR =:H00001 and ACCT_NBR =:H00003 and (:H00035 =''or
             AMOUNT =:H00007 )and (:H00037 =''or SERIAL_NBR =:H00009 )



Section Code Page = 1208

Estimated Cost = 25.945667
Estimated Cardinality = 0.017078

Access Table Name = FILM.FILM_TRANSACTIONS  ID = 2,36
|  Index Scan:  Name = FILM.FILM_TRANS_IDX1  ID = 1
|  |  Regular Index (Not Clustered)
…[23 more quoted lines elided]…
|  |  |  #Columns = 7
Return Data Completion

End of section----------------

So unless I'm reading it wrong, it is using the index.

>Depending on the number of fields you need to do the above construct
>with, it may be better to use a CASE construct for each individual
>field. More work, but better performance, and still Static.

Never used a CASE expression before, so it took me several hours, but here's
what I came up with:

       exec sql declare ft_select cursor for
           select BRCH_NBR, ACCT_NBR, POST_DATE, AMOUNT,
               SERIAL_NBR, SEQUENCE_NBR, POST_FLAG
           from FILM.FILM_TRANSACTIONS
           where BRCH_NBR = :ft-brch-nbr
             and ACCT_NBR = :ft-acct-nbr
             and AMOUNT = case
                 when :amount-flag = ' ' then
                   AMOUNT
                 else 
                   :ft-amount
                 end
             and SERIAL_NBR = case
                 when :serial-flag = ' ' then
                   SERIAL_NBR
                 else 
                   :ft-serial-nbr
                 end
       end-exec.

And here's the explain result:

SQL Statement:
  declare FT_SELECT CURSOR
  FOR
     SElect BRCH_NBR, ACCT_NBR, POST_DATE, AMOUNT, SERIAL_NBR,
             SEQUENCE_NBR, POST_FLAG
     from FILM.FILM_TRANSACTIONS
     where BRCH_NBR =:H00001 and ACCT_NBR =:H00003 and AMOUNT =
     case
     when :H00015 =''
     then AMOUNT
     else :H00007 end and SERIAL_NBR =
     case
     when :H00017 =''
     then SERIAL_NBR
     else :H00009 end


Section Code Page = 1208

Estimated Cost = 38.578434
Estimated Cardinality = 1.010237

Access Table Name = FILM.FILM_TRANSACTIONS  ID = 2,36
|  Index Scan:  Name = FILM.FILM_TRANS_IDX1  ID = 1
|  |  Regular Index (Not Clustered)
…[23 more quoted lines elided]…
|  |  |  #Columns = 7
Return Data Completion

End of section
-----------------

Not quite as efficient as the first way.  Perhaps those are not the CASE
expressions you were thinking of?

Anyway, thanks a lot!

Frank


--- 
Frank Swarbrick
Senior Developer/Analyst - Mainframe Applications
FirstBank Data Corporation - Lakewood, CO  USA
```

###### ↳ ↳ ↳ Re: input indicator variables

_(reply depth: 5)_

- **From:** Frederico Fonseca <real-email-in-msg-spam@email.com>
- **Date:** 2006-10-21T11:35:58+01:00
- **Newsgroups:** comp.databases.ibm-db2,comp.lang.cobol
- **Message-ID:** `<c5pjj25mhkal72luiq2elmfg22fi8qat88@4ax.com>`
- **References:** `<4pnadbFjlr01U1@individual.net> <eh77d4$f1a$1@lc03.rz.uni-jena.de> <4pppbnFjqtkgU1@individual.net> <d8tgj2teuj6ol4qvtjct3j4ds4aqtj5ens@4ax.com> <4pt8bkFkhgmlU1@individual.net>`

```
On Fri, 20 Oct 2006 18:36:02 -0600, "Frank Swarbrick"
<Frank.Swarbrick@efirstbank.com> wrote:

>>
>>
…[107 more quoted lines elided]…
>
snip
remaining not really important here.


Ok. You are probably using v8 or v9.

small correction to what I said before. I did not explain as I
intended.
------
Use of "OR" with fields that are part of a index will normally prevent
the use of that field in the index, e.g. will use the index fields
prior to the one containing the "OR"
------

From what I get from the above explain the select is using 2 fields of
the index (#Key Columns = 2), and not the third one as it is being
used with a OR 
(:amount-flag = ' '
or
AMOUNT = :ft-amount)


I am pretty sure that if your SQL is
     where BRCH_NBR =:H00001 and ACCT_NBR =:H00003 
       AND AMOUNT =:H00007 and SERIAL_NBR =:H00009 

you will see (#Key Columns = 4)
and if you remove the serial_nbr from the where
it will be (#Key Columns = 3)



Should you change your sql to be
     where (BRCH_NBR =:H00001 or 0=1) and ACCT_NBR =:H00003 
then I would expect (#Key Columns = 0)

I also noticed that the index is not clustered. Im assuming that you
do have another index which is clustered. If not then it might be
worthwhile changing this index to be clustered and RUNSTATS/RECORG the
table.


As for the case expression meaning was another. I will try it on the
office Monday, and then get back to you.
But the idea is to have a case surrounding the Selects, not within the
where clause.


Frederico Fonseca
ema il: frederico_fonseca at syssoft-int.com
```

###### ↳ ↳ ↳ Re: input indicator variables

_(reply depth: 6)_

- **From:** Frederico Fonseca <real-email-in-msg-spam@email.com>
- **Date:** 2006-10-26T20:03:35+01:00
- **Newsgroups:** comp.databases.ibm-db2,comp.lang.cobol
- **Message-ID:** `<1h12k25t9d7940dd2dldr8dh4rbh3bk53g@4ax.com>`
- **References:** `<4pnadbFjlr01U1@individual.net> <eh77d4$f1a$1@lc03.rz.uni-jena.de> <4pppbnFjqtkgU1@individual.net> <d8tgj2teuj6ol4qvtjct3j4ds4aqtj5ens@4ax.com> <4pt8bkFkhgmlU1@individual.net> <c5pjj25mhkal72luiq2elmfg22fi8qat88@4ax.com>`

```
Frank,

The case type I was speaking about is as follows.
Please create the following SP, and then run the explain on it.
I would like to see the results.
You may need to change the data type of the declared fields to match
the ones on your table.

Also can you tell me how big (record count) is this table?

create procedure ADMINISTRATOR.GET_ACCOUNT(IN query_type char(1))
SPECIFIC GET_ACCOUNT
    DYNAMIC RESULT SETS 1
     LANGUAGE SQL
     READS SQL DATA
   BEGIN
     DECLARE ft_brch_nbr CHAR(3);
     DECLARE ft_acct_nbr CHAR(10);
     DECLARE amount_flag CHAR(1);
     DECLARE ft_amount BIGINT DEFAULT 0;
     DECLARE serial_flag CHAR(1);
     DECLARE ft_serial_nbr BIGINT DEFAULT 0;
case query_type
when '1' then
P1: begin
DECLARE C1 CURSOR WITH RETURN TO CALLER FOR
select BRCH_NBR, ACCT_NBR, POST_DATE, AMOUNT,
       SERIAL_NBR, SEQUENCE_NBR, POST_FLAG
       from FILM_TRANSACTIONS
       where BRCH_NBR = ft_brch_nbr
      and
      ACCT_NBR = ft_acct_nbr
      and
       AMOUNT = ft_amount
;
end p1;
when '2' then
P2: begin
DECLARE C1 CURSOR WITH RETURN TO CALLER FOR
select BRCH_NBR, ACCT_NBR, POST_DATE, AMOUNT,
       SERIAL_NBR, SEQUENCE_NBR, POST_FLAG
       from FILM_TRANSACTIONS
       where BRCH_NBR = ft_brch_nbr
      and
      ACCT_NBR = ft_acct_nbr
      and
       SERIAL_NBR = ft_serial_nbr;
end p2;

end case;
END


Frederico Fonseca
ema il: frederico_fonseca at syssoft-int.com
```

###### ↳ ↳ ↳ Re: input indicator variables

_(reply depth: 7)_

- **From:** "Frank Swarbrick" <Frank.Swarbrick@efirstbank.com>
- **Date:** 2006-10-26T15:00:47-06:00
- **Newsgroups:** comp.databases.ibm-db2,comp.lang.cobol
- **Message-ID:** `<4qcm03Fmi4f4U1@individual.net>`
- **References:** `<4pnadbFjlr01U1@individual.net> <eh77d4$f1a$1@lc03.rz.uni-jena.de> <4pppbnFjqtkgU1@individual.net> <d8tgj2teuj6ol4qvtjct3j4ds4aqtj5ens@4ax.com> <4pt8bkFkhgmlU1@individual.net> <c5pjj25mhkal72luiq2elmfg22fi8qat88@4ax.com> <1h12k25t9d7940dd2dldr8dh4rbh3bk53g@4ax.com>`

```
 Frederico Fonseca<real-email-in-msg-spam@email.com> 10/26/06 1:03 PM >>>
>Frank,
>
…[4 more quoted lines elided]…
>the ones on your table.

Ah, an SP, I see.  So you would have the COBOL program call the stored
procedure?  That's definitely a way to go.  I will take a look at that.  How
do you run explain on an SP?

>Also can you tell me how big (record count) is this table?

Right now its 170,000 records.  But that's only one days worth.  Our actual
production database, which is DL/I, has two years worth of records.

Thanks again,
Frank


--- 
Frank Swarbrick
Senior Developer/Analyst - Mainframe Applications
FirstBank Data Corporation - Lakewood, CO  USA
```

###### ↳ ↳ ↳ Re: input indicator variables

_(reply depth: 8)_

- **From:** Frederico Fonseca <real-email-in-msg-spam@email.com>
- **Date:** 2006-10-26T22:37:53+01:00
- **Newsgroups:** comp.databases.ibm-db2,comp.lang.cobol
- **Message-ID:** `<62a2k2piqven4kkisu2nd2rov2b6hvr6jd@4ax.com>`
- **References:** `<4pnadbFjlr01U1@individual.net> <eh77d4$f1a$1@lc03.rz.uni-jena.de> <4pppbnFjqtkgU1@individual.net> <d8tgj2teuj6ol4qvtjct3j4ds4aqtj5ens@4ax.com> <4pt8bkFkhgmlU1@individual.net> <c5pjj25mhkal72luiq2elmfg22fi8qat88@4ax.com> <1h12k25t9d7940dd2dldr8dh4rbh3bk53g@4ax.com> <4qcm03Fmi4f4U1@individual.net>`

```
On Thu, 26 Oct 2006 15:00:47 -0600, "Frank Swarbrick"
<Frank.Swarbrick@efirstbank.com> wrote:

> Frederico Fonseca<real-email-in-msg-spam@email.com> 10/26/06 1:03 PM >>>
>>Frank,
…[9 more quoted lines elided]…
>do you run explain on an SP?


db2expln -database db_name -schema db_schema -package package_name
-version 'version' -outfile my_file

If you cant do it with a specific package_name and version try
db2expln -database db_name -schema % -package %  -outfile my_file.

It will explain all packages on the database.

Note that results can be different from your test table and the
production table.

This sp was tested in V9. I think it will work on V8 also without any
problems if that is the version you have.
>
>>Also can you tell me how big (record count) is this table?
>
>Right now its 170,000 records.  But that's only one days worth.  Our actual
>production database, which is DL/I, has two years worth of records.
so the production one is big enough.


To call the SP from COBOL you need to do as follows.

WORKING-STORAGE SECTION. 
... 
***************************************************** 
* DECLARE A RESULT SET LOCATOR FOR THE RESULT SET * 
* THAT IS RETURNED. * 
***************************************************** 
01 LOC USAGE SQL TYPE IS RESULT-SET-LOCATOR VARYING. 

  EXEC SQL INCLUDE SQLCA END-EXEC. 
PROCEDURE DIVISION. 
.... 
  EXEC SQL CALL GET_ACCOUNT(:PROCESS) 
  END-EXEC. 

* MAKE THE CALL 
  IF SQLCODE NOT EQUAL TO +466 THEN 
* IF CALL RETURNED BAD SQLCODE 
     MOVE SQLCODE TO BADCODE 
     MOVE SQLERRMC TO ERRMCODE 
     WRITE REPREC FROM ERRMREC 
  ELSE 
     PERFORM GET-PARMS 
     PERFORM GET-RESULT-SET. 

 GET-PARMS. 
* IF THE CALL WORKED, 
    IF OUT-CODE NOT EQUAL TO 0 THEN 
* DID GET_ACCOUNT HIT AN ERROR? 
     MOVE OUT-CODE TO CALLCODE 
     * DO ERROR PROCESSING.
    ELSE 
* EVERYTHING WORKED 

    END-IF.
GET-RESULT-SET. 
***************************************************** 
* ASSUME YOU KNOW THAT ONE RESULT SET IS RETURNED, * 
* AND YOU KNOW THE FORMAT OF THAT RESULT SET. * 
* ALLOCATE A CURSOR FOR THE RESULT SET, AND FETCH * 
* THE CONTENTS OF THE RESULT SET. * 
***************************************************** 
      EXEC SQL ASSOCIATE LOCATORS (:LOC) 
         WITH PROCEDURE GET_ACCOUNT
      END-EXEC. 
* LINK THE RESULT SET TO THE LOCATOR 
      EXEC SQL ALLOCATE C1 CURSOR FOR RESULT SET :LOC 
     END-EXEC. 
* LINK THE CURSOR TO THE RESULT SET 
      PERFORM GET-ROWS VARYING I 
        FROM 1 BY 1 UNTIL SQLCODE EQUAL TO +100. 
GET-ROWS. 
      EXEC SQL FETCH C1 INTO :NAME 
      END-EXEC. 



Note that the cursor MUST not be closed within the SP, but by the
COBOL program that calls the SP as soon as it is not needed.


Frederico Fonseca
ema il: frederico_fonseca at syssoft-int.com
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
