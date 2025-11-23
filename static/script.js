document.addEventListener('DOMContentLoaded', () => {
    // Preloader removed


    // Carousel Auto-scroll
    const carousel = document.querySelector('.carousel');
    if (carousel) {
        let isPaused = false;
        let animationId;

        // Clone items for infinite scroll illusion if needed, but for now simple reset
        const step = () => {
            if (!isPaused) {
                // Check if we reached the end
                if (carousel.scrollLeft + carousel.clientWidth >= carousel.scrollWidth - 1) {
                    carousel.scrollLeft = 0;
                } else {
                    carousel.scrollLeft += 1; // Adjust speed here
                }
            }
            animationId = requestAnimationFrame(step);
        };

        // Start scrolling
        animationId = requestAnimationFrame(step);

        // Pause on interaction
        carousel.addEventListener('mouseenter', () => { isPaused = true; });
        carousel.addEventListener('mouseleave', () => { isPaused = false; });
        carousel.addEventListener('touchstart', () => { isPaused = true; }, { passive: true });
        carousel.addEventListener('touchend', () => { isPaused = false; });

        // Optional: Disable scroll snap for smoother auto-scroll
        carousel.style.scrollSnapType = 'none';
    }

    // FAQ
    const faqItems = document.querySelectorAll('.faq-item');
    faqItems.forEach(item => {
        const question = item.querySelector('.faq-question');
        const answer = item.querySelector('.faq-answer');
        const icon = item.querySelector('.icon');

        if (question && answer && icon) {
            question.addEventListener('click', () => {
                const isOpen = answer.classList.toggle('open');
                icon.textContent = isOpen ? '−' : '+';
            });
        }
    });

    // Scroll to top button
    const scrollToTopBtn = document.getElementById('scrollToTopBtn');
    if (scrollToTopBtn) {
        window.addEventListener('scroll', () => {
            if (document.body.scrollTop > 20 || document.documentElement.scrollTop > 20) {
                scrollToTopBtn.style.display = 'block';
            } else {
                scrollToTopBtn.style.display = 'none';
            }
        });

        scrollToTopBtn.addEventListener('click', () => {
            document.body.scrollTop = 0; // For Safari
            document.documentElement.scrollTop = 0; // For Chrome, Firefox, IE and Opera
        });
    }

    // Advanced Scrolling Effects
    const header = document.getElementById('mainHeader');
    const heroTitle = document.querySelector('.hero-title');
    const sections = document.querySelectorAll('section');
    const animatedElements = document.querySelectorAll('.animate-on-scroll');
    const parallaxItems = document.querySelectorAll('[data-parallax]');
    const cardTargets = document.querySelectorAll('.service-card, .category-card, .project-card, .testimonial-card, .pricing-card, .carousel-item, .detail-card');

    cardTargets.forEach((card, index) => {
        card.classList.add('motion-card');
        card.style.setProperty('--motion-delay', `${(index % 4) * 0.08}s`);
    });

    if ('IntersectionObserver' in window) {
        const animateObserver = new IntersectionObserver((entries, observer) => {
            entries.forEach(entry => {
                if (entry.isIntersecting) {
                    entry.target.classList.add('in-view');
                    observer.unobserve(entry.target);
                }
            });
        }, { threshold: 0.2 });

        animatedElements.forEach(el => animateObserver.observe(el));

        const cardObserver = new IntersectionObserver((entries, observer) => {
            entries.forEach(entry => {
                if (entry.isIntersecting) {
                    entry.target.classList.add('in-view');
                    observer.unobserve(entry.target);
                }
            });
        }, { threshold: 0.2 });

        document.querySelectorAll('.motion-card').forEach(card => cardObserver.observe(card));
    } else {
        animatedElements.forEach(el => el.classList.add('in-view'));
        document.querySelectorAll('.motion-card').forEach(card => card.classList.add('in-view'));
    }

    const revealSection = () => {
        const windowHeight = window.innerHeight;
        sections.forEach(section => {
            const sectionTop = section.getBoundingClientRect().top;
            if (sectionTop < windowHeight - 150) {
                section.classList.add('reveal');
            }
        });
    };

    const applyParallax = () => {
        const scrollPosition = window.scrollY;
        parallaxItems.forEach(item => {
            const intensity = parseFloat(item.dataset.parallax) || 0.05;
            const offset = Math.min(scrollPosition * intensity, 160) * -1;
            item.style.setProperty('--parallax-offset', `${offset}px`);
        });
    };

    window.addEventListener('scroll', () => {
        const scrollPosition = window.scrollY;

        // Sticky Header Effect
        if (header) {
            if (scrollPosition > 50) {
                header.classList.add('scrolled');
            } else {
                header.classList.remove('scrolled');
            }
        }

        if (heroTitle) {
            heroTitle.style.transform = `translateY(${scrollPosition * 0.05}px)`;
        }

        revealSection();
        applyParallax();
    });

    revealSection();
    applyParallax();

    if (window.gsap && window.ScrollTrigger) {
        gsap.registerPlugin(ScrollTrigger);

        const heroTimeline = gsap.timeline({ defaults: { duration: 0.9, ease: 'power3.out' } });
        heroTimeline
            .from('.eyebrow-pill', { y: 20, opacity: 0 })
            .from('.hero-title', { y: 40, opacity: 0 }, '-=0.4')
            .from('.hero-subtitle', { y: 30, opacity: 0 }, '-=0.4')
            .from('.hero-cta .btn', { y: 20, opacity: 0, stagger: 0.1 }, '-=0.4')
            .from('.hero-signal', { y: 20, opacity: 0 }, '-=0.4')
            .from('.hero-metrics .metric-card', { y: 30, opacity: 0, stagger: 0.1 }, '-=0.3')
            .from('.floating-card', { y: 30, opacity: 0, stagger: 0.15 }, '-=0.3');

        const scrollGroups = [
            { selector: '.services-grid .service-card', y: 70, rotationX: -8 },
            { selector: '.category-grid .category-card', y: 50, rotationX: 4 },
            { selector: '.pricing-card', y: 60, rotationX: -6 },
            { selector: '.carousel-item', y: 80, rotationY: 8 },
            { selector: '.testimonial-card', y: 60, rotationX: -5 },
            { selector: '.contact-details-grid .detail-card', y: 60, rotationX: 5 }
        ];

        scrollGroups.forEach(group => {
            gsap.utils.toArray(group.selector).forEach((el, index) => {
                gsap.from(el, {
                    scrollTrigger: {
                        trigger: el,
                        start: 'top 85%',
                        toggleActions: 'play none none reverse'
                    },
                    opacity: 0,
                    y: group.y,
                    rotationX: group.rotationX || 0,
                    rotationY: group.rotationY || 0,
                    duration: 0.9,
                    delay: Math.min(index * 0.05, 0.4),
                    ease: 'power3.out'
                });
            });
        });


    }

    // Contact Form WhatsApp Redirection
    const contactForm = document.querySelector('.contact-form');
    if (contactForm) {
        contactForm.addEventListener('submit', (e) => {
            e.preventDefault();

            const name = document.getElementById('name').value;
            const email = document.getElementById('email').value;
            const phone = document.getElementById('phone').value;
            const service = document.getElementById('service').value;
            const budget = document.getElementById('budget').value;
            const message = document.getElementById('message').value;

            const whatsappNumber = '917021975373';

            let text = `*New Project Inquiry*\n\n`;
            text += `*Name:* ${name}\n`;
            text += `*Email:* ${email}\n`;
            text += `*Phone:* ${phone}\n`;
            text += `*Service:* ${service}\n`;
            text += `*Budget:* ${budget}\n`;
            text += `*Message:* ${message}`;

            const encodedText = encodeURIComponent(text);
            const whatsappUrl = `https://wa.me/${whatsappNumber}?text=${encodedText}`;

            window.open(whatsappUrl, '_blank');
        });
    }
});
