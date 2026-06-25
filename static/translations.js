const translations = {
    en: {
        instructions: "Instantly detect hidden clauses, financial traps, or misleading ad endorsements.",
        placeholder: "Paste your contract or text here...",
        btnText: "Start Intelligent Analysis",
        loading: "AI is scanning text for contractual risks... Please wait.",
        navTerms: "Terms & Conditions",
        navPrivacy: "Privacy Policy",
        navContact: "Contact",
        navGhid: "📖 User Guide & API Key",
        alertText: "Please paste text or upload a document first!",
        bifaText: "I have read, understand, and agree to the Terms of Use and Privacy Policy (GDPR).",
        blocatText: "🔒 To access upload functions and AI analysis, you must first check the box to accept the Terms above.",
        subsol: "🛡️ Contract Assistant | Owned by IULIAN ICHIM-UNGUREANU (Liak Studio)",
        c1: "<b>💡 Guidance Guide</b><br>Translates complicated contractual clauses into simple terms.",
        c2: "<b>🚩 Hidden Clauses Alert</b><br>Flags disproportionate penalties or unfair terms.",
        c3: "<b>🗣️ Negotiation Ideas</b><br>Provides you with polite arguments and wordings.",
        up_t: "Upload document (PDF, DOCX, XLSX, TXT):",
        tx_t: "Or enter text manually:",
        rap_t: "## 🔍 Contractual Audit Report",
        b_down: "📥 Download Report (.txt)",
        
        // Fereastra Pop-up pentru Contact (Rămâne în JS fiind scurtă)
  modalContactBody: `
    <p style="margin-bottom:1rem;">Have questions, feature requests, or business inquiries? Send us a direct message:</p>
    <form action="https://formspree.io/f/xbdvgpeo" method="POST" style="display:flex; flex-direction:column; gap:10px;">
        <input type="text" name="name" id="c_name" placeholder="Your Name" required style="width:100%; padding:0.6rem; background:#0b0f19; border:1px solid #334155; color:white; border-radius:4px;">
        <input type="email" name="email" id="c_email" placeholder="Your Email Address" required style="width:100%; padding:0.6rem; background:#0b0f19; border:1px solid #334155; color:white; border-radius:4px;">
        <textarea name="message" id="c_message" placeholder="Type your message here..." required style="width:100%; padding:0.6rem; background:#0b0f19; border:1px solid #334155; color:white; border-radius:4px; height:100px; padding:0.6rem; border-radius:4px;"></textarea>
        <button type="submit" style="background:#2563eb; color:white; border:none; padding:0.7rem; font-weight:bold; border-radius:4px; cursor:pointer;">Send Message</button>
    </form>
        <div id="contactSuccessMsg" style="display:none; color:#10b981; margin-top:10px; font-weight:bold;">✉️ Message sent successfully! We will get back to you shortly.</div>
        `,

        // Fereastra Pop-up pentru Ghid (Rămâne în JS fiind scurtă)
        modalGhidTitle: "User Guide & API Key Setup",
        modalGhidBody: `
            <h3>🛠️ How it works and how to use the application:</h3>
            <ol>
                <li><b>Accept Terms (Mandatory):</b> Check the GDPR confirmation box on the screen.</li>
                <li><b>Enter your API Key:</b> Enter your personal <b>Gemini API Key</b> in the input box.</li>
                <li><b>Upload the Contract:</b> Upload a file or paste text manually.</li>
                <li><b>Run the Shield:</b> Click the blue button <b>"Start Intelligent Analysis"</b>.</li>
            </ol>
            <hr>
            <h3>🔑 Step-by-Step Guide to Get a Gemini API Key (100% Free):</h3>
            <ol>
                <li>Go to the official portal: <a href="https://google.dev" target="_blank">Google AI Studio</a>.</li>
                <li>Sign in using your regular, personal <b>Gmail / Google</b> account.</li>
                <li>Click <b>"Get API key"</b> then click <b>"Create API key"</b>.</li>
                <li>Click <b>"Copy"</b> to save it and paste it back into this site!</li>
            </ol>
        `
    },
    ro: {
        instructions: "Detectează instantaneu clauzele ascunse, capcanele financiare sau reclamele mascate.",
        placeholder: "Inserează contractul sau textul aici...",
        btnText: "Pornește Analiza Inteligentă",
        loading: "AI-ul scanează textul pentru riscuri contractuale... Te rugăm să aștepți.",
        navTerms: "Termeni și Condiții",
        navPrivacy: "Politică Confidențialitate",
        navContact: "Contact",
        navGhid: "📖 Ghid de Utilizare & Cheie API",
        alertText: "Te rugăm să introduceți text sau să încarci un document mai întâi!",
        bifaText: "Am citit, înțeleg și accept în mod exprimat Termenii de Utilizare și Politica de Confidențialitate (GDPR).",
        blocatText: "🔒 Pentru a accesa funcțiile de upload și analiza AI, trebuie mai întâi să bifați căsuța de acceptare a Termenilor de mai sus.",
        subsol: "🛡️ Contract Assistant | Deținut de IULIAN ICHIM-UNGUREANU (Liak Studio)",
        c1: "<b>💡 Ghid de Îndrumare</b><br>Traduce clauzele contractuale complicate în cuvinte simple.",
        c2: "<b>🚩 Alertă Clauze Ascunse</b><br>Semnalează penalitățile disproporționate sau termenele abuzive.",
        c3: "<b>🗣️ Idei de Renegociere</b><br>Îți oferă argumente și formulări politicoase.",
        up_t: "Încarcă documentul (PDF, DOCX, XLSX, TXT):",
        tx_t: "Sau introdu textul clauzelor suspecte manual:",
        rap_t: "## 🔍 Raport de Audit Contractual",
        b_down: "📥 Descarcă Raportul (.txt)",
        
        // Fereastra Pop-up pentru Contact (RO)
        modalContactTitle: "Contact & Suport Tehnic",
        modalContactBody: `
            <p style="margin-bottom:1rem;">Aveți întrebări, sugestii de îmbunătățire sau propuneri comerciale? Trimiteți un mesaj direct:</p>
            <form onsubmit="handleContactSubmit(event)" style="display:flex; flex-direction:column; gap:10px;">
                <input type="text" id="c_name" placeholder="Numele Tău" required style="width:100%; padding:0.6rem; background:#0b0f19; border:1px solid #334155; color:white; border-radius:4px; box-sizing:border-box;">
                <input type="email" id="c_email" placeholder="Adresa ta de Email" required style="width:100%; padding:0.6rem; background:#0b0f19; border:1px solid #334155; color:white; border-radius:4px; box-sizing:border-box;">
                <textarea id="c_message" placeholder="Scrie mesajul tău aici..." required style="width:100%; height:100px; padding:0.6rem; background:#0b0f19; border:1px solid #334155; color:white; border-radius:4px; box-sizing:border-box; resize:none;"></textarea>
                <button type="submit" style="background:#2563eb; color:white; border:none; padding:0.7rem; font-weight:bold; border-radius:4px; cursor:pointer;">Trimite Mesajul</button>
            </form>
            <div id="contactSuccessMsg" style="display:none; color:#10b981; margin-top:10px; font-weight:bold;">✉️ Mesajul a fost trimis cu succes! Vă vom răspunde în cel mai scurt timp.</div>
        `,

        // Fereastra Pop-up pentru Ghid (RO)
        modalGhidTitle: "Ghid de Utilizare & Obținere Cheie API",
        modalGhidBody: `
            <h3>🛠️ Cum funcționează și cum se folosește aplicația:</h3>
            <ol>
                <li><b>Acceptarea Termenilor (Obligatoriu):</b> Bifează căsuța de confirmare GDPR de pe ecran.</li>
                <li><b>Introducerea Cheii API:</b> Introdu cheia ta personală <b>Gemini API Key</b> în căsuță.</li>
                <li><b>Încărcarea Contractului:</b> Adăugați un fișier text/PDF/Word sau folosiți introducerea manuală.</li>
                <li><b>Generarea Scutului:</b> Apasă pe butonul albastru <b>"Pornește Analiza Inteligentă"</b>.</li>
            </ol>
            <hr>
            <h3>🔑 Ghid Pas cu Pas pentru Obținerea Cheii Gemini (100% Gratuit):</h3>
            <ol>
                <li>Intră pe site-ul oficial: <a href="https://google.dev" target="_blank">Google AI Studio</a>.</li>
                <li>Conectează-te folosind contul tău personal de <b>Gmail / Google</b>.</li>
                <li>Apasă pe butonul albastru <b>"Get API key"</b> apoi pe <b>"Create API key"</b>.</li>
                <li>Apasă pe butonul <b>"Copy"</b> pentru a o salva și insereaz-o în această pagină!</li>
            </ol>
        `
    }
};

function handleContactSubmit(event) {
    event.preventDefault();
    document.getElementById('contactSuccessMsg').style.display = 'block';
    event.target.reset();
}
