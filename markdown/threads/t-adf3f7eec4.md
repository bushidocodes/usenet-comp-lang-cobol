[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# JAVA calling COBOL DLL's

_1 message · 1 participant · 1999-02_

---

### Re: JAVA calling COBOL DLL's

- **From:** Don Braffitt <braffitt@ma.ultranet.com>
- **Date:** 1999-02-05T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<36BB66B2.74845F5F@ma.ultranet.com>`
- **References:** `<36BA23CE.F697D934@pwgsc.gc.ca>`

```
> I have been trying to call a cobol DLL from a java program. Can
> anyone help me ?
> I am using Micro focus Cobol and JAVA 1.1.7. Any advice would be
> helpful

I tried something similar with DIGITAL COBOL on DIGITAL UNIX.
I have not tried this same example with Micro Focus COBOL.

========================================================================

class jni5 {
  public static native long   jni5long(long arg1);
  public static native String jni5string(String arg1);

  static {
    System.loadLibrary("jni5");
  }

  public static void main (String[] args) {
    System.out.println("Java JNI5 long   = " +
Long.toString(jni5long(1)));
    System.out.println("Java JNI5 string = " + jni5string("Str1"));
  }
}
========================================================================

#include "jni5.h"
#include <stdio.h>
#include <string.h>
void JNI5COBLONG(long *arg1);
void JNI5COBSTRING(char *arg1);

JNIEXPORT jlong JNICALL Java_jni5_jni5long (JNIEnv *env, jclass this,
    jlong arg1) {
  long retlong;
  retlong = arg1;
  printf("C    JNI5 long   = %d (before call to COBOL)\n", retlong);
  JNI5COBLONG(&retlong);
  printf("C    JNI5 long   = %d (after  call to COBOL)\n", retlong);
  return retlong;
}

JNIEXPORT jstring JNICALL Java_jni5_jni5string (JNIEnv *env, jclass
this,
    jstring arg1) {
  const char *tmp = (*env)->GetStringUTFChars(env, arg1, 0);
  char retstring[100];
  strcpy(retstring, tmp);
  printf("C    JNI5 string = %s (before call to COBOL)\n", retstring);
  JNI5COBSTRING(retstring);
  printf("C    JNI5 string = %s (after  call to COBOL)\n", retstring);
  (*env)->ReleaseStringUTFChars(env, arg1, tmp);
  return (*env)->NewStringUTF(env, retstring);
}
========================================================================

       identification division.
       program-id. JNI5COBLONG.
       environment division.
       data division.
       linkage section.
       01 llong pic s9(9) comp.
       procedure division using llong.
       p1.  add 1 to llong.
            exit program.
       end program JNI5COBLONG.

       identification division.
       program-id. JNI5COBSTRING.
       environment division.
       data division.
       working-storage section.
       01 wloc pic 9(9) comp.
       linkage section.
       01 lstring pic x(100).
       procedure division using lstring.
       p2.  call "FINDNULL" using lstring wloc.
            move "2" to lstring(4:1).
            exit program.
       identification division.
       program-id. FINDNULL.
       environment division.
       data division.
       working-storage section.
       01 wsub pic x(100).
       linkage section.
       01 lstring pic x(100).
       01 wloc pic 9(9) comp.
       procedure division using lstring wloc.
       p3.  unstring lstring delimited by "h" into wsub count in wloc.
            exit program.
       end program FINDNULL.
       end program JNI5COBSTRING.
========================================================================

javac jni5.java
javah -jni jni5
cc -c jni5c.c
cobol -ansi -c -names upper jni5cob.cob
ld -shared -no_archive jni5c.o jni5cob.o \
  -L/usr/shlib/osf.1 -lcob -lcurses -lFutil -lots2 -lots \
  -L/usr/lib/libisam.a -L/usr/lib/libtps_stub.a -lsort -lexc -lm -lc \
  -o libjni5.so
setenv LD_LIBRARY_PATH \
  /usr/shlib:/usr/users/braffitt/jni5
java  jni5
========================================================================

C    JNI5 long   = 1 (before call to COBOL)
C    JNI5 long   = 2 (after  call to COBOL)
Java JNI5 long   = 2
C    JNI5 string = Str1 (before call to COBOL)
C    JNI5 string = Str2 (after  call to COBOL)
Java JNI5 string = Str2
========================================================================

- Don Braffitt
  DIGITAL COBOL project leader
  Compaq Computer Corporation
  don.braffitt@compaq.com
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
