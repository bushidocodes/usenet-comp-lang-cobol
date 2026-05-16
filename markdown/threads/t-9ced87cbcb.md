[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Help:: IMS - Count of Values in Field using FileAid

_1 message · 0 participants · 2004-10_

**Topics:** [`Mainframe, z/OS, JCL, CICS`](../topics.md#mainframe) · [`Help requests and how-to`](../topics.md#help)

---

### Help:: IMS - Count of Values in Field using FileAid

- **From:** "Karim Jessani" <kalusalu*!spam not*!@hotmail.com>
- **Date:** 2004-10-07T11:09:34-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<41655cb4$1@post.usenet.com>`

```
**** Post for FREE via your newsreader at post.usenet.com ****

Hello all. I have access to FileAid for IMS. I have tried 2 ways to do the
following.
I need to have a count of the amount of a certain value in a field.
ie in a "TYPE CODE" that has Y and N, I need to know the number of Y's and
the number of N's.

I have tried to use the FLEX JCL Option and came up with this:

TYPE RUN;
PSB DBNAME=MYCPCSE;
SELECT SEGMENT=MYCSCSRT MAX=ALL
WHERE CS-CAPP-AGCY=4
COUNT SEGMENT=MYCSCSRT
;

Where I am looking for the count of 4's in this field. Running it, I get the
count of everything in the field. So this is not working:

So I thought to create a "Selection Criteria" through Option 6: Which
created the following for me:

IXPSC MYCPCSE YCNY 06.02.00
DIXPSC ATFD.DEVL.ATFDT8.CNTL FILEAID1
DIXPD1 ATGN.TIMS.DBDLIB MYCPCSE
DIXPD2 NOT USED
DIXPAR NOT USED
DIXPFD ATFD.TIMS.XREFC MYCPCSE
DIXPC1 ATFD.DEVL.COPYLIB
DIXPC2 ATFD.PROD.COPYLIB
1
1
1
3 CS-CAPP-AGCY=4
4MYCSCSRTY S
5 � YDR CS-CAPP-AGCY=4
6CS-CAPP-AGCY X � 14


Using the above when extracting from the database gives me all the values in
this field not just the ones I am interested in.


ANYONE Has any other ideas? Perhaps a FLEX JCL that would allow me to find
out the count of a certain field?

THANKS SO MUCH
Karim



-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
 *** Usenet.com - The #1 Usenet Newsgroup Service on The Planet! ***
                      http://www.usenet.com
Unlimited Download - 19 Seperate Servers - 90,000 groups - Uncensored
-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
