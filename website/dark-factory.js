// Dark Factory JavaScript
// Interaktive Verbindungslinien und Animationen

// ============================================
// n8n Webhook & API Konfiguration
// ============================================
const N8N_CONFIG = {
    // TODO: Ersetze diese URLs mit deinen echten n8n Webhook-URLs
    webhookBaseUrl: 'https://your-n8n-instance.com/webhook',
    endpoints: {
        newsFeed: '/news-feed',        // Für "Mehr Artikel laden"
        leadSubmission: '/lead-submit', // Für Lead-Formulare
        analytics: '/analytics'         // Für Analytics-Tracking (optional)
    }
};

// Helper: n8n Webhook aufrufen
async function callN8NWebhook(endpoint, data) {
    const url = N8N_CONFIG.webhookBaseUrl + endpoint;
    try {
        const response = await fetch(url, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify(data)
        });
        
        if (!response.ok) {
            throw new Error(`HTTP error! status: ${response.status}`);
        }
        
        return await response.json();
    } catch (error) {
        console.error('n8n Webhook Error:', error);
        return null;
    }
}

// Helper: Google Analytics Event tracken
function trackGAEvent(eventName, eventParams) {
    if (typeof gtag !== 'undefined') {
        gtag('event', eventName, eventParams);
    }
}

// Canvas für Verbindungslinien
const canvas = document.getElementById('connectionCanvas');
if (canvas) {
    const ctx = canvas.getContext('2d');
    canvas.width = window.innerWidth;
    canvas.height = window.innerHeight;
    
    // Tool Nodes für Verbindungen
    const nodes = [
        { x: 100, y: 200, tool: 'Perplexity' },
        { x: 300, y: 200, tool: 'n8n' },
        { x: 500, y: 200, tool: 'OpenAI' },
        { x: 700, y: 200, tool: 'Kie AI' },
        { x: 900, y: 200, tool: 'Opus Clip' },
        { x: 1100, y: 200, tool: 'Yapper' },
    ];
    
    // Zeichne Verbindungslinien
    function drawConnections() {
        ctx.clearRect(0, 0, canvas.width, canvas.height);
        ctx.strokeStyle = 'rgba(0, 240, 255, 0.3)';
        ctx.lineWidth = 2;
        
        for (let i = 0; i < nodes.length - 1; i++) {
            ctx.beginPath();
            ctx.moveTo(nodes[i].x, nodes[i].y);
            ctx.lineTo(nodes[i + 1].x, nodes[i + 1].y);
            ctx.stroke();
            
            // Animierte Punkte auf Linien
            const progress = (Date.now() / 1000) % 1;
            const x = nodes[i].x + (nodes[i + 1].x - nodes[i].x) * progress;
            const y = nodes[i].y + (nodes[i + 1].y - nodes[i].y) * progress;
            
            ctx.fillStyle = 'rgba(0, 240, 255, 0.8)';
            ctx.beginPath();
            ctx.arc(x, y, 4, 0, Math.PI * 2);
            ctx.fill();
        }
        
        requestAnimationFrame(drawConnections);
    }
    
    drawConnections();
    
    // Resize Handler
    window.addEventListener('resize', () => {
        canvas.width = window.innerWidth;
        canvas.height = window.innerHeight;
    });
}

// B2C/B2B Toggle
document.querySelectorAll('.toggle-btn').forEach(btn => {
    btn.addEventListener('click', () => {
        const mode = btn.dataset.mode;
        
        document.querySelectorAll('.toggle-btn').forEach(b => b.classList.remove('active'));
        btn.classList.add('active');
        
        document.getElementById('b2c-product').style.display = mode === 'b2c' ? 'block' : 'none';
        document.getElementById('b2b-product').style.display = mode === 'b2b' ? 'block' : 'none';
    });
});

// Tool Node Hover Effects
document.querySelectorAll('.tool-node').forEach(node => {
    node.addEventListener('mouseenter', function() {
        this.style.transform = 'translateY(-10px) scale(1.05)';
    });
    
    node.addEventListener('mouseleave', function() {
        this.style.transform = 'translateY(0) scale(1)';
    });
});

// Cluster Animation
const observerOptions = {
    threshold: 0.2,
    rootMargin: '0px'
};

const observer = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
        if (entry.isIntersecting) {
            entry.target.style.opacity = '1';
            entry.target.style.transform = 'translateY(0)';
        }
    });
}, observerOptions);

