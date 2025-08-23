---
layout: page
permalink: /materials/
---

<div class="materials-container">
    <header class="materials-header">
        <h1>Course Materials</h1>
        <div class="header-accent"></div>
    </header>

    <div class="materials-content">
        <div class="materials-section">
            <h2>
                <span class="section-icon">📚</span>
                Prerequisites
            </h2>
            <div class="prerequisites-text">
                <p>Students should be comfortable with <span class="highlight">multivariate calculus</span>, <span class="highlight">linear algebra</span>, <span class="highlight">probability</span>, <span class="highlight">statistics</span>, <span class="highlight">information theory</span>, and <span class="highlight">Python programming</span> to register for the course.</p>
                <p>Basic knowledge of <span class="highlight">machine learning</span> (e.g., ESE 4200, CIS 5190, or CIS 5200) would be very useful.</p>
            </div>
        </div>

        <div class="materials-section">
            <h2>
                <span class="section-icon">📖</span>
                Reference Books
            </h2>
            <div class="books-section">
                {% include image.html url="/_images/cover1.jpg" width=175 align="right" %}
                {% include image.html url="/_images/cover2.jpg" width=175 align="right" %}
                
                <div class="book-entry">
                    <div class="book-title">Generalized Principal Component Analysis</div>
                    <div class="book-authors">René Vidal, Yi Ma, Shankar Sastry</div>
                    <div class="book-details">
                        <span class="edition">1st Edition</span>
                        <span class="isbn">ISBN: 978-0-387-87810-2</span>
                    </div>
                </div>
                
                <div class="book-entry">
                    <div class="book-title">Deep Generative Modeling</div>
                    <div class="book-authors">Jakub M. Tomczak</div>
                    <div class="book-details">
                        <span class="edition">1st Edition</span>
                        <span class="isbn">ISBN: 978-3-030-93157-5</span>
                    </div>
                </div>
            </div>
        </div>
    </div>
</div>

<style>
.materials-container {
    max-width: 900px;
    margin: 0 auto;
    padding: 2rem 1rem;
    font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
}

.materials-header {
    text-align: center;
    margin-bottom: 3rem;
    position: relative;
}

.materials-header h1 {
    font-size: 2rem;
    font-weight: 600;
    color: #333 !important;
    margin-bottom: 0.5rem;
    letter-spacing: -0.025em;
}

.header-accent {
    width: 60px;
    height: 3px;
    background: linear-gradient(90deg, #3b82f6, #8b5cf6);
    margin: 0 auto;
    border-radius: 2px;
}

.materials-content {
    line-height: 1.7;
}

.materials-section {
    margin-bottom: 3rem;
}

.materials-section h2 {
    font-size: 1.5rem;
    font-weight: 600;
    color: #1a202c;
    margin-bottom: 1.5rem;
    display: flex;
    align-items: center;
    gap: 0.75rem;
}

.section-icon {
    font-size: 1.25rem;
    opacity: 0.8;
}

.prerequisites-text {
    padding-left: 2rem;
    border-left: 3px solid #e2e8f0;
    margin-left: 1.5rem;
}

.prerequisites-text p {
    color: #4a5568;
    margin-bottom: 1rem;
    line-height: 1.7;
}

.prerequisites-text p:last-child {
    margin-bottom: 0;
}

.highlight {
    color: #1a202c;
    font-weight: 600;
    background: linear-gradient(120deg, #dbeafe 0%, #e0e7ff 100%);
    padding: 0.125rem 0.375rem;
    border-radius: 4px;
    font-size: 0.95em;
}

.books-section {
    padding-left: 2rem;
    border-left: 3px solid #e2e8f0;
    margin-left: 1.5rem;
}

.book-entry {
    margin-bottom: 2rem;
    padding-bottom: 1.5rem;
    border-bottom: 1px solid #f1f5f9;
    position: relative;
}

.book-entry:last-child {
    margin-bottom: 0;
    padding-bottom: 0;
    border-bottom: none;
}

.book-entry::before {
    content: "•";
    position: absolute;
    left: -2.5rem;
    top: 0.25rem;
    color: #3b82f6;
    font-size: 1.5rem;
    font-weight: bold;
}

.book-title {
    font-size: 1.125rem;
    font-weight: 600;
    color: #1a202c;
    margin-bottom: 0.5rem;
    line-height: 1.4;
}

.book-authors {
    font-size: 0.95rem;
    color: #64748b;
    margin-bottom: 0.75rem;
    font-style: italic;
}

.book-details {
    display: flex;
    gap: 1.5rem;
    align-items: center;
    flex-wrap: wrap;
}

.edition {
    font-size: 0.875rem;
    color: #64748b;
    background: #f8fafc;
    padding: 0.25rem 0.75rem;
    border-radius: 4px;
    border: 1px solid #e2e8f0;
}

.isbn {
    font-size: 0.875rem;
    color: #3b82f6;
    font-weight: 500;
    font-family: 'Courier New', monospace;
    background: #eff6ff;
    padding: 0.25rem 0.75rem;
    border-radius: 4px;
    border: 1px solid #dbeafe;
}

/* Mobile responsiveness */
@media (max-width: 768px) {
    .materials-container {
        padding: 1rem 0.5rem;
    }
    
    .materials-header h1 {
        font-size: 1.75rem;
    }
    
    .prerequisites-text,
    .books-section {
        padding-left: 1.5rem;
        margin-left: 1rem;
    }
    
    .book-entry::before {
        left: -2rem;
    }
    
    .book-details {
        flex-direction: column;
        gap: 0.5rem;
        align-items: flex-start;
    }
}

/* Dark mode support */
@media (prefers-color-scheme: dark) {
    .materials-section h2 {
        color: #000000;
    }
    
    .prerequisites-text,
    .books-section {
        border-left-color: #2d3748;
    }
    
    .prerequisites-text p {
        color: #4a5568;
    }
    
    .highlight {
        color: #000000;
        background: linear-gradient(120deg, #dbeafe 0%, #e0e7ff 100%);
    }
    
    .book-title {
        color: #000000;
    }
    
    .book-authors {
        color: #4a5568;
    }
    
    .edition {
        background: #2d3748;
        color: #ffffff;
        border-color: #4a5568;
    }
    
    .isbn {
        background: #1e3a8a;
        color: #ffffff;
        border-color: #3b82f6;
    }
    
    .book-entry {
        border-bottom-color: #2d3748;
    }
    
    .book-entry::before {
        color: #60a5fa;
    }
}
</style>