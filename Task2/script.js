const board = document.getElementById('board'); 
const status = document.getElementById('status'); 
const restartBtn = document.getElementById('restart');

let cells = Array(9).fill(null); 
let human = 'X'; 
let ai = 'O'; 
let currentPlayer = human; 
let gameOver = false;

function createBoard() { 
  board.innerHTML = ''; 
  cells.forEach((val, idx) => { 
    const cell = document.createElement('div'); 
    cell.classList.add('cell'); 
    cell.dataset.index = idx; 
    cell.textContent = val ? val : ''; 
    cell.addEventListener('click', handleMove); 
    board.appendChild(cell); }); 
  status.textContent = "Your turn (X)"; 
}

function handleMove(e) { 
  const idx = e.target.dataset.index; 
  if (!cells[idx] && !gameOver) { 
    cells[idx] = human; 
    currentPlayer = ai; 
    updateBoard(); 
    if (!checkWin(human) && !checkDraw()) { 
      setTimeout(aiMove, 500); 
    } 
  } 
}

function aiMove() { 
  let bestScore = -Infinity; 
  let move; 
  for (let i = 0; i < cells.length; i++) { 
    if (!cells[i]) { 
      cells[i] = ai; 
      let score = minimax(cells, 0, false); 
      cells[i] = null; 
      if (score > bestScore) { 
        bestScore = score; 
        move = i; 
      } 
    } 
  } 
  cells[move] = ai; 
  currentPlayer = human; 
  updateBoard(); 
  checkWin(ai); 
  checkDraw(); 
}

function minimax(newBoard, depth, isMaximizing) { 
  if (checkWinFor(newBoard, ai)) return 10 - depth; 
  if (checkWinFor(newBoard, human)) return depth - 10; 
  if (newBoard.every(cell => cell)) return 0;

if (isMaximizing) { 
  let best = -Infinity; 
  for (let i = 0; i < newBoard.length; i++) { 
    if (!newBoard[i]) { 
      newBoard[i] = ai; 
      let score = minimax(newBoard, depth + 1, false); 
      newBoard[i] = null; 
      best = Math.max(score, best); 
    } 
  } 
  return best; 
} else { 
  let best = Infinity; 
  for (let i = 0; i < newBoard.length; i++) { 
    if (!newBoard[i]) { 
      newBoard[i] = human; 
      let score = minimax(newBoard, depth + 1, true); 
      newBoard[i] = null; 
      best = Math.min(score, best); 
    } 
  } 
  return best; 
} 
}

function updateBoard() { 
  createBoard(); 
}

function checkWin(player) { 
  const win = checkWinFor(cells, player); 
  if (win) { 
    status.textContent = '${player} wins!'; 
    gameOver = true; 
    return true; 
  } 
  return false; 
}

function checkDraw() { 
  if (cells.every(cell => cell) && !gameOver) { 
    status.textContent = "It's a draw!"; 
    gameOver = true; 
    return true; 
  } 
  return false; 
}

function checkWinFor(board, player) { 
  const winCombos = [ [0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6], [1, 4, 7], [2, 5, 8], [0, 4, 8], [2, 4, 6] ]; 
  return winCombos.some(combo => combo.every(idx => board[idx] === player)); 
}

restartBtn.addEventListener('click', () => { 
  cells = Array(9).fill(null); 
  currentPlayer = human; 
  gameOver = false; 
  createBoard(); 
});

createBoard();
