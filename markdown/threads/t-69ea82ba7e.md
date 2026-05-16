[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# REWRITE query

_11 messages · 6 participants · 2004-01_

**Topics:** [`Migration and conversion`](../topics.md#migration)

---

### REWRITE query

- **From:** ritchie_s01@yahoo.com (ritchie)
- **Date:** 2004-01-20T10:07:03-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3bee6ba6.0401201007.4dd29014@posting.google.com>`

```
Hi,

I am trying to amend a record already on file using rewrite.
This para first gets the account number to be amended, from the user.
Then reads 'file1' to see if this account exists.  Then, if it does,
it reads 'file2'
for the first transaction corresponding to this account number, and
displays the amount.
I then try to do a rewrite of the amount but get a file status 23 even
though this
record is on file2.

This file status of '23' (record not found) is after the rewrite.
When I read the file before-hand it displays the correct amount for
that specific
account, as it should, but then I try to rewrite with the new amount
and have this problem.
I have checked the file keys and they 'seem' to have the correct
values.

This is the same file setup I use for adding to both 'file1' and
'file2' and I have no
problems there.

I'm not sure what's going wrong here.
Could the keys be defined incorrectly?  I suspect that this could be
the case.

Any help would be much aprechiated.

Thanks in advance,
Ritchie

P.S (using Fujitsu v3 compiler)
PLEASE forgive the formatting.

************* START CODE
**********************************************
FILE-CONTROL.
	select file1 assign "file1.dat"
		ORGANIZATION IS Indexed
	        ACCESS MODE IS DYNAMIC
		RECORD KEY IS Account-no
		ALTERNATE RECORD KEY IS Account-name 
		WITH DUPLICATES
		FILE STATUS IS file1-status.
	select Transactions ASSIGN TO "file2.dat"
		ORGANIZATION IS Indexed
		ACCESS MODE IS DYNAMIC
		RECORD KEY IS Transaction-no
		ALTERNATE RECORD KEY IS Transaction-date
		WITH DUPLICATES
		FILE STATUS IS file2-status.
	...		
FD Accounts.
01 file1.
	03 Account-no 		PIC X(14).
	03 Account-lname 	PIC A(30).
	....                                         
FD Transactions.
01 file2.
	03 Transaction-no.
		05 Transaction-ac 	PIC X(14).
		...
		05 trans-amt 	PIC 9(5)v99.	
	...
AMEND-TRANS
***get account num from user
	display "Enter account no > "
	accept account-no-in
***move value to file1 key
	move account-no-in to file1-key
		read file1  
			invalid key 
				..
			not invalid key
				if file-status-ok
					display "Account found"
 	        		end-if
***move file1 key to file2 key for read of file2
		 move file1-key to file2-key
		
		 set not-eof-file2 to true
***start file2 at position of the account number found from file1 read
(ok up to here)
		 start file2 KEY >= account-no-in		

		 perform until eof-file2 or file1-key not = Transaction-ac  
			read file2 next record at end set eof-file2 to true				
			not at end
				if file1-key = file2-key
					set not-eof-file2 to true
***display amount fr this account (still ok up to here)
					display "Transaction old amount > " trans-amt
					
		                        display "Enter new amount"
					accept new-amt
					
					move new-amt TO trans-amt
					rewrite file2
					end-rewrite
***ERROR - file status 23 here - but record is on file.
				end-if
			end-read
		 end-perform.
***********************END CODE***************************************
```

#### ↳ Re: REWRITE query

- **From:** "JerryMouse" <nospam@bisusa.com>
- **Date:** 2004-01-20T15:05:09-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<B-mdnYQLA_qZBZDdRVn2vw@giganews.com>`
- **References:** `<3bee6ba6.0401201007.4dd29014@posting.google.com>`

```
ritchie wrote:
> Hi,
>
…[68 more quoted lines elided]…
> ***move value to file1 key




> move account-no-in to file1-key

This line - and others - reference a data item named "file1-key."
What's "file1-key?"



> read file1
> invalid key
…[31 more quoted lines elided]…
> ***********************END CODE***************************************
```

#### ↳ Re: REWRITE query

- **From:** "William M. Klein" <wmklein@nospam.netcom.com>
- **Date:** 2004-01-20T22:17:15+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<LNhPb.20983$zj7.3754@newsread1.news.pas.earthlink.net>`
- **References:** `<3bee6ba6.0401201007.4dd29014@posting.google.com>`

```
Your problem is:

 move account-no-in to file1-key
read file1
invalid key


for a file in DYNAMIC access mode, a "read" with no KEY phrase is a SEQUENTIAL
read, so you are actually just doing a "read next".  You can either use the
START statement to position your read or use the KEY phare on the READ.
```

##### ↳ ↳ Re: REWRITE query

- **From:** riplin@Azonic.co.nz (Richard)
- **Date:** 2004-01-20T21:25:19-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<217e491a.0401202125.6b36abac@posting.google.com>`
- **References:** `<3bee6ba6.0401201007.4dd29014@posting.google.com> <LNhPb.20983$zj7.3754@newsread1.news.pas.earthlink.net>`

```
"William M. Klein" <wmklein@nospam.netcom.com> wrote

>  move account-no-in to file1-key
> read file1
…[3 more quoted lines elided]…
> read, 

I can't believe that you said that, it is just not true.

For DYNAMIC access mode a READ ... NEXT is required for a sequential
read, a 'READ' is a random read.

In any case it is not the problem.
```

###### ↳ ↳ ↳ Re: REWRITE query

- **From:** "William M. Klein" <wmklein@nospam.netcom.com>
- **Date:** 2004-01-21T08:09:47+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<ftqPb.19829$1e.731@newsread2.news.pas.earthlink.net>`
- **References:** `<3bee6ba6.0401201007.4dd29014@posting.google.com> <LNhPb.20983$zj7.3754@newsread1.news.pas.earthlink.net> <217e491a.0401202125.6b36abac@posting.google.com>`

```
Sorry, believe it or not, I actually looked (too quickly) at the manual as I
couldn't remember which was the "default"
```

#### ↳ Re: REWRITE query

- **From:** riplin@Azonic.co.nz (Richard)
- **Date:** 2004-01-20T17:46:12-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<217e491a.0401201746.5c84ec20@posting.google.com>`
- **References:** `<3bee6ba6.0401201007.4dd29014@posting.google.com>`

```
ritchie_s01@yahoo.com (ritchie) wrote 

> 	select Transactions ASSIGN TO "file2.dat"
> 		ORGANIZATION IS Indexed
> 		ACCESS MODE IS DYNAMIC
> 		RECORD KEY IS Transaction-no
        NOTE:-------------------^^^^^^^
> 		ALTERNATE RECORD KEY IS Transaction-date
> 		WITH DUPLICATES
…[4 more quoted lines elided]…
> 	03 Transaction-no.
     NOTE:----^^^^^^^^^
> 		05 Transaction-ac 	PIC X(14).
                ^^
> 		...
> 		05 trans-amt 	PIC 9(5)v99.	
                ^^

The record key includes all the 05 level fields under the specified 03
key group field.  This means that the key INCLUDES the 'trans-amt'.

>      move new-amt TO trans-amt

This has now changed the key of the record, so it now no longer
matches any existing record.

>      rewrite file2

This fails because you are not rewriting the record you just read, but
some other key that does not exist.

You need to make the key of the transaction file just the account
number plus some fixed reference for that specific transaction, such
as invoice number.
```

##### ↳ ↳ Re: REWRITE query

- **From:** ritchie_s01@yahoo.com (ritchie)
- **Date:** 2004-01-22T10:43:26-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3bee6ba6.0401221043.67fbcc3d@posting.google.com>`
- **References:** `<3bee6ba6.0401201007.4dd29014@posting.google.com> <217e491a.0401201746.5c84ec20@posting.google.com>`

```
Hi,

Thanks to all who helped me before, but as usual when one problem is
solved another appears!  I just a query about methods for writing to
files using alternate records.

ie:
file1 - master file with account no's.
file2 - secondary file also with account numbers for transactions for
accounts
from file1.

I want to try to write to file2 by alternate key so there will be no
duplicate records.

Does anyone know the method that should be used?
I tried using a start 
(ie: 
start file2 key is = alternate key
	write ..
	end-write.
)

, the first transaction writes but the second is giving a duplicate
record error.
I know this is because 'transaction-ac-num'(primary key) is being
written to file2 again but I
thought this was ok because the key being used for the write is the
alternate key.

If anybody could just explain the best method to write to a file using
an alternate
key I would be most grateful.

Thanks again,
Ritchie


p.s - my file setup.

********************************
	FILE-CONTROL.
		SELECT file1 ASSIGN TO...
			ORGANIZATION IS Indexed
		        ACCESS MODE IS DYNAMIC
			RECORD KEY IS account-ac-num
			ALTERNATE RECORD KEY IS ...
			WITH DUPLICATES
			FILE STATUS IS account-file-status.
		SELECT file2 ASSIGN TO ...
			ORGANIZATION IS Indexed
			ACCESS MODE IS DYNAMIC
			RECORD KEY IS transaction-ac-num
			ALTERNATE RECORD KEY IS date WITH DUPLICATES
			FILE STATUS IS.........
***********************************

----------------------------------------------------------------------



riplin@Azonic.co.nz (Richard) wrote in message news:<217e491a.0401201746.5c84ec20@posting.google.com>...
> ritchie_s01@yahoo.com (ritchie) wrote 
> 
…[19 more quoted lines elided]…
> The r
ecord key includes all the 05 level fields under the specified 03
> key group field.  This means that the key INCLUDES the 'trans-amt'.
> 
…[12 more quoted lines elided]…
> as invoice number.
```

###### ↳ ↳ ↳ Re: REWRITE query

- **From:** riplin@Azonic.co.nz (Richard)
- **Date:** 2004-01-22T14:33:34-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<217e491a.0401221433.4b2109bc@posting.google.com>`
- **References:** `<3bee6ba6.0401201007.4dd29014@posting.google.com> <217e491a.0401201746.5c84ec20@posting.google.com> <3bee6ba6.0401221043.67fbcc3d@posting.google.com>`

```
ritchie_s01@yahoo.com (ritchie) wrote 

> Thanks to all who helped me before, but as usual when one problem is
> solved another appears!  I just a query about methods for writing to
> files using alternate records.

> I want to try to write to file2 by alternate key so there will be no
> duplicate records.

You can't "write to file2 by alternate key".  You write by _all_ keys
that you have specified as belonging to the file.

> , the first transaction writes but the second is giving a duplicate
> record error.
…[3 more quoted lines elided]…
> alternate key.

You need to construct a _unique_ primary key because duplicate primary
keys are not allowed.

> 		SELECT file2 ASSIGN TO ...
> 			ORGANIZATION IS Indexed
> 			ACCESS MODE IS DYNAMIC
> 			RECORD KEY IS transaction-key
                                  change: ^^^^  vvvv
> 			ALTERNATE RECORD KEY IS transaction-date WITH DUPLICATES
> 			FILE STATUS IS.........

If you have the record defined as:

        FD file2.
        01 transaction-record.
           03  transaction-key.
               05  transaction-acc-no     PIC X(14).
           03  transaction-data.
               05  transaction-date       PIC X(8).
               05  transaction-value      PIC S9(8)V99.
               05  ....

Then there can only be _one_ record with each different
transaction-key.  Having duplicate dates doesn't change this.  eg:

         ACCOUNT-0001     20040121    22.67
         ACCOUNT-0022     20040121    45.78
         ACCOUNT-0123     20040122   346.88

is OK even though there are several records with the same date because
you have allowed this.  BUT YOU CAN ONLY HAVE ONE TRANSACTION PER
UNIQUE PRIMARY KEY which is the transaction-acc-no.

However, if, as I have told you several times before, you add another
field to the primary key:

        01 transaction-record.
           03  transaction-key.
               05  transaction-acc-no     PIC X(14).
               05  transaction-ref        PIC X(6).
           03  transaction-data.
               05  transaction-date       PIC X(8).
               05  transaction-value      PIC S9(8)V99.
               05  ....

You should see that the primary key is now TWO fields, the account
number and a reference, such as invoice number.  Date would be a very
poor value to use as it would limit the file to only having one
transaction per day for each account.

Invoice number, payment number, etc would be unique in the system and
makes a good reference.  The file can now have records:

         <---- primary key -->  <alt key>
         ACCOUNT-0001  000123   20040121    22.67
         ACCOUNT-0001  000127   20040121    44.65
         ACCOUNT-0001  000183   20040122   334.27
         ACCOUNT-0022  000164   20040121    45.78
         ACCOUNT-0022  000184   20040122    12.33
         ACCOUNT-0123  000182   20040122   346.88
        
You should be able to see here that each record has a unique key that
is the combination of account number and reference.  Also the date key
has duplicates but this is ok because you have allowed them.  Some of
the dates are duplicated within a block of records for one account and
some are duplicated with records for other accounts.

You can read all the records for one account by moving the account
number to the transaction-key and spaces (or low-values) to the
reference and doing a START >= transaction-key.  Doing a START =
transaction-key would fail.  Then READ NEXT until EOF or the
transaction-acc-no no longer matches.
```

###### ↳ ↳ ↳ Re: REWRITE query

- **From:** robert@jones0086.freeserve.co.uk (Robert Jones)
- **Date:** 2004-01-22T17:25:09-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<fcd09c56.0401221725.3821d659@posting.google.com>`
- **References:** `<3bee6ba6.0401201007.4dd29014@posting.google.com> <217e491a.0401201746.5c84ec20@posting.google.com> <3bee6ba6.0401221043.67fbcc3d@posting.google.com>`

```
Bottom posting

ritchie_s01@yahoo.com (ritchie) wrote in message news:<3bee6ba6.0401221043.67fbcc3d@posting.google.com>...
> Hi,
> 
…[56 more quoted lines elided]…
> 
You don't write files using alternate keys to specify the record
sequence.  You just WRITE to file2 as though it didn't have alternate
keys, though of course you must include them in the data being
written.  You also don't need START to specify the position for
writing records, just use unique record keys and the system will work
out where to put them itself.  You only need START for reading files
when you want to start at a particular key position.  You might want
to use START for your input file depending on the requirements of the
problem being solved.

Good luck 

Robert
```

###### ↳ ↳ ↳ Re: REWRITE query

_(reply depth: 4)_

- **From:** ritchie_s01@yahoo.com (ritchie)
- **Date:** 2004-01-23T10:29:23-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3bee6ba6.0401231029.4a9fb470@posting.google.com>`
- **References:** `<3bee6ba6.0401201007.4dd29014@posting.google.com> <217e491a.0401201746.5c84ec20@posting.google.com> <3bee6ba6.0401221043.67fbcc3d@posting.google.com> <fcd09c56.0401221725.3821d659@posting.google.com>`

```
Hi all,

Just wanted to say a final thanks to everyone for all the help with
all my questions.

I have learned an awful lot from the postings to this group on many
different subjects and hope to be able to contribute myself soon.

I now have my previous problem with duplicates... sorted out.  
I have re-defined my file keys as suggested and thoroughly tested it
and everything seems ok now.

Thanks again to all,
Ritchie  


robert@jones0086.freeserve.co.uk (Robert Jones) wrote in message news:<fcd09c56.0401221725.3821d659@posting.google.com>...
> Bottom posting
> 
…[72 more quoted lines elided]…
> Robert
```

###### ↳ ↳ ↳ Re: REWRITE query

_(reply depth: 5)_

- **From:** docdwarf@panix.com
- **Date:** 2004-01-23T14:09:40-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<burrhk$8i4$1@panix1.panix.com>`
- **References:** `<3bee6ba6.0401201007.4dd29014@posting.google.com> <3bee6ba6.0401221043.67fbcc3d@posting.google.com> <fcd09c56.0401221725.3821d659@posting.google.com> <3bee6ba6.0401231029.4a9fb470@posting.google.com>`

```
In article <3bee6ba6.0401231029.4a9fb470@posting.google.com>,
ritchie <ritchie_s01@yahoo.com> wrote:

[snip]

>I have re-defined my file keys as suggested and thoroughly tested it
>and everything seems ok now.

When 'everything seems ok' is, quite often, a Very Good Time to start 
worrying about the soundness of the program.

DD
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
