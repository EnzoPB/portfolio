class Particles {
    constructor(canvas) {
        this.maxSpeed = 5;
        this.minRadius = 120;
        this.maxRadius = 200;

        this.canvas = canvas;
        this.ctx = this.canvas.getContext('2d');
        this.radius = Math.floor(Math.random() * this.maxRadius) + this.minRadius;

        this.x = Math.floor(Math.random() * canvas.width);
        this.y = Math.floor(Math.random() * canvas.height);

        this.speedX = Math.floor(Math.random() * 10) - 5;
        this.speedY = Math.floor(Math.random() * 10) - 5;
    }

    update() {
        ctx.fillStyle = window.getComputedStyle(canvas).color;
        // change the speed
        this.speedX += Math.floor(Math.random() * 3) - 1;
        this.speedY += Math.floor(Math.random() * 3) - 1;

        if (this.speedX > this.maxSpeed) {
            this.speedX = this.maxSpeed;
        }
        if (this.speedX < -this.maxSpeed) {
            this.speedX = -this.maxSpeed;
        }

        if (this.speedY > this.maxSpeed) {
            this.speedY = this.maxSpeed;
        }
        if (this.speedY < -this.maxSpeed) {
            this.speedY = -this.maxSpeed;
        }

        this.x += this.speedX;
        this.y += this.speedY;

        if (this.x > this.canvas.width) {
            this.speedX = -3;
            this.x = this.canvas.width;
        }
        if (this.x < 0) {
            this.speedX = 3;
            this.x = 0;
        }

        if (this.y > this.canvas.height) {
            this.speedY = -3;
            this.y = this.canvas.height;
        }
        if (this.y < 0) {
            this.speedY = 3;
            this.y = 0;
        }

        this.ctx.beginPath();
        this.ctx.arc(this.x, this.y, this.radius, 0, Math.PI * 2);
        this.ctx.fill();
    }
}

var particles = [];
var canvas;
var ctx;
function init() {
    canvas = document.getElementById('particles');
    ctx = canvas.getContext('2d');
    resetSize();
    window.requestAnimationFrame(draw);
    for (let i = 0; i < 10; i++) {
        particles.push(new Particles(canvas));
    }
}

function draw() {
    ctx.clearRect(0, 0, canvas.width, canvas.height);

    for (const particle of particles) {
        particle.update();
    }

    setTimeout(() => window.requestAnimationFrame(draw), 20);
}

window.addEventListener('resize', resetSize);
function resetSize() {
    canvas.width = canvas.offsetWidth;
    canvas.height = canvas.offsetHeight;
}

document.addEventListener('DOMContentLoaded', init);