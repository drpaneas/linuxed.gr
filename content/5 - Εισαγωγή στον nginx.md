Title: Εισαγωγή στον Nginx
Date: 2015-01-022 23:19
Tags: nginx, server
Category: Nginx
Slug: eisagogi-ston-nginx
Author: Πανος Γεωργιαδης

Σε αυτό το άρθρο θα μιλήσουμε για τον Nginx[^1] HTTP Webserver (ω ναι, υπάρχουν κι άλλοι webservers πέρα από τον *Apache*). Όταν λέω ότι θα κάνουμε μία εισαγωγή, εννοώ ότι θα ξεκινήσουμε την εξερεύνηση απαντώντας σε κάποια από τα βασικά ερωτήματα, όπως:

+ Σε τι διαφέρει από τον Apache;
+ Ποια είναι να χαρακτηριστικά του;
+ Γιατί να ασχοληθούμε μαζί του;

Καταρχάς, ο Nginx δεν είναι καινούριος. Υπάρχει εδώ και αρκετό καιρό στην *πιάτσα*, συγκεκριμένα το dev ξεκίνησε το 2002 και το 2004 κυκλοφόρισε η πρώτη του έκδοση. Ωστόσο το τελευταίο διάστημα
βλέπω ότι έχει αρχίζει να τραβάει πάνω του αρκετή προσοχή. Μάλιστα, **δεν είναι λίγοι** εκείνοι που έκαναν την μετάβαση από τον "Βασιλιά Των Webservers" (*βλ.* Apache) στον Nginx. Παρόλα αυτά, ο Apache εξακολουθεί να κρατάει σταθερά τα ηνία του HTTP, αφού κατέχει περίπου το 50-75% των webservers του Internet. Το ερώτημα, λοιπόν, είναι:

## Γιατί να ασχοληθεί κανείς με τον Nginx
Σαν κλασσικός σπασίκλας, θα σας κάνω *quote* από την Wikipedia:

> Nginx is an open source reverse proxy server for HTTP, HTTPS, SMTP, POP3, and IMAP protocols, as well as a load balancer, HTTP cache, and a web server.

### Ωραία και; Γιατί να μην βάλω Apache;
Η πιο λογική ερώτηση είναι γιατί να μην ασχοληθεί κανείς με τον Apache; Μία σκέψη που θα μπορούσε να πει κάποιος είναι: "Εδώ το μισό Internet σερβίρει... *σε εμένα θα "κολλήσει";* "
Καταρχάς μην πάσχετε από *Argumentum ad populum*[^2]. Κατά δεύτερον, η διαφορά του Nginx με τον Apache, είναι ότι ο Nginx **κάνει τα ίδια πράγματα, αλλά με τα "διαφορετικό τρόπο"**. Τώρα θα μου πείτε, τι εννοείς λέγοντας "*διαφορετικό*"; Είναι "*καλύτερος*"; Είναι "*χειρότερος*";

Well, in this context I mean . . . 

> διαφορετικός τρόπος = πολλές φορές καλύτερος από τον Apache

Για να το πω πιο τεχνικά, ο **Nginx διαφέρει από τον Apache στον τρόπο που χειρίζεται τα requests**. Ας αρχίζουμε όμως με τον Apache, ο οποίος μεταχειρίζεται (by default) τα *requests* όπως και η κάρτα γραφικών, δηλαδή: παράλληλα και σε `threads`. Το μοντέλο αυτό θα το ακούσετε και αλλιώς ως `process-oriented`. Με απλά λόγια, σημαίνει ότι: για 1 connection κάνει generate τουλάχιστον 1 thread, και φυσικά ο σκοπός είναι να τα επεξεργάζεται (όλα αυτά τα) threads παραλληλα. Πολύ έξυπνο! Πάντα ήμουν *fan* του parallel thread processing, αλλά πριν βιαστείτε δώσετε ±1, πρέπει πρώτα να σκεφτείτε ποια είναι τα πλεονεκτήματα και τα μειονεκτήματα αυτού του μοντέλου. 

