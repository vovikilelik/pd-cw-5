const headers = {
    'Accept': 'application/json',
    'Content-Type': 'application/json'
};

function sendAction(data, action) {
    const body = JSON.stringify({ ...data, action });
    return fetch('/fight/action', { method: 'POST', body, headers })
        .then(response => response.ok ? response.json() : Promise.reject(response));
}