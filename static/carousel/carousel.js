// carousel.js
import { lazyload } from './lazyload.js';

export const InstantiateCarousel = () => {
    const carouselElement = document.getElementById('carousel-example');

    const items = [
        { position: 0, el: document.getElementById('carousel-item-1') },
        { position: 1, el: document.getElementById('carousel-item-2') },
        { position: 2, el: document.getElementById('carousel-item-3') },
    ];

    const options = {
        defaultPosition: 0,
        interval: 7000,
        indicators: {
            activeClasses: 'bg-white dark:bg-gray-800',
            inactiveClasses: 'bg-white/50 dark:bg-gray-800/50 hover:bg-white dark:hover:bg-gray-800',
            items: [
                { position: 0, el: document.getElementById('carousel-indicator-1') },
                { position: 1, el: document.getElementById('carousel-indicator-2') },
                { position: 2, el: document.getElementById('carousel-indicator-3') },
            ],
        },
        onNext: () => {},
        onPrev: () => {},
        onChange: () => {},
    };

    const instanceOptions = {
        id: 'carousel-example',
        override: true
    };

    const carousel = new Carousel(carouselElement, items, options, instanceOptions);

    const $prevButton = document.getElementById('data-carousel-prev');
    const $nextButton = document.getElementById('data-carousel-next');

    carousel.cycle();
    $prevButton.addEventListener('click', () => {
        carousel.prev();
        const currentIndex = carousel.getActiveItem().position;
        lazyload(currentIndex);
    });

    $nextButton.addEventListener('click', () => {
        carousel.next();
        const currentIndex = carousel.getActiveItem().position;
        lazyload(currentIndex);
    });

    carousel.updateOnChange(() => {
        const currentIndex = carousel.getActiveItem().position;
        lazyload(currentIndex);
    });
};