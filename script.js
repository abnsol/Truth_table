let btn = document.querySelector('.btn');

btn.addEventListener('click', function() {
    var collapsable = document.getElementById('collapsable');
    if (collapsable.classList.contains('expanded')) {
        collapsable.classList.remove('expanded');
    } else {
        collapsable.classList.add('expanded');
    }
});
