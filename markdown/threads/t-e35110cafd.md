[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# 88-LEVEL / SET xx TO TRUE / SET xx TO "FALSE"

_4 messages · 2 participants · 2003-09_

---

### Re: 88-LEVEL / SET xx TO TRUE / SET xx TO "FALSE"

- **From:** Frank Swarbrick<Frank.Swarbrick@efirstbank.com>
- **Date:** 2003-09-18T17:29:02-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<bkdf5c$g99s$1@ID-184804.news.uni-berlin.de>`
- **References:** `<9e486bb5.0309160140.3f2758a0@posting.google.com> <26pdmvkam9duvd922fsl0md0ohpqldk134@4ax.com> <No2cndjGpIQSVvqiXTWJkw@giganews.com> <3f68057e_6@news.athenanews.com> <iv9ab.1464$Od.111561@twister.tampabay.rr.com> <vmim0dg4hh2hde@corp.supernews.com> <bkcf82$paj$1@peabody.colorado.edu>`

```
One thing I like about C is the enum type.  It's been a while, but I think
you do something like...

enum {checking, savings, loan} my_acct;
...or...
enum {checking = 10, savings = 20, loan = 30 } my_acct;
...or...
typedef enum {checking = 10, savings = 20, loan = 30} acct_types;
acct_types my_acct;
acct_types her_acct;
...here both my_acct and her_acct can have values of checking, savings or
loan...

...then...
my_acct = savings;

...now check which type my_acct is...
switch (my_acct)
{
  case checking: 
     printf("checking account");
     break;
  case savings: 
     printf("savings account");
     break;
  case loan: 
     printf("loan account");
     break;
}

This allows you to set the variable by name but set it to a 'word' value
instead of just a 'meaningless' number.  You can't just say 'set checking to
true' or something like that.  But searching on my_acct can show you
everywhere you are setting my_acct to a particular value.

Anyway...

--- 
Frank Swarbrick
Senior Developer/Analyst - Mainframe Applications
FirstBank Data Corporation - Lakewood, CO  USA

>>> Howard Brazee<howard@brazee.net> 09/18/03 08:25AM >>>

On 18-Sep-2003, LX-i <LXi0007@Netscape.net> wrote:

> I don't understand why people wouldn't like 88-levels.  They make code
> so readable...

Pretty much.   But you do have to check them all to make sure you find where
in
the logic that switch was set.    When we move a value to a switch, the
person
doing maintenance only has to look for instances of the single variable
name.

Still, I use 88's myself.
```

#### ↳ Re: 88-LEVEL / SET xx TO TRUE / SET xx TO "FALSE"

- **From:** "jce" <defaultuser@hotmail.com>
- **Date:** 2003-09-19T03:56:51+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<78vab.8686$Od.314122@twister.tampabay.rr.com>`
- **References:** `<9e486bb5.0309160140.3f2758a0@posting.google.com> <26pdmvkam9duvd922fsl0md0ohpqldk134@4ax.com> <No2cndjGpIQSVvqiXTWJkw@giganews.com> <3f68057e_6@news.athenanews.com> <iv9ab.1464$Od.111561@twister.tampabay.rr.com> <vmim0dg4hh2hde@corp.supernews.com> <bkcf82$paj$1@peabody.colorado.edu> <bkdf5c$g99s$1@ID-184804.news.uni-berlin.de>`

```
"Frank Swarbrick" <Frank.Swarbrick@efirstbank.com> wrote in message
news:bkdf5c$g99s$1@ID-184804.news.uni-berlin.de...
> One thing I like about C is the enum type.  It's been a while, but I think
> you do something like...
> typedef enum {checking = 10, savings = 20, loan = 30} acct_types;
> enum {checking, savings, loan} my_acct;
> enum {checking = 10, savings = 20, loan = 30 } my_acct;

> This allows you to set the variable by name but set it to a 'word' value
> instead of just a 'meaningless' number.  You can't just say 'set checking
to
> true' or something like that.  But searching on my_acct can show you
> everywhere you are setting my_acct to a particular value.
…[6 more quoted lines elided]…
> FirstBank Data Corporation - Lakewood, CO  USA

You have in your enum above set it to a "meaningless number".
You can almost duplicate this as I have below with and without 88 to achieve
exactly the same thing...dealing only with your 'word' value.

The major advantage of the enum is that it is actually a totally new data
type that can be declared as needed...that's where the flexibility comes in.
You know that the variable declared is of a type account - no questions
asked.

You do have to understand, however, that the enumerated types are actually
just unsigned ints so someone could do the following.

int my_acct = 10;
my_acct = my_acct + 10;

or (in C++ which is stricter than C and you want to use the account type and
not int)

acct_types my_acct = checking;
my_acct = acct_types(my_acct + 10)

or cooler yet an operator incrementer ...
inline acct_types &operator++(acct_types input)
{
    return acct_types(my_acct + 10);
}

Might seem hokey but imagine if your type was days_of_week and we wanted to
iterate ...we would opt for something like for (int d = monday; d < sunday;
++d).....
or  for (day_of_week d = monday .....if we had the inline operator
overloaded function).

If you added 10 to 30 however you get "an unspecified results".

So yes, if everyone uses it the same way you do then you are ok - but you
can always be sure someone will do it a way you weren't expecting sooner or
later.



Cobol equivalent:

01 MY-ACCOUNT.
    05 ACCOUNT-TYPE PIC 99.
        88 CHECKING  VALUE 10.
        88 SAVINGS     VALUE 20.
        88 LOAN           VALUE 30.

> my_acct = savings;
SET  CHECKING TO TRUE

> ...now check which type my_acct is...
> switch (my_acct)
…[10 more quoted lines elided]…
> }
EVALUATE TRUE
WHEN CHECKING
  DISPLAY 'CHECKING'
WHEN SAVINGS
  DISPLAY 'SAVINGS'
WHEN LOAN
  DISPLAY 'LOAN'
END-EVALUATE

You could also do this without 88....
01 MY-ACCOUNT  PIC X(10)..
77 CHECKING PIC X(10) VALUE 'CHECKING'.
77 SAVINGS    PIC X(10) VALUE 'SAVINGS'.
77 LOAN          PIC X(10) VALUE 'LOAN'.

MOVE CHECKING TO MY-ACCOUNT

EVALUATE TRUE
WHEN MY-ACCOUNT = CHECKING
  DISPLAY 'CHECKING'
WHEN MY-ACCOUNT = SAVINGS
  DISPLAY 'SAVINGS'
WHEN MY-ACCOUNT = LOAN
  DISPLAY 'LOAN'
END-EVALUATE

JCE
```

##### ↳ ↳ Re: 88-LEVEL / SET xx TO TRUE / SET xx TO "FALSE"

- **From:** Frank Swarbrick<Frank.Swarbrick@efirstbank.com>
- **Date:** 2003-09-22T16:13:08-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<bkns64$3pvcj$1@ID-184804.news.uni-berlin.de>`
- **References:** `<9e486bb5.0309160140.3f2758a0@posting.google.com> <26pdmvkam9duvd922fsl0md0ohpqldk134@4ax.com> <No2cndjGpIQSVvqiXTWJkw@giganews.com> <3f68057e_6@news.athenanews.com> <iv9ab.1464$Od.111561@twister.tampabay.rr.com> <vmim0dg4hh2hde@corp.supernews.com> <bkcf82$paj$1@peabody.colorado.edu> <bkdf5c$g99s$1@ID-184804.news.uni-berlin.de> <78vab.8686$Od.314122@twister.tampabay.rr.com>`

```
jce<defaultuser@hotmail.com> 09/18/03 09:56PM >>>
>"Frank Swarbrick" <Frank.Swarbrick@efirstbank.com> wrote in message
>news:bkdf5c$g99s$1@ID-184804.news.uni-berlin.de... 
>> One thing I like about C is the enum type.  It's been a while, but I
think
>> you do something like...
>> typedef enum {checking = 10, savings = 20, loan = 30} acct_types;
…[4 more quoted lines elided]…
>> instead of just a 'meaningless' number.  You can't just say 'set
checking
>to
>> true' or something like that.  But searching on my_acct can show you
…[5 more quoted lines elided]…
>type that can be declared as needed...that's where the flexibility comes
in.
>You know that the variable declared is of a type account - no questions
>asked.

Exactly.

>You do have to understand, however, that the enumerated types are actually
>just unsigned ints so someone could do the following.
…[4 more quoted lines elided]…
>or (in C++ which is stricter than C and you want to use the account type
and
>not int)
>
…[7 more quoted lines elided]…
>}

