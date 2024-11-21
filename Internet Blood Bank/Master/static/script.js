document.getElementById('dataForm').onsubmit = async function(event) {
    event.preventDefault();

    const formData = new FormData(this);

    const response = await fetch('/submit', {
        method: 'POST',
        body: formData
    });

    const data = await response.json();
    document.getElementById('result').innerHTML = `<pre>${JSON.stringify(data, null, 2)}</pre>`;
}
