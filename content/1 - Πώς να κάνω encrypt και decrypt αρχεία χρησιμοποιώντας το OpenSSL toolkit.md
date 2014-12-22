Title: Πώς να κάνω encrypt και decrypt αρχεία χρησιμοποιώντας το OpenSSL toolkit
Date: 2014-12-19 00:01
Tags: how-to, openssl
Category: How-to
Slug: pos-mporo-na-kano-encrypt-kai-decrypt-arxeia-xrismopoiontas-to-openssl-toolkit
Author: Πάνος Γεωργιάδης

Αν είστε *fan* του [LoTR](http://el.wikipedia.org/wiki/%CE%9F_%CE%86%CF%81%CF%87%CE%BF%CE%BD%CF%84%CE%B1%CF%82_%CF%84%CF%89%CE%BD_%CE%94%CE%B1%CF%87%CF%84%CF%85%CE%BB%CE%B9%CE%B4%CE%B9%CF%8E%CE%BD), φαντάζομαι πως θα θυμάστε την σκηνή που ο Gandalf μπαίνει μέσα στο σπίτι στο Bag End και ρωτάει τον Frodo: "*Is it secret? Is it safe?*". Στην συνέχεια ο Frodo του δίνει το δαχτυλίδι μέσα σ΄ενα γραμμα. Προφανώς ρε Gandalf το δαχτυλίδι δεν είναι __ούτε secret__, __ούτε safe__. Αλλά βλέπετε, εκείνη την *μυθική* εποχή της Μέσης Γης, οι μάγοι δεν είχαν PC ή Internet. Αντίθετα σήμερα, οι μάγοι της εποχής μας είναι οι Hackers. 

The openssl program is a command line tool for using the various cryptography functions of OpenSSL’s crypto library from the shell. It can be also used for file encryption and decryption with Ciphers. To use this function we’re going to use the standard command `enc`.

*enc – Encoding with Ciphers.

Next to that we are going to select the file we want to encrypt (**or the sake of simplicity let’s call our file** `foo.bar`). This is going to be the `input file`, so we have to use the `-in` option. By the way, now it’s good timing to check some of the most used `enc` options:

* -in input file
* -out output file
* -pass pass phrase source
* -e encrypt
* -d decrypt
* -k passphrase is the next argument

Next to that, we should let OpenSSL know what kind of task we want: Encryption `-e` or Decryption `-d`. By default, the `-e` flag is used, so I am no gonna use (*less is better*). So, `-e` is optional as long as you want to encrypt the file. To encrypt the file, **a Cipher type is needed**. I am gonna use the: **aes-256-cbc**.

Ok, let’s type the passphrase (symmetric key) using the `-k` option. Let’s see, hmmm, ok I figured out, so my password is going to be `darthvader666`.

Finally, save the filename using the `-out` option. So, the overall command should look like:

```bash
openssl enc -in foo.bar -e -aes-256-cbc -k darthvader666 -out foo.bar.enc
```

If someone else try to read, open, access the file, he will be out of luck. Take a look:

```bash
cat foo.bar.enc
```


Salted__ع?I??m??????pq??FPt??'qbb????5h?m?Q??Y??d???_?rQ?Р>????
?3e?4r?{w?qu6Bf??z??ah?)??/0S?y??W??%Q?$??Ռ RTя,?$%

In order to decrypt the file, use the opposite filenames (input is output and output is input) and don’t forget the ‘-d’ option. So, that’s how it’s going to be:

```bash
openssl enc -in foo.bar.enc -d -aes-256-cbc -k darthvader666 -out foo.bar
```

And now, you are able to read the file, without jabbers.

```bash
cat foo.bar
```

This file contatins super important stuff. Use it wisely:

* FBI Password: paok
* CIA Password: mpaok

Apparently, no one uses this way. Every normal human geek uses public & private keys. But I am not normal, so there you have it.
