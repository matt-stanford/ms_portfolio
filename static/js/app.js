const scroll = new SmoothScroll('a[href*="#"]', {
    speed: 500
});

const modals = document.querySelectorAll('.modal');
const modalBtns = document.querySelectorAll('#modalBtn');
const closeBtns = document.querySelectorAll('.closeBtn');

modalBtns.forEach(btn => {
    btn.addEventListener('click', function() {
        let jobId = this.dataset.jobid
        console.log(jobId)
        let modal = document.getElementById('jobModal' + jobId);
        console.log(modal)
        modal.style.display = 'block'
    });
});

closeBtns.forEach(btn => {
    btn.addEventListener('click', function() {
        let jobId = this.dataset.jobid
        console.log(jobId)
        let modal = document.getElementById('jobModal' + jobId);
        console.log(modal)
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

