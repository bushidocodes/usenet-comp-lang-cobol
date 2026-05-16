[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# ACE - the ghost of COBOL past...

_1 message · 1 participant · 2010-03_

---

### ACE - the ghost of COBOL past...

- **From:** "Pete Dashwood" <dashwood@removethis.enternet.co.nz>
- **Date:** 2010-03-07T13:42:56+13:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7vgb4iF1tcU1@mid.individual.net>`

```
I noted in passing a little while back that I have some old procedural COBOL 
code I am prepared to give away.

It is a system I wrote originally to allow mainframe platform independence 
(ACE systems can run on any mainframe because it implemented a vestigial 
glimmering of the concept of layered software (it was before "Objects" 
became available in COBOL, so it couldn't implement "objects and layers", 
but it is highly modular and that was about as close as I could get 25 years 
ago.)

I had it running quite successfully on IBM system 360/370 mainframes and 
actually transported a system which was developed to use it to an ICL 1900, 
where, somewhat to my surprise, it also worked very well. (The IBM system 
was running Taskmaster as its TP monitor and the ICL system was using 
Driver. ACE was very compatible with both of these Monitors. It was also 
working on another IBM system running IMS/DB/DC without problem.)

A few years after PCs became established (I see some of the code dated 1988) 
I decided to see if it could be moved to the PC platform. (As it was 
designed to be movable, it theoretically should have been easy. )

At that time I was using Micro Focus COBOL on a Win 3.1 platform. I remember 
spending a few weeks getting it to compile and run properly, but eventually 
it did, and the first application I built with it was for a garment retailer 
in Sydney. A feature of that system was that hand held Psion PDAs with bar 
code readers were used to manage inventory (some of the stock was sold 
directly off the back of a truck ... :-)) and each night the Psions were 
connected to the PC and everything was processed by the application system 
developed to run under ACE. This was pretty heady stuff for the time. The 
problem was that Psions could only hold information for about 60 seconds 
when a battery was being changed, so if you didn't get the battery changed 
in time, you lost data.This happened a couple of times and kind of dampened 
the success of the overall project... :-)

I was writing a monthly column for an Australian computer magazine at the 
time and the magazine ran an article about GRIP (the Garment Retailers 
Inventory Processing outlined above.) To my astonishment, there were a 
number of enquiries from people who weren't interested in GRIP, but were 
very interested in a HIERARCHICAL database system which was provided by ACE. 
I think some of this was a bit of a backlash against the Evangelism of 
Relational Database that was taking off at the time, and, as far as I 
remember, there was no IMS/DB equivalent available for PCs.

ACE provides a platform independent hierarchic database called HAM 
(Hierarchic Access Method) which is strongly modelled on IBM's IMS/DB, using 
root segments with dependent segments attached to any number of levels, and 
the possibility to remember position in a tree structure across dequeue 
boundaries (using ACE). If you are familiar with using Segment Search 
Arguments in IMS you will have no problem at all with HAM. HAM is NOT 
mandatory; it is a default. You can use whatever DB system you want to. 
Transfer is in terms of a COBOL record layout, and is managed by the ACE 
data management phase, "DATAMAN".

