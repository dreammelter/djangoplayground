/* honestly the stuff in here should be minimal but w/e

==========TO DO LIST=============
    1. simple off-screen menu for special actions and such - DONE
*/

//get elements
const menubutton = document.querySelector('.toggle-btn');
const extramenu = document.querySelector('.extra-menu');

//have menu button show the extra menu when clicked
menubutton.addEventListener('click', ()=>
    extramenu.classList.toggle('show'));