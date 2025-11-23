document.addEventListener('DOMContentLoaded', () => {
    const gallery = document.querySelector('.gallery');
    if (!gallery) return;

    let isHovered = false;
    const speed = 1; // Pixels per frame

    gallery.addEventListener('mouseenter', () => isHovered = true);
    gallery.addEventListener('mouseleave', () => isHovered = false);
    gallery.addEventListener('touchstart', () => isHovered = true);
    gallery.addEventListener('touchend', () => isHovered = false);

    function autoScroll() {
        if (!isHovered) {
            gallery.scrollLeft += speed;
            // Reset if reached end
            if (gallery.scrollLeft >= gallery.scrollWidth - gallery.clientWidth) {
                gallery.scrollLeft = 0;
            }
        }
        requestAnimationFrame(autoScroll);
    }

    // Initialize
    autoScroll();
});
