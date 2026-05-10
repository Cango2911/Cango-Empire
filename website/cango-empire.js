// CanGo Empire - Modern SaaS JavaScript
// Smooth scrolling and interactions

document.addEventListener('DOMContentLoaded', function() {
    // Smooth scroll for anchor links
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener('click', function (e) {
            e.preventDefault();
            const target = document.querySelector(this.getAttribute('href'));
            if (target) {
                target.scrollIntoView({
                    behavior: 'smooth',
                    block: 'start'
                });
            }
        });
    });

    // Navbar scroll effect
    let lastScroll = 0;
    const navbar = document.querySelector('.main-nav');
    
    window.addEventListener('scroll', () => {
        const currentScroll = window.pageYOffset;
        
        if (currentScroll > 100) {
            navbar.style.boxShadow = '0 4px 6px -1px rgba(0, 0, 0, 0.1)';
        } else {
            navbar.style.boxShadow = 'none';
        }
        
        lastScroll = currentScroll;
    });

    // Load JSON data
    loadEmpireData();
});

// Load JSON data and populate content
async function loadEmpireData() {
    try {
        const response = await fetch('cango-empire-data.json');
        const data = await response.json();
        
        // Update hero section if needed
        if (data.hero_section) {
            // Content is already in HTML, but we can enhance it
            console.log('CanGo Empire data loaded:', data);
        }
        
    } catch (error) {
        console.warn('Could not load empire data:', error);
    }
}