On the TP (Teleprocessing) side ACE provides task management, storage 
management, security, and serial reusability. It implements a Scratch Pad 
Area (SPA) that is terminal dependent (equivalent to the DFHCOMM area in 
CICS). You write your application (in COBOL) and when you are ready to 
display a screen you set an indicator in the ACE SPA. You write the screen 
(using an ACE call - the Presentation layer is completely separated from the 
Business Logic, just like the DB is...), passing it the data buffer which 
can be MFS, BMS or PC formatted. This is a thread dequeue boundary. Instead 
of waiting for the user to press ENTER (as a standard COBOL accept would), 
your thread is suspended and resources are used for other work. (In fact, in 
the PC environment, an ACE module that drives the screen IS waiting for an 
accept, but it is completely independent of your program logic.) Typically, 
your program could be running on a server and dealing with several screens, 
each at a different stage of the process. As dequeue boundaries are reached 
for one thread, another gets processed, with ACE controlling the task 
switching. When the user finally presses ENTER, the screen driver module 
formats the screen data into a buffer which is an exact duplicate of an IMS 
Message Format Services buffer (MFS) (or, you can have it generated as a 
CICS BMS buffer - they are pretty much identical... if you feel more 
comfortable with that) and ACE reactivates your task and presents it with 
the screen buffer.  (The buffer contains the AID byte and attributes 
preceding each field, as you would expect in a mainframe environment. The 
attributes are dynamically modifiable to the extent that the PC environment 
permits, and it has all been written to use the same attribute values that 
would be used by an IBM 3270...). The indicator you set before dequeueing 
tells your application program where to resume, so a series of screens for a 
process will be processed in a series of dequeues and re-enters. Obviously, 
because the SPA is terminal dependent, each of these process threads runs 
independently of the others, with a single copy of the COBOL program being 
"serially reused".

Applications in this environment are called "phases" and each phase contains 
links to the ACE system so it can use ACE for presentation and data 
management (plus some other ancilliary services like debugging and screen 
painting.)

ACE Phases written in COBOL can run on a PC or mainframe with identical user 
interfaces. It is a vindication of the idea of tiered or layered software 
separating business logic from presentation and data services. (And it was 
written in procedural COBOL, 25 years ago...)

In its day, ACE had some good successes. I suppose the biggest one was a 
major Bank which used it to move from VSAM to IMS (the actual underlying DB 
is unimportant, as the ACE data manager (DATAMAN) can utilise whatever is 
required. Data transfer is in terms of a COBOL record and this is all that 
the application phase "sees". HAM is simply a default if you have no other 
preferred DB.), and then a few years later, from IMS to DB2. It was very 
well received by programmers.

Alistair and Philip have asked for a copy and I have been doing my best to 
locate the source code. It is spread over a couple of notebooks (one of 
which runs Windows 3.1 :-)) I have finally managed to get it into a single 
directory where I can zip it up and mail it. Theoldest notebook has no USB 
ports, and the next oldest one (Windows 98) has a single one. The CD drives 
on both of them are either not working or won't accept modern CDs, the 
serial modem that each would require for internet connection is buried in a 
box somewhere and I no longer have a dial-up provider anyway :-). It was 
kind of spooky when I unearthed the oldest machine and wiped away the layer 
of dust. The screen supports are broken and I was worried it would not 
display, but I finally found a suitable power connector and tried it. It 
came up and the quality of the sound on it is better than my current 
top-of-the-range Sony VAIO... :-). I connected it with a cable to the second 
oldest machine and used a flash drive on the second machine to collect data 
laplinked from the Win 3.1 machine...

In the course of finding this stuff I came across some little nuggets that 
are buried in it. There are a number of date routines and  one that deals 
with periods (last week, last month, last year, yesterday, today, tomorrow, 
etc. so that these terms can be used on screens and recognised in programs). 
There is code to convert to and from Hex... and God knows what else... :-)

OK, if any of the above has moved any of you to think you'd like to do some 
tinkering, I am making the ACE source available for free (there is quite a 
lot of it...) and will provide it as a zip file to interested parties. I 
haven't tried recompiling any of it into a modern environment so I have no 
idea whether it will work or not. There may be some Micro Focus specific 
code in there, I honestly don't remember and I'm certainly not going to 
search through all the code. I know I wrote a Programming manual for it, but 
I cannot find it and have done extensive searches on both of the old 
notebooks. You'll have to get by on the comments in the code and a couple of 
specific documents that are in there. If enough people get into this, I'll 
allocate some time to it and see if  can produce an overview or more details 
on using it.

If anybody makes any money out of it, please give me some... :-) otherwise, 
you're pretty much free to do what you like with it.

Formal details by private mail. I'm not posting this to the web site because 
I want to maintain contact with anyone who gets it.

Pete.
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
