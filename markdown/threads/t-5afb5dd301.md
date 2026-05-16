[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Validating input file

_32 messages · 9 participants · 2008-05_

---

### Validating input file

- **From:** jeff <jmoore207@gmail.com>
- **Date:** 2008-05-13T06:37:11-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<30d67234-2965-45ed-9b66-324739333c4e@a70g2000hsh.googlegroups.com>`

```
I have a input rec coming from a customer that is defined as

 FD  DISCFILE.
 01  DISC-REC               PIC X(129).
 01  DISC-REC2 REDEFINES DISC-REC.
     03  DISC-RECR OCCURS 129  PIC X.

It is a comma-delimited file with 16 fields (15 commas). I need to
check and make sure that each line is only 129 characters and I assume
1 LF. What would be the best way to accomplish this?
```

#### ↳ Re: Validating input file

- **From:** jeff <jmoore207@gmail.com>
- **Date:** 2008-05-13T07:02:32-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<c1ee2a7f-0873-495d-9277-1efd1443b91c@f36g2000hsa.googlegroups.com>`
- **References:** `<30d67234-2965-45ed-9b66-324739333c4e@a70g2000hsh.googlegroups.com>`

```
On May 13, 9:37 am, jeff <jmoore...@gmail.com> wrote:
> I have a input rec coming from a customer that is defined as
>
…[7 more quoted lines elided]…
> 1 LF. What would be the best way to accomplish this?


How can I check 130 for LF?

Can I use an evaluate? or will it be a problem because the record is
defined as 129?
```

#### ↳ Re: Validating input file

- **From:** "Rick Smith" <ricksmith@mfi.net>
- **Date:** 2008-05-13T10:10:46-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<kPGdnfI6I7HDPLTVnZ2dnUVZ_vudnZ2d@posted.mid-floridainternet>`
- **References:** `<30d67234-2965-45ed-9b66-324739333c4e@a70g2000hsh.googlegroups.com>`

```

"jeff" <jmoore207@gmail.com> wrote in message
news:30d67234-2965-45ed-9b66-324739333c4e@a70g2000hsh.googlegroups.com...
> I have a input rec coming from a customer that is defined as
>
…[7 more quoted lines elided]…
> 1 LF. What would be the best way to accomplish this?

If this is truly a fixed-length record on disk, then the
LF should appear in the last position; if the file is "line
sequential" then the SELECT clause for the file
should reflect that and the record will be filled with
trailing spaces when it is read into the program. In other
words, the record, in memory, will always have
128 characters and a LF or 129 characters, depending.
```

##### ↳ ↳ Re: Validating input file

- **From:** jeff <jmoore207@gmail.com>
- **Date:** 2008-05-13T07:19:17-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<29ae81a8-ee4c-4fdf-84c4-84baeb7f1292@e39g2000hsf.googlegroups.com>`
- **References:** `<30d67234-2965-45ed-9b66-324739333c4e@a70g2000hsh.googlegroups.com> <kPGdnfI6I7HDPLTVnZ2dnUVZ_vudnZ2d@posted.mid-floridainternet>`

```
On May 13, 10:10 am, "Rick Smith" <ricksm...@mfi.net> wrote:
> "jeff" <jmoore...@gmail.com> wrote in message
>
…[19 more quoted lines elided]…
> 128 characters and a LF or 129 characters, depending.

It is a comma delimited file and can have blank fields
```

###### ↳ ↳ ↳ Re: Validating input file

- **From:** "Rick Smith" <ricksmith@mfi.net>
- **Date:** 2008-05-13T11:22:00-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<0Zmdncv2O9qFL7TVnZ2dnUVZWhednZ2d@posted.mid-floridainternet>`
- **References:** `<30d67234-2965-45ed-9b66-324739333c4e@a70g2000hsh.googlegroups.com> <kPGdnfI6I7HDPLTVnZ2dnUVZ_vudnZ2d@posted.mid-floridainternet> <29ae81a8-ee4c-4fdf-84c4-84baeb7f1292@e39g2000hsf.googlegroups.com>`

```

"jeff" <jmoore207@gmail.com> wrote in message
news:29ae81a8-ee4c-4fdf-84c4-84baeb7f1292@e39g2000hsf.googlegroups.com...
>On May 13, 10:10 am, "Rick Smith" <ricksm...@mfi.net> wrote:
>> "jeff" <jmoore...@gmail.com> wrote in message
…[22 more quoted lines elided]…
>It is a comma delimited file and can have blank fields

With Micro Focus, I might choose the following:

        input-output section.
        file-control.
            select discfile assign to ...
                organization line sequential.

The use of "line sequential" allows the reading of variable
length lines of text. When each "line" is read, the record,
in memory, will have each of the characters from the text
"line" followed by some number of spaces to fill out the
record; but will not have the LF (or new line) separator.

What compiler are you using? That will determine how
to set up the program to read the file.
```

#### ↳ Re: Validating input file

- **From:** Howard Brazee <howard@brazee.net>
- **Date:** 2008-05-13T08:27:03-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<k89j24tkdc8hvkt9focf510rtvp889f3ps@4ax.com>`
- **References:** `<30d67234-2965-45ed-9b66-324739333c4e@a70g2000hsh.googlegroups.com>`

```
On Tue, 13 May 2008 06:37:11 -0700 (PDT), jeff <jmoore207@gmail.com>
wrote:

>I have a input rec coming from a customer that is defined as
>
…[7 more quoted lines elided]…
>1 LF. What would be the best way to accomplish this?

Are you reading an ASCII file from one Windows machine to another
Windows machine?
```

##### ↳ ↳ Re: Validating input file

- **From:** jeff <jmoore207@gmail.com>
- **Date:** 2008-05-13T07:29:57-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<f0907ddf-24fd-48d4-b115-a223125e8ec6@l64g2000hse.googlegroups.com>`
- **References:** `<30d67234-2965-45ed-9b66-324739333c4e@a70g2000hsh.googlegroups.com> <k89j24tkdc8hvkt9focf510rtvp889f3ps@4ax.com>`

```
On May 13, 10:27 am, Howard Brazee <how...@brazee.net> wrote:
> On Tue, 13 May 2008 06:37:11 -0700 (PDT), jeff <jmoore...@gmail.com>
> wrote:
…[13 more quoted lines elided]…
> Windows machine?

Unix ascii file
```

###### ↳ ↳ ↳ Re: Validating input file

- **From:** Howard Brazee <howard@brazee.net>
- **Date:** 2008-05-13T09:05:10-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<77bj24pmj0m7gmjgss1bi3oq1qtk8eip81@4ax.com>`
- **References:** `<30d67234-2965-45ed-9b66-324739333c4e@a70g2000hsh.googlegroups.com> <k89j24tkdc8hvkt9focf510rtvp889f3ps@4ax.com> <f0907ddf-24fd-48d4-b115-a223125e8ec6@l64g2000hse.googlegroups.com>`

```
On Tue, 13 May 2008 07:29:57 -0700 (PDT), jeff <jmoore207@gmail.com>
wrote:

>> Are you reading an ASCII file from one Windows machine to another
>> Windows machine?
>
>Unix ascii file

I was surprised when I used TextWrangler on the Mac to discover all
the different formats it recognized - including Mac, Windows, Unix
(Mac uses Unix) with different line-end/form-feed combinations.
Someone here will tell what Unix files expect.

I've worked on various mainframes and almost all of them handle record
length with the OS.   A fixed 80 column record is 80 columns.  Period.
It is interesting that this is from a time when space cost more, but
it gave up space in the name of speed.
```

###### ↳ ↳ ↳ Re: Validating input file

- **From:** Alain Reymond <arwebmail@skynet.be>
- **Date:** 2008-05-13T17:15:12+02:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<4829b094$0$2998$ba620e4c@news.skynet.be>`
- **In-Reply-To:** `<f0907ddf-24fd-48d4-b115-a223125e8ec6@l64g2000hse.googlegroups.com>`
- **References:** `<30d67234-2965-45ed-9b66-324739333c4e@a70g2000hsh.googlegroups.com> <k89j24tkdc8hvkt9focf510rtvp889f3ps@4ax.com> <f0907ddf-24fd-48d4-b115-a223125e8ec6@l64g2000hse.googlegroups.com>`

```


jeff a ï¿½crit :
> On May 13, 10:27 am, Howard Brazee <how...@brazee.net> wrote:
>   
…[20 more quoted lines elided]…
>   
Jeff, if you use line sequential files, you should not have to care 
about the LF. The records will be 129 chars long.
Then, use unstring :
1 my-record.
    2 my-field pic(129) occurs 16.
....

                   unstring DISC-REC
                       delimited by ";" or "," or x'09'
                       into
                            my-field(01),
                            my-field(02),
                            my-field(03),
                            my-field(04),
                            my-field(05),
                            my-field(06),
                            my-field(07),
                            my-field(08),
                            my-field(09),
                            my-field(10),
                            my-field(11),
                            my-field(12),
                            my-field(13),
                            my-field(14),
                            my-field(15),
                            my-field(16)
                   end-unstring


Regards.

Alain
```

###### ↳ ↳ ↳ Re: Validating input file

_(reply depth: 4)_

- **From:** "HeyBub" <heybub@NOSPAMgmail.com>
- **Date:** 2008-05-13T12:55:55-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gYmdnV5TZOG0S7TVnZ2dnUVZ_jKdnZ2d@earthlink.com>`
- **References:** `<30d67234-2965-45ed-9b66-324739333c4e@a70g2000hsh.googlegroups.com> <k89j24tkdc8hvkt9focf510rtvp889f3ps@4ax.com> <f0907ddf-24fd-48d4-b115-a223125e8ec6@l64g2000hse.googlegroups.com> <4829b094$0$2998$ba620e4c@news.skynet.be>`

```
Alain Reymond wrote:
> jeff a �crit :
>> On May 13, 10:27 am, Howard Brazee <how...@brazee.net> wrote:
…[50 more quoted lines elided]…
>

Or, my favored technique:

    MOVE 1 TO DISC-POINTER.
    PERFORM VARYING I FROM 1 BY 1 UNTIL I > 16
        UNSTRING DISC-REC DELIMITED BY ',' INTO MY-FIELD(I)
            WITH POINTER DISC-POINTER
    END-PERFORM
```

###### ↳ ↳ ↳ Re: Validating input file

- **From:** Howard Brazee <howard@brazee.net>
- **Date:** 2008-05-13T09:44:30-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<5qdj24pa9p2qbpfebt5kie9m0lhukh4a8q@4ax.com>`
- **References:** `<30d67234-2965-45ed-9b66-324739333c4e@a70g2000hsh.googlegroups.com> <k89j24tkdc8hvkt9focf510rtvp889f3ps@4ax.com> <f0907ddf-24fd-48d4-b115-a223125e8ec6@l64g2000hse.googlegroups.com>`

```
Do you need to verify that you only have the 16 commas?  (None of the
data contain commas)?
```

###### ↳ ↳ ↳ Re: Validating input file

_(reply depth: 4)_

- **From:** jeff <jmoore207@gmail.com>
- **Date:** 2008-05-13T08:51:02-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<2be7df4b-8e7f-41b0-8e37-974543158b89@s50g2000hsb.googlegroups.com>`
- **References:** `<30d67234-2965-45ed-9b66-324739333c4e@a70g2000hsh.googlegroups.com> <k89j24tkdc8hvkt9focf510rtvp889f3ps@4ax.com> <f0907ddf-24fd-48d4-b115-a223125e8ec6@l64g2000hse.googlegroups.com> <5qdj24pa9p2qbpfebt5kie9m0lhukh4a8q@4ax.com>`

```
On May 13, 11:44 am, Howard Brazee <how...@brazee.net> wrote:
> Do you need to verify that you only have the 16 commas?  (None of the
> data contain commas)?

I am already checking that there is 15 characters for the 16 fields.

       Validate-File-
Format.
           Read
DISCFILE
               AT END MOVE "Y" TO WS-
EOF
           End-
Read
           Perform until WS-EOF =
"Y"
                   inspect DISC-REC tallying ws-comma-
count
                   for all
","
               If WS-Comma-Count <> 15                (file has to
have 16 colums)
                   perform display-100 thru display-100-
exit
                   go to 0400-
eoj
               End-
If
               Perform Parse-The-Record  (Here I wanna check and make
sure it is not > 129)
               Read Discfile at
end
                   Move "Y" to WS-
EOF
               End-
Read
           End-
Perform.
           CLOSE
DISCFILE.
       Validate-File-Format-Exit.
Exit.
```

###### ↳ ↳ ↳ Re: Validating input file

_(reply depth: 5)_

- **From:** Howard Brazee <howard@brazee.net>
- **Date:** 2008-05-13T10:17:53-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<knfj245lecl62jf9sgsld6aufv6bp0bn21@4ax.com>`
- **References:** `<30d67234-2965-45ed-9b66-324739333c4e@a70g2000hsh.googlegroups.com> <k89j24tkdc8hvkt9focf510rtvp889f3ps@4ax.com> <f0907ddf-24fd-48d4-b115-a223125e8ec6@l64g2000hse.googlegroups.com> <5qdj24pa9p2qbpfebt5kie9m0lhukh4a8q@4ax.com> <2be7df4b-8e7f-41b0-8e37-974543158b89@s50g2000hsb.googlegroups.com>`

```
You can do an UNSTRING and see if you get anything in the 17th field.
That way everything will be where you want it if it parses correctly.
```

###### ↳ ↳ ↳ Re: Validating input file

_(reply depth: 6)_

- **From:** jeff <jmoore207@gmail.com>
- **Date:** 2008-05-13T09:21:54-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<bd42c846-c77e-4f2e-8a6b-eede42c8aaf1@e53g2000hsa.googlegroups.com>`
- **References:** `<30d67234-2965-45ed-9b66-324739333c4e@a70g2000hsh.googlegroups.com> <k89j24tkdc8hvkt9focf510rtvp889f3ps@4ax.com> <f0907ddf-24fd-48d4-b115-a223125e8ec6@l64g2000hse.googlegroups.com> <5qdj24pa9p2qbpfebt5kie9m0lhukh4a8q@4ax.com> <2be7df4b-8e7f-41b0-8e37-974543158b89@s50g2000hsb.googlegroups.com> <knfj245lecl62jf9sgsld6aufv6bp0bn21@4ax.com>`

```
On May 13, 12:17 pm, Howard Brazee <how...@brazee.net> wrote:
> You can do an UNSTRING and see if you get anything in the 17th field.
> That way everything will be where you want it if it parses correctly.

0000000003192014,0000000003192004,12,12,12,12,12,1234567890,0003,2134,123456789012,12,123456,12,0000000058616545,0000000058878010
This rec is 129

0000000003192014,0000000003192004,12,,12,12,,1234567890,0003,,123456789012,12,123456,12,0000000058616545,0000000058878010
```

###### ↳ ↳ ↳ Re: Validating input file

_(reply depth: 5)_

- **From:** "Rick Smith" <ricksmith@mfi.net>
- **Date:** 2008-05-13T12:46:06-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<oaCdnd1E2MleWLTVnZ2dnUVZ_qXinZ2d@posted.mid-floridainternet>`
- **References:** `<30d67234-2965-45ed-9b66-324739333c4e@a70g2000hsh.googlegroups.com> <k89j24tkdc8hvkt9focf510rtvp889f3ps@4ax.com> <f0907ddf-24fd-48d4-b115-a223125e8ec6@l64g2000hse.googlegroups.com> <5qdj24pa9p2qbpfebt5kie9m0lhukh4a8q@4ax.com> <2be7df4b-8e7f-41b0-8e37-974543158b89@s50g2000hsb.googlegroups.com>`

```

"jeff" <jmoore207@gmail.com> wrote in message
news:2be7df4b-8e7f-41b0-8e37-974543158b89@s50g2000hsb.googlegroups.com...
[snip]
               Perform Parse-The-Record  (Here I wanna check and make
sure it is not > 129)

Define disc-rec as pic x(256), then use
    if disc-rec (130:) <> spaces
        display "record greater than 129 characters"
    end-if
```

###### ↳ ↳ ↳ Re: Validating input file

_(reply depth: 6)_

- **From:** jeff <jmoore207@gmail.com>
- **Date:** 2008-05-13T10:03:50-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7c26098b-3c55-438e-8aa6-f33f53cf16d2@59g2000hsb.googlegroups.com>`
- **References:** `<30d67234-2965-45ed-9b66-324739333c4e@a70g2000hsh.googlegroups.com> <k89j24tkdc8hvkt9focf510rtvp889f3ps@4ax.com> <f0907ddf-24fd-48d4-b115-a223125e8ec6@l64g2000hse.googlegroups.com> <5qdj24pa9p2qbpfebt5kie9m0lhukh4a8q@4ax.com> <2be7df4b-8e7f-41b0-8e37-974543158b89@s50g2000hsb.googlegroups.com> <oaCdnd1E2MleWLTVnZ2dnUVZ_qXinZ2d@posted.mid-floridainternet>`

```
On May 13, 12:46 pm, "Rick Smith" <ricksm...@mfi.net> wrote:
> "jeff" <jmoore...@gmail.com> wrote in message
>
…[8 more quoted lines elided]…
>     end-if

I thought about that and was wondering if Cobol is going to recognize
130 as a line feed if 129 is not spaces
```

###### ↳ ↳ ↳ Re: Validating input file

_(reply depth: 7)_

- **From:** jeff <jmoore207@gmail.com>
- **Date:** 2008-05-13T10:07:31-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<b3916fe5-a2e9-4da5-8c49-deb8f68a6c09@f36g2000hsa.googlegroups.com>`
- **References:** `<30d67234-2965-45ed-9b66-324739333c4e@a70g2000hsh.googlegroups.com> <k89j24tkdc8hvkt9focf510rtvp889f3ps@4ax.com> <f0907ddf-24fd-48d4-b115-a223125e8ec6@l64g2000hse.googlegroups.com> <5qdj24pa9p2qbpfebt5kie9m0lhukh4a8q@4ax.com> <2be7df4b-8e7f-41b0-8e37-974543158b89@s50g2000hsb.googlegroups.com> <oaCdnd1E2MleWLTVnZ2dnUVZ_qXinZ2d@posted.mid-floridainternet> <7c26098b-3c55-438e-8aa6-f33f53cf16d2@59g2000hsb.googlegroups.com>`

```
On May 13, 1:03 pm, jeff <jmoore...@gmail.com> wrote:
> On May 13, 12:46 pm, "Rick Smith" <ricksm...@mfi.net> wrote:
>
…[13 more quoted lines elided]…
> 130 as a line feed if 129 is not spaces

By the way, thanks to everyone who has responded!!!!! I was waiting
for the proverbial do your own homework from somebody. Its actually
not homework. Just a little rusty. LOL
```

###### ↳ ↳ ↳ Re: Validating input file

_(reply depth: 7)_

- **From:** "Rick Smith" <ricksmith@mfi.net>
- **Date:** 2008-05-13T13:38:03-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<UMKdnYdSj_JtTLTVnZ2dnUVZ_rfinZ2d@posted.mid-floridainternet>`
- **References:** `<30d67234-2965-45ed-9b66-324739333c4e@a70g2000hsh.googlegroups.com> <k89j24tkdc8hvkt9focf510rtvp889f3ps@4ax.com> <f0907ddf-24fd-48d4-b115-a223125e8ec6@l64g2000hse.googlegroups.com> <5qdj24pa9p2qbpfebt5kie9m0lhukh4a8q@4ax.com> <2be7df4b-8e7f-41b0-8e37-974543158b89@s50g2000hsb.googlegroups.com> <oaCdnd1E2MleWLTVnZ2dnUVZ_qXinZ2d@posted.mid-floridainternet> <7c26098b-3c55-438e-8aa6-f33f53cf16d2@59g2000hsb.googlegroups.com>`

```

"jeff" <jmoore207@gmail.com> wrote in message
news:7c26098b-3c55-438e-8aa6-f33f53cf16d2@59g2000hsb.googlegroups.com...
>On May 13, 12:46 pm, "Rick Smith" <ricksm...@mfi.net> wrote:
>> "jeff" <jmoore...@gmail.com> wrote in message
…[12 more quoted lines elided]…
>130 as a line feed if 129 is not spaces

It depends on the file type defined by the ORGANIZATION
clause. Line sequential organization, in Micro Focus, Fujitsu,
et al., will not place the line feed into the record.

What the compiler, you are using, will do depends on that
compiler.
```

###### ↳ ↳ ↳ Re: Validating input file

_(reply depth: 8)_

- **From:** jeff <jmoore207@gmail.com>
- **Date:** 2008-05-13T10:42:37-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<260b2b20-1b75-464b-9228-1c9ca25edd81@r66g2000hsg.googlegroups.com>`
- **References:** `<30d67234-2965-45ed-9b66-324739333c4e@a70g2000hsh.googlegroups.com> <k89j24tkdc8hvkt9focf510rtvp889f3ps@4ax.com> <f0907ddf-24fd-48d4-b115-a223125e8ec6@l64g2000hse.googlegroups.com> <5qdj24pa9p2qbpfebt5kie9m0lhukh4a8q@4ax.com> <2be7df4b-8e7f-41b0-8e37-974543158b89@s50g2000hsb.googlegroups.com> <oaCdnd1E2MleWLTVnZ2dnUVZ_qXinZ2d@posted.mid-floridainternet> <7c26098b-3c55-438e-8aa6-f33f53cf16d2@59g2000hsb.googlegroups.com> <UMKdnYdSj_JtTLTVnZ2dnUVZ_rfinZ2d@posted.mid-floridainternet>`

```
On May 13, 1:38 pm, "Rick Smith" <ricksm...@mfi.net> wrote:
> "jeff" <jmoore...@gmail.com> wrote in message
>
…[23 more quoted lines elided]…
> compiler.

Micro-Focus

000048     SELECT
DISCFILE                                              06283165
000050         ASSIGN TO DYNAMIC
WKFILE                                 06283165
000051         ORGANIZATION IS
SEQUENTIAL                               06283165
000052         Access Mode Is
Sequential                                06283165
000053         File Status Is File-
Status.                              06283165
```

###### ↳ ↳ ↳ Re: Validating input file

_(reply depth: 9)_

- **From:** "Rick Smith" <ricksmith@mfi.net>
- **Date:** 2008-05-13T14:24:42-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<LKOdnYH-99J8QbTVnZ2dnUVZ_v_inZ2d@posted.mid-floridainternet>`
- **References:** `<30d67234-2965-45ed-9b66-324739333c4e@a70g2000hsh.googlegroups.com> <k89j24tkdc8hvkt9focf510rtvp889f3ps@4ax.com> <f0907ddf-24fd-48d4-b115-a223125e8ec6@l64g2000hse.googlegroups.com> <5qdj24pa9p2qbpfebt5kie9m0lhukh4a8q@4ax.com> <2be7df4b-8e7f-41b0-8e37-974543158b89@s50g2000hsb.googlegroups.com> <oaCdnd1E2MleWLTVnZ2dnUVZ_qXinZ2d@posted.mid-floridainternet> <7c26098b-3c55-438e-8aa6-f33f53cf16d2@59g2000hsb.googlegroups.com> <UMKdnYdSj_JtTLTVnZ2dnUVZ_rfinZ2d@posted.mid-floridainternet> <260b2b20-1b75-464b-9228-1c9ca25edd81@r66g2000hsg.googlegroups.com>`

```

"jeff" <jmoore207@gmail.com> wrote in message
news:260b2b20-1b75-464b-9228-1c9ca25edd81@r66g2000hsg.googlegroups.com...
[snip]
>Micro-Focus
>
[snip]
>000051         ORGANIZATION IS
>SEQUENTIAL                               06283165

Sequential may contain binary data and will be either
fixed length or, if variable length, will have a header
record and a length prefix for each record. This is not
typical for files containing records with CSVs.

Use ORGANIZATION LINE SEQUENTIAL.
```

###### ↳ ↳ ↳ Re: Validating input file

_(reply depth: 10)_

- **From:** "William M. Klein" <wmklein@nospam.netcom.com>
- **Date:** 2008-05-13T23:14:07+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3hpWj.726976$Gl5.273413@fe02.news.easynews.com>`
- **References:** `<30d67234-2965-45ed-9b66-324739333c4e@a70g2000hsh.googlegroups.com> <k89j24tkdc8hvkt9focf510rtvp889f3ps@4ax.com> <f0907ddf-24fd-48d4-b115-a223125e8ec6@l64g2000hse.googlegroups.com> <5qdj24pa9p2qbpfebt5kie9m0lhukh4a8q@4ax.com> <2be7df4b-8e7f-41b0-8e37-974543158b89@s50g2000hsb.googlegroups.com> <oaCdnd1E2MleWLTVnZ2dnUVZ_qXinZ2d@posted.mid-floridainternet> <7c26098b-3c55-438e-8aa6-f33f53cf16d2@59g2000hsb.googlegroups.com> <UMKdnYdSj_JtTLTVnZ2dnUVZ_rfinZ2d@posted.mid-floridainternet> <260b2b20-1b75-464b-9228-1c9ca25edd81@r66g2000hsg.googlegroups.com> <LKOdnYH-99J8QbTVnZ2dnUVZ_v_inZ2d@posted.mid-floridainternet>`

```
With Micro Focus
   ORGANIZATION IS SEQUENTIAL

can be either line sequential or record sequential - depending the compiler 
directive, SEQUENTIAL
```

#### ↳ Re: Validating input file

- **From:** "HeyBub" <heybub@NOSPAMgmail.com>
- **Date:** 2008-05-13T10:07:26-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<JPWdnUvysMkxM7TVnZ2dnUVZ_tPinZ2d@earthlink.com>`
- **References:** `<30d67234-2965-45ed-9b66-324739333c4e@a70g2000hsh.googlegroups.com>`

```
jeff wrote:
> I have a input rec coming from a customer that is defined as
>
…[7 more quoted lines elided]…
> 1 LF. What would be the best way to accomplish this?

First, look at the file with a hex editor to validate your assumptions.

The usual purpose of a comma-delimited file is to dispense with imbedded 
blanks (else the file would have been defined as fixed length in the first 
place).

I suspect the file, if really comma-delimited, will NOT be a uniform 129 
bytes.

Going back to your question, what will you do if the record is NOT 129 (or 
130) bytes?

Assuming a variable length record, made up of variable length fields, your 
code should look like:

READ DISCFILE
UNSTRING DISC-REC DELIMITED BY ',' INTO
  FIELD-1
  FIELD-2
  FIELD-3
  ...
  FIELD-15
```

##### ↳ ↳ Re: Validating input file

- **From:** jeff <jmoore207@gmail.com>
- **Date:** 2008-05-13T08:12:00-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<d9267a9c-d9ac-4fb3-9d5e-74292fd3caad@34g2000hsf.googlegroups.com>`
- **References:** `<30d67234-2965-45ed-9b66-324739333c4e@a70g2000hsh.googlegroups.com> <JPWdnUvysMkxM7TVnZ2dnUVZ_tPinZ2d@earthlink.com>`

```
On May 13, 11:07 am, "HeyBub" <hey...@NOSPAMgmail.com> wrote:
> jeff wrote:
> > I have a input rec coming from a customer that is defined as
…[31 more quoted lines elided]…
>   FIELD-15

Yeah this is the way I was leaning, Parse out to fields and have a
count
```

###### ↳ ↳ ↳ Re: Validating input file

- **From:** "HeyBub" <heybub@NOSPAMgmail.com>
- **Date:** 2008-05-13T12:51:13-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<RKudnRaX4u-SSLTVnZ2dnUVZ_jmdnZ2d@earthlink.com>`
- **References:** `<30d67234-2965-45ed-9b66-324739333c4e@a70g2000hsh.googlegroups.com> <JPWdnUvysMkxM7TVnZ2dnUVZ_tPinZ2d@earthlink.com> <d9267a9c-d9ac-4fb3-9d5e-74292fd3caad@34g2000hsf.googlegroups.com>`

```
jeff wrote:
> On May 13, 11:07 am, "HeyBub" <hey...@NOSPAMgmail.com> wrote:
>> jeff wrote:
…[36 more quoted lines elided]…
> count

No, no, no. The point I was making is that only under the weirdest cases 
would you even CARE how long the record might be.
```

##### ↳ ↳ Re: Validating input file

- **From:** Howard Brazee <howard@brazee.net>
- **Date:** 2008-05-13T09:20:32-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<racj245mje03fp7bpc21m53hl2f5jt3mla@4ax.com>`
- **References:** `<30d67234-2965-45ed-9b66-324739333c4e@a70g2000hsh.googlegroups.com> <JPWdnUvysMkxM7TVnZ2dnUVZ_tPinZ2d@earthlink.com>`

```
On Tue, 13 May 2008 10:07:26 -0500, "HeyBub" <heybub@NOSPAMgmail.com>
wrote:

>First, look at the file with a hex editor to validate your assumptions.
>
>The usual purpose of a comma-delimited file is to dispense with imbedded 
>blanks (else the file would have been defined as fixed length in the first 
>place).

Many of the PC tools export delimited files as their natural format. I
use them to create files that they can read with their spreadsheet
programs - or to read files created by their spreadsheet programs.
```

#### ↳ Re: Validating input file

- **From:** Graham Hobbs <ghobbs@cdpwise.net>
- **Date:** 2008-05-13T21:37:46-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<ibgk24pu7alnnvukmncpcrsh29fujgnh61@4ax.com>`
- **References:** `<30d67234-2965-45ed-9b66-324739333c4e@a70g2000hsh.googlegroups.com>`

```
If you've got access to REXX I'd try the following rather than messing
with Cobol and 'unknown' file inputs ..

fi = 'path/filename'
fo = 'newfilename'
do while lines (fi)
   wsin = call filein(fi)
   le = length (wsin)
   if le = 129 then do	
      call lineout fo, wsin
   end
   else do
      if le > 129 then do
         say 'am over 129, what do i do'
      end
      else do
         newle = 129 - le
         newrec = wsin||newle(spaces)  .. forget the syntax
         call lineout fo, newrec
      end
   end
end
call lineout (fi)
call lineout (fo)

.. now they're all 129 for sure.
.. if my code's OK!

Graham Hobbs


On Tue, 13 May 2008 06:37:11 -0700 (PDT), jeff <jmoore207@gmail.com>
wrote:

>I have a input rec coming from a customer that is defined as
>
…[7 more quoted lines elided]…
>1 LF. What would be the best way to accomplish this?

** Posted from http://www.teranews.com **
```

##### ↳ ↳ Re: Validating input file

- **From:** Robert <no@e.mail>
- **Date:** 2008-05-13T21:13:33-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<pjik24tegujiqe0vjie4vg1umk5uhfg985@4ax.com>`
- **References:** `<30d67234-2965-45ed-9b66-324739333c4e@a70g2000hsh.googlegroups.com> <ibgk24pu7alnnvukmncpcrsh29fujgnh61@4ax.com>`

```
On Tue, 13 May 2008 21:37:46 -0400, Graham Hobbs <ghobbs@cdpwise.net> wrote:

>If you've got access to REXX I'd try the following rather than messing
>with Cobol and 'unknown' file inputs ..
…[24 more quoted lines elided]…
>.. if my code's OK!

Procrustes (the stretcher) ..  is a figure from Greek mythology. He was a bandit from
Attica, with a stronghold in the hills outside Eleusis. There, he had an iron bed into
which he invited every passerby to lie down. If the guest proved too tall, he would
amputate the excess length; victims who were too short were stretched on the rack until
they were long enough. Nobody ever fit in the bed because it was secretly adjustable:
Procrustes would stretch or shrink it upon sizing his victims from afar. Procrustes
continued his reign of terror until he was captured by Theseus, who "fitted" Procrustes to
his own bed and cut off his head and feet 

http://en.wikipedia.org/wiki/Procrustes
```

#### ↳ Re: Validating input file

- **From:** "William M. Klein" <wmklein@nospam.netcom.com>
- **Date:** 2008-05-14T02:21:22+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<C0sWj.727942$Gl5.618335@fe02.news.easynews.com>`
- **References:** `<30d67234-2965-45ed-9b66-324739333c4e@a70g2000hsh.googlegroups.com>`

```
I am still not %100 sure exactly what you want (after reading all the thread). 
However, if you are reading in "line sequential" input and you want to verify 
that each "line" is exactly 129 characters long (before the "end-of-line 
indicators") and you are using any Micro Focus product, I believe the following 
will do:

Select DISCFILE Assign to whatever
     Organization is Line sequential ...
FD  DiscFile
       Record contains 1 to 4096 Characters   *> or any other random large 
maximum size
          Depending on WS-Char-Cnt.
> 01  DISC-REC               PIC X(129).
> 01  DISC-REC2 REDEFINES DISC-REC.
>     03  DISC-RECR OCCURS 4096  PIC X.  *> same large max
         ...
Working-Storage Section.
  ... 01 WS-Char-Cnt   Pic 9(05) Comp-5.

Procedure division.
      ...
Read DiscFile
 If WS-Char-Cnt = 129  Then
     Perform EOL-is-129
Else
    Perform Not-129-Line-Sequential
End-if

  ****

Now, if you want to do other "validation" of the fields that are comma 
delimited, you do need other approaches and if the comma delimited fields MAY 
actually be quoted fields that include embedded commas, then you REALLY will 
need to "loop thru" each byte of the record as this is a fairly complex job.
```

##### ↳ ↳ Re: Validating input file

- **From:** "Rick Smith" <ricksmith@mfi.net>
- **Date:** 2008-05-13T23:03:21-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<vtKdnZ-Tfbroy7fVnZ2dnUVZ_hqdnZ2d@mid-floridainternet>`
- **References:** `<30d67234-2965-45ed-9b66-324739333c4e@a70g2000hsh.googlegroups.com> <C0sWj.727942$Gl5.618335@fe02.news.easynews.com>`

```

"William M. Klein" <wmklein@nospam.netcom.com> wrote in message
news:C0sWj.727942$Gl5.618335@fe02.news.easynews.com...
> I am still not %100 sure exactly what you want (after reading all the
thread).
> However, if you are reading in "line sequential" input and you want to
verify
> that each "line" is exactly 129 characters long (before the "end-of-line
> indicators") and you are using any Micro Focus product, I believe the
following
> will do:
>
…[5 more quoted lines elided]…
>           Depending on WS-Char-Cnt.

RECORD VARYING DEPENDING WS-Char-Cnt

is sufficient and the record description entry need not have
an OCCURS clause.
```

#### ↳ Re: Validating input file

- **From:** Robert <no@e.mail>
- **Date:** 2008-05-13T21:35:08-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<2rik249ar0m17reesed0cle1a0qq81rnu3@4ax.com>`
- **References:** `<30d67234-2965-45ed-9b66-324739333c4e@a70g2000hsh.googlegroups.com>`

```
On Tue, 13 May 2008 06:37:11 -0700 (PDT), jeff <jmoore207@gmail.com> wrote:

>I have a input rec coming from a customer that is defined as
>
…[7 more quoted lines elided]…
>1 LF. What would be the best way to accomplish this?

move 1 to parser
perform  with test after varying word-count from 1 by 1 
  until parser greater than length of disc-rec
    unstring disc-rec delimited by ',' into a-word with pointer parser
   if  word-count not greater than 16
      move a-word to my-word (word-count)
  end-if
end-perform
if  word-count not equal to 16
    display 'wrong number of words ' word-count ' in ' disc-rec
end-if
```

#### ↳ Re: Validating input file

- **From:** Robert <no@e.mail>
- **Date:** 2008-05-14T00:11:29-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<95sk24dvp3dor42vvmao01l4vhefe7s301@4ax.com>`
- **References:** `<30d67234-2965-45ed-9b66-324739333c4e@a70g2000hsh.googlegroups.com>`

```
On Tue, 13 May 2008 06:37:11 -0700 (PDT), jeff <jmoore207@gmail.com> wrote:

>I have a input rec coming from a customer that is defined as
>
…[7 more quoted lines elided]…
>1 LF. What would be the best way to accomplish this?

awk -F, 'NF!=16' filename

If you want to be more professional

awk -F, 'NF!=16 {print "'Bad record. Bad BAD record. " NF " " $0; exit 1}' filename
```

##### ↳ ↳ Re: Validating input file

- **From:** "Michael Mattias" <mmattias@talsystems.com>
- **Date:** 2008-05-14T08:38:24-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<6YBWj.4368$nW2.2122@nlpi064.nbdc.sbc.com>`
- **References:** `<30d67234-2965-45ed-9b66-324739333c4e@a70g2000hsh.googlegroups.com> <95sk24dvp3dor42vvmao01l4vhefe7s301@4ax.com>`

```
>
>>I have a input rec coming from a customer that is defined as
…[8 more quoted lines elided]…
>>1 LF. What would be the best way to accomplish this?


Something is wrong here.  If the record always has 129 characters, then it 
does not need to be delimited... unless - and I find this unlikely  - the 
sum of the lengths of all 16 fields is always the same.

That said, you might do better to define the input file as ..

  SELECT thefile
     organization sequential    (meaning 'record sequential' not 'line 
sequential')

FD TheFile
 01  X    PIC X (01).


Read the file a byte at a time. Buffer it up, counting commas and characters 
until you hit LineFeed. Then you have your first logical record, its length 
and comma count, and do whatever.

And no whining about "slow" ok?  You're the one with the weird set of 
conditions, so deal with it.

Personally -"If I *KNEW* the file is LF-delimited **AND** running on unix or 
could otherwise (eg compiler directive) define the record separator 
character as linefeed  I'd just call the file's organization LINE SEQUENTIAL 
and read one logical record at a time into a buffer that was both defined as 
variable lengh (RECORD CONTAINS 0 TO MANY CHARACTERS DEPENDING ON...) and 
"more than big enough to handle any malformed record."


MCM
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
