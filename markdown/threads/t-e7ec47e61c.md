[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# A STUPID nebie question...I'm BOGGING for help!!!

_11 messages · 10 participants · 1999-02_

---

### A STUPID nebie question...I'm BOGGING for help!!!

- **From:** kmckenna@q-com.com
- **Date:** 1999-02-07T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<79kgvf$5is$1@nnrp1.dejanews.com>`

```
Hi,	Thanks for even looking at this post. I am currently in 2 different
programming courses. C (Which I am picking up really fast) and COBOL 1. We
are reading Stern/Stern v.8. The instructor went right through the first 3
divisions and now, 3 weeks later we are in the procedure division, whic is
also making sense to me, because it's just functions, and I get those.	   I
understand the ID DIV...I'm not THAT stupid, but I'm lost in the environment
and data Div's.  IF, anyone of you folks would be so kind as to explain to me
how these divisions work, like I'm a 3 year old....maybe I'll get through
this class with my sanity. I have bought the "Cobol for Dummies" book, and it
doesn't help. The author goes right past these two divisions as well.	  
The instructor says I'll "get it" because he is also my C instructor, and he
figures I'm making it harder than it is, but I can't figure out what you are
supposed to write in these divisions...exactly. I'm HOPING that someone out
there has been where I am, and got through it, and figured it out, and would
be kind enough to help me. I KNOW, it's something stupid, and then it will
make sense to me.	  I get confused with the selects and assigns and
then in data division, I get confused in the FD's and then in Working
Storage, and HOW you actually set them up.	  I would be very grateful to
anyone who would care to help in whatever way I can. Thanks, Kevin
kmckenna@q-com.com

-----------== Posted via Deja News, The Discussion Network ==----------
http://www.dejanews.com/       Search, Read, Discuss, or Start Your Own
```

#### ↳ Re: A STUPID nebie question...I'm BOGGING for help!!!

- **From:** sbricklin@aol.com (SBRICKLIN)
- **Date:** 1999-02-07T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<19990207121434.18799.00001005@ng143.aol.com>`
- **References:** `<79kgvf$5is$1@nnrp1.dejanews.com>`

```

  

Special High Intensity Training

To:           All employees
From:       Management

Subject:   Special High Intensity Training


	In order to assure the highest levels of quality work and productivity from
employees, it will be our policy to keep all employees well trained through our
program of SPECIAL HIGH INTENSITY TRAINING (S.H.I.T.). We are trying to give
employees more S.H.I.T. than anymore else.
	If you feel that you do not receive your share of S.H.I.T. on the job, please
see
your manager. You will be immediately placed at the top of the S.H.I.T. list,
and our
managers are especially  skilled at seeing that you get all the S.H.I.T. you
can
handle. 
	Employees who don't take their S.H.I.T. will be placed in DEPARTMENTAL
EMPLOYEE EVALUATION PROGRAMS (D.E.E.P.S.H.I.T.). Those who will fail to
take D.E.E.P.S.H.I.T. seriously will have to go to EMPLOYEE ATTITUDE TRAINING
(E.A.T.S.H.I.T.). Since our managers took S.H.I.T. before they were promoted,
they
don't have to do S.H.I.T. anymore, and are all full of S.H.I.T. already.
	If you are full of S.H.I.T.,  you may be interested in a job training others.
We
can add your name to our BASIC UNDERSTANDING LECTURE LIST
(B.U.L.L.S.H.I.T.). Those who are full of B.U.L.L.S.H.I.T. will get the
S.H.I.T. jobs,
and can apply for promotion to DIRECTOR OF INTENSITY PROGRAMMING
(D.I.P.S.H.I.T.).
	If you have further questions, please direct them to our HEAD OF TRAINING,
SPECIAL HIGH INTENSITY TRAINING (H.O.T.S.H.I.T.).

Thank you.

BOSS IN GENERAL
SPECIAL HIGH INTENSITY TRAINING
(B.I.G.S.H.I.T.)
```

##### ↳ ↳ Re: A STUPID nebie question...I'm BOGGING for help!!!

- **From:** blind_wolf@hotmail.com (BlindWolf)
- **Date:** 1999-02-07T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<36bed2f2.1354341@corp.supernews.com>`
- **References:** `<79kgvf$5is$1@nnrp1.dejanews.com> <19990207121434.18799.00001005@ng143.aol.com>`

```
Thanks, I get the point...don't ask question in this group which might
help me...OK. I won't bother you anymore. This is just the kind of
response I didn't need today.
LaterOn 7 Feb 1999 17:14:34 GMT, sbricklin@aol.com (SBRICKLIN) wrote:

>
>  
…[40 more quoted lines elided]…
>(B.I.G.S.H.I.T.)
```

#### ↳ Re: A STUPID nebie question...I'm BOGGING for help!!!

- **From:** denis548@aol.com (Denis548)
- **Date:** 1999-02-07T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<19990207132134.19637.00001098@ng-fu1.aol.com>`
- **References:** `<79kgvf$5is$1@nnrp1.dejanews.com>`

```
As briefly as possible:

The environment division is where cobol compilers interface to files that are
outside the direct control of the compiler.  Files can be accessed but fully
controlled like you would in an operating system.  There's more to it than that
but that's the main use.  

The data division declares and "subdivides" storage.   It's like c struct's. 
Any field can be declared in such a way that it has a structure.  At program
startup, memory is allocated and initialized as shown in the data division.  If
you do not specify otherwise, all data division entries are global in the
program.  

All paragraphs in cobol are "visible" to all other paragraphs in a program as
well.  Think of memory as the playing field and paragraphs as spectators. 
Stadium seating...

Hope that helps
```

#### ↳ Re: A STUPID nebie question...I'm BOGGING for help!!!

- **From:** "Donald Tees" <donald@willmack.com>
- **Date:** 1999-02-07T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<79knch$3gd$1@news.igs.net>`
- **References:** `<79kgvf$5is$1@nnrp1.dejanews.com>`

```
The two divisions are quite simple, really.  The environment
says where everything is.  What computer you are going to
run on, where the files are located on that computer
(or network), etc.  A lot of it is documentary, but the selects
in particular link file descriptions that you plan to use to specific
files on the computer.  The type of file, the access method, and
information on sharing is also included.

The data division is where you describe your data.  File descriptions
are included, but only that portion that describes the data, not
how it is accessed because that could vary.  For example,
you could have a customer file that existed on disk and was
accessed as an ISAM file in one program, and the same data
spooled off onto tape and accessed as a line sequential tape
file in another program.  The FD's could both be copied from
the same library into two programs, but with each having
different select clauses.

Cobol is highly typed: in other words, every data name must
be described before it can be used in the program. The data
division also includes working-storage where you describe
all the variables that you want to use in your program. It is
pretty well the same as declaring variables in C, except that
it is all done in one place, and the data types that you can
set up are several thousand times as detailed.  C exists on
half a dozen basic types.  Cobol allows you to create your
own types with records and pictures.

kmckenna@q-com.com wrote in message <79kgvf$5is$1@nnrp1.dejanews.com>...
>Hi, Thanks for even looking at this post. I am currently in 2 different
>programming courses. C (Which I am picking up really fast) and COBOL 1. We
…[3 more quoted lines elided]…
>understand the ID DIV...I'm not THAT stupid, but I'm lost in the
environment
>and data Div's.  IF, anyone of you folks would be so kind as to explain to
me
>how these divisions work, like I'm a 3 year old....maybe I'll get through
>this class with my sanity. I have bought the "Cobol for Dummies" book, and
it
>doesn't help. The author goes right past these two divisions as well.
>The instructor says I'll "get it" because he is also my C instructor, and
he
>figures I'm making it harder than it is, but I can't figure out what you
are
>supposed to write in these divisions...exactly. I'm HOPING that someone out
>there has been where I am, and got through it, and figured it out, and
would
>be kind enough to help me. I KNOW, it's something stupid, and then it will
>make sense to me.   I get confused with the selects and assigns and
…[6 more quoted lines elided]…
>http://www.dejanews.com/       Search, Read, Discuss, or Start Your Own
```

#### ↳ Re: A STUPID nebie question...I'm BOGGING for help!!!

- **From:** NoLonger@ix.netcom.com (OldUncleMe)
- **Date:** 1999-02-08T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<36be6391.11134994@news>`
- **References:** `<79kgvf$5is$1@nnrp1.dejanews.com>`

```
It was: Sun, 07 Feb 1999 17:02:43 GMT and with a STARTLING amount of insight,
"kmckenna@q-com.com" posted "A STUPID nebie question...I'm BOGGING for help!!!" to
"comp.lang.cobol" :

-->Hi,	Thanks for even looking at this post. I am currently in 2 different
-->programming courses. C (Which I am picking up really fast)

<!...wow, I hope I can pick up c really fast....>

-->understand the ID DIV...I'm not THAT stupid, but I'm lost in the environment
-->and data Div's.  IF, anyone of you folks would be so kind as to explain to me

The environment division is the place to name and tell the location of the files you
will be using in your program.  (Nearly everything else normally done here is quite
specific to the machine you're working on, and usually optional.)  Say what kind of
file(s) they are, the path, explicitly, if it is not in the same place as the
program, with some compilers, and with others, always say the full path.  Describe
the type of file it is.  How it will be accessed.  Special features of the file(s).  

            Select no-name assign to 'c:\somedir\some.file'  
              organization is indexed
              access mode is dynamic
              record key is no-acct
              alternate record key is no-cust with duplicates
              file status is ww09-no-status.

no-name is the file name you will use in your program,
         the name has been assigned to the given file for
         internal use only.
path and filename:  'c:\somedir\some.file'  
how it's organized: the program must know explicitly
                                    (line sequential ??) (indexed ??)
how it's accessed:  dynamic?  random? some other way??
some advanced features follow the above, you'll get there if you're around for a
while.






DATA DIVISION:

       fd  idxn-mast.
       01  idxn-rec.
           02 idxn-acct       pic 9(5).
           02 idxn-cust       pic x(20).
           02 idxn-type       pic x.
           02 idxn-begbal     pic S9(4)v99.
           02                 pic x(48).

This describes the organization of a file, broken into records.  Each record is
considered to be 80 columns (bytes) long.  This one is broken into 
5 bytes=they are numeric data
20bytes=they are alpha-numeric
1 that is alpha-num
4 + (implied decimal point) + 2 = all numeric
48 bytes that are unused, but enumerated to fill out the record
__
80

Think of these records as lines on a page, each line is broken into described
'fields'; together all the lines make up a file, each line is 80 characters long (in
this case.)  The fields are sized as above, in order, from left to right, and contain
either data of the type specified.  If empty though, for numeric fields, zeros;  for
alphanumeric fields, spaces.  (Hopefully; though testing to assure that all of this
is true has been the goal of a lot of the programming I've encountered...)

When a record (line) of a file is read into memory by the program, the definitions
given in DD not only place the data into known memory locations but allow the program
to understand what the data is and therefore to work with the data and, perchance, to
find and request of the operating system the correct data and amount of data from
storage of some kind--disk, tape, punch card, memory, sundial.  An FD entry is often
made to describe data that will be output after processing by the program, say, to a
printer, a file, a tape drive, a card puncher, a subprogram, a servo motor
controller?

FD stands for File Description.  The WORKING STORAGE section of the data division,
OTOH, defines memory allocated for the use of the running program, not in association
with reading into ram some file's record, but for intermediate processing steps.  It
is by type of data also.  Each field is normally named something that can be referred
to.  You can move a chunk of data to a location, modify it, copy it, add to it, move
it to a described record, write it to a printer or a file.  You can compound w/s
entries to create tables or arrays that hold multiple data items in memory in an
organized, indexed even, fashion.  Then you read it, massage it, oil it, put it to
bed and it's very nice to you.  TS




"Come to think of it, there are already a million monkeys on a million
 typewriters, and Usenet is NOTHING like Shakespeare." Blair Houghton
***********entia non sunt multiplicanda praeter necessitate***********
++++++****tauceti****@****abraxis****.****com****for***email****++++++
```

##### ↳ ↳ Thanks...This helped a lot...seriously

- **From:** kmckenna@q-com.com (Kevin McKenna)
- **Date:** 1999-02-10T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<36c2a6d6.9072476@207.126.101.100>`
- **References:** `<79kgvf$5is$1@nnrp1.dejanews.com> <36be6391.11134994@news>`

```
I just wanted to say thanks to you and to others that helped me get
through this very stupid (on my part) section. Maybe now, I can get
caught up to where I should be in class.
Thanks again,
Kevin

On Mon, 08 Feb 1999 05:08:04 GMT, NoLonger@ix.netcom.com (OldUncleMe)
wrote:

>It was: Sun, 07 Feb 1999 17:02:43 GMT and with a STARTLING amount of insight,
>"kmckenna@q-com.com" posted "A STUPID nebie question...I'm BOGGING for help!!!" to
…[91 more quoted lines elided]…
>++++++****tauceti****@****abraxis****.****com****for***email****++++++
```

#### ↳ Re: A STUPID nebie question...I'm BOGGING for help!!!

- **From:** cwestbury@giant.intranet.com (Chris Westbury)
- **Date:** 1999-02-08T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1999Feb8.002502.19518@giant>`
- **References:** `<79kgvf$5is$1@nnrp1.dejanews.com>`

```
In article <79kgvf$5is$1@nnrp1.dejanews.com>,
kmckenna@q-com.com wrote:
>
> I am currently in 2 different programming courses.  C (which I am
> picking up really fast) and COBOL 1.

No offense, but this is not a good idea.  It's like trying to study flute
and clarinet at the same time.  There's no problem with studying them
separately (in either order), but if you try to learn them at the same
time, the clarinet embouchure interferes with the flute embouchure, and
it plays hob with your ear because the clarinet is in B-flat and the
flute is in concert.


> We are reading Stern/Stern v.8.

A good choice.


[...]
> I have bought the "Cobol for Dummies" book, and it doesn't help.

"Helen" will be along presently to recommend another book.  :-)

But seriously, and again no offense, what do you think I could possibly
write off the top of my head in this tiny 80 x 24 space that would help
you more than the two professionally-written, -edited, and -printed books
that you already have ??  Usenet is an extremely limited medium.

What you need is to find someone you can talk to in person, perhaps
someone who took the course last year.  It doesn't take more than a few
hours to "get it".

Pay particular attention to the DATA DIVISION, which is, if anything,
more important than the PROCEDURE DIVISION.  Above all, don't stint on
the exercises!  Exercises give you the prerequisites for understanding
even though it may not seem like it while you are doing them.
```

##### ↳ ↳ Re: A STUPID nebie question...I'm BOGGING for help!!!

- **From:** kjmckenna@q-com.com (BlindWolf)
- **Date:** 1999-02-09T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<36c04e56.1121789@corp.supernews.com>`
- **References:** `<79kgvf$5is$1@nnrp1.dejanews.com> <1999Feb8.002502.19518@giant>`

```
Chris,
   Thanks for the input, and I agree, taking these two courses at the
same time is difficult, but it is what the college I attend suggested,
based on my background.
   I have gotten the answers I needed from some very kind people in
this group. The answer wasn't all that difficult now that I see it for
what it was. I couldn't figure out the select and assigns for the PC I
am on. I missed a couple of quotes and periods, and now that I see the
syntax and the order in which it is used, it makes sense to me...as
does the data division.
   I've put the COBOL for dummies on the shelf, and have gotten fully
into Stern. 
   I do have one opinion though, I'm actually finding that one class
helps the other. I am finding that although the two languages are
completely different, they do reinforce the basic ideas of each other.
For example, the "If" statements and how one uses them becomes
clearer, to me anyway, when looking at the different ways they are
used in the two languages.
   So, with all that said, maybe I can get into the procedure division
and get my but caught up. I understand how things are being done, at
least, in the procedure division, and now that the first 3 divisions
make sense, maybe I can get an A in this course...who knows?
Thanks,
Kevin

On 8 Feb 99 00:25:02 EST, cwestbury@giant.intranet.com (Chris
Westbury) wrote:

>In article <79kgvf$5is$1@nnrp1.dejanews.com>,
>kmckenna@q-com.com wrote:
…[34 more quoted lines elided]…
>even though it may not seem like it while you are doing them.
```

###### ↳ ↳ ↳ Re: A STUPID nebie question...I'm BOGGING for help!!!

- **From:** Ed.Stevens@nmm.nissan-usa.com
- **Date:** 1999-02-10T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<79s42f$glp$1@nnrp1.dejanews.com>`
- **References:** `<79kgvf$5is$1@nnrp1.dejanews.com> <1999Feb8.002502.19518@giant> <36c04e56.1121789@corp.supernews.com>`

```
Since you're finding it easier to understand "C" than Cobol, another resource
you might want to check out is "Moving from Cobol to C" by Mo Budlong (Sam's
Publishing).  It's going the other way, but still does a good job of showing
how concepts in one relate to the other.


In article <36c04e56.1121789@corp.supernews.com>,
  kjmckenna@q-com.com wrote:
> Chris,
>    Thanks for the input, and I agree, taking these two courses at the
…[64 more quoted lines elided]…
>

Ed Stevens
Nissan Motor Mfg. Corp., USA

-----------== Posted via Deja News, The Discussion Network ==----------
http://www.dejanews.com/       Search, Read, Discuss, or Start Your Own
```

###### ↳ ↳ ↳ Re: A STUPID nebie question...I'm BOGGING for help!!!

_(reply depth: 4)_

- **From:** coboljit@aol.com (COBOLJIT)
- **Date:** 1999-02-11T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<19990211035049.28644.00000200@ngol08.aol.com>`
- **References:** `<79s42f$glp$1@nnrp1.dejanews.com>`

```

In article <79s42f$glp$1@nnrp1.dejanews.com>, Ed.Stevens@nmm.nissan-usa.com
writes:

>Since you're finding it easier to understand "C" than Cobol, another resource
>you might want to check out is "Moving from Cobol to C" by Mo Budlong (Sam's
…[3 more quoted lines elided]…
>

If you need "Moving from COBOL to C", please contact me.  The copyrights have
reverted to the author and it is being re-printed.

Helen
818-951-5240
Helen

------------------------------------------------------------------------------
King Computer Services, Inc.
COBOL Training for the Year 2000
"COBOL, Just in Time" Crash Course
"COBOL, Dates and the Year 2000" Technical Reference.
818-951-5240
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
