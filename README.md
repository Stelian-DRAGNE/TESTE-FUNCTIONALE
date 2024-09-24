# TESTE-FUNCTIONALE

FOARTE IMPORTANT !
Pentru ca testele de mai jos sa functioneze, trebuie avute in vedere urmatoarele : 
- creare cont pe site-ul https://www.mosionroata.ro/
- pe baza codurilor, este necesara completarea acestora cu informatiile marcate cu "........"
  
Proiectul are in compunere 15 teste automate.

Testele vor fi aplicate sectiunilor afisate in cadrul site-ului ales pentru testare.

Aceste teste sunt:
1.	Test verificare status pagină principală - Acest test va verifica dacă pagina principală a site-ului ales pentru testare este activă și nu returnează un cod de eroare, cel pregonizat fiind 200.
2.	Test acceptare cookie-uri pagină principală - Acest test acceptă politica de Cookie a site-ului ales pentru testare.
3.	Test scroll pe verticală pagină principală - Acest test va face Scroll pe verticală a paginii principale a site-ului ales pentru testare.
4.	Test accesare secțiunea 'DESPRE NOI' - Acest test va accesa secțiunea "DESPRE NOI", prezentă țn cadrul site-ului ales pentru testare și completarea formularului online disponibil.
5.	Test "Intra pe cont" pe site, în cont de utilizator/client creat în prealabil, verificare secțiuni disponibile, și apoi 'Logout' - În prealabil s-a creat un cont de utilizator/client, necesar ulterior în cadrul altor teste. Acest test va efectua logarea pe contul de utilizator/client, deja creat.
6.	Test funcționare caseta 'Cauta in site ...' din pagina principală - Acest test va verifica funcționalitatea casetei 'Cauta in site ...' din pagina principală a site-ului ales pentru testare.
7.	Test cautare produs 1 in caseta 'Cauta in site ...' din pagina principală și finalizare comandă - Acest test va efectua cautarea unui produs în cadrul site-ului ales pentru testare, se va accesa produsul respectiv, se configurează, se adaugă în coș și se finalizează comanda.
8.	Test cautare produs 1 in caseta 'Cauta in site ...' din pagina principală și test cautare produs 2, urmate de finalizare comandă - Acest test va efectua cautarea unui produs în cadrul site-ului ales pentru testare, se va accesa produsul respectiv, se configurează, se adaugă în coș. În continuare se va efectua cautarea unui alt produs în cadrul site-ului ales pentru testare, se va accesa produsul respectiv, se configurează, se adaugă în coș și se finalizează comanda pentru cele doua categorii de produse alese.
9.	Test sortare 'Biciclete Mountainbike' din secțiunea 'TOATE PRODUSELE' - Acest test va efectua sortarea produselor 'Biciclete Mountainbike' din secțiunea "TOATE PRODUSELE", în urma aplicării filtrelor dorite, disponibile pe pagina 'Biciclete Mountainbike'.
10.	Test accesare secțiunea 'BLOG' - Acest test va efectua accesarea secțiunii "BLOG", secțiune prezenta in cadrul site-ului ales pentru testare.
11.	Test accesare secțiunea "BRANDURI" - Acest test va prezenta lista brand-urilor comercializate de către site-ul ales pentru testare, în ordinea numărului de pagini disponibile in această secțiune a site-ului.
12.	Test accesare secțiunea "RETUR/GARANTIE" și completare Formular de Retur - Acest test va efectua accesarea și completarea formularului online cu privire la returnarea unui produs nou comandat online, produs care la primire, prezintă urme de uzura.
13.	Test accesare secțiunea "RETUR/GARANTIE" si completare Formular de Garantie - Acest test va efectua accesarea și completarea formularului online cu privire la aplicarea condițiilor de garanție comerciala asupra unui produs nou, puțin utilizat, care prezintă diverse neconcordanțe funcționale și de formă.
14.	Test accesare secțiunea "CONTACT" - Acest test va efectua accesarea secțiunii "CONTACT", secțiune prezentă în cadrul site-ului ales pentru testare și completarea formularului on-line disponibil.
15.	Test abonare la 'Newsletter' - Acest test va efectua abonarea la 'Newsletter', secțiune prezentă în cadrul site-ului ales pentru testare.
    
În cadrul unora dintre teste s-a optat pentru similaritate cu celelalte, pentru a se evidenția ceea ce se dorește a se prezenta prin intermediul respectivului test, într-o maniera cursivă și logică. Fiecare dintre teste are în compunere și assert-uri pentru diferite componente ale site-ului respectiv, presupus a fi aplicate.

In cadrul proiectului menționat mai sus, suplimentar, se prezintă și următoarele teste :
 - Testare broken-links : s-au ales 5 site-uri, și s-a testat răspunsul acestora, rezultat preconizat 200.
 - Testare Syncron pentru site-ul https://www.mosionroata.ro/.
 - Testare Asyncron pentru site-ul https://www.mosionroata.ro/ , cu răspuns 200 (True).
 - Testare Asyncron pentru site-ul https://www.mosionroata.ro/ , cu răspuns 404 (False).

