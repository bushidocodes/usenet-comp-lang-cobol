[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# COBOL - DBMS problem

_2 messages · 2 participants · 2000-01_

---

### COBOL - DBMS problem

- **From:** "Turgon" <kuiama@hotmail.com>
- **Date:** 2000-01-24T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<86i07p$ri5$1@news.news-service.com>`

```
I am working on a maintenance project for COBOL sources which are written
for a DBMS-database.
Recently we encountered a strange problem:
Somewhere in the source it says something like:

FETCH CURRENT <record_name>
IF <set> MEMBER
THEN
     FETCH OWNER WITHIN <set>
ELSE
     PERFORM <section>
END-IF

This IF-statement is nested in three other IF-statements. The name of the
set and the section are not important.

The problem is that when the program executes this part of the nested
IF-statement, it always jumps to the ELSE, even when the current record IS a
member of the set. I know this for a fact, because when I use DBQ and fetch
this record and then fetch the owner, I get the right result.
Even when I change the source and remove the IF-statement entirely and just
leave FETCH OWNER WITHIN <set> in, then the program FETCHes the right
record. So I think the problem must be the IF <set> MEMBER-statement.

Can anyone explain this, or better yet, how to solve this. Because I'm at a
loss. Any help will be appreciated.
```

#### ↳ Re: COBOL - DBMS problem

- **From:** Howard Brazee <brazee@NOSPAMwebaccess.net>
- **Date:** 2000-01-24T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<388CC33A.EC116482@NOSPAMwebaccess.net>`
- **References:** `<86i07p$ri5$1@news.news-service.com>`

```
Take a look at your compile listing.  I bet it has a series of IF, ELSE,
and even NEXT SENTENCE clauses.  When I use a pre-compiler with
condition codes, I try to end my DBMS commands with full stop periods. 
Maybe your problem can be solved with a full stop period after your
FETCH CURRENT <record_name> command.

Turgon wrote:
> 
> I am working on a maintenance project for COBOL sources which are written
…[24 more quoted lines elided]…
> loss. Any help will be appreciated.
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
