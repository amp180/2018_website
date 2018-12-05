const GRID_SIZE = 2; 
const PURPLE = `rgba(128, 0, 128, 255)`;
const DARK_PURPLE = `rgba(64, 0, 64, 128)`;
const LINE_WIDTH = 0.25;
const TICK_RATE = 1000/10;


function setCanvasDimensions(canvas) {
    // Set the canvas pixel dimensions to the dimensions of the page.
    canvas.width = window.innerWidth;
    canvas.height = window.innerHeight;
}


function clearCanvas(canvas, ctx) {
    ctx.clearRect(0, 0, canvas.width, canvas.height);
}


function drawGrid(canvas, ctx) {
    // Draw a grid of lines;
    ctx.strokeStyle = PURPLE;
    ctx.fillStyle = PURPLE;
    ctx.lineWidth = LINE_WIDTH;

    for(let i = GRID_SIZE; i<canvas.width; i+=GRID_SIZE) {
       for(let j = GRID_SIZE; j<canvas.height; j+=GRID_SIZE) {
          ctx.beginPath();
          ctx.moveTo(i, 0);
          ctx.lineTo(i, canvas.height);
          ctx.moveTo(0, j);
          ctx.lineTo(canvas.width, j);
          ctx.stroke();
          console.assert(i<10000 && j<10000, "Infinite grid loop?");
       }
    }
}


function fill_grid_box(canvas, ctx, i, j) {
    ctx.strokeStyle = PURPLE;
    ctx.fillStyle = PURPLE;

    ctx.fillRect(GRID_SIZE*i, GRID_SIZE*j, GRID_SIZE, GRID_SIZE);    
}


function start_animate_grid(canvas, ctx, animate_grid){
    let grid_width = Math.floor(canvas.width / GRID_SIZE);
    let grid_height = Math.floor(canvas.height / GRID_SIZE) / 1;
    let i = Math.floor(Math.random() * grid_width);
    let j = Math.floor(Math.random() * grid_height);
    let lives = Math.floor(Math.random() * grid_height);

    return animate_grid(canvas, ctx, animate_grid, i, j, lives-1); 
}


function animate_grid(canvas, ctx, animate_grid, i, j, lives) {
	if(lives<0) { return start_animate_grid(canvas, ctx, animate_grid); };
    if(i*GRID_SIZE>canvas.width){ return start_animate_grid(canvas, ctx, animate_grid); };
    if(j*GRID_SIZE>canvas.height){ return start_animate_grid(canvas, ctx, animate_grid); };

	clearCanvas(canvas, ctx);
    fill_grid_box(canvas, ctx, i, j);
    //drawGrid(canvas, ctx) 

    return setTimeout(function(){ animate_grid(canvas, ctx, animate_grid, i, j+1, lives-1); }, TICK_RATE);
}


function main() {
	const canvas = document.getElementById('background');
    const ctx = canvas.getContext('2d');

    window.addEventListener('resize', function(evt){
        setCanvasDimensions(canvas);
    }); 

    //start_animate_grid(canvas, ctx, animate_grid);
}


load = function(){
    let curronload = window.onload;

    window.onload = function(evt){
        if(curronload) { curronload(evt) };
        main();
    }

}
load();