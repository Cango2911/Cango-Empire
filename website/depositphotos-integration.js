/**
 * DepositPhotos API Integration
 * Lädt Stock-Bilder für die Website automatisch
 */

const DEPOSITPHOTOS_API_BASE = 'https://api.depositphotos.com';
const DEPOSITPHOTOS_API_KEY = 'YOUR_DEPOSITPHOTOS_API_KEY'; // Wird aus Environment Variable geladen

/**
 * Hole Format Keys für DepositPhotos API
 */
async function getDepositPhotosFormatKeys() {
    try {
        const response = await fetch(`${DEPOSITPHOTOS_API_BASE}/?dp_command=editor.partner.getFormatKeys`, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                'Accept': 'application/json'
            },
            body: JSON.stringify({
                dp_apikey: DEPOSITPHOTOS_API_KEY
            })
        });
        
        const data = await response.json();
        return data;
    } catch (error) {
        console.error('Error getting format keys:', error);
        return null;
    }
}

/**
 * Suche Stock-Bilder basierend auf Keywords
 */
async function searchStockImages(keywords, limit = 10, mediaType = 'photo') {
    try {
        const response = await fetch(`${DEPOSITPHOTOS_API_BASE}/?dp_command=stockContent.search`, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                'Accept': 'application/json'
            },
            body: JSON.stringify({
                dp_apikey: DEPOSITPHOTOS_API_KEY,
                dp_search_query: keywords,
                dp_search_media_type: mediaType, // 'photo', 'video', 'vector', 'editorial'
                dp_search_limit: limit,
                dp_search_orientation: 'all', // 'all', 'square', 'portrait', 'landscape'
                dp_search_sort: 'relevance' // 'relevance', 'downloads', 'date'
            })
        });
        
        const data = await response.json();
        
        if (data.type === 'success' && data.data && data.data.items) {
            return data.data.items;
        }
        
        return [];
    } catch (error) {
        console.error('Error searching stock images:', error);
        return [];
    }
}

/**
 * Lade Stock-Bild-URLs für Website-Sektionen
 */
async function loadWebsiteStockImages() {
    const imageSections = [
        { keywords: 'automation technology ai', section: 'hero', count: 1 },
        { keywords: 'time management productivity', section: 'problem', count: 4 },
        { keywords: 'artificial intelligence robot', section: 'solution', count: 3 },
        { keywords: 'content creation video production', section: 'features', count: 6 },
        { keywords: 'business package deal', section: 'packages', count: 3 },
        { keywords: 'success growth chart', section: 'success', count: 4 },
        { keywords: 'ai tools software', section: 'tools', count: 12 },
        { keywords: 'blog writing article', section: 'blog', count: 9 },
        { keywords: 'digital product shop', section: 'shop', count: 8 },
        { keywords: 'team support contact', section: 'contact', count: 1 },
        // Nischen-spezifische Bilder
        { keywords: 'money wealth investment', section: 'niche_vermoegen', count: 3 },
        { keywords: 'mindset motivation success', section: 'niche_mindset', count: 3 },
        { keywords: 'artificial intelligence technology', section: 'niche_ki', count: 3 },
        { keywords: 'bitcoin cryptocurrency', section: 'niche_krypto', count: 3 },
        { keywords: 'career job business', section: 'niche_karriere', count: 3 },
        { keywords: 'renewable energy solar', section: 'niche_energie', count: 3 },
        { keywords: 'real estate property', section: 'niche_immobilien', count: 3 }
    ];
    
    const loadedImages = {};
    
    for (const section of imageSections) {
        try {
            const images = await searchStockImages(section.keywords, section.count, 'photo');
            loadedImages[section.section] = images.map(img => ({
                id: img.id,
                url: img.url || img.preview_url || img.thumb_url || img.url_medium || img.url_big,
                title: img.title || img.description || section.keywords,
                width: img.width,
                height: img.height
            }));
        } catch (error) {
            console.warn(`Fehler beim Laden von Bildern für ${section.section}:`, error);
            loadedImages[section.section] = [];
        }
    }
    
    return loadedImages;
}

/**
 * Füge Stock-Bilder zur Website hinzu
 */