Ένα από τα **μειονεκτήματα** είναι το γεγονός ότι αν έχουμε μπόλικο static content, δηλ. πολλά αρχεία,
τότε αρχίζει και καταλαμβάνει περισσότερη μνήμη από το κανονικό, και αυτό το φαινόμενο συνεχίζει να επιδεινώνεται μέχρι να τερματίσει το εκάστωτε session.

Από την άλλη μεριά, ο Nginx δεν λειτουργεί με αυτόν τον τρόπο. Χρησιμοποιεί έναν `asynchronous event-handler` και με αυτόν
διαχειρίζεται τα requests. Αυτό σημαίνει ότι, ακόμα κι αν μεταχειρίζεται τις εισερχόμενες connections ως ανεξάρτητες μεταξύ τους, 
τις επιτρέπει να **μοιράζονται**, να κάνουν share, το memory space. Αυτό το γεγονός επιτρέπει στον Nginx να αποδίδει πολύ καλά
κάτω υπό συνθήκες μεγάλου φόρτου. Και στην πραγματικότητα, αυτός είναι ο πιο σημαντικός λόγος για τον οποίον αρκετοί
προτιμούν τον Nginx έναντι του Apache. Με τον Apache webserver, μπορείτε να *σερβίρετε* **ταυτόχρονα/παράλληλα** μερικές
εκατοντάδες connections, οι οποίες όμως εξαρτώνται "αρκετά" από τα hardware resources, και συγκεκριμένο τον χώρο και την μνήμη
που διαθέτει το μηχάνημα. Ειδικά τώρα που τα περισσότερα websites φορτώνουν διάφορα CMS, όπως Wordpress ή Drupal, το καθένα
από αυτά είναι αρκετά βαρύ και μπορεί να γίνει ακόμα πιο βαρύ προσθέτοντας διάφορα plugin. Συνεπώς, μην σας παραξενεύει
ότι το VPS των 5 Ευρώ που νοικιάζετε, με 128mb RAM, Apache και Wordpress, αρχίζει να *σέρνεται* σε ώρες **αιχμής**. Σε αντίθεση,
ο Nginx μπορεί να ανταπεξέλθει εξυπηρετώντας (όχι εκατοντάδες, αλλά) χιλιάδες connections με μικρότερη ή τουλάχιστον ίδια μνήμη,
χωρίς να έχει πρόβλημα με τις sessions.

## Nginx Features
Ο Nginx έχει ένα κάρο χαρακτηριστικά, αλλά θα σταθούμε στα πιο σημαντικά, ενώ θα τα συγκρίνουμε και με τα αντίστοιχα του Apache.

