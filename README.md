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
`git add <αρχείο>` ή γενικά `git add -u`

### Βήμα 3: Στείλε push request
`git push`

Για στήσιμο του Pelican
=======================

Pre-render HTML
```python
make html
```

Publish to Godaddy:
```python
make rsync_upload
```


