// CanGo App Empire V4.0 - MONOPOLY JavaScript
// Aggressive animations and interactions

document.addEventListener('DOMContentLoaded', function() {
    
    // Animate counters
    function animateCounter(element) {
        const target = parseInt(element.getAttribute('data-target'));
        const duration = 2000;
        const increment = target / (duration / 16);
        let current = 0;
        
        const timer = setInterval(() => {
            current += increment;
            if (current >= target) {
                element.textContent = target;
                clearInterval(timer);
            } else {
                element.textContent = Math.floor(current);
            }
        }, 16);
    }
    
    // Initialize counters
    const counters = document.querySelectorAll('.metric-value');
    const observerOptions = {
        threshold: 0.5,
        rootMargin: '0px'
    };
    
    const counterObserver = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                animateCounter(entry.target);
                counterObserver.unobserve(entry.target);
            }
        });
    }, observerOptions);
    
    counters.forEach(counter => {
        counterObserver.observe(counter);
    });
    
    // Terminal cursor effect
    const terminalTexts = document.querySelectorAll('.terminal-text');
    terminalTexts.forEach(text => {
        text.innerHTML = text.textContent + '<span class="cursor">_</span>';
    });
    
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
    
    // Territory card hover effects
    const territoryCards = document.querySelectorAll('.territory-card');
    territoryCards.forEach(card => {
        const color = card.getAttribute('data-color');
        card.addEventListener('mouseenter', function() {
            this.style.borderColor = color;
            this.style.boxShadow = `0 0 30px ${color}40`;
        });
        card.addEventListener('mouseleave', function() {
            this.style.borderColor = '';
            this.style.boxShadow = '';
        });
    });
    
    // Parallax effect for hero
    let lastScroll = 0;
    window.addEventListener('scroll', () => {
        const currentScroll = window.pageYOffset;
        const hero = document.querySelector('.hero-monopoly');
        if (hero && currentScroll < window.innerHeight) {
            hero.style.transform = `translateY(${currentScroll * 0.5}px)`;
        }
        lastScroll = currentScroll;
    });
    
    // Arsenal Tools - Load and Filter
    async function loadArsenalTools() {
        try {
            const response = await fetch('cango-empire-v4-monopoly-data.json');
            const data = await response.json();
            
            // Load Hero Section
            if (data.pages && data.pages.arsenal && data.pages.arsenal.hero) {
                const hero = data.pages.arsenal.hero;
                const headlineEl = document.querySelector('.arsenal-hero .section-headline');
                const subheadlineEl = document.querySelector('.arsenal-hero .section-subheadline');
                const statusEl = document.querySelector('.arsenal-status .status-indicator');
                const statsEl = document.querySelector('.arsenal-stats');
                
                if (headlineEl && hero.headline) headlineEl.textContent = hero.headline;
                if (subheadlineEl && hero.subheadline) subheadlineEl.textContent = hero.subheadline;
                if (statusEl && hero.status_indicator) statusEl.textContent = hero.status_indicator;
                
                if (statsEl && hero.stats && Array.isArray(hero.stats)) {
                    statsEl.innerHTML = hero.stats.map(stat => `
                        <div class="stat-item">
                            <div class="stat-value">${stat.value}</div>
                            <div class="stat-label">${stat.label}</div>
                        </div>
                    `).join('');
                }
            }
            
            // Load Filters
            if (data.pages && data.pages.arsenal && data.pages.arsenal.filters) {
                const filtersContainer = document.querySelector('.arsenal-filters');
                if (filtersContainer && Array.isArray(data.pages.arsenal.filters)) {
                    filtersContainer.innerHTML = data.pages.arsenal.filters.map((filter, index) => `
                        <button class="filter-btn ${index === 0 ? 'active' : ''}" data-filter="${filter.id}">${filter.label}</button>
                    `).join('');
                }
            }
            
            // Load Tools
            if (data.pages && data.pages.arsenal && data.pages.arsenal.products) {
                allTools = data.pages.arsenal.products;
                renderTools(allTools);
                setupFilters();
            } else if (data.pages && data.pages.tools && data.pages.tools.products) {
                // Fallback für alte Struktur
                allTools = data.pages.tools.products;
                renderTools(allTools);
                setupFilters();
            } else {
                console.warn('Tools data not found in JSON, using fallback');
                allTools = getHardcodedTools();
                renderTools(allTools);
                setupFilters();
            }
        } catch (error) {
            console.error('Error loading arsenal tools:', error);
            // Fallback: Hardcoded tools
            allTools = getHardcodedTools();
            renderTools(allTools);
            setupFilters();
        }
    }
    
    function renderTools(tools) {
        const grid = document.getElementById('toolsGrid');
        if (!grid) return;
        
        // Handle placeholder links
        function getLink(tool) {
            const link = tool.link || '#';
            // If it's a placeholder (DEIN_..._LINK), show as # for now
            if (link.startsWith('DEIN_') && link.endsWith('_LINK')) {
                return '#';
            }
            return link;
        }
        
        // Get logo URL from JSON or fallback
        function getLogoUrl(tool) {
            // Use logo from JSON if available
            if (tool.logo && tool.logo.startsWith('http')) {
                return tool.logo;
            }
            // Try Simple Icons CDN with comprehensive mapping
            const iconMap = {
                'hostinger': 'hostinger',
                'n8n': 'n8n',
                'nocodebackend': 'nocode',
                'browseract': 'browser',
                'goosevpn': 'vpn',
                'make': 'make',
                'zapier': 'zapier',
                'claude': 'anthropic',
                'chatgpt': 'openai',
                'perplexity': 'perplexity',
                'jasper': 'jasper',
                'copyai': 'copyai',
                'katteb': 'katteb',
                'voila': 'voila',
                'quillbot': 'quillbot',
                'midjourney': 'midjourney',
                'kie': 'kie',
                'runway': 'runwayml',
                'heygen': 'heygen',
                'synthesia': 'synthesia',
                'pikalabs': 'pika',
                'opus': 'opus',
                'mootion': 'mootion',
                'depositphotos': 'depositphotos',
                'canva': 'canva',
                'adcreative': 'adcreative',
                'elevenlabs': 'elevenlabs',
                'unmixr': 'unmixr',
                'suno': 'suno',
                'murf': 'murf',
                'semrush': 'semrush',
                'surfer': 'surferseo',
                'neuronwriter': 'neuronwriter',
                'sociamonials': 'sociamonials',
                'vidiq': 'vidiq',
                'feedspace': 'feedspace',
                'greta': 'greta',
                'skillplate': 'skillplate',
                'cursor': 'cursor',
                'githubcopilot': 'github',
                'notion': 'notion',
                'tidycal': 'tidycal',
                'fireflies': 'fireflies',
                'chatbase': 'chatbase',
                'deepl': 'deepl'
            };
            const iconName = iconMap[tool.id] || tool.id.toLowerCase().replace(/[^a-z0-9]/g, '');
            return `https://cdn.simpleicons.org/${iconName}/FF9900`;
        }
        
        grid.innerHTML = tools.map(tool => `
            <div class="product-card" data-category="${tool.category}" data-tool-id="${tool.id}">
                ${tool.badge ? `<div class="product-badge">${tool.badge}</div>` : ''}
                ${tool.logo || getLogoUrl(tool) ? `<img src="${tool.logo || getLogoUrl(tool)}" alt="${tool.name} Logo" class="product-logo" onerror="this.style.display='none'">` : ''}
                <h3 class="product-name">${tool.name}</h3>
                <p class="product-description">${tool.description}</p>
                <div class="product-price">${tool.price_display}</div>
                <a href="#" class="product-cta" data-tool-id="${tool.id}">DETAILS</a>
            </div>
        `).join('');
        
        // Initialize all cards as visible
        document.querySelectorAll('.tool-card').forEach(card => {
            card.style.display = 'block';
            card.style.opacity = '1';
            card.style.transform = 'translateY(0)';
        });
        
        // Add click handlers for product cards
        document.querySelectorAll('.product-card').forEach(card => {
            const cta = card.querySelector('.product-cta');
            if (cta) {
                cta.addEventListener('click', function(e) {
                    e.preventDefault();
                    e.stopPropagation();
                    const toolId = this.getAttribute('data-tool-id');
                    const tool = tools.find(t => t.id === toolId);
                    if (tool) {
                        openToolModal(tool);
                    }
                });
            }
        });
    }
    
    // Store tools globally for modal access
    let allTools = [];
    
    function openToolModal(tool) {
        const modal = document.getElementById('toolModal');
        if (!modal) return;
        
        // Get logo URL
        const logoUrl = getLogoUrl(tool);
        
        // Populate modal
        document.getElementById('modalName').textContent = tool.name;
        document.getElementById('modalBadge').textContent = tool.badge;
        document.getElementById('modalDescription').textContent = tool.description;
        document.getElementById('modalCategory').textContent = getCategoryLabel(tool.category);
        document.getElementById('modalPrice').textContent = tool.price_display;
        document.getElementById('modalStatus').textContent = tool.badge;
        
        // Set logo
        const logoImg = document.getElementById('modalLogo');
        logoImg.src = logoUrl;
        logoImg.alt = `${tool.name} Logo`;
        
        // Handle link
        const link = tool.link && !tool.link.startsWith('DEIN_') ? tool.link : '#';
        const modalLink = document.getElementById('modalLink');
        modalLink.href = link;
        if (link === '#') {
            modalLink.style.opacity = '0.5';
            modalLink.style.cursor = 'not-allowed';
            modalLink.onclick = (e) => e.preventDefault();
        } else {
            modalLink.style.opacity = '1';
            modalLink.style.cursor = 'pointer';
            modalLink.onclick = null;
        }
        
        // Features (can be extended in JSON later)
        const featuresList = document.getElementById('modalFeatures');
        featuresList.innerHTML = getToolFeatures(tool);
        
        // Show modal
        modal.classList.add('active');
        document.body.style.overflow = 'hidden';
    }
    
    function closeToolModal() {
        const modal = document.getElementById('toolModal');
        if (modal) {
            modal.classList.remove('active');
            document.body.style.overflow = '';
        }
    }
    
    function getCategoryLabel(category) {
        const labels = {
            'infrastructure': 'Infrastructure (Core)',
            'intelligence': 'Neural Intelligence',
            'visuals': 'Visual Synthesis',
            'audio': 'Audio & Voice',
            'growth': 'Growth & SEO',
            'ops': 'Operations & Coding'
        };
        return labels[category] || category;
    }
    
    function getToolFeatures(tool) {
        // Default features based on category
        const defaultFeatures = {
            'infrastructure': [
                'Kernkomponente unserer Automatisierung',
                'In Produktion seit 2024',
                '24/7 Verfügbar'
            ],
            'intelligence': [
                'Integriert in unsere Workflows',
                'Automatisierte Nutzung',
                'Qualitätsgeprüft'
            ],
            'visuals': [
                'Teil unserer Content-Pipeline',
                'Automatisierte Generierung',
                'Produktionsreif'
            ],
            'audio': [
                'Voice-Over Automatisierung',
                'In Video-Workflows integriert',
                'Hohe Qualität'
            ],
            'growth': [
                'SEO-Optimierung automatisiert',
                'Datengetriebene Entscheidungen',
                'Kontinuierliche Verbesserung'
            ],
            'ops': [
                'Entwickler-Workflow optimiert',
                'Code-Generierung automatisiert',
                'Produktivitätssteigerung'
            ]
        };
        
        const features = defaultFeatures[tool.category] || ['In Verwendung', 'Getestet & verifiziert'];
        
        return features.map(f => `<li>${f}</li>`).join('');
    }
    
    function setupFilters() {
        const filterButtons = document.querySelectorAll('.category-filters .filter-btn, .arsenal-filters .filter-btn');
        const productCards = document.querySelectorAll('.product-card');
        
        filterButtons.forEach(btn => {
            btn.addEventListener('click', function() {
                // Update active state
                const container = this.closest('.category-filters, .arsenal-filters');
                if (container) {
                    container.querySelectorAll('.filter-btn').forEach(b => b.classList.remove('active'));
                }
                this.classList.add('active');
                
                // Filter products
                const filter = this.getAttribute('data-filter');
                
                productCards.forEach(card => {
                    const category = card.getAttribute('data-category');
                    const categoryMap = {
                        'infrastructure': 'infrastructure',
                        'intelligence': 'intelligence',
                        'visuals': 'visuals',
                        'audio': 'audio',
                        'growth': 'growth',
                        'ops': 'ops',
                        'content': 'content',
                        'youtube': 'youtube',
                        'lead': 'lead',
                        'research': 'research'
                    };
                    
                    if (filter === 'all' || category === filter || categoryMap[category] === filter) {
                        card.style.display = 'block';
                        setTimeout(() => {
                            card.style.opacity = '1';
                            card.style.transform = 'translateY(0)';
                        }, 10);
                    } else {
                        card.style.opacity = '0';
                        card.style.transform = 'translateY(20px)';
                        setTimeout(() => {
                            card.style.display = 'none';
                        }, 300);
                    }
                });
            });
        });
    }
    
    // Hardcoded tools as fallback
    function getHardcodedTools() {
        return [
            {
                id: "hostinger",
                category: "infrastructure",
                name: "HOSTINGER VPS",
                badge: "CORE",
                description: "Unsere physische Heimat. KVM-Virtualisierung in Frankfurt. Hier laufen n8n und Python.",
                price_display: "AB 4,99€ / MO",
                cta: "SERVER DEPLOYEN",
                link: "#"
            },
            {
                id: "n8n",
                category: "infrastructure",
                name: "n8n",
                badge: "ORCHESTRATOR",
                description: "Das Nervensystem. Verbindet alle anderen Tools. Open-Source und unlimitiert.",
                price_display: "FREE (SELF-HOSTED)",
                cta: "LIZENZ HOLEN",
                link: "https://n8n.io"
            },
            {
                id: "claude",
                category: "intelligence",
                name: "CLAUDE 3.5 SONNET",
                badge: "CODING KING",
                description: "Das Gehirn unserer Python-Skripte. Schreibt besseren Code als GPT-4.",
                price_display: "20$ / MO",
                cta: "ZUGANG HOLEN",
                link: "https://anthropic.com"
            }
        ];
    }
    
    // Load arsenal tools
    loadArsenalTools();
    
    // Load FAQ
    loadFAQ();
    
    // Modal close handlers
    const modalClose = document.getElementById('modalClose');
    const modal = document.getElementById('toolModal');
    
    if (modalClose) {
        modalClose.addEventListener('click', closeToolModal);
    }
    
    if (modal) {
        modal.addEventListener('click', function(e) {
            if (e.target.classList.contains('modal-overlay') || e.target === modal) {
                closeToolModal();
            }
        });
        
        // Close on Escape key
        document.addEventListener('keydown', function(e) {
            if (e.key === 'Escape' && modal.classList.contains('active')) {
                closeToolModal();
            }
        });
    }
    
    // FAQ - Load and Setup
    async function loadFAQ() {
        try {
            const response = await fetch('cango-empire-v4-monopoly-data.json');
            const data = await response.json();
            
            if (data.pages && data.pages.faq) {
                const faq = data.pages.faq;
                
                // Update hero
                if (faq.hero) {
                    const headline = document.getElementById('faqHeadline');
                    const subheadline = document.getElementById('faqSubheadline');
                    const status = document.getElementById('faqStatus');
                    
                    if (headline) headline.textContent = faq.hero.headline;
                    if (subheadline) subheadline.textContent = faq.hero.subheadline;
                    if (status) status.textContent = faq.hero.status_indicator;
                }
                
                // Render categories
                if (faq.categories) {
                    renderFAQCategories(faq.categories);
                }
                
                // Update CTA
                if (faq.cta_box) {
                    const ctaText = document.getElementById('faqCtaText');
                    const ctaButton = document.getElementById('faqCtaButton');
                    
                    if (ctaText) ctaText.textContent = faq.cta_box.text;
                    if (ctaButton) {
                        ctaButton.textContent = faq.cta_box.button || 'ZUGANG KONFIGURIEREN';
                        ctaButton.href = faq.cta_box.link || '#zugang';
                    }
                }
            }
        } catch (error) {
            console.error('Error loading FAQ:', error);
        }
    }
    
    function renderFAQCategories(categories) {
        const accordionContainer = document.getElementById('faqAccordion');
        if (!accordionContainer) return;
        
        const iconMap = {
            'radar': '📡',
            'cpu': '⚙️',
            'chart': '📊'
        };
        
        accordionContainer.innerHTML = categories.map(category => `
            <div class="faq-category-accordion" data-category="${category.id}">
                <div class="faq-category-header">
                    <div class="faq-category-title-wrapper">
                        <span class="faq-category-icon">${iconMap[category.icon] || '📋'}</span>
                        <h3 class="faq-category-title">${category.title}</h3>
                    </div>
                    <span class="faq-category-toggle">▼</span>
                </div>
                <div class="faq-category-questions">
                    ${category.questions.map((item, index) => `
                        <div class="faq-item-accordion" data-index="${index}">
                            <div class="faq-question-accordion">
                                <span>${item.q}</span>
                                <span class="faq-toggle">▼</span>
                            </div>
                            <div class="faq-answer-accordion">
                                <p>${item.a}</p>
                            </div>
                        </div>
                    `).join('')}
                </div>
            </div>
        `).join('');
        
        // Setup category accordion handlers
        document.querySelectorAll('.faq-category-accordion').forEach(category => {
            const header = category.querySelector('.faq-category-header');
            header.addEventListener('click', function() {
                const isActive = category.classList.contains('active');
                
                // Close all other categories
                document.querySelectorAll('.faq-category-accordion').forEach(other => {
                    if (other !== category) {
                        other.classList.remove('active');
                    }
                });
                
                // Toggle current category
                if (isActive) {
                    category.classList.remove('active');
                } else {
                    category.classList.add('active');
                }
            });
        });
        
        // Setup question accordion handlers
        document.querySelectorAll('.faq-item-accordion').forEach(item => {
            const question = item.querySelector('.faq-question-accordion');
            question.addEventListener('click', function(e) {
                e.stopPropagation();
                const isActive = item.classList.contains('active');
                
                // Close all other items in the same category
                const category = item.closest('.faq-category-accordion');
                if (category) {
                    category.querySelectorAll('.faq-item-accordion').forEach(otherItem => {
                        if (otherItem !== item) {
                            otherItem.classList.remove('active');
                        }
                    });
                }
                
                // Toggle current item
                if (isActive) {
                    item.classList.remove('active');
                } else {
                    item.classList.add('active');
                }
            });
        });
    }
    
    // Load Workflows
    async function loadWorkflows() {
        try {
            const response = await fetch('cango-empire-v4-monopoly-data.json');
            const data = await response.json();
            
            if (data.pages && data.pages.workflows && data.pages.workflows.products) {
                const workflows = data.pages.workflows.products;
                const grid = document.getElementById('workflowsGrid');
                
                if (grid) {
                    grid.innerHTML = workflows.map(workflow => `
                        <div class="product-card" data-category="${workflow.category}" data-workflow-id="${workflow.id}">
                            ${workflow.badge ? `<div class="product-badge">${workflow.badge}</div>` : ''}
                            <h3 class="product-name">${workflow.name}</h3>
                            <p class="product-description">${workflow.description}</p>
                            <div class="product-price">${workflow.price_display || 'Preis auf Anfrage'}</div>
                            <a href="#" class="product-cta" data-workflow-id="${workflow.id}">DETAILS</a>
                        </div>
                    `).join('');
                    
                    // Add click handlers
                    document.querySelectorAll('#workflowsGrid .product-card').forEach(card => {
                        const cta = card.querySelector('.product-cta');
                        if (cta) {
                            cta.addEventListener('click', function(e) {
                                e.preventDefault();
                                e.stopPropagation();
                                const workflowId = this.getAttribute('data-workflow-id');
                                const workflow = workflows.find(w => w.id === workflowId);
                                if (workflow) {
                                    openWorkflowModal(workflow);
                                }
                            });
                        }
                    });
                }
            }
        } catch (error) {
            console.error('Error loading workflows:', error);
        }
    }
    
    function openWorkflowModal(workflow) {
        // Reuse tool modal for workflows
        const modal = document.getElementById('toolModal');
        if (!modal) return;
        
        document.getElementById('modalName').textContent = workflow.name;
        document.getElementById('modalBadge').textContent = workflow.badge || 'WORKFLOW';
        document.getElementById('modalDescription').textContent = workflow.description;
        document.getElementById('modalCategory').textContent = workflow.category || 'Workflow';
        document.getElementById('modalPrice').textContent = workflow.price_display || 'Preis auf Anfrage';
        document.getElementById('modalStatus').textContent = workflow.status || 'Active';
        
        const logoImg = document.getElementById('modalLogo');
        logoImg.style.display = 'none';
        
        const featuresList = document.getElementById('modalFeatures');
        if (workflow.features && Array.isArray(workflow.features)) {
            featuresList.innerHTML = workflow.features.map(f => `<li>${f}</li>`).join('');
        } else {
            featuresList.innerHTML = '<li>Vollautomatische Ausführung</li><li>24/7 Verfügbar</li>';
        }
        
        const modalLink = document.getElementById('modalLink');
        modalLink.href = '#kontakt';
        modalLink.textContent = 'JETZT KAUFEN →';
        
        modal.classList.add('active');
        document.body.style.overflow = 'hidden';
    }
    
});

