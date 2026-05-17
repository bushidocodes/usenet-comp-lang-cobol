[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# COBOL in containers and the cloud

_1 message · 1 participant · 2020-09_

---

### COBOL in containers and the cloud

- **From:** "dashwood" <ua-author-14501808@usenetarchives.gap>
- **Date:** 2020-09-23T21:38:01+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<ht2bkgFanumU1@mid.individual.net>`

```
PRIMA Computing, (NZ) Ltd. provides tools that migrate COBOL (from
mainframes or networked) and PowerCOBOL into Windows .Net.

We have a tool called MigTSet that will analyze your COPY Books and
create an optimized Relational Database in 3NF, generate COBOL programs
to load your new tables from the existing indexed files (PC ISAM or
VSAM/KSDS), and refactor all of the COBOL IO into a Data Access Layer
(DAL) of COBOL or C# objects.

The second major tool is called PC2N and it takes PowerCOBOL sheets
(Forms) and creates Windows Forms from them, with the PowerCOBOL
scriptlets converted into an OO COBOL Class as a code-behind for each form.

Each sheet becomes a new WinForm with its own Object Oriented
code-behind. You can also run these code-behinds through MigTSet and get
a DAL layer as described above. You end up with a Windows system running
properly on the network with everything refactored into Presentation,
Business logic, and Data Access Layers. (There is no further requirement
for PowerCOBOL; your COBOL code-behinds are full OO COBOL and can be
maintained as such.)

We have a client currently who is very interested in getting out of
PowerCOBOL. (The life of this product is nearly over and GTS don't even
mention it on their web site...) There is no PowerCOBL migration path
being offered by GTS and that's why PRIMA has provided one.

This client likes the idea of being able to use COBOL in a standard
WinForms way, running on Windows and .Net, but they also want to be able
to have it cloud based.

So, for the last couple of weeks I have been doing a certification
course online for Azure and the Cloud. (I don't want the certificate,
but I do want the knowledge... :-) It is completed now and I have moved
on to Docker and Kubernetes running under Windows but using the Windows
subsystem for Linux (WSL 2) transparently. (Docker was originally
developed for Linux, but with MS becoming much more Open Source, there
is now an excellent and seamless integration of Docker onto the Windows
platform.)

I have been amazed at how easily you can implement Docker on a desktop
and develop your containers WITHOUT needing a cloud. You can easily flip
between Windows Containers or Linux containers and it is all quite
exciting and interesting.

There are many reasons why you would use a container rather than a
Virtual Machine (VM) (not the least of which is cost, if it is cloud
based; the VMs are running 24/7, containers can spin up and down in
milliseconds on demand. Obviously, that is only one aspect and there are
still cases where you might want to use a VM...)

Anyway, our client initially was going to simply put their current
PowerCOBOL projects into separate VMs in the cloud and run them like
that. But it is horrifically expensive. (Around 300 VMs running 24/7...)

Certainly, it would allow them to keep their PowerCOBOL even if GTS
withdraws support, and it is a fairly simple "brute force" approach.

I am experimenting at the moment with converting their PowerCOBOL into
WinForms (see PC2N, above) then running the WinForms and the
code-behinds in containers in the cloud. This should be much cheaper and
removes any dependence on PowerCOBOL.

I'm trying to find a really good Windows container image and there are
over 1000 of them on Docker Hub.

It needs to be able to support COM registration and it should be able to
run SQL Server in the future... (If we get it all working we will
probably use MigTSet to get them off indexed flat files onto RDB as well...)

You can see PC2N being used to migrate a small PowerCOBOL application
(it deals with Spanish postcodes - Codigos Postales) into WinForms,
here: https://primacomputing.co.nz/videos/PC2NV41Support.mp4

So now I want to take the new WinForms application and run it from one
or more containers. (I'll figure out the actual architecture, and how I
want to distribute the application layers across one or more containers,
once I have a container image that can support it...)

I'll set it all up using Docker on the Desktop (so I'm not incurring
Cloud charges) and then I should be able to drop it into an Azure
Container Image (ACI) for the client, who is using the Azure cloud.

Now, has anybody here done anything remotely similar, running COBOL in a
container and can you give me any advice, please?

Primarily, if you can recommend a good Windows container image that will
run Fujitsu COBOL, that would be an excellent start, but any comments or
advice would be gratefully received.

Cheers,

Pete.
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
