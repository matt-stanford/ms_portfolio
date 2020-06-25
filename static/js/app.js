const scroll = new SmoothScroll('a[href*="#"]', {
    speed: 500
});

const modals = document.querySelectorAll('.modal');
const modalBtns = document.querySelectorAll('#modalBtn');
const closeBtns = document.querySelectorAll('.closeBtn');
let menuBtns = document.querySelectorAll('#menuBtn');
const toggler = document.querySelector('.toggler');

modalBtns.forEach(btn => {
    btn.addEventListener('click', function() {
        let jobId = this.dataset.jobid
        let modal = document.getElementById('jobModal' + jobId);
        modal.style.display = 'block'
    });
});

closeBtns.forEach(btn => {
    btn.addEventListener('click', function() {
        let jobId = this.dataset.jobid
        let modal = document.getElementById('jobModal' + jobId);
        modal.style.display = 'none'
    });
});

modals.forEach(modal => {
    window.addEventListener('click', function(e) {
        if(e.target == modal) {
            modal.style.display = 'none'
        }
    });
});

menuBtns.forEach(btn => {
    btn.addEventListener('click', function() {
        console.log('clicked')
        if (toggler.checked == true) {
            toggler.checked = false;
        } else {
            toggler.checked = true;
        }
    });
});

