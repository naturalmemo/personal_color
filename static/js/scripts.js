window.onload = function() {
    const spinner = document.getElementById('loading');
    spinner.classList.add('loaded');
}

$(document).ready(function(){
    $('.slider').bxSlider({
        auto: true,
        pause: 5000,
        
    });
});
