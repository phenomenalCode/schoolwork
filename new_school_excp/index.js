    const menuButton = document.getElementById('menu-btn');
    const menuContainer = document.getElementById('menu-container');
    const muayThai = document.getElementById("muay-thai")
    const bjj = document.getElementById("bjj")
    const wrestling = document.getElementById("wrestling")
    const boxing = document.getElementById("boxing")
    const mma = document.getElementById("mma")
 function handleMenuClick(sectionId) {
        const section = document.getElementById(sectionId); // Get the section by ID
        if (section) {
            // Scroll to sec using built ins to the section via geeksforgeeks
            section.scrollIntoView({ behavior: 'smooth' });
        }
    }document.addEventListener('DOMContentLoaded', () => {
  

    menuButton.addEventListener('click', function () {
        // active/hidecontainer
        menuContainer.classList.toggle('active');

        // Fill container 
        if (!menuContainer.innerHTML.trim()) {
            const menu = `
            <button onclick="handleMenuClick('section')">home</button>
                <button onclick="handleMenuClick('about')">about</button>
                <button onclick="handleMenuClick('contact')">contact</button>
                <button onclick="handleMenuClick('muay-thai')">Muay Thai</button>
                <button onclick="handleMenuClick('bjj')">BJJ</button>
                <button onclick="handleMenuClick('boxing')">Boxning</button>
                <button onclick="handleMenuClick('mma')">MMA</button>`
                
            menuContainer.innerHTML = menu;
        }
    });
   
    window.addEventListener('click', function(e) {
        if (!menuButton.contains(e.target) && !menuContainer.contains(e.target)) {
            menuContainer.classList.remove('active');
        }
    });
});