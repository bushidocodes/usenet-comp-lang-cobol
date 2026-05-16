[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# WRITE USING POINTER IN COBOL.

_7 messages · 4 participants · 2002-01_

---

### WRITE USING POINTER IN COBOL.

- **From:** nivas_shyam@indiatimes.com (shyam nivas)
- **Date:** 2002-01-16T04:34:06-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<c02fd744.0201160434.44688db0@posting.google.com>`

```
Hi,
             I have a pointer refrencing to a variable in cobol.I
would like to write the same variable in a file by using pointer not
using variable.
            Genarally we use WRITE OUT-REC.
but i would like to use:
            WRITE OUT-REC-POINTER 
 but it is  NOT WORKING.
where out-rec-pointer is pointer type variable pointing to out-rec.
thanks and Regards.
shyam nivas
```

#### ↳ Re: WRITE USING POINTER IN COBOL.

- **From:** scomstock@aol.com (S Comstock)
- **Date:** 2002-01-16T14:23:17+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<20020116092317.00742.00001438@mb-ck.aol.com>`
- **References:** `<c02fd744.0201160434.44688db0@posting.google.com>`

```
shyam nivas writes ...

>Hi,

Hi, yourself, Shyam. Did you get the DLL problem working? Never heard if you
were successful.


>             I have a pointer refrencing to a variable in cobol.I
>would like to write the same variable in a file by using pointer not
…[3 more quoted lines elided]…
>            WRITE OUT-REC-POINTER 

Well, are you trying to write out the pointer or the data pointed at by the
pointer? I presume the latter, since writing out a pointer is meaningless.

Remember, COBOL is not C (and it's a good thing, too). It sounds like you can
accomplish the task you want by using the FROM option:

    WRITE OUT-REC FROM REC-AREA

Now, if REC-AREA is in working-storage, no problem. But I gather your data may
be somewhere else. Then, you have to define REC-AREA in linkage section and
say:

     SET ADDRESS OF REC-AREA TO OUT-REC-POINTER
     WRITE OUT-REC FROM REC-AREA

> but it is  NOT WORKING.
>where out-rec-pointer is pointer type variable pointing to out-rec.
>thanks and Regards.

Let me know how it goes. [Are you sure you don't want us to come teach a
class?]

Kind regards,


Steve Comstock
Telephone: 303-393-8716
www.trainersfriend.com
email: steve@trainersfriend.com
256-B S. Monaco Parkway
Denver, CO 80224
USA
```

##### ↳ ↳ Re: WRITE USING POINTER IN COBOL.

- **From:** nivas_shyam@indiatimes.com (shyam nivas)
- **Date:** 2002-01-17T01:30:14-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<c02fd744.0201170130.11483add@posting.google.com>`
- **References:** `<c02fd744.0201160434.44688db0@posting.google.com> <20020116092317.00742.00001438@mb-ck.aol.com>`

```
Hi Steve,
             MY  DLL problem is completely solved and again many many
thanks from my side and from whole cognizant family.whatever you
suggested are generally not availabe in Books and these things are
learned only by experience.so I myself is very eager to attain your
class.I joined cognizant on 27th June 2001 and I am a trainee here.Our
company office is in Pune near Mumbai.
             Regarding calling you for teaching, Its my pleasure to
attain your class but I individually can not call you.I escalated the
matter to higher authorities and now it depends more on them and
company requirement.Frankly speaking steve, due to slowdown  the whole
Indian market is affected and right now all company is doing cost
cutting.But We have hope and I am confident that old days will come
back.
*******************************************************************************
            Now my Problem of using WRITE verb in COBOL by pointer.
My basic problem is I would like to do some manipulation on 3MB of
data in a application but I do not want to define big working section
of 3MB.My aim is to put data somewhere in virual memory outside the
application program and use pointer to that area for manipulation.Is
this possible in cobol?

Thanks and Warm Regards.
shyam
*******************************************************************************
scomstock@aol.com (S Comstock) wrote in message news:<20020116092317.00742.00001438@mb-ck.aol.com>...
> shyam nivas writes ...
> 
…[44 more quoted lines elided]…
> USA
```

###### ↳ ↳ ↳ Re: WRITE USING POINTER IN COBOL.

- **From:** scomstock@aol.com (S Comstock)
- **Date:** 2002-01-17T13:23:56+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<20020117082356.22244.00002212@mb-mm.aol.com>`
- **References:** `<c02fd744.0201170130.11483add@posting.google.com>`

```
Shyam,

I am looking at this:

>> 
>>      SET ADDRESS OF REC-AREA TO OUT-REC-POINTER
…[5 more quoted lines elided]…
>

Keep things simple. The Write statement must name an 01-level data item that
follows the FD (that is, not in working-storage or linkage sections); so you
can't use a pointer for that.

Rec-pointer must point to an area in linkage-section, then the two lines I
coded above will work.

Kind regards,


Steve Comstock
Telephone: 303-393-8716
www.trainersfriend.com
email: steve@trainersfriend.com
256-B S. Monaco Parkway
Denver, CO 80224
USA
```

###### ↳ ↳ ↳ Re: WRITE USING POINTER IN COBOL.

- **From:** "William M. Klein" <wmklein@ix.netcom.com>
- **Date:** 2002-01-18T11:58:24-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<a29no7$h8f$1@slb6.atl.mindspring.net>`
- **References:** `<c02fd744.0201160434.44688db0@posting.google.com> <20020116092317.00742.00001438@mb-ck.aol.com> <c02fd744.0201170130.11483add@posting.google.com>`

```
"shyam nivas" <nivas_shyam@indiatimes.com> wrote in message
news:c02fd744.0201170130.11483add@posting.google.com...
 <snip>
>             Now my Problem of using WRITE verb in COBOL by pointer.
> My basic problem is I would like to do some manipulation on 3MB of
…[6 more quoted lines elided]…
> shyam
 <snip>

GREAT, now you have told us WHY you want to do what you are asking about.

Now we can tell you that you will GAIN *nothing* be putting your 3MB in
"some other virtual storage" location rather than in your own working
storage.

If this is a "batch" program (and in at least one of your notes indicating
passing data from step-to-step - so I would guess that it is), then having
3MB WS items is NOT a big deal in an OS/390 (or z/OS) environment.  Any
"tricks" you might do to try and keep this "separate" from your program
would be MAINTENANCE nightmares and would NOT be a "good" think to do.

This can't be a CICS program (where a 3MB WS item *might* be a problem) -
because you wouldn't be talking about the WRITE statement.

It COULD be an IMS BMP program - and if so, having a 3MB WS item *might* be
a minor concern.  But again, doing "tricks" would probably NOT make it
worthwhile to separate your data from your program.  If you have been
"given" by your systems designer a REQUIREMENT for a "small" program, find
out WHY and let us know that.  There may well be a better way to approach
your entire application, depending on the real need.
```

###### ↳ ↳ ↳ Re: WRITE USING POINTER IN COBOL.

- **From:** scomstock@aol.com (S Comstock)
- **Date:** 2002-01-18T18:20:50+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<20020118132050.22376.00001954@mb-mm.aol.com>`
- **References:** `<c02fd744.0201170130.11483add@posting.google.com>`

```
Shyam, you wrote...

>            Now my Problem of using WRITE verb in COBOL by pointer.
>My basic problem is I would like to do some manipulation on 3MB of
…[4 more quoted lines elided]…
>

Yes, using calls to LE services. 

Ahem. Yes, we do a class on that, too.

Kind regards,


Steve Comstock
Telephone: 303-393-8716
www.trainersfriend.com
email: steve@trainersfriend.com
256-B S. Monaco Parkway
Denver, CO 80224
USA
```

#### ↳ Re: WRITE USING POINTER IN COBOL.

- **From:** "WOB" <wobconsult@sprynet.com>
- **Date:** 2002-01-16T21:30:49-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<a25cgp$gad$1@slb2.atl.mindspring.net>`
- **References:** `<c02fd744.0201160434.44688db0@posting.google.com>`

```
 Shyam,

            My biggest question would be WHY ? What are your benefits ?

            If you write the record from the POINTER and the File is
variable-length (minimum length of 4), you'll wind up with a 4-byte record,
whose contents will be meaningless.

            If the File is fixed-length and not equal to an LRECL of 4,
you'll get an error on the WRITE.

            If you define a LINKAGE SECTION "01" level that's equal in
length to OUT-REC, then set this "01" level to the POINTER and WRITE from
it.

            Forgive me, but I just can't fathom why you would want to do
this.

Puzzled,

Bill

"shyam nivas" <nivas_shyam@indiatimes.com> wrote in message
news:c02fd744.0201160434.44688db0@posting.google.com...
> Hi,
>              I have a pointer refrencing to a variable in cobol.I
…[8 more quoted lines elided]…
> shyam nivas
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
