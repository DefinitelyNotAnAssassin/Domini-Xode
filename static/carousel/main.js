// main.js
import { InstantiateCarousel } from './carousel.js';


const loadScripts = (url, callback) => { 
    const script = document.createElement('script');
    script.type = 'text/javascript';
    script.src = url;
    script.onload = callback;
    document.body.appendChild(script);

}


loadScripts('https://cdn.jsdelivr.net/npm/flowbite@2.5.1/dist/flowbite.min.js', () => {
    InstantiateCarousel();
});