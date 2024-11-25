/* change the image */
function updateIframes(htmlUrl, cssUrl, renderedUrl, clickedLink) {
    // update the iframes
    document.getElementById('iframe-html').src = htmlUrl;
    document.getElementById('iframe-css').src = cssUrl;
    document.getElementById('iframe-site').src = renderedUrl;

    // remove active class from previous link
    const links = document.querySelectorAll('.assign-link');
    links.forEach(link => link.classList.remove('active'));

    // add active class to the clicked link
    clickedLink.classList.add('active');
}

function updatePythonIframes(pythonUrl, programUrl, clickedLink) {
    // update the iframes
    document.getElementById('iframe-python').src = pythonUrl;
    document.getElementById('iframe-program').src = programUrl;

    // remove active class from previous link
    const links = document.querySelectorAll('.assign-link');
    links.forEach(link => link.classList.remove('active'));

    // add active class to the clicked link
    clickedLink.classList.add('active');
}