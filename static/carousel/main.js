// main.js
import { InstantiateCarousel } from './carousel.js';

document.addEventListener('DOMContentLoaded', () => {
    InstantiateCarousel();
});

htmx.onLoad(() => {
    if (document.getElementById('carousel-example')) {
        InstantiateCarousel();
    }
});