Linuxed.gr
==========

Καλώς ήρθατε στο git repository :)

Live website: [L I N U X E D](http://linuxed.gr)

Οδηγίες
=======
Αν θέλετε να γράψετε άρθρο, πηγαίνετε στον κατάλογο **content** και φτιάξε ένα `όνομα_αρχείου.md`. Σαν `όνομα_αρχείου` μπορείτε να βάλετε τον τίτλο του άρθρου, ενώ μέσα πρέπει να γράψετε σε Markdown. Φυσικά, υπάρχουν και εναλλακτικές: όπως το *ReStructured Text* της Python. Οι εικόνες μπαίνουν απευθείας στον φάκελο **content/images**.

> Ρίξτε μία ματιά στα ήδη υπάρχων άρθρα για να πάρετε μία ιδέα

### Βήμα 1: Clone repo
`git clone https://github.com/drpaneas/linuxed.gr.git`

Ναι, έτσι κάνετε download ολόκληρο το website, και μπορείτε να το διαβάζετε με όποιον editor θέλετε. Ναι, είπα την λέξη **editor** γιατί το Linuxed, δεν διαβάζεται μόνο μέσω browser. Άλλωστε το ίδιο του το όνομα προέρχεται από τον πρώτο Unix editor, που ήταν o **ed**.

### Βήμα 2: Πρόσθεσε αρχεία/αλλαγές για commit
`git add <αρχεία>

### Βήμα 3: Κάνε commit γράφοντας τι αλλάζεις
`git commit -m "Άρθρο 5"

### Βήμα 3: Στείλε push request
`git push`

Για στήσιμο του Pelican
=======================
Οδηγίες αργότερα


Για όσους θέλουν να στήσουν δικό τους Pelican Blog
==================================================
Πάω στο `linuxed` directory και ενεργοποιηώ το **virtualenv** της Python δίνοντας `. /bin/activate`
Στην συνέχεια, πάω στον φάκελο `content` και φτιάχνω ένα νέο άρθρο `vim <νούμερο άρθρου><ονομα άρθρου>.md`
Αν έχω φωτογραφίες, τις βάζω μέσα στον φάκελο `content/images/` και φροντίζω να είναι κάτω από 150 kb, με κατάληξη `jpg`.

Αφού τελειώσω το άρθρο, ήρθε η στιγμή να παράγω τις static HTML pages. Πηγαίνω ένα dir πάνω, δηλαδή στο `linuxed` και δίνω:

```python
make html
```

για να το δω προσωρινά στον localhost, δίνω:

```python
make serve
```

στην συνέχεια ανοίγω τον Chrome στην σελίδα: `localhost:8000`


Publish to Godaddy:
```python
make rsync_upload
```

Σημείωση: Για το Godaddy έχω πειράξει το `.htaccess` αρχείο ώστε να κάνει redirect τα Server Errors. Οπότε έχω επίσης πειράξει και το `Makefile`, συγκεκριμένα στην εντολή `rsync` ώστε να μην το λαμβάνει υπόψην της και το διαγράφει.

`rsync -e "ssh -p 22" -P -rvzc --delete /Users/drpaneas/Virtualenvs/linuxed/output/ drpaneas@502.acd.myftpupload.com:/var/chroot/home/content/52/10571152/html/linuxed --cvs-exclude --exclude '.htaccess'`
