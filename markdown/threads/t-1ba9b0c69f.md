[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Micro Focus NetExpress questions

_12 messages · 6 participants · 1998-09_

**Topics:** [`Compilers and vendors`](../topics.md#compilers)

---

### Micro Focus NetExpress questions

- **From:** kfloyd <kfloyd@shawsystems.com>
- **Date:** 1998-09-15T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<35FE3FF1.FF1AA088@shawsystems.com>`

```
I've used Micro Focus 16 bit for several years and the 32 bit version 4
for several months.  Now I'm in the process of evaluating NetExpress to
see if it will be our development environment of choice for a new
project.  Time is short, and I'm having difficulty figuring out the
NetExpress project environment.  So I'm asking for help before I give up
on NetExpress.

Here's what I want to do.  I want to have an OLE Automation Server that
can dynamically call .DLL's.  Some of the .DLLs will be based on source
that has DB2 embedded SQL.  I don't want to use the NetExpress ODBC SQL,
but instead run the source through the DB2 translator.

My first problem is that I don't see a way to put the un-translated
source in the project so that I could run the DB2 translator as part of
the build.  Does anybody know a way to accomplish that ?  My work-around
would be to run the translator outside the project.  NetExpress seems to
notice that the source has changed and will re-compile the resulting new
.CBL file.

The second problem for me is that the whole project thing seems
cumbersome for a large development effort.  I'd really rather manage
everything myself and run the compiles from the command line.  I realize
that I'm 'speaking' from ignorance, since I haven't really learned my
way around NetExpress.  But it looks like every file has to be added to
the project individually and that it would be difficult to handle
'merging' one developer's work with another.  Does anybody have
experience with large project management - several hundred .DLL's plus
hundreds more copybooks worked on by a dozen developers ?  I'm ready to
be convinced that projects are wonderful -- I just can't see it from
here.

I saw in the doc that OLE Servers have to be in a project, so my next
thought was to do that, but keep the bulk of the other code elsewhere
and do command line compiles.  But that leads to the Animator.  This is
a new development effort, so Animating is vital.  I can't figure out how
to set up the OLE Server project so that it will find the .DLL's I've
kept out of the project and go into animation on them, too.  So far I
keep getting 'called program not found'.  I've tried setting the COBDIR,
PATH, COBIDY, etc. both as project parameters and as System level
environment variables.  Does anybody know if this should work, and if
so, how to set it up ?

Thanks in advance for any help and advice

Ken Floyd
Shaw Systems
```

#### ↳ Re: Micro Focus NetExpress questions

- **From:** sands@mcmail (David Sands)
- **Date:** 1998-09-15T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<35fedaee.5211904@news.mcmail.com>`
- **References:** `<35FE3FF1.FF1AA088@shawsystems.com>`

```
On Tue, 15 Sep 1998 16:20:19 GMT, kfloyd <kfloyd@shawsystems.com>
wrote:


>My first problem is that I don't see a way to put the un-translated
>source in the project so that I could run the DB2 translator as part of
…[3 more quoted lines elided]…
>.CBL file.

Net Express has support for the DB/2 precompiler built in. You do not
need to Precompile outside the IDE but do need to set the relevant
directives. There is a documentation download on WebSync which details
all the directives. I think it also still accepts the directive that
could be using in Workbench for DB2 support. You will need to IBM DB2
SDK installed.
>
>.  But it looks like every file has to be added to
>the project individually and that it would be difficult to handle
>'merging' one developer's work with another. 

Check out the import of LBT files. It is an easy way to automate the
loading of elements to a project even if you never used them. You can
easily set up a LBT for import using redirection :- 

"dir /b *.int > myapp.lbt"

You can then highlight the INTs of the programs you want in the DLL
and right click. Select package as a DLL.

If you have multiple developers working together you should consider
investing in a good source control package (MS Source Safe or PVCS
come to mind) which could help manage the situation.

>
>I saw in the doc that OLE Servers have to be in a project, so my next
…[8 more quoted lines elided]…
>so, how to set it up ?

If the DLL name if different to the entry point you are trying to call
then you need to load the DLL first by using procedure pointers:-

01 ws-point    usage is procedure-pointer.

	set ws-point to entry "mydllname"

Hope this helps
David.
```

##### ↳ ↳ Re: Micro Focus NetExpress questions

- **From:** kfloyd <kfloyd@shawsystems.com>
- **Date:** 1998-09-16T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<35FFB07D.D9692BF6@shawsystems.com>`
- **References:** `<35FE3FF1.FF1AA088@shawsystems.com> <35fedaee.5211904@news.mcmail.com>`

```


David Sands wrote:

> Net Express has support for the DB/2 precompiler built in. You do not
> need to Precompile outside the IDE but do need to set the relevant
…[3 more quoted lines elided]…
> SDK installed.

Thanks for the pointer to WebSync.  I couldn't find any references to the DB2
pre-processor still being built in.  I'll check out Websync.
```

#### ↳ Re: Micro Focus NetExpress questions

- **From:** "Gene Webb" <gene.webb@newsguy.com>
- **Date:** 1998-09-15T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<6tnbuo$sr9@enews2.newsguy.com>`
- **References:** `<35FE3FF1.FF1AA088@shawsystems.com>`

```
I agree that the IDE/Project Environment is cumberson and a lot of times
leaves questions in my mind as to what is being compiled and linked into my
DLL/EXE.  I don't like the fact that I can't change the default compiler
directives when it comes up (you have to use a directives file to override
this).  I personally do not use the IDE at ALL!  I compile and link from the
command line. If I have to debug I use the CBL_BREAK compiler directive and
still run from the command line using the IDE only enough to animate.

We have three other developers that use Netexpress right now.  They all use
the IDE. The biggest reason they use the IDE (99%) is that they all come
from a mainframe environment where someone else usually set up the compile
and link JCL and do not understand how to compile and link from the command
line.

Of all of the problems that they have experienced 99.5% are directly related
to the IDE or not understanding how to use the IDE.  This has caused all
kinds of problems.

I STRONGLY recommend that you set up make files and compile from the command
line.  I create one directory for each program and I have a standard make
file that I replace the program name with a variable in the make file that
works for every DLL and one for every EXE file.  I can rebuild my entire
application (50 or more programs) in a couple of minutes with a simple batch
file.

I have had very few problems with the Netexpress compiler but tons of
problems with the IDE.  I remember someone once wrote in this newgroup that
an IDE should make you at least 50% more productive and I agree.  The
Netexpress IDE takes 3 to 5 times longer (I personally found the Fujitsu IDE
worse) to use, IF YOU UNDERSTAND compiling and linking.  I would contend if
you don't (and don't take the time to learn) you are going to have more
problems in the long run whether you use the IDE or not.

Okay thats my 2 cents worth.

kfloyd wrote in message <35FE3FF1.FF1AA088@shawsystems.com>...
>I've used Micro Focus 16 bit for several years and the 32 bit version 4
>for several months.  Now I'm in the process of evaluating NetExpress to
…[44 more quoted lines elided]…
>
```

##### ↳ ↳ Re: Micro Focus NetExpress questions

- **From:** kfloyd <kfloyd@shawsystems.com>
- **Date:** 1998-09-16T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<35FFB174.1309904A@shawsystems.com>`
- **References:** `<35FE3FF1.FF1AA088@shawsystems.com> <6tnbuo$sr9@enews2.newsguy.com>`

```


Gene Webb wrote:[snipped some discussion of IDE vs. Command Line]

> I STRONGLY recommend that you set up make files and compile from the command
> line.  I create one directory for each program and I have a standard make
…[12 more quoted lines elided]…
>

At the moment, I, too feel more comfortable with using the command line. Thanks
for the advice.
```

#### ↳ Re: Micro Focus NetExpress questions

- **From:** smayer@t-online.de (Sebastian Mayer)
- **Date:** 1998-09-15T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<6tmrrh$pgp$1@news02.btx.dtag.de>`
- **References:** `<35FE3FF1.FF1AA088@shawsystems.com>`

```
kfloyd wrote:
> 
> 
…[29 more quoted lines elided]…
> 
I don´t have any experience with dll´s because I´m working with int,gnt
and 
lbr´s. But perhaps you could adapt the behaviour.
1) With the above files you don´t need to take them into a project. You
can
   edit/compile one single file (like in 16bit Workbench). If another
file
   calls it, it must be only accesible via cobdir. If you use a lbr, you
must
   call it if you want to call a file within, e.g. to use file
"subprog.gnt"
   in "lib1.lbr" you must do the following:
   call "lib1.lbr"    (do it at the beginning of the program)
   ...
   call "subprog" using ...
2) If you don´t have them in the project, NetExpress doesn´t 
   notice that the source has changed and will NOT re-compile the file
3) If you have problems, animating dll´s writen in COBOL try to replace
the
   programms with their gnt/int equivalent.
```

#### ↳ Re: Micro Focus NetExpress questions

- **From:** "Leif Svalgaard" <leif@ibm.net>
- **Date:** 1998-09-15T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<35fe9530.0@news1.ibm.net>`
- **References:** `<35FE3FF1.FF1AA088@shawsystems.com>`

```
kfloyd wrote in message <35FE3FF1.FF1AA088@shawsystems.com>...
>I'm asking for help before I give up on NetExpress.


I'm sorry that I cannot help you (I'm sure someone else will).
I'm here just supporting your contention that the whole Project
idea is half-baked and won't work for large-scale development.

>
>The second problem for me is that the whole project thing seems
…[9 more quoted lines elided]…
>here.
```

##### ↳ ↳ Re: Micro Focus NetExpress questions

- **From:** "Donald Tees" <donald@willmack.com>
- **Date:** 1998-09-15T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<6tn0a8$52o$1@news.igs.net>`
- **References:** `<35FE3FF1.FF1AA088@shawsystems.com> <35fe9530.0@news1.ibm.net>`

```
Leif Svalgaard wrote in message <35fe9530.0@news1.ibm.net>...
>kfloyd wrote in message <35FE3FF1.FF1AA088@shawsystems.com>...
>
…[6 more quoted lines elided]…
>>everything myself and run the compiles from the command line.  I realize


I have not found one I like for even the smaller stuff ... my systems
typically
run about 50-80 programs, maybe 10 databases.  Not one of the systems
allows me to set up a project the way that I feel it should be set up. The
more
complex the system, the less versatile.

Funnily enough, they would all be fairly decent if they simply (and not one
I have used does)  allowed nesting. The concept of a large project being
composed of small projects never seems to have occurred to one of them.
There has also not been one that had a hook.  I want to backup by versions,
for example, as part of my make.  A nice simple make allows copies.  I have
yet to see one that scans Cobol programs and *BIULDS* dependency lists.

I see that Fujitsu actually uses a second party(MS) make, and the GUI
project
manager simply builds the make files.
```

###### ↳ ↳ ↳ Re: Micro Focus NetExpress questions

- **From:** kfloyd <kfloyd@shawsystems.com>
- **Date:** 1998-09-16T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<35FFAF92.8C889F72@shawsystems.com>`
- **References:** `<35FE3FF1.FF1AA088@shawsystems.com> <35fe9530.0@news1.ibm.net> <6tn0a8$52o$1@news.igs.net>`

```


Donald Tees wrote:

> [snipped discussion about projects...]

> I have yet to see one that scans Cobol programs and *BIULDS* dependency
> lists.

NetExpress does build copybook dependency lists.
```

#### ↳ Re: Micro Focus NetExpress questions

- **From:** smb@mfltdz.co.ukz (Steve Biggs)
- **Date:** 1998-09-16T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<6tnrsd$kv9@hyperion.mfltd.co.uk>`
- **References:** `<35FE3FF1.FF1AA088@shawsystems.com>`

```
kfloyd <kfloyd@shawsystems.com> wrote:
>I saw in the doc that OLE Servers have to be in a project

Hi Ken,
Small correction: COBOL OLE servers can be compiled outside of a project, 
it's only the class wizard that requires a project to be present in order 
to automatically create one.

After compiling, you can use a command line to link, such as:
cbllink -D -Re <nameofclassfile.obj> dllserver.obj

>, so my next
>thought was to do that, but keep the bulk of the other code elsewhere
…[7 more quoted lines elided]…
>so, how to set it up ?

If David Sands' tip about calling the DLL first doesn't work, try linking 
it as "Dynamic" (-R? using cbllink) which means that the DLL will use the 
registry for finding the COBOL run-time, rather than looking for COBDIR 
etc.

Steve.
Micro Focus Development.
```

##### ↳ ↳ Re: Micro Focus NetExpress questions

- **From:** kfloyd <kfloyd@shawsystems.com>
- **Date:** 1998-09-16T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<35FFB1C9.4E01C555@shawsystems.com>`
- **References:** `<35FE3FF1.FF1AA088@shawsystems.com> <6tnrsd$kv9@hyperion.mfltd.co.uk>`

```


Steve Biggs wrote:

> kfloyd <kfloyd@shawsystems.com> wrote:
> >I saw in the doc that OLE Servers have to be in a project
…[26 more quoted lines elided]…
> Micro Focus Development.

Thanks much for the pointers.  I'll give this a try.
```

###### ↳ ↳ ↳ Re: Micro Focus NetExpress questions

- **From:** "Donald Tees" <donald@willmack.com>
- **Date:** 1998-09-16T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<6tppt2$go4$1@news.igs.net>`
- **References:** `<35FE3FF1.FF1AA088@shawsystems.com> <6tnrsd$kv9@hyperion.mfltd.co.uk> <35FFB1C9.4E01C555@shawsystems.com>`

```

kfloyd wrote in message <35FFB1C9.4E01C555@shawsystems.com>...
>> kfloyd <kfloyd@shawsystems.com> wrote:

>> >thought was to do that, but keep the bulk of the other code elsewhere
>> >and do command line compiles.  But that leads to the Animator.  This is
>> >a new development effort, so Animating is vital.  I can't figure out how
>> >to set up the OLE Server project so that it will find the .DLL's I've


Don't know if this will work or not, but I had the same problem with
Fujitsu,
then I discovered that when a DLL is created, a parallel LIB is created. The
LIB contains pointers to the DLL, and is included in the link of the second
program that uses the DLL. That results in the calling program knowing the
correct name of the DLL, as well as the entry point.  Once I used that to
link,
windows was smart enough to follow the path statements.
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
