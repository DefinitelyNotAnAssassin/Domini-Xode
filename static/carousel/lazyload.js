// lazyload.js
export const lazyload = (index) => {
    const lazyImages = document.querySelectorAll('img[carousel-lazy]');
    if (lazyImages[index].dataset.src != undefined) {
        lazyImages[index].src = lazyImages[index].dataset.src;
        lazyImages[index].removeAttribute('data-src');
    }
};