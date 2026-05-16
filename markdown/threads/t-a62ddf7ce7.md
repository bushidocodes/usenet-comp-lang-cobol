[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Using FUNCTION-ID to create user-defined functions

_2 messages · 1 participant · 2004-12_

---

### Using FUNCTION-ID to create user-defined functions

- **From:** "Chris" <ctaliercio@yahoo.com>
- **Date:** 2004-12-07T13:58:32-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1102456712.216630.183780@c13g2000cwb.googlegroups.com>`

```
Does anyone have a working example of how to create a user-defined
function (using the FUNCTION-ID paragraph) in one program, and then
making that function available in another program?

I've scoured the group and all of the references I can think of for a
good working example, but I cannot seem to find any.

What I'd like to do is have a single library of user-defined functions,
and make those functions available to all other programs on the system.
Thanks in advance!

Chris
```

#### ↳ Re: Using FUNCTION-ID to create user-defined functions

- **From:** "Chris" <ctaliercio@yahoo.com>
- **Date:** 2004-12-09T06:26:23-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1102602383.000047.225260@z14g2000cwz.googlegroups.com>`
- **In-Reply-To:** `<1102456712.216630.183780@c13g2000cwb.googlegroups.com>`
- **References:** `<1102456712.216630.183780@c13g2000cwb.googlegroups.com>`

```
All - thank you all very much for your input. I have found this group
to be invaluable for finding creative - sometimes alternative (thanks
Jimmy) - ways to approach different scenarios I have encountered. With
that in mind, I wanted do my part to contribute and post the solution,
as provided to me by Micro Focus. It is two-fold:

1) As Bill pointed out in this thread, trying to pass/return the same
variable in the function was causing problems. You need to use two
different variables for this.
2) I was using the REPOSITORY directive improperly. Also, when the
REPOSITORY directive is used properly, you can also specify the RDFPATH
as the target for the repository information, otherwise it will default
to the source directory.

The following code samples work under MF Server Exress 4.0 SP1. No
special command line options are needed during the compile, simply use
cob <file>.

<myfunctions.cbl>

$set repository(update on)
identification division.

function-id. mydouble.
environment division.
data division.
linkage section.
01  in-number  pic  9(2).
01  out-number  pic  9(2).

procedure division using in-number returning out-number.

compute out-number = in-number * 2 end-compute
exit function
.

end function mydouble.

<myfunctiontest.cbl>

identification division.
program-id. myfunctiontest.

environment division.
configuration section.
repository.
function mydouble
.

data division.
working-storage section.
01  num-1     pic  9(2).
01  num-2     pic  9(2).

procedure division.

move 5 to num-1
compute num-2 = mydouble(num-1) end-compute
exhibit named num-2
         goback returning 0
         .
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
