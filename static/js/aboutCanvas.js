document.addEventListener('DOMContentLoaded', function() {
    var canvas = document.getElementById('teamCanvas');
    var ctx = canvas.getContext('2d');

    ctx.fillStyle = 'skyblue';
    ctx.fillRect(10, 10, 780, 380);
    ctx.font = '20px Arial';
    ctx.fillStyle = 'black';
    ctx.fillText('Meet Our Team!', 300, 50);

    // You can dynamically draw more elements here based on your team's data
});