Yep.

>Might seem hokey but imagine if your type was days_of_week and we wanted
to
>iterate ...we would opt for something like for (int d = monday; d <
sunday;
>++d).....
>or  for (day_of_week d = monday .....if we had the inline operator
…[5 more quoted lines elided]…
>can always be sure someone will do it a way you weren't expecting sooner
or
>later.
>
…[11 more quoted lines elided]…
>SET  CHECKING TO TRUE

Ah, but here is what I am trying to get it.  Let's say you want to search
your source code for every place that MY-ACCOUNT might be changed.  If you
search just for MY-ACCOUNT you will not find "SET CHECKING TO TRUE".  With
the C example you'd simply search on my_acct.  You'd then find things such
as:
my_acct = savings;
my_acct = checking;
my_acct = loan;
my_acct = 0;  // meaningless perhaps, but...

This was all I was getting at...

>> ...now check which type my_acct is...
>> switch (my_acct)
…[35 more quoted lines elided]…
>END-EVALUATE

I don't much care for this method in general, but on the other hand I do use
it if the situation calls for it.  Your example doesn't match your previous
example, though.
How about:
01 MY-ACCOUNT        PIC 99.
77 CHECKING          VALUE 10.
77 SAVINGS           VALUE 20.
77 LOAN              VALUE 30.

Anyway, no big deal.  It was just something I liked about C.



--- 
Frank Swarbrick
Senior Developer/Analyst - Mainframe Applications
FirstBank Data Corporation - Lakewood, CO  USA
```

###### ↳ ↳ ↳ Re: 88-LEVEL / SET xx TO TRUE / SET xx TO "FALSE"

- **From:** "jce" <defaultuser@hotmail.com>
- **Date:** 2003-09-23T03:45:44+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<IlPbb.3124$eS5.751@twister.tampabay.rr.com>`
- **References:** `<9e486bb5.0309160140.3f2758a0@posting.google.com> <26pdmvkam9duvd922fsl0md0ohpqldk134@4ax.com> <No2cndjGpIQSVvqiXTWJkw@giganews.com> <3f68057e_6@news.athenanews.com> <iv9ab.1464$Od.111561@twister.tampabay.rr.com> <vmim0dg4hh2hde@corp.supernews.com> <bkcf82$paj$1@peabody.colorado.edu> <bkdf5c$g99s$1@ID-184804.news.uni-berlin.de> <78vab.8686$Od.314122@twister.tampabay.rr.com> <bkns64$3pvcj$1@ID-184804.news.uni-berlin.de>`

```
"Frank Swarbrick" <Frank.Swarbrick@efirstbank.com> wrote in message
news:bkns64$3pvcj$1@ID-184804.news.uni-berlin.de...
> jce<defaultuser@hotmail.com> 09/18/03 09:56PM >>>
> >"Frank Swarbrick" <Frank.Swarbrick@efirstbank.com> wrote in message

snip snip

> Ah, but here is what I am trying to get it.  Let's say you want to search
> your source code for every place that MY-ACCOUNT might be changed.  If you
…[8 more quoted lines elided]…
> This was all I was getting at...
Point is well taken.
Of course, the issue in this instance is that you would be looking for a
particular instance of the acct_types type and unless you have only one you
may not be able to narrow it down.

I may have a function
int changeAccountType(int* accountType)
{
        return accountType + 10;
}

where it is called with:
int *alias = my_acct;
...
lines of code....other functions....
...
changeAccountType(alias);

This is still hokey to find.

My point is that there is nothing wrong with anything until someone does
something stupid - or more often "clever".  :-)

> >You could also do this without 88....
> >01 MY-ACCOUNT  PIC X(10)..
…[3 more quoted lines elided]…
> >
snip snip
> I don't much care for this method in general, but on the other hand I do
use
> it if the situation calls for it.  Your example doesn't match your
previous
> example, though.
> How about:
…[5 more quoted lines elided]…
> Anyway, no big deal.  It was just something I liked about C.
Moi aussi.  But as much as you don't like this method it does do what you
wanted - you can find every instance that it changes :-)

JCE
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