+ **Διαχειρίζεται static files, index files, και κάνει auto indexing**: Το ίδιο και ο Apache, πάμε παρακάτω...
+ **Reverse proxy with caching**: Το ίδιο μπορεί να γίνει και στον Apache, αλλά απαιτεί επιπλέον modules
+ **Load balancing**: Το ίδιο κάνει και ο Apache, αλλά θέλει plugin, ενώ ο Nginx το κάνει έχει built-in ;)
+ **Support fault tolerance**: Σας επιτρέπει να κάνετε configure πολλούς nodes που θα μοιρίζονται το ίδιο session state στην μνήμη μεταξύ τους. Δεν υπάρχει κάτι αντίστοιχο για τον Apache.
+ **OpenSSL Support (including SNI και OCSP stapling)**: Αυτό είναι σημαντικό γιατί όπως είδατε πρόσφατα[^3], το *SSL* είναι πλέον το πιο *trendy* στόχαστρο των hackers. Οπότε, υποστηρίζοντας τα *latest and greatest* της κρυπτογραφίας, *ίσως* είναι καλύτερο.
+ **FastCGI, PHP-FPM και SCGI Support**: Στην ουσία είναι modules που προσδίδουν την δυνατότητα εκτέλεσης scripts (*πχ* php), τα οποία μπορεί να κάνουν ο,τιδήποτε μας έρθει στο κεφάλι, αλλά αυτά που συναντάμε συνήθως έχουν να κάνουν με τα κλασσικά πράγματα που απασχολούν τον *web development*, όπως πχ το *authetication*.
+ **Fully IPv6**: Υποστηρίζει πλήρως το IPv6. Το ίδιο και ο Apache αλλά με module, μετά την έκδοση 2.2
+ **Websockets και HTTP/1.1**: Αναμενόμενο και για τους δύο, αφού είναι webserver.
+ **Live stream file compression**: Ιδανικό για video streaming. Ο Apache δεν διαθέτει κάτι ανάλογο.
+ **URL Redirects και rewriting**: Ψωμοτύρι για τους webservers, πάμε παρακάτω...
+ **Bandwidth Throttling**: Υποστηρίζεται και στον Apache μέσω modules, ενώ στον nginx είναι απλά μία ρύθμιση το base configuration file.
+ **Geolocation of IP**: Από τις πιο *sexy* τεχνολογίες του Nginx, όπου σου παρέχει έναν τρόπο να κάνεις διαχείριση των IP σε σχέση με την τοποθεσία τους. Χρησιμοποιείται κυρίως για CDNs[^4] που *σερβίρουν* static content.
+ **ΠΟΛΥ Λίγη μνήμη**: Όπως είπαμε και πριν, μπορεί να διαχειριστεί **10.000 ταυτόχρονες συνδέσεις με μόλις 2.5mb μνήμης** χωρίς πρόβλημα στο keep-alive πάρα-δώσε που έχουν οι sessions για να παραμένουν ανοιχτές.

## Είναι η νέα γενιά των webservers
Όπως ξέρουμε τα πράγματα σήμερα, ο Apache είναι ο Βασιλιάς των Webserbers, σερβίροντας το Internet
στα πιάτα των περισσότερων ανθρώπων. Ωστόσο, όσο το Internet of Things αρχίζει να μπαίνει όλο και
περισσότερο στην ζωή μας, η ανάγκη για *better perfomance* γίνεται όλο και πιο επιτακτική. Σκεφτείτε
πόσες συσκευές χρησιμοποιούμε στην καθημεριμενότητά μας, και πόσες από αυτές χρησιμοποιούν δίκτυο: TV, Smart-Watch, Smartphones, Keyboards, Tablets κλπ είναι λογικό λοιπόν, αφού αυξάνονται οι clients
να αυξάνονται και τα connections προς τους servers. Σκεπτόμενοι ότι ο *average Joe* θέλει να 
έχει άμεση πρόσβαση στο περιεχόμενό του, είναι ανυπόμονος και θέλει να του σερβίρουν (server) το φαγητό (web) "*τώρα*", τότε τουλάχιστον 2 πράγματα είναι ξεκάθαρα ότι θα χρειαστούμε:

1. Μείωση του Response Time
2. Περισσότερες παράλληλες συνδέσεις

Για την ώρα λοιπόν, όσο η ανάγκη για το Internet of Things μεγαλώνει, τόσο μεγαλύτερη
διαφήμιση θα αποκτά ο Nginx.

[^1]: Προφέρεται "engine" "X"
[^2]: Σύνδρομο της Αγγέλης ([περισσότερα](http://el.wikipedia.org/wiki/%CE%A3%CF%8D%CE%BD%CE%B4%CF%81%CE%BF%CE%BC%CE%BF_%CF%84%CE%B7%CF%82_%CE%B1%CE%B3%CE%AD%CE%BB%CE%B7%CF%82))
[^3]: Αναφέρομαι στο Heartbleed bug
[^4]: CDN είναι μία ομάδα από webnodes, που σου σερβίρουν περιεχόμενο με βάση το που βρίσκεσαι (την γεωγραφική σου τοποθεσία). Δηλαδή επιλέγουν να σου στείλουν το content από τον server που βρίσκεται πιο κοντά
σου.
