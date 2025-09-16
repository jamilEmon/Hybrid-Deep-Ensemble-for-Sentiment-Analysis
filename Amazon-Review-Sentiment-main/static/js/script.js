// ===== Highlight prediction results with colors =====
document.addEventListener('DOMContentLoaded', function() {
    const sentiments = document.querySelectorAll('.sentiment');
    sentiments.forEach(span => {
        const li = span.parentElement;
        const text = span.textContent.trim().toLowerCase(); // clean whitespace & lowercase

        if(text === 'positive'){
            li.classList.add('sentiment-positive');
        } 
        else if(text === 'negative'){
            li.classList.add('sentiment-negative');
        }

        li.style.fontWeight = 'bold';
    });
});
