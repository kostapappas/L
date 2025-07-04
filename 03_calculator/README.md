# 🧮 Υπολογιστής έκδοσης πιστοποιητικών - Δήμος Άρτας

Μια απλή Flask εφαρμογή που υπολογίζει το κόστος έκδοσης πιστοποιητικών για εκπαιδευτικούς σκοπούς.

## 🎯 Στόχος της Άσκησης

Αυτή η εφαρμογή σχεδιάστηκε για να μάθουν οι σπουδαστές:
- Πως να χειρίζονται φόρμες σε Flask
- Πως να κάνουν υπολογισμούς βάσει εισόδου χρήστη
- Πως να εμφανίζουν αποτελέσματα σε HTML templates
- Πως να συνδέουν Python λογική με HTML εμφάνιση

## 📋 Προαπαιτούμενα

- Python 3.6+
- Web browser

## 🚀 Εγκατάσταση και Εκκίνηση

### 1. Δημιουργία Virtual Environment
```bash
python3 -m venv venv
source venv/bin/activate  # Linux/Mac
# ή
venv\Scripts\activate     # Windows
```

### 2. Εγκατάσταση Dependencies
```bash
pip install -r requirements.txt
```

### 3. Εκκίνηση Εφαρμογής
```bash
python3 app.py
```

### 4. Επίσκεψη στην Εφαρμογή
- **Υπολογιστής:** http://localhost:5003
- **Οδηγίες Ασκήσεων:** http://localhost:5003/οδηγιες

## 🏗️ Δομή Εφαρμογής

```
03_calculator/
├── app.py                    # Κύρια Flask εφαρμογή
├── requirements.txt          # Python dependencies
├── templates/               # HTML templates
│   ├── calculator.html      # Φόρμα υπολογισμού
│   ├── αποτελεσμα.html     # Σελίδα αποτελεσμάτων
│   └── οδηγιες.html        # Οδηγίες για σπουδαστές
├── static/
│   └── style.css           # CSS styling
└── README.md               # Αυτό το αρχείο
```

## 🔧 Πως Λειτουργεί

### Κύρια Λογική (app.py)

1. **Σταθερές:** Οι τιμές είναι εύκολα τροποποιήσιμες
   ```python
   ΒΑΣΙΚΟ_ΚΟΣΤΟΣ = 3.0
   ΚΟΣΤΟΣ_ΕΠΕΙΓΟΝ = 2.0
   ```

2. **Routes:**
   - `/` - Φόρμα υπολογισμού
   - `/υπολογισμος` - Επεξεργασία φόρμας και υπολογισμός
   - `/οδηγιες` - Οδηγίες για ασκήσεις

3. **Υπολογισμός:**
   - Βασικό κόστος: €3.00
   - Επείγον: +€2.00
   - Σύνολο εμφανίζεται με ανάλυση

### Φόρμα Εισόδου

- **Όνομα:** Κείμενο
- **Τύπος Πιστοποιητικού:** Dropdown menu
- **Επείγον:** Radio buttons

### Σελίδα Αποτελεσμάτων

- Εμφάνιση στοιχείων αίτησης
- Ανάλυση κόστους
- Επόμενα βήματα
- Πληροφορίες επικοινωνίας

## 📚 Ασκήσεις για Σπουδαστές

Επισκεφτείτε `/οδηγιες` για 3 προοδευτικές ασκήσεις:

### 🟢 Άσκηση 1: Αλλαγή Τιμών (Εύκολη)
- Αλλαγή βασικού κόστους και επείγοντος
- Χρόνος: 5 λεπτά

### 🟡 Άσκηση 2: Νέος Τύπος Πιστοποιητικού (Μέτρια)
- Προσθήκη νέου τύπου στη λίστα
- Χρόνος: 7 λεπτά

### 🔴 Άσκηση 3: Έκπτωση Συνταξιούχων (Δύσκολη)
- Νέο πεδίο φόρμας
- Λογική έκπτωσης 50%
- Αλλαγές σε 3 αρχεία
- Χρόνος: 8 λεπτά

## 💡 Εκπαιδευτικά Σημεία

### Python Concepts:
- Μεταβλητές σταθερές
- Λίστες
- Conditionals (if/else)
- String formatting
- Function definitions
- Form handling

### Flask Concepts:
- Routes και HTTP methods
- Template rendering
- Form data processing
- URL building
- Static files

### HTML/CSS:
- Forms και input types
- Template variables
- Responsive design
- Modern CSS styling

## 🚀 Επιπλέον Προκλήσεις

1. **Διαφορετικές τιμές ανά τύπο** - Κάθε πιστοποιητικό διαφορετική τιμή
2. **Πολλαπλά πιστοποιητικά** - Επιλογή ποσότητας
3. **Αποθήκευση αιτήσεων** - Σε αρχείο ή βάση δεδομένων
4. **Email notifications** - Αποστολή επιβεβαίωσης
5. **User authentication** - Login system

## 🐛 Troubleshooting

### Κοινά Προβλήματα:

1. **ModuleNotFoundError:** Βεβαιωθείτε ότι έχετε ενεργοποιήσει το virtual environment
2. **Port already in use:** Αλλάξτε το port στο app.py
3. **Template not found:** Ελέγξτε ότι τα αρχεία είναι στο σωστό φάκελο templates/
4. **CSS δεν φορτώνει:** Ελέγξτε το φάκελο static/

### Χρήσιμες Εντολές:

```bash
# Έλεγχος αν τρέχει η εφαρμογή
curl http://localhost:5003

# Σταμάτημα εφαρμογής
Ctrl + C

# Επανεκκίνηση με αλλαγές
python3 app.py
```

## 📖 Περαιτέρω Μάθηση

Μετά από αυτή την άσκηση, οι σπουδαστές μπορούν να μάθουν:
- Databases (SQLite, PostgreSQL)
- User authentication
- API development
- Testing
- Deployment
- JavaScript frontend interaction

## 🤝 Συνεισφορά

Για εκπαιδευτικούς σκοπούς - οι σπουδαστές ενθαρρύνονται να:
- Προτείνουν βελτιώσεις
- Προσθέσουν νέα features
- Φτιάξουν τη δική τους έκδοση
- Μοιραστούν τις λύσεις τους

---

**Καλή επιτυχία στον προγραμματισμό! 🚀** 