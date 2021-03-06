Title: Πώς να κάνω encrypt και decrypt αρχεία χρησιμοποιώντας το OpenSSL toolkit
Date: 2014-12-19 00:01
Tags: how-to, openssl
Category: How-to
Slug: pos-mporo-na-kano-encrypt-kai-decrypt-arxeia-xrismopoiontas-to-openssl-toolkit
Author: Πανος Γεωργιαδης

Ντεμπούτο του Linuxed! Αναρωτιώμουν από πού να ξεκινήσω το άρθρο μου, αλλά σήμερα νιώθω ότι έχω πολλά να πω, και θέλω να αποφύγω να ξεκινάω να σας γράφω *για το ένα και για το άλλο* και να αφήνω το σημαντικό στο τέλος. Αποφάσισα λοιπόν αντί άλλων καθυστερήσεων να μπω κατευθείαν στο κυρίως κείμενο... *με μία μικρή εισαγωγή*... 

Αν είστε *fan* του [LoTR](http://el.wikipedia.org/wiki/%CE%9F_%CE%86%CF%81%CF%87%CE%BF%CE%BD%CF%84%CE%B1%CF%82_%CF%84%CF%89%CE%BD_%CE%94%CE%B1%CF%87%CF%84%CF%85%CE%BB%CE%B9%CE%B4%CE%B9%CF%8E%CE%BD), φαντάζομαι πως θα θυμάστε την σκηνή[^1] που ο Gandalf μπαίνει μέσα στο Bag End και ρωτάει τον Frodo: "*Is it secret? Is it safe?*". Στην συνέχεια, ο Frodo επιβεβαιώνει τα λεγόμενά του, δείχνοτας πως το δαχτυλίδι παραμένει σφραγισμένο μέσα στον φάκελο. Προφανώς, για όλους εμάς, ένας φάκελος και μια σφραγίδα, δεν καλύπτουν τα σημερινα security standards. Οπότε, για όλους εμάς, το *δαχτυλίδι* δεν είναι __ούτε secret__, __ούτε safe__, αλλά βλέπετε, εκείνη την *μυθική* εποχή της *Μέσης Γης*, οι μάγοι και άλλα πλάσματα του Eru Ilúvatar, δεν είχαν PC ή Internet. Αντίθετα σήμερα, οι μάγοι της εποχής μας έχουν τα δικά τους εργαλεία και είναι γνωστοί ως Hackers.

> Αυτό όμως είναι μία ιστορία, θα πούμε άλλη φορά!

## Keep it secret, Keep it Safe

Το βασικό μου πρόβλημα ξεκίνησε όταν θέλησα να στείλω ένα αρχείο *από* τον server μου στην Ελλάδα *στο* macbook μου εδώ στην Γερμανία. Λοιπόν, για να πούμε τα πράγματα με το όνομά τους: Δεν ήταν ένα οποιοδήποτε αρχείο. Δεν μπορώ να σας πω "τι είναι" και "τι δεν είναι", καθώς η κρυφή του ταυτότητα θαρρώ πως δίνει ένα "μυστικό τόνο" στο άρθρο. Αυτό δε σημαίνει ότι είναι μυστικό και σ'εμένα, μια χαρά ξέρω "περί" ποιου αρχείου πρόκειται. Κατά μία έννοια θα μπορούσε να πει κανείς ότι κ εσείς ξέρετε, ακόμα κι αν δεν έχετε άμεση πρόσβαση στο μυαλό μου ή τον υπολογιστή μου, μπορείτε να κάνετε εικασίες. 

Καταλαβαίνετε που το πάω; Μπορεί να (μην) ξέρετε για ποιο αρχείο σας μιλάω, αλλά για όσους με ξέρουν και "το μυαλό τους πηγαίνει κατά κει", να ξέρουν οτι δεν θα το βρουν. Unsurprisingly, την ίδια μοίρα μ'εσάς, θα έχει και η Deutsche Telekom και η NSA που έχουν"έχει στήσει αφτί" αμφότεροι στο τέλος της γραμμής. Όχι, δεν μπορεί και δεν θα μπορέσει ποτέ **κανείς** να μάθει για ποιο αρχείο σας μιλάω. Μπα. Με τίποτα[^2].

Αν προσπαθείσετε να δείτε τα περιεχόμενα του αρχείου:
```bash
$ cat file 
```
θα δείτε κάτι τέτοιο:
```bash
Salted__???~?B?'?`c?g<?)/g&??????[?<???O?d?S??~?q???Ѫi??C??
                                                           "?Fz@????\pg????2?i|?f??L?>?d{?:*???????v??K?"?Y?̷?p?Z???(?Q???????*dme???Fgۦ?	??
 c??n?[Bo?r?^?;L+!?
                   %7?L?*?Qr?Plb?b{Y	/?1[?=,﹯?}8K?rP?Ņ??U????f"{Ǒ?
                                                                     ?-?&??O[????m?Qw$???҈R?(?]	??6;yQ??Wy)?FO?K?*I??URZ?l2)Xʓ????N?%??Q-??d??{??U?o
     ?ڎ?;U'?i?eR?/?R~???`???NM<?ԡ|0o=?P??9?̢j?/??
?3?v?S?o'?????۬?GM?X϶?^??OVr?"????\&L.?V8\|??b??????ՉJ?)????9;+??SC?c?㱶?]??\$?7G6??W??j??!l??$?_UO?i??H?H???
??IHq??:?M ?G??I(4??/??S:Ӷ???Z?z??????E?9'?a?(U߃D?Ny5???hD????@Z2U<?ɽ?
sx?ϴ#??????W1?'?T??|=ы?5?d?$?}?쪯YX(J/?}2?'xx?t??Q#?@?>c{{????Dd5??&?~?lBmR?
?jf?????@n?R??թG???T?I_W??(??????wQ?)q,?6M?(?w$???ᬥ???1??uxc,9(??*t1??yh??+U?? ?d??NL?8?ȴ?/?'?OLa??z?&J9DR\c??f?%??sÒu????
                                                                                                                        )s?9?f?x??E???\q???l??;?9
???!L?z?%?})?(??a?}?>_?-?_?????&???R?XQ?x??U?C7?Z?:`F)@[?W5u??je??$??$`&??3?[jF
                                                                               ¡?R??#??a??w?@ q|y6??5??*&??Vw?9}???om?a?_8??M0?!???c??h?}};گ?#?G?ĩ?	??BVJ^Ґ?V9
                  H???*W6?kE??????Ơ
                                   Zp]F86?b?8?5?8?N?,?N???1'.??1???:??%@=?I@???????'?OW?s?u?O?ꨯm??s?Mwzq???????????*?ƾx1V4???.?Ր???87??e
??ܢO?r???DՁZ?1????Y7?WQE?ְ?X?Ps??Gseݍ
8?wP?)??/%????}?`?Has?I?B?l'????+
?ۖF
   ?L? ?F?rT?)?e{?#^m!IO??0P?3????_4Kgϗ,\???D???????8;???H?q
????nTdZS???_???|\߷?t???P?
                          ?.???t?0c:=?3yney#E??D?~?5????؅????أ8% .?U?l!6&
q4$i???8?ЕP7F|Ԃ0Q????:??C???B?y??Ә*WW?j>V貺???Vi5uwyc??7%[?
???s$?N???p??\ri5xza???&l?"o@?T?몜??o#u?$H???
/O?F?"?R@n??6?o??8?:??Άf?.|?????9P??n
                                     >?`?O$*?????x????ã??)??5?D?{v???Q&?Q??????9??j	*-
                                                                                          ?Zxߚ?A?U?O?v>j?g??-?>&:??i?]??????5$a?9?U+????셴<+???k??r$O?;x:???l=?B4arp?
??B??4?@??[?3N?q??!h???g`?pJ6???뭁????N??#??q??/???>?Q??#??ҧ?Q?W?????L??5xVnلΐ
??(?"t?7???ň=?MH?O??c?sbF?@a??#?aK,?Q?q??b??Z ͊?F??g%܅??1v??$
```
Οι παραπάνω "*ασυναρτησίες*" οφείλονται στο γεγονός ότι το αρχείο είναι κρυπτογραφημένο (*encrypted*). Και ένα αρχείο, μη προσπελάσιμο, είναι τελείως άχρηστο. Για να το αποκρυπτογραφίσετε, θα πρέπει να γνωρίζετε την τέχνη του OpenSSL, καθώς και κάποια άλλα πράγματα, όπως: τον **Cipher** και το **passphrase**.

------------------

## Κρυπτογράφιση με το OpenSSL
![Keep it secret keep it safe](/images/gandalfopenssl.png "Keep it Secret, Keep it Safe")
### Βήμα 1: Ενεργοποιήστε την κατάσταση κωδικοποίησης αρχείου

The openssl program is a command line tool for using the various cryptography functions of OpenSSL’s crypto library from the shell. It can be also used for file encryption and decryption with Ciphers[^3]. Για να χρησιμοποιήσουμε αυτή την λειτουργία, αρκεί να δώσουμε την παράμετρο `enc`.

+ `enc` – Encoding with Ciphers.

### Βήμα 2: Επιλέξτε το αρχείο που θέλετε να κρυπτογραφίσετε

Στην συνέχεια θα επιλέξουμε το αρχείο που θέλουμε να κρυπτογραφίσουμε (**για λόγους ευκολίας, ας ονομάσουμε το αρχείο με το προτώτυπο όνομα που είμαι σίγουρος ότι δεν έχετε ξαναδει ποτέ μπροστά σας** `foo.bar`). Αυτό λοιπόν πρόκειται να παίξει τον ρόλο του `input file`, γεγονός που δηλώνεται με την παράμετρο `-in`. Με την ευκαιρία, ας δούμε μερικές από τις επιλογές που μπορείτε να συνδυάσετε παρέα με την παράμετρο `enc`:

* `-in` input file
* `-out` output file
* `-pass` pass phrase source
* `-e` encrypt (by default)
* `-d` decrypt
* `-k` passphrase is the next argument

### Βήμα 3: Κρυπτογράφιση ή Αποκρυπτογράφιση;

Το επόμενο βήμα είναι να ορίσουμε τι θέλουμε να κάνουμε με το αρχείο: 
+ Encryption `-e` ή
+ Decryption `-d`. 

Κάπου διάβασα, ότι η μεγαλύτερη παγίδα της σκέψης είναι αυτή του αυτονόητου, αλλά εδώ δεν χρίζει λόγος ανησυχίας. By default λοιπόν, χρησιμοποίεται η σημαία `-e`, την οποία δεν δείτε να την χρησιμοποιούν ιδιαίτερα  (*όσο λιγότερα, τόσο το καλύτερο*). Οπότε, η επιλογή `-e` είναι optional με την προϋπόθεση ότι η πρόθεσή σας είναι να κρυπτογραφίσετε το αρχείο. Για να ολοκληρώσετε την *κρυπτογράφιση* του αρχείου, το μόνο που μένει είναι να δηλώσετε άλλα δύο πράγματα:

1. Cipher (δηλαδή τον αλγόριθμο)
2. Passphrase[^4] (κλειδί)

### Βήμα 4: Επιλογή αλγορίθμου

Για να κρυπτογραφίσουμε ένα αρχείο,  **χρειαζόμαστε έναν Cipher**. Χωρίς να θέλω να πρωτοτυπήσω θα χρησιμοποιήσω τον: **aes-256-cbc**.

### Βήμα 5: Επιλογή κλειδιού

Για passphrase (symmetric key) θα χρησιμοποιήσουμε την επιλογή `-k`. Χμμμ, για να σκεφτώ... ok I figured out, το passphrase μου θα είναι `darthvader666`.

Αν και σας είπα ότι έχουμε μόνο δύο πράγματα (τον αλγόριθμο και το passphrase), η αλήθεια είναι ότι μένει κάτι ακόμα. Υποθέτω, ότι δεν φαντάζει λογικώς ορθό να κάνουμε edit ένα αρχείο και -- *at the same time* -- να το κάνουμε replace. Συνεπώς, χρειαζόμαστε ένα `output file` το οποίο θα είναι το τελικό αποτέλεσμα (δηλ. *το κρυπτογραφημένο αρχείο*). Για να το πω πιο απλά, είναι το αντίστοιχο του "**save as**". Για να το κάνουμε αυτό από γραμμή εντολών, το OpenSSL διαθέτει στο ρεπερτόριο εντολών του την επιλογή `-out`. 

Για να δούμε λίγο ολόκληρη την εντολή:

```bash
openssl enc -in foo.bar -e -aes-256-cbc -k darthvader666 -out foo.bar.enc
```

Οπότε, ακόμα κι αν κάποιος υποκλέψει το αρχείο foo.bar.enc (το `enc` απλά δηλώνει ότι το αρχείο είναι κρυπτογραφημένο. Ο λόγος που το βάζουμε είναι για να ξέρουμε εκ των πρωτέρων ότι το αρχείο είναι encrypted και τίποτε άλλο). Διαφορετικά, αν προσπαθήσει να το ανοίξει κάποιος τρίτος, θα δει "*ασυναρτησίες*".

> Παρατηρήστε το `salted` στην αρχή της πρότασης. Σημαίνει ότι το αρχείο είναι encrypted.

##  Αποκρυπτογράφιση με το OpenSSL
Η λύση για να αποκαλυφθούν τα περιεχόμενα του αρχείου βρίσκεται στην αντίστροφη λειτουργία της κρυπτογράφισης ή αλλιώς: **απο**κρυπτογράφισης (*decryption*). Αν δεν υπάρχει *κρυπτογραφημένο αρχείο*, δεν υπάρχει λόγος για *αποκρυπτογράφιση*. Αν δεν υπάρχει λόγος για αποκτυπρογράφιση, τότε γιατί ταλαιπωρούμαστε; Να σας πω γιατί ταλαιπωρούμαστε: Ταλαιπωρούμαστε, αγαπητοί μου, γιατί ως άνθρωποι του Internet, είμαστε εκτεθημένοι σε ξένα μάτια. Μάτια που βλέπουν μέσα από τα καλώδια. Αν λοιπόν, έρθει μία στιγμή στην ζωή σας (πχ δουλειά) όπου θέλετε να κρατήσετε τα *μάτια των άλλων* μακρυά από ένα συγκεκριμένο αρχείο, τότε θα χρειαστείτε όλα αυτά για τα οποία σας μιλάω σ'αυτό το άρθρο. Καλύτερα τώρα; 

Αλλα πείτε μου, ποιός ο λόγος να κρυπτογραφίσω ένα αρχείο αν δεν μπορώ να το διαβάσω *ούτε εγώ ο ίδιος* (;). Για να κάνουμε decrypt λοιπόν, αρχικά θα χρησιμοποιήσουμε τα ίδια filenames **αντίστροφα** (είσοδος -> έξοδος) καθώς επίσης και την παράμετρο `-d`. 

Για να δούμε ολόκληρη την εντολή:
```bash
openssl enc -in foo.bar.enc -d -aes-256-cbc -k darthvader666 -out foo.bar
```
Και τώρα, αν προσπαθείσετε να δείτε τα περιεχόμενα του αρχείου:

```bash
cat foo.bar
```
Θα δείτε **επιτέλους** τα περιεχόμενα και τις πληροφορίες που έκρυβε όσο ήταν κρυπτογραφημένο:

```bash
This file contatins super important stuff. Use it wisely:

* FBI Password: paok
* CIA Password: mpaok
```
## Συνοψίζοντας

Αν το όλο άρθρο σας κέντρισε το ενδιαφέρον με την κρυπτογράφιση, θα σας πρότεινα να μελετήσετε το concept των **public & private keys**. Καθώς και το αντίστοιχο course στο Coursera. Όχι, δεν σας δίνω το link[^5] γιατί βαριέμαι, αλλά γιατί περιμένω να ενεργοποιήθειτε και να ψάξετε! Run Forest! Run![^6]

[^1]: Δείτε το [βίντεο](https://www.youtube.com/watch?v=E5jdaolDq7A) στο youtube ώστε να καταλάβετε για ποια σκηνή σας μιλάω.
[^2]: Κάτι [τέτοια](http://arstechnica.com/security/2012/12/25-gpu-cluster-cracks-every-standard-windows-password-in-6-hours/) διαβάζω, και σκέφτομαι αν η χρήση του χρονικού επιρρήματος "*ποτέ*" ήταν σωστή σ'αυτή την περίπτωση. Υπερβολές!
[^3]: Για την ώρα SSLv3 και v2 θεωρούνται vulnerable (βλ. [*Exploiting Poodle SSLv3*](https://www.openssl.org/~bodo/ssl-poodle.pdf)) οπότε γενικά προτείνουμε TLS 1. Ωστόσο, η πλήρης λίστα βρίσκεται [εδώ](https://www.openssl.org/docs/apps/ciphers.html#cipher_suite_names)
[^4]: Μάθετε σχετικά με το [Συμμετρικό κλειδί](http://en.wikipedia.org/wiki/Symmetric-key_algorithm)
[^5]: ή πιο απλά, [let me google that for you](http://lmgtfy.com/?q=Coursera+Cryptography#)
[^6]: Ε, μη μου πείτε ότι δεν έχετε δει την [συγκεκριμένη σκηνή](https://www.youtube.com/watch?v=x2-MCPa_3rU) από την ταινία Forest Gump
