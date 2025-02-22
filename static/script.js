function getUrl() {
  return window.location.href;
}

function onRequestError(response) {
  alert(
    `Error Code: ${response.status}\nError Message: ${response.statusText}\nFrom URL: ${response.url}`
  );
}

function createStatement(text, index, isLie) {
  const statementsBox = document.getElementById("statements");
  const newStatement = document.createElement('div');
  newStatement.setAttribute("class", "statement");
  newStatement.setAttribute("index", index);
  newStatement.setAttribute("isselected", false);
  newStatement.setAttribute("islie", isLie);
  const statementText = document.createElement('div');
  statementText.setAttribute("class", "text");
  statementText.setAttribute("id", "text");
  statementText.textContent = text
  const statementButton = document.createElement('div');
  statementButton.setAttribute("class", "selector button");
  statementButton.setAttribute("onclick", `selectStatementButton(${index})`);
  newStatement.appendChild(statementText);
  newStatement.appendChild(statementButton);
  statementsBox.append(newStatement);
}

async function getRandomPuzzle() {
  let url = `${getUrl()}/puzzle`;
  const res = await fetch(url, {
    method: 'GET',
    credentials: 'include'
  })
  if (res.status >= 300) {
    onRequestError(res);
  }
  const data = await res.json();
  return data;
}

function displayPuzzle(puzzle) {
  const nameBox = document.getElementById('name');
  nameBox.textContent = puzzle.name;
  for (let i = 0, isLie; i < 3; i ++) {
    isLie = (puzzle.lie_index == i);
    createStatement(puzzle.statements[i], i, isLie);
  }
}

function selectStatementButton(index) {
  const statements = document.getElementsByClassName('statement');

  Array.from(statements).forEach(statement => {
    let textDiv = statement.firstChild;
    if (statement.getAttribute("index") == index) {
      statement.setAttribute("isSelected", true)
      textDiv.style.backgroundColor = "#e1b8b8";
    } else {
      statement.setAttribute("isSelected", false)
      textDiv.style.backgroundColor = "white";
    }
  })
  hideUserError();
}

async function load2T1L() {
  const puzzle = await getRandomPuzzle();
  displayPuzzle(puzzle)
}


function displayUserError(message) {
  const errorBox = document.getElementById("error-box");
  errorBox.textContent = message;
  errorBox.style.opacity = 1;
}

function hideUserError() {
  const errorBox = document.getElementById("error-box");
  errorBox.textContent = "";
  errorBox.style.opacity = 0;
}

function getSelectedStatement() {
  const statements = document.getElementsByClassName('statement');
  for (let i = 0, statement; i < 3; i++) {
    statement = statements[i];
    if (statement.getAttribute("isselected") == "true") {
      return statement;
    }
  }
  displayUserError("Please choose a statement you think is a lie!")
  return null;
}

function check() {
  const selectedStatement = getSelectedStatement();
  if (selectedStatement == null) {
    return;
  }
  runSpinner();
  if (selectedStatement.getAttribute("islie")) {

  }
  else {

  }
}

function getLieIndex() {
  const statements = document.getElementsByClassName('statement');
  for (let i = 0, statement; i < 3; i++) {
    statement = statements[i];
    if (statement.getAttribute("islie") == "true") {
      return i;
    }
  }
}

function makeBoxes(boxes) {
  // make the random boxes
  const random_boxes_text = [
    "✅","❌","❌","✅","❌","✅","❌","✅","✅","❌","✅","❌","❌","✅","❌","✅","❌","✅","✅","❌"]
  for (let i = 0; i < 20; i++) {
    let box = document.createElement("div");
    box.classList.add("box");
    box.textContent = random_boxes_text[i];
    boxes.appendChild(box);
  }
  // add final correct boxes
  const lieIndex = getLieIndex();
  for (let i = 0; i < 3; i++) {
    let box = document.createElement("div");
    box.classList.add("box");
    if (i == lieIndex) {
      box.textContent = "❌";
    } else {
      box.textContent = "✅";
    }
    boxes.appendChild(box);
  }
}


function runSpinner() {
  const boxes = document.getElementById("boxes");
  makeBoxes(boxes)
  let boxHeight = 80;
  let numberOfBoxes = boxes.childElementCount;
  boxes.style.transform = `translateY(-${
        boxHeight * (numberOfBoxes - 3)
      }px)`;
}