// frontend/script.js

const rows = 10, cols = 10;
let grid = [];
let start = null;
let end = null;

const container = document.getElementById('grid-container');

function initGrid() {
  container.innerHTML = '';
  grid = [];

  for (let i = 0; i < rows; i++) {
    const row = [];
    for (let j = 0; j < cols; j++) {
      const cell = document.createElement('div');
      cell.className = 'cell';
      cell.dataset.row = i;
      cell.dataset.col = j;
      cell.onclick = () => handleCellClick(cell, i, j);
      container.appendChild(cell);
      row.push(0);
    }
    grid.push(row);
  }
}

function handleCellClick(cell, i, j) {
  if (!start) {
    start = [i, j];
    cell.classList.add('start');
  } else if (!end) {
    end = [i, j];
    cell.classList.add('end');
  } else {
    if (!cell.classList.contains('obstacle')) {
      cell.classList.add('obstacle');
      grid[i][j] = 1;
    }
  }
}

async function findPath() {
  if (!start || !end) {
    alert("Please set both start and end points.");
    return;
  }

  try {
    const response = await fetch('http://127.0.0.1:5000/find-path', {
      method: 'POST',
      mode: 'cors',
      headers: {
        'Content-Type': 'application/json'
      },
      body: JSON.stringify({ grid, start, end })
    });

    if (!response.ok) {
      const err = await response.text();
      throw new Error(`Server error: ${response.status} - ${err}`);
    }

    const data = await response.json();
    drawPath(data.path);
  } catch (err) {
    console.error("Error:", err);
    alert("Something went wrong: " + err.message);
  }
}

function drawPath(path) {
  path.forEach(([i, j]) => {
    const index = i * cols + j;
    const cell = container.children[index];
    if (!cell.classList.contains('start') && !cell.classList.contains('end')) {
      cell.classList.add('path');
    }
  });
}

function resetGrid() {
  start = null;
  end = null;
  initGrid();
}

initGrid();
