
function Badge(str,id) {
    let className = `.Item-Card-${id}`;
    let D = document.querySelector(className);
    D.querySelector(".badge.bg-primary").innerHTML = `${str}`;
}


