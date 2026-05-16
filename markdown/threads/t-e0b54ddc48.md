[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# alternate index in an entry sequenced data set

_1 message · 1 participant · 2001-03_

---

### Re: alternate index in an entry sequenced data set

- **From:** Volker Bandke <vbandke@bsp-gmbh.com>
- **Date:** 2001-03-18T19:33:25+01:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<0it8btsb42sh0e9mah3jvc2vp827n418jq@4ax.com>`
- **References:** `<98vlj6$tv8$1@rohrpostix.uta4you.at> <330A8E1C779A8957.924944EF936DBD4A.E2205E1033721A3B@lp.airnews.net>`

```
On Sat, 17 Mar 2001 14:05:22 -0500, SkippyPB <swiegand@neo.rr.com.nospam> wrote:


>Are you sure the file is an ESDS file?  Because by definition, an ESDS
>file does not have an index 

true

>and therefore could not possibly have 3 alternate indicies.

non sequitur, and false

A VSAM ESDS does indeed allow an alternate index.  You define the ESDS file, and specify
in the definition of the alternate index where the key in the ESDS record is located. This
key is an alternate key (possibly non-unique).  And what is the primary key?  The RBA.
VSAM maintains the relationship between alternate key and RBA in the alternate Index/path


      
      
      
      
                                                            
     With kind Regards            |\      _,,,---,,_        
                            ZZZzz /,`.-'`'    -.  ;-;;,     
     Volker Bandke               |,4-  ) )-,_. ,\ (  `'-'   
      (BSP GmbH)                '---''(_/--'  `-'\_)        
                                                            
      Fate just keeps on happening. -- Anita Loos
      
        (Another Wisdom from my fortune cookie jar)
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
