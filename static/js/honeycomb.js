
const canvas = document.getElementById('bg');
const ctx = canvas.getContext('2d');

let width, height;
let hexagons = [];
const hexSize = 20;
const hexWidth = hexSize * Math.sqrt(3);
const hexHeight = hexSize * 2;
const numCols = 50;
const numRows = 50;

const mouse = {
    x: undefined,
    y: undefined,
    radius: 150
};

// Pre-parse colors to array [r, g, b, a] to avoid parsing every frame
const parseColorString = (color) => {
    if (color.startsWith('#')) {
        return [
            parseInt(color.slice(1, 3), 16),
            parseInt(color.slice(3, 5), 16),
            parseInt(color.slice(5, 7), 16),
            1
        ];
    }
    if (color.startsWith('rgba')) {
        return color.substring(5, color.length - 1).split(',').map(s => parseFloat(s.trim()));
    }
    return [10, 10, 10, 0.5]; // Default base color
};

const colorsStrings = ['#5FF7FF', '#40E0D0', '#00CED1', '#20B2AA', '#008B8B'];
const colors = colorsStrings.map(parseColorString);
const baseColor = [10, 10, 10, 0.5];

function init() {
    width = canvas.width = window.innerWidth;
    height = canvas.height = window.innerHeight;
    hexagons = [];
    // Reduce density on smaller screens if we were to run it, but we will skip it.
    if (width < 768) return;

    for (let row = 0; row < numRows; row++) {
        for (let col = 0; col < numCols; col++) {
            const x = col * hexWidth + (row % 2) * (hexWidth / 2);
            const y = row * (hexHeight * 0.75);
            hexagons.push(new Hexagon(x, y));
        }
    }
}

class Hexagon {
    constructor(x, y) {
        this.x = x;
        this.y = y;
        this.size = hexSize;
        this.color = [...baseColor]; // Clone array
        this.targetColor = baseColor;
        this.colorSpeed = 0.05;
    }

    draw() {
        ctx.beginPath();
        for (let i = 0; i < 6; i++) {
            const angle = (Math.PI / 3) * i;
            const x_i = this.x + this.size * Math.cos(angle);
            const y_i = this.y + this.size * Math.sin(angle);
            if (i === 0) {
                ctx.moveTo(x_i, y_i);
            } else {
                ctx.lineTo(x_i, y_i);
            }
        }
        ctx.closePath();
        // Convert array back to string only for drawing
        ctx.fillStyle = `rgba(${Math.round(this.color[0])}, ${Math.round(this.color[1])}, ${Math.round(this.color[2])}, ${this.color[3]})`;
        ctx.fill();
    }

    update() {
        const dx = this.x - mouse.x;
        const dy = this.y - mouse.y;
        const distance = Math.sqrt(dx * dx + dy * dy);

        if (distance < mouse.radius) {
            const index = Math.floor(distance / mouse.radius * colors.length);
            this.targetColor = colors[Math.min(index, colors.length - 1)];
        } else {
            this.targetColor = baseColor;
        }

        // Interpolate colors
        this.color[0] += (this.targetColor[0] - this.color[0]) * this.colorSpeed;
        this.color[1] += (this.targetColor[1] - this.color[1]) * this.colorSpeed;
        this.color[2] += (this.targetColor[2] - this.color[2]) * this.colorSpeed;
        this.color[3] += (this.targetColor[3] - this.color[3]) * this.colorSpeed;

        this.draw();
    }
}

function animate() {
    // Disable animation loop on mobile
    if (window.innerWidth < 768) {
        ctx.clearRect(0, 0, width, height);
        return;
    }

    ctx.clearRect(0, 0, width, height);
    for (const hex of hexagons) {
        hex.update();
    }
    requestAnimationFrame(animate);
}

window.addEventListener('resize', () => {
    init();
    // Restart animation if resizing from mobile to desktop
    if (window.innerWidth >= 768 && hexagons.length === 0) {
        animate();
    }
});

window.addEventListener('mousemove', (event) => {
    mouse.x = event.x;
    mouse.y = event.y;
});

// Check initial size
init();
animate();
