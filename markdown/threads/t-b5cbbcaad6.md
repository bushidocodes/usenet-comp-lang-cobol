[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# BlueTooth Windows API Question

_6 messages · 3 participants · 2009-01_

---

### BlueTooth Windows API Question

- **From:** bhennessey60@gmail.com
- **Date:** 2009-01-07T07:37:58-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<14a2559e-ed38-4cb5-9ea0-be5536752009@x38g2000yqj.googlegroups.com>`

```
Good Morning,

I am trying to use Windows APIs to read and write data to a bluetooth
receipt printer.

Writing to the device is working fine, but I am unable to read from
the device.

There are actually two serial communications ports involved, Port 3 is
the port I need to read from and Port 4 is the port I need to write
to.

I believe the problem is when I use the CreateFileA API to access Port
3. Instead of getting back a valid handle I am getting back the
numeric value (-1) that indicates that the port could not be opened.

I do a GetLastError API and that comes back with a numeric 2.

I believe this is caused because the port is in use by the blue tooth
device, but I tried open it as File_Share_Read and that did not help.

Any advice would be most welcomed.

Thanks,
Bob
```

#### ↳ Re: BlueTooth Windows API Question

- **From:** "Michael Mattias" <mmattias@talsystems.com>
- **Date:** 2009-01-07T09:46:47-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<X749l.440$PE4.175@nlpi061.nbdc.sbc.com>`
- **References:** `<14a2559e-ed38-4cb5-9ea0-be5536752009@x38g2000yqj.googlegroups.com>`

```
<bhennessey60@gmail.com> wrote in message 
news:14a2559e-ed38-4cb5-9ea0-be5536752009@x38g2000yqj.googlegroups.com...
> Good Morning,
>
…[19 more quoted lines elided]…
> Any advice would be most welcomed.

CreateFile/Error 2 is "The system cannot find the file specified."

File in use would normally be returned as error 5, "Access denied" or yiou 
might get the dreaded '83' "invalid parameter" if, say, the share mode is 
incompatible with other users of the device.

You sure you coded the device name corrrectly? Or, maybe you did not pick 
the correct flags/options in the CreateFile call?  (Code not shown).
```

#### ↳ Re: BlueTooth Windows API Question

- **From:** "Michael Mattias" <mmattias@talsystems.com>
- **Date:** 2009-01-07T09:49:16-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<ia49l.441$PE4.308@nlpi061.nbdc.sbc.com>`
- **References:** `<14a2559e-ed38-4cb5-9ea0-be5536752009@x38g2000yqj.googlegroups.com>`

```
Duh.

File_share_read is not enough if you are opening the file for I-O. You need 
to try File_share_read OR ( boolean or) file_share_write.
```

##### ↳ ↳ Re: BlueTooth Windows API Question

- **From:** "Pete Dashwood" <dashwood@removethis.enternet.co.nz>
- **Date:** 2009-01-08T13:04:01+13:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<6sku7fF6i0l7U1@mid.individual.net>`
- **References:** `<14a2559e-ed38-4cb5-9ea0-be5536752009@x38g2000yqj.googlegroups.com> <ia49l.441$PE4.308@nlpi061.nbdc.sbc.com>`

```
Michael Mattias wrote:
> Duh.
>
> File_share_read is not enough if you are opening the file for I-O.
> You need to try File_share_read OR ( boolean or) file_share_write.

Good job, Michael.

Pete.
```

###### ↳ ↳ ↳ Re: BlueTooth Windows API Question

- **From:** bhennessey60@gmail.com
- **Date:** 2009-01-09T13:18:38-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8b6396e8-d77d-431f-b611-55f83043bcbf@e18g2000vbe.googlegroups.com>`
- **References:** `<14a2559e-ed38-4cb5-9ea0-be5536752009@x38g2000yqj.googlegroups.com> <ia49l.441$PE4.308@nlpi061.nbdc.sbc.com> <6sku7fF6i0l7U1@mid.individual.net>`

```
On Jan 7, 7:04 pm, "Pete Dashwood"
<dashw...@removethis.enternet.co.nz> wrote:
> Michael Mattias wrote:
> > Duh.
…[8 more quoted lines elided]…
> "I used to write COBOL...now I can do anything."
```

###### ↳ ↳ ↳ Re: BlueTooth Windows API Question

- **From:** bhennessey60@gmail.com
- **Date:** 2009-01-09T13:19:36-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<ae791424-7006-4076-94db-1bffa572e372@d36g2000prf.googlegroups.com>`
- **References:** `<14a2559e-ed38-4cb5-9ea0-be5536752009@x38g2000yqj.googlegroups.com> <ia49l.441$PE4.308@nlpi061.nbdc.sbc.com> <6sku7fF6i0l7U1@mid.individual.net>`

```
Good Afternoon,

Thanks for the help.  Everything is working now.

Bob
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
