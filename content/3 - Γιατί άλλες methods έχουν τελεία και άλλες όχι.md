Title: Γιατί άλλες methods έχουν τελεία και άλλες όχι;
Date: 2015-01-04 17:41
Tags: python
Category: Python
Slug: giati-alles-methods-exoun-teleia-kai-alles-oxi
Author: Πανος Γεωργιαδης

Για παράδειγμα, έστω ότι έχουμε τις εξής `methods`:

+ `len(string)` - επιστρέφει το μήκος του string
+ `str(object)` - επιστρέφει μία απεικόνιση του object σε string
+ `string.upper()` - επιστρέφει το string με κεφαλαία γράμματα
+ `string.lower()` - επιστρέφει το string με μικρά γράμματα

```python
ministry = "The Ministry of Silly Walks"

print len(ministry)
print ministry.upper()
```

Το ερώτημα είναι γιατί άλλες από αυτές εφαρμόζονται με **dot notation** και άλλες όχι.

> Τα παρακάτω παραδείγματα είναι από το [CodeAcademy](http://www.codecademy.com/courses/python-beginner-sRXwR/1/1?curriculum_id=4f89dab3d788890003000096)

#### len()
```python
parrot = "Norwegian Blue"
print len(parrot)
```
Έξοδος: `14`

#### lower() 
```python
parrot = "Norwegian Blue"
print parrot.lower()
```
Έξοδος: `norwegian blue`

#### upper()
```python
parrot = "norwegian blue"
print parrot.upper()
```
Έξοδος: `NORWEGIAN BLUE`

#### str()
```python
pi = 3.14
print str(pi)
```
Έξοδος: `3.14`. 
Με άλλα λόγια, αυτό που κάνει είναι: `3.14` -> `"3.14"`


### Η απάντηση είναι ...
... απλή και κατατοπιστική:
Οι `methods` που χρησιμοποιούν `.` εφαρμόζονται μόνο σε `strings`, ενώ οι άλλες (*len()* και *str()*) μπορούν να εφαρμοστούν και σε άλλα **data types**.

Για παράδειγμα, σύμφωνα με το doc[^1], η `len(s)` μπορεί να λειτουργήσει και σε άλλα data types, αρκεί αυτά να είναι αποτέλεσμα ακολουθίας (*πχ string, bytes, tuple, list, ή range) ή κάτι που η python ονομάζει *collection* (πχ dictionary, set, ή frozen set).

H `str` '*επιστρέφει*' την απεικόνιση ενός *object* σε *string*. Αν της δώσεις ένα *string* τότε θα σου επιστρέψει το *ίδιο το string*. 

Η διαφορά με την `repr(object)` είναι ότι η `str(object)` δεν την ενδιαφέρει να επιστρέψει ένα *string* αποδεκτό από την `eval()`. Αυτό που την ενδιαφέρει μόνο, είναι να μετατρέψει ό,τι της δώσεις σε *string*, και *that's all*. Τελος, αν δεν της δώσεις καμία είσοδο, τότε θα επιστρέψει ένα *empty string*, δηλαδή `""`.


[^1]: https://docs.python.org/2/library/functions.html#str
