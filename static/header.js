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

    // 2. Smart Sticky Header Scroll Effect (Hide on scroll down, Show on scroll up)
    if (header) {
        let lastScrollY = window.scrollY;

        const handleScroll = () => {
            const currentScrollY = window.scrollY;

            // Add 'scrolled' class for background style if not at top
            if (currentScrollY > 20) {
                header.classList.add('scrolled');
                // For project pages that might expect 'active' class
                header.classList.add('active');
            } else {
                header.classList.remove('scrolled');
                header.classList.remove('active');
            }

            // Smart Hide Logic: Only applicable if we are not at the very top
            // and if the menu is NOT open (to avoid hiding navigation while using it)
            if (navMenu && !navMenu.classList.contains('open')) {
                if (currentScrollY > 100) {
                    if (currentScrollY > lastScrollY) {
                        // Scrolling DOWN -> Hide
                        header.classList.add('header-hidden');
                    } else {
                        // Scrolling UP -> Show
                        header.classList.remove('header-hidden');
                    }
                } else {
                    // Near top -> Show
                    header.classList.remove('header-hidden');
                }
            }

            lastScrollY = currentScrollY;
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
