[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# iteration using level 88 range-vars

_2 messages · 2 participants · 2002-09_

---

### iteration using level 88 range-vars

- **From:** "Torsten Reichert" <Thorsten.Reichert@dresdner-bank.com>
- **Date:** 2002-09-27T10:31:17+02:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<an140j$cus1@news-1.bank.dresdner.net>`

```
Hi everybody

Does anyone know a solution for the displaying all valid values of a split
range ?

05    RANGE-VAR-88        PIC S9(02).
        ...
        88  RANGE-A    VALUE     1 THRU  8
                                                   41 THRU 45.
        ...


    SET   RANGE-A                  TO TRUE
    MOVE RANGE-VAR-88     TO COND-VAR

    PERFORM UNTIL ???????
          DISPLAY COND-VAR
    END-PERFORM

Thank you
```

#### ↳ Re: iteration using level 88 range-vars

- **From:** Volker Bandke <vbandke@bsp-gmbh.com>
- **Date:** 2002-09-27T12:22:54+02:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<j7c8pukjc9j6iag3d8booqpt10ntuss2f7@4ax.com>`
- **References:** `<an140j$cus1@news-1.bank.dresdner.net>`

```
PERFORM VARYING I FROM -99 BY 1 UNTIL I > +99
   MOVE I TO RANGE-VAR-88
   IF RANGE-A THEN
      DISPLAY I
   END-IF
END-PERFORM



And now go and make the rest of your Homework
      
      
      
      
                                                            
     With kind Regards            |\      _,,,---,,_        
                            ZZZzz /,`.-'`'    -.  ;-;;,     
     Volker Bandke               |,4-  ) )-,_. ,\ (  `'-'   
      (BSP GmbH)                '---''(_/--'  `-'\_)        
                                                            
      Given my druthers, I'd druther not.
      
        (Another Wisdom from my fortune cookie jar)         


-----------== Posted via Newsfeed.Com - Uncensored Usenet News ==----------
   http://www.newsfeed.com       The #1 Newsgroup Service in the World!
-----= Over 100,000 Newsgroups - Unlimited Fast Downloads - 19 Servers =-----
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
