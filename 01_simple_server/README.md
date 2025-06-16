# Δήμος Άρτας - Απλό Παράδειγμα Web Server σε Python

Ένα απλό παράδειγμα web server με το Flask που εμφανίζει μια ιστοσελίδα ελληνικού δήμου για εκπαιδευτικούς σκοπούς.

## 🎯 Τι θα μάθετε

Αυτό το παράδειγμα δείχνει:
- Πως δημιουργούμε έναν web server με Python
- Πως συνδέουμε διαφορετικές σελίδες (routes)
- Πως χρησιμοποιούμε HTML templates
- Πως στέλνουμε δεδομένα από Python στο HTML
- Πως χειριζόμαστε ελληνικό κείμενο

## 📋 Τι χρειάζεστε

- Python 3.6 ή νεότερο
- Έναν web browser (Chrome, Firefox, Safari)
- Έναν text editor

## 🚀 Οδηγίες Εγκατάστασης

### Βήμα 1: Δημιουργία Εικονικού Περιβάλλοντος (Virtual Environment)

```bash
python3 -m venv venv
```

**Τι κάνει αυτή η εντολή:**
- `python3 -m venv` = Χρησιμοποιεί το Python module για virtual environments
- `venv` = Το όνομα του φακέλου που θα δημιουργηθεί
- **Γιατί το κάνουμε:** Δημιουργεί έναν ξεχωριστό χώρο για τα Python packages του project μας, χωρίς να επηρεάσουμε το σύστημά μας

### Βήμα 2: Ενεργοποίηση του Εικονικού Περιβάλλοντος

```bash
source venv/bin/activate
```

**Τι κάνει αυτή η εντολή:**
- Ενεργοποιεί το virtual environment
- Θα δείτε `(venv)` στην αρχή της γραμμής εντολών
- Από εδώ και πέρα όλες οι εντολές Python θα τρέχουν μέσα στο virtual environment

### Βήμα 3: Εγκατάσταση των Dependencies

```bash
pip install -r requirements.txt
```

**Τι κάνει αυτή η εντολή:**
- Διαβάζει το αρχείο `requirements.txt`
- Κατεβάζει και εγκαθιστά το Flask και τα απαραίτητα packages
- Τώρα μπορείτε να χρησιμοποιήσετε `pip` (όχι `pip3`) γιατί είμαστε στο virtual environment

### Βήμα 4: Εκκίνηση του Server

```bash
python app.py
```

**Τι κάνει αυτή η εντολή:**
- Τρέχει το πρόγραμμα `app.py`
- Ξεκινάει τον web server στο http://localhost:5001

### Βήμα 5: Δείτε την Ιστοσελίδα

Ανοίξτε τον browser σας και πηγαίνετε στο: **http://localhost:5001**

## 📁 Δομή του Project

```
01_simple_server/
├── app.py              # Το κύριο πρόγραμμα (ο web server)
├── requirements.txt    # Λίστα με τα Python packages που χρειαζόμαστε
├── venv/              # Φάκελος του virtual environment (αυτόματα δημιουργημένος)
├── templates/         # Φάκελος με τα HTML αρχεία
│   ├── index.html     # Αρχική σελίδα
│   ├── services.html  # Σελίδα υπηρεσιών
│   └── contact.html   # Σελίδα επικοινωνίας
├── static/           # Φάκελος με CSS, εικόνες κ.α.
│   └── style.css     # Το αρχείο στυλ
└── README.md         # Αυτό το αρχείο με τις οδηγίες
```

## 🔍 Πως Λειτουργεί το app.py

Το `app.py` είναι το κύριο πρόγραμμα που δημιουργεί τον web server. Ας δούμε τι κάνει κάθε μέρος:

### 1. Εισαγωγή Βιβλιοθηκών
```python
from flask import Flask, render_template
```
- Εισάγουμε το Flask για να δημιουργήσουμε τον web server
- Εισάγουμε το `render_template` για να εμφανίζουμε HTML σελίδες

### 2. Δημιουργία της Εφαρμογής
```python
app = Flask(__name__)
```
- Δημιουργούμε μια νέα Flask εφαρμογή

### 3. Routes (Διαδρομές/Σελίδες)
```python
@app.route('/')
def home():
    return render_template('index.html')
```

