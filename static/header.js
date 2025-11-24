document.addEventListener('DOMContentLoaded', () => {
    // 1. Hamburger Menu Logic
    const navBtn = document.getElementById('navToggle');
    const navMenu = document.getElementById('headerNav');
    const header = document.getElementById('mainHeader');

    if (navBtn && navMenu) {
        // Toggle menu on click
        navBtn.addEventListener('click', (e) => {
            e.stopPropagation(); // Prevent immediate closing
            const expanded = navBtn.getAttribute('aria-expanded') === 'true' || false;
            navBtn.setAttribute('aria-expanded', !expanded);
            navMenu.classList.toggle('open');
            navBtn.classList.toggle('active'); // Optional: for hamburger animation
        });

        // Close menu when clicking outside
        document.addEventListener('click', (e) => {
            if (navMenu.classList.contains('open')) {
                if (!navMenu.contains(e.target) && !navBtn.contains(e.target)) {
                    navMenu.classList.remove('open');
                    navBtn.setAttribute('aria-expanded', 'false');
                    navBtn.classList.remove('active');
                }
            }
        });

        // Close menu when a link is clicked (mobile UX)
        navMenu.querySelectorAll('a').forEach(link => {
            link.addEventListener('click', () => {
                if (window.innerWidth < 820) { // Check if in mobile mode
                    navMenu.classList.remove('open');
                    navBtn.setAttribute('aria-expanded', 'false');
                    navBtn.classList.remove('active');
                }
            });
        });

        // Handle Escape key to close menu
        document.addEventListener('keydown', (e) => {
            if (e.key === 'Escape' && navMenu.classList.contains('open')) {
                navMenu.classList.remove('open');
                navBtn.setAttribute('aria-expanded', 'false');
                navBtn.classList.remove('active');
                navBtn.focus(); // Return focus to toggle button
            }
        });
    }

    // 2. Sticky Header Scroll Effect
    if (header) {
        const handleScroll = () => {
            if (window.scrollY > 20) {
                header.classList.add('scrolled');
                // For project pages that might expect 'active' class
                header.classList.add('active');
            } else {
                header.classList.remove('scrolled');
                header.classList.remove('active');
            }
        };

        // Throttle scroll event slightly for performance
        let ticking = false;
        window.addEventListener('scroll', () => {
            if (!ticking) {
                window.requestAnimationFrame(() => {
                    handleScroll();
                    ticking = false;
                });
                ticking = true;
            }
        });

        // Initial check
        handleScroll();
    }
});
