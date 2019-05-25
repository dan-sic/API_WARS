function formatPopulation(num) {

    if (num === 'unknown') {
        return num;
    }

    const population = String(num);
    let newPopulationStr = '';
    const l = population.length;
    let n = Math.floor(l / 3);
    if (l % 3 === 0) n--;

    for (let i=0; i<l; i++) {
        newPopulationStr += population[i];
        if ((i === (l - (n * 3)) - 1) && i < l - 1) {
            newPopulationStr += ',';
            n--;
        }
    }
    return newPopulationStr;
}

function displayTableBody(data) {
    const tbody = document.querySelector('[data-js="tbody"]');
    const planets = data.results;
    const table = planets.reduce((s, planet, index) => {
        return s + `
            <tr>
                <th scope="row">${index}</th>
                <td>${planet.name}</td>
                <td>${planet.diameter}</td>
                <td>${planet.climate}</td>
                <td>${planet.terrain}</td>
                <td>${planet.surface_water}</td>
                <td>${formatPopulation(planet.population)}</td>
            </tr>
        `
    }, '');

    tbody.innerHTML = '';
    tbody.insertAdjacentHTML('afterbegin', table);
};

function displayNavBUttons(data) {
    const buttonContainer = document.querySelector('[data-js="button-container"]');
    buttonContainer.innerHTML = '';

    const btnPrev = document.createElement('button');
    btnPrev.className = 'btn btn-md btn-primary text-white mr-4';
    if (!data.previous) btnPrev.classList.add('disabled');

    const btnNext = document.createElement('button');
    btnNext.className = 'btn btn-md btn-primary text-white';
    if (!data.next) btnNext.classList.add('disabled');

    btnPrev.addEventListener('click', displayTable.bind(null, data.previous));
    btnPrev.appendChild(document.createTextNode('Previous'));

    btnNext.addEventListener('click', displayTable.bind(null, data.next));
    btnNext.appendChild(document.createTextNode('Next'));

    buttonContainer.insertAdjacentElement('afterbegin', btnPrev);
    buttonContainer.insertAdjacentElement('beforeend', btnNext);

}

function addSpinner() {
    console.log('spinner');
    const body = document.querySelector('body');
    const spinnerHtml = `
      <div class="card-spinner">
        <svg viewBox="0 0 32 32" width="32" height="32">
          <circle cx="16" cy="16" r="14" fill="none"></circle>
        </svg>
      </div>
    `;
    body.insertAdjacentHTML('beforeend', spinnerHtml);
}

function removeSpinner() {
    const body = document.querySelector('body');
    const spinner = document.querySelector('.card-spinner');
    body.removeChild(spinner);
}

function displayTable(url) {
    if (url) {
        addSpinner();
        fetch(url).then(res => res.json()).then(data => {
            removeSpinner();
            displayTableBody(data);
            displayNavBUttons(data);
        })
    }
}

window.addEventListener('DOMContentLoaded', displayTable.bind(null, 'https://swapi.co/api/planets/'));