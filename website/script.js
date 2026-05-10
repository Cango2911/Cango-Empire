// Tab Switching
document.querySelectorAll('.tab-btn').forEach(btn => {
    btn.addEventListener('click', () => {
        const tabId = btn.dataset.tab;
        
        // Remove active class from all tabs and contents
        document.querySelectorAll('.tab-btn').forEach(b => b.classList.remove('active'));
        document.querySelectorAll('.tab-content').forEach(c => c.classList.remove('active'));
        
        // Add active class to clicked tab and corresponding content
        btn.classList.add('active');
        document.getElementById(tabId).classList.add('active');
    });
});

// FAQ Toggle
document.querySelectorAll('.faq-question').forEach(question => {
    question.addEventListener('click', () => {
        const faqItem = question.parentElement;
        const isActive = faqItem.classList.contains('active');
        
        // Close all FAQ items
        document.querySelectorAll('.faq-item').forEach(item => {
            item.classList.remove('active');
        });
        
        // Toggle current item
        if (!isActive) {
            faqItem.classList.add('active');
        }
    });
});

// Smooth Scrolling
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

// Form Submission
document.getElementById('contactForm')?.addEventListener('submit', (e) => {
    e.preventDefault();
    alert('Vielen Dank für deine Nachricht! Wir melden uns schnellstmöglich bei dir.');
    e.target.reset();
});

// Navbar Scroll Effect
let lastScroll = 0;
const navbar = document.querySelector('.navbar');

window.addEventListener('scroll', () => {
    const currentScroll = window.pageYOffset;
    
    if (currentScroll > 100) {
        navbar.style.boxShadow = '0 4px 20px rgba(0,0,0,0.1)';
    } else {
        navbar.style.boxShadow = '0 2px 10px rgba(0,0,0,0.1)';
    }
    
    lastScroll = currentScroll;
});

// Animate on Scroll
const observerOptions = {
    threshold: 0.1,
    rootMargin: '0px 0px -50px 0px'
};

const observer = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
        if (entry.isIntersecting) {
            entry.target.style.opacity = '1';
            entry.target.style.transform = 'translateY(0)';
        }
    });
}, observerOptions);

// Observe all cards
document.querySelectorAll('.problem-card, .solution-card, .feature-card, .package-card, .success-card, .tool-card, .blog-card, .product-card, .borsen-card').forEach(card => {
    card.style.opacity = '0';
    card.style.transform = 'translateY(20px)';
    card.style.transition = 'opacity 0.6s, transform 0.6s';
    observer.observe(card);
});

// Tool Tabs Switching
document.querySelectorAll('.tool-tab-btn').forEach(btn => {
    btn.addEventListener('click', () => {
        const category = btn.dataset.category;
        
        // Remove active class from all tabs
        document.querySelectorAll('.tool-tab-btn').forEach(b => b.classList.remove('active'));
        document.querySelectorAll('.tools-category').forEach(c => c.classList.remove('active'));
        
        // Add active class to clicked tab
        btn.classList.add('active');
        
        // Show corresponding category
        const categoryId = category === 'appsumo' ? 'appsumo-tools' : 
                          category === 'empire-tools' ? 'empire-tools-list' :
                          category === 'api-tools' ? 'api-tools-list' :
                          'ai-borsen-tools';
        document.getElementById(categoryId)?.classList.add('active');
    });
});

// Blog Category Filter
document.querySelectorAll('.blog-cat-btn').forEach(btn => {
    btn.addEventListener('click', () => {
        const category = btn.dataset.category;
        
        // Remove active class from all buttons
        document.querySelectorAll('.blog-cat-btn').forEach(b => b.classList.remove('active'));
        btn.classList.add('active');
        
        // Filter blog cards
        document.querySelectorAll('.blog-card').forEach(card => {
            if (category === 'all' || card.dataset.category.includes(category)) {
                card.style.display = 'block';
            } else {
                card.style.display = 'none';
            }
        });
    });
});

// Shop Category Filter
document.querySelectorAll('.shop-cat-btn').forEach(btn => {
    btn.addEventListener('click', () => {
        const category = btn.dataset.category;
        
        // Remove active class from all buttons
        document.querySelectorAll('.shop-cat-btn').forEach(b => b.classList.remove('active'));
        btn.classList.add('active');
        
        // Filter product cards
        document.querySelectorAll('.product-card').forEach(card => {
            if (category === 'all' || card.dataset.category === category) {
                card.style.display = 'block';
            } else {
                card.style.display = 'none';
            }
        });
    });
});

// B2C/B2B Toggle
document.querySelectorAll('.toggle-btn').forEach(btn => {
    btn.addEventListener('click', () => {
        const mode = btn.dataset.mode;
        
        // Remove active class from all buttons
        document.querySelectorAll('.toggle-btn').forEach(b => b.classList.remove('active'));
        btn.classList.add('active');
        
        // Show/hide packages
        document.getElementById('b2c-packages').style.display = mode === 'b2c' ? 'block' : 'none';
        document.getElementById('b2b-packages').style.display = mode === 'b2b' ? 'block' : 'none';
    });
});

// Newsletter Form
document.getElementById('newsletterForm')?.addEventListener('submit', (e) => {
    e.preventDefault();
    alert('Vielen Dank für deine Newsletter-Anmeldung! Du erhältst jetzt die besten AI Tools Deals.');
    e.target.reset();
});

