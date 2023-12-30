let arr2 = document.getElementsByClassName('title');
let arr3 = document.getElementsByClassName('text-secondary');
const searchInput = document.querySelector('[data-search]')
const arr = Array.from(arr2);
const sec = Array.from(arr3);
i = -1
ducks = arr.map(duck => {
    i++
    return { name: duck.innerText, type: sec[i].innerText, par: duck.offsetParent.parentElement }
})
console.log(ducks);
searchInput.addEventListener("input", e => {
    const value = e.target.value.toLowerCase()
    ducks.forEach(duck => {
        const isVis = duck.name.toLowerCase().includes(value) || duck.type.toLowerCase().includes(value)
        duck.par.classList.toggle("hide", !isVis)
    })
})
/*
for(let i = 0; i<arr.length; i++){
    console.log(arr[i].innerText);
}*/

