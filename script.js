// Selectare elemente pentru Meniul Mobil
const hamburger = document.querySelector('.hamburger-menu');
const mobileOverlay = document.querySelector('.mobile-overlay');
const mobileLinks = document.querySelectorAll('.mobile-link');

// Funcție toggle pentru meniu
function toggleMenu() {
    hamburger.classList.toggle('active');
    mobileOverlay.classList.toggle('active');
    
    // Blochează scroll-ul pe fundal când meniul e deschis
    if (mobileOverlay.classList.contains('active')) {
        document.body.style.overflow = 'hidden';
    } else {
        document.body.style.overflow = 'auto';
    }
}

// Eveniment click pe hamburger
hamburger.addEventListener('click', toggleMenu);

// Închide meniul când se dă click pe un link din interiorul lui
mobileLinks.forEach(link => {
    link.addEventListener('click', () => {
        hamburger.classList.remove('active');
        mobileOverlay.classList.remove('active');
        document.body.style.overflow = 'auto';
    });
});

// Gestionare trimitere formular de contact
document.querySelector('.contact-form').addEventListener('submit', function(e) {
    e.preventDefault();
    const name = this.querySelector('input[type="text"]').value;
    const submitBtn = this.querySelector('.btn-submit');
    
    // Feedback vizual premium
    submitBtn.disabled = true;
    submitBtn.textContent = 'Se trimite...';
    
    setTimeout(() => {
        alert(`Mulțumim, ${name}! Mesajul tău a fost înregistrat.`);
        this.reset();
        submitBtn.disabled = false;
        submitBtn.textContent = 'Trimite Mesajul';
    }, 1200);
});

// Smooth Scroll fluid pentru legăturile interne
document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener('click', function (e) {
        e.preventDefault();
        const target = document.querySelector(this.getAttribute('href'));
        if(target) {
            target.scrollIntoView({ behavior: 'smooth', block: 'start' });
        }
    });
});
