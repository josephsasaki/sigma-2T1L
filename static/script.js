function getUrl() {
  return window.location.href;
}

function onError(response) {
  alert(
    `Error Code: ${response.status}\nError Message: ${response.statusText}\nFrom URL: ${response.url}`
  );
}


function createStatement(text) {
  const statementsBox = document.getElementById("statements");
  const newStatement = document.createElement('div');
  const statementText = document.createElement('div');
  statementText.textContent = text
  const statementButton = document.createElement('div');
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
    onError(res);
  }
  const data = await res.json();
  return data;
}

function displayPuzzle(puzzle) {
  const nameBox = document.getElementById('name');
  nameBox.textContent = puzzle.name;
  createStatement(puzzle.lie)
  createStatement(puzzle.truth_1)
  createStatement(puzzle.truth_2)
}

async function load2T1L() {
  const puzzle = await getRandomPuzzle();
  displayPuzzle(puzzle)
}

