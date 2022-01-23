// var homepageCarousel = document.getElementById('homepageCarousel')

var myCarousel = document.querySelector('#homepageCarousel')
var homepageCarousel = new bootstrap.Carousel(myCarousel, {
    interval: 10,
    wrap: false
})