function injectStockImages(images) {
    // Hero Section Background
    if (images.hero && images.hero.length > 0) {
        const heroSection = document.querySelector('.hero');
        if (heroSection) {
            heroSection.style.backgroundImage = `linear-gradient(135deg, rgba(99, 102, 241, 0.85) 0%, rgba(139, 92, 246, 0.85) 50%, rgba(236, 72, 153, 0.85) 100%), url(${images.hero[0].url})`;
            heroSection.style.backgroundSize = 'cover';
            heroSection.style.backgroundPosition = 'center';
            heroSection.style.backgroundBlendMode = 'overlay';
        }
    }
    
    // Problem Cards
    if (images.problem && images.problem.length > 0) {
        const problemCards = document.querySelectorAll('.problem-card');
        problemCards.forEach((card, index) => {
            if (images.problem[index]) {
                const icon = card.querySelector('.problem-icon');
                if (icon) {
                    const img = document.createElement('img');
                    img.src = images.problem[index].url;
                    img.alt = images.problem[index].title;
                    img.className = 'stock-image';
                    img.style.width = '100%';
                    img.style.height = '180px';
                    img.style.objectFit = 'cover';
                    img.style.borderRadius = '8px';
                    img.style.marginBottom = '1rem';
                    card.insertBefore(img, icon);
                }
            }
        });
    }
    
    // Solution Cards
    if (images.solution && images.solution.length > 0) {
        const solutionCards = document.querySelectorAll('.solution-card');
        solutionCards.forEach((card, index) => {
            if (images.solution[index]) {
                const icon = card.querySelector('.solution-icon');
                if (icon) {
                    const img = document.createElement('img');
                    img.src = images.solution[index].url;
                    img.alt = images.solution[index].title;
                    img.className = 'stock-image';
                    img.style.width = '100%';
                    img.style.height = '200px';
                    img.style.objectFit = 'cover';
                    img.style.borderRadius = '8px';
                    img.style.marginBottom = '1rem';
                    img.style.opacity = '0.9';
                    card.insertBefore(img, icon);
                }
            }
        });
    }
    
    // Feature Cards
    if (images.features && images.features.length > 0) {
        const featureCards = document.querySelectorAll('.feature-card');
        featureCards.forEach((card, index) => {
            if (images.features[index]) {
                const img = document.createElement('img');
                img.src = images.features[index].url;
                img.alt = images.features[index].title;
                img.className = 'stock-image';
                img.style.width = '100%';
                img.style.height = '200px';
                img.style.objectFit = 'cover';
                img.style.borderRadius = '8px';
                img.style.marginBottom = '1rem';
                card.insertBefore(img, card.firstChild);
            }
        });
    }
    
    // Package Cards
    if (images.packages && images.packages.length > 0) {
        const packageCards = document.querySelectorAll('.package-card');
        packageCards.forEach((card, index) => {
            if (images.packages[index]) {
                const img = document.createElement('img');
                img.src = images.packages[index].url;
                img.alt = images.packages[index].title;
                img.className = 'stock-image';
                img.style.width = '100%';
                img.style.height = '180px';
                img.style.objectFit = 'cover';
                img.style.borderRadius = '8px';
                img.style.marginBottom = '1rem';
                card.insertBefore(img, card.firstChild);
            }
        });
    }
    
    // Success Cards
    if (images.success && images.success.length > 0) {
        const successCards = document.querySelectorAll('.success-card');
        successCards.forEach((card, index) => {
            if (images.success[index]) {
                const icon = card.querySelector('.success-icon');
                if (icon) {
                    const img = document.createElement('img');
                    img.src = images.success[index].url;
                    img.alt = images.success[index].title;
                    img.className = 'stock-image';
                    img.style.width = '100px';
                    img.style.height = '100px';
                    img.style.borderRadius = '50%';
                    img.style.objectFit = 'cover';
                    img.style.marginBottom = '1rem';
                    icon.replaceWith(img);
                }
            }
        });
    }
    
    // Tool Cards
    if (images.tools && images.tools.length > 0) {
        const toolCards = document.querySelectorAll('.tool-card');
        toolCards.forEach((card, index) => {
            if (images.tools[index]) {
                const icon = card.querySelector('.tool-icon');
                if (icon) {
                    const img = document.createElement('img');
                    img.src = images.tools[index].url;
                    img.alt = images.tools[index].title;
                    img.className = 'stock-image';
                    img.style.width = '100%';
                    img.style.height = '150px';
                    img.style.objectFit = 'cover';
                    img.style.borderRadius = '8px';
                    img.style.marginBottom = '1rem';
                    icon.replaceWith(img);
                }
            }
        });
    }
    
    // Blog Cards
    if (images.blog && images.blog.length > 0) {
        const blogCards = document.querySelectorAll('.blog-card');
        blogCards.forEach((card, index) => {
            if (images.blog[index]) {
                const imageDiv = card.querySelector('.blog-image');
                if (imageDiv) {
                    const img = document.createElement('img');
                    img.src = images.blog[index].url;
                    img.alt = images.blog[index].title;
                    img.className = 'stock-image';
                    img.style.width = '100%';
                    img.style.height = '100%';
                    img.style.objectFit = 'cover';
                    imageDiv.style.background = 'none';
                    imageDiv.style.padding = '0';
                    imageDiv.innerHTML = '';
                    imageDiv.appendChild(img);
                }
            }
        });
    }
    
    // Product Cards (Shop)
    if (images.shop && images.shop.length > 0) {
        const productCards = document.querySelectorAll('.product-card');
        productCards.forEach((card, index) => {
            if (images.shop[index]) {
                const imageDiv = card.querySelector('.product-image');
                if (imageDiv) {
                    const img = document.createElement('img');
                    img.src = images.shop[index].url;
                    img.alt = images.shop[index].title;
                    img.className = 'stock-image';
                    img.style.width = '100%';
                    img.style.height = '200px';
                    img.style.objectFit = 'cover';
                    img.style.borderRadius = '8px';
                    imageDiv.replaceWith(img);
                }
            }
        });
    }
    
    // Börsen Cards
    if (images.tools && images.tools.length > 0) {
        const borsenCards = document.querySelectorAll('.borsen-card');
        borsenCards.forEach((card, index) => {
            const toolIndex = index + 6; // Starte nach den Tool Cards
            if (images.tools[toolIndex]) {
                const logo = card.querySelector('.borsen-logo');
                if (logo) {
                    const img = document.createElement('img');
                    img.src = images.tools[toolIndex].url;
                    img.alt = images.tools[toolIndex].title;
                    img.className = 'stock-image';
                    img.style.width = '80px';
                    img.style.height = '80px';
                    img.style.borderRadius = '50%';
                    img.style.objectFit = 'cover';
                    logo.replaceWith(img);
                }
            }
        });
    }
    
    // Nischen-spezifische Bilder (wenn auf Nischen-Seite)
    const currentPath = window.location.pathname;
    if (currentPath.includes('vermoegen')) {
        injectNicheImages(images.niche_vermoegen || []);
    } else if (currentPath.includes('mindset')) {
        injectNicheImages(images.niche_mindset || []);
    } else if (currentPath.includes('ki')) {
        injectNicheImages(images.niche_ki || []);
    } else if (currentPath.includes('krypto')) {
        injectNicheImages(images.niche_krypto || []);
    } else if (currentPath.includes('karriere')) {
        injectNicheImages(images.niche_karriere || []);
    } else if (currentPath.includes('energie')) {
        injectNicheImages(images.niche_energie || []);
    } else if (currentPath.includes('immobilien')) {
        injectNicheImages(images.niche_immobilien || []);
    }
}

