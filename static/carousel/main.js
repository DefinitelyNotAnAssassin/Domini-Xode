// main.js
import { InstantiateCarousel } from './carousel.js';


const loadScripts = (url, callback) => { 
    const script = document.createElement('script');
    script.type = 'text/javascript';
    script.src = url;
    script.onload = callback;
    document.body.appendChild(script);

}

const loadStyles = (url, callback) => {
    const link = document.createElement('link');
    link.rel = 'stylesheet';
    link.href = url;
    link.onload = callback;
    document.head.appendChild(link);
}


loadStyles('https://cdn.jsdelivr.net/npm/flowbite@2.5.1/dist/flowbite.min.css', () => {
});



loadScripts('https://cdn.jsdelivr.net/npm/flowbite@2.5.1/dist/flowbite.min.js', () => {
    InstantiateCarousel();

    htmx.onLoad(() => {
        if (document.getElementById('carousel-example')) {
            InstantiateCarousel();
        }
    });
});


