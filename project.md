---
layout: page
permalink: /project/
---

<div class="project-container">
    <header class="project-header">
        <h1>Final Project</h1>
        <p class="project-description">TBA</p>
    </header>
</div>

<style>
.project-container {
    max-width: 800px;
    margin: 0 auto;
    padding: 2rem 1rem;
    font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
}

.project-header {
    text-align: center;
    margin-bottom: 3rem;
}

.project-header h1 {
    font-size: 2rem;
    font-weight: 600;
    color: #333 !important;
    margin-bottom: 1rem;
}

.project-description {
    font-size: 1rem;
    color: #64748b;
    max-width: 600px;
    margin: 0 auto;
    line-height: 1.5;
}

/* Mobile responsiveness */
@media (max-width: 768px) {
    .project-container {
        padding: 1rem 0.5rem;
    }
    
    .project-header h1 {
        font-size: 1.75rem;
    }
}

/* Dark mode support */
@media (prefers-color-scheme: dark) {
    .project-header h1 {
        color: #e2e8f0;
    }
    
    .project-description {
        color: #a0aec0;
    }
}
</style>