/**
 * Füge Nischen-spezifische Bilder hinzu
 */
function injectNicheImages(images) {
    if (!images || images.length === 0) return;
    
    // Hero Background
    const heroSection = document.querySelector('.niche-hero');
    if (heroSection && images[0]) {
        heroSection.style.backgroundImage = `linear-gradient(135deg, rgba(0,0,0,0.6) 0%, rgba(0,0,0,0.4) 100%), url(${images[0].url})`;
        heroSection.style.backgroundSize = 'cover';
        heroSection.style.backgroundPosition = 'center';
    }
    
    // Feature Cards
    const featureCards = document.querySelectorAll('.feature-card');
    featureCards.forEach((card, index) => {
        if (images[index + 1]) {
            const img = document.createElement('img');
            img.src = images[index + 1].url;
            img.alt = images[index + 1].title;
            img.className = 'stock-image';
            img.style.width = '100%';
            img.style.height = '200px';
            img.style.objectFit = 'cover';
            img.style.borderRadius = '8px';
            img.style.marginBottom = '1rem';
            card.insertBefore(img, card.firstChild);
        }
    });
}

/**
 * Fallback-Bilder (wenn API nicht verfügbar)
 */
function useFallbackImages() {
    console.log('Verwende Fallback-Bilder für bessere UX');
    // Placeholder-Bilder werden durch CSS-Gradienten ersetzt
    // Die Website funktioniert auch ohne API
}

/**
 * Initialisiere DepositPhotos Integration
 */
async function initDepositPhotos() {
    // API Key aus Environment Variable oder Config holen
    const apiKey = window.DEPOSITPHOTOS_API_KEY || DEPOSITPHOTOS_API_KEY;
    
    if (!apiKey || apiKey === 'YOUR_DEPOSITPHOTOS_API_KEY' || apiKey === '{{ DEPOSITPHOTOS_API_KEY }}') {
        console.warn('DepositPhotos API Key nicht konfiguriert. Verwende Fallback-Bilder.');
        useFallbackImages();
        return;
    }
    
    try {
        // Lade Stock-Bilder
        const images = await loadWebsiteStockImages();
        
        // Füge Bilder zur Website hinzu
        injectStockImages(images);
        
        console.log('✅ DepositPhotos Bilder erfolgreich geladen');
    } catch (error) {
        console.error('Fehler beim Laden der DepositPhotos Bilder:', error);
        useFallbackImages();
    }
}

// Initialisiere beim Laden der Seite
if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', initDepositPhotos);
} else {
    initDepositPhotos();
}

// Export für n8n Workflows
if (typeof module !== 'undefined' && module.exports) {
    module.exports = {
        searchStockImages,
        getDepositPhotosFormatKeys,
        loadWebsiteStockImages
    };
}

