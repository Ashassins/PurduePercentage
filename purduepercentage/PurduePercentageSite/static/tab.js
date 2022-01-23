// alert("Tab.js is running POGGIES");
// var triggerTabList = [].slice.call(document.querySelectorAll('#examTabs button'))
// triggerTabList.forEach(function (triggerEl) {
//     var tabTrigger = new bootstrap.Tab(triggerEl)

//     console.log("triggerEl");
//     triggerEl.addEventListener('click', function (event) {
//     event.preventDefault()
//     tabTrigger.show()
//     console.log("click");
//     })
// })

// var firstTabEl = document.querySelector('#examTabs li:last-child button')
// var firstTab = new bootstrap.Tab(firstTabEl)

// firstTab.show()

// $('#scatter-tab').on('click', selector, func) {

// }

console.log("js");
//$(document).ready(function() {
    $("#scatter-tab").click(function(e){
        e.preventDefault();
        $(this).tab("show");
        $("#scatter").display("show");
        console.log("click");
    });
// });