**Τι σημαίνει αυτό:**
- `@app.route('/')` = "Όταν κάποιος επισκεφτεί την αρχική σελίδα"
- `def home():` = "Τρέξε αυτή τη συνάρτηση"
- `render_template('index.html')` = "Εμφάνισε το αρχείο index.html"

**Αντίστοιχα για τις άλλες σελίδες:**
- `/services` → εμφανίζει το `services.html`
- `/contact` → εμφανίζει το `contact.html`

### 4. Δεδομένα στις Σελίδες
```python
services_list = ["Έκδοση Πιστοποιητικών", ...]
return render_template('services.html', services=services_list)
```

**Τι κάνει:**
- Δημιουργεί μια λίστα με υπηρεσίες
- Στέλνει τη λίστα στο HTML template
- Το HTML μπορεί να εμφανίσει τα δεδομένα αυτά

## 🌐 Τι Τύπος Rendering Είναι Αυτός;

Αυτός ο server χρησιμοποιεί **SSR (Server-Side Rendering)**:

**Τι σημαίνει αυτό:**
- Όταν ζητάτε μια σελίδα, ο server δημιουργεί την HTML
- Ο server στέλνει την έτοιμη HTML στον browser σας
- Ο browser απλά την εμφανίζει

**Εναλλακτικά υπάρχει το CSR (Client-Side Rendering):**
- Ο server στέλνει JavaScript κώδικα
- Ο browser τρέχει τον κώδικα και δημιουργεί την HTML
- Π.χ. React, Vue.js applications

**Γιατί χρησιμοποιούμε SSR εδώ:**
- Είναι πιο απλό για αρχάριους
- Δεν χρειάζεται JavaScript
- Φορτώνει πιο γρήγορα

## 📝 Για το Contact Form

**Σημαντική σημείωση:** Το contact form στη σελίδα επικοινωνίας **ΔΕΝ λειτουργεί πραγματικά**.

**Τι κάνει τώρα:**
- Εμφανίζει τη φόρμα επικοινωνίας
- Όταν πατήσετε "Αποστολή", τίποτα δεν συμβαίνει

**Για να λειτουργήσει θα χρειαζόταν:**
```python
@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        # Κώδικας για να χειριστούμε τη φόρμα
        name = request.form['name']
        email = request.form['email']
        # ... κάντε κάτι με τα δεδομένα
```

## 💡 Πως Λειτουργεί ένας Web Server (Απλά)

1. **Ο Server Περιμένει:** Τρέχει συνέχεια και περιμένει αιτήματα
2. **Κάποιος Επισκέπτεται:** Browser στέλνει αίτημα (π.χ. GET /services)
3. **Ο Server Βρίσκει την Route:** Ψάχνει ποια συνάρτηση να τρέξει
4. **Εκτελεί τον Κώδικα:** Τρέχει τη συνάρτηση (π.χ. services())
5. **Δημιουργεί HTML:** Συνδυάζει template + δεδομένα
6. **Στέλνει Απάντηση:** Επιστρέφει την HTML στον browser

## 🎓 Ασκήσεις για Εκπαιδευόμενους

1. **Αλλάξτε το περιεχόμενο:** Προσθέστε περισσότερες υπηρεσίες στη λίστα
2. **Νέα σελίδα:** Δημιουργήστε μια σελίδα "Νέα" ή "Εκδηλώσεις"
3. **Αλλάξτε τα χρώματα:** Τροποποιήστε το `style.css`
4. **Προσθέστε φόρμα:** Δοκιμάστε να κάνετε το contact form να λειτουργεί

## ⚙️ Τεχνικές Λεπτομέρειες

- **Framework:** Flask 3.0.0
- **Template Engine:** Jinja2 (ενσωματωμένο στο Flask)
- **Κωδικοποίηση:** UTF-8 για ελληνικά
- **Port:** 5001 (αλλάξτε το στο app.py αν χρειάζεται)
- **Debug Mode:** Ενεργοποιημένο (ο server επανεκκινεί όταν αλλάζετε κώδικα)

## 🛑 Για να Σταματήσετε τον Server

Πατήστε `Ctrl + C` στο terminal

## 📚 Επόμενα Βήματα

Αφού καταλάβετε αυτό το παράδειγμα, μπορείτε να μάθετε:
- Databases (SQLite, PostgreSQL)
- Forms και POST requests
- User authentication
- REST APIs
- Deployment σε production server 