document.querySelectorAll('.cluster').forEach(cluster => {
    cluster.style.opacity = '0';
    cluster.style.transform = 'translateY(50px)';
    cluster.style.transition = 'opacity 0.6s, transform 0.6s';
    observer.observe(cluster);
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
document.getElementById('deploymentForm')?.addEventListener('submit', (e) => {
    e.preventDefault();
    alert('DEPLOYMENT REQUEST INITIATED. Wir melden uns innerhalb von 24 Stunden.');
    e.target.reset();
});

// Navbar Scroll Effect
let lastScroll = 0;
const navbar = document.querySelector('.dark-nav');

window.addEventListener('scroll', () => {
    const currentScroll = window.pageYOffset;
    
    if (currentScroll > 100) {
        navbar.style.background = 'rgba(0, 0, 0, 0.98)';
        navbar.style.boxShadow = '0 4px 20px rgba(0, 0, 0, 0.5)';
    } else {
        navbar.style.background = 'rgba(0, 0, 0, 0.95)';
        navbar.style.boxShadow = 'none';
    }
    
    lastScroll = currentScroll;
});

// Affiliate Link Tracking
document.querySelectorAll('[data-affiliate]').forEach(link => {
    link.addEventListener('click', function(e) {
        const affiliateId = this.dataset.affiliate;
        // Hier kann später Affiliate-Tracking implementiert werden
        console.log('Affiliate Link clicked:', affiliateId);
    });
});

// Market Card Animations
document.querySelectorAll('.market-card').forEach(card => {
    card.addEventListener('mouseenter', function() {
        const icon = this.querySelector('.market-icon');
        if (icon) {
            icon.style.transform = 'scale(1.2) rotate(5deg)';
            icon.style.transition = 'transform 0.3s';
        }
    });
    
    card.addEventListener('mouseleave', function() {
        const icon = this.querySelector('.market-icon');
        if (icon) {
            icon.style.transform = 'scale(1) rotate(0deg)';
        }
    });
});

// Typing Effect für Hero Headline (optional)
function typeWriter(element, text, speed = 100) {
    let i = 0;
    element.textContent = '';
    
    function type() {
        if (i < text.length) {
            element.textContent += text.charAt(i);
            i++;
            setTimeout(type, speed);
        }
    }
    
    type();
}

// System Requirements Checklist Management
function initSystemRequirements() {
    const checklistItems = document.querySelectorAll('.checklist-item');
    const requiredCount = document.querySelectorAll('.status-indicator.red').length;
    const activatedCount = document.querySelectorAll('.status-indicator.green').length;
    const pendingCount = requiredCount - activatedCount;
    
    // Update counts
    const requiredCountEl = document.getElementById('required-count');
    const activatedCountEl = document.getElementById('activated-count');
    const pendingCountEl = document.getElementById('pending-count');
    
    if (requiredCountEl) requiredCountEl.textContent = requiredCount;
    if (activatedCountEl) activatedCountEl.textContent = activatedCount;
    if (pendingCountEl) pendingCountEl.textContent = pendingCount;
    
    // Update status message
    const statusMessage = document.getElementById('status-message');
    if (statusMessage) {
        if (pendingCount === 0) {
            statusMessage.className = 'status-message system-ready';
            statusMessage.innerHTML = '<p>🟢 <strong>System Ready:</strong> Alle erforderlichen Komponenten sind aktiviert. Ihre Node kann gestartet werden.</p>';
        } else {
            statusMessage.className = 'status-message';
            statusMessage.innerHTML = `<p>🔴 <strong>Systemstopp:</strong> Bitte erwerben Sie ${pendingCount} weitere erforderliche Lizenzen, um Ihre Node zu aktivieren.</p>`;
        }
    }
    
    // Add click handlers for requirement links with fallback logic
    document.querySelectorAll('.req-action-link').forEach(link => {
        link.addEventListener('click', function(e) {
            const affiliateId = this.dataset.affiliate;
            const fallbackUrl = this.dataset.fallback;
            const primaryUrl = this.href;
            
            // Check if AppSumo deal is available (you can implement API check here)
            // For now, use primary URL if available, otherwise fallback
            if (affiliateId) {
                console.log('Affiliate Link clicked:', affiliateId);
                // Here you can add analytics tracking and fallback logic
                // Example: Check deal status and use appropriate URL
            }
        });
    });
}

// Load JSON data and populate owned assets
async function loadEmpireData() {
    try {
        const response = await fetch('dark-factory-data.json');
        const data = await response.json();
        
        // Highlight owned assets
        if (data.intelligence_grid && data.intelligence_grid.clusters) {
            data.intelligence_grid.clusters.forEach(cluster => {
                cluster.tools.forEach(tool => {
                    if (tool.is_owned_ltd) {
                        const toolNode = document.querySelector(`[data-tool="${tool.name}"]`);
                        if (toolNode) {
                            toolNode.classList.add('owned-asset');
                            // Add owned badge if not already present
                            if (!toolNode.querySelector('.tool-badge-owned')) {
                                const badge = document.createElement('div');
                                badge.className = 'tool-badge-owned';
                                badge.textContent = tool.badge || 'OWNED ASSET';
                                toolNode.insertBefore(badge, toolNode.firstChild);
                            }
                        }
                    }
                });
            });
        }
        
        // Update live metrics from JSON
        if (data.hero_terminal && data.hero_terminal.live_metrics) {
            const metrics = data.hero_terminal.live_metrics;
            // Metrics are already in HTML, but we can update them dynamically if needed
        }
        
    } catch (error) {
        console.warn('Could not load empire data:', error);
    }
}

// Simulate requirement activation (for demo purposes)
function activateRequirement(requirementId) {
    const item = document.querySelector(`[data-requirement="${requirementId}"]`);
    if (item) {
        const indicator = item.querySelector('.status-indicator');
        if (indicator.textContent === '🔴') {
            indicator.textContent = '🟢';
            indicator.className = 'status-indicator green';
            initSystemRequirements(); // Recalculate
        }
    }
}

// News Feed Filter Functionality
function initNewsFilter() {
    const filterTabs = document.querySelectorAll('.filter-tab');
    const newsCards = document.querySelectorAll('.news-card');
    
    filterTabs.forEach(tab => {
        tab.addEventListener('click', () => {
            // Remove active class from all tabs
            filterTabs.forEach(t => t.classList.remove('active'));
            // Add active class to clicked tab
            tab.classList.add('active');
            
            const niche = tab.dataset.niche;
            
            // Filter news cards
            newsCards.forEach(card => {
                if (niche === 'all' || card.dataset.niche === niche) {
                    card.style.display = 'flex';
                    card.style.animation = 'fadeIn 0.5s ease';
                } else {
                    card.style.display = 'none';
                }
            });
        });
    });
}

// Load More News Functionality
function initLoadMoreNews() {
    const loadMoreBtn = document.getElementById('loadMoreNews');
    if (loadMoreBtn) {
        loadMoreBtn.addEventListener('click', async () => {
            console.log('Loading more news from n8n workflows...');
            loadMoreBtn.textContent = 'Lädt...';
            loadMoreBtn.disabled = true;
            
            try {
                // API call to n8n workflow endpoint
                const currentNiche = document.querySelector('.news-tab.active')?.dataset.niche || 'all';
                const currentCount = document.querySelectorAll('.news-card:not([style*="display: none"])').length;
                
                const response = await callN8NWebhook(N8N_CONFIG.endpoints.newsFeed, {
                    niche: currentNiche,
                    offset: currentCount,
                    limit: 10
                });
                
                if (response && response.articles && response.articles.length > 0) {
                    // Artikel werden hier dynamisch eingefügt
                    // Das HTML-Rendering sollte entsprechend implementiert werden
                    console.log('News loaded:', response.articles);
                    
                    // Track event
                    trackGAEvent('news_load_more', {
                        niche: currentNiche,
                        articles_loaded: response.articles.length
                    });
                    
                    alert(`${response.articles.length} weitere Artikel geladen!`);
                } else {
                    alert('Aktuell sind alle verfügbaren Artikel angezeigt. Neue Artikel werden automatisch von unseren n8n Workflows generiert.');
                }
            } catch (error) {
                console.error('Error loading news:', error);
                // Fallback: Info-Meldung
                alert('Weitere Artikel werden automatisch von unseren n8n Workflows generiert und hier angezeigt.');
            } finally {
                loadMoreBtn.textContent = 'Mehr Artikel laden';
                loadMoreBtn.disabled = false;
            }
        });
    }
}

// Upgrade Area Category Tabs
function initUpgradeCategoryTabs() {
    const categoryTabs = document.querySelectorAll('.category-tab');
    const categories = document.querySelectorAll('.upgrade-category');
    
    categoryTabs.forEach(tab => {
        tab.addEventListener('click', () => {
            // Remove active class from all tabs and categories
            categoryTabs.forEach(t => t.classList.remove('active'));
            categories.forEach(c => {
                c.classList.remove('active');
                c.style.display = 'none';
            });
            
            // Add active class to clicked tab
            tab.classList.add('active');
            
            // Show corresponding category
            const categoryId = `category-${tab.dataset.category}`;
            const category = document.getElementById(categoryId);
            if (category) {
                category.classList.add('active');
                category.style.display = 'block';
            }
        });
    });
}

// Lead Form Handling
function initLeadForms() {
    const leadForms = document.querySelectorAll('.lead-form');
    
    leadForms.forEach(form => {
        form.addEventListener('submit', async (e) => {
            e.preventDefault();
            
            const submitButton = form.querySelector('button[type="submit"]');
            const originalButtonText = submitButton?.textContent || 'Absenden';
            
            if (submitButton) {
                submitButton.disabled = true;
                submitButton.textContent = 'Wird gesendet...';
            }
            
            try {
                // Formular-Daten sammeln
                const formData = new FormData(form);
                const leadData = {
                    name: formData.get('name') || formData.get('fullname'),
                    email: formData.get('email'),
                    phone: formData.get('phone') || '',
                    message: formData.get('message') || formData.get('notes') || '',
                    category: form.querySelector('[data-category]')?.dataset.category || 'general',
                    source: window.location.href,
                    timestamp: new Date().toISOString(),
                    utm_source: new URLSearchParams(window.location.search).get('utm_source') || 'direct',
                    utm_medium: new URLSearchParams(window.location.search).get('utm_medium') || '',
                    utm_campaign: new URLSearchParams(window.location.search).get('utm_campaign') || ''
                };
                
                console.log('Lead form submitted:', leadData);
                
                // Connect to n8n webhook for lead submission
                const response = await callN8NWebhook(N8N_CONFIG.endpoints.leadSubmission, leadData);
                
                if (response) {
                    // Track Google Analytics Event
                    trackGAEvent('lead_form_submit', {
                        category: leadData.category,
                        value: 1
                    });
                    
                    alert('Vielen Dank! Wir melden uns in Kürze bei Ihnen.');
                    form.reset();
                } else {
                    throw new Error('Webhook call failed');
                }
            } catch (error) {
                console.error('Error submitting lead form:', error);
                // Fallback: Trotzdem Erfolgsmeldung anzeigen (User Experience)
                trackGAEvent('lead_form_submit_error', {
                    error: error.message
                });
            alert('Vielen Dank! Wir melden uns in Kürze bei Ihnen.');
            form.reset();
            } finally {
                if (submitButton) {
                    submitButton.disabled = false;
                    submitButton.textContent = originalButtonText;
                }
            }
        });
    });
}

// Affiliate Link Tracking
function initAffiliateTracking() {
    const affiliateLinks = document.querySelectorAll('[data-affiliate]');
    
    affiliateLinks.forEach(link => {
        link.addEventListener('click', (e) => {
            const affiliateId = link.dataset.affiliate;
            const affiliateUrl = link.href;
            const linkText = link.textContent.trim();
            
            console.log('Affiliate link clicked:', affiliateId);
            
            // Track affiliate click via analytics (Google Analytics)
            trackGAEvent('affiliate_click', {
                affiliate_id: affiliateId,
                link_url: affiliateUrl,
                link_text: linkText,
                page_url: window.location.href
            });
            
            // Optional: Sende auch an n8n Analytics Webhook (falls konfiguriert)
            if (N8N_CONFIG.webhookBaseUrl && !N8N_CONFIG.webhookBaseUrl.includes('your-n8n-instance.com')) {
                callN8NWebhook(N8N_CONFIG.endpoints.analytics, {
                    event_type: 'affiliate_click',
                    affiliate_id: affiliateId,
                    link_url: affiliateUrl,
                    link_text: linkText,
                    timestamp: new Date().toISOString(),
                    page_url: window.location.href
                }).catch(err => console.error('Analytics webhook error:', err));
            }
        });
    });
}

// Initialize
document.addEventListener('DOMContentLoaded', () => {
    console.log('⚡ CanGo App Empire - Dark Factory Initialized');
    console.log('🔧 System Config: Dark Industrial v2');
    console.log('🏭 Operating System Mode: ACTIVE');
    initSystemRequirements();
    loadEmpireData();
    initNewsFilter();
    initLoadMoreNews();
    initUpgradeCategoryTabs();
    initLeadForms();
    initAffiliateTracking();
});

// Add fadeIn animation
const style = document.createElement('style');
style.textContent = `
    @keyframes fadeIn {
        from {
            opacity: 0;
            transform: translateY(10px);
        }
        to {
            opacity: 1;
            transform: translateY(0);
        }
    }
`;
document.head.appendChild(style);

