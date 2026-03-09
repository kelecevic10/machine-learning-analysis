# Klasifikacija Fontova na osnovu Slika Karaktera

Ovaj projekat se bavi analizom, pretprocesiranjem i klasifikacijom karaktera različitih fontova koristeći mašinsko učenje.

## 📊 Podaci

Ulazni podaci su velikog memorijskog zauzeća (**1.1 GB**) i, zajedno sa pretprocesiranim podacima, izostavljeni su iz repozitorijuma (`.gitignore`) zbog ograničenja GitHub-a.

### Uputstvo za preuzimanje i postavku:
1.  **Izvor podataka:** [UCI Machine Learning Repository - Character Font Images](https://archive.ics.uci.edu/dataset/417/character+font+images)
2.  **Postupak:** Preuzmite podatke i raspakujte ih u direktorijum `data/raw`.
3.  **Očekivani rezultat:** Unutar `data/raw` treba da se nalazi **153 .csv fajla** (uzorci karaktera za različite fontove).

**Napomena:** Svi dalji oblici i transformacije podataka biće generisani direktno iz priloženih Jupyter sveski.


## 📁 Struktura `src` direktorijuma

Projekat je organizovan modularno kako bi se lakše upravljalo resursima i analizom:

* **`models/`** – Sadrži celokupne implementacije svih 5 modela i njihove pojedinačne evaluacije.
* **`preprocessing/`** – Direktorijum namenjen učitavanju, strukturnoj analizi, pretprocesiranju, PCA redukciji i vizualizaciji.
* **`analysis.ipynb`** – Glavni notebook sa sveobuhvatnom analizom problema, poređenjem modela i finalnim rezultatima.
* **Utility klase:**
    * `load_processed.py`: Pomoćna klasa za učitavanje procesiranih podataka.
    * `results_manager.py`: Upravljanje rezultatima i metrikama radi čistije implementacije.



## ⚙️ Pipeline i Reprodukcija

Da biste reprodukovali rezultate, pratite redosled izvršavanja u `preprocessing/` direktorijumu:

1.  **`01_load_preview.ipynb`** – Učitavanje raw podataka, analiza strukture, definisanje skupa feature-a i klasifikacionog problema.
2.  **`02_preprocessing.ipynb`** – Strukturna obrada i čuvanje podataka u `data/processed/preprocessed.npz`.
3.  **`03_pca.ipynb`** – Implementacija PCA redukcije. Rezultat se čuva u `data/processed/pca_preprocessed.npz`.
4.  **`04_data_visualization.ipynb`** – 2D i 3D vizualizacija procesiranih podataka radi boljeg razumevanja strukture.

Nakon pretprocesiranja, mogu se pokrenuti modeli u `models/` direktorijumu. Svaki model obuhvata:
* Model-specific procesiranje.
* Treniranje i predikciju.
* Metodološku analizu rezultata.


## 📈 Rezultati i Evaluacija

Svi rezultati su sistematizovani u `results/` direktorijumu:
* **Trenirani modeli:** Skladišteni kao `model.pkl` u `results/ime_modela/` kako bi se uštedelo vreme pri ponovnom pokretanju.
* **Metrike:** Osnovne metrike se čuvaju u `metrics.json`.
* **Detaljne analize:** Dodatni podaci analize se čuvaju u `.csv` fajlovima.

Finalno poređenje svih modela nad istim metrikama vrši se u svesci `src/analysis.ipynb`.


## 💡 Izazovi

Glavni izazov tokom rada bila je **veličina skupa podataka**. Vreme treniranja, memorijska velicina modela i manipulacija velikim fajlovima direktno su uslovili ovakvu modularnu strukturu projekta, omogućavajući efikasno istraživanje i skalabilnost.